"""设备初始化信息"""
from appium import webdriver
import time


def module_devices(self):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'  # 声明是iOS还是Android系统
    desired_caps['platformVersion'] = '5.1.1'  # Android内核版本号
    desired_caps['deviceName'] = '127.0.0.1:62025'  # 连接的设备名称
    # desired_caps['platformVersion'] = '7.1.2'  # Android内核版本号
    # desired_caps['deviceName'] = '127.0.0.1:62027'  # 连接的设备名称
    desired_caps['appPackage'] = 'com.ximalaya.ting.android'  # apk的包名
    desired_caps['appActivity'] = '.host.activity.MainActivity'  # apk的launcherActivity
    desired_caps['unicodeKeyboard'] = True  # 使用Unicode编码方式发送字符串
    desired_caps['resetKeyboard'] = True  # 隐藏键盘
    desired_caps['Reset'] = False  # 是否重新安装apk
    desired_caps['automationName'] = 'uiautomator2'
    self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 建立session
    # self.driver.implicitly_wait(30)
    time.sleep(10)


'''
def module_devices_712(self):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'  # 声明是iOS还是Android系统
    desired_caps['platformVersion'] = '7.1.2'  # Android内核版本号
    desired_caps['deviceName'] = '127.0.0.1:62027'  # 连接的设备名称
    desired_caps['appPackage'] = 'com.ximalaya.ting.android'  # apk的包名
    desired_caps['appActivity'] = 'host.activity.WelComeActivity'  # apk的launcherActivity
    desired_caps['unicodeKeyboard'] = True  # 使用Unicode编码方式发送字符串
    desired_caps['resetKeyboard'] = True  # 隐藏键盘
    desired_caps['Reset'] = True  #不需要每次都安装apk
    desired_caps['automationName'] = 'uiautomator2'
    self.driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_caps)  # 建立session
    # self.driver.implicitly_wait(30)
    time.sleep(10)
'''

