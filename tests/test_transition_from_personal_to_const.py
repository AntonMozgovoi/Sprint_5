import time

from selenium.webdriver.support.wait import WebDriverWait
from locators import StellaLocators
from data import Data
from test_auth import TestStellarAuthtorisation


class TestTransitionFromPersonalToConst:
    def test_transitional_to_const_link(self,driver):
        TestStellarAuthtorisation.test_auth_button_account(self,driver)

        personal_account_link = driver.find_element(*StellaLocators.LINK_PERSONAL_ACCOUNT)
        personal_account_link.click()

        constructor_link = driver.find_element(*StellaLocators.LINK_CONSTRUCTOR)
        constructor_link.click()
        assert driver.current_url == Data.STELLAR_TRANSIT

    def test_transitional_to_const_logo(self,driver):
        TestStellarAuthtorisation.test_auth_button_account(self,driver)

        personal_account_link = driver.find_element(*StellaLocators.LINK_PERSONAL_ACCOUNT)
        personal_account_link.click()

        logo_link = driver.find_element(*StellaLocators.LOGO)
        logo_link.click()

        constructor_link = driver.find_element(*StellaLocators.LINK_CONSTRUCTOR)
        constructor_link.click()
        assert driver.current_url == Data.STELLAR_TRANSIT