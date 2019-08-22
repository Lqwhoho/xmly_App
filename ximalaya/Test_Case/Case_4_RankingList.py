# coding=utf-8
from Package import *
from Public_Module import *
import time
import unittest
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'''调用location.py文件的定位方法'''
we = location

'''调用Swipe.py文件的定位方法'''
swipe = Swipe


class RankingList(unittest.TestCase):
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

    def test_ranking_list(self):
        u"""喜马拉雅FMAPP【排行榜】功能"""
        # 调用公共模块---首次启动APP会出现个性化定制选择界面以及新手福利弹窗
        Module_Launch_Judge.module_launch_judge(self)

        playbtn = we.findId(self.driver, 'com.ximalaya.ting.android:id/host_bottom_hot_lay')
        playbtns = playbtn.find_elements_by_class_name('android.widget.FrameLayout')
        playbtns[2].click()
        time.sleep(2)
        self.add_img()

        we.findText(self.driver, 'VIP 热听榜').click()
        time.sleep(1)
        self.add_img()
        layoutbtn = we.findId(self.driver, 'android:id/list')
        layoutbtns = layoutbtn.find_elements_by_class_name('android.widget.RelativeLayout')
        layoutbtns[0].click()
        time.sleep(8)
        self.add_img()
        Relative_Coordinate_Click.relative_coordinate_click(self.driver, 123, 768)
        time.sleep(3)

        # WebDriverWait(self.driver,60,0.5).until(lambda x: x.find_element_by_accessibility_id
        # ("Web View").is_displayed(),message='页面加载失败')

        nb = 0
        while nb < 10:
            Relative_Coordinate_Click.relative_coordinate_click(self.driver, 96, 136)
            time.sleep(7)
            if Element_Existence_IF.element_exist_resource_id(self.driver,
                                                              'com.ximalaya.ting.android:id/main_login_with_pwd'):
                print('已成功跳转到登录界面')
                break
            else:
                nb = nb + 1
                if nb % 3 == 0:
                    self.driver.back()
                    time.sleep(2)
                    Relative_Coordinate_Click.relative_coordinate_click(self.driver, 123, 768)
                    time.sleep(2)
        else:
            print("页面加载失败")

        Judging_Element_Existence.element_exist_text(self.driver, '密码登录')
        we.findId(self.driver, "com.ximalaya.ting.android:id/main_login_with_pwd").click()
        self.add_img()
        we.findId(self.driver, "com.ximalaya.ting.android:id/main_username").send_keys('15918860373')
        self.add_img()
        we.findId(self.driver, "com.ximalaya.ting.android:id/main_password").send_keys('QQ45266347')
        self.add_img()
        we.findId(self.driver, "com.ximalaya.ting.android:id/main_login").click()
        Wait_Element.wait_element(self.driver, 60, By.ID, 'com.ximalaya.ting.android:id/comp_actionbar_up', "页面加载失败")
        self.add_img()

        '''
        Relative_Coordinate_Click.relative_coordinate_click(self.driver,123,768)
        time.sleep(8)
        self.add_img()
        Judging_Element_Existence.Element_exist_Text(self.driver,'确认支付')
        '''

        self.driver.back()
        time.sleep(1)
        self.add_img()
        self.driver.back()
        time.sleep(6)
        self.add_img()
        we.findText(self.driver, '主播榜').click()
        time.sleep(1)
        self.add_img()
        layoutbtn = we.findId(self.driver, 'android:id/list')
        layoutbtns = layoutbtn.find_elements_by_class_name('android.widget.RelativeLayout')
        layoutbtns[0].click()
        time.sleep(5)
        self.add_img()
        anchorname = we.findId(self.driver, 'com.ximalaya.ting.android:id/main_tv_nickname').text

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
        we.findAcId(self.driver, '取消关注').click()
        self.add_img()

        # Judging_Toast.find_toast(self.driver,'关注成功')

        self.driver.back()
        time.sleep(1)
        self.add_img()
        self.driver.back()
        time.sleep(1)
        self.add_img()
        # 此处的【返回】操作主要是防止首页出现弹窗
        self.driver.back()

        accountbtn = we.findId(self.driver, 'com.ximalaya.ting.android:id/host_bottom_hot_lay')
        accountbtns = accountbtn.find_elements_by_class_name('android.widget.FrameLayout')
        accountbtns[4].click()
        time.sleep(2)
        self.add_img()

        we.findId(self.driver, 'com.ximalaya.ting.android:id/main_my_space_my_attention').click()
        time.sleep(2)
        Wait_Element.wait_element(self.driver, 30, By.ID, 'com.ximalaya.ting.android:id/main_btn_follow', '【关注】页面加载失败')
        self.add_img()
        Judging_Element_Existence.element_exist_text(self.driver, anchorname)
        we.findText(self.driver, anchorname).click()
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
    suite = unittest.TestLoader().loadTestsFromTestCase(RankingList)
    unittest.TextTestRunner(verbosity=2).run(suite)


