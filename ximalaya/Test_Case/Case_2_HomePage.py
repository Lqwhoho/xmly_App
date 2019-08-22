# coding = utf - 8
import time
import unittest
import os
import sys

sys.path.append('..')   # 表示导入当前文件的上层目录到搜素路径中
sys.path.append('/Public_Module')   # 绝对路径

from Package import *
from Public_Module import *


'''调用location.py文件的定位方法'''
we = location

'''调用Swipe.py文件的定位方法'''
swipe = Swipe


class HomePage(unittest.TestCase):
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

        """如果APP还在运行，则执行driver.quit操作"""
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

    def test_homepage(self):
        u"""喜马拉雅FMAPP【首页】功能"""
        # 调用公共模块---首次启动APP会出现个性化定制选择界面以及新手福利弹窗
        Module_Launch_Judge.module_launch_judge(self)

        '''调用公共模块---登录'''
        Module_Login.module_login(self)

        self.driver.back()
        homepagebtn = we.findId(self.driver, 'com.ximalaya.ting.android:id/host_bottom_hot_lay')
        homepagebtns = homepagebtn.find_elements_by_class_name('android.widget.FrameLayout')
        homepagebtns[0].click()
        time.sleep(2)
        self.add_img()

        # 此处的【返回】操作主要是防止首页出现弹窗
        self.driver.back()

        we.findId(self.driver, "com.ximalaya.ting.android:id/main_tv_search").click()
        time.sleep(2)
        self.add_img()
        we.findId(self.driver, "com.ximalaya.ting.android:id/search_search_et").send_keys(u'三国演义[经典')
        time.sleep(2)
        self.add_img()
        we.findId(self.driver, "com.ximalaya.ting.android:id/search_search_et").click()
        time.sleep(5)
        self.add_img()

        '''
        we.findXpath(self.driver, "//android.widget.TextView[@content-desc='下载']/../../android.widget.TextView"
                                  "[contains(@text,'三国演义[经典评书]')]").click()
        '''
        we.findText(self.driver, '三国演义[经典评书]').click()
        time.sleep(3)
        self.add_img()
        we.findText(self.driver, '三国演义001回-鞭督邮刘备走代州').click()
        time.sleep(2)
        self.add_img()
        '''判断是否存在引导按钮'''
        def check_guidebtn():
            try:
                guidebtn = we.findText(self.driver, '三国演义001回-鞭督邮刘备走代州')
            except:
                return True
            else:
                guidebtn.click()
                self.add_img()
        check_guidebtn()
        time.sleep(10)

        we.findId(self.driver, "com.ximalaya.ting.android:id/main_iv_like").click()
        time.sleep(2)
        self.add_img()

        '''判断是否存在收藏按钮'''
        def check_likebtn():
            try:
                likebtn = we.findId(self.driver, "com.ximalaya.ting.android:id/main_iv_like")
            except:
                return True
            else:
                likebtn.click()
                self.add_img()
                time.sleep(2)
        check_likebtn()

        we.findId(self.driver, "com.ximalaya.ting.android:id/main_iv_like").click()
        self.add_img()
        '''
        判断取消喜欢后是否弹出[已取消喜欢]提示
        Judging_Toast.Find_Toast(self.driver,'已取消喜欢')
        '''
        time.sleep(4)
        we.findId(self.driver, "com.ximalaya.ting.android:id/main_tv_quora_input").click()
        time.sleep(2)
        self.add_img()
        we.findId(self.driver, "com.ximalaya.ting.android:id/et_input").click()
        time.sleep(1)
        we.findId(self.driver, "com.ximalaya.ting.android:id/et_input").send_keys('喜欢')
        time.sleep(2)
        self.add_img()
        # 需要点击的控件(相对坐标),,点击【发表评论】按钮
        # Relative_Coordinate_Click.relative_coordinate_click(self.driver, 427, 768)
        we.findId(self.driver, 'com.ximalaya.ting.android:id/tv_send').click()
        time.sleep(5)
        self.add_img()
        '''判断评论之后，是否弹出评价APP弹窗'''
        def check_evaluateclosebtn():
            try:
                evaluateclosebtn = we.findId(self.driver, "com.ximalaya.ting.android:id/close")
            except:
                pass
            else:
                evaluateclosebtn.click()
                self.add_img()
        check_evaluateclosebtn()
        we.findAcId(self.driver, "更多").click()
        time.sleep(4)
        self.add_img()
        Swipe.swipe_left(self.driver, 442, 686, 105, 686)
        # self.driver.swipe(442, 686, 105, 686, 400)
        time.sleep(2)
        Relative_Coordinate_Click.relative_coordinate_click(self.driver, 276, 689)
        time.sleep(2)
        Judging_Element_Existence.element_exist_text(self.driver, '播放历史')
        self.add_img()

        Judging_Element_Existence.element_exist_text(self.driver, '三国演义001回-鞭督邮刘备走代州')

        we.findAcId(self.driver, "清空").click()
        time.sleep(2)
        self.add_img()
        we.findId(self.driver, "com.ximalaya.ting.android:id/ok_btn").click()
        time.sleep(1)
        self.add_img()
        Judging_Element_Existence.element_exist_text(self.driver, '没有收听过节目')

        self.driver.back()
        time.sleep(1)
        self.add_img()
        we.findAcId(self.driver, "返回").click()
        self.add_img()
        self.driver.back()
        time.sleep(2)
        self.add_img()
        self.driver.back()
        time.sleep(1)
        self.add_img()

        '''此处的【返回】操作主要是防止首页出现弹窗'''
        self.driver.back()

        we.findId(self.driver, "com.ximalaya.ting.android:id/main_lottie_view_edit_tab").click()
        time.sleep(1)
        self.add_img()
        we.findText(self.driver, '编辑').click()
        time.sleep(1)
        self.add_img()
        we.findText(self.driver, '小说').click()
        time.sleep(1)
        self.add_img()
        we.findText(self.driver, '完成').click()
        self.add_img()
        # '''判断是否弹出[分类已保存]提示'''
        # Judging_Toast.find_toast(self.driver,'分类已保存')
        time.sleep(1)

        self.driver.back()
        time.sleep(2)
        self.add_img()

        we.findId(self.driver, "com.ximalaya.ting.android:id/main_lottie_view_edit_tab").click()
        time.sleep(1)
        self.add_img()
        we.findText(self.driver, '编辑').click()
        time.sleep(1)
        self.add_img()
        we.findText(self.driver, '小说').click()
        time.sleep(1)
        self.add_img()
        we.findText(self.driver, '完成').click()
        time.sleep(1)
        self.add_img()
        self.driver.back()
        time.sleep(2)
        self.add_img()
        Judging_Element_Existence.element_exist_text(self.driver, '小说')

        we.findId(self.driver, "com.ximalaya.ting.android:id/main_lottie_view_edit_tab").click()
        time.sleep(2)
        self.add_img()
        we.findText(self.driver, '广州').click()
        time.sleep(5)
        self.add_img()

        Judging_Element_Existence.element_exist_text(self.driver, '广州')
        time.sleep(2)
        self.driver.back()
        time.sleep(1)
        self.add_img()
        self.driver.back()
        time.sleep(1)
        self.add_img()

        down_button = we.findId(self.driver, 'com.ximalaya.ting.android:id/host_bottom_hot_lay')
        down_buttons = down_button.find_elements_by_class_name('android.widget.FrameLayout')
        down_buttons[4].click()
        time.sleep(2)
        self.add_img()

        we.findAcId(self.driver, '设置').click()
        time.sleep(2)
        self.add_img()
        '''调用公共模块---退出登录'''
        Module_Logout.module_logout(self)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HomePage)
    unittest.TextTestRunner(verbosity=2).run(suite)
