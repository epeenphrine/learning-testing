
#%%
## selenium imports 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# this setting works for indeed job application
firefox_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
gecko_driver_path= "C:\\Users\\dong\\Desktop\\repo\\learning_testing\\selenium\\geckodriver.exe"
options = webdriver.FirefoxOptions()
options.binary_location = firefox_path 
options.set_preference("useAutomationExtension", False)
options.set_preference("dom.webdriver.enabled", False)
driver = webdriver.Firefox(options=options, executable_path=gecko_driver_path)