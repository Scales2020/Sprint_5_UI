from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators

class TestStellarKonstruktor:
#Проверка: убедиться, что работают переходы к разделам: из Булки в Соусы
    def test_switch_from_bulki_to_sauce_section_successful(self, driver):
        driver.find_element(*Locators.KONSTRUKTOR_SAUCE).click()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.SAUCE_PICTURE))

#Проверка: убедиться, что работают переходы к разделам: из Булки в Начинки
    def test_switch_from_bulki_to_filling_section_successful(self, driver):
        driver.find_element(*Locators.KONSTRUKTOR_FILLINGS).click()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.FILLING_PICTURE))

#Проверка, что работают переходы к разделам: из Булки в Начинки и потом в Булки
    def test_switch_from_fillings_to_bulki_section_successful(self, driver):
        driver.find_element(*Locators.KONSTRUKTOR_FILLINGS).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.FILLING_PICTURE))
        driver.find_element(*Locators.KONSTRUKTOR_BULKI).click()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.BULKA_PICTURE))
