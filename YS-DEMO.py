#coding=utf-8
from appium import webdriver
import os

#获取项目的根目录路径
p = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),".."))
print(p)

#获取APP的路径
appPath = lambda x:os.path.join(p,"app",x)

print(appPath("baiduyuedu_5891.apk"))

os.system("adb install baiduyuedu_5891.apk") #安装APP，为了方便， 把APP放到当前脚本同一目录

desired_caps = {}
desired_caps['platformName'] = 'Android'  #声明是iOS还是Android系统
desired_caps['platformVersion'] = '4.4.2'  #Android内核版本号
desired_caps['deviceName'] = '127.0.0.1:62001'  #连接的设备名称
desired_caps['appPackage'] = 'com.baidu.yuedu'  #apk的包名
desired_caps['appActivity'] = '.com.baidu.yuedu.splashActivity'  #apk的launcherActivity
# 不需要每次都安装apk
desired_caps['noReset'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps) #建立session


# os.system("adb uninstall com.baidu.yuedu") #卸载安装APP

