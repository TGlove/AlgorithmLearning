#-*- coding: UTF-8 -*-
# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
def f(n):
    l =[]
    i = 1
    while i<n:
        if n%i==0:
            l.append(i)
        i += 1
    if sum(l)==n:
        return l
    return 'None'

def prin(f,n):
    l = f(n)
    if l!='None':
        print '%d='%(n),
        for i in range(len(l)-1):
            print l[i],'+',
        print l[len(l)-1]
# prin(f,6)

for i in range(4,1001):
    prin(f,i)