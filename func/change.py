from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import sys, time, os
cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}
url = 'http://localhost:4721'
from watchlog import Watchlog
watchlog_instance = Watchlog()
# watchlog_instance.increment('OrderMemberByPurchasePass')
# watchlog_instance.increment('AddAccountFailed')
time.sleep(1.5)
watchlog_instance.increment('AddAccount')
# watchlog_instance.increment('TooManyOrderForChannelByPurchaseFiled')
# watchlog_instance.increment('TestOrder_5_PostViewByPurchaseFailed')
# watchlog_instance.increment('TestOrderMemberByPurchaseFailed')

# watchlog_instance.increment('TestOrderCountryMemberByCoinByCoinFailed')