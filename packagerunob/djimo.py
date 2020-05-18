#coding:utf-8
#用自己定义的接口测试
import requests
import json

'''
#post测试
#定义一个字典data，放到requests
data={
    'username':'mushishi',
    'password':'123'
}
url1='http://127.0.0.1:8000/login/'
'''

'''
res = requests.post(url='http://127.0.0.1:8000/login/', data=data)
#打印res的内容
print res.text
#打印res的类型：字典
print type(res.json())
'''

'''
#封装一个方法sendpost
def sendpost(url,data):
    #re = requests.post(url=url, data=data).json()
    # print json.dumps(re)
    re = requests.post(url=url, data=data)
    # r.text是decode成Unicode
    print re.text
    #<type 'unicode'>类型是unicode
    print type(re.text)

    print re.json()
    # <type 'dict'>类型是字典
    print type(re.json())

    #字典转化成字符串
    print json.dumps(re.json())
    #<type 'str'>类型是字符串
    print type(json.dumps(re.json()))


sendpost(url1,data)
'''

'''
#http://127.0.0.1:8000/login?username=mushishi&mobile=123
#get测试
data={
    'username':'mushishi',
    'mobile':'123'
}
url2="http://127.0.0.1:8000/login?username=mushishi&mobile=123"

def sendget(url):
    re = requests.get(url).json()
    print json.dumps(re)
sendget(url2)
'''
