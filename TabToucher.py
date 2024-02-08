import ctypes
import time
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#This will initialize the WebDriver
driver = webdriver.Chrome()

#Open a webpage
driver.get("https://www.google.com")
#driver.refresh() 
#driver.back()  
#driver.forward() 
#driver.quit()

