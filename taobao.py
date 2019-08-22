# coding=utf-8
from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'            #声明是iOS还是Android系统
desired_caps['platformVersion'] = '5.1.1'           #Android内核版本号
desired_caps['deviceName'] = '127.0.0.1:62025'      #连接的设备名称
desired_caps['appPackage'] = 'com.taobao.taobao'    #apk的包名
desired_caps['appActivity'] = 'com.taobao.tao.welcome.Welcome'           #apk的launcherActivity
desired_caps['unicodeKeyboard'] = True              #使用Unicode编码方式发送字符串
desired_caps['resetKeyboard'] = True                #隐藏键盘
desired_caps['noReset'] = True                      #不需要每次都安装apk

time.sleep(5)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)  #建立session

time.sleep(10)

'''
driver.find_element_by_id("com.taobao.taobao:id/searchEdit").click()
time.sleep(10)
driver.find_element_by_id("com.taobao.taobao:id/searchEdit").send_keys(u"法兰绒衬衫")
time.sleep(5)
# driver.find_element_by_id("com.taobao.taobao:id/searchbtn").click()
driver.find_element_by_accessibility_id("搜索").click()           #定位content-desc的值
'''

# driver.find_element_by_xpath("//*[@resource-id='com.taobao.taobao:id/tv_scan_text']").click()
driver.find_element_by_accessibility_id('我的淘宝').click()
time.sleep(5)
driver.quit()
