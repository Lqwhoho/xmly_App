# coding=utf-8
"""
此模块使用相对坐标点击方法，适用于录制的手机分辨率为480*800
相对坐标 = (绝对坐标 / 录制脚本手机分辨率) * 当前手机分辨率
"""


def relative_coordinate_click(driver, x, y):
    a = round(x/480, 2)  # 保留两位小数
    b = round(y/800, 2)
    x1 = driver.get_window_size()['width']
    y1 = driver.get_window_size()['height']
    x2 = int(a * x1)
    y2 = int(b * y1)
    driver.tap([(x2, y2)])




