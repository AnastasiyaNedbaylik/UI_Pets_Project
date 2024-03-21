import pytest
from selenium import webdriver
from data.data import LoginPageData
from pages.login_page import LoginPage


@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture()
def execute_login(browser):
    page = LoginPage(browser, LoginPageData.LOGIN_PAGE_URL)
    page.open()
    page.enter_valid_login()
    page.enter_pass()
    page.submit_btn()
