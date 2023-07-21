import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

url = "http://suninjuly.github.io/huge_form.html"

with Chrome() as browser:
    browser.get(url)

    fields = browser.find_elements(By.TAG_NAME, "input")
    for field in fields:
        field.send_keys("A")

    submit_button = browser.find_element(By.TAG_NAME, "button")
    submit_button.click()
    time.sleep(5)
