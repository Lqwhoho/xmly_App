# coding=utf-8
import time
import unittest
import sys
import HTMLTestRunner_cn
import os
import re

sys.path.append("\Test_Case")

log_file = 'E:\\Python脚本\\APP\\ximalaya\Log'
ListCase = 'E:\\Python脚本\\APP\\ximalaya\\Test_Case'


def creatsuitel():
    testunit = unittest.TestSuite()     # 定义一个单元测试容器
    discover = unittest.defaultTestLoader.discover(
                                                    ListCase,
                                                    pattern='Case_*.py',
                                                    top_level_dir=None
                                                  )

    # 将Discover方法筛选出来的用例，循环添加到测试套件中
    for Test_Suite in discover:
        for Test_Case in Test_Suite:
            testunit.addTest(Test_Case)
            print(testunit)
    return testunit


AllTestNames = creatsuitel()

'''测试报告存放位置'''
Now = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime(time.time()))
FileName = 'E:\\Python脚本\\APP\\ximalaya\\Report\\'+Now+'Result.html'
FP = open(FileName, 'wb')

'''获取手机log日志，存放到电脑上'''
logname = log_file + "\\"+Now+r"log.txt"
logcat_cmd = "adb -s 127.0.0.1:62025 logcat  -v time >%s" % logname
os.popen(logcat_cmd)


runner = HTMLTestRunner_cn.HTMLTestRunner(
    stream=FP,
    title=u'喜马拉雅FMAPP测试报告',
    description=u'用例执行情况:',
    verbosity=2,
    retry=0,    # 失败脚本重试次数
    save_last_try=True  # 如果save_last_try 为True ，一个用例仅显示最后一次测试的结果，如果save_last_try为False，则显示所有重试的结果
)

runner.run(AllTestNames)
