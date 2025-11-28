import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import time

load_dotenv()

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://monkeytype.com/")
print(driver.title)

assert 'Monkeytype' in driver.title


element = driver.find_element(By.TAG_NAME, 'body') 
touch = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[text()="accept all"]'))
)
touch.click()

# Find login button - try multiple strategies
login = None
loginStrategies = [
    (By.XPATH, '/html/body/div[11]/header/nav/a[5]'),  # Current correct path
    (By.XPATH, '//*[@id="app"]/header/nav/a[4]'),  # Previous path
    (By.XPATH, '//a[contains(@href, "login") or contains(text(), "login")]'),
    (By.XPATH, '//nav//a[contains(text(), "Login") or contains(text(), "login")]'),
    (By.CSS_SELECTOR, 'nav a[href*="login"]'),
]

for i, strategy in enumerate(loginStrategies):
    try:
        login = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(strategy)
        )
        print(f"Found login button using strategy {i+1}")
        break
    except Exception:
        continue

if not login:
    raise Exception("Could not find login button. The page structure may have changed.")
login.click()

# Wait for login page to load
time.sleep(1)

# Find GitHub button - try multiple strategies
github = None
githubStrategies = [
    (By.XPATH, '//button[contains(text(), "GitHub") or contains(text(), "github")]'),
    (By.XPATH, '//button[contains(@class, "github") or contains(@class, "GitHub")]'),
    (By.XPATH, '//*[@id="pageLogin"]//button[contains(text(), "GitHub")]'),
    (By.XPATH, '//button[contains(., "GitHub")]'),
    (By.XPATH, '//*[@id="pageLogin"]/div[4]/div[2]/button[2]'),  # Original fallback
    (By.XPATH, '//button[contains(@aria-label, "GitHub")]'),
    (By.XPATH, '//a[contains(@href, "github")]//button | //button[ancestor::a[contains(@href, "github")]]'),
]

for i, strategy in enumerate(githubStrategies):
    try:
        github = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(strategy)
        )
        print(f"Found GitHub button using strategy {i+1}")
        break
    except Exception:
        continue

if not github:
    raise Exception("Could not find GitHub login button. The page structure may have changed.")
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

# Find GitHub signin button - try multiple strategies
signin = None
signinStrategies = [
    (By.XPATH, '//input[@type="submit" and contains(@value, "Sign in")]'),
    (By.XPATH, '//input[@name="commit"]'),
    (By.XPATH, '//button[contains(text(), "Sign in")]'),
    (By.XPATH, '//*[@id="login"]//input[@type="submit"]'),
    (By.XPATH, '//*[@id="login"]/div[3]/form/div/input[13]'),  # Original fallback
    (By.XPATH, '//form//input[@type="submit"]'),
    (By.CSS_SELECTOR, 'input[type="submit"][value*="Sign"]'),
    (By.CSS_SELECTOR, 'input[name="commit"]'),
]

for i, strategy in enumerate(signinStrategies):
    try:
        signin = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(strategy)
        )
        print(f"Found GitHub signin button using strategy {i+1}")
        break
    except Exception:
        continue

if not signin:
    raise Exception("Could not find GitHub signin button. The page structure may have changed.")
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