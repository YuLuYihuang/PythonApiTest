#coding:utf-8
import requests
import json

'''
#/delimont.saas_tnt/employee/list接口
url1= "https://stargate.ar.elenet.me/delimont.saas_tnt/employee/list"
data1 ="{\"index\": 1,\"limit\": 10,\"total\": 10,\"pageName\": 3}\n"
#/delimont.saas_tnt/employee/addInitEmployee接口
url2="https://stargate.ar.elenet.me/delimont.saas_tnt/employee/addInitEmployee"
data2 = "{\"employee\": {\"tenantId\": 100,\"name\": \"黄wu金\",\"account\": \"jinwuhang@ele.me\",\"gender\": -1,\"email\": \"jinwuhuang@ele.me\",\"phone\": \"13618346522\"}}\n"


def sendpost(url,data):
    headers = {
        'Cookie': "PASSPORT_DELIMONT_TOKEN=PBE_2.0_5cd1c6141c127d41e288b71b457273d0b19d8756dc99f5cd6a68c7b7a5d58dfc9cab018be714ad5ee44cb95f5095f317f766c461a02d7c1337e76fb0c79e764f43206a39bf2d49ac5270fdb745ad1ecd22c23d4675e934a825369421715ae84555ae90d0e6c731d77ed13c9c30b33081d1bbfa6e68a75f9901d393eaeb1df7777eaa6d8fbc1578436086c60ed328483b8d2a44812a7789cacc95f96bf91f999e3cb14bceec8292aa0194b68207d95fb341ccc8bda99110724fae1ee8b03826d6abd9342fb98e73f5b99efedcd28f918149b2be6bb5237c811fbd7feccf156aac5bff6c5619f1c1647aa3db240b43fe58e223edb54d69863f24c56fd037d1e49d3e5824b4dcfaa8abd81d46eca6b1dc9b31d2195d5892d1fcd9dd7efc1446197683d78e6429f066071f4896ab5fcf203392b1cdfbac7e9f88453e2c477375a7dcbd1ffe39b20fef2b1d75cf62973d905866508daaff355eb879741321fc43354a41c41e8328b33cf3",
        'Content-Type': "application/json",
        'X-shard': "shardid=2",
        'cache-control': "no-cache",
        'Postman-Token': "031e8a5f-ce53-4163-b873-bfe07bbd7b3c"
    }
    response = requests.request("POST", url, data=data, headers=headers)
    #print response.text
    print json.dumps(response.json(),indent=2,sort_keys=True)
sendpost(url1,data1)
sendpost(url2,data2)


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

'''
url1= "https://stargate.ar.elenet.me/delimont.saas_tnt/employee/list"
data1 ="{\"index\": 1,\"limit\": 10,\"total\": 10,\"pageName\": 3}\n"

url2="http://127.0.0.1:8000/login?username=mushishi&mobile=123"

#把send_post和send_get方法封装起来只调一个方法

def send_post(url,data):
    headers = {
        'Cookie': "PASSPORT_DELIMONT_TOKEN=PBE_2.0_5cd1c6141c127d41e288b71b457273d0b19d8756dc99f5cd6a68c7b7a5d58dfc9cab018be714ad5ee44cb95f5095f317f766c461a02d7c1337e76fb0c79e764f43206a39bf2d49ac5270fdb745ad1ecd22c23d4675e934a825369421715ae84555ae90d0e6c731d77ed13c9c30b33081d1bbfa6e68a75f9901d393eaeb1df7777eaa6d8fbc1578436086c60ed328483b8d2a44812a7789cacc95f96bf91f999e3cb14bceec8292aa0194b68207d95fb341ccc8bda99110724fae1ee8b03826d6abd9342fb98e73f5b99efedcd28f918149b2be6bb5237c811fbd7feccf156aac5bff6c5619f1c1647aa3db240b43fe58e223edb54d69863f24c56fd037d1e49d3e5824b4dcfaa8abd81d46eca6b1dc9b31d2195d5892d1fcd9dd7efc1446197683d78e6429f066071f4896ab5fcf203392b1cdfbac7e9f88453e2c477375a7dcbd1ffe39b20fef2b1d75cf62973d905866508daaff355eb879741321fc43354a41c41e8328b33cf3",
        'Content-Type': "application/json",
        'X-shard': "shardid=2",
        'cache-control': "no-cache",
        'Postman-Token': "031e8a5f-ce53-4163-b873-bfe07bbd7b3c"
    }
    resq = requests.post(url=url,data=data,headers=headers).json()
    return json.dumps(resq,indent=2,sort_keys=True)#有返回值


def send_get(url,data):
    res = requests.get(url=url,data=data).json()
    return json.dumps(res,indent=2,sort_keys=True)#有返回值

#定义一个run_main方法，data可以为空，data参数必须放在最后
def run_main(url,method,data=None):
    #定义一个res，初始为空
    res = None
    if method == 'POST':
        #执行完赋值给res
        res = send_post(url,data)
    else:
        # 执行完赋值给res
        res = send_get(url,data)
    return res#返回res
print run_main(url1,'POST',data1)
'''



#使用类封装接口测试脚本
class RunMain:
    # 构造函数，传要传的参数
    def __init__(self,url,method,data=None):
        self.resq = self.run_main(url,method,data)#当前的类

    def send_post(self,url, data):
        headers = {
            'Cookie': "PASSPORT_DELIMONT_TOKEN=PBE_2.0_5cd1c6141c127d41e288b71b457273d0b19d8756dc99f5cd6a68c7b7a5d58dfc9cab018be714ad5ee44cb95f5095f317f766c461a02d7c1337e76fb0c79e764f43206a39bf2d49ac5270fdb745ad1ecd22c23d4675e934a825369421715ae84555ae90d0e6c731d77ed13c9c30b33081d1bbfa6e68a75f9901d393eaeb1df7777eaa6d8fbc1578436086c60ed328483b8d2a44812a7789cacc95f96bf91f999e3cb14bceec8292aa0194b68207d95fb341ccc8bda99110724fae1ee8b03826d6abd9342fb98e73f5b99efedcd28f918149b2be6bb5237c811fbd7feccf156aac5bff6c5619f1c1647aa3db240b43fe58e223edb54d69863f24c56fd037d1e49d3e5824b4dcfaa8abd81d46eca6b1dc9b31d2195d5892d1fcd9dd7efc1446197683d78e6429f066071f4896ab5fcf203392b1cdfbac7e9f88453e2c477375a7dcbd1ffe39b20fef2b1d75cf62973d905866508daaff355eb879741321fc43354a41c41e8328b33cf3",
            'Content-Type': "application/json",
            'X-shard': "shardid=2",
            'cache-control': "no-cache",
            'Postman-Token': "031e8a5f-ce53-4163-b873-bfe07bbd7b3c"
        }

        res = requests.post(url=url, data=data, headers=headers).json()
        return json.dumps(res, indent=2, sort_keys=True)  # 有返回值
        #res = requests.post(url=url, data=data, headers=headers).text
        #return res

    def send_get(self,url, data):
        res = requests.get(url=url, data=data).json()
        return json.dumps(res, indent=2, sort_keys=True)  # 有返回值

    # 封装一个函数，run_main方法，data可以为空，data参数必须放在最后
    def run_main(self,url, method, data=None):
        # 定义一个res，初始为空
        res = None
        if method == 'POST':
            # 执行完赋值给res
            res = self.send_post(url, data)
        else:
            # 执行完赋值给res
            res = self.send_get(url, data)
        return res  # 返回res

if __name__ == '__main__':#把上面的三个方法都到类里面，运行的时候if判断

    url1 = "https://stargate.ar.elenet.me/delimont.saas_tnt/employee/list"
    data1 = "{\"index\": 1,\"limit\": 10,\"total\": 10,\"pageName\": 3}\n"

    url2 = "http://127.0.0.1:8000/login?username=mushishi&mobile=123"

    rm = RunMain(url1, 'POST', data1)#实例化RunMain，一个对象rm
    print rm.resq



