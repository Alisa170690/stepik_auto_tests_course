from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
link = "https://suninjuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    radio_btn = browser.find_element(By.ID, "robotsRule")
    # прокрутка страницы
    browser.execute_script("window.scrollBy(0, 100);", radio_btn)
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(y)
    robot = browser.find_element(By.ID, "robotCheckbox")
    robot.click()
    robots_rule = browser.find_element(By.ID, "robotsRule")
    robots_rule.click()
    radio_btn.click()
    sub_button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    sub_button.click()
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()




