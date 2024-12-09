from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import sys, time, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
sys.path.append("../Membersgram")
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
from function.CloseAddAccountFullScreeen import CloseAddAccountFullScreeen
from function.AddaccountFullScreen import AddAccountFullScreen
from function.Permision import Permision
from function.sitecustomize import shot

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}
url = 'http://localhost:4721'
desired_caps: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
 
 
# Permision(driver)
# time.sleep(0.5)
# Language(driver)
# time.sleep(0.5)
# Register(driver)
# time.sleep(0.5)
# CloseAddAccountFullScreeen(driver)
# time.sleep(1.5)
# LogOut(driver)
# time.sleep(1.5)
# Language(driver)
# time.sleep(1.5)
# LoginEmail(driver)
# time.sleep(1.5)
# AddAccountFullScreen(driver)
# time.sleep(1.5)
# TransferCoin(driver)
# time.sleep(1.5)
# OrderMemberByCoin(driver)
# time.sleep(1.5)
# OrderMemberByPurchase(driver)
# time.sleep(1.5)
OrderViewByCoin(driver)
time.sleep(1.5)
OrderViewByPurchase(driver)
time.sleep(1.5)
AddAccount(driver, desired_caps, url)
