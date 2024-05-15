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
touch.tap(x=374, y=1430).release().perform()

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
############################
# دکمه هوم گوشی

# driver.press_keycode(3)
