'''
    Super classes for Page object
    Serve as a base template for page 
    automating functions with selenium
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.best_buy.locators import Locators
from utils.best_buy import urls

class BasePage():
    
    # Initialize browser
    def __init__(self, driver):
        self.driver = driver

    # Wait for element to be clickable and click
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    # Select element in webpage and fill text
    def enter_text(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # Check if the current url is correct to use for this object
    def is_correct_url(self, target_url):
        if self.driver.current_url == target_url:
            return True
        else:
            return False

class SignInPage(BasePage):

    def __init__(self, email, password):
        super().__init__()
        self.url = urls.sign_in
        self.email = email
        self.password = password

    def sign_in(self, driver):
        # Fill email and password fields
        self.enter_text(Locators.SignInPage.email_fld, self.email)
        self.enter_text(Locators.SignInPage.password_fld, self.password)

        # Submit / Signin button
        driver.find_element_by_class_name(self.BB_signin_selector).click()
        WebDriverWait(driver, 10).until(EC.url_changes(self.driver.current_url))
        #WebDriverWait(driver, 10).until(EC.url_changes(current_signin_url))