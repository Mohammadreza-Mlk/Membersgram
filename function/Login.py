
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from watchlog import Watchlog
watchlog_instance = Watchlog()

def LoginEmail(driver):
    driver.implicitly_wait(30)

    LoginButton = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Login"]')
    LoginButton.click()
    driver.implicitly_wait(30)

    ############ email & pass is empty  
    LoginButton = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Login"]')
    LoginButton.click()
    driver.implicitly_wait(30)
    ErrorEmailEmpty = driver.find_element(by=AppiumBy.XPATH,
                    value='//*[contains(@text, "Email must not be empty")]')
    if ErrorEmailEmpty:
        print("Email Empty Error is : pass ✅")
        watchlog_instance.increment('EmailEmptyErrorPass')
    else:
        print("Email Empty Error is : Failed ❌")
        watchlog_instance.increment('EmailEmptyErrorFaild')

    ############ email format incorrect
    EmailBox = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextEmailLogin"]')
    EmailBox.send_keys("test")
    LoginButton = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Login"]')
    LoginButton.click()
    driver.implicitly_wait(30)
    ErrorEmail = driver.find_element(by=AppiumBy.XPATH,
                    value='//*[contains(@text, "Email format is incorrect")]')

    if ErrorEmail:
        print("Email format Incorrect is : pass ✅ ")
        watchlog_instance.increment('EmailFormatIncorrectPass')
    else:
        print("Email format Incorrect is : Failed ❌")
        watchlog_instance.increment('EmailFormatIncorrectFaild')
    ############ email  True and password Empty
    driver.implicitly_wait(8)
    EmailBox = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextEmailLogin"]')
    EmailBox.send_keys("testphoenixmlk@gmail.com")   
    Password = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.EditText[@text="Password"]')
    Password.send_keys("")
    LoginButton.click()
    driver.implicitly_wait(8)
    PasswordEmpty = driver.find_element(by=AppiumBy.XPATH,
                    value='//*[contains(@text, "Password must not be empty")]')
    if PasswordEmpty:
        print("Password must not be empty Error is : Pass ✅")
        watchlog_instance.increment('PasswordMustNotBeEmptyErrorPass')
    else:
        print("Password must not be empty Error is : Failed ❌")
        watchlog_instance.increment('PasswordMustNotBeEmptyErrorFaild')
    ############ Email not registeresd before
    EmailBox = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextEmailLogin"]')
    EmailBox.send_keys("emailnotregistered@gmail.com")
    Password = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.EditText[@text="Password"]')
    Password.send_keys("111111111")
    LoginButton.click()

    driver.implicitly_wait(30)
    EmailNotRegistered = driver.find_element(by=AppiumBy.XPATH,
                    value='//*[contains(@text, "This email has not been registered before")]')

    if EmailNotRegistered:
        print("This email has not been registered before is : pass ✅ ")
        watchlog_instance.increment('TheEmailNotRegisteredPass')
    else:
        print("This email has not been registered before is : Failed ❌")
        watchlog_instance.increment('TheEmailNotRegisteredFailed')



    ############ email  True and password under8character
    EmailBox = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextEmailLogin"]')
    EmailBox.send_keys("testphoenixmlk@gmail.com")   

    Password.send_keys("1111111")
    LoginButton.click()
    driver.implicitly_wait(8)
    PasswordUnder8Characters = driver.find_element(by=AppiumBy.XPATH,
                    value='//*[contains(@text, "Password must be at least 8 characters")]')
    if PasswordUnder8Characters:
        print("Password under 8 is : Pass ✅")
        watchlog_instance.increment('PasswordUnder8Pass')
    else:
        print("Password under 8 is : Failed ❌")
        watchlog_instance.increment('PasswordUnder8Failed')

    ############ email format True and password incorrect
    EmailBox = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextEmailLogin"]')
    EmailBox.send_keys("testphoenixmlk@gmail.com")   

    Password.send_keys("111111112")
    LoginButton.click()
    driver.implicitly_wait(30)
    PasswordIncorrect = driver.find_element(by=AppiumBy.XPATH,
                    value='//*[contains(@text, "Password is incorrect")]')
    if PasswordIncorrect:
        print("Password is incorrect is : Pass ✅")
        watchlog_instance.increment('PasswordIncorrectPass')
    else:
        print("Password is incorrect is : Failed ❌")
        watchlog_instance.increment('PasswordIncorrectFailed')
        

    ############ email format and password True  
    EmailBox = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextEmailLogin"]')
    EmailBox.send_keys("testphoenixmlk@gmail.com")   

    Password.send_keys("11111111")
    LoginButton.click()
    driver.implicitly_wait(10)
    # watchlog_instance.increment('LoginEmail')
    # HomePage = driver.find_element(by=AppiumBy.XPATH,
    #                 value='//android.widget.LinearLayout[@content-desc="Member"]')
    # if HomePage:
    #     print("Login is : Pass ✅")
    # else:
    #     print("Login is : Failed ❌")
        