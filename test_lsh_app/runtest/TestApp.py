#-*- coding: utf-8 -*-
import os
import sys
import unittest



sys.path.append(os.path.dirname(os.getcwd()))
from test_lsh_app.base.AppBase import AppBase
from test_lsh_app.modules.login.LoginTest import LoginTest
from test_lsh_app.modules.register.RegisterTest import RegisterTest


class TestApp(unittest.TestCase):
    def setUp(self):
        appBase = AppBase("qa","")
        self.host = appBase.getHost()

    def tearDown(self):
        pass

    #测试登录
    def testLogin(self):
        appBase = AppBase("qa", "login")
        testCaseDoc = appBase.getTestCaseDoc()#获得登录testcase文件
        loginTest = LoginTest()
        loginTest.loginTest(self.host,testCaseDoc)

    #测试注册
    def testRegister(self):
        appBase = AppBase("qa", "register")
        testCaseDoc = appBase.getTestCaseDoc()#获得注册testcase文件
        registerTest = RegisterTest()
        registerTest.registerTest(self.host,testCaseDoc)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestApp("testLogin"))
    suite.addTest(TestApp("testRegister"))

    runner = unittest.TextTestRunner()
    runner.run(suite)