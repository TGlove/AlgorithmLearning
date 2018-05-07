#-*- coding: UTF-8 -*-
from SortTestHelper import SortTestHelper

# 冒泡排序
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

# def Insert_Sort(arr):
#     for i in range(1, len(arr)):
#         for j in range(i):
#             if arr[i] < arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]
#     return arr

# l = SortTestHelper.generateRandomArray(10,1,999)
# print(l)
# print(Insert_Sort(l))

l1 = SortTestHelper.generateRandomArray(10,1,999)
print(l1)
print(bubble_sort(l1))

print(range(len(l1)))