from appium import webdriver
import time
import threading

desired_caps1 = {
    'platformName':  'Android',
    'deviceName': '127.0.0.1: 62025',
    'platformVersion': '5.1.1',
    'appPackage': 'com.ximalaya.ting.android',
    'appActivity': 'host.activity.WelComeActivity',
}

desired_caps2 = {
    'platformName':  'Android',
    'deviceName':  '127.0.0.1: 62007',
    'platformVersion':  '7.1.2',
    'appPackage':  'com.ximalaya.ting.android',
    'appActivity':  'host.activity.WelComeActivity',
}


def task1(): 
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps1)
    # 休眠20s等待页面加载完成
    time.sleep(20)
    print(driver.contexts)
    driver.quit()


def task2(): 
    driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_caps2)
    # 休眠20s等待页面加载完成
    time.sleep(20)
    print(driver.contexts)
    driver.quit()


def task3():
    driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_caps2)
    # 休眠20s等待页面加载完成
    time.sleep(20)
    print(driver.contexts)
    driver.quit()


threads = []
t1 = threading.Thread(target=task1)
threads.append(t1)      # 添加线程到线程列表

t2 = threading.Thread(target=task2)
threads.append(t2)

t3 = threading.Thread(target=task3)
threads.append(t3)

if __name__ == '__main__': 
    for t in threads: 
        t.start()
