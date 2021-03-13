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

# OTHERS
LINE = '<>'*20
WORDS_PER_LINE = 12
RESULT_VIEWING_TIME = 15
FINAL_VIEWING_TIME = 60*60  # 1 hour

def main():
    # Initilize settings
    setting = read_ini_settings()
    typing_test_url = setting['typing_test_url']
    use_account = setting['use_account']
    word_per_sec = float(setting['word_per_sec'])
    num_test_loop = int(setting['num_test_loop'])
    extract_text_to_file = setting['extract_text_to_file']
    extracted_text = ''
    driver = webdriver.Chrome()

    # Sign in
    if use_account == True:
        sign_in(driver, setting)
    else:
        print(LINE+"\nPlaying anonymously...")

    # Get text and type
    for i in range(num_test_loop):
        word_count = 0
        driver.get(typing_test_url)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, TARGET_WORD_SLTCR)))
        print("\nYAY! It's typing... "+LINE)
        
        while True:
            target_word = driver.find_element_by_css_selector(TARGET_WORD_SLTCR).text
            if target_word != '':
                type_word(target_word, driver)
                if extract_text_to_file == True:
                    word_count += 1
                    extracted_text = accumulate_words(target_word, word_count, extracted_text)
                time.sleep(word_per_sec)
            else:
                time.sleep(RESULT_VIEWING_TIME)
                break

    # extract words from test to file
    if extract_text_to_file:
        with open('competition_text_file.txt', 'w') as text_f:
            text_f.write(extracted_text)

    print('\n'+LINE+"\nALL DONE! Check your browser for results!")

    # Retain browser for viewing
    time.sleep(FINAL_VIEWING_TIME)

def read_ini_settings():
    setting_temp = []
    setting = {}
    num_of_value = 1
    seperate_symbol = '=' 

    # Open and read setting.ini
    with open('setting.ini') as f:
        for item in f:
            if not (item.startswith('#') or item.startswith('\n')):
                setting_temp.append(item.split(seperate_symbol))  # Will result with a 2D list

    # Convert setting list to dictionary
        for x in range(len(setting_temp)):
            for y in range(num_of_value):
                key = setting_temp[x][y].strip()
                value = setting_temp[x][y+1].strip()
                if value.lower() == 'true':
                    value = True
                setting[key] = value
    return setting

def sign_in(driver, setting):
    email = setting['email']
    password = setting['password']

    # Fill text fields with account info
    driver.get(SIGNIN_URL)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID,USERNAME_ID)))
    driver.find_element_by_id(USERNAME_ID).send_keys(email)
    driver.find_element_by_id(PASSWORD_ID).send_keys(password)
    
    # Try logging in
    driver.find_element_by_id(LOGIN_BTN_ID).click()
    try:
        WebDriverWait(driver, 15).until(EC.url_changes(SIGNIN_URL))
    except:
        print('Unable to sign in! Playing anonymously...')
    else:
        print('Sign in successfully!')

def type_word(target_word, driver):
    driver.find_element_by_id(INPUT_FIELD_ID).send_keys(target_word+SPACE_KEY)

def accumulate_words(target_word, word_count, extracted_text):
    if word_count % WORDS_PER_LINE == 0:
        extracted_text += target_word + '\n'
    else:
        extracted_text += target_word+' '
    return extracted_text

main()