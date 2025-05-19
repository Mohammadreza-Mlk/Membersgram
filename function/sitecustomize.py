from appium import webdriver
from typing import Any, Dict
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from typing import sys
sys.path.append("../TelegramAuto")
from time import sleep
import time
import sys, time, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

sys.path.append("../func")
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.pointer_input import PointerInput
from watchlog import Watchlog
watchlog_instance = Watchlog()

import os
 
def shot(driver):
    from appium import webdriver
    import base64
    from datetime import datetime  # اضافه کردن datetime برای زمان

    video_folder = "video/bugsmedia"  # مسیر دلخواه شما
    if not os.path.exists(video_folder):
        os.makedirs(video_folder)  # اگر پوشه وجود ندارد، ایجاد کن

    # تولید نام فایل با زمان فعلی
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # فرمت زمان
    video_path = os.path.join(video_folder, f"recorded_video_{current_time}.mp4")

    # شروع ضبط ویدئو
    print("شروع ضبط صفحه...")
    driver.start_recording_screen()

    # اجرای برخی عملیات
    time.sleep(15)

    # توقف ضبط ویدئو
    print("توقف ضبط صفحه...")
    raw_video = driver.stop_recording_screen()

    # ذخیره ویدئو در فایل مشخص‌شده
    with open(video_path, "wb") as video_file:
        video_file.write(base64.b64decode(raw_video))

    print(f"ویدئو ضبط‌شده در مسیر ذخیره شد: {video_path}")

    