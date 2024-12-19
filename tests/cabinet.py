from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from locators import Locators
from constants import Constants


class TestStellarCabinet:
#Проверка: Проверь переход по клику на «Личный кабинет»
    def test_authoriseduser_from_main_to_cabinet_see_personal_data(self, driver, login):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.AUTH_BUTTON_CHANGED))
        driver.find_element(*Locators.AUTH_CABINET_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CABINET_TEXT))
        assert "В этом разделе вы можете изменить свои персональные данные" in driver.find_element(*Locators.CABINET_TEXT).text

#Проверка: Проверь переход из Личного кабинета по клику на «Конструктор» и на логотип Stellar Burgers
    def test_from_cabinet_to_konstruktor_new_screen(self,driver,login, cabinet_page):
        driver.find_element(*Locators.BUTTON_KONSTRUKTOR).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.MAINPAGE_KONSTRUKTOR))
        assert "Соберите бургер" in driver.find_element(*Locators.MAINPAGE_KONSTRUKTOR).text

    def test_from_cabinet_to_logo_new_screen(self,driver,login, cabinet_page):
        driver.find_element(*Locators.BUTTON_LOGO).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.MAINPAGE_KONSTRUKTOR))
        assert "Соберите бургер" in driver.find_element(*Locators.MAINPAGE_KONSTRUKTOR).text

#Проверка: Проверь выход по кнопке «Выйти» в личном кабинете
    def test_exit_button_in_cabinet_successful_logout(self, driver,login, cabinet_page):
        driver.find_element(*Locators.BUTTON_LOGOUT).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Constants.URL_LOGIN))
        assert "Войти" in driver.find_element(*Locators.AUTH_LOGINBUTTON).text


