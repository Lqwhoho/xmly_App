# coding=utf-8
import time
import unittest
import sys
import HTMLTestRunner_cn
import os

sys.path.append("\Test_Case")

log_file = 'E:\\Python脚本\\APP\\ximalaya\Log'         # 定义手机日志所在文件
ListCase = 'E:\\Python脚本\\APP\\ximalaya\\Test_Case'  # 定义测试集所在文件夹

# pattern='Case_*.py' 规定测试集文件开头命名为Case，也可以是pattern='Case_.py'
# discover方法找到path 目录下所有文件到的测试用例组装到测试套件
# 因此可以直接通过run()方法执行discover
discover = unittest.defaultTestLoader.discover(ListCase, pattern='Case_*.py', top_level_dir=None)
runner = unittest.TextTestRunner
'''
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
'''


'''测试报告存放位置'''
Now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
FileName = 'E:\\Python脚本\\APP\\ximalaya\\Report\\'+Now+'Result.html'
FP = open(FileName, 'wb')

'''获取手机log日志，存放到电脑上'''
# logcat日志存放路径，文件名称为设备名称+当前时间+log.txt
device_name1 = "Mi_Note2" + '_'
device_name = "127.0.0.1:62025"
logname = log_file + "\\"+device_name1+Now+r"log.txt"
# logcat_cmd = "adb -s 127.0.0.1:62025 logcat  -v time >%s" % logname
package_name = "com.ximalaya.ting.android"
logcat_cmd = "adb -s %s logcat | find \"%s\" >%s" % (device_name, package_name, logname)
# 执行cmd命令
os.popen(logcat_cmd)


runner = HTMLTestRunner_cn.HTMLTestRunner(
    stream=FP,
    title=u'喜马拉雅FMAPP测试报告',
    description=u'用例执行情况:',
    verbosity=2,
    retry=0,    # 失败脚本重试次数
    save_last_try=True  # 如果save_last_try 为True ，一个用例仅显示最后一次测试的结果，如果save_last_try为False，则显示所有重试的结果
)

runner.run(discover)
