# coding=utf-8
from Package import *
from Public_Module import *
import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

'''调用location.py文件的定位方法'''
we = location

'''调用Swipe.py文件的定位方法'''
swipe = Swipe


class Listen(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """调用公共模块---设备初始化信息"""
        Module_Devices.module_devices(cls)

    @classmethod
    def tearDownClass(cls):
        f = os.popen(r"adb shell dumpsys activity top | findstr ACTIVITY", "r")  # 获取当前界面的Activity
        current_activity = f.read()
        f.close()
        # print(current_activity)  # cmd输出结果

        apppackage_name = 'com.ximalaya.ting.android'
        if apppackage_name in current_activity:
            cls.driver.quit()
        else:
            pass

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        self.imgs = []
        self.addCleanup(self.cleanup)

    def cleanup(self):
        pass

    def test_listen(self):
        u"""喜马拉雅FMAPP【我听】功能"""
        # 调用公共模块---首次启动APP会出现个性化定制选择界面以及新手福利弹窗
        Module_Launch_Judge.module_launch_judge(self)

        '''调用公共模块---登录'''
        Module_Login.module_login(self)

        self.driver.back()
        homepagebtn = we.findId(self.driver, 'com.ximalaya.ting.android:id/host_bottom_hot_lay')
        homepagebtns = homepagebtn.find_elements_by_class_name('android.widget.FrameLayout')
        homepagebtns[0].click()
        time.sleep(5)
        self.add_img()

        '''此处的【返回】操作主要是防止首页出现弹窗'''
        self.driver.back()

        we.findId(self.driver, "com.ximalaya.ting.android:id/main_tv_search").click()
        time.sleep(2)
        self.add_img()
        we.findId(self.driver, "com.ximalaya.ting.android:id/search_search_et").send_keys(u'单田芳经典—西游')
        time.sleep(2)
        self.add_img()
        we.findId(self.driver, "com.ximalaya.ting.android:id/search_search_button").click()
        time.sleep(5)
        self.add_img()
        '''
         we.findXpath(self.driver,
                     "//android.widget.TextView[@content-desc='下载']/../../android.widget.TextView[contains"
                     "(@text,'单田芳经典—西游记')]").click()       
        '''

        we.findText(self.driver, '单田芳经典—西游记').click()
        time.sleep(3)
        self.add_img()
        we.findText(self.driver, '单田芳_西游记_001').click()
        time.sleep(2)
        self.add_img()
        '''判断是否存在引导按钮'''
        def check_guidebtn():
            try:
                guidebtn = we.findText(self.driver, '单田芳_西游记_001')
            except:
                return True
            else:
                guidebtn.click()
                self.add_img()
        check_guidebtn()
        time.sleep(10)
        we.findId(self.driver, 'com.ximalaya.ting.android:id/main_iv_like').click()

        '''IF逻辑判断，如果已经喜欢了，先取消喜欢，再进行点击喜欢操作'''
        def find_toast(driver, message, timeout=5, poll_frequency=0.5):
            try:
                toast = ("xpath", ".//*[contains(@text,'%s')]" % message)
                WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast))
            except:
                return True
            else:
                we.findId(self.driver, 'com.ximalaya.ting.android:id/main_iv_like').click()
                self.add_img()
        find_toast(self.driver, '已取消喜欢')
        self.add_img()

        time.sleep(3)
        Relative_Coordinate_Click.relative_coordinate_click(self.driver, 425, 697)
        time.sleep(1)
        self.add_img()
        '''判断是否弹出取消订阅弹窗'''
        def check_unsubscribebtn():
            try:
                we.findText(self.driver, '确定取消订阅该专辑？')
            except:
                return True
            else:
                we.findId(self.driver, 'com.ximalaya.ting.android:id/ok_btn').click()
                time.sleep(4)
                self.add_img()
                Relative_Coordinate_Click.relative_coordinate_click(self.driver, 422, 466)
                self.add_img()
        check_unsubscribebtn()
        # Judging_Toast.Find_Toast(self.driver,'订阅成功！')
        time.sleep(3)
        we.findAcId(self.driver, "更多").click()
        time.sleep(2)
        self.add_img()
        Relative_Coordinate_Click.relative_coordinate_click(self.driver, 43, 662)
        time.sleep(2)
        self.add_img()
        we.findText(self.driver, '智能选择').click()
        # Judging_Toast.Find_Toast(self.driver, '已添加到下载列表')
        self.add_img()
        time.sleep(3)
        we.findAcId(self.driver, '返回').click()
        time.sleep(1)
        self.add_img()
        self.driver.back()
        time.sleep(1)
        self.add_img()
        self.driver.back()
        time.sleep(1)
        self.add_img()
        self.driver.back()
        time.sleep(1)
        self.add_img()

        listenbtn = we.findId(self.driver, 'com.ximalaya.ting.android:id/host_bottom_hot_lay')
        listenbtns = listenbtn.find_elements_by_class_name('android.widget.FrameLayout')
        listenbtns[1].click()
        time.sleep(2)
        self.add_img()
        we.findId(self.driver, 'com.ximalaya.ting.android:id/main_sort_tv').click()
        time.sleep(1)
        self.add_img()
        we.findText(self.driver, '最新订阅').click()
        time.sleep(1)
        self.add_img()
        we.findAcId(self.driver, '更多按钮').click()
        time.sleep(1)
        self.add_img()
        we.findText(self.driver, '取消订阅').click()
        time.sleep(1)
        self.add_img()
        we.findText(self.driver, '确定').click()
        time.sleep(1)
        self.add_img()
        Judging_Element_Existence.element_noexist_text(self.driver, '单田芳_西游记_100')
        time.sleep(5)

        we.findId(self.driver, 'com.ximalaya.ting.android:id/main_download').click()
        time.sleep(1)
        self.add_img()
        we.findText(self.driver, '声音').click()
        time.sleep(1)
        self.add_img()
        Judging_Element_Existence.element_exist_text(self.driver, '单田芳_西游记_001')
        we.findId(self.driver, 'com.ximalaya.ting.android:id/main_clear_all').click()
        time.sleep(1)
        self.add_img()
        we.findText(self.driver, '全选').click()
        time.sleep(1)
        self.add_img()
        we.findId(self.driver, 'com.ximalaya.ting.android:id/main_batch_delete_track').click()
        time.sleep(1)
        self.add_img()
        we.findId(self.driver, 'com.ximalaya.ting.android:id/ok_btn').click()
        time.sleep(1)
        self.add_img()
        Judging_Element_Existence.element_exist_acid(self.driver, '没有内容')
        self.driver.back()
        self.add_img()

        we.findAcId(self.driver, '历史').click()
        time.sleep(1)
        self.add_img()
        Judging_Element_Existence.element_exist_text(self.driver, '单田芳_西游记_001')
        we.findAcId(self.driver, '清空').click()
        time.sleep(1)
        self.add_img()
        we.findId(self.driver, 'com.ximalaya.ting.android:id/ok_btn').click()
        time.sleep(1)
        self.add_img()
        Judging_Element_Existence.element_exist_text(self.driver, '没有收听过节目')
        self.driver.back()
        time.sleep(1)
        self.add_img()

        we.findAcId(self.driver, '听单').click()
        time.sleep(1)
        self.add_img()
        we.findText(self.driver, '我喜欢的声音').click()
        time.sleep(1)
        self.add_img()
        Judging_Element_Existence.element_exist_text(self.driver, '单田芳_西游记_001')
        we.findText(self.driver, '单田芳_西游记_001').click()
        time.sleep(1)
        self.add_img()
        # PlayBtn = we.findId(self.driver,'com.ximalaya.ting.android:id/host_bottom_hot_lay')
        # PlayBtns = PlayBtn.find_elements_by_class_name('android.widget.FrameLayout')
        # PlayBtns[2].click()
        # time.sleep(2)
        # self.add_img()
        we.findId(self.driver, "com.ximalaya.ting.android:id/main_iv_like").click()
        self.add_img()
        '''
        判断取消喜欢后是否弹出[已取消喜欢]提示
        Judging_Toast.Find_Toast(self.driver,'已取消喜欢')
        '''
        time.sleep(2)
        we.findAcId(self.driver, "返回").click()
        time.sleep(1)
        self.add_img()
        self.driver.back()
        time.sleep(1)
        self.add_img()
        we.findText(self.driver, '我喜欢的声音').click()
        time.sleep(1)
        self.add_img()
        Judging_Element_Existence.element_exist_text(self.driver, '单田芳_西游记_001')

        self.driver.back()
        time.sleep(1)
        self.add_img()
        self.driver.back()
        time.sleep(1)
        self.add_img()

        '''此处的【返回】操作主要是防止首页出现弹窗'''
        self.driver.back()

        accountbtn = we.findId(self.driver, 'com.ximalaya.ting.android:id/host_bottom_hot_lay')
        accountbtns = accountbtn.find_elements_by_class_name('android.widget.FrameLayout')
        accountbtns[4].click()
        time.sleep(2)
        self.add_img()

        we.findAcId(self.driver, '设置').click()
        time.sleep(2)
        self.add_img()
        '''调用公共模块---退出登录'''
        Module_Logout.module_logout(self)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Listen)
    unittest.TextTestRunner(verbosity=2).run(suite)






