# -*- coding: UTF-8 -*-
import time

from SortTestHelper import SortTestHelper


# 插入排序

def insert_sort(array):
    # 循环的是第二个到最后（待摸的牌）
    for i in range(1, len(array)):
        # 待插入的数（摸上来的牌）
        min = array[i]
        # 已排好序的最右边一个元素（手里的牌的最右边）
        j = i - 1
        # 一只和排好的牌比较，排好的牌的牌的索引必须大于等于0
        # 比较过程中，如果手里的比摸上来的大，
        while j >= 0 and array[j] > min:
            # 那么手里的牌往右边移动一位，就是把j付给j+1
            array[j + 1] = array[j]
            # 换完以后在和下一张比较
            j -= 1
        # 找到了手里的牌比摸上来的牌小或等于的时候，就把摸上来的放到它右边
        array[j + 1] = min
    return array


def f_sort(arr):
    for i in range(1, len(arr)):
        min = arr[i]
        j = i
        while j > 0 and arr[j - 1] > min:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = min
    return arr


l = SortTestHelper.generateRandomArray(10, 1, 999)
s = time.clock()
print l
print f_sort(l)


# print time.clock()-s
# print insert_sort(l)
# print f_sort(l)


def a(arr):
    for i in range(1, len(arr)):
        min = arr[i]
        j = i
        while j > 0 and arr[j - 1] > min:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = min
    return arr


def b(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


print('\n\n')
l1 = SortTestHelper.generateRandomArray(10, 1, 999)
l2 = SortTestHelper.generateRandomArray(10, 1, 999)
print(l1)
print(a(l1))
print(l2)
print(b(l2))

