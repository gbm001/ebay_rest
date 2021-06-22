# coding: utf-8

"""
    Metadata API

    The Metadata API has operations that retrieve configuration details pertaining to the different eBay marketplaces. In addition to marketplace information, the API also has operations that get information that helps sellers list items on eBay.  # noqa: E501

    OpenAPI spec version: v1.4.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ItemCondition(object):
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
        'condition_description': 'str',
        'condition_id': 'str'
    }

    attribute_map = {
        'condition_description': 'conditionDescription',
        'condition_id': 'conditionId'
    }

    def __init__(self, condition_description=None, condition_id=None):  # noqa: E501
        """ItemCondition - a model defined in Swagger"""  # noqa: E501
        self._condition_description = None
        self._condition_id = None
        self.discriminator = None
        if condition_description is not None:
            self.condition_description = condition_description
        if condition_id is not None:
            self.condition_id = condition_id

    @property
    def condition_description(self):
        """Gets the condition_description of this ItemCondition.  # noqa: E501

        The human-readable label for the condition (e.g., &quot;New&quot;). This value is typically localized for each site. Note that the display name can vary by category. For example, the description for condition ID 1000 could be called &quot;New: with Tags&quot; in one category and &quot;Brand New&quot; in another. For details on condition IDs and descriptions, see Item condition ID and name values.  # noqa: E501

        :return: The condition_description of this ItemCondition.  # noqa: E501
        :rtype: str
        """
        return self._condition_description

    @condition_description.setter
    def condition_description(self, condition_description):
        """Sets the condition_description of this ItemCondition.

        The human-readable label for the condition (e.g., &quot;New&quot;). This value is typically localized for each site. Note that the display name can vary by category. For example, the description for condition ID 1000 could be called &quot;New: with Tags&quot; in one category and &quot;Brand New&quot; in another. For details on condition IDs and descriptions, see Item condition ID and name values.  # noqa: E501

        :param condition_description: The condition_description of this ItemCondition.  # noqa: E501
        :type: str
        """

        self._condition_description = condition_description

    @property
    def condition_id(self):
        """Gets the condition_id of this ItemCondition.  # noqa: E501

        The ID value of the selected item condition. For information on the supported condition ID values, see Item condition ID and name values.  # noqa: E501

        :return: The condition_id of this ItemCondition.  # noqa: E501
        :rtype: str
        """
        return self._condition_id

    @condition_id.setter
    def condition_id(self, condition_id):
        """Sets the condition_id of this ItemCondition.

        The ID value of the selected item condition. For information on the supported condition ID values, see Item condition ID and name values.  # noqa: E501

        :param condition_id: The condition_id of this ItemCondition.  # noqa: E501
        :type: str
        """

        self._condition_id = condition_id

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
        if issubclass(ItemCondition, dict):
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
        if not isinstance(other, ItemCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
