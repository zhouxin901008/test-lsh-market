import requests

from test_lsh_mis.base.MisBase import MisBase


class MisBasic():
    def __init__(self,environment):
        self.environment = environment

    def getCookie(self):
        base = MisBase()
        host = base.getHost(self.environment)
        email = base.getEmail()
        password = base.getPassword()
        params = {'email': email, 'pwd': password}
        result = requests.post(host + '/account/user/checklogin', params = params)
        cookies = result.headers.get('Set-Cookie')
        return cookies

    def getVerifyCode(self,username):
        mis = MisBase()
        misHost = mis.getHost(self.environment)
        headers = {'Cookie': self.getCookie()}
        result = requests.get(misHost + '/customermanage/user/searchverify?cellphone=' + username, headers=headers)
        resultContent = result.json()['content'][0]
        verifyCode = resultContent['verify_code']
        return verifyCode
