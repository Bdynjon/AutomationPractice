import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome


url = "http://suninjuly.github.io/registration2.html"
welcome_text = "Congratulations! You have successfully registered!"

with Chrome() as browser:
    browser.get(url)
    time.sleep(1)

    first_name_field = browser.find_element(By.CSS_SELECTOR, "div.first_block input.first")
    first_name_field.send_keys("My first name")

    last_name_field = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
    last_name_field.send_keys("My last name")

    city_field = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
    city_field.send_keys("Email")

    submit_button = browser.find_element(By.CLASS_NAME, "btn")
    submit_button.click()

    h1 = browser.find_element(By.TAG_NAME, "h1")

    assert welcome_text == h1.text
    time.sleep(2)
