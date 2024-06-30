import random,time
from typing import Any, Dict
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time, random

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}
url = 'http://localhost:4721'

driver_SamsungA71 = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

def RandomName(driver_SamsungA71):
    touch = TouchAction(driver_SamsungA71)

    try: 
        global Account_names
        Account_names = ["Testpnx5", "Testpnx6", "Testpnx7", "Testpnx8", "Testpnx9", "Testpnx10"]

        time.sleep(3)
        for i in range(5):
    # استخراج عنصر iام از آرایه
            account_name = Account_names[i]
            print(f"Account Name: {account_name}")
            
            # توقف به مدت 3 ثانیه
            time.sleep(3)
            
            
            time.sleep(4)
            SearchButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                                    value='//android.widget.ImageButton[@content-desc="Search"]/android.widget.ImageView')
            SearchButton.click()
            time.sleep(4)
            SearchInput = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                                    value='//android.widget.EditText[@text="Search"]')


            SearchInput.send_keys(account_name)
            time.sleep(2)
            print("12")
            touch.tap(x=400, y=840).release().perform()
            time.sleep(1)
            print("12")
           
            JoinButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                                    value='//android.view.View[@content-desc="JOIN"]')
            time.sleep(2)
            JoinButton.click()
            try: 
                time.sleep(2)
                confirmJoin = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                                    value='//android.widget.TextView[@text="Are you sure want to join this channel?"]')
                if confirmJoin:
                    OkButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                                    value='//android.widget.TextView[@text="OK"]')
                    OkButton.click()
                    
            except:
                print("")
            time.sleep(2)
            BackButtonInchannel = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                                    value='//android.widget.ImageView[@content-desc="Go back"]')
            time.sleep(2)
            BackButtonInchannel.click()
            
    except:
        print("Name is not found")

RandomName(driver_SamsungA71)