
from appium.webdriver.common.appiumby import AppiumBy
import sys, time
sys.path.append("../TelegramAuto")
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import sys, time
from watchlog import Watchlog
watchlog_instance = Watchlog()
from function.result import log_test_result
 
def OrderViewByPurchase(driver):

    time.sleep(2)
    HomeTab = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.FrameLayout[@content-desc="Home"]')
    HomeTab.click()
    driver.implicitly_wait(10)
    ViewTab = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.TextView[@text="View"]')
    
    ViewTab.click()
    driver.implicitly_wait(30)
    Onepost = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.Button[@text="One Post"]')
    Onepost.click()
    driver.implicitly_wait(30)
    view200 = driver.find_element(by=AppiumBy.XPATH,
                value='//androidx.recyclerview.widget.RecyclerView[@content-desc="View bundles list"]/android.view.ViewGroup[1]')
    view200.click()

    driver.implicitly_wait(30)
    PostLink = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextUserName"]')


    NextButton = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.Button[@text="Next"]')
    NextButton.click()
    driver.implicitly_wait(30)
    LinkEmpty = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.TextView[@text="Link must not be empty"]')
    if LinkEmpty:
        print("Link Empty in view one post By Purchase is : pass ✅ ")
        # watchlog_instance.increment('LinkEmptyInViewOnePostByByPurchasePass')
    else:
        print("Link Empty in view one post By Purchase is : Failed ❌")
        # watchlog_instance.increment('LinkEmptyInViewOnePostByPurchaseFailed')

    driver.implicitly_wait(30)
    PostLink = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextUserName"]')

    PostLink.send_keys('testpnx1')
    NextButton.click()

    FormatError = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.TextView[@text="Format is incorrect"]')
    if FormatError:
        print("Format link incorrect in view one Purchase is : pass ✅ ")
        # watchlog_instance.increment('FormatLinkIncorrectInViewOnePostByPurchasePass')
    else:
        print("Format link incorrect in view one Purchase is : Failed ❌")
        # watchlog_instance.increment('FormatLinkIncorrectInViewOnePostByPurchaseFailed')

    PostLink.send_keys("t.me/testpnx1/3")    
    NextButton.click()
        
    driver.implicitly_wait(30)  
    PayInButtomshit = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Pay"]')
    PayInButtomshit.click()
    # driver.implicitly_wait(30)


    # AgreeButtonInGoogleButtomsheet = driver.find_element(by=AppiumBy.XPATH,
    #                 value='//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]')
    # AgreeButtonInGoogleButtomsheet.click()
    driver.implicitly_wait(30)

    OneTapBuy = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]')
    OneTapBuy.click()
    driver.implicitly_wait(30)

    SeccessfulView = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.TextView[@text="Successful payment"]')
    # watchlog_instance.increment('Order_1_PostViewByPurchase')
    if SeccessfulView:
        print("Order View in view one Purchase is : pass ✅ ")
        log_test_result("purchase view one post", "pass")
        # watchlog_instance.increment('OrderViewOnePostByPurchasePass')
        
        GotItView = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Got it"]')
        GotItView.click()
        driver.implicitly_wait(5)
        HomeTab = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.FrameLayout[@content-desc="Home"]')
        HomeTab.click()
    else:
        print("Order View in view one Purchase is : Failed ❌")
        log_test_result("purchase view one post", "failed")
        # watchlog_instance.increment('OrderViewOnePostByPurchaseFailed')
        


    ############## Order View for 5 post 

        
    driver.implicitly_wait(30)
    ViewTab = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.TextView[@text="View"]')
    ViewTab.click()
    driver.implicitly_wait(30)
    FivePost = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.Button[@text="5 Posts"]')
    FivePost.click()
    view200 = driver.find_element(by=AppiumBy.XPATH,
                value='//androidx.recyclerview.widget.RecyclerView[@content-desc="View bundles list"]/android.view.ViewGroup[1]')
    view200.click()

    driver.implicitly_wait(30)
    PostLink = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextUserName"]')


    NextButton = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.Button[@text="Next"]')
    NextButton.click()
    driver.implicitly_wait(30)
    LinkEmpty = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.TextView[@text="Username must not be empty"]')
    if LinkEmpty:
        print("Username Empty in view for 5 Purchase is : pass ✅ ")
        # watchlog_instance.increment('UsernameEmptyInViewFor_5_PostByPurchasePass')
    else:
        print("Username Empty in view for 5 Purchase is : Failed ❌")
        # watchlog_instance.increment('UsernameEmptyInViewFor_5_PostByPurchaseFailed')

    driver.implicitly_wait(30)
    PostLink = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextUserName"]')

    PostLink.send_keys('1testpnx1')
    NextButton.click()

    FormatError = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.TextView[@text="Format is incorrect"]')
    if FormatError:
        print("Format link incorrect in view for 5 Purchase is : pass ✅ ")
        # watchlog_instance.increment('FormatLinkIncorrectInView_5_PostByPurchasePass')
    else:
        print("Format link incorrect in view for 5 Purchase is : Failed ❌")
        # watchlog_instance.increment('FormatLinkIncorrectInView_5_PostByPurchaseFailed')

    PostLink.send_keys("t.me/testpnx1")    
    NextButton.click()
    driver.implicitly_wait(30) 
    ConfirmBottomSheet = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Yes, next"]')
    ConfirmBottomSheet.click()
    driver.implicitly_wait(30)  
    PayInButtomshit = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Pay"]')
    PayInButtomshit.click()
    # driver.implicitly_wait(30)

    # AgreeButtonInGoogleButtomsheet = driver.find_element(by=AppiumBy.XPATH,
    #                 value='//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]')
    # AgreeButtonInGoogleButtomsheet.click()
    driver.implicitly_wait(30)

    OneTapBuy = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]')
    OneTapBuy.click()
    driver.implicitly_wait(30)
    SeccessfulView = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.TextView[@text="Successful payment"]')
    # watchlog_instance.increment('Order_5_PostViewByPurchase')
    if SeccessfulView:
        print("Order View in view for 5 Purchase is : pass ✅ ")
        log_test_result("purchase view five post", "pass")
        # watchlog_instance.increment('Order_5_PostViewByPurchasePass')
        GotItView = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Got it"]')
        GotItView.click()
        driver.implicitly_wait(10)
        HomeTab = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.FrameLayout[@content-desc="Home"]')
        HomeTab.click()
    else:
        print("Order View in view for 5 Purchase is : Failed ❌")
        log_test_result("purchase view five post", "failed")
        
        
        
         