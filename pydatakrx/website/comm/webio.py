import requests
import time
from abc import abstractmethod

KRX_LOGIN_URL = "http://data.krx.co.kr/comm/member/login.cmd"

class SessionManager:
    def __init__(self):
        self._session = None
        self._last_login_time = 0
        self._login_params = {}
        self._session_duration = 20 * 60

    def set_credentials(self, mbrNm, telNo, di, certType, mbrId, pw):
        self._login_params = {
            "mbrNm": mbrNm,
            "telNo": telNo,
            "di": di,
            "certType": certType,
            "mbrId": mbrId,
            "pw": pw
        }
        self._session = None
        self._last_login_time = 0

    def login(self):
        session = requests.Session()
        if self._login_params:
            session.post(KRX_LOGIN_URL, data=self._login_params)

        self._session = session
        self._last_login_time = time.time()

    def get_session(self):
        if self._session is None or (time.time() - self._last_login_time > self._session_duration):
            self.login()
        return self._session

_session_manager = SessionManager()

def set_krx_login_info(mbrNm="", telNo="", di="", certType="", mbrId="sankenan", pw=""):
    _session_manager.set_credentials(mbrNm, telNo, di, certType, mbrId, pw)


class Get:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0", 
            "Referer": "http://data.krx.co.kr/"
        }

    def read(self, **params):
        resp = _session_manager.get_session().get(self.url, headers=self.headers, params=params)
        return resp

    @property
    @abstractmethod
    def url(self):
        return NotImplementedError


class Post:
    def __init__(self, headers=None):
        self.headers = {
            "User-Agent": "Mozilla/5.0",
            "Referer": "http://data.krx.co.kr/"
        }
        if headers is not None:
            self.headers.update(headers)

    def read(self, **params):
        resp = _session_manager.get_session().post(self.url, headers=self.headers, data=params)
        return resp

    @property
    @abstractmethod
    def url(self):
        return NotImplementedError
