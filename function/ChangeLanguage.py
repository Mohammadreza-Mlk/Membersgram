import time
from appium.webdriver.common.appiumby import AppiumBy
from watchlog import Watchlog
watchlog_instance = Watchlog()


def Language(driver):
    try:
        driver.implicitly_wait(5)

        LanguageButton = driver.find_element(by=AppiumBy.XPATH,
                                                            value='//android.widget.Button[@text="زبان (Language)"]')
        LanguageButton.click()
        
        driver.implicitly_wait(5)

        English = driver.find_element(by=AppiumBy.XPATH,
                                        value='//android.widget.RadioButton[@resource-id="gram.members.android:id/englishButton"]')
        English.click()
        print("metric")
        watchlog_instance.increment('Change_Language')
    except:
            print("language is English")