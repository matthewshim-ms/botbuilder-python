from microsoft.botbuilder.schema import Activity
from microsoft.botbuilder.middleware import Middleware
import requests
import asyncio

class QnaMakerMiddleware(Middleware):
    def __init__(self, options):
        self._options = options


    async def receive_activity(self, context):
