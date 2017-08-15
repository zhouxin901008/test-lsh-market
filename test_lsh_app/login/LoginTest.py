#-*- coding: utf-8 -*-
import time
import os
import requests

from xlutils.copy import copy
from test_lsh_app.base.TestCase import TestCase


class LoginTest():
    def loginTest(self,host):
        testCase = TestCase()
        excel = testCase.getAppTestCase("appcase.xls")
        sheet = excel.sheets()[0]
        nrows = sheet.nrows
        wb = copy(excel)
        ws = wb.get_sheet(0)
        amount = 0

        for i in range(1, nrows):
            url = sheet.cell(i, 3).value
            params = eval(sheet.cell(i, 4).value)
            result = requests.post(host + url , params = params )
            #print result.text
            responseTime = (result.elapsed.microseconds)/1000
            ws.write(i,7,responseTime)
            status = sheet.cell(i,5).value
            if result.json()['ret'] == status :
                print "第%d条用例pass" % i
                ws.write(i,6,"pass")
                amount+=1
            else :
                print "第%d条用例failure" % i
                ws.write(i,6,result.text)
        a = (amount / float(i))*100
        ws.write(i, 9, "%.2f" % a)
        print "case通过率为%.2f" % a + "%"
        resultTime = time.strftime('%Y-%m-%d_%H:%M:%S')
        wb.save(os.path.dirname(os.getcwd()) + '/appTestResults/appTestResult_' + resultTime + '.xls')
