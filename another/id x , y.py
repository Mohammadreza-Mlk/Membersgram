from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time

url = 'http://localhost:4720'

# Device 1 (Samsung)
capabilities_samsung_j5: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'platformVersion': '9.0',
    'deviceName': 'Samsung',
    'language': 'en',
    'locale': 'us'
}

driver_samsung_j5 = webdriver.Remote(url, options=AppiumOptions().load_capabilities(capabilities_samsung_j5))
touch = TouchAction(driver_samsung_j5)
print('sgdfsgdsg')
driver_samsung_j5.press_keycode(4)

print(f'name tis account is : ')
    
VerifycodeInputBox = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                    value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]')
