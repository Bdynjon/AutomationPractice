import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x: int):
    return math.log(abs(12*math.sin(x)))


url = "http://suninjuly.github.io/explicit_wait2.html"


with Chrome() as browser:
    browser.get(url)
    browser.implicitly_wait(5)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    button = browser.find_element(By.CSS_SELECTOR, "button[id='book']")
    button.click()

    span_x = browser.find_element(By.ID, "input_value")
    x = int(span_x.text)

    result_field = browser.find_element(By.ID, "answer")
    result_field.send_keys(str(calc(x)))

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    alert = browser.switch_to.alert
    print(alert.text)
    time.sleep(5)
