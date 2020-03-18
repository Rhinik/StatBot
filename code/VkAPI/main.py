import requests as r
import time
from config import load
from DotDict import DotDict
from .exception import VkError

class VkAPI:
    """
    Main VK API handler
    """

    def __init__(
                self,
                token=load().vk.token,
                group_id=load().vk.group_id,
                v='5.103'
                ):

        self._url = 'https://api.vk.com/method/'
        self._token = token
        self._group_id = group_id
        self._v = v
        self._data_sending = {
            'access_token': token,
            'v': v
        }

        ## For __getattr__
        self.__method_header = None

        ## LP
        lp_data = r.post(self._url + 'groups.getLongPollServer', data={
                'access_token': self._token,
                'v': self._v,
                'group_id': self._group_id
            }).json()['response']

        self.__key = lp_data['key']
        self.__server = lp_data['server']
        self.__ts = lp_data['ts']

        ## Time of last request for control destance ~0.34
        self.last_req = time.time()
        ## 192979547
        ## groups.getTokenPermissions for token validator




    def __call__(self, **data) -> DotDict:
        """
        Make requests to VK API
        """

        now = time.time()

        if now - self.last_req < 0.34:
            time.sleep(0.34 - (now - self.last_req))


        req = r.post(self._url + self.__method_header, data={**data, **self._data_sending}).json()

        if 'error' in req:
            self.__method_header = None
            raise VkError(
                f"[{req['error']['error_code']}] -- {req['error']['error_msg']}",
                req['error']['request_params']
                )
        else:
            self.__method_header = None
            return DotDict(req["response"]) if isinstance(req["response"], dict) else req["response"]






    def __getattr__(self, value):
        """
        Перегружен для красивых запросов
        """
        if self.__method_header is not None:
            self.__method_header += '.' + value
        else:
            self.__method_header = value

        return self




    def __iter__(self):
        """
        Itering for LongPoll
        """

        while True:

            req = r.post(self.__server, data={
                "act": "a_check",
                "key": self.__key,
                "ts": self.__ts,
                "wait": 25
                }).json()
            for i in req['updates']:
                yield DotDict(i)

            self.__ts = req['ts']
