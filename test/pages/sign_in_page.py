'''
    Login Page class
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_pages import BasePage

class LoginPage(BasePage):
    # DEFAULT URL
    url = 'https://10fastfingers.com/login'

    # LOCATORS
    username_fld = (By.ID, "UserEmail")
    password_fld = (By.ID, "UserPassword")
    signin_btn = (By.ID, "login-form-submit")

    def __init__(self, email='', password=''):
        super().__init__()
        self.__email = email
        self.__password = password

    def set_account(self, email, password):
        self.__email = email
        self.__password = password

    def sign_in(self, driver):
        # Fill email and password fields
        self.enter_text(self.username_fld, self.__email)
        self.enter_text(self.password_fld, self.__password)

        # Submit / Signin button
        driver.find_element(self.signin_btn).click()
        WebDriverWait(driver, 10).until(EC.url_changes(self.driver.current_url))