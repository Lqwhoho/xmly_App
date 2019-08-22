"""APP启动判断（弹出个性化选择界面和新手福利弹窗）"""
import time
from Package import *
from selenium.common.exceptions import NoSuchElementException
'''调用location.py文件的定位方法'''
we = location


def module_launch_judge(self):
    """判断APP启动后是否存在跳过按钮，,如果存在按钮则点击跳过，采用Try-Except方法"""
    time.sleep(15)

    def check_skipbtn():
        try:
            skipbtn = we.findText(self.driver, '跳过')
        except NoSuchElementException:
            print("No SkipBtn")
        else:
            skipbtn.click()
            self.add_img()
    check_skipbtn()
    time.sleep(8)

    '''判断是否弹出立即开始按钮'''
    def check_startbtn():
            try:
                startbtn = we.findText(self.driver, '立即开始')
            except NoSuchElementException:
                print("No StartBtn")
            else:
                startbtn.click()
                time.sleep(1)
                self.add_img()
                self.driver.back()
                self.add_img()
    check_startbtn()
    time.sleep(15)

    '''判断是否弹出新手福利窗口，如果存在弹窗则点击X，关闭弹窗'''
    def check_launch_closebtn():
        try:
            launch_closebtn = we.findId(self.driver, "com.ximalaya.ting.android:id/main_iv_close")
        except NoSuchElementException:
            print("No Launch_CloseBtn")
        else:
            launch_closebtn.click()
            self.add_img()
    check_launch_closebtn()
    time.sleep(3)

    time.sleep(3)
    '''此处的【返回】操作主要是防止首页出现弹窗'''
    self.driver.back()
