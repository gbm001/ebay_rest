# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (eBay business policies and seller-defined custom policies), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br/><br/>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SpecialHours(object):
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
        '_date': 'str',
        'intervals': 'list[Interval]'
    }

    attribute_map = {
        '_date': 'date',
        'intervals': 'intervals'
    }

    def __init__(self, _date=None, intervals=None):  # noqa: E501
        """SpecialHours - a model defined in Swagger"""  # noqa: E501
        self.__date = None
        self._intervals = None
        self.discriminator = None
        if _date is not None:
            self._date = _date
        if intervals is not None:
            self.intervals = intervals

    @property
    def _date(self):
        """Gets the _date of this SpecialHours.  # noqa: E501

        A <strong>date</strong> value is required for each specific date that the store location has special operating hours.  <br/><br/>The timestamp is formatted as an <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html \" title=\"https://www.iso.org \" target=\"_blank\">ISO 8601</a> string, which is based on the 24-hour Coordinated Universal Time (UTC) clock.  <br/><br/><b>Format:</b> <code>[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z</code> <br/><b>Example:</b> <code>2018-08-04T07:09:00.000Z</code> <br/><br/>This field is returned if set for the store location.  # noqa: E501

        :return: The _date of this SpecialHours.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this SpecialHours.

        A <strong>date</strong> value is required for each specific date that the store location has special operating hours.  <br/><br/>The timestamp is formatted as an <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html \" title=\"https://www.iso.org \" target=\"_blank\">ISO 8601</a> string, which is based on the 24-hour Coordinated Universal Time (UTC) clock.  <br/><br/><b>Format:</b> <code>[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z</code> <br/><b>Example:</b> <code>2018-08-04T07:09:00.000Z</code> <br/><br/>This field is returned if set for the store location.  # noqa: E501

        :param _date: The _date of this SpecialHours.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def intervals(self):
        """Gets the intervals of this SpecialHours.  # noqa: E501

        This container is used to define the opening and closing times of a store on a specific date (defined in the <strong>date</strong> field). An <strong>intervals</strong> container is needed for each specific date that the store has special operating hours. These special operating hours on the specific date override the normal operating hours for the specific day of the week. If a store location closes for lunch (or any other period during the day) and then reopens, multiple <strong>open</strong> and <strong>close</strong> pairs are needed. <br/><br/>This container is returned if set for the store location.  # noqa: E501

        :return: The intervals of this SpecialHours.  # noqa: E501
        :rtype: list[Interval]
        """
        return self._intervals

    @intervals.setter
    def intervals(self, intervals):
        """Sets the intervals of this SpecialHours.

        This container is used to define the opening and closing times of a store on a specific date (defined in the <strong>date</strong> field). An <strong>intervals</strong> container is needed for each specific date that the store has special operating hours. These special operating hours on the specific date override the normal operating hours for the specific day of the week. If a store location closes for lunch (or any other period during the day) and then reopens, multiple <strong>open</strong> and <strong>close</strong> pairs are needed. <br/><br/>This container is returned if set for the store location.  # noqa: E501

        :param intervals: The intervals of this SpecialHours.  # noqa: E501
        :type: list[Interval]
        """

        self._intervals = intervals

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
        if issubclass(SpecialHours, dict):
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
        if not isinstance(other, SpecialHours):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
