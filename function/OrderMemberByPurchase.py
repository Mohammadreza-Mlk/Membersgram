
from appium.webdriver.common.appiumby import AppiumBy
import sys, time
sys.path.append("../TelegramAuto")
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import sys, time

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
            RetryButton.click()
        else:
            print("Package Member is : Ok ✅")
    except:
        print("Package loaded")

    driver.implicitly_wait(5)
    WorldPackage = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="🌏  World"]')
    WorldPackage.click()
    driver.implicitly_wait(5)

        
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
    driver.implicitly_wait(5)
    NextButton = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Next"]')
    NextButton.click()
    driver.implicitly_wait(5)
    EmptyIdError = driver.find_element(by=AppiumBy.XPATH,
                        value='//*[contains(@text, "Username must not be empty")]')
    if EmptyIdError:
        print("Empty Id Error via purchase is : pass ✅")
    else:
        print("Empty Id Error via purchase is : Failed ❌")
        
    UsernameInput = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextUserName"]')
    UsernameInput.send_keys("1111")
    NextButton = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Next"]')
    NextButton.click()
    driver.implicitly_wait(5)
    FormatIdError = driver.find_element(by=AppiumBy.XPATH,
                        value='//*[contains(@text, "Format is incorrect")]')
    if FormatIdError:
        print("Format Id incorrect Error via purchase is : pass ✅")
    else:
        print("Format Id incorrect Error via purchase is : Failed ❌")
    UsernameInput.send_keys("testpnx3")
    NextButton.click()
    driver.implicitly_wait(5)
        
        
    driver.implicitly_wait(5) 
    ConfirmButtomShit = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Yes, next"]')
    ConfirmButtomShit.click()
    driver.implicitly_wait(5)
    PayButton = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Pay"]')
    PayButton.click()
    driver.implicitly_wait(5)
    
    AgreeButtonInGoogleButtomsheet = driver.find_element(by=AppiumBy.XPATH,
        value='//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]')
    AgreeButtonInGoogleButtomsheet.click()
    driver.implicitly_wait(5)

    OneTapBuy = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]')
    OneTapBuy.click()
    driver.implicitly_wait(15)
    
    SeccessfulPayment = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.TextView[@text="Successful payment"]')
    SeccessfulPayment.click()
    if SeccessfulPayment:
        GotItButton = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Got it"]')
        GotItButton.click()
        if GotItButton:
            print("Order Member By Purchase is : pass ✅")
        else:
            print("Order Member By Purchase is : Failed ❌")
                
                #####################################
                #####################################
                #####################################
                
    OrderMemberByPurchase = driver.find_element(by=AppiumBy.XPATH,
            value='//android.widget.GridView[@content-desc="Member bundles list"]/android.view.ViewGroup[1]')
    OrderMemberByPurchase.click()
    UsernameInput = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextUserName"]')
    UsernameInput.send_keys("testpnx3")
    driver.implicitly_wait(5)
    NextButton = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Next"]')
    NextButton.click()
    
    driver.implicitly_wait(5)
    TooManyOrderForChannel = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.TextView[@text="Too many orders in progress"]')
    if TooManyOrderForChannel:
            print("Too Many Order For Channel via purchase is : pass ✅")
            OkForTooManyChannel = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="OK"]')
            OkForTooManyChannel.click()
            driver.implicitly_wait(5)
            Backbutton = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.ImageButton[@content-desc="Navigate up"]')
            Backbutton.click()
            time.sleep(2)
    else:
            print("Too Many Order For Channel via purchase is : Failed ❌")
            driver.implicitly_wait(5) 
                    
                    
                    
    #           
                    
    NigeriaMember = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Nigeria"]')
    NigeriaMember.click()              
    driver.implicitly_wait(5)
    GetMemberByPurchaseNigeria = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.GridView[@content-desc="Member bundles list"]/android.view.ViewGroup[1]')

    GetMemberByPurchaseNigeria.click()
    driver.implicitly_wait(5)
    NextButton = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Next"]')
    NextButton.click()
    driver.implicitly_wait(5)
    EmptyIdError = driver.find_element(by=AppiumBy.XPATH,
                        value='//*[contains(@text, "Username must not be empty")]')
    if EmptyIdError:
        print("Empty Id Empty In country order via purchase Error is : pass ✅")
    else:
        print("Empty Id Empty In country order via purchase Error is : Failed ❌")
        
    UsernameInput = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextUserName"]')
    UsernameInput.send_keys("1111")
    NextButton = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Next"]')
    NextButton.click()
    driver.implicitly_wait(5)
    FormatIdError = driver.find_element(by=AppiumBy.XPATH,
                        value='//*[contains(@text, "Format is incorrect")]')
    if FormatIdError:
        print("Format Id incorrect In country order Error via purchase is : pass ✅")
    else:
        print("Format Id incorrect In country order Error via purchase is : Failed ❌")
        
     
    UsernameInput.send_keys("testpnx3")
    NextButton.click()

    driver.implicitly_wait(5)
    TooManyOrderForChannel = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.TextView[@text="Too many orders in progress"]')
    if TooManyOrderForChannel:
            print("Too Many Order For Channel in country order via purchase is : pass ✅")
            
            OkForTooManyChannel = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="OK"]')
            OkForTooManyChannel.click()
            driver.implicitly_wait(5)
            
            UsernameInput = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextUserName"]')
            UsernameInput.send_keys("testpnx4")
            driver.implicitly_wait(5)
            NextButton.click()
            driver.implicitly_wait(5) 
            ConfirmButtomShit = driver.find_element(by=AppiumBy.XPATH,
                            value='//android.widget.Button[@text="Yes, next"]')
            ConfirmButtomShit.click()
            driver.implicitly_wait(5)
            PayButton = driver.find_element(by=AppiumBy.XPATH,
                                value='//android.widget.Button[@text="Pay"]')
            PayButton.click()
            driver.implicitly_wait(5)
            
            AgreeButtonInGoogleButtomsheet = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]')
            AgreeButtonInGoogleButtomsheet.click()
            driver.implicitly_wait(5)

            OneTapBuy = driver.find_element(by=AppiumBy.XPATH,
                            value='//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]')
            OneTapBuy.click()
            driver.implicitly_wait(15)
            SeccessfulPayment = driver.find_element(by=AppiumBy.XPATH,
                                value='//android.widget.TextView[@text="Successful payment"]')
            SeccessfulPayment.click()
            if SeccessfulPayment:
                GotItButton = driver.find_element(by=AppiumBy.XPATH,
                                value='//android.widget.Button[@text="Got it"]')
                GotItButton.click()
                if GotItButton:
                    time.sleep(4)
                    print("Nigeria Member Order By Purchase is : pass ✅")
                else:
                    print("Nigeria Member Order By Purchase is : Failed ❌")
                   
            else:
                            print("Too Many Order For Channel In Memeber Nigeria via purchase is : Failed ❌")
        # else:
        #     driver.quit()