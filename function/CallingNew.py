from typing import Any, Dict
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import sys, time, requests

sys.path.append("../TelegramAuto")
from function.UnistallApp import UnistalTelegram
from function.installTelegram import InstallTelegram

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}
url = 'http://localhost:4721'

def Calling(driver_SamsungA71, activationId):
    try:
        touch = TouchAction(driver_SamsungA71)  
        print("start check_For_Calling_Code")
        time.sleep(6)
        GetCodeInCall = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//*[starts-with(@text, "Calling")]')
        time.sleep(4)
        CallinYourPhone = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//*[starts-with(@text, "Calling your phone")]')
        
        if GetCodeInCall or CallinYourPhone:
                        
            time.sleep(6)
            
            print("CallinYourPhone is true")
            
            headers = {'activationId': f'{activationId}'}
            print(activationId)
            # print("2 minute to cancell number :")
            
            
            driver_SamsungA71.press_keycode(3)
            time.sleep(3)
            UnistalTelegram(driver_SamsungA71)
            # time.sleep(120)
            # CancelBuyPoneNumberApi = 'https://fotorplusapi.membersgram.com/cancelPurchase'
            # CancelBuyRequest = requests.get(CancelBuyPoneNumberApi, headers=headers)
            # print(CancelBuyRequest.text)
            time.sleep(5)
            InstallTelegram(driver_SamsungA71)

            return True
        return False


    except:
        print("Calling to code not found")