#-*- coding: UTF-8 -*-
def storage(n,m):
    nlist = []
    mlist = []
    d = float(10000/float(n))
    f = float(10000/float(n+m))
    for i in range(n):
        nlist.append(i*d)
    for i in range(n+m):
        mlist.append(i*f)
    return nlist,mlist

def calculating(nlist,mlist):
    summove = 0.0
    for i in range(1,len(nlist)):
        minR = abs(nlist[1] - mlist[1])
        locateJ = 0
        for j in range(1,len(mlist)):
            compa = abs(nlist[i] - mlist[j])
            if compa <= minR:
                minR = compa
                locateJ = j
        summove +=minR
        del mlist[locateJ]
    return summove

if __name__ == '__main__':
    n,m = (x for x in raw_input('please input the n&m : ').split(' '))
    n = int(n)
    m = int(m)
    nlist,mlist = storage(n,m)
    result = calculating(nlist,mlist)
    print ('result = %0.4f'%(result))