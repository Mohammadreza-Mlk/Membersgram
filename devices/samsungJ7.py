from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import sys, time
sys.path.append("../TelegramAuto")
from function.checkForCallingCode import check_For_Calling_Code
from function.check_for_send_verify_code_to_another_telegram_sesseion import check_for_send_verify_code_to_another_telegram_sesseion
from function.Email_check import Email_check_j7
from function.GetNumberAndGetCodeApi import GetNumberApi
from function.PhoneNumberIsBan import PhonenNumberBan
from function.CheckVerfiCodeSms import Check_Verify_code
from function.NameAccount import RandomName
from function.TooManyAttempts import TooManyAttempts
from function.FotorPlus import FotorPlus
from function.LogOut import LogOut
caap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'platformVersion': '9.0',
    'deviceName': 'Samsung',
    'language': 'en',
    'locale': 'us'
}
url = 'http://localhost:4721'


driver_SamsungJ7 = webdriver.Remote(url, options=AppiumOptions().load_capabilities(caap))
touch = TouchAction(driver_SamsungJ7)

print("start create Account")
for i in range(20):
    phoneNumber = ""
    activationId = ""
    try:
        time.sleep(5)
        StartMessage = driver_SamsungJ7.find_element(by=AppiumBy.XPATH,
                                    value='//android.widget.TextView[@text="Start Messaging"]')
        StartMessage.click()
        print(" start button clicked")

    except:
        print("no start button")
        
    try:
        time.sleep(5)
        PhoneNumberInput = driver_SamsungJ7.find_element(by=AppiumBy.XPATH,
                                                        value='//android.widget.EditText[@content-desc="Country code"]')
        if PhoneNumberInput:
            print("PhoneNumberInput found! Start phone number giving :)")
            
            phoneNumber,activationId = GetNumberApi()
            time.sleep(2)
            PhoneNumberInput.send_keys(phoneNumber)
            time.sleep(2)
            nextButton =   driver_SamsungJ7.find_element(by=AppiumBy.XPATH,
                                                        value='//android.widget.FrameLayout[@content-desc="Done"]/android.view.View')
            nextButton.click()  # click On next
            time.sleep(1)
            ConfirmNumberButton =   driver_SamsungJ7.find_element(by=AppiumBy.XPATH,
                                                                value='//android.widget.TextView[@text="Yes"]')
            ConfirmNumberButton.click()
            time.sleep(2)
    except:
        print("PhoneNumberInput not found")

    TooManyAttempts(driver_SamsungJ7)
    time.sleep(6)
    resultBan = PhonenNumberBan(driver_SamsungJ7)
    if not resultBan :
        time.sleep(3)
        Email_check_j7(driver_SamsungJ7)

        time.sleep(3)
        anotherTelegram = check_for_send_verify_code_to_another_telegram_sesseion(driver_SamsungJ7)
        if not anotherTelegram:

            time.sleep(3)
            check_For_Calling_Code(driver_SamsungJ7)

            time.sleep(3)
            resultCode = Check_Verify_code(driver_SamsungJ7, phoneNumber , activationId)
            if resultCode : 
                RandomName(driver_SamsungJ7)
                time.sleep(6)
                FotorPlus(driver_SamsungJ7, phoneNumber)
                time.sleep(6)
                LogOut(driver_SamsungJ7)

    # time.sleep(2)40610
