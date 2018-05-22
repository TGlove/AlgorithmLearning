#-*- coding: UTF-8 -*-
# 输入某年某月某日，判断这一天是这一年的第几天？

Mday = [0,31,28,31,30,31,30,31,31,30,31,30]
year,month,day = (x for x in raw_input('please input the date : ').split(' '))
year = int(year)
month = int(month)
day = int(day)
plist = []
sumday = 0
for i in range(len(Mday)):
    sumday += Mday[i]
    plist.append(sumday)
print('this day is the %dth day of the %d'%(plist[month-1]+day,year))