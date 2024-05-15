# from _ast import expr
# import requests
import json
from appium import webdriver
from typing import Any, Dict, sys
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time
sys.path.append("../TelegramAuto")
from function.GetNumberAndGetCodeApi import GetVerifycode

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

def Check_Verify_code(driver_SamsungA71, phonNumber, activationId):
    
    print("check verify start")
    try:
        time.sleep(1)
        GetCodeInSms = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//*[starts-with(@text, "We’ve sent an SMS with an activation code to")]')

        if GetCodeInSms:
            print("Start Get code")
            time.sleep(5)
            VerifycodeInputBox = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]')
            time.sleep(12)
            verificationcodeTel = GetVerifycode(activationId)
            if len(verificationcodeTel) > 0 : 
                time.sleep(2)
                VerifycodeInputBox.send_keys(verificationcodeTel)
                time.sleep(5)
                
                print(verificationcodeTel)
                return True
        else : 
            return False
    except:
        print('Send Sms Not found')
        return False

# Check_Verify_code()