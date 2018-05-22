# -*- coding: UTF-8 -*-
# 输入三个整数x,y,z，请把这三个数由小到大输出。
def sortion(list):
    for i in range(len(list)):
        minnum = list[i]
        j = i + 1
        for j in range(j, len(list)):
            if list[j] < minnum:
                list[i], list[j] = list[j], list[i]
                minnum = list[j]


def f_sort(arr):
    for i in range(1, len(arr)):
        min = arr[i]
        j = i
        while j > 0 and arr[j - 1] > min:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = min
    return arr


def sortthr(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a,b,c
print(sortthr(11,9,7))

# l.sort()
