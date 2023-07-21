import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome


def calc(x: int):
    return math.log(abs(12*math.sin(x)))


url = "http://suninjuly.github.io/alert_accept.html"


with Chrome() as browser:
    browser.get(url)
    time.sleep(1)

    magic_button = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    magic_button.click()

    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)

    span_x = browser.find_element(By.ID, "input_value")
    x = int(span_x.text)

    result_field = browser.find_element(By.ID, "answer")
    result_field.send_keys(str(calc(x)))

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    time.sleep(5)
