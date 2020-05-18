#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
import MySQLdb

#import mysql.connector

# 打开数据库连接
#db = MySQLdb.connect("localhost", "root", "75LU32!!yi15", "scrapyDB", charset='utf8')
coon = MySQLdb.connect(host="localhost", prot=3306,user="root",passwd="75LU32!!yi15",db='mysql')
cursor = coon.cursor()

cursor.execute("SELECT VERSION()")
print "Database version : %s " % data
db.close()


from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='75LU32!!yi15',
                                 host='localhost',
                                 database='scrapyDB')
cnx.close()


from mysql.connector import (connection)
cnx = connection.MySQLConnection(user='root', password='75LU32!!yi15',
                                 host='localhost',
                                 database='scrapyDB')
cnx.close()


import MySQLdb
db = MySQLdb.connect(user='root', password='75LU32!!yi15',
                                 host='localhost',
                                 database='scrapyDB')
'''


#连接数据库
from mysql.connector import (connection)
#打开数据库连接
cnx = connection.MySQLConnection(user='root', password='75LU32!!yi15',
                                 host='localhost',
                                 database='scrapyDB')
# 使用cursor()方法获取操作游标
cursor = cnx.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print "Database version : %s " % data

# 关闭数据库连接
cnx.close()


'''
#数据库插入操作
from mysql.connector import (connection)
#打开数据库连接
cnx = connection.MySQLConnection(user='root', password='75LU32!!yi15',
                                 host='localhost',
                                 database='scrapyDB')
# 使用cursor()方法获取操作游标
cursor = cnx.cursor()
# SQL 插入语句
sql = """INSERT INTO weather(date,
         week, weather)
         VALUES ('23','星期三','雨天')"""
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    cursor.commit()
except:
    # 发生错误时回滚
    cnx.rollback()
# 关闭数据库连接
cursor.close()
'''


#数据库查询语句
from mysql.connector import (connection)
#打开数据库连接
cnx = connection.MySQLConnection(user='root', password='75LU32!!yi15',
                                 host='localhost',
                                 database='scrapyDB')
# 使用cursor()方法获取操作游标
cursor = cnx.cursor()
#sql查询语句
sql = "SELECT * FROM weather"
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      date = row[0]
      week = row[1]
      weather = row[2]
      # 打印结果
      print"date=%s,week=%s,weather=%s" % \
             (date,week,weather )
except:
   print "Error: unable to fecth data"

# 关闭数据库连接
cursor.close()


import pymysql
db = pymysql.connect(user='root',password='75LU32!!yi15',
                                 host='localhost',
                                 database='scrapyDB',charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()



#SQL 插入语句
#sql1 = """INSERT INTO weather(date,
 #        week, weather)
  #       VALUES ('23','星期五','雨天')"""


sql2="SELECT * FROM weather"
try:
    # 执行sql语句
    cursor.execute(sql2)
    # 提交到数据库执行
    db.commit()
    cursor.execute(sql2)
    results = cursor.fetchmany(5)
    for row in results:
        print row
        #print type(row)
except:
    db.rollback()
    db.close()


'''
from mysql.connector import (connection)
#打开数据库连接
cnx = connection.MySQLConnection(user='root', password='75LU32!!yi15',
                                 host='localhost',
                                 database='scrapyDB',charset='utf8')
# 使用cursor()方法获取操作游标
cursor = cnx.cursor()
sql2="SELECT * FROM weather"
try:
    # 执行sql语句
    cursor.execute(sql2)
    # 提交到数据库执行
    cnx.commit()
    cursor.execute(sql2)
    results = cursor.fetchmany(5)
    for row in results:
        print row
        #print type(row)
except:
    cnx.rollback()
    cnx.close()
'''