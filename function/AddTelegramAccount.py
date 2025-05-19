
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from appium import webdriver
from typing import Any, Dict
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from typing import sys
sys.path.append("../TelegramAuto")
from time import sleep
from datetime import datetime 
import sys, time, os, base64, re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append("../func")
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.pointer_input import PointerInput
from watchlog import Watchlog
watchlog_instance = Watchlog()


def swipe_left(driver):
    start_x = 650
    end_x = 300
    start_y = 400
    end_y = 400

    driver.press(x=start_x, y=start_y).wait(1000).move_to(x=end_x, y=end_y).release().perform()


def AddAccount(driver, desired_caps, url):
    print("\033[32m***********  Login an account  *********** .\033[0m")

    driver.implicitly_wait(30) 
    CoinTab = driver.find_element(by=AppiumBy.XPATH,
                    value='(//android.widget.ImageView[@resource-id="gram.members.android:id/navigation_bar_item_icon_view"])[2]')
    CoinTab.click()
    driver.implicitly_wait(30)
    FreeTab =driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.LinearLayout[@content-desc="Join"]')  
    FreeTab.click()
    driver.implicitly_wait(30)


    AddTelegramAccountbuttomsheet = driver.find_element(by=AppiumBy.XPATH,
                    value='//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView[1]')
    AddTelegramAccountbuttomsheet.click()
    driver.implicitly_wait(30)  
    AddTelegramAccount = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Add Telegram account"]')
    AddTelegramAccount.click()
    driver.implicitly_wait(30)
    PhoneNumber = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextTelegramLoginPhone"]')
    PhoneNumber.send_keys("7066819795")
    for addaccount in range(3):
        # driver.start_recording_screen()
        driver.implicitly_wait(20) 
        
        NextButton = driver.find_element(by=AppiumBy.XPATH,
                        value='//android.widget.Button')
        NextButton.click()
        try:
            codeInput = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@resource-id="gram.members.android:id/login2CustomTv1"]'))
            )
            print("codeInput پیدا شد!")
        except:
            codeInput = None
            print("codeInput پیدا نشد!")
            
        if codeInput:
            # عملیات در صورت پیدا شدن codeInput
            print("ادامه فرآیند...")
            # استاپ کردن ضبط صفحه (اگر قبلاً شروع شده باشد)
            video_folder = "video/bugsmedia"
            if not os.path.exists(video_folder):
                os.makedirs(video_folder)
            current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            video_path = os.path.join(video_folder, f"recorded_video_{current_time}.mp4")

            # print("توقف ضبط صفحه...")
            # raw_video = driver.stop_recording_screen()
            # with open(video_path, "wb") as video_file:
            #     video_file.write(base64.b64decode(raw_video))
            # print(f"ویدئو ضبط‌شده در مسیر ذخیره شد: {video_path}")

            # ادامه کار
            driver.press_keycode(3)
            AkaApp = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@content-desc="aka"]'))
            )
            AkaApp.click()
            sleep(5)
            # سایر عملیات مرتبط...
            
            driver.press_keycode(3)

            driver.implicitly_wait(30) 
            AkaApp = driver.find_element(by=AppiumBy.XPATH,
                            value='//android.widget.TextView[@content-desc="aka"]')
            AkaApp.click()
            sleep(5)
            searchIcon = driver.find_element(by=AppiumBy.XPATH,
                            value='//android.widget.ImageButton[@content-desc="Search"]/android.widget.ImageView')
            searchIcon.click()
            searchInput = driver.find_element(by=AppiumBy.XPATH,
                            value='//android.widget.EditText[@text="Search"]')
            searchInput.send_keys("Telegram")
            sleep(5) 
            x, y = 300, 500
            driver.tap([(x, y)])
            sleep(5)
            # touch.tap(x=300, y=500).release().perform()
            x, y = 500, 1850
            driver.tap([(x, y)])

            # touch.long_press(x=500, y=1850).release().perform()
            time.sleep(1.5)
            x, y = 390, 1493
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

            
            sleep(1)
            
            clipboard_text = driver.get_clipboard_text()
            print(f"Clipboard text: {clipboard_text}")
            
            clipboard_text = driver.get_clipboard_text()
            def extract_code(message):
                # استفاده از regex برای پیدا کردن کد عددی 5 رقمی
                match = re.search(r'\b\d{5}\b', message)
                if match:
                    return match.group()
                return None

            # استخراج کدها

            code = extract_code(clipboard_text)
            driver.set_clipboard_text(code)

            print("کد :", code)

            # appium_options = UiAutomator2Options().load_capabilities(desired_caps)
            # driver = webdriver.Remote(url, options=appium_options)
            # driver.execute_script('mobile: longClickGesture', {'x': 460, 'y': 1072, 'duration': 1000})
        
