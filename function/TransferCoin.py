from appium.webdriver.common.appiumby import AppiumBy
import sys, time, subprocess
sys.path.append("../TelegramAuto")
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import sys, time
from watchlog import Watchlog
watchlog_instance = Watchlog()

def TransferCoin(driver):
    
    javascript_file = 'api.js'

    # اجرای فایل جاوا اسکریپت
    result = subprocess.run(['node', javascript_file], capture_output=True, text=True)

    # نمایش خروجی
    MyCoinsBeforeTransfer = result.stdout
    print("MyCoinsBeforeTransfer :", MyCoinsBeforeTransfer )
    driver.implicitly_wait(10)
    CoinTab = driver.find_element(by=AppiumBy.XPATH,
                    value='(//android.widget.ImageView[@resource-id="gram.members.android:id/navigation_bar_item_icon_view"])[2]')
    CoinTab.click()
    driver.implicitly_wait(10)

    TransferTab = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.TextView[@text="Transfer"]')

    TransferTab.click()
    driver.implicitly_wait(10)

    ########  Email format incorrect
    EmailInput = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextNumberTransferCoin"]')
    EmailInput.send_keys("1111")
    CoinInput = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextCoinTransferCoin"]')
    CoinInput.send_keys("5")
    TransferButton = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Transfer"]')
    TransferButton.click()

    EmailFormatError = driver.find_element(by=AppiumBy.XPATH,
                    value='//*[contains(@text, "Email format is incorrect")]')

    if EmailFormatError:
        print("Email format Incorrect is : pass ✅ ")
    else:
        print("Email format Incorrect is : Failed ❌")

    ########  Email not register before 

    EmailInput.send_keys("fakemail@gmail.com")
    TransferButton.click()
    time.sleep(5)
    EmailNotFound = driver.find_element(by=AppiumBy.XPATH,
                    value='//*[contains(@text, "An account with this email was not found")]')
    if EmailNotFound:
        print("Email not found is : pass ✅ ")
    else:
        print("Email not found is : Failed ❌")


    ###coins under 10
    EmailInput.send_keys("pnxdevices@gmail.com")
    CoinInput.send_keys("5")
    TransferButton.click()

    time.sleep(5)
    CoinsRangeForTransfer = driver.find_element(by=AppiumBy.XPATH,
                    value='//*[contains(@text, "coins must be between 10 and 10000")]')
    if CoinsRangeForTransfer:
        print("coins Under Range for transfer is : pass ✅ ")
    else:
        print("coins Under Range for transfer is : Failed ❌")
    ###coins over 10000

    # EmailInput.send_keys("pnxdevices@gmail.com")
    # CoinInput.send_keys("10001")
    
    # TransferButton.click()

    # time.sleep(5)
    # CoinsRangeForTransfer = driver.find_element(by=AppiumBy.XPATH,
    #                 value='//*[contains(@text, "coins must be between 10 and 10000")]')
    # if CoinsRangeForTransfer:
    #     print("Coins Over Range for transfer is : pass ✅ ")
    #     watchlog_instance.increment('CoinsOverRangeforTransferPass')
    # else:
    #     print("coins Over Range for transfer is : Failed ❌")
    #     watchlog_instance.increment('CoinsOverRangeforTransferFailed')

    # Seccessful
    driver.implicitly_wait(10)

    EmailInput = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.EditText[@resource-id="gram.members.android:id/textInputEditTextNumberTransferCoin"]')
    EmailInput.send_keys("pnxdevices@gmail.com")
    CoinInput.send_keys(MyCoinsBeforeTransfer)
    time.sleep(1)
    CoinInput.click()
    x, y = 930, 1620
    driver.tap([(x, y)])
    driver.press_keycode(4)
    time.sleep(1)
    TransferButton.click()


    time.sleep(5)
    seccessfullTransfer = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.TextView[@text="Successful transfer"]')
    if seccessfullTransfer:
        okButton = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="OK"]')
        okButton.click()
        print("coins Range for transfer is : pass ✅ ")
        watchlog_instance.increment('transferCoinPass')
        HomePage = driver.find_element(by=AppiumBy.XPATH,
                    value='(//android.widget.FrameLayout[@resource-id="gram.members.android:id/navigation_bar_item_icon_container"])[1]')
        HomePage.click()
    else:
        print("coins Range for transfer is : Failed ❌")
        watchlog_instance.increment('transferCoin')
    
   