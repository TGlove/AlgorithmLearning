#-*- coding: UTF-8 -*-
# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
def calculating(n):
    result = []
    i=1
    while i<=n:
        i +=1
        if n%i==0:
            result.append(i)
            n = n/i
            i=1
    return result
l = calculating(90)
for i in range(len(l)):
    if i <= len(l)-2:
        print l[i],'*',
    else:
        print l[i],'=90'