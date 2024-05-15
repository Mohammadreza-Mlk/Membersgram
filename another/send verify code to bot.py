from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time
import random

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
    'language': 'en',
    'locale': 'us'
}

url = 'http://localhost:4723'
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
touch = TouchAction(driver)
# open telegram chat
touch.tap(x=500, y=330).release().perform()
# press on the final telegram message
touch.long_press(x=500, y=1777).release().perform()
# tap on copy icon
touch.tap(x=744, y=164).release().perform()
# tap on backspace icon
touch.tap(x=102, y=129).release().perform()
# tap on search icon
touch.tap(x=1012, y=169).release().perform()
# find input box & search id of the bot
SearchBox = driver.find_element(by=AppiumBy.XPATH,   value='//android.widget.EditText[@text="Search"]')
SearchBox.send_keys('mehdinajmtestbot')
time.sleep(2)
# tap On bot for sale accont
touch.tap(x=270, y=516).release().perform()
time.sleep(3)
# find messagebox
MessageBox = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Message"]')
MessageBox.click()
# long press on message box for open the menu for paste code
touch.long_press(MessageBox).release().perform()
# tap on the paste
touch.tap(x=120, y=1063).release().perform()

############
# location of mark massage to delete
start_point = {'x': 292, 'y': 1062}
startClearAll = {'x': 148, 'y': 1126}

# انتها
end_point = {'x': 530, 'y': 1360}
endClearAll = {'x': 460, 'y': 1400}

# پاک کردن اضافه پیام برای نمایان شدن متن کد
for i in range(2):
    touch.long_press(x=start_point['x'], y=start_point['y']).move_to(x=end_point['x'],
                                                                     y=end_point['y']).release().perform()
    for j in range(3):
        touch.tap(x=994, y=1889).release().perform()
touch.long_press(x=600, y=1060).release().perform()
touch.tap(x=641, y=880).release().perform()
touch.long_press(x=600, y=1060).release().perform()
touch.tap(x=283, y=880).release().perform()
touch.tap(x=994, y=1889).release().perform()

# touch.long_press(x=startClearAll['x'], y=startClearAll['y']).move_to(x=endClearAll['x'], y=endClearAll['y']).release().perform()
# touch.tap(x=994, y=1889).release().perform()

MessageBox = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Message"]')
MessageBox.send_keys("mlkTest_")
# long press for open the menu for paste button
touch.long_press(x=583, y=1222).release().perform()
# tap on paste button
touch.tap(x=530, y=1068).release().perform()
time.sleep(1)
SendButton = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Send"]')
SendButton.click()
############################
# دکمه هوم گوشی

# driver.press_keycode(3)
