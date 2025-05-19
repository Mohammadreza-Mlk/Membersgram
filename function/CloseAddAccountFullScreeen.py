import sys, time
sys.path.append("../TelegramAuto")

from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from function.AddTelegramAccount import AddAccount
from watchlog import Watchlog
watchlog_instance = Watchlog()
from function.result import log_test_result

def CloseAddAccountFullScreeen(driver):
    try:
               
        driver.implicitly_wait(15)
        AddTelegramAccount = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Add Telegram account"]')
        if AddTelegramAccount :
            driver.implicitly_wait(15)
            closeButton = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.ImageView[@content-desc="Close"]')
            closeButton.click()
            time.sleep(1)
            # watchlog_instance.increment('AddAccountFullScreen')
            log_test_result("Add account dialog fulscreen", "pass")
        else:
            log_test_result("Add account dialog fulscreen", "failed")
    
    except:
        print("AddAcoount not  found")