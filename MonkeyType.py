import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time

load_dotenv()

PATH = "./cd/chromedriver"
service = Service(PATH)
driver = webdriver.Chrome(service=service)
driver.get("https://monkeytype.com/")
print(driver.title)

assert 'Monkeytype' in driver.title


element = driver.find_element(By.TAG_NAME, 'body') 
touch = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[text()="accept all"]'))
)
touch.click()

login = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/header/nav/a[4]'))
)
login.click()


github = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="pageLogin"]/div[4]/div[2]/button[2]'))
)
github.click()


# LOGIN TO GITHUB
time.sleep(2)
driver.switch_to.window(driver.window_handles[-1])

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.TAG_NAME, 'body'))
)

login_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'login_field'))
)
login_input.send_keys(os.getenv('LOGIN_ID'))

password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'password'))
)
password_input.send_keys(os.getenv('LOGIN_PASSWORD'))

signin = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="login"]/div[3]/form/div/input[13]'))
)
signin.click()


# CHANGING TO GAME WINDOW
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
title = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="logo"]'))
)
title.click()


# GAME
time.sleep(2)
words_input = driver.find_element(By.ID, 'wordsInput')

while True:
    try:
        active_word = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="word active"]'))
        )
        words_input.send_keys(active_word.text + " ")
        time.sleep(0.5)
    except Exception as e:
        break

input("Press Enter to quit")
driver.quit()