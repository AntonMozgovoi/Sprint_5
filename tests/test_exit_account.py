from selenium.webdriver.support.wait import WebDriverWait
from locators import StellaLocators
from selenium.webdriver.support import expected_conditions
from test_auth import TestStellarAuthtorisation


class TestExitAccont:
    def test_button_exit(self, driver):
        TestStellarAuthtorisation.test_auth_button_account(self, driver)
        enter_personal_button = driver.find_element(*StellaLocators.LINK_PERSONAL_ACCOUNT)
        enter_personal_button.click()
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(StellaLocators.EXIT_BUTTON))
        exit_button = driver.find_element(*StellaLocators.EXIT_BUTTON)
        exit_button.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellaLocators.LOGIN_SUBMINT_BUTTON))
        assert (driver.find_element(*StellaLocators.LOGIN_SUBMINT_BUTTON)).is_displayed()
