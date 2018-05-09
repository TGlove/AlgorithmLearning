# -*- coding: UTF-8 -*-

def storage(n, m):
    caliberlist = []
    capacitylist = []
    for a in range(n):
        caliber = int(raw_input('please input the caliber of the devil dragon :'))
        caliberlist.append(caliber)
    for b in range(m):
        capacity = int(raw_input('please input the capacity of the cavalier :'))
        capacitylist.append(capacity)

    for i in range(1,len(caliberlist)):
        mincali = caliberlist[i]
        j = i
        while j > 0 and caliberlist[j - 1] > mincali:
            caliberlist[j] = caliberlist[j - 1]
            j -= 1
        caliberlist[j] = mincali

    for i in range(1,len(capacitylist)):
        mincapa = capacitylist[i]
        j = i
        while j > 0 and capacitylist[j - 1] > mincapa:
            capacitylist[j] = capacitylist[j - 1]
            j -= 1
            capacitylist[j] = mincali
    return caliberlist, capacitylist


def calculating(n, m, caliberlist, capacitylist):
    maxcaliber = int(max(caliberlist))
    maxcapacity = int(max(capacitylist))
    moneylist = []
    if m < n or maxcaliber > maxcapacity or sum(caliberlist) > sum(capacitylist):
        return 'Loowater is doomed!'
    for i in range(len(caliberlist)):
        for j in range(len(capacitylist)):
            if caliberlist[i] <= capacitylist[j]:
                moneylist.append(capacitylist[j])
                del capacitylist[j]
                break
            else:
                return 'Loowater is doomed!'
    return moneylist

if __name__ == '__main__':
    n,m=(x for x in raw_input('please input the number of dragon and cavalier :').split(' '))
    n = int(n)
    m = int(m)
    caliberlist,capacitylist = storage(n,m)
    # print caliberlist
    # print capacitylist
    moneylist = calculating(n, m, caliberlist, capacitylist)
    if moneylist == 'Loowater is doomed!':
        print moneylist
    else:
        print('the minimum cost is :',sum(moneylist))