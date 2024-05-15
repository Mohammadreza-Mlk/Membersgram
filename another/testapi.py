import requests
import json
import time

activationId = '2419560668'
codeTel = ''
for m in range(10):
    time.sleep(5)
    RequestNumberOneVerifyCode = 'https://fotorplusapi.membersgram.com/getcode'
    headers = {
        'activationId': f'{activationId}'
    }
    response_verify = requests.get(RequestNumberOneVerifyCode, headers=headers)
    print(response_verify.text)
    response_verifyCode = json.loads(response_verify.text).get("status")
    if response_verifyCode == 'STATUS_WAIT_CODE':{
                    print('Verification code not received')

                                                }
            
    else:
            print(' Verification code received.')
            response_codeTe = response_verify.text  # ذخیره محتوای دریافتی در متغیر
            print('Response ', response_codeTe)
            codeTel = json.loads(response_codeTe).get("data").get("smsCode")
            print(codeTel)
            break