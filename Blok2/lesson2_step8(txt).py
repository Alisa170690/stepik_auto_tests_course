from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.XPATH,  '/html/body/div/form/div/input[1]')
    first_name.send_keys('imya')
    last_name = browser.find_element(By.XPATH,  '/html/body/div/form/div/input[2]')
    last_name.send_keys('familiya')
    email = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(6)')
    email.send_keys('111@gmail.com')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла
    element = (browser.find_element(By.ID, 'file'))
    element.send_keys(file_path)
    submint = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    submint.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
