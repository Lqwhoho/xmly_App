# coding = utf - 8
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


class Login(unittest.TestCase):
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

    def test_login(self):
        u"""喜马拉雅FMAPP【登录流程】"""
        # 调用公共模块---首次启动APP会出现个性化定制选择界面以及新手福利弹窗
        Module_Launch_Judge.module_launch_judge(self)

        '''点击底部按钮【未登录】，此处采用层级定位list定位方法'''
        down_button = we.findId(self.driver, 'com.ximalaya.ting.android:id/host_bottom_hot_lay')
        down_buttons = down_button.find_elements_by_class_name('android.widget.FrameLayout')
        down_buttons[4].click()
        self.add_img()

        we.findAcId(self.driver, '设置').click()
        time.sleep(2)
        self.add_img()

        swipe.swipeUp(self.driver)
        time.sleep(2)
        self.add_img()

        # we.findId(self.driver, "com.ximalaya.ting.android:id/main_tv_login").click()
        we.find_reid(self.driver, "com.ximalaya.ting.android:id/main_tv_login").click()
        time.sleep(1)
        self.add_img()
        we.findId(self.driver, "com.ximalaya.ting.android:id/main_login_more").click()
        time.sleep(1)
        self.add_img()
        we.findId(self.driver, "com.ximalaya.ting.android:id/main_login_with_pwd").click()
        time.sleep(1)
        self.add_img()
        we.findId(self.driver, "com.ximalaya.ting.android:id/main_username").send_keys('15918860373')
        time.sleep(1)
        self.add_img()
        we.findId(self.driver, "com.ximalaya.ting.android:id/main_password").send_keys('QQ45266347')
        time.sleep(1)
        self.add_img()
        we.findId(self.driver, "com.ximalaya.ting.android:id/main_login").click()
        Wait_Element.wait_element(self.driver, 60, By.ID, 'com.ximalaya.ting.android:id/layout_center', '页面加载失败')
        self.add_img()
        swipe.swipeUp(self.driver)
        time.sleep(1)

        '''检查是否登录成功'''
        logoutbtn = we.findId(self.driver, "com.ximalaya.ting.android:id/main_tv_login").text
        self.assertEqual(logoutbtn, '退出登录')


# threads = []
# t1 = threading.Thread(target=Module_Devices.module_devices_511())
# threads.append(t1)
#
# t2 = threading.Thread(target=Module_Devices.module_devices_712())
# threads.append(t2)


if __name__ == "__main__":
    # unittest.main()
    # for t in threads:
    #     t.start()
    suite = unittest.TestLoader().loadTestsFromTestCase(Login)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # suite = unittest.TestLoader().loadTestsFromTestCase(Login)
    # Now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
    # FileName = 'E:\\Python脚本\\APP\\ximalaya\\Report\\' + Now + 'Result.html'
    # FP = open(FileName, 'wb')
    #
    # runner = HTMLTestRunner(
    #     stream=FP,
    #     title=u'喜马拉雅FMAPP测试报告',
    #     description=u'用例执行情况:',
    #     verbosity=2,
    #     retry=1,
    #     save_last_try=True
    # )
    # runner.run(suite)

