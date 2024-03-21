import pytest
from data.data import RegisterPageData, LoginPageData
from pages.register_page import RegisterPage
from locators.profile_page_locators import ProfilePageLocators
from locators.register_page_locators import RegisterPageLocators


@pytest.mark.smoke
def test_register(browser):
    page = RegisterPage(browser, RegisterPageData.REGISTER_PAGE_URL)
    page.open()
    page.input_email()
    page.input_password()
    page.show_password()
    page.confirm_password()
    browser.save_screenshot('/Users/anastasiya.niadbailik/Automation/Selenium_UI_Pets/screenshots/registr_new_user.png')
    page.submit_registration()
    page.element_is_visible(ProfilePageLocators.PET_ADDING_BUTTON)


@pytest.mark.parametrize("email", LoginPageData.INCORRECT_EMAILS)
@pytest.mark.regression
def test_register_with_incorrect_email(browser, email):
    page = RegisterPage(browser, RegisterPageData.REGISTER_PAGE_URL)
    page.open()
    page.input_emails(email)
    page.input_password()
    page.show_password()
    page.confirm_password()
    page.submit_registration()
    page.element_is_visible(RegisterPageLocators.FIELD_IS_EMAIL, 3)
    browser.save_screenshot('/Users/anastasiya.niadbailik/Automation/Selenium_UI_Pets/screenshots/regist_bad_email.png')
