
from appium.webdriver.common.appiumby import AppiumBy
import sys, time
sys.path.append("../TelegramAuto")
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import sys, time
 
def OrderViewByPurchase(driver):

    # HomePage = driver.find_element(by=AppiumBy.XPATH,
    #                 value='(//android.widget.FrameLayout[@resource-id="com.membersgram.android:id/navHostMain"])[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView')
    # HomePage.click()   
    time.sleep(2)
    
    ViewTab = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.TextView[@text="View"]')
    
    ViewTab.click()
    driver.implicitly_wait(30)
    Onepost = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.Button[@text="One Post"]')
    Onepost.click()
    driver.implicitly_wait(30)
    view1000 = driver.find_element(by=AppiumBy.XPATH,
                value='//androidx.recyclerview.widget.RecyclerView[@content-desc="View bundles list"]/android.view.ViewGroup[1]')
    view1000.click()

    driver.implicitly_wait(30)
    PostLink = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.TextView[@text="Please enter the link to the desired post"]')


    NextButton = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.Button[@text="Next"]')
    NextButton.click()
    driver.implicitly_wait(30)
    LinkEmpty = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.TextView[@text="Link must not be empty"]')
    if LinkEmpty:
        print("Link Empty in view one post By Purchase is : pass ✅ ")
    else:
        print("Link Empty in view one post By Purchase is : Failed ❌")

    driver.implicitly_wait(30)
    PostLink = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextUserName"]')

    PostLink.send_keys('testpnx1')
    NextButton.click()

    FormatError = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.TextView[@text="Format is incorrect"]')
    if FormatError:
        print("Format link incorrect in view one Purchase is : pass ✅ ")
    else:
        print("Format link incorrect in view one Purchase is : Failed ❌")

    PostLink.send_keys("t.me/testpnx1/3")    
    NextButton.click()
        
    driver.implicitly_wait(30)  
    PayInButtomshit = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Pay"]')
    PayInButtomshit.click()
    driver.implicitly_wait(30)


    AgreeButtonInGoogleButtomsheet = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]')
    AgreeButtonInGoogleButtomsheet.click()
    driver.implicitly_wait(30)

    OneTapBuy = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]')
    OneTapBuy.click()
    driver.implicitly_wait(30)

    SeccessfulView = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.TextView[@text="Successful payment"]')
    if SeccessfulView:
        print("Order View in view one Purchase is : pass ✅ ")
        GotItView = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Got it"]')
        GotItView.click()
    else:
        print("Order View in view one Purchase is : Failed ❌")
        


    ############## Order View for 5 post 

        
    driver.implicitly_wait(30)
    ViewTab = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.TextView[@text="View"]')
    ViewTab.click()
    driver.implicitly_wait(30)
    FivePost = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.Button[@text="5 Posts"]')
    FivePost.click()
    view1000 = driver.find_element(by=AppiumBy.XPATH,
                value='//androidx.recyclerview.widget.RecyclerView[@content-desc="View bundles list"]/android.view.ViewGroup[1]')
    view1000.click()

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
    else:
        print("Username Empty in view for 5 Purchase is : Failed ❌")

    driver.implicitly_wait(30)
    PostLink = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextUserName"]')

    PostLink.send_keys('1testpnx1')
    NextButton.click()

    FormatError = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.TextView[@text="Format is incorrect"]')
    if FormatError:
        print("Format link incorrect in view for 5 Purchase is : pass ✅ ")
    else:
        print("Format link incorrect in view for 5 Purchase is : Failed ❌")

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
    driver.implicitly_wait(30)

    AgreeButtonInGoogleButtomsheet = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]')
    AgreeButtonInGoogleButtomsheet.click()
    driver.implicitly_wait(30)

    OneTapBuy = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]')
    OneTapBuy.click()
    driver.implicitly_wait(30)
    SeccessfulView = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.TextView[@text="Successful payment"]')
    if SeccessfulView:
        print("Order View in view for 5 Purchase is : pass ✅ ")
        GotItView = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Got it"]')
        GotItView.click()
    else:
        print("Order View in view for 5 Purchase is : Failed ❌")
        
        
        
        
            
        # OnePost = driver.find_element(by=AppiumBy.XPATH,
        #             value='//android.widget.Button[@text="One Post"]')
        # OnePost.click()
        