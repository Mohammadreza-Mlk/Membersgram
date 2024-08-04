
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
# cap: Dict[str, Any] = {
#     'platformName': 'Android',
#     'automationName': 'uiautomator2',
#     'deviceName': 'SamsungA71',
#     "platformVersion": "13.0",
#     'language': 'en',
#     'locale': 'us'
# }
# url = 'http://localhost:4721'


# driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
# touch = TouchAction(driver)

def LoginEmail(driver):
    driver.implicitly_wait(5)

    LoginButton = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Login"]')
    LoginButton.click()
    driver.implicitly_wait(5)

    ############ email & pass is empty  
    LoginButton = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Login"]')
    LoginButton.click()
    driver.implicitly_wait(5)
    ErrorEmailEmpty = driver.find_element(by=AppiumBy.XPATH,
                    value='//*[contains(@text, "Email must not be empty")]')
    if ErrorEmailEmpty:
        print("Email Empty Error is : pass ✅")
    else:
        print("Email Empty Error is : Failed ❌")

    ############ email format incorrect
    EmailBox = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextEmailLogin"]')
    EmailBox.send_keys("test")
    LoginButton = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Login"]')
    LoginButton.click()
    driver.implicitly_wait(5)
    ErrorEmail = driver.find_element(by=AppiumBy.XPATH,
                    value='//*[contains(@text, "Email format is incorrect")]')

    if ErrorEmail:
        print("Email format Incorrect is : pass ✅ ")
    else:
        print("Email format Incorrect is : Failed ❌")
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
    else:
        print("Password must not be empty Error is : Failed ❌")
    ############ Email not registeresd before
    EmailBox = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextEmailLogin"]')
    EmailBox.send_keys("emailnotregistered@gmail.com")
    Password = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.EditText[@text="Password"]')
    Password.send_keys("111111111")
    LoginButton.click()

    driver.implicitly_wait(5)
    EmailNotRegistered = driver.find_element(by=AppiumBy.XPATH,
                    value='//*[contains(@text, "This email has not been registered before")]')

    if EmailNotRegistered:
        print("This email has not been registered before is : pass ✅ ")
    else:
        print("This email has not been registered before is : Failed ❌")



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
    else:
        print("Password under 8 is : Failed ❌")

    ############ email format True and password incorrect
    EmailBox = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextEmailLogin"]')
    EmailBox.send_keys("testphoenixmlk@gmail.com")   

    Password.send_keys("111111112")
    LoginButton.click()
    driver.implicitly_wait(5)
    PasswordIncorrect = driver.find_element(by=AppiumBy.XPATH,
                    value='//*[contains(@text, "Password is incorrect")]')
    if PasswordIncorrect:
        print("Password is incorrect is : Pass ✅")
    else:
        print("Password is incorrect is : Failed ❌")

    ############ email format and password True  
    EmailBox = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextEmailLogin"]')
    EmailBox.send_keys("testphoenixmlk@gmail.com")   

    Password.send_keys("11111111")
    LoginButton.click()
    driver.implicitly_wait(10)

    # HomePage = driver.find_element(by=AppiumBy.XPATH,
    #                 value='//android.widget.LinearLayout[@content-desc="Member"]')
    # if HomePage:
    #     print("Login is : Pass ✅")
    # else:
    #     print("Login is : Failed ❌")
        