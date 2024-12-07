import sys, time
sys.path.append("../TelegramAuto")

from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from watchlog import Watchlog
watchlog_instance = Watchlog()

def AddAccountFullScreen(driver):
    try:
               
        driver.implicitly_wait(15)
        AddTelegramAccount = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.TextView[@text="Add Telegram account"]')
        if AddTelegramAccount :
            driver.implicitly_wait(15)
            AddAccountOne =  driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button[@text="Login to Telegram"]')
            AddAccountOne.click()



            PhoneNumber = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextTelegramLoginPhone"]')
            PhoneNumber.send_keys("6603455472")
            driver.implicitly_wait(30) 
            NextButton = driver.find_element(by=AppiumBy.XPATH,
                            value='//android.widget.Button')
            NextButton.click()
            for i in range(4):
                try:
                    driver.implicitly_wait(30) 
                    codeInput = driver.find_element(by=AppiumBy.XPATH,
                                    value='//android.widget.TextView[@resource-id="gram.members.android:id/login2CustomTv1"]')
                    if codeInput : 
                            driver.press_keycode(3)
                            
                            driver.implicitly_wait(30) 
                            Vidogram = driver.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.TextView[@content-desc="Vidogram"]')
                            Vidogram.click()
                            time.sleep(5)
                            searchIcon = driver.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.ImageButton[@content-desc="Search"]/android.widget.ImageView')
                            searchIcon.click()
                            searchInput = driver.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.EditText[@text="Search"]')
                            searchInput.send_keys("Telegram")
                            time.sleep(5) 
                            x, y = 300, 500
                            driver.tap([(x, y)])
                            time.sleep(2)
                            print('log test')
                            # touch.tap(x=300, y=500).release().perform()
                            x, y = 500, 1850
                            driver.tap([(x, y)])
                            print('log test2')
                            # touch.long_press(x=500, y=1850).release().perform()
                            time.sleep(1.5)
                            x, y = 390, 1130
                            driver.tap([(x, y)])
                            # copyIcon = touch.tap(x=580, y=170).release().perform()
                            driver.implicitly_wait(30) 
                            MessageBox = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Message"]')
                            MessageBox.click()
                        
                            
                            x, y = 244, 1355
                            driver.tap([(x, y)])
                            # driver.long_press(MessageBox)
                            # touch.long_press(MessageBox).release().perform()
                            x, y = 150, 1240
                            driver.tap([(x, y)])
                            # touch.tap(x=150, y=1240).release().perform()
                            time.sleep(1)
                            # پاک کردن اضافه پیام برای نمایان شدن متن کد
                            for m in range(70):
                               
                                driver.long_press_keycode(67)
                            time.sleep(1)   
                            x, y = 460, 1070
                            driver.tap([(x, y)])
                            time.sleep(1)

                            driver.execute_script('mobile: longClickGesture', {'x': 460, 'y': 1072, 'duration': 1000})
                
                            # touch.long_press(x=440, y=1148).release().perform()
                            time.sleep(1)
                            x, y = 320, 975
                            driver.tap([(x, y)])
                            # touch.tap(x=370, y=1035).release().perform()
                            x, y = 920, 1378
                            driver.tap([(x, y)])
                            time.sleep(1)
                            # پاک کردن اضافه پیام برای نمایان شدن متن کد
                            for m in range(100):
                                # location of mark massage to delete
                                driver.long_press_keycode(67)   
                            
                                # touch.long_press(x=990, y=2042).release().perform()
                            driver.press_keycode(4)
                            driver.press_keycode(4)
                            driver.press_keycode(3)
                            driver.implicitly_wait(5)
                            MembersgramApp = driver.find_element(by=AppiumBy.XPATH,
                                            value='(//android.widget.TextView[@content-desc="Membersgram"])[1]')
                            MembersgramApp.click()
                            time.sleep(2)
                            x, y = 484, 1468
                            driver.tap([(x, y)])
                            # touch.tap(x=484, y=1468).release().perform()
                            driver.implicitly_wait(3)
                            NextButton = driver.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.Button')
                            NextButton.click()
                            driver.implicitly_wait(15)
                            StartBot = driver.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.Button[@text="Start"]')
                            StartBot.click()
                            watchlog_instance.increment('AddAccountFullScreen')
                            break
                    else:
                        time.sleep(30)
                        NextButton = driver.find_element(by=AppiumBy.XPATH,
                                value='//android.widget.Button')
                        NextButton.click()
                        driver.implicitly_wait(30) 
                except:
                    print()
    except:
        print("AddAcoount not  found")