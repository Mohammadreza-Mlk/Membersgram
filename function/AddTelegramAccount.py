from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from typing import sys
sys.path.append("../TelegramAuto")
from time import sleep
import time

def swipe_left(driver):
    start_x = 650
    end_x = 300
    start_y = 400
    end_y = 400

    action = TouchAction(driver)
    action.press(x=start_x, y=start_y).wait(1000).move_to(x=end_x, y=end_y).release().perform()


def AddAccount(driver, touch):
    print("\033[32m***********  Login an account  *********** .\033[0m")

    driver.implicitly_wait(10) 
    CoinTab = driver.find_element(by=AppiumBy.XPATH,
                    value='(//android.widget.ImageView[@resource-id="gram.members.android:id/navigation_bar_item_icon_view"])[2]')
    CoinTab.click()
    driver.implicitly_wait(10)
    FreeTab =driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.LinearLayout[@content-desc="Free"]')  
    FreeTab.click()
    driver.implicitly_wait(10)

    AddTelegramAccount = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Add Telegram account"]')
    AddTelegramAccount.click()
    PhoneNumber = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextTelegramLoginPhone"]')
    PhoneNumber.send_keys("6603455472")
    driver.implicitly_wait(10) 
    NextButton = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button')
    NextButton.click()
    driver.implicitly_wait(10) 
    codeInput = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.TextView[@resource-id="gram.members.android:id/login2CustomTv1"]')
    driver.press_keycode(3)

    driver.implicitly_wait(10) 
    Vidogram = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.TextView[@content-desc="Vidogram"]')
    Vidogram.click()
    sleep(5)
    searchIcon = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.ImageButton[@content-desc="Search"]/android.widget.ImageView')
    searchIcon.click()
    searchInput = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.EditText[@text="Search"]')
    searchInput.send_keys("Telegram")
    sleep(5) 

    touch.tap(x=300, y=500).release().perform()
    touch.long_press(x=500, y=1850).release().perform()
    copyIcon = touch.tap(x=580, y=170).release().perform()
    driver.implicitly_wait(10) 
    MessageBox = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Message"]')
    MessageBox.click()

    touch.long_press(MessageBox).release().perform()
    touch.tap(x=150, y=1240).release().perform()

    
    sleep(1)
    # پاک کردن اضافه پیام برای نمایان شدن متن کد
    for m in range(2):
        # location of mark massage to delete
        start_point = {'x': 160, 'y': 1236}
        end_point = {'x': 960, 'y': 1283}

        touch.long_press(x=start_point['x'], y=start_point['y']).move_to(x=end_point['x'], y=end_point['y']).release().perform()
        touch.tap(x=1000, y=2000).release().perform()
        touch.tap(x=1000, y=2000).release().perform()
        touch.tap(x=1000, y=2000).release().perform()

    touch.tap(x=440, y=1150).release().perform()
    touch.long_press(x=440, y=1148).release().perform()
    touch.tap(x=370, y=1035).release().perform()
    touch.tap(x=844, y=1280).release().perform()

    touch.tap(x=700, y=1360).release().perform()
    sleep(1)
        
    for i in range(3):
        touch.long_press(x=990, y=2042).release().perform()
    driver.press_keycode(4)
    driver.press_keycode(4)
    driver.press_keycode(3)
    driver.implicitly_wait(5)
    MembersgramApp = driver.find_element(by=AppiumBy.XPATH,
                    value='(//android.widget.TextView[@content-desc="Membersgram"])[1]')
    MembersgramApp.click()
    time.sleep(2)
    touch.tap(x=484, y=1468).release().perform()
    driver.implicitly_wait(3)
    NextButton = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button')
    NextButton.click()
    driver.implicitly_wait(15)
    StartBot = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Start"]')
    StartBot.click()
    driver.implicitly_wait(15)
    FreeCoinAfterAddAccount = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.TextView[@text="🇺🇸 +1 660-345-5472"]')
    if FreeCoinAfterAddAccount:
        print("\033[32m***********  Login telegram acount  ✅ *********** .\033[0m")