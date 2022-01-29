from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from utils import inicialize_driver, login, roll_page_down

leads_urls = 'https://www.linkedin.com/sales/search/people?page=4&query=(filters%3AList((type%3ASENIORITY_LEVEL%2Cvalues%3AList((id%3A10%2Ctext%3AOwner%2CselectionType%3AINCLUDED)%2C(id%3A8%2Ctext%3ACXO%2CselectionType%3AINCLUDED)%2C(id%3A9%2Ctext%3APartner%2CselectionType%3AINCLUDED)))%2C(type%3ACOMPANY_HEADCOUNT%2Cvalues%3AList((id%3AB%2Ctext%3A1-10%2CselectionType%3AINCLUDED)%2C(id%3AC%2Ctext%3A11-50%2CselectionType%3AINCLUDED)%2C(id%3AD%2Ctext%3A51-200%2CselectionType%3AINCLUDED)))%2C(type%3AINDUSTRY%2Cvalues%3AList((id%3A96%2Ctext%3AInformation%2520Technology%2520and%2520Services%2CselectionType%3AINCLUDED)))%2C(type%3AREGION%2Cvalues%3AList((id%3A106057199%2Ctext%3ABrazil%2CselectionType%3AINCLUDED)))))&savedSearchId=50526514&sessionId=DctHq%2FppSxCMPUkwcpAcKg%3D%3D'
should_connect = 100

def get_leads(driver):
    leads_list = driver.find_element_by_class_name("artdeco-list")
    leads = leads_list.find_elements_by_class_name("artdeco-list__item")
    return leads

def click_dropdown_button(lead):
    dropdown_button = lead.find_element_by_class_name("artdeco-dropdown__trigger")
    dropdown_button.click()

def click_connect_button(lead):
    connect_button = lead.find_element_by_xpath("//*[ text() = 'Connect' ]")
    connect_button.click()

def click_send_invitation(driver):
    send_invitation = driver.find_element_by_xpath("//*[ text() = 'Send Invitation' ]")
    send_invitation.click()

def click_warning_button(driver):
    warning_button = driver.find_element_by_xpath("//*[ text() = 'Got it' ]")
    print(warning_button)
    warning_button.click()

def click_close_modal(driver):
    close_modal = driver.find_element_by_xpath('//*[@id="ember1397"]/li-icon/svg')
    close_modal.click()

def click_next_button(driver):
    next_button = driver.find_element_by_class_name('artdeco-pagination__button--next')
    next_button.click()

driver = inicialize_driver()

login(driver)

driver.get(leads_urls)

time.sleep(10)

connect_success = 0
connect_fail = 0

should_continue = connect_success < should_connect

while should_continue:
    leads = get_leads(driver)

    time.sleep(5)

    page_down_counter = 0
    for lead in leads:
        if page_down_counter == 2:
            roll_page_down(driver)
            page_down_counter = 0

        if should_continue:
            time.sleep(3)

            try:
                click_dropdown_button(lead)

                click_connect_button(lead)

                click_send_invitation(driver)

                try:
                    time.sleep(2)
                    click_warning_button(driver)
                except:
                    pass

                try:
                    is_email_required = driver.find_element_by_xpath('//*[@id="connect-cta-form__email]')

                    click_close_modal(driver)
                except:
                    pass


                connect_success += 1
                print('success!!')
            except:
                connect_fail += 1
                print('fail!!')
            page_down_counter += 1

    if should_continue:
        click_next_button(driver)
        time.sleep(10)

print('sucess: ' + str(connect_success))
print('fail: ' + str(connect_fail))

driver.quit()