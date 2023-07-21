from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


url = "http://suninjuly.github.io/cats.html"


with Chrome() as browser:
    browser.get(url)
    browser.find_element(By.ID, "button")
