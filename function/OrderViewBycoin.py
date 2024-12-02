
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
 
def OrderViewByCoin(driver):
    time.sleep(3)
    CoinTab = driver.find_element(by=AppiumBy.XPATH,
                value='(//android.widget.FrameLayout[@resource-id="gram.members.android:id/navigation_bar_item_icon_container"])[2]')
    CoinTab.click()
    driver.implicitly_wait(5)
    HomePage = driver.find_element(by=AppiumBy.XPATH,
                value='(//android.widget.ImageView[@resource-id="gram.members.android:id/navigation_bar_item_icon_view"])[1]')
    HomePage.click()
    driver.implicitly_wait(5)
    ViewTab = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.TextView[@text="View"]')
    ViewTab.click()
    driver.implicitly_wait(5)
    Onepost = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.Button[@text="One Post"]')
    Onepost.click()
    view100 = driver.find_element(by=AppiumBy.XPATH,
                value='//androidx.recyclerview.widget.RecyclerView[@content-desc="View bundles list"]/android.view.ViewGroup[3]')
    view100.click()

    driver.implicitly_wait(5)
    PostLink = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.TextView[@text="Please enter the link to the desired post"]')


    NextButton = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.Button[@text="Next"]')
    NextButton.click()
    driver.implicitly_wait(5)
    LinkEmpty = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.TextView[@text="Link must not be empty"]')
    if LinkEmpty:
        print("Link Empty in view one post is : pass ✅ ")
        watchlog_instance.increment('LinkEmptyInViewOnePostByCoinPass')
    else:
        print("Link Empty in view one post is : Failed ❌")
        watchlog_instance.increment('LinkEmptyInViewOnePostByCoinFailed')

    driver.implicitly_wait(5)
    PostLink = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextUserName"]')

    PostLink.send_keys('testpnx1')
    NextButton.click()

    FormatError = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.TextView[@text="Format is incorrect"]')
    if FormatError:
        print("Format link incorrect in view one post is : pass ✅ ")
        watchlog_instance.increment('FormatLinkIncorrectInViewOnePostByCoinPass')
    else:
        print("Format link incorrect in view one post is : Failed ❌")
        watchlog_instance.increment('FormatLinkIncorrectInViewOnePostByCoinFailed')

    PostLink.send_keys("t.me/testpnx1/3")    
    NextButton.click()
        
    driver.implicitly_wait(5)  
    PayInButtomshit = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Pay"]')
    PayInButtomshit.click()
    driver.implicitly_wait(5)
    SeccessfulView = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.TextView[@text="Successful payment"]')
    if SeccessfulView:
        print("Order View in view one post is : pass ✅ ")
      
        watchlog_instance.increment('OrderViewOnePostByCoinPass')
        GotItView = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Got it"]')
        GotItView.click()
    else:
        print("Order View in view one post is : Failed ❌")
        watchlog_instance.increment('OrderViewOnePostByCoinFailed')
        


    ############## Order View for 5 post 

        
    driver.implicitly_wait(5)
    ViewTab = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.TextView[@text="View"]')
    ViewTab.click()
    driver.implicitly_wait(5)
    FivePost = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.Button[@text="5 Posts"]')
    FivePost.click()
    view100 = driver.find_element(by=AppiumBy.XPATH,
                value='//androidx.recyclerview.widget.RecyclerView[@content-desc="View bundles list"]/android.view.ViewGroup[3]')
    view100.click()

    driver.implicitly_wait(5)
    PostLink = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextUserName"]')


    NextButton = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.Button[@text="Next"]')
    NextButton.click()
    driver.implicitly_wait(5)
    LinkEmpty = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.TextView[@text="Username must not be empty"]')
    if LinkEmpty:
        print("Username Empty in view for 5 post is : pass ✅ ")
        watchlog_instance.increment('UsernameEmptyInViewFor_5_PostByCoinPass')
    else:
        print("Username Empty in view for 5 post is : Failed ❌")
        watchlog_instance.increment('UsernameEmptyInViewFor_5_PostByCoinFailed')

    driver.implicitly_wait(5)
    PostLink = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextUserName"]')

    PostLink.send_keys('1testpnx1')
    NextButton.click()

    FormatError = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.TextView[@text="Format is incorrect"]')
    if FormatError:
        print("Format link incorrect in view for 5 post is : pass ✅ ")
        watchlog_instance.increment('FormatLinkIncorrectInView_5_PostByCoinPass')
    else:
        print("Format link incorrect in view for 5 post is : Failed ❌")
        watchlog_instance.increment('FormatLinkIncorrectInView_5_PostByCoinFailed')

    PostLink.send_keys("t.me/testpnx1")    
    NextButton.click()
    driver.implicitly_wait(5) 
    ConfirmBottomSheet = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Yes, next"]')
    ConfirmBottomSheet.click()
    driver.implicitly_wait(5)  
    PayInButtomshit = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Pay"]')
    PayInButtomshit.click()
    driver.implicitly_wait(5)
    SeccessfulView = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.TextView[@text="Successful payment"]')
    if SeccessfulView:
        print("Order View in view for 5 post is : pass ✅ ")
        watchlog_instance.increment('Order_5_PostViewByCoinPass')
        GotItView = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Got it"]')
        GotItView.click()
    else:
        print("Order View in view for 5 post is : Failed ❌")
        
        
        
        
            
        # OnePost = driver.find_element(by=AppiumBy.XPATH,
        #             value='//android.widget.Button[@text="One Post"]')
        # OnePost.click()
        