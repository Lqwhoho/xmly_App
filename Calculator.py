# coding=utf-8
from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'    # 声明是iOS还是Android系统
desired_caps['platformVersion'] = '4.4.2'   # Android内核版本号
desired_caps['deviceName'] = '127.0.0.1:62001'  # 连接的设备名称
# 测试apk包的路径
# desired_caps['app'] = apk_path + '\\app\\shoujibaidu.apk'
# 不需要每次都安装apk
desired_caps['noReset'] = True
desired_caps['appPackage'] = 'com.youdao.calculator'    # apk的包名
desired_caps['appActivity'] = '.activities.MainActivity'    # apk的launcherActivity

time.sleep(3)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)      # 建立session

driver.find_element_by_name('2').click()

driver.find_element_by_name('5').click()

driver.find_element_by_name('0').click()

driver.find_element_by_name('×').click()

driver.find_element_by_name('2').click()

driver.find_element_by_name('+').click()

driver.find_element_by_name('3').click()

driver.find_element_by_name('8').click()

driver.find_element_by_name('−').click()

driver.find_element_by_name('1').click()

driver.find_element_by_name('7').click()

driver.find_element_by_name('.').click()

driver.find_element_by_name('8').click()

driver.find_element_by_name('6').click()

driver.find_element_by_name('8').click()

driver.find_element_by_name('6').click()

driver.find_element_by_name('=').click()

# assertEqual('520.1314',driver.find_elements_by_class_name("android.widget.EditText").text)

driver.quit()
