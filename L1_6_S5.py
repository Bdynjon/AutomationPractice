import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome


url = "http://suninjuly.github.io/find_link_text"

with Chrome() as browser:
    browser.get(url)
    time.sleep(0.5)

    result = math.ceil(math.pow(math.pi, math.e)*10000)
    print(result)
    correct_link = browser.find_element(By.LINK_TEXT, str(result))
    correct_link.click()
    time.sleep(1)

    first_name_field = browser.find_element(By.NAME, "first_name")
    first_name_field.send_keys("My first name")

    last_name_field = browser.find_element(By.NAME, "last_name")
    last_name_field.send_keys("My last name")

    city_field = browser.find_element(By.CLASS_NAME, "city")
    city_field.send_keys("City")

    country_field = browser.find_element(By.ID, "country")
    country_field.send_keys("Country")

    submit_button = browser.find_element(By.CLASS_NAME, "btn")
    submit_button.click()
    time.sleep(5)
