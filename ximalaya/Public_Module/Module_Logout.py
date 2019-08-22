"""退出登录操作模块"""
import time
from Package import *
'''调用location.py文件的定位方法'''
we = location

'''调用Swipe.py文件的定位方法'''
swipe = Swipe


def module_logout(self):
    swipe.swipeUp(self.driver)
    time.sleep(1)
    swipe.swipeUp(self.driver)
    time.sleep(2)

    # 退出登录
    we.findId(self.driver, "com.ximalaya.ting.android:id/main_tv_login").click()
    time.sleep(1)
    self.add_img()
    we.findId(self.driver, "com.ximalaya.ting.android:id/ok_btn").click()
    time.sleep(1)
    self.add_img()

    '''检查是否成功退出登录'''
    Judging_Element_Existence.element_noexist_text(self.driver, '退出登录')
