from datetime import datetime
current_datetime = datetime.now()


class RegisterPageData:
    REGISTER_PAGE_URL = 'http://34.141.58.52:8080/#/register'
    # LOGIN = 'tests2@pets.com' #для одного аккаунта
    # LOGIN = 'anastasiya.niadbailik+autotest2@gmail.com'
    LOGIN = f'anastasiya.niadbailik+{current_datetime.microsecond}@gmail.com' #для всех последующих аккаунтов
    PASS = 'fhfurbd4547474@!@!'


class LoginPageData:
    LOGIN_PAGE_URL = 'http://34.141.58.52:8080/#/login'
    VALID_EMAIL = 'anastasiya.niadbailik+autotest2@gmail.com'
    VALID_EMAILS = ['anastasiya.niadbailik+autotest2@gmail.com', 'tests2@pets.com']
    VALID_PASS = 'fhfurbd4547474@!@!'
    INVALID_PASS = ['12345', 'password']
    INVALID_EMAILS = ['qwerty@pet.com', 'qwertyu@pet.com']
    INCORRECT_EMAILS = ['tests.tests.net', 'tut@com']


class MainPageData:
    MAIN_PAGE_URL = 'http://34.141.58.52:8080/#/'
    PET_NAME = "Lea"


class ProfilePageData:
    PROFILE_PAGE_URL = 'http://34.141.58.52:8080/#/profile'


class NewPetData:
    NEW_PET_PAGE_URL = 'http://34.141.58.52:8080/#/pet-new/pet'
    NEW_PET_POST = 'http://34.141.58.52:8000/pets'
    NEW_PET_NAME = 'Lea'
    PET_NAME = 'Sunny'
    PET_AGE = "3"
    NEW_PET_AGE = '5'
    NEW_IMG_LINK = r"/Users/anastasiya.niadbailik/Automation/Selenium_UI_Pets/images_for_tests/hamster2.png"
    IMG_LINK = r"/Users/anastasiya.niadbailik/Automation/Selenium_UI_Pets/images_for_tests/sad-hamster.png"


class PetEditPage:
    PET_EDIT_URL = 'http://34.141.58.52:8080/#/pet-edit/%'
