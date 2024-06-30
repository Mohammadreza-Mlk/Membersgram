from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import sys, time
sys.path.append("../TelegramAuto")

from function.GetNumberAndGetCodeApi import GetVerifycode
from function.UnistallApp import UnistalTelegram
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
        time.sleep(5)
        GetCodeInSms = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//*[starts-with(@text, "We’ve sent an SMS with an activation code to")]')
        time.sleep(2)
        if GetCodeInSms:
            print("Start Get code")
            time.sleep(5)
            VerifycodeInputBox = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]')
            time.sleep(2)
            verificationcodeTel = GetVerifycode(activationId, driver_SamsungA71)
            if len(verificationcodeTel) > 0 : 
                time.sleep(2)
                VerifycodeInputBox.send_keys(verificationcodeTel)
                
                return True
        else : 
            UnistalTelegram(driver_SamsungA71)
            return False
    except:
        print('Send Sms Not found')
        return False

# Check_Verify_code()