from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep
import sys, time, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

sys.path.append("../func")
from typing import Any, Dict


desired_caps: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}

# =================================================================================
## Different ways to make gestures in appium:
# 1. "touch_action/multi_action" libraries (deprecated)
# 2. W3C Actions (action_builder library)
# 3. "action_helper" library (some already created w3c actions)
# 4. Mobile gestures
#   - (https://github.com/appium/appium-uiautomator2-driver/tree/master?tab=readme-ov-file#mobile-gesture-commands)
#   - (https://github.com/appium/appium-uiautomator2-driver/blob/master/docs/android-mobile-gestures.md)
# 5. Android UiScrollable Class (https://developer.android.com/reference/androidx/test/uiautomator/UiScrollable)
# 6. Appium Gesture Plugin (https://github.com/AppiumTestDistribution/appium-gestures-plugin)
# =================================================================================
## Difference between gestures:
# Tap: Use fingers
# Click: Use mouse
# Press: Use input device / Hold fingers on screen
# Scroll: From element to another element
# Swipe: From a point to another point (With duration - Release hand after it is done)
# Flick: From a point to another point (No control and duration - Release hand before it is done)
# =================================================================================
appium_server = 'http://localhost:4721'
# >>> All `sleep`s are for demo purpose


# =================================================================================
# 6. Double Tap - Actions API - W3C
# appium_options = UiAutomator2Options().load_capabilities(desired_caps)
# driver = webdriver.Remote(appium_server, options=appium_options)
# driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Text').click()
# driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='LogTextBox').click()
# el_coords = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Add').location
# x, y = 454, 1072
# driver.tap([(x, y)])
# driver.tap([(x, y)])



# # =================================================================================
# # 7. Double Tap - Mobile Gesture Commands - W3C
# appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
# driver = webdriver.Remote(appium_server, options=appium_options)
# driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Text').click()
# driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='LogTextBox').click()
# el_coords = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Add').location
# driver.execute_script('mobile: doubleClickGesture', {'x': el_coords['x'], 'y': el_coords['y']})
# sleep(2)  # For demo purpose
# driver.quit()

# # =================================================================================
# # 8. Press and Hold - TouchAction
# appium_options = UiAutomator2Options().load_capabilities(desired_caps.contacts)
# driver = webdriver.Remote(appium_server, options=appium_options)
# contacts = driver.find_elements(by=AppiumBy.ID, value="com.android.contacts:id/cliv_name_textview")
# actions = TouchAction(driver)

# # actions.long_press(el=contacts[0]).perform()
# # or:
# actions.press(el=contacts[0]).wait(ms=1000).release().perform()
# sleep(2)  # For demo purpose
# driver.quit()

# # =================================================================================
# # 9. Press and Hold - Actions API - W3C
# appium_options = UiAutomator2Options().load_capabilities(desired_caps.contacts)
# driver = webdriver.Remote(appium_server, options=appium_options)
# contacts = driver.find_elements(by=AppiumBy.ID, value="com.android.contacts:id/cliv_name_textview")
# chains = ActionChains(driver)
# chains.w3c_actions.pointer_action.click_and_hold(contacts[0])
# chains.perform()
# sleep(2)  # For demo purpose
# driver.quit()


# =================================================================================
# 10. Press and Hold - Mobile Gesture Commands - W3C


appium_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.execute_script('mobile: longClickGesture', {'x': 145, 'y': 1072, 'duration': 1000})
sleep(2)  # For demo purpose
driver.quit()




# # # =================================================================================
# # # 10. Press and Hold - Mobile Gesture Commands - W3C
# appium_options = UiAutomator2Options().load_capabilities(desired_caps)
# driver = webdriver.Remote(appium_server, options=appium_options)
# # contacts = driver.find_elements(by=AppiumBy.ID, value="com.android.contacts:id/cliv_name_textview")
# # element_coord = contacts[0].location
# # appium_options = UiAutomator2Options().load_capabilities(desired_caps)
# # driver = webdriver.Remote(appium_server, options=appium_options)
# x, y = 454, 1072

# driver.execute_script('mobile: longClickGesture', {x, y})
# # sleep(2)  # For demo purpose
# # driver.quit()


