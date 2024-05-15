from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time

url = 'http://localhost:4720'

# Device 1 (Samsung)
capabilities_samsung_j5: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'platformVersion': '9.0',
    'deviceName': 'Samsung',
    'language': 'en',
    'locale': 'us'
}

driver_samsung_j5 = webdriver.Remote(url, options=AppiumOptions().load_capabilities(capabilities_samsung_j5))
touch = TouchAction(driver_samsung_j5)

# Common code for both devices
for i in range(50):

    print("\033[32m*********** *********** Start for on Samsung for *********** *********** .\033[0m")
    time.sleep(2)

    #####################################
    #        مراحل فروش اکانت ـ        ##
    #####################################

    time.sleep(3)
    SearchButton = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                  value='//android.widget.ImageButton[@content-desc="Search"]/android.widget.ImageView')
    SearchButton.click()
    SearchInput = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                 value='//android.widget.EditText[@text="Search"]')
    SearchInput.send_keys("fotor_plus_bot")
    time.sleep(10)
    print("type fotor is ok")

    touch.tap(x=400, y=300).release().perform()
    time.sleep(2)
    touch.tap(x=346, y=1230).release().perform()
    
    #BotKeyboard = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
      #                                           value='//android.widget.ImageView[@content-desc="Bot keyboard"]')
    # BotKeyboard.click()
    time.sleep(2)

    SellingAccount = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@text="Sending an account (selling an account)"]')
    SellingAccount.click()

    MessageBox = driver_samsung_j5.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Message"]')
    time.sleep(5)

    MessageBox.send_keys("+15204649647")

    SendMessageIcon = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                     value='//android.view.View[@content-desc="Send"]')
    SendMessageIcon.click()
    time.sleep(20)

    BackButton = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.ImageView[@content-desc="Go back"]')
    BackButton.click()
    time.sleep(10)
    SearchButton.click()

    SearchInput.send_keys("telegram")
    time.sleep(2)

    touch.tap(x=400, y=250).release().perform()

    ##########
    ##########

    time.sleep(3)
    # press on the final telegram message
    touch.long_press(x=500, y=1100).release().perform()
    # tap on copy icon
    touch.tap(x=460, y=124).release().perform()
    time.sleep(1)
    BackButtonTelegramChat = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                            value='//android.widget.ImageView[@content-desc="Go back"]')
    BackButtonTelegramChat.click()
    time.sleep(2)

    SearchButton.click()
    time.sleep(2)

    SearchInput.send_keys("fotor_plus_bot")

    time.sleep(5)
    print("type fotor is ok")

    touch.tap(x=400, y=300).release().perform()
    #######
    #######
    ######
    #########
    #########
    MessageBox = driver_samsung_j5.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Message"]')

    MessageBox.click()
    time.sleep(2)

    touch.long_press(x=245, y=610).release().perform()
    time.sleep(1)

    touch.tap(x=70, y=530).release().perform()

    time.sleep(2)
    print("message pasted")
    # پاک کردن اضافه پیام برای نمایان شدن متن کد
    for m in range(2):
        # location of mark massage to delete
        start_point = {'x': 120, 'y': 491}
        end_point = {'x': 400, 'y': 625}

        touch.long_press(x=start_point['x'], y=start_point['y']).move_to(x=end_point['x'], y=end_point['y']).release().perform()
        touch.tap(x=660, y=1100).release().perform()

    touch.tap(x=350, y=444).release().perform()
    touch.long_press(x=350, y=444).release().perform()
    touch.tap(x=272, y=350).release().perform()
    startClearAll = {'x': 117, 'y': 435}
    endClearAll = {'x': 530, 'y': 622}

    touch.long_press(x=startClearAll['x'], y=startClearAll['y']).move_to(x=endClearAll['x'], y=endClearAll['y']).release().perform()

    touch.tap(x=660, y=1100).release().perform()
    touch.long_press(x=660, y=1100).release().perform()
    MessageBox.send_keys("fotor_")
    # long press for open the menu for paste button
    touch.long_press(x=300, y=607).release().perform()
    # tap on paste button
    touch.tap(x=103, y=531).release().perform()
    touch.tap(x=245, y=607).release().perform()
    time.sleep(1)
    SendButton = driver_samsung_j5.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Send"]')
    SendButton.click()
    time.sleep(2)
    BackButton.click()

# Close both drivers when done
driver_samsung_j5.quit()
