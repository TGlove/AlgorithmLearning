# -*- coding: UTF-8 -*-

def storage(L, T, n):
    xlist = []
    for i in range(n):
        x, location = (x for x in raw_input('Please input x,direction:').split(' '))
        x = int(x)
        location = str(location)
        if x > L:
            print('invalid input!  x must less and equal to L')
            x, location = raw_input('redo it:')
        if location != 'R' and location != 'L':
            print('invalid input! location must be R or L')
            x, location = raw_input('redo it:')
        if T * 1 + x > 2 * L:
            xlist.append(['Fell off',0,i])
        else:
            xlist.append([x, location,i])
    for i in range(1, len(xlist)):
        minL = xlist[i]
        j = i
        while j > 0 and xlist[j - 1][0] > minL[0]:
            xlist[j] = xlist[j - 1]
            j -= 1
        xlist[j] = minL

    return xlist


def calculating(L, T, n, list):
    if T == 0:
        return list

    def minT():
        minlist = []
        for i in range(1, len(list)):
            if list[i][1] == 'L':
                for j in list[i::-1]:
                    if j[1] == 'R':
                        distance = list[i][0] - j[0]
                        minlist.append(distance)
                        break
        if len(minlist) > 0:
            c = min(minlist)
            result = float(c) / 2
        else:
            result = 0.0
        return result

    minNUM = minT()

    if minNUM >= T:
        if minNUM == T:
            for i in range(len(list)):
                if list[i][1] == 'R':
                    if (list[i][0] + minNUM) > L:
                        list[i] = ['Fell off',0,list[i][2]]
                    else:
                        list[i][0] = list[i][0] + minNUM
                if list[i][1] == 'L':
                    if (list[i][0] - minNUM) < 0:
                        list[i] = ['Fell off',0,list[i][2]]
                    else:
                        list[i][0] = list[i][0] - minNUM
            for i in range(len(list)):
                for j in range(i + 1, len(list)):
                    if list[i][0] == list[j][0]:
                        list[i] = ['Turning',0,list[i][2]]
                        list[j] = ['Turning',0,list[j][2]]
            return list

        else:
            for i in range(len(list)):
                if list[i][1] == 'R':
                    list[i][0] = list[i][0] + minNUM
                if list[i][1] == 'L':
                    list[i][0] = list[i][0] - minNUM
            return list
    else:
        if minNUM == 0:
            for i in range(len(list)):
                if list[i][1] == 'R':
                    if (list[i][0] + T) > L:
                        list[i] = ['Fell off',0,list[i][2]]
                    else:
                        list[i][0] = list[i][0] + T
                if list[i][1] == 'L':
                    if (list[i][0] - T) < 0:
                        list[i] = ['Fell off',0,list[i][2]]
                    else:
                        list[i][0] = list[i][0] - T
            T = 0
            return list
        else:
            for i in range(len(list)):
                if list[i][1] == 'R':
                    list[i][0] = list[i][0] + minNUM
                if list[i][1] == 'L':
                    list[i][0] = list[i][0] - minNUM
            for i in range(len(list)):
                for j in range(i + 1, len(list)):
                    if list[i][0] == list[j][0]:
                        list[i][1] = 'L'
                        list[j][1] = 'R'
            return calculating(L, T - minNUM, n, list)


if __name__ == '__main__':
    L, T, n = (x for x in raw_input('Length of the crabstick,time,total number of the ant: ').split(' '))
    L = int(L)
    T = int(T)
    n = int(n)
    list = storage(L, T, n)
    def k(l):
        return l[2]
    finallist = calculating(L, T, n, list)
    finallist.sort(key=k)

    print('#case 1 ')
    for ant in finallist:
        if ant[0] == 'Fell off':
            print(ant[0])
        elif ant[0] == 'Turning':
            print (ant[0])
        else:
            print ant[0], ' ', ant[1]
