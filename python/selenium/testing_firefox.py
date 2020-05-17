
#%%
## selenium imports 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os
import platform
## make secrets.py with variable username and password 
if os.path.exists("secrets.py"):
    import secrets 
    username = secrets.username
    password = secrets.password
else: 
    print("no secrets provided")
print(platform.system())

if str(platform.system()) == "Linux":
    print(f"running on {platform.system()}")
    gecko_driver_path = "./geckodriver"

elif str(platform.system()) == "Windows":
    print(f"running on {platform.system()}")
    gecko_driver_path = "./geckodriver.exe"
else: 
    print("are you using a mac?")

# this setting works for indeed job application

#firefox_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"

gecko_driver_path = "./geckodriver"
options = webdriver.FirefoxOptions()

#options.binary_location = firefox_path
## !!!important setting for botting!!!

options.set_preference("useAutomationExtension", False)
options.set_preference("dom.webdriver.enabled", False)

driver = webdriver.Firefox(options=options, executable_path=gecko_driver_path)
## wait 2 seconds
wait = WebDriverWait(driver, 4)
# %% loggin in 
login_page = "https://secure.indeed.com/account/login?hl=en_US&co=US&continue=https%3A%2F%2Fwww.indeed.com%2Fjobs%3Fq%3Dsoftware%2Bdeveloper%26l%3DStaten%2BIsland%252C%2BNY&tmpl=desktop&service=my&from=gnav-util-jobsearch--jasx&_ga=2.240860416.2019939741.1589031436-1268019068.1589031436"
driver.get(login_page)
#%%
google_login_button = driver.find_element_by_xpath('//*[@id="login-google-button"]')
google_login_button.click()

#%% selecting login window
base_window = driver.window_handles[0]
print(driver.window_handles)
driver.switch_to_window(driver.window_handles[1])
#%% input fields
time.sleep(2)
select_username = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
select_username.send_keys(username)
select_username.send_keys(Keys.ENTER)
time.sleep(2)
## password field selection / keyboard input
## need timeout so that the password field render before selecting it 
select_password = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
select_password.send_keys(password)
## press ENTER key 
select_password.send_keys(Keys.ENTER)
driver.switch_to_window(driver.window_handles[0])

# %%
