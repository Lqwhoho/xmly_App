# conding:utf-8
import os


class keyevent():
    '''常用的keyevent事件'''
    KEYCODE_HOME = 3            #home键
    KEYCODE_MENU = 82           #menu键
    KEYCODE_BACK = 4            #back键
    KEYCODE_POWER = 26          #power键
    KEYCODE_DPAD_UP = 19        #向上
    KEYCODE_DPAD_DOWN = 20      #向下
    KEYCODE_DPAD_LEFT = 21      #向左
    KEYCODE_DPAD_RIGHT = 22     #向右
    KEYCODE_NOTIFICATION = 83   #解锁


def adbKeyEvent(keyname = keyevent.KEYCODE_BACK):
    '''执行adb keyevent事件 参数从keyevent类里面关联'''
    adb = 'adb shell input keyevent %s' % keyname
    os.system(adb)

if __name__ == "__main__":
    #执行back键操作
    adbKeyEvent(keyevent.KEYCODE_BACK)