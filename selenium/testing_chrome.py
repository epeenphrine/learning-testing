#%%
## selenium imports 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
chrome_driver_path = "C:/Users/dong/Desktop/repo/learning_testing/selenium/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.binary_location = chrome_path
options.add_argument("C:/Users/dong/AppData/Local/Google/Chrome/User Data/Default")
driver = webdriver.Chrome(options=options, executable_path=chrome_driver_path)

#%% login
driver.get("https://secure.indeed.com/account/login?hl=en_US&co=US&service=my&from=gnav-util-jobsearch--jasx")

select_google_button = driver.find_element_by_xpath('//*[@id="login-google-button"]')
select_google_button.click()
## browser window handle. Tell selenium which window to use in multi window scenario
base_window = driver.window_handles[0]
print(driver.window_handles)
driver.switch_to_window(driver.window_handles[1])
## email field selection / keyboard input
select_username = driver.find_element_by_xpath('//*[@id="identifierId"]')
select_username.send_keys("")
select_username.send_keys(Keys.ENTER)
## password field selection / keyboard input
## need timeout so that the password field render before selecting it 
driver.implicitly_wait(5) 
select_password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
select_password.send_keys("")
## press ENTER key 
select_password.send_keys(Keys.ENTER)
driver.switch_to_window(driver.window_handles[0])
# %% job page
driver.get("https://www.indeed.com/viewjob?adid=139594145&cmp=Rustik-Tavern&from=iaBackPress&jk=88c6564cfb0d2797&pub=4a1b367933fd867b19b072952f68dceb&sjdu=QwrRXKrqZ3CNX5W-O9jEvcyjzvCBAsZ0BtjoMkcy3uUNu6xem00KSJhNGu-XwWmElug-cTG16ui2oASVaDt7rQTuorx8s5wYHRDhJ5peePo&t=Recipe%20Developer&tk=1e7n5tahd34vl000&vjs=3")
