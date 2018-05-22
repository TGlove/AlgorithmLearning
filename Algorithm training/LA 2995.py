# -*- coding: UTF-8 -*-
def storage(n):
    result = []
    for i in range(n):
        s = raw_input('please input the view : ').split(' ')
        result.append(s)
    return result


def calculate(n, list):
    forward = []
    left = []
    backward = []
    right = []
    up = []
    down = []
    sumlack = 0
    for i in range(n):
        forward.append(list[i][0])
        left.append(list[i][1])
        backward.append(list[i][2])
        right.append(list[i][3])
        up.append(list[i][4])
        down.append(list[i][5])

    def countpoint(str):
        count = 0
        for i in str:
            if i == '.':
                count += 1
        return count

    # forward
    for i in range(n):
        sumlack = countpoint(forward[i]) * 3

    def locatecolumn(s):
        locate = -1
        for i in s:
            if i == '.':
                locate = i
        return locate

    def locaterow(l):
        locate = []
        for i in range(len(l)):
            if l[i].find('.') >= 0:
                locate.append(l[i].find('.'))
        return locate

    def locatecolumnlist(l):
        locate = []
        for i in range(len(l)):
            lo = locatecolumn(l[i])
            if lo != -1:
                locate.append(lo)
        return locate

    # left
    countj = 0
    for j in locatecolumnlist(left):
        for i in locatecolumnlist(forward):
            if i == j:
                sumlack += countpoint(left[i]) * 2
                countj += 1
                continue
    sumlack += (countpoint(left) - countj) * 3

    # top
    for i in locaterow(up):
        for j in locaterow(forward):
            if i == j:

