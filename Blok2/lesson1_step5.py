import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Функция для вычисления значения по формуле
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Запуск браузера
browser = webdriver.Chrome()

try:
    # Открытие страницы
    browser.get("https://suninjuly.github.io/math.html")

    # Получаем значение x со страницы
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # Вычисляем результат
    result = calc(x)

    # Вводим результат в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)

    # Отмечаем checkbox "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Выбираем radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # Ожидание, чтобы увидеть результат
    time.sleep(5)

finally:
    browser.quit()
