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

class RateLimit(object):
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
        'api_context': 'str',
        'api_name': 'str',
        'api_version': 'str',
        'resources': 'list[Resource]'
    }

    attribute_map = {
        'api_context': 'apiContext',
        'api_name': 'apiName',
        'api_version': 'apiVersion',
        'resources': 'resources'
    }

    def __init__(self, api_context=None, api_name=None, api_version=None, resources=None):  # noqa: E501
        """RateLimit - a model defined in Swagger"""  # noqa: E501
        self._api_context = None
        self._api_name = None
        self._api_version = None
        self._resources = None
        self.discriminator = None
        if api_context is not None:
            self.api_context = api_context
        if api_name is not None:
            self.api_name = api_name
        if api_version is not None:
            self.api_version = api_version
        if resources is not None:
            self.resources = resources

    @property
    def api_context(self):
        """Gets the api_context of this RateLimit.  # noqa: E501

        The context of the API for which rate-limit data is returned. For example <code>buy</code>, <code>sell</code>, <code>commerce</code>, <code>developer</code> or <code>tradingapi</code>.  # noqa: E501

        :return: The api_context of this RateLimit.  # noqa: E501
        :rtype: str
        """
        return self._api_context

    @api_context.setter
    def api_context(self, api_context):
        """Sets the api_context of this RateLimit.

        The context of the API for which rate-limit data is returned. For example <code>buy</code>, <code>sell</code>, <code>commerce</code>, <code>developer</code> or <code>tradingapi</code>.  # noqa: E501

        :param api_context: The api_context of this RateLimit.  # noqa: E501
        :type: str
        """

        self._api_context = api_context

    @property
    def api_name(self):
        """Gets the api_name of this RateLimit.  # noqa: E501

        The name of the API for which rate-limit data is returned. For example <code>browse</code> for the Buy API, <code>inventory</code> for the Sell API, <code>taxonomy</code> for the Commerce API, or <code>tradingapi</code> for Trading API.  # noqa: E501

        :return: The api_name of this RateLimit.  # noqa: E501
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        """Sets the api_name of this RateLimit.

        The name of the API for which rate-limit data is returned. For example <code>browse</code> for the Buy API, <code>inventory</code> for the Sell API, <code>taxonomy</code> for the Commerce API, or <code>tradingapi</code> for Trading API.  # noqa: E501

        :param api_name: The api_name of this RateLimit.  # noqa: E501
        :type: str
        """

        self._api_name = api_name

    @property
    def api_version(self):
        """Gets the api_version of this RateLimit.  # noqa: E501

        The version of the API for which rate-limit data is returned. For example <code>v1</code> or <code>v2</code>.  # noqa: E501

        :return: The api_version of this RateLimit.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this RateLimit.

        The version of the API for which rate-limit data is returned. For example <code>v1</code> or <code>v2</code>.  # noqa: E501

        :param api_version: The api_version of this RateLimit.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def resources(self):
        """Gets the resources of this RateLimit.  # noqa: E501

        A list of the methods for which rate-limit data is returned. For example <code>item</code> for the Feed API, <code>getOrder</code> for the Fulfillment API, <code>getProduct</code> for the Catalog API, <code>AddItems</code> for the Trading API.  # noqa: E501

        :return: The resources of this RateLimit.  # noqa: E501
        :rtype: list[Resource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this RateLimit.

        A list of the methods for which rate-limit data is returned. For example <code>item</code> for the Feed API, <code>getOrder</code> for the Fulfillment API, <code>getProduct</code> for the Catalog API, <code>AddItems</code> for the Trading API.  # noqa: E501

        :param resources: The resources of this RateLimit.  # noqa: E501
        :type: list[Resource]
        """

        self._resources = resources

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
        if issubclass(RateLimit, dict):
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
        if not isinstance(other, RateLimit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
