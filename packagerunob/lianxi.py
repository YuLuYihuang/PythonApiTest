#!/usr/bin/env python
#coding:utf-8

'''
import time;  # 引入time模块

ticks = time.time()
print "当前时间戳为:", ticks

name = "jiaohuang"
if name == "jiaohuang":
   print "yes"
else:
   print name

na = 10
if na == 1:
   print 'a'
elif na == 2:
   print 'b'
elif na == 3:
   print 'c'
elif na > 20:
   print 'd'
else:            #条件都不满足
   print 'e'


#判断n3在10~20或者25~30之间
n3 = 32
if (n3 > 10 and n3 <20 ) or (n3 > 25 and n3 < 30):
   print u"n3在这个区间之内"
else:
   print u"n3不在这个区间，找错了"

num = 0
while (num <= 10):
   print "num is ", num
   num = num + 1
print num          #num是加1后的结果
print "------"

nu = 0
while nu < 10 :
   nu += 1
   if nu % 2 > 0 : #判断nu除以2是否有余数，有余数是奇数就跳过次循环
      continue
   else :
      print nu    #偶数就输出nu
print "-----------"

nu = 0
while 1:  #循环条件为1必定成立
   print nu  #输出0，1，2，3，4，5
   nu += 1
   if nu > 5 :  #当nu>5的时候就停止循环
      break
#print nu  #nu是6

import random
ans = int (random.uniform(1,10))
num = int (input('猜猜数字：'))
#第一次猜，两种情况，猜对了或者没猜对
if num == ans :    #猜对了，等于ans
   print (u"厉害了，第一次就猜对了")
while num != ans2:   #猜错了，不等于ans
   if num > ans :
      print (u"cai大了")
      num = int (input('再猜一次：'))
   if num < ans :
      print (u"cai小了")
      num = int (input('再猜一次：'))
   if num == ans :
      print (u"bigon")
      break;

for x in 'apple' :  #字符串‘apple’，遍历字符串’apple‘
   print u"apple的字母有：", x

xs = ['xa','xb','xc','xd']  #xs是数组，遍历数组中的元素
for x in xs :
   print u"xs中有：", x


xs = ['cat','dog','monkey']
#len函数是数组的长度，range函数是返回一个序列的数组，表示数组下标
for index in range(len(xs)) :  #index是数组下标，xs[index]是遍历数组
   print u"xs中有：", xs[index]

str1 = "wel"
str2 = "com"
print u"str1和str2拼接后是：", str1 + str2
print str2 * 2


lista = ['list1', 'list2', 'list3']
list0 = ['cat', 'dog', 'monkey']
print ("lista[0]:", lista[0])
print ("list0[1:3]:", list0[1:3])
lista[1] = 'listb';
print(u"lista修改", lista);
list0.append('fish');
print(u"list0添加元素", list0);
del(list0[0]);
print(u"list0删除列表第一个元素：", list0);
#listl = lista + list0;
print("合并list：", lista+list0);


tup1 = ('sh',10,23,22)
tup2 = 'x','y','z'
print("tup1的第一个元素：", tup1[0]);
print("tup2的第二个到第三个元素：", tup2[1:3]);
print("tup1+tup2的元素：", tup1+tup2);
del (tup2)
print("tup2删除之后：")
print("tup1的长度：", len(tup1));
tup3=(100,)*4
print("输出tup3：", tup3)
for x in tup1:print (x)


dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
a = {'name': 'zhangsan', 'hingh': 'm', 'class': 'student'}
print("a['name']：",a['name'])
print("dict['Age']：",dict['Age'])
dict['Name'] = 'liming'  #修改name
print("dict['Name']:", dict['Name'])
dict['school'] = 'abc' #添加key，school
print(dict)  #输出dict
del dict['school']  #删除school
print(dict)
dict.clear()
print("清空后的：",dict)
a.keys()
a.values()
print("返回a的所有键：", a.keys())
print("返回a的所有值：", a.values())
for x in dict :
    print("循环输出：", dict{})

list=[1,2,4,3,3,4,3]
print(list.count(3)) #list.count()统计次数
3 in list


#斐波那契数列
#两个元素的总和确定了下一个数
a, b = 0, 1
while (b < 100):
    print(b)  #print(b, end=',') #end以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
    a , b = b , a+b  #先计算右边的计算式，在把右边的值同时赋值给左边

#输出变量值
i= 245*342
print('i的值是：', i)
print(5==6)

age = int (input("请输入狗的年龄："))
print('')
if(age < 0 ):
    print('在搞笑')
elif(age == 1):
    print('相当于14')
elif(age == 2):
    print('相当于22')
elif(age > 2):
    print('相当于', 22+(age-2)*5)0
else: #输入0时，else是以上条件都不满足，只满足else的条件
    print('请来一条狗')
input('点击enter退出')



if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句


num = int (input('请输入一个数字：'))
if (num < 50 and num > 0):
    if (num > 40):    #先是小范围的判断，距离50最近的范围40
        print('num>40')
    elif (num > 30):
        print('num>30')
    else:
        print('0<num<30')
elif (num == 50):
    print('num = 50')
elif (num == 100):
    print('num=100')
elif (num == 0):
    print('num=0')
else:
    if (num > 80):
        print('num>80')
    elif (num > 70):
        print('num>70')
    else:
        print('num>50')


#以下实例使用了 while 来计算 1 到 100 的总和
n = 100 #n是用于格式字符串的，可以随时进行变化
sum = 0
cun = 1
while cun <= n: #cun小于
    sum = sum + cun
    cun += 1
print("1到 %d 的和是：%d" % (n,sum))

var = 1
while var == 1:
    num = int (input('请输入数字：'))
    print('输入的数字是：', num)

#while中的else，循环使用else
count = 0
while count < 5:
    print(count,'小于5')
    count += 1
else:
    print("大于5")


list = [1,2,3,4,5]
it = iter(list)
for x in it:
    print (x,end=' ')


import sys  #引入sys模块
list = [1,2,3,4,5]
it = iter(list)  #创建迭代器对象
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()


#构造一个迭代器
class Mynumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
myclass = Mynumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))


#StopIteration异常用于标识迭代的完成，防止出现无限循环的情况，
# 在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
class Mynumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclass = Mynumbers()
myiter = iter(myclass)
for x in myiter:
    print (x)


def hello():
    print('hello')
hello()

def print_huang(name):
    print('welcome', name)
print_huang('huangjiao')

def area(height, width):
    return (height*width)
h = 1
w = 2
print('height=',h,'width=',w, 'area=',area(h,w))

a = int(input('请输入一个数字：'))
b=1
def change(a):
    b=a
    print '交换之后b=',b #2.7不带括号
change(a)


def printme(str):#方法声明
    print(str) #调用print方法
    return
printme('第一次调用你')
print 'hello!'

listl=['tr','tt','yt']
for x in listl:
    #printme(x)
    if x == 'tt' :
        printme(x)
    elif x == 'tr' :
        print 'erro'
    else :
        print x


import time;
times = time.time()
print times


def chang(a):
    a = 2
b=3
chang(b)
print b

#import MySQL


def changelist (mylist):
    mylist.append([1,2,3,4])
myli=[4,3,6,7]
changelist(myli)
print myli


prstr = raw_input("请输入：")
print '输入的内容是:',prstr
'''


from packagerunob.runob1 import runob1
from packagerunob.runob2 import runob2
runob1()
runob2()
