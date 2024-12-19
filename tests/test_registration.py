from faker.contrib.pytest.plugin import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from constants import Constants

faker = Faker()

class TestStellarReg:
    def test_new_registration_successful(self, reg_page):
        name = faker.name()
        reg_page.find_element(*Locators.REG_NAME_FIELD).send_keys(name)
        email = faker.email()
        reg_page.find_element(*Locators.REG_EMAIL_FIELD).send_keys(email)
        reg_page.find_element(*Locators.REG_PASSWORD_FIELD).send_keys("qwerty")
        reg_page.find_element(*Locators.REG_SIGNIN_BUTTON).click()
        WebDriverWait(reg_page, 7).until(expected_conditions.visibility_of_element_located((Locators.REG_FINAL_TITLE)))
        assert "Вход" in reg_page.find_element(*Locators.REG_FINAL_TITLE).text

    def test_registration_incorrect_password_errormessage(self, reg_page):
        name = faker.name()
        reg_page.find_element(*Locators.REG_NAME_FIELD).send_keys(name)
        email = faker.email()
        reg_page.find_element(*Locators.REG_EMAIL_FIELD).send_keys(email)
        reg_page.find_element(*Locators.REG_PASSWORD_FIELD).send_keys("qwer")
        reg_page.find_element(*Locators.REG_SIGNIN_BUTTON).click()
        WebDriverWait(reg_page, 7).until(expected_conditions.visibility_of_element_located((Locators.REG_INCORRECT_PASSWORD_MESS)))
        assert "Некорректный пароль" in reg_page.find_element(*Locators.REG_INCORRECT_PASSWORD_MESS).text

