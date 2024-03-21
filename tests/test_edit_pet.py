import time
import pytest
from data.data import PetEditPage
from locators.profile_page_locators import ProfilePageLocators
from pages.edit_pet import EditPet


@pytest.mark.smoke
def test_editing_pet(browser, execute_login):
    page = EditPet(browser, PetEditPage.PET_EDIT_URL)
    page.edit_pet_btn()
    page.clear() # поле не очищается, нужно подобрать другой локатор или другой метод очистки поля
    time.sleep(3)
    page.input_new_pet_name()
    time.sleep(3)
    page.input_new_pet_age()
    time.sleep(3)
    page.select_new_pet_gender()
    time.sleep(3)
    page.edit_pet_ava()
    page.save_edited_pet()
    time.sleep(3)
    page.check_success_message()
    element = page.element_is_visible(ProfilePageLocators.SUCCESS_MESSAGE, 3)
    browser.save_screenshot("/Users/anastasiya.niadbailik/Automation/Selenium_UI_Pets/screenshots/edit_pet.png")
    assert element.is_displayed() is True
