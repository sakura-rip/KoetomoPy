from .config import Config


class Talk(object):
    def __init__(self):
        pass

    def get_post(self, count=20):
        param = {
            "auth_token": self.token,
            "version": Config.APP_VERSION,
            "count": str(count)
        }
        r = self.request.get(
            Config.KOETOMO_HOST + Config.FEED_PATH,
            headers=self.headers,
            params=param
        )
        if r.status_code == 200:
            print("O")

    def call(self, target):
        param = {
            "auth_token": self.token,
            "version": Config.APP_VERSION,
            "target_id": target
        }
        self.request.post(
            Config.KOETOMO_HOST + Config.CALL,
            headers=self.headers,
            params=param
        )

    def comment_comment(self, postid, text):
        param = {
            "auth_token": self.token,
            "version": Config.APP_VERSION,
            "text": text
        }
        self.request.post(
            Config.KOETOMO_HOST + f"{Config.FEED_PATH}/{postid}/comments",
            headers=self.header,
            params=param
        )

    def line_post(self, postid):
        param = {
            "auth_token": self.token,
            "version": Config.APP_VERSION
        }
        self.request.post(
            Config.KOETOMO_HOST + f"{Config.FEED_PATH}/{postid}/like",
            headers=self.headers
            params=param
        )

    def follod(self, id_):
        param = {
            "auth_token": self.token,
            "target_id": id_,
            "version": Config.APP_VERSION
        }
        r = self.request.post(
            Config.KOETOMO_HOST + Config.FOLLOW,
            headers=self.header,
            params=param
        )
        if r.status_code == 200:
            print("OK")
