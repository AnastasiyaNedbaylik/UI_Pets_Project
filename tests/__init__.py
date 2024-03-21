import pytest
from pages.login_page import LoginPage


@pytest.fixture(scope='package')
def execute_login(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
