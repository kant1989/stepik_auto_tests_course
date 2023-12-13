from selenium import webdriver
from selenium.webdriver.common.by import By
import time

page_link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(page_link)

    input1 = browser.find_element(By.TAG_NAME, "input")  # //input[@name='first_name']
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")  # //input[@name='last_name']
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")  # //input[contains(@class, 'city')]
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")  # //input[@id='country']
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
