from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
link = "https://suninjuly.github.io/math.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, ' #input_value')
    x = x_element.text
    y = calc(x)
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(y)
    robot = browser.find_element(By.ID, "robotCheckbox")
    robot.click()
    robots_rule = browser.find_element(By.ID, "robotsRule")
    robots_rule.click()
    submint = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    submint.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
