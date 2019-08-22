# coding=utf-8
from selenium.common.exceptions import NoSuchElementException
"""断言控件存在或不存在"""


'''控件属性:resource-id'''


def element_exist_id(driver, byid):
    try:
        driver.find_element_by_id(byid)
    except NoSuchElementException:
        print("没有找到控件:%s" % byid)
        driver.quit()
    else:
        return True


def element_noexist_id(driver, byid):
    try:
        driver.find_element_by_id(byid)
    except NoSuchElementException:
        return True
    else:
        print("断言控件不存在:%s失败" % byid)
        driver.quit()


"""控件属性:accessibility_id"""


def element_exist_acid(driver, acid):
    try:
        driver.find_element_by_accessibility_id(acid)
    except NoSuchElementException:
        print("没有找到控件:%s" % acid)
        driver.quit()
    else:
        return True


def element_noexist_acid(driver, acid):
    try:
        driver.find_element_by_accessibility_id(acid)
    except NoSuchElementException:
        return True
    else:
        print("断言控件不存在:%s失败" % acid)
        driver.quit()


'''控件属性:text'''


def element_exist_text(driver, text):
    try:
        driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % text)
    except NoSuchElementException:
        print("没有找到控件:%s" % text)
        driver.quit()
    else:
        return True


def element_noexist_text(driver, text):
    try:
        driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % text)
    except NoSuchElementException:
        return True
    else:
        print("断言控件不存在:%s失败" % text)
        driver.quit()


'''
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def Element_Exit(driver,locator):

    # 结合WebDriverWait和excepted_conditions判断
    # 每间隔1秒判断一次，30s超时，存在返回True，不存在返回False
    # :param locator:locator为元组类型，如("id","yoyo")
    # :return:bool值,True or False

    try:
        WebDriverWait(driver,30,1).until(EC.presence_of_element_located(locator))
        return True
    except:
        return False

if __name__ =='__main__':
    locl = ("id","yoyo") #元素1
    Element_Exit(driver,locl)
'''

