from appium.webdriver.common.appiumby import AppiumBy
import sys, time
sys.path.append("../TelegramAuto")
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import sys, time

 
def BuyCoin(driver):
    driver.implicitly_wait(30)
    CoinTab = driver.find_element(by=AppiumBy.XPATH,
                    value='(//android.widget.ImageView[@resource-id="gram.members.android:id/navigation_bar_item_icon_view"])[2]')
    CoinTab.click()
    driver.implicitly_wait(30)
    BuyTab = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.TextView[@text="Buy"]')

    BuyTab.click()
    driver.implicitly_wait(50)
    Package_of_FiveThousandCoins = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.TextView[@text="5,000"]')
    Package_of_FiveThousandCoins.click()
    driver.implicitly_wait(30)

    AgreeButtonInGoogleButtomsheet = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]')
    AgreeButtonInGoogleButtomsheet.click()
    driver.implicitly_wait(30)

    OneTapBuy = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]')
    OneTapBuy.click()
    driver.implicitly_wait(30)

    SeccessfulPaymentForCoin = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.TextView[@text="Congratulations"]')
    if SeccessfulPaymentForCoin : 
        print("purchase 5000 coins is :  pass ✅ ")
        OkButton = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="OK"]')
        OkButton.click()
        HomeTab = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.TextView[@resource-id="gram.members.android:id/navigation_bar_item_small_label_view" and @text="Home"]')
        HomeTab.click()
    else:
        print("purchase 5000 coins is : Failed ❌")
    