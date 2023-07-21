import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select


url = "http://suninjuly.github.io/selects2.html"


with Chrome() as browser:
    browser.get(url)
    time.sleep(1)

    first_value = int(browser.find_element(By.ID, "num1").text)
    second_value = int(browser.find_element(By.ID, "num2").text)
    result = first_value + second_value

    answers_list = browser.find_element(By.ID, "dropdown")
    selector_answer = Select(answers_list)
    selector_answer.select_by_value(str(result))

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(5)
