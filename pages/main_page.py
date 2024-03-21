from selenium.webdriver import Keys
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data.data import MainPageData


class MainPage(BasePage):

    def filter_by_type(self):
        self.browser.find_element(*MainPageLocators.FILTER_BY_TYPE).click()

    def go_to_dog_list(self):
        self.browser.find_element(*MainPageLocators.DOG_CATEGORY).click()

    def go_to_cat_list(self):
        self.browser.find_element(*MainPageLocators.CAT_CATEGORY).click()

    def go_to_reptile_list(self):
        self.browser.find_element(*MainPageLocators.REPTILE_CATEGORY).click()

    def go_to_hamster_list(self):
        self.browser.find_element(*MainPageLocators.HAMSTER_CATEGORY).click()

    def go_to_parrot_list(self):
        self.browser.find_element(*MainPageLocators.PARROT_CATEGORY).click()

    def filter_by_name(self):
        pet_name = self.browser.find_element(*MainPageLocators.FILTER_BY_NAME)
        pet_name.click()
        pet_name.send_keys(MainPageData.PET_NAME)
        pet_name.send_keys(Keys.ENTER)

    def like_pet(self):
        self.browser.find_element(*MainPageLocators.LIKE_BTN).click()

    def go_to_next_page(self):
        self.browser.find_element(*MainPageLocators.NEXT_PAGE).click()

    def go_to_last_page(self):
        self.browser.find_element(*MainPageLocators.LAST_PAGE).click()

    def go_to_details(self):
        self.browser.find_element(*MainPageLocators.DETAILS_BTN).click()

    def go_to_profile(self):
        self.browser.find_element(*MainPageLocators.PROFILE_BTN).click()

    def click_logo_btn(self):
        self.browser.find_element(*MainPageLocators.LOGO).click()

    def logout(self):
        self.browser.find_element(*MainPageLocators.QUIT_BTN).click()

    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()

    def go_to_register_page(self):
        self.browser.find_element(*MainPageLocators.REGISTER_LINK).click()
