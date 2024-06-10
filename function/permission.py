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



touch.long_press(x=405, y=295).release().perform()
time.sleep(2)

AppInfo = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.ImageView[@content-desc="App info"]')
time.sleep(2)
AppInfo.click()

time.sleep(2)
Permision = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.TextView[@resource-id="android:id/title" and @text="Permissions"]')
time.sleep(2)
Permision.click()
time.sleep(2)
contact = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//androidx.recyclerview.widget.RecyclerView[@resource-id="com.android.permissioncontroller:id/recycler_view"]/android.widget.LinearLayout[6]/android.widget.RelativeLayout')
time.sleep(2)
contact.click()

time.sleep(2)
AlowPermission = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.RadioButton[@resource-id="com.android.permissioncontroller:id/allow_radio_button"]')
AlowPermission.click()
time.sleep(1)
driver_SamsungA71.press_keycode(4)
time.sleep(2)

start_x = 800
start_y = 800  
end_x = 801  
end_y = 200  
touch.press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()


time.sleep(2)
notif = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.TextView[@resource-id="android:id/title" and @text="Notifications"]')
time.sleep(1)
notif.click()
time.sleep(2)
notifAllow = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.TextView[@resource-id="com.android.settings:id/switch_text"]')
time.sleep(1)
notifAllow.click()
driver_SamsungA71.press_keycode(4)
time.sleep(2)
PhotosAndVideo = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.TextView[@resource-id="android:id/title" and @text="Photos and videos"]')
time.sleep(1)
PhotosAndVideo.click()

time.sleep(1)
AlowPermissionPhotosAndVideo = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.RadioButton[@resource-id="com.android.permissioncontroller:id/allow_radio_button"]')
AlowPermissionPhotosAndVideo.click()
for i in range (3) : 
    driver_SamsungA71.press_keycode(4)
  
