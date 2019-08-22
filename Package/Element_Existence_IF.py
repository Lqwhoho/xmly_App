# coding=utf-8
"""
适用于IF逻辑，判断某个元素是否存在
如果不存在，程序不退出
场景介绍：当出现界面加载缓慢且需要循环点击某个控件（或坐标）才能进行接下里的操作
"""


def element_exist_resource_id(driver, rid):
    s = driver.find_elements_by_id(rid)  # resource-id
    if len(s) == 0:
        print("控件未找到:%s" % rid)
        return False
    elif len(s) == 1:
        return True
    else:
        print("找到%s个控件：%s" % (len(s), rid))
        return False


"""
if逻辑;如果存在某个控件，就执行点击控件的操作
"""


def if_element_exist_resource_id_click(driver, rid):
    s = driver.find_elements_by_id(rid)  # resource-id
    if len(s) == 0:
        print("控件未找到:%s" % rid)
        return False
    elif len(s) == 1:
        s.click()
    else:
        print("找到%s个控件：%s" % (len(s), rid))
        return False
