# coding:utf-8
import unittest
import json
# import HTMLTestRunner
import HTMLTestRunnerCN
from mock import mock

from demo import RunMain


# 类继承unittest.TestCase

class TestMethod(unittest.TestCase):

    def setUp(self):
        self.rm = RunMain()

    # 获取雇员列表
    def test_01(self):
        url = 'https://stargate.ar.elenet.me/delimont.saas_tnt/employee/list'
        data = "{\"index\": 1,\"limit\": 10,\"total\": 10,\"pageName\": 3}\n"
        #把data作为返回值
        mock_data = mock.Mock(return_value=data)
        self.rm.run_main = mock_data
        res = self.rm.run_main(url, 'POST', data)
        print res
        #self.assertEqual(res['code'], '200', '测试失败')
        print '这是第一个测试'



    def test_04(self):
        url = 'https://stargate.ar.elenet.me/delimont.saas_tnt/employee/get'
        data = "{\"employeeId\": 571}"
        res = self.rm.run_main(url, 'POST', data)
        self.assertEqual(res['code'], '200', '测试失败')
        print '这是第二个测试'


if __name__ == '__main__':
    unittest.main()
