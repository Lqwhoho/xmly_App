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


class Setting(unittest.TestCase):
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

    def test_setting(self):
        u"""喜马拉雅FMAPP【设置】功能"""
        # 调用公共模块---首次启动APP会出现个性化定制选择界面以及新手福利弹窗
        Module_Launch_Judge.module_launch_judge(self)

        '''调用公共模块---登录'''
        Module_Login.module_login(self)

        time.sleep(2)
        swipe.swipeDown(self.driver)
        time.sleep(1)
        self.add_img()
        swipe.swipeDown(self.driver)
        time.sleep(1)
        self.add_img()

        we.findId(self.driver, "com.ximalaya.ting.android:id/main_tv_hardware").click()
        time.sleep(2)
        self.add_img()
        dowmloadbtn1 = we.findId(self.driver, "com.ximalaya.ting.android:id/host_tv_download").text
        self.assertEqual(dowmloadbtn1, '下载')
        we.findId(self.driver, "com.ximalaya.ting.android:id/host_tv_cancel").click()
        time.sleep(1)
        self.add_img()

        we.findId(self.driver, "com.ximalaya.ting.android:id/main_tv_carmode").click()
        self.add_img()
        dowmloadbtn2 = we.findId(self.driver, "com.ximalaya.ting.android:id/host_tv_download").text
        self.assertEqual(dowmloadbtn2, '下载')
        we.findId(self.driver, "com.ximalaya.ting.android:id/host_tv_cancel").click()
        time.sleep(1)
        self.add_img()

        we.findId(self.driver, "com.ximalaya.ting.android:id/main_tv_watch").click()
        self.add_img()
        dowmloadbtn3 = we.findId(self.driver,"com.ximalaya.ting.android:id/host_tv_download").text
        self.assertEqual(dowmloadbtn3, '下载')
        we.findId(self.driver, "com.ximalaya.ting.android:id/host_tv_cancel").click()
        time.sleep(1)
        self.add_img()

        we.findId(self.driver, "com.ximalaya.ting.android:id/main_tv_special_alarm").click()
        time.sleep(3)
        self.add_img()
        alarmbtn = we.findId(self.driver, "com.ximalaya.ting.android:id/main_wakeup_name").text
        self.assertEqual(alarmbtn, '闹铃开关')
        self.driver.back()
        time.sleep(3)
        self.add_img()

        we.findId(self.driver, "com.ximalaya.ting.android:id/main_tv_account_safety").click()
        # time.sleep(8)
        self.add_img()
        Wait_Element.wait_element(self.driver, 15, By.XPATH,  '//*[@text="账号绑定"]', '【账号与安全】界面加载失败')
        we.findText(self.driver, '账号绑定').click()
        self.add_img()
        phone_number = we.findId(self.driver,
                                 "com.ximalaya.ting.android:id/main_setting_otherinfo").text
        self.assertEqual(phone_number, '159****0373')
        self.driver.back()
        self.add_img()
        we.findText(self.driver, '最近登录设备').click()
        time.sleep(3)
        self.add_img()
        '''判断是否存在【广州】控件'''
        Judging_Element_Existence.element_exist_text(self.driver, '广州')

        self.driver.back()
        self.add_img()
        we.findText(self.driver, '常见问题').click()
        time.sleep(1)
        self.add_img()
        self.driver.back()
        time.sleep(1)
        self.add_img()
        self.driver.back()
        time.sleep(1)
        self.add_img()

        we.findText(self.driver, '推送设置').click()
        self.add_img()
        self.driver.back()
        time.sleep(1)
        self.add_img()

        we.findText(self.driver, '下载音质设置').click()
        time.sleep(1)
        self.add_img()
        we.findId(self.driver, "com.ximalaya.ting.android:id/main_tv_title_1").click()
        time.sleep(1)
        self.add_img()
        self.driver.back()
        time.sleep(1)
        self.add_img()
        '''判断是否存在【高清优先】控件'''
        Judging_Element_Existence.element_exist_text(self.driver, '高清优先')

        we.findId(self.driver, "com.ximalaya.ting.android:id/main_tv_down_cache").click()
        time.sleep(1)
        self.add_img()
        self.driver.back()
        self.add_img()
        Swipe.swipeUp(self.driver)
        time.sleep(1)
        self.add_img()

        we.findId(self.driver, "com.ximalaya.ting.android:id/main_specialFunc").click()
        time.sleep(1)
        self.add_img()
        we.findId(self.driver, "com.ximalaya.ting.android:id/comp_actionbar_icon").click()
        self.add_img()
        '''判断是否存在【微信朋友圈】控件'''
        Judging_Element_Existence.element_exist_text(self.driver, '微信朋友圈')
        we.findId(self.driver, "com.ximalaya.ting.android:id/host_cancle_share_and_dismiss").click()
        time.sleep(1)
        self.add_img()
        self.driver.back()
        self.add_img()
        swipe.swipeUp(self.driver)
        time.sleep(1)
        self.add_img()

        we.findId(self.driver, "com.ximalaya.ting.android:id/main_newVersionIntro").click()
        time.sleep(2)
        self.add_img()
        we.findAcId(self.driver, "返回").click()
        time.sleep(1)
        self.add_img()
        '''APP存在bug，需点击两次以上才会出现提示'''
        we.findId(self.driver, "com.ximalaya.ting.android:id/main_tv_check_update").click()
        self.add_img()
        we.findId(self.driver, "com.ximalaya.ting.android:id/main_tv_check_update").click()
        self.add_img()
        '''判断是否存在提示【当前已是最新版本】Toast'''
        Judging_Toast.find_toast(self.driver, '当前已是最新版本')
        time.sleep(2)

        we.findId(self.driver, "com.ximalaya.ting.android:id/main_tv_about").click()
        self.add_img()
        '''判断是否存在【喜马拉雅app图标】控件'''
        Judging_Element_Existence.element_exist_acid(self.driver, '喜马拉雅app图标')
        self.driver.back()
        self.add_img()
        swipe.swipeUp(self.driver)
        self.add_img()

        '''调用公共模块---退出登录'''
        Module_Logout.module_logout(self)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Setting)
    unittest.TextTestRunner(verbosity=2).run(suite)
