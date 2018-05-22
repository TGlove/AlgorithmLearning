#-*- coding: UTF-8 -*-
# 暂停一秒输出，并格式化当前时间。
import datetime,time

Time = datetime.datetime.now()
time.sleep(1)
print Time.strftime("%Y-%m-%d %H:%M:%S")