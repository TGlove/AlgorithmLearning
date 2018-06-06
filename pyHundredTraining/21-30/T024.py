#-*- coding: UTF-8 -*-
# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
a = [2,3,5,8,13,21]
b = [1,2,3,5,8,13]

# a = 2.0
# b = 1.0
# s = 0
# for n in range(1,21):
#     s += a / b
#     t = a
#     a = a + b
#     b = t
# print s

# a = 2.0
# b = 1.0
# l = []
# l.append(a / b)
# for n in range(1,20):
#     b,a = a,a + b
#     l.append(a / b)
# print reduce(lambda x,y: x + y,l)

def seriesa(n):
    l=[2,3]
    if n == 1:
        return l[0]
    elif n==2:
        return l[1]
    else:
        for i in range(2,n):
            l.append(l[i-1]+l[i-2])
        return l[n-1]
def seriesb(n):
    l=[1,2]
    if n == 1:
        return l[0]
    elif n==2:
        return l[1]
    else:
        for i in range(2,n):
            l.append(l[i-1]+l[i-2])
        return l[n-1]

def calculate(n):
    sum = 0
    for i in range(n):
        a = seriesa(i+1)
        b = seriesb(i+1)
        sum += float(a)/float(b)
    return sum
print calculate(20)