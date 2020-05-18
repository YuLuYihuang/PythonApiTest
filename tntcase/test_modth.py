#coding:utf-8
import unittest
import json
import HTMLTestRunnerCN
from demo import RunMain
#类继承unittest.TestCase
class TestMethod(unittest.TestCase):
    def setUp(self):
        self.rm =RunMain()
    #获取雇员列表
    def test_01(self):
        url = 'https://stargate.ar.elenet.me/delimont.saas_tnt/employee/list'
        data = "{\"index\": 1,\"limit\": 10,\"total\": 10,\"pageName\": 3}\n"
        res = self.rm.run_main(url, 'POST', data)
        print json.dumps(res).decode('unicode-escape')
        self.assertEqual(res['code'].encode('utf8'),'200','测试失败')
    #添加初始雇员
    def test_02(self):
        url = 'https://stargate.ar.elenet.me/delimont.saas_tnt/employee/addInitEmployee'
        data = "{\"employee\": {\"tenantId\": 100,\"name\": \"黄就品\",\"account\": \"jiupinhang@ele.me\",\"gender\": -1,\"email\": \"jiupinhuang@ele.me\",\"phone\": \"18765639876\"}}\n"
        res = self.rm.run_main(url,'POST',data)
        print json.dumps(res).decode('unicode-escape')
        self.assertEqual(res['code'].encode('utf8'),'200')
    #获取雇员信息根据雇员id
    def test_03(self):
        url = 'https://stargate.ar.elenet.me/delimont.saas_tnt/employee/get'
        data = "{\"employeeId\": 571}"
        res = self.rm.run_main(url,'POST',data)
        print json.dumps(res).decode('unicode-escape')
        self.assertEqual(res['code'], '200')
if __name__ == '__main__':
    #定义文件发现
    filepath = "../report/htmlreport.html"
    #资源流，读写的形式打开
    fp = file(filepath,'wb')
    #生成容器
    suite = unittest.TestSuite()
    #添加方法
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
    suite.addTest(TestMethod('test_03'))
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp,title='this is first report')
    runner.run(suite)
