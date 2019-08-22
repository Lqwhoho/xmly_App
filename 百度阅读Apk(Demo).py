#coding=utf-8
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
desired_caps['platformName'] = 'Android'            #声明是iOS还是Android系统
desired_caps['platformVersion'] = '5.1.1'           #Android内核版本号
desired_caps['deviceName'] = '127.0.0.1:62025'      #连接的设备名称
desired_caps['appPackage'] = 'com.baidu.yuedu'    #apk的包名
desired_caps['appActivity'] = 'com.baidu.yuedu.splash.SplashActivity'           #apk的launcherActivity
desired_caps['unicodeKeyboard'] = True              #使用Unicode编码方式发送字符串
desired_caps['resetKeyboard'] = True                #隐藏键盘
desired_caps['noReset'] = True                      #不需要每次都安装apk
desired_caps['automationName'] = 'Uiautomator2'

time.sleep(5)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)  #建立session
time.sleep(20)
# #获取当前界面的activity
# ac = driver.current_activity
# print(ac)
driver.wait_activity(".base.ui.MainActivity",10)                #等主页面activity出现30秒内

'''
#android_uiautomator定位
#1.text定位
loc_text = 'new UiSelector().text("图书")'
driver.find_element_by_android_uiautomator(loc_text).click()

#2.textContains
loc_textContains = 'new UiSelector().textContains("男生")'
driver.find_element_by_android_uiautomator(loc_textContains).click()

#3.textStartsWith
loc_textStart = 'new UiSelector().textStartsWith("VIP")'
driver.find_element_by_android_uiautomator(loc_textStart).click()

#resourceId定位搜索框
loc_id = 'new UiSelector().resourceId("com.baidu.yuedu:id/tv_search")'
driver.find_element_by_android_uiautomator(loc_id).click()
time.sleep(2)

#classname复数定位
loc_class = 'new UiSelector().className("android.widget.ImageView")'
driver.find_elements_by_android_uiautomator(loc_class)[0].click()

#4.id+text
id_text = 'resourceId("com.baidu.yuedu:id/tv_search").text("搜索")'
driver.find_element_by_android_uiautomator(id_text).click()
time.sleep(2)


#5.class+text
class_text = 'className("android.widget.TextView").text("免费图书")'
driver.find_element_by_android_uiautomator(class_text).click()
time.sleep(2)

#6.父子关系childSe;ector
son = 'resourceId("com.baidu.yuedu:id/ll_online_tabs").childSelector(text("男生"))'
driver.find_element_by_android_uiautomator(son).click()

#7.兄弟关系fromParent
brother = 'resourceId("com.baidu.yuedu:id/tv_search").fromParent(text("分类"))'
driver.find_element_by_android_uiautomator(brother).click()
time.sleep(2)

#8.resourceIdMatches(".*xxx$")
idMatches = 'resourceIdMatches(".*id/tv_search$")'
driver.find_element_by_android_uiautomator(idMatches).click()
time.sleep(2)

#9.classNameMatches(".*xxx$")
classMatches = 'classNameMatches(".*android.widget.TextView$").text("女生")'
driver.find_element_by_android_uiautomator(classMatches).click()
time.sleep(2)
'''


'''
#list定位
search = driver.find_element_by_id("com.baidu.yuedu:id/tv_search")      #定位搜索按钮
print(search)                                                           #打印元素对象
searchs = driver.find_elements_by_id("com.baidu.yuedu:id/tv_search")
print(searchs)                                                          #打印list
print(type(searchs))
driver.find_element_by_id("com.baidu.yuedu:id/tv_search").click()
time.sleep(3)
driver.find_element_by_id("com.baidu.yuedu:id/full_text_search_bar_input").send_keys(u"Python接口")       #输入文字Python接口
time.sleep(3)
driver.find_element_by_id("com.baidu.yuedu:id/full_text_search_bar_search").click()         #点击搜索按钮
time.sleep(5)
print(driver.contexts)
'''


'''
#toast消息判断
driver.find_element_by_id('com.baidu.yuedu:id/tinyin_title').click()                     #点击书城按钮
time.sleep(2)
driver.find_element_by_xpath("//*[@text='图书']").click()       #Xpath定位点击图书控件
# driver.find_element_by_name("图书").click()                   #点击图书按钮
time.sleep(2)
driver.back()           #点击返回
toast_loc = ("xpath",".//*[contains(@text,'再按一次退出')]")     #定位toast元素
t = WebDriverWait(driver,10,0.1).until(EC.presence_of_element_located(toast_loc))
print(t)
'''


'''
#获取坐标
#获取屏幕的size
size = driver.get_window_size()
print(size)

#获取屏幕宽度width
print(size['width'])

#获取屏幕高度width
print(size['height'])
'''


'''
#模拟手势点击tap 坐标定位
driver.find_element_by_id("com.baidu.yuedu:id/iv_book_shelf_icon").click() #点击书架按钮
time.sleep(3)
driver.tap([(270,753),(449,849) ],500) #点击去找书
time.sleep(3)
driver.find_element_by_name("分类").click()   #点击右上角分类按钮
time.sleep(3)
driver.back()                   #返回上一页
time.sleep(3)
driver.find_element_by_id("com.baidu.yuedu:id/iv_book_shelf_icon").click() #点击书架按钮
time.sleep(3)
driver.tap([(660,62),(696,98)],500)        #点击右上角搜索按钮
time.sleep(5)
'''


'''
#获取元素属性
#1.获取text
driver.find_element_by_id("com.baidu.yuedu:id/useraccount_title").click()
time.sleep(2)
text = driver.find_element_by_id("com.baidu.yuedu:id/tx_account_name").text
print(text)

#2.获取tag_name（实质上是获取class属性）
t2 = driver.find_element_by_id("com.baidu.yuedu:id/book_title").tag_name
print(t2)

#3.获取get_attribute
#content-desc属性不为空
driver.find_element_by_id("com.baidu.yuedu:id/useraccount_title").click()
time.sleep(2)
t3 = driver.find_element_by_id("com.baidu.yuedu:id/news_center_icon").get_attribute("name")
print(t3)
'''


'''
#adb shell点击事件(tap) input事件
adb1 = 'adb shell input tap 600 1255'
os.system(adb1)
time.sleep(2)

adb2 = 'adb shell input tap 180 180'
os.system(adb2)
time.sleep(2)
'''



'''
#长按(long_press)
driver.press_keycode(3)
time.sleep(2)
el = driver.find_element_by_accessibility_id("通讯录")
TouchAction(driver).long_press(el).perform()
time.sleep(3)
'''

#Xpath定位
#1.基本属性定位
driver.find_element_by_xpath("//*[@text='我的']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@content-desc='用户头像']").click()
time.sleep(6)
driver.back()           #物理返回键
time.sleep(2)
driver.find_element_by_xpath('//*[contains(@text,"联名卡")]').click()      #contains模糊匹配text
time.sleep(2)
driver.press_keycode(4)             #物理返回键
time.sleep(2)
#模糊定位
driver.find_element_by_xpath("//*[contains(@content-desc,'消息')]").click()        #contains模糊匹配content-desc
time.sleep(2)
driver.find_element_by_xpath("//*[contains(@resource-id,'com.baidu.yuedu:id/infocenter_backbutton_imageview')]").click()      #contains模糊匹配resource-id
time.sleep(2)
driver.find_element_by_id("com.baidu.yuedu:id/tinyin_title").click()
time.sleep(1)
driver.find_element_by_id("com.baidu.yuedu:id/tv_search").click()
time.sleep(1)
driver.find_element_by_xpath("//*[contains(@class,'EditText')]").click()                 #contains模糊匹配class
time.sleep(1)
driver.back()
driver.find_element_by_xpath("//*[contains(@content-desc,'购物')]").click()
time.sleep(2)
#组合定位
id_class = '//android.widget.TextView[@resource-id="com.baidu.yuedu:id/wr_change"]'     #id和class属性
driver.find_element_by_xpath(id_class).click()
time.sleep(2)
text_index = '//*[@text="去书城逛逛" and @index = "2"]'                                  #text和index属性
driver.find_element_by_xpath(text_index).click()
time.sleep(3)
driver.find_element_by_id("com.baidu.yuedu:id/tv_search").click()
time.sleep(1)
class_text = '//android.widget.EditText[@text = "书名、作者、出版社"]'                  #class和text属性
driver.find_element_by_xpath(class_text).send_keys("橙红年代")
time.sleep(2)
id_desc = '//*[contains(@resource-id,"com.baidu.yuedu:id/full_text_search_bar_search") and @content-desc="去找书"]'            #id和class属性
driver.find_element_by_xpath(id_desc).click()
time.sleep(5)
#层级定位-父定位子
# driver.find_element_by_id('com.baidu.yuedu:id/full_text_search_bar_back').click()
fa_sun = '//*[@resource-id="com.baidu.yuedu:id/full_text_search_bar"] /android.widget.ImageView[1]'                 #多个相同class，通过xpath索引去查找
driver.find_element_by_xpath(fa_sun).click()
time.sleep(2)

