# -*- coding: UTF-8 -*-
# 题目：输出指定格式的日期。
#
# 程序分析：使用 datetime 模块。
import datetime

now = datetime.datetime.now().strftime('%Y-%m-%d')
print now

# create date obj
ctime = datetime.date(1999, 6, 21)
print (ctime.strftime('%d/%m/%Y'))

# time calcute
ctime = ctime + datetime.timedelta(days=1)
print(ctime)

# replacetime
ctime = ctime.replace(ctime.year + 1)
print(ctime)
