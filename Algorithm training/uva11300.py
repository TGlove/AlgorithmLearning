# -*- coding: UTF-8 -*-


def storage(n):
    numlist = []
    for i in range(n):
        num = int(raw_input('please input the number of each persons coins : '))
        numlist.append(num)
    return numlist


def calculating(n, list):
    if sum(list) % n != 0:
        return 'no answer'
    clist = []
    M = sum(list)/n
    for i in range(len(list)-1):
        sumA = 0
        for j in range(i+1):
            sumA += list[j]
        Cn = sumA - (i+1)*M
        clist.append(Cn)
    cclist = clist
    clist.append(M-list[-1])
    clist.sort()
    if n%2 == 0:
        locat = (n/2)-1
        x1 = clist[locat]
    else:
        locat = n/2
        x1 = clist[locat]
    result = abs(x1)
    for i in range(len(cclist)):
        result += abs(x1 - cclist[i])
    return result

if __name__ == '__main__':
    n = int(raw_input('please input the number of people : '))
    list = storage(n)
    result = calculating(n, list)
    print('the minimum rotated coins is :', result)
