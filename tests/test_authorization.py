from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import pass_recov_page
from locators import Locators
from constants import Constants


class TestStellarAuth:
#Проверка: вход по кнопке «Войти в аккаунт» на главной
    def test_authorization_button_enteracc_successful_auth(self,driver):
        driver.find_element(*Locators.AUTH_ENTERACC_BUTTON).click()
        driver.find_element(*Locators.REG_EMAIL_FIELD).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.REG_PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_LOGINBUTTON).click()
        reg_text = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.AUTH_BUTTON_CHANGED)).text
        assert reg_text == "Оформить заказ"

#Проверка: вход через кнопку «Личный кабинет»
    def test_authorization_button_cabinet_successful_auth(self,driver):
        driver.find_element(*Locators.AUTH_CABINET_BUTTON).click()
        driver.find_element(*Locators.REG_EMAIL_FIELD).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.REG_PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_LOGINBUTTON).click()
        reg_text = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.AUTH_BUTTON_CHANGED)).text
        assert reg_text == "Оформить заказ"

#Проверка: вход через кнопку в форме регистрации
    def test_authorization_button_on_registration_page_successful_auth(self,reg_page):
        reg_page.find_element(*Locators.AUTH_LOGIN_BUTTON_IN_REGISTR).click()
        reg_page.find_element(*Locators.REG_EMAIL_FIELD).send_keys(Constants.EMAIL)
        reg_page.find_element(*Locators.REG_PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        reg_page.find_element(*Locators.AUTH_LOGINBUTTON).click()
        reg_text = WebDriverWait(reg_page, 5).until(expected_conditions.visibility_of_element_located(Locators.AUTH_BUTTON_CHANGED)).text
        assert reg_text == "Оформить заказ"

#Проверка: вход через кнопку в форме восстановления пароля
    def test_authorization_button_on_password_recovery_page_successful_auth(self, pass_recov_page):
        pass_recov_page.find_element(*Locators.AUTH_LOGIN_BUTTON_IN_PASSWORD).click()
        pass_recov_page.find_element(*Locators.REG_EMAIL_FIELD).send_keys(Constants.EMAIL)
        pass_recov_page.find_element(*Locators.REG_PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        pass_recov_page.find_element(*Locators.AUTH_LOGINBUTTON).click()
        reg_text = WebDriverWait(pass_recov_page, 5).until(expected_conditions.visibility_of_element_located(Locators.AUTH_BUTTON_CHANGED)).text
        assert reg_text == "Оформить заказ"

