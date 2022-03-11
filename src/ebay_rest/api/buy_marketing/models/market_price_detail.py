# coding: utf-8

"""
    Buy Marketing API

    The Marketing API retrieves eBay products based on a metric, such as Best Selling, as well as products that were also bought and also viewed.  # noqa: E501

    OpenAPI spec version: v1_beta.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MarketPriceDetail(object):
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
        'condition_group': 'str',
        'condition_ids': 'list[str]',
        'estimated_start_price': 'Amount'
    }

    attribute_map = {
        'condition_group': 'conditionGroup',
        'condition_ids': 'conditionIds',
        'estimated_start_price': 'estimatedStartPrice'
    }

    def __init__(self, condition_group=None, condition_ids=None, estimated_start_price=None):  # noqa: E501
        """MarketPriceDetail - a model defined in Swagger"""  # noqa: E501
        self._condition_group = None
        self._condition_ids = None
        self._estimated_start_price = None
        self.discriminator = None
        if condition_group is not None:
            self.condition_group = condition_group
        if condition_ids is not None:
            self.condition_ids = condition_ids
        if estimated_start_price is not None:
            self.estimated_start_price = estimated_start_price

    @property
    def condition_group(self):
        """Gets the condition_group of this MarketPriceDetail.  # noqa: E501

        The name for the condition of the product. For example: NEW  # noqa: E501

        :return: The condition_group of this MarketPriceDetail.  # noqa: E501
        :rtype: str
        """
        return self._condition_group

    @condition_group.setter
    def condition_group(self, condition_group):
        """Sets the condition_group of this MarketPriceDetail.

        The name for the condition of the product. For example: NEW  # noqa: E501

        :param condition_group: The condition_group of this MarketPriceDetail.  # noqa: E501
        :type: str
        """

        self._condition_group = condition_group

    @property
    def condition_ids(self):
        """Gets the condition_ids of this MarketPriceDetail.  # noqa: E501

        An array of condition identifiers for the product.  # noqa: E501

        :return: The condition_ids of this MarketPriceDetail.  # noqa: E501
        :rtype: list[str]
        """
        return self._condition_ids

    @condition_ids.setter
    def condition_ids(self, condition_ids):
        """Sets the condition_ids of this MarketPriceDetail.

        An array of condition identifiers for the product.  # noqa: E501

        :param condition_ids: The condition_ids of this MarketPriceDetail.  # noqa: E501
        :type: list[str]
        """

        self._condition_ids = condition_ids

    @property
    def estimated_start_price(self):
        """Gets the estimated_start_price of this MarketPriceDetail.  # noqa: E501


        :return: The estimated_start_price of this MarketPriceDetail.  # noqa: E501
        :rtype: Amount
        """
        return self._estimated_start_price

    @estimated_start_price.setter
    def estimated_start_price(self, estimated_start_price):
        """Sets the estimated_start_price of this MarketPriceDetail.


        :param estimated_start_price: The estimated_start_price of this MarketPriceDetail.  # noqa: E501
        :type: Amount
        """

        self._estimated_start_price = estimated_start_price

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
        if issubclass(MarketPriceDetail, dict):
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
        if not isinstance(other, MarketPriceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
