from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import sys, time, os
cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}
url = 'http://localhost:4721'


driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))


import sys, time
sys.path.append("../TelegramAuto")
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from function.AddaccountFullScreen import AddAccountFullScreen
from datetime import datetime


def Registerrr(driver, touch):
    
    driver.implicitly_wait(15)
    RegisterButton = driver.find_element(by=AppiumBy.XPATH,
                                                        value='//android.widget.Button[@text="Register"]')
    RegisterButton.click()
    
    driver.implicitly_wait(15)
    ################# Email is Empty 
    NextButton = driver.find_element(by=AppiumBy.XPATH,
                                    value='//android.widget.Button[@text="Next"]')
    NextButton.click()
    driver.implicitly_wait(15)
    ErrorEmailEmpty = driver.find_element(by=AppiumBy.XPATH,
                value='//*[contains(@text, "Email must not be empty")]')
    if ErrorEmailEmpty:
        print("Email Empty Error is : pass ✅")
    else:
        print("Email Empty Error is : Failed ❌")
        
    ################# Email format is Incorrect
    EmailInput = driver.find_element(by=AppiumBy.XPATH,
                                    value='//android.widget.EditText[@text="Email"]')
    EmailInput.send_keys("test")
    driver.implicitly_wait(15)
    NextButton = driver.find_element(by=AppiumBy.XPATH,
                                    value='//android.widget.Button[@text="Next"]')
    NextButton.click()
    driver.implicitly_wait(15)
    ErrorEmail = driver.find_element(by=AppiumBy.XPATH,
                    value='//*[contains(@text, "Email format is incorrect")]')

    if ErrorEmail:
        print("Email format Incorrect is : pass ✅ ")
    else:
        print("Email format Incorrect is : Failed ❌")
    ################# Email registerd Before
    
    EmailInput.send_keys("testphoenixmlk@gmail.com")
    driver.implicitly_wait(15)
    NextButton = driver.find_element(by=AppiumBy.XPATH,
                                    value='//android.widget.Button[@text="Next"]')
    NextButton.click()
    
    driver.implicitly_wait(15)

    EmailRegisteredBefore = driver.find_element(by=AppiumBy.XPATH,
                                    value='//android.widget.TextView[@text="You have registered before"]')
    if EmailRegisteredBefore:
        
        CancelEmail = driver.find_element(by=AppiumBy.XPATH,
                                    value='//android.widget.Button[@text="Cancel"]')
        CancelEmail.click()
        print("Email is already registered  pass ✅")
        driver.implicitly_wait(15)
    
    else :
        print("Email is already registered is : Failed ❌")
    ################# Email format true
    
    # دریافت زمان فعلی
    current_time = datetime.now().timestamp()
    
    EmailInput.send_keys(f"testpnxmlk{current_time}@gmail.com")
    driver.implicitly_wait(15)
    NextButton = driver.find_element(by=AppiumBy.XPATH,
                                    value='//android.widget.Button[@text="Next"]')
    NextButton.click()
    time.sleep(2)
    PasswordBox = driver.find_element(by=AppiumBy.XPATH,
                                    value='//android.widget.EditText[@text="Password"]')
    if PasswordBox : 
        print("Email format True is : pass ✅ ")
    else:
        print("Email format True is : Failed ❌")
     
    ################# Email true & Password Emtpy
    time.sleep(2)
    x, y = 200, 2125
    driver.tap([(x, y)])
    # touch.tap(x=200, y=2125).release().perform() #for click on  agree privacy
    PasswordBox = driver.find_element(by=AppiumBy.XPATH,
                                    value='//android.widget.EditText[@text="Password"]')
    Register_Button = driver.find_element(by=AppiumBy.XPATH,
                                    value='//android.widget.Button[@text="Register"]')
    Register_Button.click()
    driver.implicitly_wait(10)

    EmptyPassword = driver.find_element(by=AppiumBy.XPATH,
                    value='//*[contains(@text, "Password must not be empty")]')
    driver.implicitly_wait(15)
    if EmptyPassword:
        print("Password Empty is : pass ✅ ")
    else:
        print("Password Empty is : Failed ❌")
    
    driver.implicitly_wait(10)

    
    ################# Email true & Password Under 8
    
    PasswordBox.send_keys("1111111")
    Register_Button.click()
    driver.implicitly_wait(15)
    PasswordUnder8Characters = driver.find_element(by=AppiumBy.XPATH,
                value='//*[contains(@text, "Password must be at least 8 characters")]')
    if PasswordUnder8Characters:
        print("Password under 8 is : Pass ✅")
    else:
        print("Password under 8 is : Failed ❌")

    ################# Email true & Password ok And confirm Pass is Empty
    
    PasswordBox.send_keys("11111111")
    
    
    Register_Button.click()
    driver.implicitly_wait(15)
    if EmptyPassword:
        print("confirm Password Empty is : pass ✅ ")
    else:
        print("confirm Password Empty is : Failed ❌")
        
    
    ################# Email true & Password ok And confirm Pass under 8 
    ConfirmPassword = driver.find_element(by=AppiumBy.XPATH,
                                    value='//android.widget.EditText[@text="Confirm password"]')
    ConfirmPassword.send_keys("111111")
    Register_Button.click()
    driver.implicitly_wait(15)
    PasswordUnder8Character = driver.find_element(by=AppiumBy.XPATH,
                                value='//*[contains(@text, "Password must be at least 8 characters")]')
    if PasswordUnder8Character:
     print("confirm Password under 8 is : Pass ✅")
    else:
        print("confirm Password under 8 is : Failed ❌")
        
    ################# Email true & Password ok And confirm do not match
    
    # ConfirmPassword = driver.find_element(by=AppiumBy.XPATH,
    #                                 value='//android.widget.EditText[@text="Confirm password"]')
    ConfirmPassword.send_keys("11111112")
    Register_Button.click()
    driver.implicitly_wait(15)
    PasswordDoNotMatch = driver.find_element(by=AppiumBy.XPATH,
                                value='//*[contains(@text, "Passwords do not match")]')
    
    if PasswordDoNotMatch:
     print("Password Do Not Match is : Pass ✅")
    else:
        print("Password Do Not Match is : Failed ❌")
    ################# Email true & Password And confirm ok 
    
    ConfirmPassword.send_keys("11111111")
    Register_Button.click()
    driver.implicitly_wait(15)
    
    try:
        PhoneNumber = driver.find_element(by=AppiumBy.XPATH,
                value='//android.widget.TextView[@text="Phone number"]')
        if PhoneNumber:
            CountryCode = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.EditText[@text="98"]')
            CountryCode.click()
            driver.implicitly_wait(15)
            SearchCountry = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.EditText[@resource-id="gram.members.android:id/etSearchCountry"]')
            SearchCountry.send_keys("canada")
            CanadaCountry = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.TextView[@text="Canada (+1)"]')
            CanadaCountry.click()
            driver.implicitly_wait(15)
            PhoneNumberInput = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.EditText[@resource-id="gram.members.android:id/editTextPhoneRegister"]')
            PhoneNumberInput.send_keys("6603455472")
            NextButton = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Next"]')
            NextButton.click()
        
    except:
        print("")
    # driver.implicitly_wait(10)
    # HomePage = driver.find_element(by=AppiumBy.XPATH,
    #                 value='//android.widget.LinearLayout[@content-desc="Member"]')
    # if HomePage:
    #     print("Register is : Pass ✅")
    # else:
    #     print("Register is : Failed ❌")
    
    
    
    