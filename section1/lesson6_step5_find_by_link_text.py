import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

page_link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(page_link)

    link_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    link = browser.find_element(By.LINK_TEXT, link_text)  # "//a[text()=" + link_text + "]"
    link.click()

    input1 = browser.find_element(By.TAG_NAME, "input")  # //input[@name='first_name']
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")  # //input[@name='last_name']
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")  # //input[contains(@class, 'city')]
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")  # //input[@id='country']
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")  # //button[contains(@class, 'btn')]
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
