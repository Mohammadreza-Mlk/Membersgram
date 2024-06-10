import requests
import json
import time

activationId = '176142160'
codeTel = ''
for m in range(10):
    RequestForVerifyCode = 'https://fotorplusapi.membersgram.com/getcode'
    headers = {'activationId': f'{activationId}'}
    response_verify = requests.get(RequestForVerifyCode, headers=headers)
    print(response_verify.text)
    response_verifyCode = json.loads(response_verify.text).get("status")