# coding=utf-8
"""生成随机值模块"""
import random
import string


'''获取固定长度随机字符串'''


def random_char(l):
    return ''.join(random.sample(string.ascii_lowercase, l))


'''生成随机指定位数的整数数字'''


def random_integer(l):
    return ''.join(str(i) for i in random.sample(range(0, 9), l))


'''获取固定长度随机字符串(字母+数字)'''


def random_char_number(l):
    return ''.join(random.sample(string.ascii_letters + string.digits, l))


'''
def random_char_number(l):
    n = random.randint(1, 4)     # 数字个数1~4之间
    c = l - n
    print(n, c)

    list_n = '1234567890'
    list_c = 'abcdefghigklmnopqrstuvwxyz'
    s = ""                # 保存随机码
    for x in range(n):
        s += random.choice(list_n)  # 随机数字
    for x in range(c):
        s += random.choice(list_c)  # 随机字符
    return s                       # 返回随机码
'''
