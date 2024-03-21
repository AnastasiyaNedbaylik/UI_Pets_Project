from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_PAGE_LINK = (By.XPATH, '//*[@id="app"]/header/div/ul/li[1]')
    PROFILE_PAGE_LINK2 = (By.XPATH, '//span[2]')
    MAIN_PAGE_LINK = (By.XPATH, '//*[@id="app"]/header/div/div')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".p-toast-message-text")
    PET_ADDING_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/div[1]/div/div[1]/button/span[1]')
    PET_EDIT_BUTTON = (By.XPATH, "//div[5]/div/div[2]/button/span[2]")
    PET_DELETE_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[1]/div/div[2]/button[2]')
    PET_DELETE_CONFIRM_BUTTON_YES = (By.XPATH, "/html/body/div[3]/div[2]/button[2]")
    PET_PROFILE_SAVING = (By.XPATH, "//span[contains(.,'Save')]")
    PET_POP_UP = (By.CSS_SELECTOR, 'html > body > div:nth-of-type(2) > div > div > div')
    PET_LIST = (By.CSS_SELECTOR, ".col-12")
    ADDED_PET = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[5]')
    SITE_LOGO = (By.XPATH, '//*[@id="app"]/header/div/div')
    QUIT_BTN = (By.CSS_SELECTOR, 'li:nth-child(2) a:nth-child(1)')
    DELITE_PROFILE_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]')


class AddPetsLocators:
    ADD_PET_NAME = (By.ID, "name")
    ADD_PET_TYPE = (By.ID, "typeSelector")
    SELECT_PET_TYPE = (By.XPATH, "//li[4]")
    ADD_PET_AGE = (By.XPATH, "//span[@id='age']/input")
    ADD_PET_GENDER = (By.ID, "genderSelector")
    SELECT_PET_GENDER = (By.XPATH, "//div[3]/div/ul/li")
    SELECT_PET_GENDER_FEMALE = (By.XPATH, '/html/body/div[3]/div/ul/li[2]')
    PET_SUBMIT_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[1]')
    PET_CHOOSE_INPUT = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div[2]/div/span/input')
    PET_CHOOSE_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div[2]/div/span')


class EditPetLocators:
    # PET_NAME = (By.CSS_SELECTOR, '#name')
    PET_NAME = (By.ID, 'name')
    # PET_NAME = (By.XPATH, '/html/body/div[1]/main/div/form/div/div[2]/div[2]/div[2]/div[1]/input')
    IMAGE_INPUT = (By.XPATH, '//*[@id="app"]/main/div/form/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/span/input')
    IMAGE_CHOOSE_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/form/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/span')


