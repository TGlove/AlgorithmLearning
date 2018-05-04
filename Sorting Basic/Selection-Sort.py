#-*- coding: UTF-8 -*-
import time

from SortTestHelper import SortTestHelper

# def testime(f):
#     start = time.clock()
#     f
#     end = time.clock()
#     c = end-start
#     print round(c,10)

# 直接排序
def selectionSort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                arr[i],arr[j] = arr[j],arr[i]
    return  arr

def selectionSort_1(arr):
    for i in range(len(arr)-1):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min=j
        arr[i],arr[min] = arr[min],arr[i]
    return arr

l = SortTestHelper.generateRandomArray(100,1,999)
s = time.clock()
print selectionSort(l)
print time.clock()-s

# testime(selectionSort(l))
#
# # a = '4.27618145548e-07'
# # b = float(a)
# # c= int(b)
# # print(c)