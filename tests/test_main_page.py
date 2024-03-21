from pages.main_page import MainPage
from data.data import MainPageData, ProfilePageData, LoginPageData
import requests
import pytest
import time


@pytest.mark.smoke
def test_go_to_profile_page(browser, execute_login):
    page = MainPage(browser, MainPageData.MAIN_PAGE_URL)
    page.open()
    page.click_logo_btn()
    time.sleep(5)
    page.go_to_profile()
    response = requests.get(ProfilePageData.PROFILE_PAGE_URL)
    assert response.status_code == 200


@pytest.mark.regression
def test_logout(browser, execute_login):
    page = MainPage(browser, MainPageData.MAIN_PAGE_URL)
    page.open()
    page.click_logo_btn()
    page.logout()
    response = requests.get(LoginPageData.LOGIN_PAGE_URL)
    assert response.status_code == 200


@pytest.mark.smoke
def test_filter_pet_by_type(browser):
    page = MainPage(browser, MainPageData.MAIN_PAGE_URL)
    page.open()
    page.filter_by_type()
    page.go_to_cat_list()
    time.sleep(3)
    browser.save_screenshot('/Users/anastasiya.niadbailik/Automation/Selenium_UI_Pets/screenshots/filters_cat.png')


@pytest.mark.smoke
def test_filter_pet_by_type(browser):
    page = MainPage(browser, MainPageData.MAIN_PAGE_URL)
    page.open()
    page.filter_by_type()
    time.sleep(3)
    page.go_to_dog_list()
    time.sleep(3)
    browser.save_screenshot('/Users/anastasiya.niadbailik/Automation/Selenium_UI_Pets/screenshots/filters_dogs.png')


@pytest.mark.regression
def test_filter_pet_by_type(browser):
    page = MainPage(browser, MainPageData.MAIN_PAGE_URL)
    page.open()
    page.filter_by_type()
    page.go_to_hamster_list()
    time.sleep(3)
    browser.save_screenshot('/Users/anastasiya.niadbailik/Automation/Selenium_UI_Pets/screenshots/filters_hamster.png')


@pytest.mark.smoke
def test_filter_pet_by_type(browser):
    page = MainPage(browser, MainPageData.MAIN_PAGE_URL)
    page.open()
    page.filter_by_type()
    page.go_to_reptile_list()
    time.sleep(3)
    browser.save_screenshot('/Users/anastasiya.niadbailik/Automation/Selenium_UI_Pets/screenshots/filters_rept.png')


@pytest.mark.smoke
def test_filter_by_pet_name(browser):
    page = MainPage(browser, MainPageData.MAIN_PAGE_URL)
    page.open()
    page.filter_by_name()
    time.sleep(3)
    browser.save_screenshot('/Users/anastasiya.niadbailik/Automation/Selenium_UI_Pets/screenshots/filter_by_name.png')


@pytest.mark.smoke
def test_pet_detail(browser):
    page = MainPage(browser, MainPageData.MAIN_PAGE_URL)
    page.open()
    page.go_to_details()
    time.sleep(2)
    browser.save_screenshot('/Users/anastasiya.niadbailik/Automation/Selenium_UI_Pets/screenshots/pet_details.png')


@pytest.mark.smoke
def test_like(browser):
    page = MainPage(browser, MainPageData.MAIN_PAGE_URL)
    page.open()
    page.like_pet()
    time.sleep(2)
    browser.save_screenshot('/Users/anastasiya.niadbailik/Automation/Selenium_UI_Pets/screenshots/like_pet_after.png')


@pytest.mark.skip
def test_unlike(browser):
    page = MainPage(browser, MainPageData.MAIN_PAGE_URL)
    page.open()
    page.like_pet()
    time.sleep(2)
    browser.save_screenshot('/Users/anastasiya.niadbailik/Automation/Selenium_UI_Pets/screenshots/unlike_pet_after.png')


@pytest.mark.regression
def test_go_to_last_page(browser):
    page = MainPage(browser, MainPageData.MAIN_PAGE_URL)
    page.open()
    time.sleep(3)
    page.go_to_last_page()
    time.sleep(2)


@pytest.mark.regression
def test_go_to_next_page(browser):
    page = MainPage(browser, MainPageData.MAIN_PAGE_URL)
    page.open()
    time.sleep(1)
    page.go_to_next_page()
    time.sleep(2)
