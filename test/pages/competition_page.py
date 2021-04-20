'''
    Competition Page class
'''


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_pages import BasePage

class CompetitionPage(BasePage):
    # LOCATORS
    target_word_loc = "#row1 > span.highlight"
    input_fld = "inputfield"

    # SPECIAL INPUT
    input_space_key = "\ue00d"

    def __init__(self, driver, url=''):
        super().__init__(driver)
        self.url = url

    def set_url(self, url):
        self.url = url
    
    def get_text(self, ):
        pass

    def type_word(target_word):
        pass