from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time
 
# cap: Dict[str, Any] = {
#     'platformName': 'Android',
#     'automationName': 'uiautomator2',
#     'deviceName': 'SamsungA71',
#     "platformVersion": "13.0",
#     'language': 'en',
#     'locale': 'us'
# }
# url = 'http://localhost:4721'
# driver_SamsungA71 = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))


def Email_check(driver_SamsungA71):
    time.sleep(1)
    touch = TouchAction(driver_SamsungA71)  
    
    try:
        time.sleep(2)
        NeedEmail = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.TextView[@text="Choose a login email"]')
        if NeedEmail:
            time.sleep(3)
            EmailInput = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.EditText')
        
            EmailInput.send_keys("testphoenixmlk@gmail.com")
            time.sleep(2)
            nextEmailButtun = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.FrameLayout[@content-desc="Done"]/android.view.View')
            nextEmailButtun.click()
            time.sleep(2)
            veifyCodeEmail = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]')
            if veifyCodeEmail:
                driver_SamsungA71.press_keycode(3)
        
        try:
            time.sleep(10)
            gmailApp=''
            gmailApp = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@content-desc="Gmail"]')
            time.sleep(1)
            gmailApp.click()
        except:
            print(" gmail not found")
        try:
            time.sleep(10)
            gmailAppNotif = None
            gmailAppNotif= driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@content-desc="Gmail, 1 notification"]')
            time.sleep(1)
            gmailAppNotif.click()
        except:
            print(" gmail notif not found")
        if gmailAppNotif or gmailApp :
            time.sleep(10)
            touch.tap(x=666, y=580).release().perform()

            time.sleep(3)

            touch.long_press(x=385, y=840).release().perform()
            time.sleep(3)

            touch.tap(x=120, y=780).release().perform()
            time.sleep(3)

            Back_in_email_chat = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                                value='//android.widget.ImageButton[@content-desc="Navigate up"]')
            Back_in_email_chat.click()
            driver_SamsungA71.press_keycode(3)
            time.sleep(2)

            TelegramApp = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                                value='//android.widget.TextView[@content-desc="Telegram Beta"]')
            TelegramApp.click()
            time.sleep(2)
            touch.long_press(x=270, y=950).release().perform()
            time.sleep(1)
            touch.tap(x=240, y=824).release().perform()
            
    
    except:
        print('need email not found')
        
# Email_check(driver_SamsungA71)