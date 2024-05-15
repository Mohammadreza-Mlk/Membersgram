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

NavigationMenu = driver.find_element(by=AppiumBy.XPATH,
                                     value='//android.widget.ImageView[@content-desc="Open navigation menu"]')
NavigationMenu.click()
time.sleep(2)
touch.tap(x=374, y=1014).release().perform()
time.sleep(2)

start_point = {'x': 530, 'y': 1200}

# انتها
end_point = {'x': 520, 'y': 300}
touch.long_press(x=start_point['x'], y=start_point['y']).move_to(x=end_point['x'],
                                                                 y=end_point['y']).release().perform()
Devices = driver.find_element(by=AppiumBy.XPATH,
                              value='//android.widget.FrameLayout[@text="Devices"]')
Devices.click()
time.sleep(2)
touch.long_press(x=start_point['x'], y=start_point['y']).move_to(x=end_point['x'],
                                                                 y=end_point['y']).release().perform()

FotorSession = driver.find_element(by=AppiumBy.XPATH,
                                   value='(//android.widget.TextView[@text="membersgram2"])')
if FotorSession:
    backButton = driver.find_element(by=AppiumBy.XPATH,
                                     value='//android.widget.ImageView[@content-desc="Go back"]')
    backButton.click()

    CircleForOpenMenu = driver.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.ImageButton[@content-desc="More options"]/android.widget.ImageView')
    CircleForOpenMenu.click()

    LogOutInMenu = driver.find_element(by=AppiumBy.XPATH,
                                       value='//android.widget.TextView[@text="Log Out"]')
    LogOutInMenu.click()
    LogOutInMenu2 = driver.find_element(by=AppiumBy.XPATH,
                                        value='(//android.widget.TextView[@text="Log Out"])[2]')
    LogOutInMenu2.click()

    LogOutInDialogBOx = driver.find_element(by=AppiumBy.XPATH,
                                            value='(//android.widget.TextView[@text="Log Out"])[2]')
    LogOutInDialogBOx.click()
