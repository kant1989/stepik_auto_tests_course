import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def is_present(browser, xpath):
    try:
        browser.find_element(By.XPATH, xpath)
        return True
    except NoSuchElementException:
        return False


def answer():
    return str(math.log(int(time.time())))


class TestParameterization():
    @pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                      "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                      "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                      "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
    def test_parameterization(self, browser, link):
        browser.get(link)
        # блок авторизации
        sign_button1 = WebDriverWait(browser, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a.navbar__auth_login"))
        )
        sign_button1.click()

        input_email = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
        input_email.send_keys("login")

        input_password = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
        input_password.send_keys("password")

        sign_button2 = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
        sign_button2.click()

        time.sleep(5)

        # блок ввода ответа в поле и отправка
        if is_present(browser, "//button[text()='Начать сначала (сброс)']"):
            button_again = browser.find_element(By.XPATH, "//button[text()='Начать сначала (сброс)']")
            button_again.click()
            ok_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']"))
            )
            ok_button.click()
            WebDriverWait(browser, 10).until(
                EC.staleness_of(button_again)
            )
        elif is_present(browser, "//button[text()='Решить снова']"):
            button_again = browser.find_element(By.XPATH, "//button[text()='Решить снова']")
            button_again.click()
            WebDriverWait(browser, 10).until(
                EC.staleness_of(button_again)
            )

        textarea = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea"))
        )
        textarea.send_keys(answer())
        submit_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
        submit_button.click()
        WebDriverWait(browser, 10).until(
            EC.staleness_of(submit_button)
        )

        answer_text = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint"))
        )

        assert answer_text.text == "Correct!", "Incorrect answer"
