from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import sys, time
sys.path.append("../TelegramAuto")

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}
url = 'http://localhost:4721'



def InstallTelegram(driver_SamsungA71):
    touch = TouchAction(driver_SamsungA71)
    time.sleep(7)
    print("Start Install telegram")
    time.sleep(5)
    touch.tap(x=165, y=1385).release().perform()

    time.sleep(3)
    InstallButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.Button[@resource-id="android:id/button1"]')
    time.sleep(1)
    InstallButton.click()
    time.sleep(15)
    # DoneButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
    #                                             value='//android.widget.Button[@resource-id="android:id/button2"]')
    # if DoneButton:
    #     print("DoneButton founde")
    #     time.sleep(9.5)
    #     DoneButton.click()
    touch.tap(x=400, y=600).release().perform()
    time.sleep(10)
    touch.tap(x=400, y=600).release().perform()
    time.sleep(6)

    start_x = 800
    start_y = 1200  
    end_x = 801  
    end_y = 500  
    driver_SamsungA71.swipe(start_x, start_y, end_x, end_y, duration=200)

    time.sleep(5)
    TelegamAppMenu = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@content-desc="Telegram"]')
    time.sleep(0.5)
    touch.long_press(TelegamAppMenu).release().perform()


    time.sleep(5)
    TelegamApp = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@content-desc="Telegram"]')

    time.sleep(3)
    touch.long_press(TelegamApp).release().perform()

    time.sleep(2)

    AppInfo = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.ImageView[@content-desc="App info"]')
    time.sleep(2)
    AppInfo.click()

    time.sleep(2)
    Permision = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@resource-id="android:id/title" and @text="Permissions"]')
    time.sleep(2)
    Permision.click()
    time.sleep(2)
    contact = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@resource-id="android:id/title" and @text="Contacts"]')
    time.sleep(2)
    contact.click()

    time.sleep(2)
    AlowPermission = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.RadioButton[@resource-id="com.android.permissioncontroller:id/allow_radio_button"]')
    AlowPermission.click()
    time.sleep(1)
    driver_SamsungA71.press_keycode(4)
    time.sleep(6)

    start_x = 800
    start_y = 800  
    end_x = 801  
    end_y = 200  
    driver_SamsungA71.swipe(start_x, start_y, end_x, end_y, duration=800)


    time.sleep(2)
    notif = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@resource-id="android:id/title" and @text="Notifications"]')
    time.sleep(1)
    notif.click()
    time.sleep(2)
    notifAllow = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@resource-id="com.android.settings:id/switch_text"]')
    time.sleep(1)
    notifAllow.click()
    driver_SamsungA71.press_keycode(4)
    time.sleep(2)
    PhotosAndVideo = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@resource-id="android:id/title" and @text="Photos and videos"]')
    time.sleep(1)
    PhotosAndVideo.click()

    time.sleep(1)
    AlowPermissionPhotosAndVideo = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.RadioButton[@resource-id="com.android.permissioncontroller:id/allow_radio_button"]')
    AlowPermissionPhotosAndVideo.click()
    for i in range (3) : 
        driver_SamsungA71.press_keycode(4)
    

    time.sleep(1)  
    
    TelegamApp.click()
    try:
        time.sleep(15)  
        AppUpdateTelegram  = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@resource-id="android:id/alertTitle"]')
    
     
        if AppUpdateTelegram:
            
            AskMeInDay = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='//android.widget.Button[@resource-id="android:id/button2"]')
            time.sleep(1)
            AskMeInDay.click()
    except:
        print("")
    
    
    return TelegamApp