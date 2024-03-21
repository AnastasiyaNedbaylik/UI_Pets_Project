import requests
from locators.profile_page_locators import ProfilePageLocators, AddPetsLocators
from .base_page import BasePage
from data.data import NewPetData


class AddPetsForm(BasePage):

    def add_pet_btn(self):
        self.browser.find_element(*ProfilePageLocators.PET_ADDING_BUTTON).click()

    def input_pet_name(self):
        self.browser.find_element(*AddPetsLocators.ADD_PET_NAME).send_keys(*NewPetData.PET_NAME)

    def select_pet_type(self):
        self.browser.find_element(*AddPetsLocators.ADD_PET_TYPE).click()
        self.browser.find_element(*AddPetsLocators.SELECT_PET_TYPE).click()

    def input_pet_age(self):
        self.browser.find_element(*AddPetsLocators.ADD_PET_AGE).send_keys(*NewPetData.PET_AGE)

    def select_pet_gender(self):
        self.browser.find_element(*AddPetsLocators.ADD_PET_GENDER).click()
        self.browser.find_element(*AddPetsLocators.SELECT_PET_GENDER).click()

    def submit_button(self):
        self.browser.find_element(*AddPetsLocators.PET_SUBMIT_BUTTON).click()

    def add_pet_ava(self):
        self.browser.find_element(*AddPetsLocators.PET_CHOOSE_INPUT).send_keys(*NewPetData.IMG_LINK)
        # path to uploaded file
        self.browser.find_element(*AddPetsLocators.PET_CHOOSE_BUTTON).click()

    def open_profile_page(self):
        self.browser.find_element(*ProfilePageLocators.PROFILE_PAGE_LINK).click()

    def check_success_message(self):
        success_message = self.browser.find_element(*ProfilePageLocators.SUCCESS_MESSAGE)
        assert success_message

    def check_added_pet_in_profile(self):
        find_added_pet = self.browser.find_element(*ProfilePageLocators.PET_LIST)
        assert find_added_pet

    def check_response_for_pet_adding(self):
        response = requests.post(NewPetData.NEW_PET_POST)
        status_code = response.status_code
        assert status_code == 200, f'{response} is not our expectation'  # возвращаем текст ошибки
