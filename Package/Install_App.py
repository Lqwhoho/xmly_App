#!C:\Users\liuquanwei\AppData\Local\Programs\Python\Python37
# -*- coding:utf-8 -*-
# @Author：liuquanwei
# @Time：2019/10/18 08:55
# @Filename：Reissue_application.py
# @Desc：====================================================
"""
通过adb命令进行卸载APP的操作
"""
# @Software：PyCharm
import os
import logging


def uninstall_app(device_name, app_name):
    """
    卸载APP
    :return:
    """
    result_file = os.popen('adb -s %s uninstall %s' % (device_name, app_name))
    result = result_file.read()
    if "Success" in result:
        logging.info("应用卸载成功")
        print("应用卸载成功")
    elif "Failure" in result:
        logging.info("应用卸载失败")
        print("应用卸载失败")
