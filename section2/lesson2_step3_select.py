from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element = browser.find_element(By.CSS_SELECTOR, '#num1')  # //span[@id='num1']
    num1 = int(num1_element.text)

    num2_element = browser.find_element(By.CSS_SELECTOR, '#num2')  # //span[@id='num2']
    num2 = int(num2_element.text)

    total = num1 + num2

    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))  # //select
    select.select_by_visible_text(str(total))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()