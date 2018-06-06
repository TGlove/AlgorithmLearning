#-*- coding: UTF-8 -*-
# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
def cal(n,l,h):
    if n==0:
        return l
    else:
        l += h*0.5 + h
        h = h*0.5
        n -=1
        return cal(n,l,h)
print cal(10.0,0.0,100.0)
print (0.5)**10*100