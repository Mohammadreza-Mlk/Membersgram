import requests, json, time 
import json
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction


url = 'http://localhost:4721'

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}


global activationId
activationId="22222222222" 

def GetNumberApi():
    GetNumber = 'https://fotorplusapi.membersgram.com/getnumber'
    response = requests.get(GetNumber)
    global activationId 
    activationId = ''
    global PhoneNumber
    PhoneNumber = ''
    print(PhoneNumber)
    if response.status_code == 200:
        print("\033[32mResponseCode is : 200")
        Api_Received = json.loads(response.text).get("data")
        print('Content received from Api :    ', Api_Received)
        PhoneNumber = json.loads(response.text).get("data").get("phonenumber")
        activationId = json.loads(response.text).get("data").get("activationId")
    print("PhoneNumber in func = " f'{PhoneNumber}')
    print("activationId in func = " f'{activationId}')
    return(PhoneNumber, activationId)


def GetVerifycode(activationId, driver_SamsungA71):
    # verifyCode = ""
    print('activation =' f'{activationId}')
    touch = TouchAction(driver_SamsungA71)

    for repeat_for_getCode in range(1, 12):
        time.sleep(20)
        RequestForVerifyCode = 'https://fotorplusapi.membersgram.com/getcode'
        headers = {'activationId': f'{activationId}'}
        response_verify = requests.get(RequestForVerifyCode, headers=headers)
        print(response_verify.text)
        response_verifyCode = json.loads(response_verify.text).get("status")
        
        if response_verifyCode == 'STATUS_WAIT_CODE':
            print(f'{response_verifyCode}   ')
            if repeat_for_getCode == 11:
                print("CancelBuyPoneNumberApi")
                time.sleep(2)
                CancelBuyPoneNumberApi = 'https://fotorplusapi.membersgram.com/cancelPurchase'
                CancelBuyRequest = requests.get(CancelBuyPoneNumberApi, headers=headers)
                time.sleep(2)
                response_canscel = json.loads(CancelBuyRequest.text).get("status")
                time.sleep(2)
                print(CancelBuyRequest.text)
                print(response_canscel)
                try:
                    if response_canscel == 'ACCESS_CANCEL':
                        time.sleep(2)
                        
                    
                        print("edit number")
                        time.sleep(2)
                        print("sleep 2 secound")
                        
                        print("Back to EditNumber")
                        driver_SamsungA71.press_keycode(4)
                        print("Back to EditNumber")
                        time.sleep(2)
                        EditButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='//android.widget.TextView[@text="Edit"]')
                        time.sleep(2)
                        EditButton.click()
                        time.sleep(2)
                        backspaceButtonInKeybord = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='//android.view.ViewGroup/android.widget.ImageView')
                        touch.long_press(backspaceButtonInKeybord).release().perform()
                    

                        # time.sleep(2)
                        # backbutton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                        #                                 value='//android.widget.ImageView[@content-desc="Back"]')
                        # backbutton.click()
                        # time.sleep(2)
                        # EditButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                        #                                 value='//android.widget.TextView[@text="Edit"]')
                        # time.sleep(2)
                        # EditButton.click()
                        # time.sleep(2)
                        # backspaceButtonInKeybord = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                        #                                 value='//android.view.ViewGroup/android.widget.ImageView')
                        # touch.long_press(backspaceButtonInKeybord).release().perform()
                    
                        
                except:
                    print("back for phone failde")
                
        else:
            print(' Verification code received.')
            response_codeTe = response_verify.text  # ذخیره محتوای دریافتی در متغیر
            print('Response ', response_codeTe)
            verificationcodeTel = json.loads(response_codeTe).get("data").get("smsCode")
            print(verificationcodeTel)
            break
            
    
    return verificationcodeTel


    
# GetNumberApi()
# GetVerifycode(activationId)