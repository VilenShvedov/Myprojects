from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


webdriver_location = 'chromedriver.exe'
driver = webdriver.Chrome()
driver.implicitly_wait(7)
driver.get('https://particle-clicker.web.cern.ch/')

click_object = driver.find_element_by_id('detector-events')

actions = ActionChains(driver)
actions.click(click_object)
count = 0

for i in range(20):
    actions.perform()









'''link = driver.find_element_by_partial_link_text('infot')
link.click()
source1 = driver.page_source
time.sleep(5)
driver.back()
source2 = driver.page_source
if source2 == source1:
    print('same page')
else:
    print('not same page')
driver.forward()'''











'''email_input = driver.find_element_by_id('user_email')
email_input.send_keys('Tratevs@gmail.com')


sing_up_button = driver.find_element_by_xpath('/html/body/div[4]/main/div[1]/div[1]/div[1]/div/div/div[1]/form/div/button')
sing_up_button.click()
time.sleep(7)
sing_up_button = driver.find_element_by_class_name('signup-continue-button')
sing_up_button.click()
password_input = driver.find_element_by_id('password')
password_input.send_keys('Afasfasf223')
password_input.send_keys(Keys.RETURN)
time.sleep(3)
continue_button = driver.find_element_by_xpath('/html/body/div[4]/main/div[2]/text-suggester/div[1]/form/div[2]/div[2]/button')
continue_button.click()

driver.find_element_by_css_selector('#login')
driver.find_element_by_id('login')
driver.find_element_by_tag_name('div')'''













'''if search.is_enabled():
    print('All good')
    search.send_keys('python')
    search.send_keys(Keys.RETURN)
else:
    print('Error')'''