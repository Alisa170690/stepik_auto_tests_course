import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Вычисляем зашифрованный текст ссылки
link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

# Запускаем браузер
browser = webdriver.Chrome()

try:
    # Открываем нужную страницу
    browser.get("http://suninjuly.github.io/find_link_text")

    # Ищем ссылку с нужным текстом и кликаем по ней
    link = browser.find_element(By.LINK_TEXT, link_text)
    link.click()

    # Заполняем форму на открывшейся странице
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Имя")

    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Фамилия")

    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Город")

    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Страна")

    # Нажимаем кнопку отправки
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Ждём, чтобы увидеть результат
    time.sleep(10)

finally:
    browser.quit()
