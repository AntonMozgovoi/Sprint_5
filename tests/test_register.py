from selenium.webdriver.support.wait import WebDriverWait
from locators import StellaLocators
from data import Data


class TestStellarRegister:
    def test_stellar_register_positive(self, driver):
        enter_button = driver.find_element(*StellaLocators.ENTER_ACCOUNT_BUTTON)
        enter_button.click()

        register_link = driver.find_element(*StellaLocators.REGISTER_LINK)
        register_link.click()


        name_input = driver.find_element(*StellaLocators.NAME_REG_INPUT)
        name_input.send_keys(Data.REG_NAME)


        email_input = driver.find_element(*StellaLocators.EMAIL_REG_INPUT)
        email_input.send_keys(Data.REG_EMAIL)

        password_input = driver.find_element(*StellaLocators.PASSWORD_REG_INPUT)
        password_input.send_keys(Data.REG_PASSWORD)


        register_button = driver.find_element(*StellaLocators.BUTTON_REG)
        register_button.click()

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_stellar_register_negative(self, driver):
        enter_button = driver.find_element(*StellaLocators.ENTER_ACCOUNT_BUTTON)
        enter_button.click()

        register_link = driver.find_element(*StellaLocators.REGISTER_LINK)
        register_link.click()

        name_input = driver.find_element(*StellaLocators.NAME_REG_INPUT)
        name_input.send_keys(Data.REG_NAME)

        email_input = driver.find_element(*StellaLocators.EMAIL_REG_INPUT)
        email_input.send_keys(Data.REG_EMAIL)

        password_input = driver.find_element(*StellaLocators.PASSWORD_REG_INPUT)
        password_input.send_keys(Data.UNCORRECT_REG_PASSWORD)

        register_button = driver.find_element(*StellaLocators.BUTTON_REG)
        register_button.click()

        error_message = driver.find_element(*StellaLocators.ERROR_MESSAGE)
        assert error_message.is_displayed()





