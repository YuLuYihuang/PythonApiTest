#!/usr/bin/env python
#coding:utf-8


name = "jiaohuang"
if name == "jiaohuang":
    print "yes"
else:
    print name


def changelist (mylist):
    mylist.append([1,2,3,4])
myli=[4,3,6,7]
changelist(myli)
print myli


class Student:
    count=0
    def __init__(self,name,age):
        self.name= name
        self.age = age
        Student.count+=1
    def dicount(self):
        print "Total Student :" %Student.count
    def diprit(self):
        print "name:", self.name,",age:",self.age

#创建 Employee 类的第一个对象
stu1 = Student('ZA',18)
stu2 = Student('UR',20)
stu1.diprit()
stu2.diprit()
print "Total Student %d" %Student.count

stu1.phone=18049050196