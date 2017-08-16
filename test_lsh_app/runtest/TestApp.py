#-*- coding: utf-8 -*-
import unittest
import os
import sys


sys.path.append(os.path.dirname(os.getcwd()))
from test_lsh_app.base.AppBase import AppBase
from test_lsh_app.login.LoginTest import LoginTest
from test_lsh_app.login.RegisterTest import RegisterTest

appBase = AppBase()
class TestApp(unittest.TestCase):
    def setUp(self):
        self.host = appBase.getHost()

    def tearDown(self):
        pass

    #测试登录
    def testLogin(self):
        self.testCaseDoc = appBase.getTestCaseDoc("login")#获得登录testcase文件
        loginTest = LoginTest()
        loginTest.loginTest(self.host,self.testCaseDoc)

    #测试注册
    def testRegister(self):
        self.testCaseDoc = appBase.getTestCaseDoc("register")#获得注册testcase文件
        registerTest = RegisterTest()
        registerTest.registerTest(self.host,self.testCaseDoc)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestApp("testLogin"))
    suite.addTest(TestApp("testRegister"))

    runner = unittest.TextTestRunner()
    runner.run(suite)