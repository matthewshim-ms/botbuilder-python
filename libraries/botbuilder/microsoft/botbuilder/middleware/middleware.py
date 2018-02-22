# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.


from abc import ABC, abstractmethod


class Middleware(ABC):
    """
    It is not required to implement this class as MiddlewareSet also features support for dicts.
    When implementing this class you will either need to implement each method.
    To avoid having having use each method, either create a dict or override the method to pass.
    """
    @abstractmethod
    async def context_created(self, context):
        """
        (Optional) called when a new context object has been created.
        Plugins can extend the context object in this call.
        :param context:
        :return:
        """
        pass

    @abstractmethod
    async def receive_activity(self, context):
        """
        (Optional) called after context_created to route a receive activity.
        Plugins can return `{'handled': True}` to indicate that they have successfully routed the
        activity. This will prevent further calls to receive_activity()
        :param context:
        :return:
        """
        pass

    @abstractmethod
    async def send_activity(self, context, activities):
        """
        (Optional) called anytime an outgoing set of activities are being sent.
        Plugins can implement logic to either transform the outgoing activities or to persist some
        state prior to delivery of the activities.
        :param context:
        :param activities:
        :return:
        """
        pass
