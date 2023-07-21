import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome


def calc(x: int):
    return math.log(abs(12*math.sin(x)))


url = "http://suninjuly.github.io/redirect_accept.html"


with Chrome() as browser:
    browser.get(url)
    time.sleep(1)

    magic_button = browser.find_element(By.CLASS_NAME, "trollface")
    magic_button.click()

    second_window_name = browser.window_handles[1]
    browser.switch_to.window(second_window_name)
    time.sleep(1)

    span_x = browser.find_element(By.ID, "input_value")
    x = int(span_x.text)

    result_field = browser.find_element(By.ID, "answer")
    result_field.send_keys(str(calc(x)))

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    alert = browser.switch_to.alert
    print(alert.text)
    time.sleep(5)
