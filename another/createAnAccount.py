from _ast import expr
import requests
import json
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time
from NameAccount import Account_names, RandomAccountNames

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
    'language': 'en',
    'locale': 'us'
}

url = 'http://localhost:4723'

driver_samsung_j5 = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
touch = TouchAction(driver_samsung_j5)

for i in range(1000):
    # start creating an account
    StartMessage = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                       value='//android.widget.TextView[@text="Start Messaging"]')
    StartMessage.click()
    time.sleep(1)
    ##########
    ##########
    PhoneNumberInput = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                           value='//android.widget.EditText[@content-desc="Country code"]')

    if PhoneNumberInput:
            print("PhoneNumberInput found! Start phone number giving")
            # get phone number of API

            RequestNumberOne = 'https://fotorplusapi.membersgram.com/getnumber'

            response = requests.get(RequestNumberOne)
            activationId = ''
            PhoneNumber1 = ''
            if response.status_code == 200:
                print(' موفقیت‌آمیز .')
                print('محتوای دریافتی: ', response.text)
                Api_Received = json.loads(response.text).get("data")
                print(Api_Received)
                PhoneNumber1 = json.loads(response.text).get("data").get("phonenumber")
                print(PhoneNumber1)

                activationId = json.loads(response.text).get("data").get("activationId")

            print(PhoneNumber1)
            time.sleep(2)
            PhoneNumberInput.send_keys(PhoneNumber1)
            # click On next
            time.sleep(2)
            touch.tap(x=600, y=750).release().perform()
            time.sleep(1)
            touch.tap(x=600, y=750).release().perform()
            time.sleep(20)

            try:
                VerificationInputBoxCodeTelegram = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                       value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]')

                if VerificationInputBoxCodeTelegram:
                    print("Phone Number IS Ok")
                    # گرفتن کد از Api
                    time.sleep(15)

                    print(f'{activationId}')
                    RequestNumberOneVerifyCode = 'https://fotorplusapi.membersgram.com/getcode'
                    headers = {
                        'activationId': f'{activationId}'
                    }
                    response_verify = requests.get(RequestNumberOneVerifyCode, headers=headers)
                    print("* * * * * *")
                    print(response_verify)
                    if response_verify.status_code == 200:
                        print(' موفقیت‌آمیز .')
                        response_codeTe = response_verify.text  # ذخیره محتوای دریافتی در متغیر
                        print('محتوای دریافتی: ', response_codeTe)
                        codeTel = json.loads(response_codeTe).get("data").get("smsCode")
                        print(codeTel)
                        time.sleep(5)
                        # وارد کردن کد
                        VerificationInputBoxCodeTelegram.send_keys(codeTel)
                        time.sleep(5)

                    else:
                        print("heeeel2")

                    # چک کردن وجود داشتن باکس نام
                    try:

                        NAmeInput = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                        value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.EditText')
                        if NAmeInput:
                            random_names = RandomAccountNames[i]
                            print(f'name tis account is : {random_names}')
                            time.sleep(0.5)
                            NAmeInput.send_keys(random_names)

                            NAmeInputNextButton = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                      value='//android.widget.FrameLayout[@content-desc="Done"]/android.view.View')
                            NAmeInputNextButton.click()

                            # در بعضی کد کشور ها بعد از ثبت نام  یک ترم آف سرویس میاورد

                            try:

                                TermOfService = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                    value='//android.widget.TextView[@text="Terms of Service"]')
                                if TermOfService:
                                    TermOfServiceAccept = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                              value='//android.widget.TextView[@text="Accept"]')
                                    TermOfServiceAccept.click()
                            except Exception as e:
                                print("Term of service not fount")
                                
                            try:
                                print("\033[32m*********** *********** Start for on Samsung for *********** *********** .\033[0m")
                                time.sleep(2)

                                #####################################
                                #        مراحل فروش اکانت ـ        ##
                                #####################################

                                time.sleep(3)
                                SearchButton = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                            value='//android.widget.ImageButton[@content-desc="Search"]/android.widget.ImageView')
                                SearchButton.click()
                                SearchInput = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                            value='//android.widget.EditText[@text="Search"]')
                                SearchInput.send_keys("fotor_plus_bot")
                                time.sleep(10)
                                print("type fotor is ok")

                                touch.tap(x=400, y=300).release().perform()
                                time.sleep(2)
                                # touch.tap(x=346, y=1230).release().perform()
                                
                                #BotKeyboard = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                #                                           value='//android.widget.ImageView[@content-desc="Bot keyboard"]')
                                # BotKeyboard.click()
                                time.sleep(2)

                                SellingAccount = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                            value='//android.widget.TextView[@text="Sending an account (selling an account)"]')
                                SellingAccount.click()

                                MessageBox = driver_samsung_j5.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Message"]')
                                time.sleep(5)

                                MessageBox.send_keys("+447399161722")

                                SendMessageIcon = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                value='//android.view.View[@content-desc="Send"]')
                                SendMessageIcon.click()
                                time.sleep(20)

                                BackButton = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                            value='//android.widget.ImageView[@content-desc="Go back"]')
                                BackButton.click()
                                time.sleep(3)
                                SearchButton.click()

                                SearchInput.send_keys("telegram")
                                time.sleep(2)

                                touch.tap(x=400, y=250).release().perform()

                                ##########
                                ##########

                                time.sleep(3)
                                # press on the final telegram message
                                touch.long_press(x=500, y=1100).release().perform()
                                # tap on copy icon
                                touch.tap(x=460, y=124).release().perform()
                                time.sleep(1)
                                BackButtonTelegramChat = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                        value='//android.widget.ImageView[@content-desc="Go back"]')
                                BackButtonTelegramChat.click()
                                time.sleep(2)

                                SearchButton.click()
                                time.sleep(2)

                                SearchInput.send_keys("fotor_plus_bot")

                                time.sleep(5)
                                print("type fotor is ok")

                                touch.tap(x=400, y=300).release().perform()
                                #######
                                #######
                                ######
                                #########
                                #########
                                MessageBox = driver_samsung_j5.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Message"]')

                                MessageBox.click()
                                time.sleep(2)

                                touch.long_press(x=245, y=610).release().perform()
                                time.sleep(1)

                                touch.tap(x=70, y=530).release().perform()

                                time.sleep(2)
                                print("message pasted")
                                # پاک کردن اضافه پیام برای نمایان شدن متن کد
                                for m in range(2):
                                    # location of mark massage to delete
                                    start_point = {'x': 120, 'y': 491}
                                    end_point = {'x': 400, 'y': 625}

                                    touch.long_press(x=start_point['x'], y=start_point['y']).move_to(x=end_point['x'], y=end_point['y']).release().perform()
                                    touch.tap(x=660, y=1100).release().perform()

                                touch.tap(x=350, y=444).release().perform()
                                touch.long_press(x=350, y=444).release().perform()
                                touch.tap(x=272, y=350).release().perform()
                                startClearAll = {'x': 117, 'y': 435}
                                endClearAll = {'x': 530, 'y': 622}

                                touch.long_press(x=startClearAll['x'], y=startClearAll['y']).move_to(x=endClearAll['x'], y=endClearAll['y']).release().perform()

                                touch.tap(x=660, y=1100).release().perform()
                                touch.long_press(x=660, y=1100).release().perform()
                                MessageBox.send_keys("fotor_")
                                # long press for open the menu for paste button
                                touch.long_press(x=300, y=607).release().perform()
                                # tap on paste button
                                touch.tap(x=103, y=531).release().perform()
                                touch.tap(x=245, y=607).release().perform()
                                time.sleep(1)
                                SendButton = driver_samsung_j5.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Send"]')
                                SendButton.click()
                                time.sleep(2)
                                BackButton.click()
                            except Exception as e:
                                print('')
                    except Exception as e:
                        print("account created")

                    #

                    #

                    # end create account
                # دکمه هوم گوشی

                # driver.press_keycode(3)
            except Exception as e:
                print(f"Error: verification code not find {e}")

            try:
                PhoneNumberBanned = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                        value='//android.widget.TextView[@text="This phone number is banned."]')

                if PhoneNumberBanned:
                    okButtonBanned = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                         value='//android.widget.TextView[@text="OK"]')
                    print("PhoneNumberBanned")
                    okButtonBanned.click()
                    BackspaceButton = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                          value='//android.view.ViewGroup/android.widget.ImageView')

                    for BackspaceButtonCount in range(2):
                        touch.long_press(BackspaceButton).wait(1).release().perform()
            except Exception as e:
                print(f"Error: #### banned is not true #### {e}")

    else:
            print("محدود شدن در ثبت نام اکانت")
            time.sleep(25200)
