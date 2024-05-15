from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from typing import sys
sys.path.append("../TelegramAuto")
from function.GetNumberAndGetCodeApi import GetNumberApi
import time

def LogOut(driver_SamsungA71):
    touch = TouchAction(driver_SamsungA71)  
    try: #log out from account
        
        NavigationMenu = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.ImageView[@content-desc="Open navigation menu"]')
        NavigationMenu.click()
        time.sleep(2)
        touch.tap(x=260, y=1375).release().perform()
        time.sleep(2)
        start_point = {'x': 530, 'y': 1300}
        # انتها
        end_point = {'x': 520, 'y': 800}
        touch.long_press(x=start_point['x'], y=start_point['y']).move_to(x=end_point['x'],
                                                                        y=end_point['y']).release().perform()
        time.sleep(2)
        Devices = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                    value='//android.widget.FrameLayout[@text="Devices"]')
        Devices.click()
        time.sleep(3)
        
        FotorSession = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                        value='(//android.widget.TextView[@text="membersgram2"])')
        time.sleep(2)
        if FotorSession:
            time.sleep(2)
            backButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.ImageView[@content-desc="Go back"]')
            backButton.click()
            time.sleep(2)
            CircleForOpenMenu = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='//android.widget.ImageButton[@content-desc="More options"]/android.widget.ImageView')
            CircleForOpenMenu.click()
            time.sleep(2)
            LogOutInMenu = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.TextView[@text="Log Out"]')
            time.sleep(2)
            LogOutInMenu.click()
            time.sleep(2)
            LogOutInMenu2 = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='(//android.widget.TextView[@text="Log Out"])[2]')
            LogOutInMenu2.click()
            time.sleep(2)
            LogOutInDialogBOx = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='(//android.widget.TextView[@text="Log Out"])[2]')
            LogOutInDialogBOx.click()
            print('selling is ok')
            time.sleep(20)
            StartMessage = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                        value='//android.widget.TextView[@text="Start Messaging"]')
            StartMessage.click()

            
    except:
        print('Log out not found')