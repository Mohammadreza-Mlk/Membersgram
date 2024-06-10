import time
from appium import webdriver
from typing import Any, Dict, sys
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

# from devices.A71New import url, cap
url = 'http://localhost:4721'

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}
 
def TooManyAttempts(driver_SamsungA71):
    touch = TouchAction(driver_SamsungA71)

    try:
        
            
        time.sleep(2)
        TooManyAttemptsText = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                        value='//android.widget.TextView[@text="Too many attempts, please try again later."]') 
        if TooManyAttemptsText:
            time.sleep(2)
            OkButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                        value='//android.widget.TextView[@text="OK"]')
            OkButton.click()
            driver_SamsungA71.press_keycode(3)
            time.sleep(2)
            
        
        touch.long_press(x=405, y=295).release().perform()
        time.sleep(2)
        
        Unistall = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.FrameLayout[@content-desc="Uninstall, Button"]/android.widget.LinearLayout')
    
        Unistall.click()
        confirmUninstall = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.Button[@resource-id="android:id/button1"]')
        confirmUninstall.click()
    except:
        print('TooManyAttempts not found')
        
