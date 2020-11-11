# coding:utf-8
import unittest
import json
import HTMLTestRunner_PY3
# from mock import mock
from demo import RunMain
from mock_demo import mock_test


class TestMethod(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()

    def test_03(self):
        url = 'http://172.16.10.221/user/modifyPwd'
        data = {
            'timestamp': '1507034803124',
            'userId': '976022',
            'oldPassword': '123456',
            'password': '123456',
            'debug': 'true'
        }
        # self.run.run_main = mock.Mock(return_value=data)
        res = mock_test(self.run.run_main, data, url, "POST", data)
        # res = self.run.run_main(url,'POST',data)
        print(res)
        self.assertEqual(res['errorCode'], 200, "测试失败")
        print("这是第一个case")

    # @unittest.skip('test_02')
    def test_02(self):
        url = 'http://172.16.10.221/user/modifyPwd'
        data = {
            'timestamp': '1507034803124',
            'userId': '976022',
            'oldPassword': '123456',
            'password': '123456',
            'debug': 'true'}

        res = self.run.run_main(url, 'POST', data)
        self.assertEqual(res['errorCode'], 200, "测试失败")
        print("这是第二个case")
# mock


if __name__ == '__main__':
    unittest.main()
