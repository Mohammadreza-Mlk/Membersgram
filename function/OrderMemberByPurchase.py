
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
def OrderMemberByPurchase(driver):

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
            watchlog_instance.increment('LoadPackageMemberByPurchaseFailed')
            RetryButton.click()
        else:
            print("Package Member is : Ok ✅")
            watchlog_instance.increment('LoadPackageMemberByPurchasePass')
    except:
        print("Package loaded")

    driver.implicitly_wait(10)
    WorldPackage = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="🌏  World"]')
    WorldPackage.click()
    driver.implicitly_wait(30)

        
    OrderMemberByPurchase = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.GridView[@content-desc="Member bundles list"]/android.view.ViewGroup[1]')
    OrderMemberByPurchase.click()
        
    try:
        time.sleep(2)
        MemberNotice = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.TextView[@text="Member order notice"]')
        
        if MemberNotice:
            
            time.sleep(11)
            CheckboxMemberNotice = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.CheckBox[@resource-id="gram.members.android:id/cbMemberNotice"]')

            CheckboxMemberNotice.click()
            Got_it_InMemberNotice = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Got it"]')
            Got_it_InMemberNotice.click()
    except:
        print("There is no member notice")
    driver.implicitly_wait(30)
    NextButton = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Next"]')
    NextButton.click()
    driver.implicitly_wait(30)
    EmptyIdError = driver.find_element(by=AppiumBy.XPATH,
                        value='//*[contains(@text, "Username must not be empty")]')
    if EmptyIdError:
        print("Empty Id Error via purchase is : pass ✅")
        watchlog_instance.increment('EmptyIdErrorByPurchasePass')
    else:
        print("Empty Id Error via purchase is : Failed ❌")
        watchlog_instance.increment('EmptyIdErrorByPurchaseFailed')
    UsernameInput = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextUserName"]')
    UsernameInput.send_keys("1111")
    NextButton = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Next"]')
    NextButton.click()
    driver.implicitly_wait(30)
    FormatIdError = driver.find_element(by=AppiumBy.XPATH,
                        value='//*[contains(@text, "Format is incorrect")]')
    if FormatIdError:
        print("Format Id incorrect Error via purchase is : pass ✅")
        watchlog_instance.increment('FormatIdIncorrectErrorByPurchasePass')
    else:
        print("Format Id incorrect Error via purchase is : Failed ❌")
        watchlog_instance.increment('FormatIdIncorrectErrorByPurchaseFailed')
    UsernameInput.send_keys("testpnx3")
    time.sleep(1)
    NextButton = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Next"]')
    NextButton.click()
     
        
        
    driver.implicitly_wait(30) 
    
    ConfirmButtomShit = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Yes, next"]')
    ConfirmButtomShit.click()
    driver.implicitly_wait(30)
    PayButton = driver.find_element(by=AppiumBy.XPATH,
                            value='//android.widget.Button[@text="Pay"]')
    PayButton.click()
   
    # driver.implicitly_wait(30)
    # AgreeButtonInGoogleButtomsheet = driver.find_element(by=AppiumBy.XPATH,
    #     value='//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]')
    # AgreeButtonInGoogleButtomsheet.click()
    driver.implicitly_wait(30)

    OneTapBuy = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]')
    OneTapBuy.click()
    driver.implicitly_wait(30)
    
    SeccessfulPayment = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.TextView[@text="Successful payment"]')
    SeccessfulPayment.click()
    if SeccessfulPayment:
        GotItButton = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Got it"]')
        GotItButton.click()
        HomeTab = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.FrameLayout[@content-desc="Home"]')
        HomeTab.click()
        if GotItButton:
            print("Order Member By Purchase is : pass ✅")
            watchlog_instance.increment('OrderMemberByPurchasePass')
             
        else:
            print("Order Member By Purchase is : Failed ❌")
            watchlog_instance.increment('OrderMemberByPurchaseFailed')
                
                #####################################
                #####################################
                #####################################
                
    
    

    # for OrderCount in range(3):
         
    #     WorldPackage = driver.find_element(by=AppiumBy.XPATH,
    #                 value='//android.widget.Button[@text="🌏  World"]')
    #     WorldPackage.click()
    #     driver.implicitly_wait(30)
    #     OrderMemberByPurchase = driver.find_element(by=AppiumBy.XPATH,
    #                 value='//android.widget.GridView[@content-desc="Member bundles list"]/android.view.ViewGroup[1]')
    #     OrderMemberByPurchase.click()
    #     driver.implicitly_wait(30)
    #     UsernameInput = driver.find_element(by=AppiumBy.XPATH,
    #                     value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextUserName"]')
    #     UsernameInput.send_keys("testpnx3")
    #     NextButton = driver.find_element(by=AppiumBy.XPATH,
    #                     value='//android.widget.Button[@text="Next"]')
    #     NextButton.click()
    #     try:          
    #         driver.implicitly_wait(30) 

    #         ConfirmButtomShit = driver.find_element(by=AppiumBy.XPATH,
    #                         value='//android.widget.Button[@text="Yes, next"]')
    #         ConfirmButtomShit.click()
    #         driver.implicitly_wait(30)
    #         PayButton = driver.find_element(by=AppiumBy.XPATH,
    #                             value='//android.widget.Button[@text="Pay"]')
    #         PayButton.click()
    #         driver.implicitly_wait(30)
            
    #         AgreeButtonInGoogleButtomsheet = driver.find_element(by=AppiumBy.XPATH,
    #             value='//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]')
    #         AgreeButtonInGoogleButtomsheet.click()
    #         driver.implicitly_wait(30)

    #         OneTapBuy = driver.find_element(by=AppiumBy.XPATH,
    #                         value='//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]')
    #         OneTapBuy.click()
    #         driver.implicitly_wait(30)
    #     except:
    #         print()
    #     try:
    #         SeccessfulPayment = driver.find_element(by=AppiumBy.XPATH,
    #                             value='//android.widget.TextView[@text="Successful payment"]')
    #         SeccessfulPayment.click()
        
    #         if SeccessfulPayment:
    #             GotItButton = driver.find_element(by=AppiumBy.XPATH,
    #                             value='//android.widget.Button[@text="Got it"]')
    #             GotItButton.click()
    #     except:
    #         print()
    #     try:
    #         TooManyOrderForChannel = driver.find_element(by=AppiumBy.XPATH,
    #                             value='//android.widget.TextView[@text="Too many orders in progress"]')
    #     except:
    #         print("")
    #     if TooManyOrderForChannel:
    #             print("Too Many Order For Channel via purchase is : pass ✅")
    #             watchlog_instance.increment('TooManyOrderForChannelByPurchasePass')
    #             OkForTooManyChannel = driver.find_element(by=AppiumBy.XPATH,
    #                         value='//android.widget.Button[@text="OK"]')
    #             OkForTooManyChannel.click()
    #             driver.implicitly_wait(30)
    #             Backbutton = driver.find_element(by=AppiumBy.XPATH,
    #                         value='//android.widget.ImageButton[@content-desc="Navigate up"]')
    #             Backbutton.click()
    #             time.sleep(2)
    #     else:
    #             print("Too Many Order For Channel via purchase is : Failed ❌")
    #             watchlog_instance.increment('TooManyOrderForChannelByPurchaseFiled')
    #             driver.implicitly_wait(30) 
                        
                    
                    
    #           
                    
    NigeriaMember = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Nigeria"]')
    NigeriaMember.click()              
    driver.implicitly_wait(30)
    GetMemberByPurchaseNigeria = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.GridView[@content-desc="Member bundles list"]/android.view.ViewGroup[1]')

    GetMemberByPurchaseNigeria.click()
    driver.implicitly_wait(30)
    NextButton = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Next"]')
    NextButton.click()
    driver.implicitly_wait(30)
    EmptyIdError = driver.find_element(by=AppiumBy.XPATH,
                        value='//*[contains(@text, "Username must not be empty")]')
    if EmptyIdError:
        print("Empty Id In country order via purchase Error is : pass ✅")
        watchlog_instance.increment('EmptyIdIncorrectInCountryOrderErrorByPurchasePass')
    else:
        print("Empty Id  In country order via purchase Error is : Failed ❌")
        watchlog_instance.increment('EmptyIdIncorrectInCountryOrderErrorByPurchaseFiled')
    UsernameInput = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextUserName"]')
    UsernameInput.send_keys("1111")
    NextButton = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Next"]')
    NextButton.click()
    driver.implicitly_wait(30)
    FormatIdError = driver.find_element(by=AppiumBy.XPATH,
                        value='//*[contains(@text, "Format is incorrect")]')
    if FormatIdError:
        print("Format Id incorrect In country order Error via purchase is : pass ✅")
        watchlog_instance.increment('FormatIdIncorrectInCountryOrderErrorByPurchasePass')
    else:
        print("Format Id incorrect In country order Error via purchase is : Failed ❌")
        watchlog_instance.increment('FormatIdIncorrectInCountryOrderErrorByPurchaseFiled')
        
     
    UsernameInput.send_keys("testpnx3")
    NextButton.click()

    driver.implicitly_wait(30)
    TooManyOrderForChannel = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.TextView[@text="Too many orders in progress"]')
    if TooManyOrderForChannel:
            print("Too Many Order For Channel in country order via purchase is : pass ✅")
            watchlog_instance.increment('TooManyOrderForChannelByPurchasePass')
            
            OkForTooManyChannel = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="OK"]')
            OkForTooManyChannel.click()
            driver.implicitly_wait(30)
            
            UsernameInput = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextUserName"]')
            UsernameInput.send_keys("testpnx4")
            driver.implicitly_wait(30)
            NextButton.click()
            driver.implicitly_wait(30) 
            ConfirmButtomShit = driver.find_element(by=AppiumBy.XPATH,
                            value='//android.widget.Button[@text="Yes, next"]')
            ConfirmButtomShit.click()
            driver.implicitly_wait(30)
            PayButton = driver.find_element(by=AppiumBy.XPATH,
                                value='//android.widget.Button[@text="Pay"]')
            PayButton.click()
            driver.implicitly_wait(30)
            
            # AgreeButtonInGoogleButtomsheet = driver.find_element(by=AppiumBy.XPATH,
            #     value='//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]')
            # AgreeButtonInGoogleButtomsheet.click()
            # driver.implicitly_wait(30)

            OneTapBuy = driver.find_element(by=AppiumBy.XPATH,
                            value='//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]')
            OneTapBuy.click()
            driver.implicitly_wait(30)
            SeccessfulPayment = driver.find_element(by=AppiumBy.XPATH,
                                value='//android.widget.TextView[@text="Successful payment"]')
            SeccessfulPayment.click()
            if SeccessfulPayment:
                GotItButton = driver.find_element(by=AppiumBy.XPATH,
                                value='//android.widget.Button[@text="Got it"]')
                GotItButton.click()
                HomeTab = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.FrameLayout[@content-desc="Home"]')
                HomeTab.click()
                if GotItButton:
                    time.sleep(4)
                    print("Nigeria Member Order By Purchase is : pass ✅")
                    watchlog_instance.increment('OrderCountryMemberByPurchasePass')
                else:
                    print("Nigeria Member Order By Purchase is : Failed ❌")
                    watchlog_instance.increment('OrderCountryMemberByPurchaseFailed')
                   
            else:
                    print("Too Many Order For Channel In Memeber Nigeria via purchase is : Failed ❌")
                    watchlog_instance.increment('TooManyOrderForChannelByPurchaseFailed')
        # else:
        