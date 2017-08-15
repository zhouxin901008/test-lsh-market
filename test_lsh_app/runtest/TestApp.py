#-*- coding: utf-8 -*-
import unittest
import os
import sys

sys.path.append(os.path.dirname(os.getcwd()))
from test_lsh_app.base.AppBase import AppBase
from test_lsh_app.login.LoginTest import LoginTest


class TestApp(unittest.TestCase):
    def setUp(self):
        appBase = AppBase()
        self.host = appBase.getHost()

    def tearDown(self):
        pass

    def testLogin(self):
        loginTest = LoginTest()
        loginTest.loginTest(self.host)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestApp("testLogin"))

    runner = unittest.TextTestRunner()
    runner.run(suite)