import requests
import json

def GetNumber():
    GetNumberUrl = 'https://fotorplusapi.membersgram.com/getnumber'
    try:
        response = requests.get(GetNumberUrl)
        activationId = ''
        PhoneNumber1 = ''
        if response.status_code == 200:
            print("\033[32mResponseCode is : 200")
            Api_Received = json.loads(response.text).get("data")
            print('Content received from Api :    ', Api_Received)
            PhoneNumber1 = Api_Received.get("phonenumber")
            activationId = Api_Received.get("activationId")
        print(PhoneNumber1)
        print(activationId)
    except Exception as e:
        print("Error occurred:", e)

# فراخوانی تابع GetNumber
GetNumber()
