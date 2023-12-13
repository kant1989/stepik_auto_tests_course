from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("Ivanov")

    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("Ivan@test.com")

    os.chdir("..")
    file_path = os.path.join(os.getcwd(), 'resources', 'upload.txt')

    file = browser.find_element(By.CSS_SELECTOR, "#file")
    file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
