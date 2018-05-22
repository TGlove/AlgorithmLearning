#-*- coding: UTF-8 -*-
# 斐波那契数列（Fibonacci sequence），又称黄金分割数列，
# 指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……
def series(n):
    if n==1:
        return [1]
    if n==2:
        return [1]
    fbs = [1,1]
    for i in range(n-2):
        fbs.append(fbs[-1]+fbs[-2])
    return fbs
def fb(n):
    if n==1 or n==2:
        return 1
    return fb(n-1)+fb(n-2)
def fb3(n):
    a,b = 1,1
    for i in range(n-2):
        a,b = b,a+b
    return b
print(series(10))
print(fb(10))
print(fb(10))