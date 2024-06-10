from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import sys, time
sys.path.append("../TelegramAuto")
url = 'http://localhost:4721'

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'}

# driver_SamsungA71 = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

def check_For_Calling_Code(driver_SamsungA71):
    
    try:
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
            print("wait 100 sec")
            
            time.sleep(100)
            print("start to finde get the code via sms")
            try:
                time.sleep(10)
                
                GetCodeInSms = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.TextView[@text="Get the code via SMS"]')
                
                print("Get the code via SMS Found")
                if GetCodeInSms:
                    time.sleep(2)
                    print("GetCodeInSms click")
                    GetCodeInSms.click()
                    
                    touch = TouchAction(driver_SamsungA71)
                    print("x, y  click")
                    touch.tap(x=500, y=1650).release().perform()
                else:
                    
                    time.sleep(4)
                    touch.tap(x=499, y= 1649).release().perform()
      
            except:
                print("code via sms not found")
            print("x, y  click2")
            time.sleep(2)
            touch.long_press(x=500, y=1650).release().perform()
            print("x, y  long preess done")
            time.sleep(10)
            
            GetCodeInSms = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                        value='//android.widget.TextView[@text="Get the code via SMS"]')
            
            print("Get the code via SMS Found")
            time.sleep(2)
            print("GetCodeInSms click")
            GetCodeInSms.click()
                
    except:
        print('Calling not found')
# check_For_Calling_Code()