
from appium.webdriver.common.appiumby import AppiumBy
import sys, time
sys.path.append("../TelegramAuto")
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from function.BuyCoin import BuyCoin
import sys, time
from watchlog import Watchlog
watchlog_instance = Watchlog()

def OrderMemberByCoin(driver):

# HomePage = driver.find_element(by=AppiumBy.XPATH,
#                 value='(//android.widget.FrameLayout[@resource-id="com.membersgram.android:id/navHostMain"])[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView')
# if HomePage:
    try:
        SomthingWentWrong = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.TextView[@text="Something went wrong."]')
        if SomthingWentWrong :
            RetryButton = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Retry"]')
            print("Package Member is : Somthing went wrong ❌")
            watchlog_instance.increment('LoadPackageMemberByCoinFailed')
            RetryButton.click()
        else:
            print("Package Member is : Ok ✅")
            watchlog_instance.increment('LoadPackageMemberByCoinPass')
    except:
        print("")
    driver.implicitly_wait(30)
    WorldPackage = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.Button[@text="🌏  World"]')
    WorldPackage.click()
    driver.implicitly_wait(30)
    Order50MemberByCoin = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.TextView[@text="50"]')
    Order50MemberByCoin.click()
    driver.implicitly_wait(30)
    try:
        InsufficientBalance = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.TextView[@text="Insufficient Balance"]')
        if InsufficientBalance:
            CancelButtom = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Cancel"]')
            CancelButtom.click()
            time.sleep(2)
            BuyCoin(driver)
            driver.implicitly_wait(30)
            Order50MemberByCoin = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.GridView[@content-desc="Member bundles list"]/android.view.ViewGroup[3]')
            Order50MemberByCoin.click()
    except:
        print("coins enough")
        

    # for ordercount in range(2):
        # if ordercount == 1 :
    driver.implicitly_wait(30)
    # Order50MemberByCoin = driver.find_element(by=AppiumBy.XPATH,
    #             value='//android.widget.TextView[@text="50"]')
    # Order50MemberByCoin.click()
    # driver.implicitly_wait(30)
        # else:
    try:
        time.sleep(2)
        driver.implicitly_wait(30)
        MemberNotice = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.TextView[@text="Member order notice"]')
        if MemberNotice:
            time.sleep(11)
            CheckboxMemberNotice = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.CheckBox[@resource-id="gram.members.android:id/cbMemberNotice"]')

            CheckboxMemberNotice.click()
            driver.implicitly_wait(30)
            Got_it_InMemberNotice = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Got it"]')
            Got_it_InMemberNotice.click()
    except:
        print("membernotice Notfound")
    time.sleep(2)
    NextButton = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Next"]')
    NextButton.click()
    time.sleep(2)
    EmptyIdError = driver.find_element(by=AppiumBy.XPATH,
                        value='//*[contains(@text, "Username must not be empty")]')
    if EmptyIdError:
        print("Empty Id Empty Error is : pass ✅")
        watchlog_instance.increment('EmptyIdErrorByCoinPass')
    else:
        print("Empty Id Empty Error is : Failed ❌")
        watchlog_instance.increment('EmptyIdErrorByCoinFailed')
    driver.implicitly_wait(30)    
    UsernameInput = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextUserName"]')
    UsernameInput.send_keys("1111")
    driver.implicitly_wait(30)
    NextButton = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Next"]')
    NextButton.click()
    time.sleep(2)
    FormatIdError = driver.find_element(by=AppiumBy.XPATH,
                        value='//*[contains(@text, "Format is incorrect")]')
    if FormatIdError:
        print("Format Id incorrect Error is : pass ✅")
        watchlog_instance.increment('FormatIdIncorrectErrorByCoinPass')
    else:
        print("Format Id incorrect Error is : Failed ❌")
        watchlog_instance.increment('FormatIdIncorrectErrorByCoinFailed')
    UsernameInput =   driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextUserName"]')
    UsernameInput.send_keys("testpnx1")
    NextButton.click()
    time.sleep(2)
    ConfirmButtomShit = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Yes, next"]')
    ConfirmButtomShit.click()
    time.sleep(2)
    PayButton = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Pay"]')
    PayButton.click()
    time.sleep(2)
    
    SeccessfulPayment = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.TextView[@text="Successful payment"]')
    SeccessfulPayment.click()
    if SeccessfulPayment:
        GotItButton = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Got it"]')
        GotItButton.click()
        if GotItButton:
            print("Order Member By Coin is : pass ✅")
            watchlog_instance.increment('OrderMemberByCoinIsPass')
        else:
            print("Order Member By Coin is : Failed ❌")
            watchlog_instance.increment('OrderMemberByCoinFalse')
    
        time.sleep(2)
    
    
    
     
    
    
        
    #           
    time.sleep(2)           
    NigeriaMember = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Nigeria"]')
    NigeriaMember.click()              
    time.sleep(2)
    GetMemberByCoinNigeria = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.GridView[@content-desc="Member bundles list"]/android.view.ViewGroup[2]')

    GetMemberByCoinNigeria.click()
    time.sleep(2)
    
    
    UsernameInput = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextUserName"]')
    UsernameInput.send_keys("testpnx1")
    NextButton = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Next"]')
    NextButton.click()
    time.sleep(2)
    
    TooManyOrderForChannel = driver.find_element(by=AppiumBy.XPATH,
                            value='//android.widget.TextView[@text="Too many orders in progress"]')
    if TooManyOrderForChannel :
        driver.implicitly_wait(30)
        
        
        print("Too Many Order For Channel is : pass ✅")
        watchlog_instance.increment('TooManyOrderForChannelByCoinPass')
        driver.implicitly_wait(30)
        OkForTooManyChannel = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="OK"]')
        OkForTooManyChannel.click()
        time.sleep(2)
        
    else:
        print("Too Many Order For Channel is : Failed ❌")
        watchlog_instance.increment('TooManyOrderForChannelByCoinFiled')
        time.sleep(2) 
    
    driver.implicitly_wait(30)
    
    UsernameInput = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextUserName"]')
    UsernameInput.send_keys("1111")
    NextButton = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Next"]')
    NextButton.click()
    time.sleep(2)
    FormatIdError = driver.find_element(by=AppiumBy.XPATH,
                        value='//*[contains(@text, "Format is incorrect")]')
    if FormatIdError:
        print("Format Id incorrect In country order Error is : pass ✅")
        watchlog_instance.increment('FormatIdIncorrectInCountryOrderByCoinErrorPass')
    else:
        print("Format Id incorrect In country order Error is : Failed ❌")
        watchlog_instance.increment('FormatIdIncorrectInCountryOrderErrorByCoinFiled')

     
    driver.implicitly_wait(30)
    UsernameInput = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextUserName"]')   
    

    UsernameInput.send_keys("testpnx2")
    driver.implicitly_wait(30)
    NextButton.click()
    driver.implicitly_wait(30)
    ConfirmButtomShit = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Yes, next"]')
    ConfirmButtomShit.click()
    time.sleep(2)
    PayButton = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Pay"]')
    PayButton.click()
    time.sleep(2)
    
    SeccessfulPayment = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.TextView[@text="Successful payment"]')
    SeccessfulPayment.click()
    if SeccessfulPayment:
        GotItButton = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Got it"]')
        GotItButton.click()
        if GotItButton:
            print("Nigeria Member Order By Coin is : pass ✅")
            watchlog_instance.increment('OrderCountryMemberByCoinByCoinPass')
        else:
            print("Nigeria Member Order By Coin is : Failed ❌")
            watchlog_instance.increment('OrderCountryMemberByCoinByCoinFailed')
            
    else:
            print("Too Many Order For Channel In Memeber Nigeria is : Failed ❌")
