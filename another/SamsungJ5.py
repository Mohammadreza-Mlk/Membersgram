import requests
import json
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time
import random


Account_names = [
    "Emir", "Kerem", "Arda", "Can", "Ali", "Selim", "Ege", "Umut", "Baran", "Burak", "Deniz", "Yusuf", "Oğuz", "Kaan", "Mete", "Berk", "Cem", "Taylan", "Serkan", "Eren","Ömer", "Alp", "Kuzey", "Kaya", "Orhan", "Hakan", "Mert", "Levent", "Volkan", "Tolga",
    "Serdar", "Ertan", "Ferit", "lker", "Taner", "Emre", "Onur", "Halit", "Ilgın", "Akın", "Aarav", "Aryan", "Aditya", "Arjun", "Rohan", "Siddharth", "Akshay", "Virat", "Kunal", "Varun","Aakash", "Rahul", "Dev", "Harsh", "Yash", "Aniket", "Kabir", "Rishi", "Arnav", "Karan",
    "Shivansh", "Jayden", "Ansh", "Vihaan", "Vedant", "Parth", "Krish", "Advait", "Ayaan", "Dhruv", "Neil", "Raghav", "Kabir", "Aadi", "Vivaan", "Arush", "Tanish", "Omkar", "Advik", "Shaurya",
    "Ishan", "Rehan", "Anshuman", "Vihaan", "Zayn", "Shreyansh", "Aarush", "Aryan", "Arnav", "Lakshya", "Adam", "Jakub", "Kacper", "Szymon", "Mateusz", "Michał", "Filip", "Aleksander", "Mikołaj", "Wojciech", "Paweł", "Jan", "Wiktor", "Igor", "Alan", "Adrian", "Patryk", "Damian", "Oskar", "Artur", "Łukasz", "Bartosz", "Piotr", "Daniel", "Krzysztof", "Marcel", "Hubert", "Tomasz", "Dominik", "Sebastian", "Kamil", "Dawid", "Jacek", "Rafał", "Karol", "Sławomir", "Grzegorz", "Igor", "Radosław", "Dariusz", "Łukasz", "Marek", "Bogdan", "Zbigniew", "Jarosław", "Aleks", "Konrad", "Krystian", "Arkadiusz", "Edward",
    "Erkan", "Cihan", "Tarkan", "Gokhan", "Serhat", "Sinan", "Kaan", "Murat", "Oktay", "Arif", "आरव", "आर्यन", "आदित्य",
    "अर्जुन", "रोहन", "सिद्धार्थ", "अक्षय", "विराट", "कुणाल", "वरुण", "आकाश", "राहुल", "देव", "हर्ष", "यश", "अनिकेत",
    "कबीर", "रिषि", "अर्णव", "करण",  "शिवांश", "जेडन", "आंश", "विहान", "वेदांत", "पार्थ", "कृष", "आद्वैत", "आयान", "ध्रुव",  "नील", "रघव", "कबीर", "आदि", "विवान", "आरुष", "तनिष", "ओमकार", "अद्विक", "शौर्य",  "ईशान", "रेहन", "आंशुमान", "विहान", "ज़यन", "श्रेयांश", "आरुष", "आर्यन", "अर्णव", "लक्ष्य",  "अर्थ", "हृदय", "रुद्र", "सार्थक", "ईश्वर", "आरुष", "अविनाश", "आरुष", "प्रणव", "विहान", "सर्वेश", "पारस", "आदित्य", "रुद्रांश", "रिषभ", "अभिनव", "वंश", "अंशुल", "दक्ष", "आर्य", "अंशिका", "आदर्श", "आर्यमान", "सुर्यांश", "श्लोक", "रिषित", "अनय", "युवराज", "आद्वय", "यथार्थ",
    "रित्विक", "आयुष", "समय", "अव्यक्त", "रेयांश", "परम", "कियान", "हृदान", "निवान", "आथर्व", "Serdar", "Gurbanguly",
    "Meret", "Döwlet", "Aman", "Nurmuhammet", "Maksat", "Arslan", "Atajan", "Çarymyrat", "Hoja", "Döwran", "Atamyrat", "Saparmyrat", "Yagşymyrat", "Suleyman", "Begmyrat", "Rejep", "Gorogly", "Ishanguly",
    "Çagamyrat", "Rovşen", "Baýram", "Balamyrat", "Döwranşa", "Durmuhammet", "Alym", "Garay", "Nazar", "Nebi",
    "Magtymguly", "Tagan", "Rejepguly", "Seyitmuhammet", "Kakajan", "Göçli", "Döwletgeldi", "Gün", "Azat", "Berdi", "Ata", "Gahryman", "Köçli", "Bolat", "Geldi", "Şageldi", "Çygyldam", "Muhammet", "Berdymyrat", "Wepa", "Gurban", "Nazarguly", "Myrat", "Durdi", "Atamyrat", "Bazar", "Allamyrat", "Zarif", "Chary", "Akmurat",
    "Jemşid", "Çolak", "Şiraly", "Garay", "Rejepmyrat", "Magtymgeldi", "Öwez", "Ata", "Dayanch", "Çelebi",
    "Geldi", "Azat", "Gochmyrat", "Amanmyrat", "Hojaguly", "Döwletmyrat", "Mälim", "Täçberdi", "Dayanç", "Göroglu",
    "Nury", "Begench", "Myrat", "Mämmed", "Annasoltan", "Täzel", "Begmyrat", "Ylham", "Bashim", "Atageldi"]

# ایاد آرایه اسم تصادفی برای اکانت
RandomAccountNames = random.sample(Account_names, 330)

caap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'platformVersion': '9.0',
    'deviceName': 'Samsung',
    'language': 'en',
    'locale': 'us'
}
url = 'http://localhost:4721'

driver_samsung_j5 = webdriver.Remote(url, options=AppiumOptions().load_capabilities(caap))
touch = TouchAction(driver_samsung_j5)

print("start create Account")


for i in range(20):
    time.sleep(2)
    PhoneNumberInput = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                          value='//android.widget.EditText[@content-desc="Country code"]')

    if PhoneNumberInput:
            print("PhoneNumberInput found! Start phone number giving :)")
            # get phone number of API
            GetNumber = 'https://fotorplusapi.membersgram.com/getnumber'
            response = requests.get(GetNumber)
            activationId = ''
            PhoneNumber1 = ''
            if response.status_code == 200:
                print("\033[32mResponseCode is : 200")
                Api_Received = json.loads(response.text).get("data")
                print('Content received from Api :    ', Api_Received)
                PhoneNumber1 = json.loads(response.text).get("data").get("phonenumber")
                activationId = json.loads(response.text).get("data").get("activationId")
            print(PhoneNumber1)
            print(activationId)
            time.sleep(2)
            PhoneNumberInput.send_keys(PhoneNumber1)
            time.sleep(2)
            touch.tap(x=600, y=750).release().perform()  # click On next
            time.sleep(1)
            touch.tap(x=600, y=750).release().perform()
            time.sleep(20)

            try:
                input_google_box =  driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                  value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout')
                if input_google_box:
                    
                    input_google_box.send_keys("pnxdevices@gmail.com")
                    time.sleep(1)
                    touch.tap(x=600, y=550).release().perform()
                    print("select the pnx@devices@gmail.cpm ")
                    time.sleep(15)
                    pnxEmail = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                  value='//android.widget.TextView[@resource-id="com.google.android.gms:id/account_name"]')
                          
                    pnxEmail.click()   
            except:
                print("Email box not found")
            try:
                VerificationInputBoxCodeTelegram = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                  value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]')

                time.sleep(90)
                print("stay fo 90 sec")
                Get_the_code_via_SMS = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                  value='//android.widget.TextView[@text="Get the code via SMS"]')
                
                print("Get_the_code_via_SMS step")
                if Get_the_code_via_SMS:
                        Get_the_code_via_SMS.click() 
                        time.sleep(2)
                        print("Get_the_code_via_SMS clicked")
                  
                try: 
                    if VerificationInputBoxCodeTelegram:
                        print("Phone Number IS Ok\033[0m")
                        # گرفتن کد از Api
                        print(f'{activationId}')
                    
                        if Get_the_code_via_SMS:
                            Get_the_code_via_SMS.click()
                            for repeat_for_getCode in range(1, 11):
                                time.sleep(20)
                                RequestNumberOneVerifyCode = 'https://fotorplusapi.membersgram.com/getcode'
                                headers = {
                                    'activationId': f'{activationId}'
                                }
                                response_verify = requests.get(RequestNumberOneVerifyCode, headers=headers)
                                print(response_verify.text)
                                response_verifyCode = json.loads(response_verify.text).get("status")
                                if response_verifyCode == 'STATUS_WAIT_CODE':
                                    print(f'{repeat_for_getCode : }Verification code not received')
                                    if repeat_for_getCode == 10:
                                        time.sleep(2)
                                        CancelBuyPoneNumberApi = 'https://fotorplusapi.membersgram.com/cancelPurchase'
                                        CancelBuyRequest = requests.get(CancelBuyPoneNumberApi, headers=headers)
                                        time.sleep(2)
                                        driver_samsung_j5.press_keycode(4)
                                        if CancelBuyRequest.status_code == 200:
                                            print(CancelBuyPoneNumberApi)

                                else:
                                    print(' Verification code received.')
                                    response_codeTe = response_verify.text  # ذخیره محتوای دریافتی در متغیر
                                    print('Response ', response_codeTe)
                                    verificationcodeTel = json.loads(response_codeTe).get("data").get("smsCode")
                                    print(verificationcodeTel)
                                    break
                        time.sleep(5)
                        # وارد کردن کد
                        VerificationInputBoxCodeTelegram.send_keys(verificationcodeTel)
                        time.sleep(5)
                        # چک کردن وجود داشتن باکس نام
                        driver_samsung_j5.press_keycode(4)
                        time.sleep(3)
                        NAmeInput = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.EditText')
                        random_names = RandomAccountNames[i]
                        print(f'name tis account is : {random_names}')
                        if NAmeInput:

                            time.sleep(0.5)
                            NAmeInput.send_keys(random_names)

                            NAmeInputNextButton = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                value='//android.widget.FrameLayout[@content-desc="Done"]/android.view.View')
                            NAmeInputNextButton.click()
                            time.sleep(2)

                            # در بعضی کد کشور ها بعد از ثبت نام  یک ترم آف سرویس میاورد

                            try:

                                TermOfService = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                            value='//android.widget.TextView[@text="Terms of Service"]')
                                if TermOfService:
                                    TermOfServiceAccept = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                        value='//android.widget.TextView[@text="Accept"]')
                                    TermOfServiceAccept.click()
                            except:
                                print("Term of service not fount")

                            print("$$$$$$$$$   Account created   $$$$$$$$$$$")
                            try:
                                print("\033[32m***********  Start for FOTOR PLUS  *********** .\033[0m")
                                time.sleep(10)

                                #####################################
                                #        مراحل فروش اکانت ـ        ##
                                #####################################
                                SearchButton = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                            value='//android.widget.ImageButton[@content-desc="Search"]/android.widget.ImageView')
                                SearchButton.click()
                                time.sleep(3)
                                SearchInput = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                            value='//android.widget.EditText[@text="Search"]')
                                SearchInput.send_keys("fotor_plus_bot")
                                print("type fotor is ok")
                                time.sleep(15)
                                touch.tap(x=400, y=300).release().perform()
                                time.sleep(5)
                                touch.tap(x=346, y=1230).release().perform()  # for start button of the bot
                                # BotKeyboard = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                #                                           value='//android.widget.ImageView[@content-desc="Bot keyboard"]')
                                # BotKeyboard.click()
                                time.sleep(5)

                                SellingAccount = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                value='//android.widget.TextView[@text="Sending an account (selling an account)"]')
                                SellingAccount.click()
                                time.sleep(3)
                                MessageBox = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                            value='//android.widget.EditText[@text="Message"]')
                                time.sleep(5)

                                MessageBox.send_keys(PhoneNumber1)

                                SendMessageIcon = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                value='//android.view.View[@content-desc="Send"]')
                                SendMessageIcon.click()
                                time.sleep(20)

                                BackButton = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                            value='//android.widget.ImageView[@content-desc="Go back"]')
                                BackButton.click()
                                time.sleep(10)
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
                                MessageBox = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                            value='//android.widget.EditText[@text="Message"]')

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

                                    touch.long_press(x=start_point['x'], y=start_point['y']).move_to(x=end_point['x'],
                                                                                                    y=end_point[
                                                                                                        'y']).release().perform()
                                    touch.tap(x=660, y=1100).release().perform()

                                touch.tap(x=350, y=444).release().perform()
                                touch.long_press(x=350, y=444).release().perform()
                                touch.tap(x=272, y=350).release().perform()
                                startClearAll = {'x': 117, 'y': 435}
                                endClearAll = {'x': 530, 'y': 622}

                                touch.long_press(x=startClearAll['x'], y=startClearAll['y']).move_to(x=endClearAll['x'],
                                                                                                    y=endClearAll[
                                                                                                        'y']).release().perform()

                                touch.tap(x=660, y=1100).release().perform()
                                touch.long_press(x=660, y=1100).release().perform()
                                MessageBox.send_keys("fotor_")
                                # long press for open the menu for paste button
                                touch.long_press(x=300, y=607).release().perform()
                                # tap on paste button
                                touch.tap(x=103, y=531).release().perform()
                                touch.tap(x=245, y=607).release().perform()
                                time.sleep(1)
                                SendButton = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                            value='//android.view.View[@content-desc="Send"]')
                                SendButton.click()
                                time.sleep(2)
                                touch.tap(x=54, y=106).release().perform()

                                try:  # log out from account
                                    time.sleep(2)

                                    NavigationMenu = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                    value='//android.widget.ImageView[@content-desc="Open navigation menu"]')
                                    NavigationMenu.click()
                                    time.sleep(2)
                                    touch.tap(x=300, y=985).release().perform()
                                    time.sleep(2)
                                    start_point = {'x': 530, 'y': 1000}
                                    # انتها
                                    end_point = {'x': 520, 'y': 300}
                                    touch.long_press(x=start_point['x'], y=start_point['y']).move_to(x=end_point['x'],
                                                                                                    y=end_point['y']).release().perform()
                                    time.sleep(2)
                                    Devices = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                            value='//android.widget.FrameLayout[@text="Devices"]')
                                    Devices.click()
                                    time.sleep(2)
                                    touch.long_press(x=start_point['x'], y=start_point['y']).move_to(x=end_point['x'],
                                                                                                    y=end_point['y']).release().perform()

                                    time.sleep(2)
                                    FotorSession = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                value='(//android.widget.TextView[@text="membersgram2"])')
                                    time.sleep(2)
                                    if FotorSession:
                                        backButton = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                    value='//android.widget.ImageView[@content-desc="Go back"]')
                                        backButton.click()
                                        time.sleep(2)
                                        CircleForOpenMenu = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                        value='//android.widget.ImageButton[@content-desc="More options"]/android.widget.ImageView')
                                        CircleForOpenMenu.click()
                                        time.sleep(2)
                                        LogOutInMenu = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                    value='//android.widget.TextView[@text="Log Out"]')
                                        time.sleep(2)
                                        LogOutInMenu.click()
                                        time.sleep(2)
                                        LogOutInMenu2 = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                    value='(//android.widget.TextView[@text="Log Out"])[2]')
                                        LogOutInMenu2.click()
                                        time.sleep(2)
                                        LogOutInDialogBOx = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                        value='(//android.widget.TextView[@text="Log Out"])[2]')
                                        LogOutInDialogBOx.click()
                                        time.sleep(20)
                                        print('selling be OK :)')
                                        Start_Message = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                    value='//android.widget.TextView[@text="Start Messaging"]')
                                        Start_Message.click()
                                        

                                except:
                                    print("log out faild")


                            except:
                                print(f'sell Account {PhoneNumber1} failed')


                    ############ اینجا مراحل  پاک کرد  و درخواست مجدد برای شماره اجرا شود

                    #

                    #

                    # end create account
                    # دکمه هوم گوشی

                    # driver.press_keycode(3)
                    else:
                        print("\033[31mPhone Number is not be OK!.\033[0m")
                except:
                    print("Error: verification code not find ")
            except:
                print("Error: Get_the_code_via_SMS not find ")
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
            except:
                print("\033[31mError: #### banned is not true ####\033[31m")
 