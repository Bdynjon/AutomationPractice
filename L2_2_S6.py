import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome


def calc(x: int):
    return math.log(abs(12*math.sin(x)))


url = "http://suninjuly.github.io/execute_script.html"


with Chrome() as browser:
    browser.get(url)
    time.sleep(1)

    span_x = browser.find_element(By.ID, "input_value")
    x = int(span_x.text)

    result_field = browser.find_element(By.ID, "answer")
    result_field.send_keys(str(calc(x)))

    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    robot_radio = browser.find_element(By.ID, "robotsRule")
    robot_radio.click()

    button.click()
    time.sleep(5)
