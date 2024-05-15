
from appium.webdriver.common.appiumby import AppiumBy

def TermOfService(driver_SamsungA71):
    try:

        TermOfService = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.TextView[@text="Terms of Service"]')
        if TermOfService:
            TermOfServiceAccept = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='//android.widget.TextView[@text="Accept"]')
            TermOfServiceAccept.click()
    except:
        print("Term of service not fount")