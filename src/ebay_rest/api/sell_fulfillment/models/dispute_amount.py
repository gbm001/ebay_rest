# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DisputeAmount(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'converted_from_currency': 'str',
        'converted_from_value': 'str',
        'currency': 'str',
        'exchange_rate': 'str',
        'value': 'str'
    }

    attribute_map = {
        'converted_from_currency': 'convertedFromCurrency',
        'converted_from_value': 'convertedFromValue',
        'currency': 'currency',
        'exchange_rate': 'exchangeRate',
        'value': 'value'
    }

    def __init__(self, converted_from_currency=None, converted_from_value=None, currency=None, exchange_rate=None, value=None):  # noqa: E501
        """DisputeAmount - a model defined in Swagger"""  # noqa: E501
        self._converted_from_currency = None
        self._converted_from_value = None
        self._currency = None
        self._exchange_rate = None
        self._value = None
        self.discriminator = None
        if converted_from_currency is not None:
            self.converted_from_currency = converted_from_currency
        if converted_from_value is not None:
            self.converted_from_value = converted_from_value
        if currency is not None:
            self.currency = currency
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if value is not None:
            self.value = value

    @property
    def converted_from_currency(self):
        """Gets the converted_from_currency of this DisputeAmount.  # noqa: E501

        The three-letter ISO 4217 code representing the currency of the amount in the convertedFromValue field. This value is the pre-conversion currency. This field is only returned if/when currency conversion was applied by eBay. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/ba:CurrencyCodeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The converted_from_currency of this DisputeAmount.  # noqa: E501
        :rtype: str
        """
        return self._converted_from_currency

    @converted_from_currency.setter
    def converted_from_currency(self, converted_from_currency):
        """Sets the converted_from_currency of this DisputeAmount.

        The three-letter ISO 4217 code representing the currency of the amount in the convertedFromValue field. This value is the pre-conversion currency. This field is only returned if/when currency conversion was applied by eBay. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/ba:CurrencyCodeEnum'>eBay API documentation</a>  # noqa: E501

        :param converted_from_currency: The converted_from_currency of this DisputeAmount.  # noqa: E501
        :type: str
        """

        self._converted_from_currency = converted_from_currency

    @property
    def converted_from_value(self):
        """Gets the converted_from_value of this DisputeAmount.  # noqa: E501

        The monetary amount before any conversion is performed, in the currency specified by the convertedFromCurrency field. This value is the pre-conversion amount. The value field contains the converted amount of this value, in the currency specified by the currency field. This field is only returned if/when currency conversion was applied by eBay.  # noqa: E501

        :return: The converted_from_value of this DisputeAmount.  # noqa: E501
        :rtype: str
        """
        return self._converted_from_value

    @converted_from_value.setter
    def converted_from_value(self, converted_from_value):
        """Sets the converted_from_value of this DisputeAmount.

        The monetary amount before any conversion is performed, in the currency specified by the convertedFromCurrency field. This value is the pre-conversion amount. The value field contains the converted amount of this value, in the currency specified by the currency field. This field is only returned if/when currency conversion was applied by eBay.  # noqa: E501

        :param converted_from_value: The converted_from_value of this DisputeAmount.  # noqa: E501
        :type: str
        """

        self._converted_from_value = converted_from_value

    @property
    def currency(self):
        """Gets the currency of this DisputeAmount.  # noqa: E501

        A three-letter ISO 4217 code that indicates the currency of the amount in the value field. This field is always returned with any container using Amount type. Default: The currency of the authenticated user's country. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/ba:CurrencyCodeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The currency of this DisputeAmount.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this DisputeAmount.

        A three-letter ISO 4217 code that indicates the currency of the amount in the value field. This field is always returned with any container using Amount type. Default: The currency of the authenticated user's country. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/ba:CurrencyCodeEnum'>eBay API documentation</a>  # noqa: E501

        :param currency: The currency of this DisputeAmount.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this DisputeAmount.  # noqa: E501

        The exchange rate used for the monetary conversion. This field shows the exchange rate used to convert the dollar value in the value field from the dollar value in the convertedFromValue field. This field is only returned if/when currency conversion was applied by eBay.  # noqa: E501

        :return: The exchange_rate of this DisputeAmount.  # noqa: E501
        :rtype: str
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this DisputeAmount.

        The exchange rate used for the monetary conversion. This field shows the exchange rate used to convert the dollar value in the value field from the dollar value in the convertedFromValue field. This field is only returned if/when currency conversion was applied by eBay.  # noqa: E501

        :param exchange_rate: The exchange_rate of this DisputeAmount.  # noqa: E501
        :type: str
        """

        self._exchange_rate = exchange_rate

    @property
    def value(self):
        """Gets the value of this DisputeAmount.  # noqa: E501

        The monetary amount, in the currency specified by the currency field. This field is always returned with any container using Amount type.  # noqa: E501

        :return: The value of this DisputeAmount.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DisputeAmount.

        The monetary amount, in the currency specified by the currency field. This field is always returned with any container using Amount type.  # noqa: E501

        :param value: The value of this DisputeAmount.  # noqa: E501
        :type: str
        """

        self._value = value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DisputeAmount, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DisputeAmount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
