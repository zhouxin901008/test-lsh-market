import ConfigParser
import os

cf = ConfigParser.ConfigParser()
cf.read(os.path.dirname(os.getcwd()) + "/conf/app_config.ini")

class AppBase:
    def getUsername(self):
        username = cf.get("app_user","username")
        return username

    def getPassword(self):
        password = cf.get("app_user","password")
        return password

    def getHeaders(self):
        headers = cf.get("app_headers","headers")
        return headers

    def getHost(self):
        host = cf.get("app_host","host")
        return host