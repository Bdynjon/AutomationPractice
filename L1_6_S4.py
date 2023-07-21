import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome


url = "http://suninjuly.github.io/simple_form_find_task.html"

with Chrome() as browser:
    browser.get(url)
    time.sleep(1)

    first_name_field = browser.find_element(By.NAME, "first_name")
    first_name_field.send_keys("My first name")

    last_name_field = browser.find_element(By.NAME, "last_name")
    last_name_field.send_keys("My last name")

    city_field = browser.find_element(By.CLASS_NAME, "city")
    city_field.send_keys("City")

    country_field = browser.find_element(By.ID, "country")
    country_field.send_keys("Country")

    submit_button = browser.find_element(By.ID, "submit_button")
    submit_button.click()
    time.sleep(5)

    browser.quit()
