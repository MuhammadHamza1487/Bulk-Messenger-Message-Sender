import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


file_path = 'data.xlsx'
data = pd.read_excel(file_path)

options = webdriver.ChromeOptions()
user_data_dir = r"C:\Users\James' PC\AppData\Local\Google\Chrome\User Data"
profile_dir = 'Default'
options.add_argument(f"--user-data-dir={user_data_dir}")
options.add_argument(f"--profile-directory={profile_dir}")
options.add_argument("--start-maximized")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--disable-extensions")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-infobars")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def send_message(page_link, message):
    try:
        driver.get(page_link)
        time.sleep(5)

        message_button = driver.find_element(By.XPATH, "//span[text()='Message' and contains(@class, 'x1lliihq')]")
        message_button.click()
        time.sleep(2)

        message_input = driver.find_element(By.XPATH, "//div[@aria-label='Message' and @role='textbox']")
        message_input.send_keys(message)
        time.sleep(2)

        send_button = driver.find_element(By.XPATH, "//div[@aria-label='Press enter to send' and @role='button']")
        send_button.click()
        time.sleep(2)

        print(f"Message sent to {page_link}")

    except Exception as e:
        print(f"Failed to send message to {page_link}: {e}")
        driver.save_screenshot(f'error_{index}.png')

for index, row in data.iterrows():
    page_link = row['Profile Link']
    message = row['Message']
    send_message(page_link, message)

driver.quit()
