from .base_page import BasePage
from locators.login_page_locators import LoginPageLocator
from data.data import LoginPageData


class LoginPage(BasePage):
    # def go_to_login(self):
    #     self.browser.find_element(*LoginPageLocator.LOGIN_EMAIL).send_keys(*LoginPageData.VALID_EMAIL)
    #     self.browser.find_element(*LoginPageLocator.LOGIN_PASSWORD).send_keys(*LoginPageData.VALID_PASS)
    #     self.browser.find_element(*LoginPageLocator.LOGIN_BUTTON).submit()

    def enter_valid_login(self):
        self.browser.find_element(*LoginPageLocator.LOGIN_EMAIL).send_keys(*LoginPageData.VALID_EMAIL)

    def enter_login(self, email):
        self.browser.find_element(*LoginPageLocator.LOGIN_EMAIL).send_keys(email)

    def enter_pass(self):
        self.browser.find_element(*LoginPageLocator.LOGIN_PASSWORD).send_keys(*LoginPageData.VALID_PASS)

    def enter_invalid_pass(self, password):
        self.browser.find_element(*LoginPageLocator.LOGIN_PASSWORD).send_keys(password)

    def submit_btn(self):
        self.browser.find_element(*LoginPageLocator.LOGIN_BUTTON).submit()
