# coding = utf - 8
from Package import *
from Public_Module import *
import time
import unittest
import os


'''调用location.py文件的定位方法'''
we = location

'''调用Swipe.py文件的定位方法'''
swipe = Swipe


class Logout(unittest.TestCase):
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

    def test_logout(self):
        u"""喜马拉雅FMAPP【退出登录】"""
        # 调用公共模块---首次启动APP会出现个性化定制选择界面以及新手福利弹窗
        Module_Launch_Judge.module_launch_judge(self)

        '''调用公共模块---登录'''
        Module_Login.module_login(self)

        swipe.swipeUp(self.driver)
        time.sleep(2)
        self.add_img()

        # 退出登录
        we.findId(self.driver, "com.ximalaya.ting.android:id/main_tv_login").click()
        time.sleep(1)
        self.add_img()
        we.findId(self.driver, "com.ximalaya.ting.android:id/ok_btn").click()
        time.sleep(1)
        self.add_img()
        swipe.swipeUp(self.driver)
        time.sleep(2)
        self.add_img()

        '''检查是否成功退出登录'''
        Judging_Element_Existence.element_noexist_text(self.driver, '退出登录')


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(Logout)
    unittest.TextTestRunner(verbosity=2).run(suite)
