import requests
import random
from .config import Config
from datetime import datetime as dt
from .talk import  Talk


class KoeTomo(Talk):
    def __init__(self):
        self.headers = {
            'User-Agent': Config.USER_AGENT
        }
        self.request = requests.Session()
        Talk.__init__(self)

    def __str__(self):
        return f"""-----------------------------------------------------
name : {self.name}
passwd : {self.passwd}
user id : {self.user_id}
mail : {self.mail}
token : {self.token}
-----------------------------------------------------"""

    def create_account(self):
        self.register_email()
        self.sighup_acctoun()
        self.login_account()
        self.arrive()

    def arrive(self):
        param = {
            "auth_token": self.token,
            "version": Config.APP_VERSION
        }
        self.request.post(
            Config.KOETOMO_HOST + Config.ARRIVE_PAHT,
            headers=self.headers,
            params=param
        )

    def login_account(self):
        param = {
            "auth_token": self.token,
            "version": Config.APP_VERSION,
            "email": self.mail,
            "password": self.passwd,
            "device_uid": self.uid
        }
        r = self.request.post(
            Config.KOETOMO_HOST + Config.LOGIN_PATH,
            headers=self.headers,
            params=param
        )
        if r.status_code == 200:
            jso = r.json()
            print("login : success")
            self.user_id = jso["data"]["user_id"]
            self.token = jso["data"]["auth_token"]

    def sighup_acctoun(self):
        param = {
            "auth_token": "",
            "version": "android_3.3.35",
            "email": self.mail,
            "password": self.create_passwd(),
            "name": self.create_name(),
            "sex": "2",
            "birthday": self.create_dirth_day(),
            "device_uid": self.create_device_uid()
        }
        r = self.request.post(
            Config.KOETOMO_HOST + Config.SIGNIN_PATH,
            headers=self.headers,
            params=param
        )
        if r.status_code == 200:
            print("signup : success")
            jso = r.json()
            self.token = jso["data"]["auth_token"]

    def register_email(self):
        param = {
            "auth_token": "",
            "version": Config.APP_VERSION,
            "email": self.create_mail()
        }
        r = self.request.post(
            Config.KOETOMO_HOST + Config.EMAIL_REGISTER,
            headers=self.headers,
            params=param
        )
        if r.status_code == 200:
            print("register_email : success")

    def random_string(self, length):
        ad = "abcdefghijklmnopqrstuvwxyz1234567890"
        return "".join([random.choice(ad) for _ in range(length)])

    def create_mail(self):
        self.mail = f"{self.random_string(8)}@{self.random_string(6)}.com"
        return self.mail

    def create_passwd(self):
        self.passwd = self.random_string(6)
        return self.passwd

    def create_name(self):
        self.name = self.random_string(5)
        return self.name

    def create_device_uid(self):
        self.uid = self.random_string(32)
        return self.uid

    def create_dirth_day(self):
        self.birthday = dt.now().strftime('%Y/%m/%d')
        return self.birthday
