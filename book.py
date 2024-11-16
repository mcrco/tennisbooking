import argparse
import calendar
import time
import json
import os

from cryptography.fernet import Fernet
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from tqdm import tqdm
import logging

# Get current date to set as default booking date
current_date = datetime.now()
future_date = current_date + timedelta(days=2)

parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(
    prog="Caltech Tennis Court Booker",
    description="Books a tennis court from given a date and time slot. \
        Defaults to booking a court 2 days in advance from 4-5 PM.",
)
parser.add_argument("-k", "--key", type=str)
parser.add_argument("-y", "--year", type=str, default=future_date.year)
parser.add_argument("-m", "--month", type=str, default=future_date.month)
parser.add_argument("-d", "--day", type=str, default=future_date.day)
parser.add_argument("-t", "--time", type=str, default="4 - 5 PM")

args = parser.parse_args()

formatted_date = f"{args.month}/{args.day}/{args.year}"
if args.month < 1 or args.month > 12 or args.day < 1 or args.day > 31:
    raise Exception("Invalid date:", formatted_date)

timeslot = str(args.time)

script_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(script_dir, "log")
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

timestamp = datetime.now().strftime("%Y%m%d%_H%M%S")
log_file = f"{timestamp}.log"
log_path = os.path.join(log_dir, log_file)
logger = logging.getLogger(__name__)
logging.basicConfig(filename=log_path, encoding="utf-8", level=logging.DEBUG)

logging.info(f"Booking court for {formatted_date} at {timeslot}")

# Set up the WebDriver
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

# Open the login page
driver.get("https://rec.caltech.edu/booking")

# Wait until login button shows up
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.ID, "loginLinkBtn")
        )  # Replace with an element that appears after login
    )
    logging.info("Located login button.")
except:
    logging.error("No login button.")

# Find the username and password fields and enter credentials
login_button = driver.find_element(By.ID, "loginLinkBtn")
login_button.click()

# Wait until imss button shows up
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                ".btn.btn-primary.btn-block.btn-external-login.btn-sign-in.btn-sso-shibboleth",
            )
        )
    )
    logging.info("Located IMSS credentials button.")
except:
    logging.error("No IMSS credentials button.")

imss_button = driver.find_element(
    By.CSS_SELECTOR,
    ".btn.btn-primary.btn-block.btn-external-login.btn-sign-in.btn-sso-shibboleth",
)

imss_button.click()

try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    logging.info("Loaded Shibboleth login page.")
except:
    logging.error("Shibboleth login page took too long to load.")

# Get username and encrypted password
with open("credentials.json", "r") as f:
    data = json.load(f)
    username = data["username"]
    encrypted_password = data["password"]

# Decrypt password
decrypt_key = args.key
cipher = Fernet(decrypt_key)
password = cipher.decrypt(encrypted_password).decode()

# Log in
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
username_field.send_keys(username)
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

# Wait for some time to ensure the login is successful
time.sleep(1)

# Go to tennis court booking site
driver.get("https://rec.caltech.edu/booking/f20965ff-b976-4e7d-9ad5-f7759b823407")

# Wait until booking date appears
date_text = str(calendar.month_name[args.month][:3]) + " " + str(args.day)
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, f"//p[contains(text(), '{date_text}')]/ancestor::button")
        )
    )
    logging.info(f"Located tab for {formatted_date}")
    date_button = driver.find_element(
        By.XPATH, f"//p[contains(text(), '{date_text}')]/ancestor::button"
    )
    date_button.click()
except:
    logging.error(f"Unable to find tab for {formatted_date}")

courts = [6, 4, 3, 1, 2]
result = None
print("Checking courts...")
for court in tqdm(courts):
    court_text = f"Tennis Court #{court}"
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f"//button[contains(@class, 'text-primary') and .//span[contains(text(), '{court_text}')]]",
                )
            )
        )
    except TimeoutException:
        print("Could not find tab for", court_text)
        continue

    button = driver.find_element(
        By.XPATH,
        f"//button[contains(@class, 'text-primary') and .//span[contains(text(), '{court_text}')]]",
    )
    button.click()
    time.sleep(0.5)

    try:
        xpath = (
            f"//button[@data-slot-text='{timeslot}' and contains(text(), 'Book Now')]"
        )
        button = driver.find_element(By.XPATH, xpath)
        button.click()

        result = f"Booked {court_text} for {timeslot}"
    except:
        continue

if result is not None:
    print(result)
    logging.info(result)
print(f"Unable to find court for {timeslot} on {formatted_date}")
logging.error(f"Unable to find court for {timeslot} on {formatted_date}")


# Close the browser
driver.quit()
