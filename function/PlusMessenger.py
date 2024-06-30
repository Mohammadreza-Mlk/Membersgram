import time
from appium import webdriver
from typing import Any, Dict, sys
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import sys, time
sys.path.append("../TelegramAuto")
from function.UnistallApp import UnistalTelegram
from function.installTelegram import InstallTelegram
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

def PlusMessanger(driver_SamsungA71, phoneNumber, TelegramApp):
    touch = TouchAction(driver_SamsungA71)
    time.sleep(2)
    driver_SamsungA71.press_keycode(3)
    time.sleep(2)
            
    PlusMessage = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.TextView[@content-desc="aka"]')
    time.sleep(2)
    PlusMessage.click()
    time.sleep(8)
    try:
        NotificationError = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@text="Turn on notifications"]')
        if NotificationError:
            time.sleep(2)
            touch.tap(x=550, y=900).release().perform()
    except:
        print("Notif not found")
    time.sleep(2)
    # NavigationMenu = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
    #                                         value='//android.widget.ImageView[@content-desc="Open navigation menu"]')
    # NavigationMenu.click()
    # time.sleep(4)
    touch.tap(x=70, y=160).release().perform()
    time.sleep(4)
    AddAccount = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                        value='//android.widget.TextView[@text="Add Account"]')
    time.sleep(4)
    AddAccount.click()
    time.sleep(4)
    NumberInput = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                        value='//android.widget.EditText[@content-desc="Country code"]')
    time.sleep(4)
    NumberInput.send_keys(phoneNumber)
    # print("1")
    time.sleep(4)
    
    time.sleep(3)
    NextButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                        value='//android.widget.FrameLayout[@content-desc="Done"]/android.view.View')
    time.sleep(4)
    NextButton.click()
    time.sleep(4)
    confirmButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                        value='//android.widget.TextView[@text="Yes"]')
    time.sleep(4)
    confirmButton.click()
    time.sleep(4)
    print("waite for code")
    time.sleep(4)
    driver_SamsungA71.press_keycode(3)
    time.sleep(5)
    TelegramApp = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                            value='//android.widget.TextView[@content-desc="Telegram, 1 notification"]')
    time.sleep(4)
    TelegramApp.click()


    time.sleep(10)
    SearchButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                            value='//android.widget.ImageButton[@content-desc="Search"]/android.widget.ImageView')
    SearchButton.click()
    time.sleep(4)
    SearchInput = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                            value='//android.widget.EditText[@text="Search"]')


    SearchInput.send_keys("telegram ")
    time.sleep(5)
    touch.tap(x=400, y=350).release().perform()

    ##########
    ##########

    time.sleep(3)
    # press on the final telegram message
    touch.long_press(x=500, y=1800).release().perform()
    time.sleep(4)
    # tap on copy icon
    touch.tap(x=750, y=170).release().perform()
    time.sleep(4)
    print("code copied")

    MessageBox = driver_SamsungA71.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Message"]')

    MessageBox.click()
    time.sleep(2)

    touch.long_press(MessageBox).release().perform()
    time.sleep(1)

    touch.tap(x=150, y=1240).release().perform()

    time.sleep(2)
    print("message pasted")
    time.sleep(2)



    for m in range(2):
            # location of mark massage to delete
            start_point = {'x': 155, 'y': 1235}
            end_point = {'x': 960, 'y': 1360}

            touch.long_press(x=start_point['x'], y=start_point['y']).move_to(x=end_point['x'], y=end_point['y']).release().perform()
            touch.tap(x=1000, y=2000).release().perform()
            touch.tap(x=1000, y=2000).release().perform()
            touch.tap(x=1000, y=2000).release().perform()

    touch.tap(x=450, y=1235).release().perform()
    touch.long_press(x=440, y=1235).release().perform()
    touch.tap(x=370, y=1130).release().perform()

    time.sleep(2)
    driver_SamsungA71.press_keycode(3)
    time.sleep(2)
            
    PlusMessage = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.TextView[@content-desc="aka"]')
    time.sleep(2)
    PlusMessage.click()
    time.sleep(2)
    touch.long_press(x=320, y=975).release().perform()
    touch.tap(x=320, y=790).release().perform()

    time.sleep(19)    
    # try:
    #     category = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
    #                                         value='//*[starts-with(@text, "Telegram has added Folders (more info: https://telegram.org/blog/folders)."]')
    #     if category:
    #         time.sleep(4)
    #         OkButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
    #                                         value='//android.widget.TextView[@text="OK"]')
    #         time.sleep(2)
    #         OkButton.click()
    #         time.sleep(2)
    #         BackButtonCategory = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
    #                                         value='//android.widget.ImageView[@content-desc="Go back"]')
    #         time.sleep(2)
    #         BackButtonCategory.click()
    # except:
    #     print("")   
    try:
        NotificationError = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@text="Turn on notifications"]')
        if NotificationError:
            time.sleep(2)
            touch.tap(x=550, y=900).release().perform()
    except:
        print("Notif not found")
    time.sleep(4)
    SearchButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                            value='//android.widget.ImageButton[@content-desc="Search"]/android.widget.ImageView')
    SearchButton.click()
    time.sleep(4)
    SearchInput = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                            value='//android.widget.EditText[@text="Search"]')


    SearchInput.send_keys("fotorchannelplusmessage")
    time.sleep(7)
    touch.tap(x=400, y=465).release().perform()
    time.sleep(5)
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
    
    time.sleep(2)
    driver_SamsungA71.press_keycode(3)

    UnistalTelegram(driver_SamsungA71)

    time.sleep(8)
    InstallTelegram(driver_SamsungA71)


        
