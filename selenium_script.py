import argparse
import time
import json

from cryptography.fernet import Fernet

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

parser = argparse.ArgumentParser() 
parser.add_argument('-k', '--key', type=str)

args = parser.parse_args()

# Set up the WebDriver
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


# Find the username and password fields and enter your credentials
login_button = driver.find_element(By.ID, 'loginLinkBtn')
login_button.click()

# Wait until imss button shows up
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.btn.btn-primary.btn-block.btn-external-login.btn-sign-in.btn-sso-shibboleth'))  # Replace with an element that appears after login
    )
    print("Located login button")
except:
    print("No login button")

imss_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary.btn-block.btn-external-login.btn-sign-in.btn-sso-shibboleth')
imss_button.click()

with open('credentials.json', 'r') as f:
    data = json.load(f)
    username = data['username']
    encrypted_password = data['password']

decrypt_key = args.key
cipher = Fernet(decrypt_key)
password = cipher.decrypt(encrypted_password).decode()

username_field = driver.find_element(By.ID, 'username')  # Replace with the actual name attribute of the username field
password_field = driver.find_element(By.ID, 'password')  # Replace with the actual name attribute of the password field

username_field.send_keys(username)  # Replace with your actual username
password_field.send_keys(password)  # Replace with your actual password

# Submit the login form
password_field.send_keys(Keys.RETURN)

# Wait for some time to ensure the login is successful
time.sleep(2)
print(driver.title)

cookie_list = driver.get_cookies();
shibsession_field = ''
for cookie in cookie_list:
    if 'shibsession' in cookie['name']:
        shibsession_field = cookie['name']
cookie_fields = ['ASP.NET_SessionId', '__RequestVerificationToken', shibsession_field, '.AspNet.ApplicationCookie']
cookies = {}
for cookie in cookie_list:
    cookies[cookie['name']] = cookie['value']

cookie_string = ""
for key in cookie_fields:
    val = cookies[key]
    cookie_string += f"{key}={val}; "
cookie_string += "cookieControl=true; cookieControlPrefs=[]"

with open('./cookie', 'w') as f:
    f.write(cookie_string)

# Close the browser
driver.quit()
