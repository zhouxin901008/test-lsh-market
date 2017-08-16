#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

from test_lsh_app.base.AppBase import AppBase
from test_lsh_mis.base import MisLogin
from test_lsh_mis.base.MisBase import MisBase


class AppLogin:
    def marketLogin(self):
        base = AppBase()
        username = base.getUsername()
        password = base.getPassword()
        host = base.getHost()
        headers = eval(base.getHeaders())
        user = {'username': username, 'password': password}
        result = requests.post(host + '/user/info/login', params = user, headers = headers)
        if result.json()['ret'] == 1004 :
            #请求验证码
            requests.post(host + '/captcha/sms/sendVerifyUnusual?cellphone=' + username)
            misLogin = MisLogin()
            cookie = misLogin.misLogin()
            mis = MisBase()
            misHost = mis.getHost()
            headers = {'Cookie': cookie}
            result = requests.get(misHost + '/customermanage/user/searchverify?cellphone=' + username,headers = headers)
            resultContent = result.json()['content'][0]
            verifyCode = resultContent['verify_code']
            user = {'username': username, 'password': password, 'verify_code': verifyCode}
            result = requests.post(host + '/user/info/login', params = user, headers=headers)
        token = result.json()['content']['token']
        return token
