import math
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
button = browser.find_element(By.CSS_SELECTOR, "#book")
WebDriverWait(browser, 13).until(ec.text_to_be_present_in_element((By.ID, "price"), "$100"))
button.click()
sub_button = browser.find_element(By.XPATH, "//*[@id='solve']")
# прокрутка страницы
browser.execute_script("window.scrollBy(0, 100);", sub_button)
x_element = browser.find_element(By.CSS_SELECTOR, ' #input_value')
x = x_element.text
y = calc(x)
answer = browser.find_element(By.CSS_SELECTOR, '#answer')
answer.send_keys(y)
sub_button.click()
time.sleep(5)
