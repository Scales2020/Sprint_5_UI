from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(Constants.URL)
    yield browser
    browser.quit()

@pytest.fixture
def reg_page():
    browser = webdriver.Chrome()
    browser.get(Constants.URL_REG)
    yield browser
    browser.quit()

@pytest.fixture
def pass_recov_page():
    browser = webdriver.Chrome()
    browser.get(Constants.URL_PASS_RECOVERY)
    yield browser
    browser.quit()

@pytest.fixture
def login(driver):
    driver.find_element(*Locators.AUTH_ENTERACC_BUTTON).click()
    driver.find_element(*Locators.REG_EMAIL_FIELD).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.REG_PASSWORD_FIELD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.AUTH_LOGINBUTTON).click()

@pytest.fixture
def cabinet_page(driver, login):
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.AUTH_BUTTON_CHANGED))
    driver.find_element(*Locators.AUTH_CABINET_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CABINET_TEXT))

