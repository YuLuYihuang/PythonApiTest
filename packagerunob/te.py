#!/usr/bin/env python
#coding:utf-8

'''
import time;  # 引入time模块
import calendar
ticks = time.time()
print "当前时间戳为:", ticks
localtime = time.localtime(time.time())
print "本地时间是：",localtime
# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

cal=calendar.month(2019,1)
print "以下输出1月份的日历:"
print cal
'''
import time

print time.time();
print time.localtime();
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime());


import calendar
print calendar.month(2019,3);

print time.strftime("%Y-%m-%d %H:%M:%S %B %A",time.localtime());
print time.localtime();