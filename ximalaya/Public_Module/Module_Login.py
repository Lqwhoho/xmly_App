"""登录APP操作模块"""
import time
from Package import *
from selenium.webdriver.common.by import By
'''调用location.py文件的定位方法'''
we = location

'''调用Swipe.py文件的定位方法'''
swipe = Swipe


def module_login(self):
    listdata = Read_Excel_Data.read_excel_data_by_index('E:\\Python脚本\\APP\\ximalaya\\Data\\userinfo.xlsx')
    print(listdata)
    if len(listdata) <= 0:
        assert 0, u"Excel数据异常"
    """点击底部按钮【未登录】，此处采用层级定位list定位方法"""
    down_button = we.findId(self.driver, 'com.ximalaya.ting.android:id/host_bottom_hot_lay')
    down_buttons = down_button.find_elements_by_class_name('android.widget.FrameLayout')
    down_buttons[4].click()
    time.sleep(1)
    self.add_img()

    we.findAcId(self.driver, '设置').click()
    time.sleep(2)
    self.add_img()

    swipe.swipeUp(self.driver)
    time.sleep(2)
    self.add_img()

    we.findId(self.driver, "com.ximalaya.ting.android:id/main_tv_login").click()
    time.sleep(1)
    self.add_img()
    we.findId(self.driver, "com.ximalaya.ting.android:id/main_login_more").click()
    time.sleep(1)
    self.add_img()
    we.findId(self.driver, "com.ximalaya.ting.android:id/main_login_with_pwd").click()
    time.sleep(1)
    self.add_img()
    we.findId(self.driver, "com.ximalaya.ting.android:id/main_username").send_keys(listdata[0]['username'])
    time.sleep(1)
    self.add_img()
    we.findId(self.driver, "com.ximalaya.ting.android:id/main_password").send_keys(listdata[0]['password'])
    time.sleep(1)
    self.add_img()
    we.findId(self.driver, "com.ximalaya.ting.android:id/main_login").click()
    self.add_img()
    # Judging_Toast.Find_Toast(self.driver,'登录成功')
    time.sleep(13)
    Wait_Element.wait_element(self.driver, 60, By.ID, 'com.ximalaya.ting.android:id/layout_center', '页面加载失败')
    swipe.swipeUp(self.driver)
    time.sleep(1)

    '''检查是否登录成功'''
    logoutbtn = we.findId(self.driver, "com.ximalaya.ting.android:id/main_tv_login").text
    self.assertEqual(logoutbtn, '退出登录')
