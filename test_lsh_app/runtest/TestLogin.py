#-*- coding: utf-8 -*-
import requests
import sys,os
import unittest
import time

from test_lsh_app.login.LoginTest import LoginTest

sys.path.append(os.path.dirname(os.getcwd()))
from xlutils.copy import copy
from test_lsh_app.base.AppBase import AppBase
from test_lsh_app.base.TestCase import TestCase



class TestLogin(unittest.TestCase):
    def setUp(self):
        appBase = AppBase()
        self.host = appBase.getHost()
        #self.headers = eval(appBase.getHeaders())

    def tearDown(self):
        pass

    def testLogin(self):
        loginTest = LoginTest()
        loginTest.loginTest(self.host)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestLogin("testLogin"))

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)