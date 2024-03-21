import time
import pytest
import requests
from data.data import ProfilePageData
from locators.profile_page_locators import ProfilePageLocators
from pages.add_pets import AddPetsForm


@pytest.mark.smoke
def test_add_pet_with_required_data(browser, execute_login):
    page = AddPetsForm(browser, ProfilePageData.PROFILE_PAGE_URL)
    page.add_pet_btn()
    page.input_pet_name()
    page.select_pet_type()
    page.input_pet_age()
    page.select_pet_gender()
    page.submit_button()
    time.sleep(2)
    page.open_profile_page()
    page.check_success_message()
    element = page.element_is_visible(ProfilePageLocators.SUCCESS_MESSAGE, 3)
    browser.save_screenshot("/Users/anastasiya.niadbailik/Automation/Selenium_UI_Pets/screenshots/add_pet.png")
    assert element.is_displayed() is True
    response = requests.get(ProfilePageData.PROFILE_PAGE_URL)
    assert response.status_code == 200
    page.check_added_pet_in_profile()


@pytest.mark.smoke
def test_add_pet_with_ava(browser, execute_login):
    page = AddPetsForm(browser, ProfilePageData.PROFILE_PAGE_URL)
    page.add_pet_btn()
    page.input_pet_name()
    page.select_pet_type()
    page.input_pet_age()
    page.select_pet_gender()
    page.submit_button()
    time.sleep(2)
    page.add_pet_ava()
    time.sleep(3)
    page.check_success_message()
    element = page.element_is_visible(ProfilePageLocators.SUCCESS_MESSAGE, 3)
    browser.save_screenshot("/Users/anastasiya.niadbailik/Automation/Selenium_UI_Pets/screenshots/add_pet_with_ava.png")
    assert element.is_displayed() is True
    response = requests.get(ProfilePageData.PROFILE_PAGE_URL)
    assert response.status_code == 200
    page.check_added_pet_in_profile()


@pytest.mark.xfail
def test_add_pet_with_ava(browser, execute_login):
    page = AddPetsForm(browser, ProfilePageData.PROFILE_PAGE_URL)
    page.add_pet_btn()
    page.input_pet_name()
    page.select_pet_type()
    page.input_pet_age()
    page.select_pet_gender()
    page.submit_button()
    time.sleep(2)
    page.add_pet_ava()
    time.sleep(3)
    page.check_response_for_pet_adding()
    page.check_success_message()
    element = page.element_is_visible(ProfilePageLocators.SUCCESS_MESSAGE, 3)
    browser.save_screenshot("/Users/anastasiya.niadbailik/Automation/Selenium_UI_Pets/screenshots/add_pet_with_ava.png")
    assert element.is_displayed() is True
    response = requests.get(ProfilePageData.PROFILE_PAGE_URL)
    assert response.status_code == 200
    page.check_added_pet_in_profile()
