from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
from function.installTelegram import InstallTelegram

from typing import sys
sys.path.append("../TelegramAuto")


from function.UnistallApp import UnistalTelegram
# from function.GetNumberAndGetCodeApi import GetNumberApi
import time

def LogOut(driver_SamsungA71):
    touch = TouchAction(driver_SamsungA71)  
    try: #log out from account
        
        NavigationMenu = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.ImageView[@content-desc="Open navigation menu"]')
        NavigationMenu.click()
        time.sleep(2)
        touch.tap(x=260, y=1360).release().perform()
        time.sleep(2)
        
        CircleForOpenMenu = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.ImageButton[@content-desc="More options"]/android.widget.ImageView')
        CircleForOpenMenu.click()
        time.sleep(2)
        LogOutInMenu = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                        value='//android.widget.TextView[@text="Log Out"]')
        time.sleep(2)
        LogOutInMenu.click()
        time.sleep(2)
        LogOutInMenu2 = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='(//android.widget.TextView[@text="Log Out"])[2]')
        LogOutInMenu2.click()
        time.sleep(2)
        LogOutInDialogBOx = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='(//android.widget.TextView[@text="Log Out"])[2]')
        LogOutInDialogBOx.click()
        print('sendin number to fotor is ✅✅✅✅')
        time.sleep(2)
                       
        driver_SamsungA71.press_keycode(3)
           
        time.sleep(2)
         
        UnistalTelegram(driver_SamsungA71)
        print("ok")
        time.sleep(20)
        InstallTelegram(driver_SamsungA71)
   
    except:
        print('Log out not found')