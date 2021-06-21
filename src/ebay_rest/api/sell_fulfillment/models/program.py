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

class Program(object):
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
        'authenticity_verification': 'PostSaleAuthenticationProgram',
        'fulfillment_program': 'EbayFulfillmentProgram'
    }

    attribute_map = {
        'authenticity_verification': 'authenticityVerification',
        'fulfillment_program': 'fulfillmentProgram'
    }

    def __init__(self, authenticity_verification=None, fulfillment_program=None):  # noqa: E501
        """Program - a model defined in Swagger"""  # noqa: E501
        self._authenticity_verification = None
        self._fulfillment_program = None
        self.discriminator = None
        if authenticity_verification is not None:
            self.authenticity_verification = authenticity_verification
        if fulfillment_program is not None:
            self.fulfillment_program = fulfillment_program

    @property
    def authenticity_verification(self):
        """Gets the authenticity_verification of this Program.  # noqa: E501


        :return: The authenticity_verification of this Program.  # noqa: E501
        :rtype: PostSaleAuthenticationProgram
        """
        return self._authenticity_verification

    @authenticity_verification.setter
    def authenticity_verification(self, authenticity_verification):
        """Sets the authenticity_verification of this Program.


        :param authenticity_verification: The authenticity_verification of this Program.  # noqa: E501
        :type: PostSaleAuthenticationProgram
        """

        self._authenticity_verification = authenticity_verification

    @property
    def fulfillment_program(self):
        """Gets the fulfillment_program of this Program.  # noqa: E501


        :return: The fulfillment_program of this Program.  # noqa: E501
        :rtype: EbayFulfillmentProgram
        """
        return self._fulfillment_program

    @fulfillment_program.setter
    def fulfillment_program(self, fulfillment_program):
        """Sets the fulfillment_program of this Program.


        :param fulfillment_program: The fulfillment_program of this Program.  # noqa: E501
        :type: EbayFulfillmentProgram
        """

        self._fulfillment_program = fulfillment_program

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
        if issubclass(Program, dict):
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
        if not isinstance(other, Program):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
