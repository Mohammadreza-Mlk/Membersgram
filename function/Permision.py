import time
from appium.webdriver.common.appiumby import AppiumBy
from watchlog import Watchlog
watchlog_instance = Watchlog()
import sys, time, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
sys.path.append("../Membersgram")
from function.result import log_test_result

def Permision(driver):
     
    
    try:
        driver.implicitly_wait(5)

        AllowButton = driver.find_element(by=AppiumBy.XPATH,
                                                            value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]')
        AllowButton.click()
        
        time.sleep(2)
        log_test_result("permission", "pass")
 
    except:
            print("")