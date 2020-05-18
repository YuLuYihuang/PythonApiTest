#coding:utf-8
import unittest

'''
class TestMethod(unittest.TestCase):#类继承unittest.TestCase
    #注解说明是类方法
    @classmethod
    def setUpClass(cls):
        print '类执行之前的方法'

    @classmethod
    def tearDownClass(cls):
        print '类执行之后的方法'


    #每次方法之前执行
    def setUp(self):
        print 'test--setUp'
    #每次方法之后执行
    def tearDown(self):
        print 'test--tearDown'
    def test_01(self):
        print '测试方法01'

    def test_02(self):
        print '测试方法02'

if __name__ == '__main__':
    unittest.main()
'''

from packagerunob.saaszh import RunMain
#类继承unittest.TestCase
class TestMethod(unittest.TestCase):

    def setUp(self):
        self.rm =RunMain()
    def test_01(self):
        url = 'https://stargate.ar.elenet.me/delimont.saas_tnt/employee/list'
        data = "{\"index\": 1,\"limit\": 10,\"total\": 10,\"pageName\": 3}\n"
        res = self.rm.run_main(url, 'POST', data)
        print res


    def test_02(self):
        url = 'https://stargate.ar.elenet.me/delimont.saas_tnt/employee/list'
        data = "{\"index\": 2,\"limit\": 10,\"total\": 10,\"pageName\": 3}\n"
        res = self.rm.run_main(url, 'POST', data)
        print res


if __name__ == '__main__':
	unittest.main()