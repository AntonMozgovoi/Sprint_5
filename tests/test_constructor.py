from locators import StellaLocators
from test_auth import TestStellarAuthtorisation
import time

class TestConstructor:
    def test_souces(self,driver):
        sauces = driver.find_element(*StellaLocators.SAUCE_ON_MENU)
        sauces.click()

        sauce_item = driver.find_element(*StellaLocators.SAUCE)
        assert sauce_item.is_displayed()
    def test_fillings(self, driver):
        fillings = driver.find_element(*StellaLocators.FILLINGS_ON_MENU)
        fillings.click()

        fillings_item = driver.find_element(*StellaLocators.FILLINGS)
        assert fillings_item.is_displayed()

    def test_bun(self, driver):
        driver.find_element(*StellaLocators.BUN_ON_MENU)
        fillings_item = driver.find_element(*StellaLocators.BUN)
        assert fillings_item.is_displayed()
