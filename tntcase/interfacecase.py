# coding:utf-8
import unittest
import json
# import HTMLTestRunner
import HTMLTestRunnerCN
from mock import mock
from base import RunMain


# 类继承unittest.TestCase
class TestMethod(unittest.TestCase):
    def setUp(self):
        self.rm = RunMain()

    # 获取雇员列表
    def test_01(self):
        url = 'https://stargate.ar.elenet.me/delimont.saas_tnt/employee/list'
        data = "{\"index\": 1,\"limit\": 10,\"total\": 10,\"pageName\": 3}\n"
        # 把data作为返回值
        # mock_data = mock.Mock(return_value=data)
        # self.rm.run_main = mock_data

        res = self.rm.run_main(url, 'POST', data)
        print res
        # print type(res)

        # if res['code'] == '200':
        # print '测试通过'
        # else:
        # print '测试失败'

        self.assertEqual(res['code'], '200', '测试失败')
        self.assertTrue(True)
        print '这是第一个测试'

    ''' 
    def test_02(self):
        url = 'https://stargate.ar.elenet.me/delimont.saas_tnt/employee/list'
        data = "{\"index\": 2,\"limit\": 10,\"total\": 10,\"pageName\": 3}\n"
        res = self.rm.run_main(url, 'POST', data)

        #if res['code'] == '200':
            #print '测试通过'
        #else:
            #print '测试失败'

        self.assertEqual(res['code'],'200','测试失败')
    '''

    '''
    #添加初始雇员
    def test_03(self):
        url = 'https://stargate.ar.elenet.me/delimont.saas_tnt/employee/addInitEmployee'
        data2 = "{\"employee\": {\"tenantId\": 100,\"name\": \"黄wu金\",\"account\": \"jinwuhang@ele.me\",\"gender\": -1,\"email\": \"jinwuhuang@ele.me\",\"phone\": \"13618346522\"}}\n"
        res = self.rm.run_main(url,'POST',data2)
        self.assertEqual(res['code'],'200','测试失败')
    '''

    # 获取雇员信息根据雇员id
    # @unittest.skip('test_04')
    def test_04(self):
        url = 'https://stargate.ar.elenet.me/delimont.saas_tnt/employee/get'
        data = "{\"employeeId\": 571}"
        res = self.rm.run_main(url, 'POST', data)
        self.assertEqual(res['code'], '200', '测试失败')
        print '这是第二个测试'

    '''
    #获取当前登录用户的权限
    def test_05(self):
        url='https://stargate.ar.elenet.me/delimont.saas_tnt/auth/permission'
        res = self.rm.run_main(url,'POST')
        print res
    '''


if __name__ == '__main__':
    # 定义文件发现
    filepath = "../report/htmlreport.html"
    # 资源流，读写的形式打开
    fp = file(filepath, 'wb')
    # 生成容器
    suite = unittest.TestSuite()
    # 添加方法
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_04'))
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='this is first report')
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='this is first report')
    runner.run(suite)
    # unittest.TextTestRunner().run(suite)
