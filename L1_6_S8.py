import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome


url = "http://suninjuly.github.io/find_xpath_form"

with Chrome() as browser:
    browser.get(url)
    time.sleep(1)

    first_name_field = browser.find_element(By.XPATH, "//input[@name='first_name']")
    first_name_field.send_keys("My first name")

    last_name_field = browser.find_element(By.XPATH, "//input[@name='last_name']")
    last_name_field.send_keys("My last name")

    city_field = browser.find_element(By.XPATH, "//input[@class='form-control city']")
    city_field.send_keys("City")

    country_field = browser.find_element(By.XPATH, "//input[@id='country']")
    country_field.send_keys("Country")

    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    time.sleep(5)
