import requests, json, time 
import json
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
url = 'http://localhost:4721'

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}

driver_SamsungA71 = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
global activationId 

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
    print(PhoneNumber)
    print(activationId)
    return(PhoneNumber, activationId)


def GetVerifycode(activationId):
    # verifyCode = ""
    print(activationId)
    
    for repeat_for_getCode in range(1, 11):
        time.sleep(20)
        RequestForVerifyCode = 'https://fotorplusapi.membersgram.com/getcode'
        headers = {'activationId': f'{activationId}'}
        response_verify = requests.get(RequestForVerifyCode, headers=headers)
        print(response_verify.text)
        response_verifyCode = json.loads(response_verify.text).get("status")
        
        if response_verifyCode == 'STATUS_WAIT_CODE':
            print('Verification code not received')
            if repeat_for_getCode == 10:
                time.sleep(2)
                CancelBuyPoneNumberApi = 'https://fotorplusapi.membersgram.com/cancelPurchase'
                CancelBuyRequest = requests.get(CancelBuyPoneNumberApi, headers=headers)
                time.sleep(2)
                driver_SamsungA71.press_keycode(4)
                if CancelBuyRequest.status_code == 200:
                    print(CancelBuyPoneNumberApi)
            
        else:
            print(' Verification code received.')
            response_codeTe = response_verify.text  # ذخیره محتوای دریافتی در متغیر
            print('Response ', response_codeTe)
            verificationcodeTel = json.loads(response_codeTe).get("data").get("smsCode")
            print(verificationcodeTel)
            break
            
    
    return verificationcodeTel










































    
                # print('Verification code not received')
                # if repeat_for_getCode == 10:
                #     time.sleep(2)
                #     CancelBuyPoneNumberApi = 'https://fotorplusapi.membersgram.com/cancelPurchase'
                #     CancelBuyRequest = requests.get(CancelBuyPoneNumberApi, headers=headers)
                #     time.sleep(2)
                #     driver_SamsungA71.press_keycode(4)
                #     if CancelBuyRequest.status_code == 200:
                #         print(CancelBuyPoneNumberApi)
                                
                #     else:
                #         print(' Verification code received.')
                #         response_codeTe = response_verify.text  # ذخیره محتوای دریافتی در متغیر
                #         print('Response ', response_codeTe)
                #         global verificationcodeTel
                #         verificationcodeTel = json.loads(response_codeTe).get("data").get("smsCode")
                #         print(verificationcodeTel)
                #         return verificationcodeTel
                #         break
    
    
   
    
# if response_verifyCode == 'STATUS_WAIT_CODE':
#             print(' Verification code not received.')
#             response_codeTe = response_verify.text  # ذخیره محتوای دریافتی در متغیر
#             print('Response ', response_codeTe)
#             verifyCode = json.loads(response_codeTe).get("data").get("smsCode")
#             print(verifyCode)
    
    
    
    
    
    
    
    
# GetNumberApi()
# GetVerifycode(activationId)