from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import sys, time
sys.path.append("../TelegramAuto")
from function.checkForCallingCode import check_For_Calling_Code
from function.check_for_send_verify_code_to_another_telegram_sesseion import check_for_send_verify_code_to_another_telegram_sesseion
from function.Email_check import Email_check
from function.GetNumberAndGetCodeApi import GetNumberApi
# from function.AccountNAmes import random_name
from function.PhoneNumberIsBan import PhonenNumberBan
from function.CheckVerfiCodeSms import Check_Verify_code
from function.NameAccount import RandomName
from function.TooManyAttempts import TooManyAttempts
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

print("start create Account")
for i in range(20):
    phoneNumber = ""
    activationId = ""
    try:
        time.sleep(5)
        StartMessage = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                    value='//android.widget.TextView[@text="Start Messaging"]')
        StartMessage.click()
        print(" start button clicked")

    except:
        print("no start button")
        
    try:
        time.sleep(5)
        PhoneNumberInput = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                        value='//android.widget.EditText[@content-desc="Country code"]')
        if PhoneNumberInput:
            print("PhoneNumberInput found! Start phone number giving :)")
            
            phoneNumber,activationId = GetNumberApi()
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

    TooManyAttempts(driver_SamsungA71)
    time.sleep(6)
    resultBan = PhonenNumberBan(driver_SamsungA71)
    if not resultBan :
        time.sleep(3)
        Email_check(driver_SamsungA71)

        time.sleep(3)
        check_for_send_verify_code_to_another_telegram_sesseion(driver_SamsungA71)


        time.sleep(6)
        check_For_Calling_Code(driver_SamsungA71)

        time.sleep(6)
        resultCode = Check_Verify_code(driver_SamsungA71, phoneNumber , activationId)
        if resultCode : 
            RandomName(driver_SamsungA71)
            time.sleep(6)
            FotorPlus(driver_SamsungA71, phoneNumber)
            time.sleep(6)
            LogOut(driver_SamsungA71)

    # time.sleep(2)
