#-*- coding: UTF-8 -*-
# 暂停一秒输出。
#
# 程序分析：使用 time 模块的 sleep() 函数。
import time


def pr(content):
    print 'I am ...'
    time.sleep(2)
    print(content)

con = 'sleepy'
pr(con)