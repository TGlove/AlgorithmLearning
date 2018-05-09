#-*- coding: UTF-8 -*-

def storage(n):
    timelist=[]
    for i in range(n):
        b,j = (x for x in raw_input('please input your time to allocate and execute task:').split(' '))
        b = int(b)
        j = int(j)
        timelist.append((b,j))
    return timelist

def calculating(list):
    sumB  = 0
    for i in range(len(list)):
        sumB += list[i][0]
    minJ = list[0][1]
    for i in range(len(list)):
        if list[i][1] <= minJ:
            minJ = list[i][1]
    maxJ = list[0][1]
    locateJ = 0
    for i in range(len(list)):
        if list[i][1] >= maxJ:
            locateJ = i
            maxJ = list[i][1]
    if (sumB+minJ-list[locateJ][0])<maxJ:
        return list[locateJ][0]+list[locateJ][1]
    else:
        return sumB+minJ
if __name__ == '__main__':
    n = int(raw_input('please input the number of your guard :'))
    timelist = storage(n)
    result = calculating(timelist)
    print('case # :',result)