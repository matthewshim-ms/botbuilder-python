import asyncio
from microsoft.botbuilder.luisruntime import luis_client
from microsoft.botbuilder.middleware import IntentRecognizerMiddleware

class LuisRecognizerMiddleware(IntentRecognizerMiddleware):
    def __init__(self, app_id, app_key):
        self._app_ID = app_id or False
        if not self._app_ID:
            raise TypeError('Invalid LUIS App ID')
        self._app_Key = app_key or False
        if not self._app_Key:
            raise TypeError('Invalid LUIS App Key')

        self._luis_client = luis_client(app_id, app_key)


    @classmethod
    def from_base_Uri(cls, base_Uri):

    def setup_on_recognize(self):
        self.on_recognize()

class LuisEntity():
    def __init__(self):
        self.__type =