from locators.profile_page_locators import ProfilePageLocators
from pages.profile_page import ProfilePage
from data.data import LoginPageData, ProfilePageData, NewPetData, MainPageData, PetEditPage
import requests
import pytest
import time


@pytest.mark.smoke
def test_quit_profile(browser, execute_login):
    page = ProfilePage(browser, ProfilePageData.PROFILE_PAGE_URL)
    page.open()
    page.click_quit_btn()
    time.sleep(3)
    response = requests.get(LoginPageData.LOGIN_PAGE_URL)
    r = response.status_code
    assert response.status_code == 200, f'{r} is not our expectation'  # если вернется ошибка


@pytest.mark.smoke
def test_go_to_add_pet_page(browser, execute_login):
    page = ProfilePage(browser, ProfilePageData.PROFILE_PAGE_URL)
    page.open()
    page.click_add_pet()
    time.sleep(3)
    response = requests.get(NewPetData.NEW_PET_PAGE_URL)
    assert response.status_code == 200


@pytest.mark.regression
def test_go_to_pet_edit(browser, execute_login):
    page = ProfilePage(browser, ProfilePageData.PROFILE_PAGE_URL)
    page.open()
    page.edit_pet()
    time.sleep(2)
    response = requests.get(PetEditPage.PET_EDIT_URL)
    browser.save_screenshot("/Users/anastasiya.niadbailik/Automation/Selenium_UI_Pets/screenshots/edit_pet_page.png")
    assert response.status_code == 200


@pytest.mark.regression
def test_delete_pet(browser, execute_login):
    page = ProfilePage(browser, ProfilePageData.PROFILE_PAGE_URL)
    page.open()
    page.delete_pet()
    time.sleep(2)
    page.confirm_deleting()
    time.sleep(3)
    page.check_success_message()
    element = page.element_is_visible(ProfilePageLocators.SUCCESS_MESSAGE, 3)
    browser.save_screenshot("/Users/anastasiya.niadbailik/Automation/Selenium_UI_Pets/screenshots/delete_pet.png")
    assert element.is_displayed() is True
    response = requests.get(PetEditPage.PET_EDIT_URL)
    assert response.status_code == 200


@pytest.mark.regression
def test_go_to_main_page(browser, execute_login):
    page = ProfilePage(browser, ProfilePageData.PROFILE_PAGE_URL)
    page.open()
    page.click_logo_btn()
    browser.save_screenshot("/Users/anastasiya.niadbailik/Automation/Selenium_UI_Pets/screenshots/main_page.png")
    response = requests.get(MainPageData.MAIN_PAGE_URL)
    assert response.status_code == 200

# @pytest.mark.skip
# @pytest.mark.regression
# def test_delete_profile(browser, execute_login):
#     page = ProfilePage(browser, ProfilePageData.PROFILE_PAGE_URL)
#     page.open()
#     page.delete_profile()
#     time.sleep(3)
#     response = requests.get(LoginPageData.LOGIN_PAGE_URL)
#     assert response.status_code == 200
