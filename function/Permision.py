import time
from appium.webdriver.common.appiumby import AppiumBy
from watchlog import Watchlog
watchlog_instance = Watchlog()


def Permision(driver):
    try:
        driver.implicitly_wait(5)

        AllowButton = driver.find_element(by=AppiumBy.XPATH,
                                                            value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]')
        AllowButton.click()
        
        time.sleep(2)
 
    except:
            print("")