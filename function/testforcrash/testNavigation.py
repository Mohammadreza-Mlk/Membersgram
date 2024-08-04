from appium.webdriver.common.appiumby import AppiumBy
import sys, time
sys.path.append("../TelegramAuto")
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import sys, time

 

cap: Dict[str, Any] = {
  "platformName": "Android",
  "appium:platformVersion": "10.0",
  "appium:deviceName": "e037c505",
  "appium:App": "C:\\Users\\testp\\OneDrive\\Desktop\\store.apk",
  "appium:automationName": "UIAutomator2",
  "appium:ensureWebviewsHavePages": "true"
}
url = 'http://localhost:4723'


driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
touch = TouchAction(driver)
for i in range(500):
    
    touch.tap(x=145, y=2000).release().perform()
    # time.sleep(1)
    touch.tap(x=360, y=2000).release().perform()
    # time.sleep(1)
    touch.tap(x=145, y=2000).release().perform()
    # time.sleep(1)
    touch.tap(x=360, y=2000).release().perform()
    # time.sleep(1)
    touch.tap(x=640, y=2000).release().perform()
    # time.sleep(1)
    touch.tap(x=360, y=2000).release().perform()
    # time.sleep(1)
    touch.tap(x=940, y=2000).release().perform()
    # time.sleep(1)
    touch.tap(x=360, y=2000).release().perform()
    # time.sleep(1)
    touch.tap(x=145, y=2000).release().perform()
    # time.sleep(1)
    touch.tap(x=360, y=2000).release().perform()
    # time.sleep(1)
    touch.tap(x=145, y=2000).release().perform()
    # time.sleep(1)
    touch.tap(x=360, y=2000).release().perform()
    # time.sleep(1)
    touch.tap(x=640, y=2000).release().perform()
    # time.sleep(1)
    touch.tap(x=360, y=2000).release().perform()
    # time.sleep(1)
    touch.tap(x=940, y=2000).release().perform()
    # time.sleep(1)
    touch.tap(x=360, y=2000).release().perform()
    # time.sleep(1)
    
   
    