import time
#import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#This will initialize the WebDriver
driver = webdriver.Chrome()

#Open a webpage and open up multiple tabs
driver.get("https://www.google.com")

i = 0
while i < 200:
    driver.switch_to.new_window('tab') 
    driver.get("https://giphy.com/gifs/math-lady-meme-WRQBXSCnEFJIuxktnw")
    i += 1


#Webdriver closes once the action of using driver.get is completed, or perhaps any action for that matter.
time.sleep(1000)

