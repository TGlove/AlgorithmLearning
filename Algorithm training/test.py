#-*- coding: UTF-8 -*-
import json
# x,lo=( x for x in raw_input().split(' '))
# print x,lo

# a,b=0,1
# while a<1000:
#     a,b=b,a+b
#     print(a,b)

# def a():
#     a=1
#     def b(x):
#         return x*6
#
#     return b(a)
# print(a())

# str1,a = (x for x in raw_input().split(' '))
# str1 = str(str1)
# a = str(a)
# print(a)
# print(str1)
# if str1 != 'R' and str1 !='L':
#     print 'yes'
# else:
#     print('no')
# L =[1,2,3,4,56,6]
# C = min(L)
# print(C)
# print range(5,3)
a = [0,1,2,3,4,5,6,7,8,9]
print a[:5:-1]
print a[6::-1]
a = a[5:]+a[:5]
print a
for i in range(1):
    print '1'
c = [4,6,8,2,8,24]
c.sort()
print(c)
f = 123456.314159265
print('%0.3f'%(f))
# print sum(a)
# print(a[-2])
# l = range(-5,0)
# #print(l)
# for i in range(1,5):
#     print(i)