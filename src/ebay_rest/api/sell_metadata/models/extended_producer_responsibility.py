# coding: utf-8

"""
    Metadata API

    The Metadata API has operations that retrieve configuration details pertaining to the different eBay marketplaces. In addition to marketplace information, the API also has operations that get information that helps sellers list items on eBay.  # noqa: E501

    OpenAPI spec version: v1.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ExtendedProducerResponsibility(object):
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
        'enabled_for_variations': 'bool',
        'name': 'str',
        'usage': 'str'
    }

    attribute_map = {
        'enabled_for_variations': 'enabledForVariations',
        'name': 'name',
        'usage': 'usage'
    }

    def __init__(self, enabled_for_variations=None, name=None, usage=None):  # noqa: E501
        """ExtendedProducerResponsibility - a model defined in Swagger"""  # noqa: E501
        self._enabled_for_variations = None
        self._name = None
        self._usage = None
        self.discriminator = None
        if enabled_for_variations is not None:
            self.enabled_for_variations = enabled_for_variations
        if name is not None:
            self.name = name
        if usage is not None:
            self.usage = usage

    @property
    def enabled_for_variations(self):
        """Gets the enabled_for_variations of this ExtendedProducerResponsibility.  # noqa: E501

        An indication of whether the attribute can be enabled for listing variations.<br /><br />If the value is <code>true</code>, the attribute may be specified at the variation level.  # noqa: E501

        :return: The enabled_for_variations of this ExtendedProducerResponsibility.  # noqa: E501
        :rtype: bool
        """
        return self._enabled_for_variations

    @enabled_for_variations.setter
    def enabled_for_variations(self, enabled_for_variations):
        """Sets the enabled_for_variations of this ExtendedProducerResponsibility.

        An indication of whether the attribute can be enabled for listing variations.<br /><br />If the value is <code>true</code>, the attribute may be specified at the variation level.  # noqa: E501

        :param enabled_for_variations: The enabled_for_variations of this ExtendedProducerResponsibility.  # noqa: E501
        :type: bool
        """

        self._enabled_for_variations = enabled_for_variations

    @property
    def name(self):
        """Gets the name of this ExtendedProducerResponsibility.  # noqa: E501

        The name of the attribute included in the policy. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/metadata/types/sel:ExtendedProducerResponsibilityEnum'>eBay API documentation</a>  # noqa: E501

        :return: The name of this ExtendedProducerResponsibility.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExtendedProducerResponsibility.

        The name of the attribute included in the policy. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/metadata/types/sel:ExtendedProducerResponsibilityEnum'>eBay API documentation</a>  # noqa: E501

        :param name: The name of this ExtendedProducerResponsibility.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def usage(self):
        """Gets the usage of this ExtendedProducerResponsibility.  # noqa: E501

        The usage guidelines for the attribute, in the specified marketplace. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/metadata/types/sel:GenericUsageEnum'>eBay API documentation</a>  # noqa: E501

        :return: The usage of this ExtendedProducerResponsibility.  # noqa: E501
        :rtype: str
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this ExtendedProducerResponsibility.

        The usage guidelines for the attribute, in the specified marketplace. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/metadata/types/sel:GenericUsageEnum'>eBay API documentation</a>  # noqa: E501

        :param usage: The usage of this ExtendedProducerResponsibility.  # noqa: E501
        :type: str
        """

        self._usage = usage

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
        if issubclass(ExtendedProducerResponsibility, dict):
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
        if not isinstance(other, ExtendedProducerResponsibility):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other