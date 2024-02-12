import time
import platform
import sys
import comtypes
import math
import os
if "macOS" in platform.platform():
    import osascript


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


#This portion of code will lock the workstation
import ctypes
#lock_ws = ctypes.windll.user32.LockWorkStation()

#This portion of code focuses on importing Windows related modules
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


#This portion of code is for initializing windows audio functionality
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))


#This reassigned the webdriver.Chrome() function to "driver"
driver = webdriver.Chrome()





#Open a webpage and open up multiple tabs
driver.get("https://www.google.com")

i = 0
while i < 100:
    driver.switch_to.new_window('tab') 
    driver.get("https://www.google.com")
    volume.SetMasterVolumeLevelScalar(1.0, None)
    time.sleep(0.5)
    i += 1


#This will check if macOS & Windows are found in the platform.platform(), if not the program will not run.
#This will then check if macOS and Window is found in platform.platform(). 
#If the statement is true, it will run the commands within the if statements.
#if "macOS" in platform.platform():
#        osascript.osascript("set volume output volume 100")

#The range here goes from -65.0 to 0. Anything higher than 0 or lower than -65.0 will produce an error.




#This will lock the workstation
lock_ws()
#Webdriver closes once the action of using driver.get is completed, or perhaps any action for that matter; so here we use time.sleep()
time.sleep(1000)