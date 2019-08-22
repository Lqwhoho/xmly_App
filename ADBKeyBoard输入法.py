# coding:utf-8
import os


def adbSendText(text):
    '''执行adb ADBKeyBoard事件输入中文'''
    adb1 = 'adb shell ime set com.android.adbkeyboard/.AdbIME'
    os.system(adb1)
    adb2 = "adb shell am broadcast -a ADB_INPUT_TEXT --es msg '%s'" % text
    os.system(adb2)

if __name__ == "__main__":
    #执行back键操作
    adbSendText("海贼王")