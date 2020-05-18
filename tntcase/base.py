#coding:utf-8
import requests
import json

#使用类封装接口测试脚本
class RunMain:

    def send_post(self,url, data):
        headers = {
            'Cookie': "PASSPORT_DELIMONT_TOKEN=PBE_2.0_5cd1c6141c127d419f4bcae9f2648bb064aa81e86f244f82a92669d67e3796044af5f0da8db1445c74e3c06cdc28c404bdd458d908ecb547e94c6902cd995f3e987bbc9ea71dccb34a6383570d6858ceb3fe68bd31e7e77771ca1b436a5dd6fedeb7b7949c40c3efda970558e18e1063ea06aeaa2aea21aab4246fd4323f02e7ad4b4185afc3e8207133f7960cfaa275a1a190aa3c0630fb4ea218b94d87a7d4b54cf1e28cd3c812881be4cd3b8e56a371aad46cedaa25cdbfb22595be65480870bb2d7ae2a2254d79ab9843e8b894a7d2d9cb9a47b6772e732f9c53477aa931b01492da338abf7fb43fa86f7ce86cbb37e2d117ae0d4147ae2aa738576379469d2d53c08298f6d545a19adf1b17cf637f132fe6408ccbe94cc0df7207ded21bb674bea6839a7089c8e2f41be0320eb74b12ef8cc6269820e57a28026626c61cfaf97d96976eff0cc5857013faa8ef6c3e8e745bd2ad349673afb3851969ed1690e8d245bd44efe2",
            'Content-Type': "application/json",
            'X-shard': "shardid=2",
            'cache-control': "no-cache",
            'Postman-Token': "031e8a5f-ce53-4163-b873-bfe07bbd7b3c"
        }

        res = requests.post(url=url, data=data, headers=headers).json()
        return res  # 有返回值
        #return json.dumps(res,indent=2,sort_keys=True)
        #res = requests.post(url=url, data=data, headers=headers).text
        #return res

    def send_get(self,url, data):
        res = requests.get(url=url, data=data).json()
        return res  # 有返回值
        #return json.dumps(res,indent=2,sort_keys=True)


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

    #rm = RunMain(url1, 'POST', data1)#实例化RunMain，一个对象rm

    rm = RunMain()
    res = rm.run_main(url1, 'POST', data1)
    print res
    #print type(res)
