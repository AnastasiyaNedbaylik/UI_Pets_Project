from selenium.webdriver.common.by import By


class LoginPageLocator:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BUTTON = (By.CLASS_NAME, "p-button-label")
    SUCCESS_LOGIN_SIGN = (By.CSS_SELECTOR, ".pi-plus")
    INVALID_EMAIL_LOGIN_WARNING = (By.XPATH, '//*[@id="pv_id_2_content"]/div/div')
    WRONG_MESSAGE = (By.CSS_SELECTOR, '#pv_id_2_content > div > div > div')
    VALIDATION_FIELD_IS_EMAIL = (By.CSS_SELECTOR, "#pv_id_2_content > div > form > div:nth-child(1) > div")
    VALIDATION_FIELD_IS_REQUIRED = (By.CLASS_NAME, 'text-red-500')