from typing import Any, Dict
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import sys, time
sys.path.append("../TelegramAuto")

def UnistalTelegram(driver_SamsungA71):
        touch = TouchAction(driver_SamsungA71)
        driver_SamsungA71.press_keycode(3)
        try:
                time.sleep(2)
                
                try:
                    time.sleep(2)
                    print("start to unistall")
                    # telegramBetaApp = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                    #                                         value='//android.widget.TextView[@content-desc="Telegram Beta"]')
                    time.sleep(2)
                    touch.long_press(x=921, y=1024).release().perform()
                    
                    time.sleep(2)
                    unistallTelegram = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                            value='//android.widget.FrameLayout[@content-desc="Uninstall, Button"]/android.widget.LinearLayout')
                    time.sleep(2)
                    unistallTelegram.click()
                    time.sleep(2)
                    confirmUnistall = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                            value='//android.widget.Button[@resource-id="android:id/button1"]')
                    time.sleep(2)
                    confirmUnistall.click()
                    if confirmUnistall:
                        print("unistall seccess")

                except:
                    print("telegram Beta app not found1")
        except:
                print("telegram Beta app not found 2")