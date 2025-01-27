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

class Subscription(object):
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
        'marketplace_id': 'str',
        'subscription_id': 'str',
        'subscription_level': 'str',
        'subscription_type': 'str',
        'term': 'TimeDuration'
    }

    attribute_map = {
        'marketplace_id': 'marketplaceId',
        'subscription_id': 'subscriptionId',
        'subscription_level': 'subscriptionLevel',
        'subscription_type': 'subscriptionType',
        'term': 'term'
    }

    def __init__(self, marketplace_id=None, subscription_id=None, subscription_level=None, subscription_type=None, term=None):  # noqa: E501
        """Subscription - a model defined in Swagger"""  # noqa: E501
        self._marketplace_id = None
        self._subscription_id = None
        self._subscription_level = None
        self._subscription_type = None
        self._term = None
        self.discriminator = None
        if marketplace_id is not None:
            self.marketplace_id = marketplace_id
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if subscription_level is not None:
            self.subscription_level = subscription_level
        if subscription_type is not None:
            self.subscription_type = subscription_type
        if term is not None:
            self.term = term

    @property
    def marketplace_id(self):
        """Gets the marketplace_id of this Subscription.  # noqa: E501

        The marketplace with which the subscription is associated. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :return: The marketplace_id of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._marketplace_id

    @marketplace_id.setter
    def marketplace_id(self, marketplace_id):
        """Sets the marketplace_id of this Subscription.

        The marketplace with which the subscription is associated. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :param marketplace_id: The marketplace_id of this Subscription.  # noqa: E501
        :type: str
        """

        self._marketplace_id = marketplace_id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this Subscription.  # noqa: E501

        The subscription ID.  # noqa: E501

        :return: The subscription_id of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this Subscription.

        The subscription ID.  # noqa: E501

        :param subscription_id: The subscription_id of this Subscription.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def subscription_level(self):
        """Gets the subscription_level of this Subscription.  # noqa: E501

        The subscription level. For example, subscription levels for an eBay store include Starter, Basic, Featured, Anchor, and Enterprise levels.  # noqa: E501

        :return: The subscription_level of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._subscription_level

    @subscription_level.setter
    def subscription_level(self, subscription_level):
        """Sets the subscription_level of this Subscription.

        The subscription level. For example, subscription levels for an eBay store include Starter, Basic, Featured, Anchor, and Enterprise levels.  # noqa: E501

        :param subscription_level: The subscription_level of this Subscription.  # noqa: E501
        :type: str
        """

        self._subscription_level = subscription_level

    @property
    def subscription_type(self):
        """Gets the subscription_type of this Subscription.  # noqa: E501

        The kind of entity with which the subscription is associated, such as an eBay store. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:SubscriptionTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The subscription_type of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._subscription_type

    @subscription_type.setter
    def subscription_type(self, subscription_type):
        """Sets the subscription_type of this Subscription.

        The kind of entity with which the subscription is associated, such as an eBay store. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:SubscriptionTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param subscription_type: The subscription_type of this Subscription.  # noqa: E501
        :type: str
        """

        self._subscription_type = subscription_type

    @property
    def term(self):
        """Gets the term of this Subscription.  # noqa: E501


        :return: The term of this Subscription.  # noqa: E501
        :rtype: TimeDuration
        """
        return self._term

    @term.setter
    def term(self, term):
        """Sets the term of this Subscription.


        :param term: The term of this Subscription.  # noqa: E501
        :type: TimeDuration
        """

        self._term = term

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
        if issubclass(Subscription, dict):
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
        if not isinstance(other, Subscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
