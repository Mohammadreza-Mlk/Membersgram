from _ast import expr
import requests
import json
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time
import random
 
url = 'http://localhost:4721'

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}
######## test for sms
driver_SamsungA71 = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
touch = TouchAction(driver_SamsungA71)
time.sleep(5)
elements = driver_SamsungA71.find_elements_by_xpath("//*[starts-with(@text, 'calling')]")
time.sleep(3)
if elements:
    GetSms = driver_SamsungA71.find_elements_by_xpath("//*[starts-with(@text, 'Get the')]")
    time.sleep(3)
    GetSms.click()







