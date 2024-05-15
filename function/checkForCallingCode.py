from _ast import expr
import requests
import json
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time
import random
url = 'http://localhost:4721'

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}



def check_For_Calling_Code(driver_SamsungA71):
    
    try:
        print("start check_For_Calling_Code")
        time.sleep(2)
        GetCodeInCall = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//*[starts-with(@text, "Calling")]')
        
        if GetCodeInCall:
            time.sleep(4)
            CallinYourPhone = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//*[starts-with(@text, "Calling your phone")]')
            
            time.sleep(6)
            if CallinYourPhone :
                print("CallinYourPhone is true")
                print("wait 75 sec")
                
                time.sleep(50)
                GetCodeInSms = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.TextView[@text="Get the code via SMS"]')
                
                print("Get the code via SMS Found")
                time.sleep(6)
                print("GetCodeInSms click")
                GetCodeInSms.click()
    except:
        print('Calling not found')
# check_For_Calling_Code()