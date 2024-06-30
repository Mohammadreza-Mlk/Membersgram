from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import sys, time
sys.path.append("../TelegramAuto")
# from function.checkForCallingCode import check_For_Calling_Code
from function.installTelegram import InstallTelegram
from function.CallingNew import Calling
from function.check_for_send_verify_code_to_another_telegram_sesseion import check_for_send_verify_code_to_another_telegram_sesseion
from function.Email_check import Email_check
from function.GetNumberAndGetCodeApi import GetNumberApi
from function.PhoneNumberIsBan import PhonenNumberBan, InvalidPhonenNumber
from function.CheckVerfiCodeSms import Check_Verify_code
from function.NameAccount import RandomName
from function.TooManyAttempts import TooManyAttempts
from function.PlusMessenger import PlusMessanger
from function.FotorPlus import FotorPlus
from function.LogOut import LogOut
cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}
url = 'http://localhost:4721'


driver_SamsungA71 = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
touch = TouchAction(driver_SamsungA71)
phoneNumber = ""
activationId = ""

# TelegramApp =  driver_SamsungA71.find_element(by=AppiumBy.XPATH,
#                                             value='//android.widget.TextView[@content-desc="Telegram Beta"]')

time.sleep(5)
TelegramApp = InstallTelegram(driver_SamsungA71) 

print("start create Account")
for i in range(20):
             
    # for i in range(1):
    try:
        time.sleep(5)
        StartMessage = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                    value='//android.widget.TextView[@text="Start Messaging"]')
        StartMessage.click()
        print(" start button clicked")

    except:
        print("no start button")
        
    try:
        time.sleep(2)
        PhoneNumberInput = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                        value='//android.widget.EditText[@content-desc="Country code"]')
        if PhoneNumberInput:
            print("PhoneNumberInput found! Start phone number giving :)")
            
            phoneNumber,activationId = GetNumberApi()
            # print("phoneNumber A71 = " f'{phoneNumber}')
            # print("activationId A71 = " f'{activationId}')
            time.sleep(2)
            PhoneNumberInput.send_keys(phoneNumber)
            time.sleep(2)
            nextButton =   driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                        value='//android.widget.FrameLayout[@content-desc="Done"]/android.view.View')
            nextButton.click()  # click On next
            time.sleep(1)
            ConfirmNumberButton =   driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                                value='//android.widget.TextView[@text="Yes"]')
            ConfirmNumberButton.click()
            time.sleep(2)
        
    except:
        print("PhoneNumberInput not found")
    time.sleep(2)
    TooManyAttempts(driver_SamsungA71)
    time.sleep(4)
    InvalidPhonenNumber(driver_SamsungA71)
    time.sleep(4)
    resultBan = PhonenNumberBan(driver_SamsungA71)
    if not resultBan :
        time.sleep(3)
        Email_check(driver_SamsungA71, TelegramApp)

        time.sleep(3)
        anotherTelegram = check_for_send_verify_code_to_another_telegram_sesseion(driver_SamsungA71)
        if not anotherTelegram:
            # for i in range (2):
                time.sleep(4)
                print(activationId)
                resultCalling = Calling(driver_SamsungA71, activationId, phoneNumber)
                if not resultCalling:
                    
                    time.sleep(5)
                    resultCode = Check_Verify_code(driver_SamsungA71, phoneNumber , activationId)
                    if resultCode : 
                        RandomName(driver_SamsungA71)
                        time.sleep(6)
                        PlusMessanger(driver_SamsungA71, phoneNumber, TelegramApp)
                        # FotorPlus(driver_SamsungA71, phoneNumber)
                        # time.sleep(6)
                        # LogOut(driver_SamsungA71)
        else:
            print("another telegram session in phone number")
    # time.sleep(2)40610
