#coding=utf-8
from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'  #声明是iOS还是Android系统
desired_caps['platformVersion'] = '4.4.2'  #Android内核版本号
desired_caps['deviceName'] = '127.0.0.1:62001'  #连接的设备名称
desired_caps['appPackage'] = 'com.android.settings'  #apk的包名
desired_caps['appActivity'] = 'Settings'  #apk的launcherActivity

time.sleep(3)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)  #建立session

driver.find_element_by_name('声音').click()  #点击元素

driver.find_element_by_name('音量').click()

driver.keyevent(4)

driver.keyevent(24)

driver.keyevent(24)

driver.keyevent(25)

driver.quit()