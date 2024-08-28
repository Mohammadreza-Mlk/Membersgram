from appium import webdriver
from typing import Any, Dict
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from typing import sys
sys.path.append("../TelegramAuto")
from time import sleep
import time
import sys, time, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

sys.path.append("../func")
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.pointer_input import PointerInput

appium_server = 'http://localhost:4721'
def swipe_left(driver):
    start_x = 650
    end_x = 300
    start_y = 400
    end_y = 400

    action = TouchAction(driver)
    action.press(x=start_x, y=start_y).wait(1000).move_to(x=end_x, y=end_y).release().perform()


def AddAccount(driver, touch, desired_caps):
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
    x, y = 300, 500
    driver.tap([(x, y)])
    sleep(5)
    # touch.tap(x=300, y=500).release().perform()
    x, y = 500, 1850
    driver.tap([(x, y)])

    # touch.long_press(x=500, y=1850).release().perform()
    time.sleep(1.5)
    x, y = 390, 1130
    driver.tap([(x, y)])
    # copyIcon = touch.tap(x=580, y=170).release().perform()
    driver.implicitly_wait(10) 
    MessageBox = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Message"]')
    MessageBox.click()
 
    
    x, y = 244, 1355
    driver.tap([(x, y)])
    # driver.long_press(MessageBox)
    # touch.long_press(MessageBox).release().perform()
    x, y = 150, 1240
    driver.tap([(x, y)])
    # touch.tap(x=150, y=1240).release().perform()

    
    sleep(1)
    # پاک کردن اضافه پیام برای نمایان شدن متن کد
    for m in range(60):
        # location of mark massage to delete
        driver.long_press_keycode(67)
    sleep(1)   
    x, y = 460, 1070
    driver.tap([(x, y)])
    sleep(1)

    appium_options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote(appium_server, options=appium_options)
    driver.execute_script('mobile: longClickGesture', {'x': 460, 'y': 1072, 'duration': 1000})
   




    # touch.long_press(x=440, y=1148).release().perform()
    sleep(1)
    x, y = 320, 975
    driver.tap([(x, y)])
    # touch.tap(x=370, y=1035).release().perform()
    
        
    
        # touch.long_press(x=990, y=2042).release().perform()
    driver.press_keycode(4)
    driver.press_keycode(4)
    driver.press_keycode(3)
    driver.implicitly_wait(5)
    MembersgramApp = driver.find_element(by=AppiumBy.XPATH,
                    value='(//android.widget.TextView[@content-desc="Membersgram"])[1]')
    MembersgramApp.click()
    time.sleep(2)
    x, y = 484, 1468
    driver.tap([(x, y)])
    # touch.tap(x=484, y=1468).release().perform()
    driver.implicitly_wait(3)
    NextButton = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button')
    NextButton.click()
    driver.implicitly_wait(15)
    StartBot = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Start"]')
    StartBot.click()
    driver.implicitly_wait(30)
    FreeCoinAfterAddAccount = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.TextView[@text="🇺🇸 +1 660-345-5472"]')
    if FreeCoinAfterAddAccount:
        print("\033[32m***********  Login telegram acount  ✅ *********** .\033[0m")