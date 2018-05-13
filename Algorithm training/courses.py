#-*- coding: UTF-8 -*-
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def contin_miunes(a,b):
    while(a!=b):
        if a<b:
            b=b-a
        else:
            a=a-b
    return a
print gcd(98,63)
print contin_miunes(98,63)