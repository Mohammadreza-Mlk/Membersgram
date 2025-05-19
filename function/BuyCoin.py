from appium.webdriver.common.appiumby import AppiumBy
import sys, time
sys.path.append("../TelegramAuto")
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import sys, time,subprocess
from watchlog import Watchlog
watchlog_instance = Watchlog()
from function.result import log_test_result

 
def BuyCoin(driver):
    
     
    javascript_file = 'api.js'

    # اجرای فایل جاوا اسکریپت
    result = subprocess.run(['node', javascript_file], capture_output=True, text=True)

    # نمایش خروجی
    MyCoinsBeforePurchase = result.stdout
    print("My coins Before Purchase :", MyCoinsBeforePurchase )
 
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
                    value='//androidx.recyclerview.widget.RecyclerView[@resource-id="gram.members.android:id/rvPurchaseCoin"]/android.view.ViewGroup[2]')
    Package_of_FiveThousandCoins.click()
    driver.implicitly_wait(30)

    # AgreeButtonInGoogleButtomsheet = driver.find_element(by=AppiumBy.XPATH,
    #                 value='//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]')
    # AgreeButtonInGoogleButtomsheet.click()
    # driver.implicitly_wait(30)

    OneTapBuy = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]')
    OneTapBuy.click()
    

    try:
        driver.implicitly_wait(30)
        SeccessfulPaymentForCoin = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.TextView[@text="Successful payment"]')
        
    
             
        if SeccessfulPaymentForCoin : 
            # watchlog_instance.increment('BuyCoin')
            print("purchase 5000 coins is :  pass ✅ ")
            log_test_result("buy coin", "pass")
            driver.implicitly_wait(30)
            OkButton = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="OK"]')
            OkButton.click()
            # اجرای فایل جاوا اسکریپت
            result = subprocess.run(['node', javascript_file], capture_output=True, text=True)

            # نمایش خروجی
            MyCoinsAfterPurchase = result.stdout
            print("MyCoinsAfterPurchase", MyCoinsAfterPurchase )
            if MyCoinsAfterPurchase > MyCoinsBeforePurchase:
                print("PASS")
                # watchlog_instance.increment('BuyCoinpass')
            
            
            
        else:
            print("purchase 5000 coins is : Failed ❌")
            log_test_result("buy coin", "failed")
            # watchlog_instance.increment('BuyCoinFail')
    except:
        print( )