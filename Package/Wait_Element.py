# coding=utf-8
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

'''智能等待函数，等待界面出现某元素才执行接下来的操作，否则程序退出'''


def wait_element(driver, time, element_by, element, msg):
    """
    等待元素出现
    :param driver: driver
    :param time: 超时等待时间
    :param element_by: 元素类型
    :param element: 元素关键字
    :param msg: 输出信息
    :return:

    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"

    find_element(By.ID,'id')
    find_element(By.NAME,'name')
    find_element(By.CLASS_NAME,'classname')
    find_element(By.TAG_NAME,'tagname')
    find_element(By.LINK_TEXT,'linktext')
    find_element(By.PARTIAL_LINK_TEXT,'partiallinktext')
    find_element(By.XPATH,'xpath')
    find_element(By.CSS_SELECTOR,'cssselector')
    """

    '''
     try:
        WebDriverWait(driver,timeout).until(EC.presence_of_element_located(element_by,element))
        return True
    except NoSuchElementException:
        print(msg)
        driver.quit()   
    '''

    WebDriverWait(driver, time).until(expected_conditions.presence_of_element_located((element_by, element)), msg)
