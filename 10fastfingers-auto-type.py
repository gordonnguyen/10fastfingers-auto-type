from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URLS
SIGNIN_URL = "https://10fastfingers.com/login"

# ELEMENTS SELECTORS
USERNAME_ID = "UserEmail"
PASSWORD_ID = "UserPassword"
LOGIN_BTN_ID = "login-form-submit"
TARGET_WORD_SLTCR = "#row1 > span.highlight"
INPUT_FIELD_ID = "inputfield"

# SPECIAL TYPE INPUT
SPACE_KEY = "\ue00d"


def main():
    # Initilize settings from .ini
    setting = read_ini_settings()
    use_account = setting['use_account']
    word_per_sec = float(setting['word_per_sec'])
    typing_test_url = setting['typing_test_url']
    extract_text_to_file = setting['extract_text_to_file']
    num_test_loop = int(setting['num_test_loop'])
    extracted_text = ''
    
    # Sign in
    driver = webdriver.Chrome()
    if use_account:
        sign_in(driver, setting)
    else:
        print("Playing anonymously...")

    # Find text and type
    for i in range(num_test_loop):
        driver.get(typing_test_url)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, TARGET_WORD_SLTCR)))
        print("YAY! It's typing...")

        while True:
            target_word = driver.find_element_by_css_selector(TARGET_WORD_SLTCR).text
            if target_word != '':
                type_word(target_word, driver)
                print(target_word, end=' ')
                if extract_text_to_file:
                    extracted_text += target_word
                time.sleep(word_per_sec)
            else:
                break

    if extract_text_to_file:
        with open('competition_text_file.txt', 'w') as text_f:
            text_f.write(extracted_text+' ')

    print("\nALL DONE! Check your browser for results!")

    # Retain browser for viewing
    while True:
        pass

def type_word(target_word, driver):
    driver.find_element_by_id(INPUT_FIELD_ID).send_keys(target_word+SPACE_KEY)

def sign_in(driver, setting):
    email = setting['email']
    password = setting['password']

    driver.get(SIGNIN_URL)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID,USERNAME_ID)))
    driver.find_element_by_id(USERNAME_ID).send_keys(email)
    driver.find_element_by_id(PASSWORD_ID).send_keys(password)
    driver.find_element_by_id(LOGIN_BTN_ID).click()
    WebDriverWait(driver, 15).until(EC.url_changes(SIGNIN_URL))

    print('Sign in successfully!')

def read_ini_settings():
    setting_temp = []
    setting = {}
    pair_num = 2
    file_key_value_sep = ' = ' 

    with open('setting.ini') as f:
        for item in f:
            if not (item.startswith('#') or item.startswith('\n')):
                setting_temp.append(item.strip().split(file_key_value_sep))  # Will result with a 2D list

        for x in range(len(setting_temp)):
            for y in range(pair_num-1):
                key = setting_temp[x][y]
                value = setting_temp[x][y+1]
                if value == 'True':
                    value == True
                setting[key] = value
        print(setting)

    return setting
        
main()