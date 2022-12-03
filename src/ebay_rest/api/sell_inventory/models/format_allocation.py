# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.16.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FormatAllocation(object):
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
        'auction': 'int',
        'fixed_price': 'int'
    }

    attribute_map = {
        'auction': 'auction',
        'fixed_price': 'fixedPrice'
    }

    def __init__(self, auction=None, fixed_price=None):  # noqa: E501
        """FormatAllocation - a model defined in Swagger"""  # noqa: E501
        self._auction = None
        self._fixed_price = None
        self.discriminator = None
        if auction is not None:
            self.auction = auction
        if fixed_price is not None:
            self.fixed_price = fixed_price

    @property
    def auction(self):
        """Gets the auction of this FormatAllocation.  # noqa: E501

        This integer value indicates the quantity of the inventory item that is reserved for the published auction format offers of the SKU.  # noqa: E501

        :return: The auction of this FormatAllocation.  # noqa: E501
        :rtype: int
        """
        return self._auction

    @auction.setter
    def auction(self, auction):
        """Sets the auction of this FormatAllocation.

        This integer value indicates the quantity of the inventory item that is reserved for the published auction format offers of the SKU.  # noqa: E501

        :param auction: The auction of this FormatAllocation.  # noqa: E501
        :type: int
        """

        self._auction = auction

    @property
    def fixed_price(self):
        """Gets the fixed_price of this FormatAllocation.  # noqa: E501

        This integer value indicates the quantity of the inventory item that is available for the fixed-price offers of the SKU.  # noqa: E501

        :return: The fixed_price of this FormatAllocation.  # noqa: E501
        :rtype: int
        """
        return self._fixed_price

    @fixed_price.setter
    def fixed_price(self, fixed_price):
        """Sets the fixed_price of this FormatAllocation.

        This integer value indicates the quantity of the inventory item that is available for the fixed-price offers of the SKU.  # noqa: E501

        :param fixed_price: The fixed_price of this FormatAllocation.  # noqa: E501
        :type: int
        """

        self._fixed_price = fixed_price

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
        if issubclass(FormatAllocation, dict):
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
        if not isinstance(other, FormatAllocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
