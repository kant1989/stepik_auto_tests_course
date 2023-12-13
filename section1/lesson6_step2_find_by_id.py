from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
print(type(browser))
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit_button")
# button = browser.find_element(By.XPATH, "//button[@id='submit_button']")
browser.quit()
