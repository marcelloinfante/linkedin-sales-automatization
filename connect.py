from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

leads_urls = 'https://www.linkedin.com/sales/search/people?page=4&query=(filters%3AList((type%3ASENIORITY_LEVEL%2Cvalues%3AList((id%3A10%2Ctext%3AOwner%2CselectionType%3AINCLUDED)%2C(id%3A8%2Ctext%3ACXO%2CselectionType%3AINCLUDED)%2C(id%3A9%2Ctext%3APartner%2CselectionType%3AINCLUDED)))%2C(type%3ACOMPANY_HEADCOUNT%2Cvalues%3AList((id%3AB%2Ctext%3A1-10%2CselectionType%3AINCLUDED)%2C(id%3AC%2Ctext%3A11-50%2CselectionType%3AINCLUDED)%2C(id%3AD%2Ctext%3A51-200%2CselectionType%3AINCLUDED)))%2C(type%3AINDUSTRY%2Cvalues%3AList((id%3A96%2Ctext%3AInformation%2520Technology%2520and%2520Services%2CselectionType%3AINCLUDED)))%2C(type%3AREGION%2Cvalues%3AList((id%3A106057199%2Ctext%3ABrazil%2CselectionType%3AINCLUDED)))))&savedSearchId=50526514&sessionId=DctHq%2FppSxCMPUkwcpAcKg%3D%3D'
should_connect = 20

driver = webdriver.Firefox()
driver.get('https://www.linkedin.com/login')

time.sleep(2)
    
username = driver.find_element(By.XPATH, "//input[@name='session_key']")
username.send_keys('contato@marcelloinfante.com.br')

password = driver.find_element(By.XPATH, "//input[@name='session_password']")
password.send_keys('s!u+X8$?8HUwc!*' + Keys.ENTER)

time.sleep(5)

driver.get(leads_urls)

time.sleep(10)
    
connect_success = 0
connect_fail = 0

while connect_success < should_connect:
    leads_list = driver.find_element_by_class_name('artdeco-list')
    leads = leads_list.find_elements_by_class_name('artdeco-list__item')

    time.sleep(10)

    page_down_counter = 0
    for lead in leads:
        if page_down_counter == 4:
            body = driver.find_element_by_css_selector('body')
            body.send_keys(Keys.PAGE_DOWN)
            page_down_counter = 0

        if connect_success < should_connect:
            time.sleep(3)
            try:
                dropdown_button = lead.find_element_by_class_name('artdeco-dropdown__trigger')
                dropdown_button.click()

                connect_button = lead.find_element_by_xpath("//*[ text() = 'Connect' ]")
                connect_button.click()

                send_invitation = driver.find_element_by_xpath("//*[ text() = 'Send Invitation' ]")
                send_invitation.click()

                connect_success += 1
                print('success!!')
            except:
                connect_fail += 1
                print('fail!!')
            page_down_counter += 1

    if connect_success < should_connect:
        next_button = driver.find_element_by_class_name('artdeco-pagination__button--next')
        next_button.click()
        time.sleep(10)

print('sucess: ' + str(connect_success))
print('fail: ' + str(connect_fail))


# driver.quit()