import pytest
from data.data import LoginPageData
from pages.login_page import LoginPage
from locators.profile_page_locators import ProfilePageLocators
from locators.login_page_locators import LoginPageLocator


@pytest.mark.parametrize("email", LoginPageData.VALID_EMAILS)
@pytest.mark.smoke
def test_login(browser, email):
    page = LoginPage(browser, LoginPageData.LOGIN_PAGE_URL)
    page.open()
    page.enter_login(email)
    page.enter_pass()
    page.submit_btn()
    element = page.element_is_visible(ProfilePageLocators.PET_ADDING_BUTTON, 3)
    browser.save_screenshot("/Users/anastasiya.niadbailik/Automation/Selenium_UI_Pets/screenshots/login.png")
    assert element.is_displayed() is True


@pytest.mark.parametrize("email", LoginPageData.INVALID_EMAILS)
@pytest.mark.smoke
def test_login_with_unregistered_email(browser, email):
    page = LoginPage(browser, LoginPageData.LOGIN_PAGE_URL)
    page.open()
    page.enter_login(email)
    page.enter_pass()
    page.submit_btn()
    page.element_is_visible(LoginPageLocator.INVALID_EMAIL_LOGIN_WARNING, 3)
    browser.save_screenshot("/Users/anastasiya.niadbailik/Automation/Selenium_UI_Pets/screenshots/login.png")


@pytest.mark.parametrize("email", LoginPageData.INCORRECT_EMAILS)
@pytest.mark.regression
def test_login_with_incorrect_email(browser, email):
    page = LoginPage(browser, LoginPageData.LOGIN_PAGE_URL)
    page.open()
    page.enter_login(email)
    page.enter_pass()
    page.submit_btn()
    page.element_is_visible(LoginPageLocator.VALIDATION_FIELD_IS_EMAIL, 3)
    browser.save_screenshot("/Users/anastasiya.niadbailik/Automation/Selenium_UI_Pets/screenshots/login.png")


@pytest.mark.parametrize("password", LoginPageData.INVALID_PASS)
@pytest.mark.regression
def test_login_with_invalid_password(browser, password):
    page = LoginPage(browser, LoginPageData.LOGIN_PAGE_URL)
    page.open()
    page.enter_valid_login()
    page.enter_invalid_pass(password)
    page.submit_btn()
    element = page.element_is_visible(LoginPageLocator.WRONG_MESSAGE, 3)
    browser.save_screenshot("/Users/anastasiya.niadbailik/Automation/Selenium_UI_Pets/screenshots/invalid_pass.png")
    assert element.is_displayed() is True


@pytest.mark.extended_path
def test_login_fields_validation(browser):
    page = LoginPage(browser, LoginPageData.LOGIN_PAGE_URL)
    page.open()
    page.submit_btn()
    elements = page.elements_are_visible(LoginPageLocator.VALIDATION_FIELD_IS_REQUIRED, 3)
    browser.save_screenshot("/Users/anastasiya.niadbailik/Automation/Selenium_UI_Pets/screenshots/field_validation.png")
    validation_messages = len(elements)
    assert len(elements) == 2
