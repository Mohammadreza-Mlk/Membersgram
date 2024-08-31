import time
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from watchlog import Watchlog
watchlog_instance = Watchlog()

def LogOut(driver):
    driver.implicitly_wait(15)
    ProfileTab = driver.find_element(by=AppiumBy.XPATH,
                    value='(//android.widget.FrameLayout[@resource-id="gram.members.android:id/navigation_bar_item_icon_container"])[4]')
    ProfileTab.click()
    driver.implicitly_wait(15)
    LogOutInProfile = driver.find_element(by=AppiumBy.XPATH,
                    value='//androidx.recyclerview.widget.RecyclerView[@resource-id="gram.members.android:id/rvProfile"]/android.view.ViewGroup[7]')
    LogOutInProfile.click()
    driver.implicitly_wait(15)
    LogOutButton = driver.find_element(by=AppiumBy.XPATH,
                    value='//androidx.recyclerview.widget.RecyclerView[@resource-id="gram.members.android:id/rvExitAccount"]/android.view.ViewGroup[4]')
    LogOutButton.click()
    ConfirmLogOut = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Logout"]')
    ConfirmLogOut.click()
    watchlog_instance.increment('LogOut')