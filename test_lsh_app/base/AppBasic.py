#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

from test_lsh_app.base.AppBase import AppBase
from test_lsh_mis.base.MisBasic import MisBasic


class AppBasic:
    def __init__(self,environment):
        self.environment = environment

    def getToken(self):
        base = AppBase()
        username = base.getUsername()
        password = base.getPassword()
        host = base.getHost(self.environment)
        headers = eval(base.getHeaders())
        params = {'username': username, 'password': password}
        result = requests.post(host + '/user/info/login', params = params)
        if result.json()['ret'] == 1004 :
            #请求验证码
            requests.post(host + '/captcha/sms/sendVerifyUnusual?cellphone=' + username)
            misBasic = MisBasic()
            verifyCode = misBasic.getVerifyCode(username)
            user = {'username': username, 'password': password, 'verify_code': verifyCode}
            result = requests.post(host + '/user/info/login', params = user, headers=headers)
        token = result.json()['content']['token']
        return token
