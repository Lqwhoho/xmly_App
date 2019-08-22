# coding=utf-8
from Package import *
from Public_Module import *
import time
import unittest
from selenium.webdriver.common.by import By
import os


'''调用location.py文件的定位方法'''
we = location

'''调用Swipe.py文件的定位方法'''
swipe = Swipe


class Discovery(unittest.TestCase):
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

    def test_discovery(self):
        u"""喜马拉雅FMAPP【发现】功能"""
        # 调用公共模块---首次启动APP会出现个性化定制选择界面以及新手福利弹窗
        Module_Launch_Judge.module_launch_judge(self)

        '''调用公共模块---登录'''
        Module_Login.module_login(self)

        self.driver.back()
        discoverybtn = we.findId(self.driver, 'com.ximalaya.ting.android:id/host_bottom_hot_lay')
        discoverybtns = discoverybtn.find_elements_by_class_name('android.widget.FrameLayout')
        discoverybtns[3].click()
        time.sleep(8)
        self.add_img()

        we.findId(self.driver, 'com.ximalaya.ting.android:id/feed_home_iv_back').click()
        time.sleep(2)
        self.add_img()
        Relative_Coordinate_Click.relative_coordinate_click(self.driver, 450, 45)
        self.add_img()
        we.findId(self.driver, 'com.ximalaya.ting.android:id/search_search_et').send_keys(u'超级制作')
        self.add_img()
        we.findId(self.driver, 'com.ximalaya.ting.android:id/search_search_button').click()
        time.sleep(2)
        self.add_img()

        id1 = we.findsText(self.driver, '超级制作')
        id1[1].click()
        self.add_img()
        time.sleep(10)

        def check_attention():
            try:
                we.findAcId(self.driver, '关注主播')
            except:
                return True
            else:
                we.findAcId(self.driver, '关注主播').click()
                time.sleep(3)
                self.add_img()
                we.findText(self.driver, '确定').click()
                time.sleep(4)
                self.add_img()
        check_attention()
        time.sleep(1)
        we.findAcId(self.driver, '取消关注').click()
        self.add_img()
        # Judging_Toast.find_toast(self.driver, '关注成功')
        self.driver.back()
        time.sleep(1)
        self.add_img()
        self.driver.back()
        time.sleep(1)
        self.add_img()
        we.findText(self.driver, '通讯录好友').click()
        time.sleep(1)
        self.add_img()
        Judging_Element_Existence.element_exist_text(self.driver, '呼朋引伴来喜马拉雅吧～')
        self.driver.back()
        time.sleep(1)
        self.add_img()
        self.driver.back()
        time.sleep(1)
        self.add_img()
        we.findId(self.driver, 'com.ximalaya.ting.android:id/feed_home_title_search').click()
        time.sleep(1)
        self.add_img()
        we.findId(self.driver, "com.ximalaya.ting.android:id/search_search_et").send_keys(u'水浒传')
        time.sleep(1)
        self.add_img()
        we.findId(self.driver, "com.ximalaya.ting.android:id/search_search_button").click()
        time.sleep(3)
        self.add_img()
        self.driver.back()
        time.sleep(1)
        self.add_img()
        self.driver.back()
        time.sleep(1)
        self.add_img()
        we.findId(self.driver, 'com.ximalaya.ting.android:id/feed_home_title_search').click()
        time.sleep(2)
        self.add_img()
        Judging_Element_Existence.element_exist_text(self.driver, '水浒传')
        we.findXpath(self.driver, '//android.widget.ImageView[@content-desc="清除历史数据"]').click()
        time.sleep(2)
        self.add_img()
        self.driver.back()
        time.sleep(1)
        self.add_img()

        we.findText(self.driver, '关注').click()
        time.sleep(8)
        self.add_img()

        Relative_Coordinate_Click.relative_coordinate_click(self.driver, 439, 704)
        self.add_img()

        we.findText(self.driver, '图文').click()
        self.add_img()
        we.findId(self.driver, 'com.ximalaya.ting.android:id/feed_edit_content').send_keys(u'nice')
        self.add_img()
        time.sleep(1)
        we.findText(self.driver, '发布').click()
        self.add_img()
        # Judging_Toast.find_toast(self.driver, '动态发布成功')
        time.sleep(3)

        accountbtn = we.findId(self.driver,'com.ximalaya.ting.android:id/host_bottom_hot_lay')
        accountbtns = accountbtn.find_elements_by_class_name('android.widget.FrameLayout')
        accountbtns[4].click()
        time.sleep(2)
        self.add_img()

        swipe.swipeDown(self.driver)
        time.sleep(1)
        self.add_img()
        # Relative_Coordinate_Click.relative_coordinate_click(self.driver, 191, 132)
        we.findId(self.driver, 'com.ximalaya.ting.android:id/main_my_space_my_attention').click()
        time.sleep(2)
        Wait_Element.wait_element(self.driver, 30, By.ID, 'com.ximalaya.ting.android:id/main_btn_follow', '【关注】页面加载失败')
        self.add_img()
        Judging_Element_Existence.element_exist_text(self.driver, '超级制作')
        we.findText(self.driver, '超级制作').click()
        time.sleep(5)
        self.add_img()
        we.findAcId(self.driver, '关注主播').click()
        time.sleep(1)
        self.add_img()
        we.findText(self.driver, '确定').click()
        time.sleep(4)
        self.add_img()
        Judging_Element_Existence.element_exist_acid(self.driver, '取消关注')
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.add_img()
        self.driver.back()
        time.sleep(1)
        self.add_img()

        we.findAcId(self.driver, '设置').click()
        time.sleep(2)
        self.add_img()
        '''调用公共模块---退出登录'''
        Module_Logout.module_logout(self)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Discovery)
    unittest.TextTestRunner(verbosity=2).run(suite)










