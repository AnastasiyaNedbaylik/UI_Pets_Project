from .base_page import BasePage
from locators.register_page_locators import RegisterPageLocators
from data.data import RegisterPageData


class RegisterPage(BasePage):
    def input_email(self):
        self.browser.find_element(*RegisterPageLocators.LOGIN_INPUT).send_keys(*RegisterPageData.LOGIN)

    def input_password(self):
        self.browser.find_element(*RegisterPageLocators.INPUT_PASS).send_keys(*RegisterPageData.PASS)

    def confirm_password(self):
        self.browser.find_element(*RegisterPageLocators.CONFIRM_PASS).send_keys(*RegisterPageData.PASS)

    def submit_registration(self):
        self.browser.find_element(*RegisterPageLocators.SUBMIT_BTTN).submit()

    def input_emails(self, email):
        self.browser.find_element(*RegisterPageLocators.LOGIN_INPUT).send_keys(email)

    def show_password(self):
        self.browser.find_element(*RegisterPageLocators.TOGGLE_PASS_VISIBILITY).click()
