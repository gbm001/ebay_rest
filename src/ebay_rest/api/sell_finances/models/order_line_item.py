# coding: utf-8

"""
    eBay Finances API

    This API is used to retrieve seller payouts and monetary transaction details related to those payouts.  # noqa: E501

    OpenAPI spec version: v1.15.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class OrderLineItem(object):
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
        'fee_basis_amount': 'Amount',
        'line_item_id': 'str',
        'marketplace_fees': 'list[Fee]'
    }

    attribute_map = {
        'fee_basis_amount': 'feeBasisAmount',
        'line_item_id': 'lineItemId',
        'marketplace_fees': 'marketplaceFees'
    }

    def __init__(self, fee_basis_amount=None, line_item_id=None, marketplace_fees=None):  # noqa: E501
        """OrderLineItem - a model defined in Swagger"""  # noqa: E501
        self._fee_basis_amount = None
        self._line_item_id = None
        self._marketplace_fees = None
        self.discriminator = None
        if fee_basis_amount is not None:
            self.fee_basis_amount = fee_basis_amount
        if line_item_id is not None:
            self.line_item_id = line_item_id
        if marketplace_fees is not None:
            self.marketplace_fees = marketplace_fees

    @property
    def fee_basis_amount(self):
        """Gets the fee_basis_amount of this OrderLineItem.  # noqa: E501


        :return: The fee_basis_amount of this OrderLineItem.  # noqa: E501
        :rtype: Amount
        """
        return self._fee_basis_amount

    @fee_basis_amount.setter
    def fee_basis_amount(self, fee_basis_amount):
        """Sets the fee_basis_amount of this OrderLineItem.


        :param fee_basis_amount: The fee_basis_amount of this OrderLineItem.  # noqa: E501
        :type: Amount
        """

        self._fee_basis_amount = fee_basis_amount

    @property
    def line_item_id(self):
        """Gets the line_item_id of this OrderLineItem.  # noqa: E501

        The unique identifier of an order line item.  # noqa: E501

        :return: The line_item_id of this OrderLineItem.  # noqa: E501
        :rtype: str
        """
        return self._line_item_id

    @line_item_id.setter
    def line_item_id(self, line_item_id):
        """Sets the line_item_id of this OrderLineItem.

        The unique identifier of an order line item.  # noqa: E501

        :param line_item_id: The line_item_id of this OrderLineItem.  # noqa: E501
        :type: str
        """

        self._line_item_id = line_item_id

    @property
    def marketplace_fees(self):
        """Gets the marketplace_fees of this OrderLineItem.  # noqa: E501

        An array of all fees accrued for the order line item and deducted from a seller payout.  # noqa: E501

        :return: The marketplace_fees of this OrderLineItem.  # noqa: E501
        :rtype: list[Fee]
        """
        return self._marketplace_fees

    @marketplace_fees.setter
    def marketplace_fees(self, marketplace_fees):
        """Sets the marketplace_fees of this OrderLineItem.

        An array of all fees accrued for the order line item and deducted from a seller payout.  # noqa: E501

        :param marketplace_fees: The marketplace_fees of this OrderLineItem.  # noqa: E501
        :type: list[Fee]
        """

        self._marketplace_fees = marketplace_fees

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
        if issubclass(OrderLineItem, dict):
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
        if not isinstance(other, OrderLineItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
