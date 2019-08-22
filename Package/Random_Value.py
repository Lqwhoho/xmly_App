# coding=utf-8
"""生成随机值模块"""
import random
import string


'''获取固定长度随机字符串'''


def random_char(l):
    return ''.join(random.sample
                   (string.ascii_lowercase, l))


'''获取固定长度随机字符串(字母+数字)'''


def random_char_number(l):
    random_value = ''.join(random.sample(string.ascii_letters + string.digits, l))
    return random_value
