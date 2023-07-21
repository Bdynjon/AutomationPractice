import time
from os import path
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome


url = "http://suninjuly.github.io/file_input.html"
filepath = path.join(path.dirname(__file__), 'file.txt')

with Chrome() as browser:
    browser.get(url)
    time.sleep(1)

    first_name_field = browser.find_element(By.NAME, "firstname")
    first_name_field.send_keys("first name")

    last_name_field = browser.find_element(By.NAME, "lastname")
    last_name_field.send_keys("last name")

    email_field = browser.find_element(By.NAME, "email")
    email_field.send_keys("email")

    choose_file_button = browser.find_element(By.NAME, "file")
    choose_file_button.send_keys(filepath)

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    time.sleep(5)
