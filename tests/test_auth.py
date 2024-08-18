from selenium.webdriver.support.wait import WebDriverWait
from locators import StellaLocators
from data import Data


class TestStellarAuthtorisation:

        def test_auth_button_account(self, driver):
            enter_button = driver.find_element(*StellaLocators.ENTER_ACCOUNT_BUTTON)
            enter_button.click()

            name_input = driver.find_element(*StellaLocators.LOGIN_INPUT)
            name_input.send_keys(Data.AUTH_EMAIL)

            password_input = driver.find_element(*StellaLocators.PASSWORD_INPUT)
            password_input.send_keys(Data.AUTH_PASSWORD)

            submint_button = driver.find_element(*StellaLocators.LOGIN_SUBMINT_BUTTON)
            submint_button.click()
            assert driver.current_url == Data.STELLAR_LOG

        def testAuthPersonal(self, driver):
            enter_button = driver.find_element(*StellaLocators.ENTER_ACCOUNT_BUTTON)
            enter_button.click()

            name_input = driver.find_element(*StellaLocators.LOGIN_INPUT)
            name_input.send_keys(Data.AUTH_EMAIL)

            password_input = driver.find_element(*StellaLocators.PASSWORD_INPUT)
            password_input.send_keys(Data.AUTH_PASSWORD)

            submint_button = driver.find_element(*StellaLocators.LOGIN_SUBMINT_BUTTON)
            submint_button.click()
            assert driver.current_url == Data.STELLAR_LOG

        def testAuthRegisterFormButton(self, driver):

            enter_button = driver.find_element(*StellaLocators.ENTER_ACCOUNT_BUTTON)
            enter_button.click()

            enter_button = driver.find_element(*StellaLocators.LINK_REGISTER)
            enter_button.click()

            enter_button = driver.find_element(*StellaLocators.LINK_ENTER)
            enter_button.click()

            name_input = driver.find_element(*StellaLocators.LOGIN_INPUT)
            name_input.send_keys(Data.AUTH_EMAIL)

            password_input = driver.find_element(*StellaLocators.PASSWORD_INPUT)
            password_input.send_keys(Data.AUTH_PASSWORD)

            submint_button = driver.find_element(*StellaLocators.LOGIN_SUBMINT_BUTTON)
            submint_button.click()
            assert driver.current_url == Data.STELLAR_LOG
        def testAuthRecoverPassword(self, driver):
            enter_button = driver.find_element(*StellaLocators.ENTER_ACCOUNT_BUTTON)
            enter_button.click()

            enter_button = driver.find_element(*StellaLocators.LINK_REGISTER)
            enter_button.click()

            enter_button = driver.find_element(*StellaLocators.LINK_ENTER)
            enter_button.click()

            enter_button = driver.find_element(*StellaLocators.LINK_RECOVER_PASSWORD)
            enter_button.click()

            enter_button = driver.find_element(*StellaLocators.LINK_ENTER)
            enter_button.click()

            name_input = driver.find_element(*StellaLocators.LOGIN_INPUT)
            name_input.send_keys(Data.AUTH_EMAIL)

            password_input = driver.find_element(*StellaLocators.PASSWORD_INPUT)
            password_input.send_keys(Data.AUTH_PASSWORD)

            submint_button = driver.find_element(*StellaLocators.LOGIN_SUBMINT_BUTTON)
            submint_button.click()
            assert driver.current_url == Data.STELLAR_LOG



