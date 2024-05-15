from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time
 
url = 'http://localhost:4721'

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}

######## test for sms


time.sleep(3)
def check_for_send_verify_code_to_another_telegram_sesseion(driver_SamsungA71):
    time.sleep(5)
    touch = TouchAction(driver_SamsungA71)
    try:
        AnothertelegramFOrVerifyCode  = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.TextView[@text="Check your Telegram messages"]')
        if AnothertelegramFOrVerifyCode:
            BackButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.ImageView[@content-desc="Back"]')
            BackButton.click()
            time.sleep(2)

            editnumberbuttun = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.TextView[@text="Edit"]')
            editnumberbuttun.click()
            time.sleep(2)
            backspaceButtonInKeybord = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.view.ViewGroup/android.widget.ImageView')
            touch.long_press(backspaceButtonInKeybord).release().perform()
            
    except:
        print('another telegram for verify code not found')