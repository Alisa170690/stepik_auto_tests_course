from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
def calc(n):
    return str(int(n1)+int(n2))
link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    n1_element = browser.find_element(By.CSS_SELECTOR, ' #num1')
    n1 = n1_element.text
    n2_element = browser.find_element(By.CSS_SELECTOR, ' #num2')
    n2 = n2_element.text
    n = int(n1)+int(n2)
    y = calc(n)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y)
    sub_button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    sub_button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()