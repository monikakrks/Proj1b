from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browse = webdriver.Chrome()
browse.get("https://system.aliorbank.pl/sign-in")
time.sleep(3) # Sleep for 3 seconds

title = browse.title
print(title)

from selenium.webdriver.common.by import By

webdriver.find_element("xpath", '//*[@id="https://system.aliorbank.pl/sign-in"]//input')
def find_element():
    find_element(By.ID, "id")
    find_element(By.password, "password")
    find_element(By.XPATH, "xpath")

username_field = webdriver.find_element(By.XPATH, value='/html/body/div/div/app-ajs-root/div/div[3]/auth/div/auth.sign-in/div/div/auth.sign-in.cif/div/main/div/div/div/div[1]/external-section/section/div/cif-form/form/div/div/fieldset/div')


webdriver.find_element(By.ID, 'login')
ID = "id"
password = "password"


username_field = webdriver.find_element(By.XPATH, value='/html/body/div/div/app-ajs-root/div/div[3]/auth/div/auth.sign-in/div/div/auth.sign-in.cif/div/main/div/div/div/div[1]/external-section/section/div/cif-form/form/div/div/fieldset/div')

username_field.send_keys('test-user')

button = webdriver.find_element_by_xpath('/html/body/div/div/app-ajs-root/div/div[3]/auth/div/auth.sign-in/div/div/auth.sign-in.cif/div/main/div/div/div/div[1]/external-section/section/div/cif-form/form/div/div/button')

button.click()


browse.quit()



