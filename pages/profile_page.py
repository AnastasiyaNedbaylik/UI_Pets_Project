from .base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):

    def click_quit_btn(self):
        self.browser.find_element(*ProfilePageLocators.QUIT_BTN).click()

    def click_add_pet(self):
        self.browser.find_element(*ProfilePageLocators.PET_ADDING_BUTTON).click()

    def delete_profile(self):
        self.browser.find_element(*ProfilePageLocators.DELITE_PROFILE_BTN).click()

    def edit_pet(self):
        self.browser.find_element(*ProfilePageLocators.PET_EDIT_BUTTON).click()

    def delete_pet(self):
        self.browser.find_element(*ProfilePageLocators.PET_DELETE_BUTTON).click()

    def confirm_deleting(self):
        self.browser.find_element(*ProfilePageLocators.PET_DELETE_CONFIRM_BUTTON_YES).click()

    def check_success_message(self):
        self.browser.find_element(*ProfilePageLocators.SUCCESS_MESSAGE)

    def click_logo_btn(self):
        self.browser.find_element(*ProfilePageLocators.SITE_LOGO).click()
