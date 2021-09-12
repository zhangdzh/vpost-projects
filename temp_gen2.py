# div class service-row
# div id stateDelegate and stateSenator
# div class service-name
# format name into last, first m.
# dels here: https://virginiageneralassembly.gov/house/members/members.php
# look up by name, get email

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome('/Users/dorot/Downloads/chromedriver.exe')
driver.get("https://whosmy.virginiageneralassembly.gov/index.php")
# time.sleep(2)

# try searching?
st_add = input("Please enter your street address: ")
city = input("Please enter your city: ")

search = driver.find_element_by_id('addressSearchInput')
WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located)
# WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'index-banner')))
search.send_keys("{}, {}, VA, USA".format(st_add, city))
button = driver.find_element_by_id('findBtn')
button.click()
driver.maximize_window()
'''
# val = driver.find_element_by_xpath('//div[@id="stateDelegate"]/div[@class="service-name"]')
# val = driver.find_element_by_id('stateDelegate')
# val = driver.find_elements_by_link_text("Email")

# val = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'stateDelegate')))
WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located)
val = driver.find_element_by_id('stateDelegate')
print(val.text)
'''
# try to click more info
WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located)
time.sleep(3)
more_info = driver.find_element_by_link_text("More Info")

more_info.click()


links = driver.find_elements_by_css_selector("a")

for link in links:
    email = link.get_attribute('href')
    try:
        if '@' in email and 'Del' in email:
            del_email = email.split(":")[-1]
    except:
        pass


driver.quit()

# get del name
e_lst = del_email.split("@")
del_lname = e_lst[0][4:]

# copied from temp_gen3

to = del_email
subject = "Subject Line"
sender = input("Please enter your name (First Last): ")
# can include district too
message = "Dear Delegate {}, \n\tMessage here\n\nSincerely,\n{}".format(del_lname, sender)

# reformat later
print("\nPlease see your template below: ")
print("\nTo: ", to)
print("Subject: ", subject)
print()
print(message)
