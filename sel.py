import argparse
import calendar
import time
import json

from cryptography.fernet import Fernet
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pyvirtualdisplay.display import Display

# Get current date to set as default booking date
current_date = datetime.now()
future_date = current_date + timedelta(days=2)

parser = argparse.ArgumentParser() 
parser = argparse.ArgumentParser(
        prog='Caltech Tennis Court Booker',
        description='Books a tennis court from 5-7 given a date'
        )
parser.add_argument('-k', '--key', type=str)
parser.add_argument('-y', '--year', type=str, default=future_date.year)
parser.add_argument('-m', '--month', type=str, default=future_date.month)
parser.add_argument('-d', '--day', type=str, default=future_date.day)

args = parser.parse_args()

formatted_date = f"{args.month}/{args.day}/{args.year}"
if args.month < 1 or args.month > 12 or args.day < 1 or args.day > 31:
    raise Exception('Invalid date:', formatted_date)

print("Booking court for", formatted_date)

# Set up the WebDriver
display = Display(visible=False, size=(1080, 1920))  
display.start()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the login page
driver.get('https://rec.caltech.edu/booking') 

# Wait until login button shows up
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'loginLinkBtn'))  # Replace with an element that appears after login
    )
    print("Located login button")
except:
    print("No login button")

# Find the username and password fields and enter credentials
login_button = driver.find_element(By.ID, 'loginLinkBtn')
login_button.click()

# Wait until imss button shows up
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.btn.btn-primary.btn-block.btn-external-login.btn-sign-in.btn-sso-shibboleth'))
    )
    print("Located IMSS credentials button")
except:
    print("No IMSS credentials button")

imss_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary.btn-block.btn-external-login.btn-sign-in.btn-sso-shibboleth')
imss_button.click()

# Get username and encrypted password
with open('credentials.json', 'r') as f:
    data = json.load(f)
    username = data['username']
    encrypted_password = data['password']

# Decrypt password
decrypt_key = args.key
cipher = Fernet(decrypt_key)
password = cipher.decrypt(encrypted_password).decode()

# Log in
username_field = driver.find_element(By.ID, 'username') 
password_field = driver.find_element(By.ID, 'password')
username_field.send_keys(username) 
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

# Wait for some time to ensure the login is successful
time.sleep(1)

# Go to tennis court booking site
driver.get('https://rec.caltech.edu/booking/f20965ff-b976-4e7d-9ad5-f7759b823407')

# Wait until booking date appears
date_text = str(calendar.month_name[args.month][:3]) + ' ' + str(args.day)
print(date_text)
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, f"//p[contains(text(), '{date_text}')]/ancestor::button"))
    )
    print("Located tab for", formatted_date)
    date_button = driver.find_element(By.XPATH, f"//p[contains(text(), '{date_text}')]/ancestor::button")
    date_button.click()
except:
    print('Unable to find tab for', formatted_date)

with open('page.html', 'w', encoding='utf-8') as file:
    page_source = driver.page_source
    file.write(page_source)

timeslots = ['5 - 6 PM', '6 - 7 PM']
for court in range(1, 7):
    court_text = f"Tennis Court #{court}"
    print('Checking', court_text)
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//button[contains(@class, 'text-primary') and .//span[contains(text(), '{court_text}')]]"))
        )
    except TimeoutException:
        print('Could not find tab for', court_text)
        continue

    button = driver.find_element(By.XPATH, f"//button[contains(@class, 'text-primary') and .//span[contains(text(), '{court_text}')]]")
    button.click()
    time.sleep(0.5)

    for t in timeslots:
        try:
            xpath = f"//button[@data-slot-text='{t}' and contains(text(), 'Book Now')]"
            button = driver.find_element(By.XPATH, xpath)
            button.click()
            print('Booked', court_text, 'for', t)
            timeslots.remove(t)
        except:
            continue

# Close the browser
driver.quit()
