import requests
import json,time

def CancelNumber():
    activationId = "172593576"
    headers = {'activationId': f'{activationId}'}
        
    CancelBuyPoneNumberApi = 'https://fotorplusapi.membersgram.com/cancelPurchase'
    CancelBuyRequest = requests.get(CancelBuyPoneNumberApi, headers=headers)
    print(CancelBuyRequest.text)
    time.sleep(2)
    # if CancelBuyRequest.text.status == "ACCESS_CANCEL":
    #     print(CancelBuyRequest.text)
    # else:
    #     time.sleep(10)
    #     CancelBuyRequest = requests.get(CancelBuyPoneNumberApi, headers=headers)
    #     print(CancelBuyRequest.text)
# فراخوانی تابع GetNumber
CancelNumber()
