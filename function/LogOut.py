import time
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from watchlog import Watchlog
watchlog_instance = Watchlog()
from function.result import log_test_result 

def LogOut(driver):
    driver.implicitly_wait(15)
    ProfileTab = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.FrameLayout[@content-desc="Profile"]')
    ProfileTab.click()
    driver.implicitly_wait(15)
    EditButton = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Edit"]')
    EditButton.click()
    
    driver.implicitly_wait(15)
    circlemenu = driver.find_element(by=AppiumBy.XPATH,
                    value='(//android.widget.FrameLayout[@resource-id="gram.members.android:id/nav_host_fragment"])[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageButton[2]')
    circlemenu.click()
    driver.implicitly_wait(15)
    LogOutInProfile = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.TextView[@text="Logout"]')
    LogOutInProfile.click()
    driver.implicitly_wait(15)
    LogOutButton = driver.find_element(by=AppiumBy.XPATH,
                    value='//androidx.recyclerview.widget.RecyclerView[@resource-id="gram.members.android:id/rvExitAccount"]/android.view.ViewGroup[4]')
    LogOutButton.click()
    ConfirmLogOut = driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.Button[@text="Logout"]')
    ConfirmLogOut.click()
    log_test_result("logout", "pass")
    # time.sleep(2)
    # print("metric")
    # watchlog_instance.increment('LogOut')
    # time.sleep(2)
    # print("metric")
