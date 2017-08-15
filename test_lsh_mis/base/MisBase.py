import ConfigParser
import os

cf = ConfigParser.ConfigParser()
cf.read(os.path.dirname(os.getcwd()) + "/conf/mis_config.ini")

class MisBase:
    def getEmail(self):
        email = cf.get("mis_user","email")
        return email

    def getPassword(self):
        password = cf.get("mis_user","password")
        return password

    def getHost(self):
        host = cf.get("mis_host","host")
        return host