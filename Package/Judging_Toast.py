# coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def find_toast(driver, message, timeout=15, poll_frequency=0.5):
    """
    :param driver:driver
    :param message:消息提示框内容
    :param timeout:最大超时时间，默认30s
    :param poll_frequency:间隔查询时间，默认0.5s查询一次
    """
    try:
        # toast = ("xpath", ".//*[contains(@text,'%s')]" % message)
        toast = (By.XPATH, "//*[contains(@text, " + "'" + message + "'" + ")]")
        WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast))
        # print(element.text)
        # element.text == Toast
        return True
    except NoSuchElementException:
        print("未找到控件:%s" % message)
        driver.quit()


'''
IF逻辑判断toast，如果存在执行某一操作，不存在执行别的操作
def find_toast(driver,message,timeout=5,poll_frequency=0.5):
    try:
        toast = ("xpath", ".//*[contains(@text,'%s')]" %message)
        WebDriverWait(driver,timeout,poll_frequency).until(EC.presence_of_element_located(toast))
    except:
        return True
        else:
        we.findId(self.driver,'com.ximalaya.ting.android.main.application:id/main_lottie_like').click()
find_toast(self.driver,'已取消喜欢')
'''
