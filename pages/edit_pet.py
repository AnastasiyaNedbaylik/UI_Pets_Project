import time
from tkinter import *
from tkinter import END

from locators.profile_page_locators import ProfilePageLocators, AddPetsLocators, EditPetLocators
from .base_page import BasePage
from .login_page import LoginPage
from data.data import NewPetData


class EditPet(BasePage):

    def edit_pet_btn(self):
        self.browser.find_element(*ProfilePageLocators.PET_EDIT_BUTTON).click()

    def clear(self):
        self.browser.find_element(*EditPetLocators.PET_NAME).click()
        self.browser.find_element(*EditPetLocators.PET_NAME).clear()

    def input_new_pet_name(self):
        self.browser.find_element(*EditPetLocators.PET_NAME).send_keys(*NewPetData.NEW_PET_NAME)

    def input_new_pet_age(self):
        self.browser.find_element(*AddPetsLocators.ADD_PET_AGE).clear()
        time.sleep(4)
        self.browser.find_element(*AddPetsLocators.ADD_PET_AGE).send_keys(*NewPetData.NEW_PET_AGE)

    def select_new_pet_gender(self):
        self.browser.find_element(*AddPetsLocators.ADD_PET_GENDER).click()
        self.browser.find_element(*AddPetsLocators.SELECT_PET_GENDER_FEMALE).click()

    def edit_pet_ava(self):
        self.browser.find_element(*EditPetLocators.IMAGE_INPUT).send_keys(*NewPetData.NEW_IMG_LINK)
        # path to uploaded file
        self.browser.find_element(*EditPetLocators.IMAGE_CHOOSE_BUTTON).click()

    def save_edited_pet(self):
        self.browser.find_element(*ProfilePageLocators.PET_PROFILE_SAVING).click()

    def check_success_message(self):
        success_message = self.browser.find_element(*ProfilePageLocators.SUCCESS_MESSAGE)
        assert success_message
