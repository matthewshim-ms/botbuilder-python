# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PaymentCurrencyAmount(Model):
    """Supplies monetary amounts.

    :param currency: A currency identifier
    :type currency: str
    :param value: Decimal monetary value
    :type value: str
    :param currency_system: Currency system
    :type currency_system: str
    """

    _attribute_map = {
        'currency': {'key': 'currency', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'currency_system': {'key': 'currencySystem', 'type': 'str'},
    }

    def __init__(self, currency=None, value=None, currency_system=None):
        super(PaymentCurrencyAmount, self).__init__()
        self.currency = currency
        self.value = value
        self.currency_system = currency_system
