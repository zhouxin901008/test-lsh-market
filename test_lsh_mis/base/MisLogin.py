import requests

from test_lsh_mis.base.MisBase import MisBase


class MisLogin():
    def misLogin(self):
        base = MisBase()
        host = base.getHost()
        email = base.getEmail()
        password = base.getPassword()
        params = {'email': email, 'pwd': password}
        result = requests.post(host + '/account/user/checklogin', params = params)
        cookies = result.headers.get('Set-Cookie')
        return cookies
