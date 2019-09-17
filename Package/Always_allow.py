from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def always_allow(driver, number=5):
    """
    fuction:权限弹窗-始终允许
    :param driver: 传driver
    :param number: 判断弹窗次数，默认5次
    WebDriverWait里面0.5s判断一次是否有弹窗，1s超时
    """
    for i in range(number):
        loc = ("xpath", "//*[@text='始终允许']")
        try:
            e = WebDriverWait(driver, 1, 0.5).until(ec.presence_of_element_located(loc))
            e.click()
        except:
            pass
