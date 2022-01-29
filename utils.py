from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from decouple import config

from oauth2client.service_account import ServiceAccountCredentials

import pandas as pd
import gspread
import time



def inicialize_driver():
    driver = webdriver.Firefox()
    driver.get('https://www.linkedin.com/login')
    time.sleep(2)
    return driver

def insert_username(driver):
    USERNAME = config('LINKEDIN_USERNAME')
    username = driver.find_element(By.XPATH, "//input[@name='session_key']")
    username.send_keys(USERNAME)

def insert_password(driver):
    PASSWORD = config('LINKEDIN_PASSWORD')
    password = driver.find_element(By.XPATH, "//input[@name='session_password']")
    password.send_keys(PASSWORD + Keys.ENTER)

def login(driver):
    insert_username(driver)
    insert_password(driver)
    time.sleep(5)

def roll_page_down(driver):
    body = driver.find_element_by_css_selector('body')
    body.send_keys(Keys.PAGE_DOWN)

def initialize_spreadsheets():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('linkedin-bots-0a9b8a844a62.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('Foremind - Leads')
    return sheet.get_worksheet(0)

def get_leads_data_from_spreadsheets():
    sheet_instance = initialize_spreadsheets()
    records_data = sheet_instance.get_all_records()
    records_df = pd.DataFrame.from_dict(records_data)
    return records_df