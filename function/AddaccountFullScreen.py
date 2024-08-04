import sys, time
sys.path.append("../TelegramAuto")

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from function.AddTelegramAccount import AddAccount


def AddAccountFullScreen(driver):
    time.sleep(2)
    
    driver.implicitly_wait(15)
    AddTelegramAccount = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.TextView[@text="Add Telegram account"]')
    if AddTelegramAccount :
        driver.implicitly_wait(15)
        closeButton = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.ImageView[@content-desc="Close"]')
        closeButton.click()
        # LoginTelegram = driver.find_element(by=AppiumBy.XPATH,
        #             value='//android.widget.Button[@text="Login to Telegram"]')
        # LoginTelegram.click()
        # AddAccount(driver)
            
   
      