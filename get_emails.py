from selenium.webdriver.common.by import By
from datetime import datetime
import time

from utils import inicialize_driver, login, roll_page_down, initialize_spreadsheets, get_leads_data_from_spreadsheets

should_get_emails = 20

def get_leads(driver):
    leads_list = driver.find_element_by_class_name('search-results__result-list')
    leads = leads_list.find_elements_by_class_name('search-results__result-item')
    time.sleep(5)
    return leads

def get_lead_name(lead):
    lead_name = lead.find_element_by_tag_name('dt').find_element_by_tag_name('a')
    return lead_name.text

def open_message_section(lead):
    message_button = lead.find_element_by_class_name('artdeco-button')
    message_button.click()
    time.sleep(2)

def get_contact_list(driver):
    contact_section = driver.find_elements_by_class_name('conversation-insights__section')
    contact_list = contact_section[1].find_elements_by_tag_name('li')
    return contact_list

def add_leads_data(lead_name, contact_value, leads_data):
    current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    name = lead_name
    email = contact_value.replace('mailto:', '')
    was_email_sended = False
    email_sended_at = ''
    data = [current_date, name, email, was_email_sended, email_sended_at]
    leads_data.append(data)

def close_message_section(driver):
    exit_button = driver.find_element(By.XPATH, "/html/body/div[2]/section/header/button[2]")
    exit_button.click()
    time.sleep(3)

def go_to_next_page(driver):
    next_button = driver.find_element_by_class_name('search-results__pagination-next-button')
    next_button.click()
    time.sleep(10)

def filter_existing_data(leads_data, csv_dataframe):
    filtered_data = []

    for lead in leads_data:
        lead_email = lead[2]

        exists = False
        for email in csv_dataframe.email:
            if lead_email == email:
                exists = True
                break

        if not exists:
            filtered_data.append(lead)

    return filtered_data

def add_leads_data_to_spreadsheets(leads_data):
    csv_dataframe = get_leads_data_from_spreadsheets()
    filtered_data = filter_existing_data(leads_data, csv_dataframe)
    sheet_instance = initialize_spreadsheets()
    sheet_instance.append_rows(filtered_data)

driver = inicialize_driver()

login(driver)

driver.get('https://www.linkedin.com/sales/search/people/list/saved-leads')
time.sleep(10)

try:
    while True:
        leads = get_leads(driver)
        leads_data = []

        page_down_counter = 0
        for lead in leads:
            if page_down_counter == 2:
                roll_page_down(driver)
                page_down_counter = 0

            try:
                lead_name = get_lead_name(lead)
                open_message_section(lead)

                contact_list = get_contact_list(driver)

                for contact in contact_list:
                    contact_value = contact.find_element_by_tag_name('a').get_attribute('href')
                    is_contact_email = 'mailto:' in contact_value

                    if is_contact_email:
                        add_leads_data(lead_name, contact_value, leads_data)
                        print('success!!')
                        break
                        
                close_message_section(driver)

            except:
                print('fail!!')

            page_down_counter += 1
            print(leads_data)


        add_leads_data_to_spreadsheets(leads_data)
        go_to_next_page(driver)
except:
    print("Finished")