# coding=utf-8
import time
from selenium.common.exceptions import NoSuchElementException

"""
本文件简易的封装定位单位元素和定位一组元素的方法
"""


'''定位单个元素封装'''


def findId(driver, id):
    f = driver.find_element_by_id(id)
    return f


def findName(driver, name):
    """对应的是text属性内容"""
    f = driver.find_element_by_name(name)
    return f


def findText(driver, Text):
    f = driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % Text)
    return f


def findClassName(driver, name):
    f = driver.find_element_by_class_name(name)
    return f


def findAcId(driver, text):
    """	content-desc的值"""
    f = driver.find_element_by_accessibility_id(text)
    return f


def findTagName(driver, name):
    f = driver.find_element_by_tag_name(name)
    return f


def findLinkText(driver, text):
    f = driver.find_element_by_link_text(text)
    return f


def findPLinkText(driver,text):
    f = driver.find_element_by_partial_link_text(text)
    return f


def findXpath(driver,xpath):
    f = driver.find_element_by_xpath(xpath)
    return f


def findCss(driver,css):
    f = driver.find_element_by_css_selector(css)
    return f


'''定义一组元素封装'''


def findsId(driver,id):
    f = driver.find_elements_by_id(id)
    return f


def findsName(driver,name):
    f = driver.find_elements_by_name(name)
    return f


def findsAcId(driver,text):
    f = driver.find_elements_by_accessibility_id(text)
    return f


def findsText(driver,Text):
    f = driver.find_elements_by_android_uiautomator('new UiSelector().text("%s")'%Text)
    return f


def findsClassName(driver,name):
    f = driver.find_elements_by_class_name(name)
    return f


def findsTagName(driver,name):
    f = driver.find_elements_by_tag_name(name)
    return f


def findsLinkText(driver,text):
    f = driver.find_elements_by_link_text(text)
    return f


def findsPLinkText(driver,text):
    f = driver.find_elements_by_partial_link_text(text)
    return f


def findsXpath(driver,xpath):
    f = driver.find_elements_by_xpath(xpath)
    return f


def findsCss(driver,css):
    f = driver.find_elements_by_css_selector(css)
    return f


"""
控件点击，可设置超时时间n,默认为15秒
设计思路：
当找不到控件的时候，使用循环语句，等待一秒后再次查找控件，
如果找到控件，则跳出循环，循环结束后还没找到控件，则打印未找到控件XXX的信息
用while循环，可以看到经过了多久才把控件加载出来
"""


def find_element_resource_id(driver, resource_id, n=15):
    while n > 0:
        try:
            s = driver.find_element_by_id(resource_id)
            break
        except NoSuchElementException:
            n = n - 1
            print(n)
            time.sleep(1)
    else:
        print('未找到控件%s' % resource_id)
        driver.quit()
    return s


def find_reid(driver, resource_id, n=15):
    for i in range(n):
        try:
            s = driver.find_element_by_id(resource_id)
            break
        except:
            pass
        time.sleep(1)
    else:
        print('未找到控件%s' % resource_id)
        driver.quit()
    return s


