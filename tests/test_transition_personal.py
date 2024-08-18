from selenium.webdriver.support.wait import WebDriverWait
from locators import StellaLocators
from data import Data
import time

class Test_transition_personal:

        def test_transition_by_button(self, driver):
            enter_button = driver.find_element(*StellaLocators.ENTER_ACCOUNT_BUTTON)
            enter_button.click()

            name_input = driver.find_element(*StellaLocators.LOGIN_INPUT)
            name_input.send_keys(Data.AUTH_EMAIL)

            password_input = driver.find_element(*StellaLocators.PASSWORD_INPUT)
            password_input.send_keys(Data.AUTH_PASSWORD)

            submint_button = driver.find_element(*StellaLocators.LOGIN_SUBMINT_BUTTON)
            submint_button.click()
            assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

