import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome


def calc(x: int):
    return math.log(abs(12*math.sin(x)))


url = "http://suninjuly.github.io/get_attribute.html"


with Chrome() as browser:
    browser.get(url)
    time.sleep(1)

    treasure_img = browser.find_element(By.ID, "treasure")
    x = int(treasure_img.get_attribute("valuex"))

    result_field = browser.find_element(By.ID, "answer")
    result_field.send_keys(str(calc(x)))

    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    robot_radio = browser.find_element(By.ID, "robotsRule")
    robot_radio.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(5)
