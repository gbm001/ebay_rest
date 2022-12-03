# coding: utf-8

"""
    Progress to Rate Limit API

    The <b>Analytics API</b> retrieves call-limit data and the quotas that are set for the RESTful APIs and the legacy Trading API.  <br><br>Responses from calls made to <b>getRateLimits</b> and <b>getUerRateLimits</b> include a list of the applicable resources and the \"call limit\", or quota, that is set for each resource. In addition to quota information, the response also includes the number of remaining calls available before the limit is reached, the time remaining before the quota resets, and the length of the \"time window\" to which the quota applies.  <br><br>The <b>getRateLimits</b> and <b>getUserRateLimits</b> methods retrieve call-limit information for either an application or user, respectively, and each method must be called with an appropriate OAuth token. That is, <b>getRateLimites</b> requires an access token generated with a client credentials grant and <b>getUserRateLimites</b> requires an access token generated with an authorization code grant. For more information, see <a href=\"/api-docs/static/oauth-tokens.html\">OAuth tokens</a>.  <br><br>Users can analyze the response data to see whether or not a limit might be reached, and from that determine if any action needs to be taken (such as programmatically throttling their request rate). For more on call limits, see <a href=\"https://developer.ebay.com/support/app-check\" target=\"_blank\">Compatible Application Check</a>.  # noqa: E501

    OpenAPI spec version: v1_beta.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Resource(object):
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
        'name': 'str',
        'rates': 'list[Rate]'
    }

    attribute_map = {
        'name': 'name',
        'rates': 'rates'
    }

    def __init__(self, name=None, rates=None):  # noqa: E501
        """Resource - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._rates = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if rates is not None:
            self.rates = rates

    @property
    def name(self):
        """Gets the name of this Resource.  # noqa: E501

        The name of the resource (an API or an API method) to which the rate-limit data applies.  # noqa: E501

        :return: The name of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Resource.

        The name of the resource (an API or an API method) to which the rate-limit data applies.  # noqa: E501

        :param name: The name of this Resource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def rates(self):
        """Gets the rates of this Resource.  # noqa: E501

        A list of rate-limit data, where each list element represents the rate-limit data for a specific resource.  # noqa: E501

        :return: The rates of this Resource.  # noqa: E501
        :rtype: list[Rate]
        """
        return self._rates

    @rates.setter
    def rates(self, rates):
        """Sets the rates of this Resource.

        A list of rate-limit data, where each list element represents the rate-limit data for a specific resource.  # noqa: E501

        :param rates: The rates of this Resource.  # noqa: E501
        :type: list[Rate]
        """

        self._rates = rates

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
        if issubclass(Resource, dict):
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
        if not isinstance(other, Resource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
