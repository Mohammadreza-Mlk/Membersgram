from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import sys, time
sys.path.append("../TelegramAuto")
from function.ChangeLanguage import Language
from function.Register import Register
from function.Login import LoginEmail
from function.BuyCoin import BuyCoin
from function.AddTelegramAccount import AddAccount
from function.LogOut import LogOut
from function.OrderMemberByCoin import OrderMemberByCoin
from function.OrderMemberByPurchase import OrderMemberByPurchase
from function.OrderViewBycoin import OrderViewByCoin
from function.OrderViewByPurchase import OrderViewByPurchase
from function.TransferCoin import TransferCoin
from function.AddaccountFullScreen import AddAccountFullScreen


cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}
url = 'http://localhost:4721'


driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
touch = TouchAction(driver)
Language(driver)
time.sleep(4)
Register(driver, touch)
time.sleep(4)
AddAccountFullScreen(driver)
time.sleep(4)
LogOut(driver)
time.sleep(4)
Language(driver)
time.sleep(4)
LoginEmail(driver)
time.sleep(4)
AddAccountFullScreen(driver)
time.sleep(4)
OrderMemberByCoin(driver)
time.sleep(4)
OrderMemberByPurchase(driver)
time.sleep(4)
OrderViewByCoin(driver)
time.sleep(4)
OrderViewByPurchase(driver)
time.sleep(4)
TransferCoin(driver)
time.sleep(4)
BuyCoin(driver)
time.sleep(4)
AddAccount(driver, touch)