from datetime import date
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
from bs4 import BeautifulSoup
import time
import pandas as pd

date_string = pd.to_datetime('today').date().strftime('%m_%d_%Y')
chromedriver_location = "./chromedriver"

# Initiailze Web Page
options = Options()
options.headless = True
driver = webdriver.Chrome(chromedriver_location, options=options)
driver.set_window_size(1920, 1080)
driver.get('https://www.placeholder.com')

# Selectors for Automated Browser Actions
client_login_link = '//*[@id="comp-k9wyuvo1"]/h5/a'
email_input = 'input_input_emailInput_SM_ROOT_COMP1'
password_input = '//*[@id="input_input_passwordInput_SM_ROOT_COMP1"]'
login_button = '//*[@id="okButton_SM_ROOT_COMP1"]/button'

# Automated Browser Actions
driver.find_element_by_xpath(client_login_link).click()
driver.implicitly_wait(5)
driver.find_element_by_id(email_input).send_keys("email-placeholder")
driver.find_element_by_xpath(password_input).send_keys("password-placeholder")
driver.find_element_by_xpath(login_button).click()

# Javascript Rendering
time.sleep(5)
data = driver.page_source

# Parsing Source for CSV Path
parsed = BeautifulSoup(data, 'html.parser')
date_string = pd.to_datetime('today').date().strftime('%m_%d_%Y')
link = parsed.find('a', href=re.compile(date_string))
path = link['href']
df = pd.read_csv(path)

print(df)