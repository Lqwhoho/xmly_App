# coding = utf-8


def swipeUp(driver, t=500, n=1):
    """向上滑动屏幕"""
    l = driver.get_window_size()
    x1 = l['width'] * 0.5     # x坐标
    y1 = l['height'] * 0.75   # 起始y坐标
    y2 = l['height'] * 0.25   # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


def swipeDown(driver, t=500, n=1):
    """向下滑动屏幕"""
    l = driver.get_window_size()
    x1 = l['width'] * 0.5          # x坐标
    y1 = l['height'] * 0.25        # 起始y坐标
    y2 = l['height'] * 0.75         # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


def swipLeft(driver, t=500, n=1):
    """向左滑动屏幕"""
    l = driver.get_window_size()
    x1 = l['width'] * 0.75
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.25
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)


def swipRight(driver, t=500, n=1):
    """向右滑动屏幕"""
    l = driver.get_window_size()
    x1 = l['width'] * 0.25
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)


def swipe_left(driver, sx, sy, ex, ey, t=500, n=1):
    """指定位置向左滑动"""
    a = round(sx/480, 2)
    b = round(sy/800, 2)
    c = round(ex/480, 2)
    d = round(ey/800, 2)
    x = driver.get_window_size()['width']
    print(x)
    y = driver.get_window_size()['height']
    print(y)
    x1 = int(x * a)
    y1 = int(y * b)
    x2 = int(x * c)
    y2 = int(y * d)
    for i in range(n):
        driver.swipe(x1, y1, x2, y2, t)
