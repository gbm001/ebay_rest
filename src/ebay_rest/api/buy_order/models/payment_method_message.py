# coding: utf-8

"""
    Order API

    The Order API provides interfaces that lets shoppers pay for items (for both eBay guest and eBay member buyers). It also returns payment and shipping status of the order. It enables eBay partners to use accept payment without being <a href=\"https://www.pcisecuritystandards.org/\">PCI compliant</a> and use the <a href=\"/api-docs/buy/static/api-order.html#Post\">Post Order API</a> for returns and cancellations for eBay member buyers.   <p>The Order API has the following resources:  </p>  <ul>  <li><b>checkout_session:</b> Lets eBay members purchase items using PayPal or a credit card.</li>  <li><b>guest_checkout_session:</b> Lets eBay guests purchase items using a credit card or the <a href=\"/api-docs/buy/static/api-order.html#spb-checkout\">PayPal Smart Button</a>.</li>   <li><b>proxy_guest_checkout_session:</b> Lets eBay guests purchase items through a <a href=\"/api-docs/buy/static/api-order.html#vsp-checkout\">vault service provider</a> (VSP). &nbsp;&nbsp;<b>*Note:* </b>Due to the requirement of having a VSP, this resource is not available in the eBay <a href=\"https://developer.ebay.com/my/api_test_tool?index=0\">API Explorer</a>.</li>  <li><b>guest_purchase_order</b> and <b>purchase_order:</b> Lets eBay partners track the payment status and show the buyers their purchase order. </li> </ul>  # noqa: E501

    OpenAPI spec version: v1_beta.29.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PaymentMethodMessage(object):
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
        'legal_message': 'str',
        'privacy_policy_web_url': 'str',
        'required_for_user_confirmation': 'bool',
        'user_agreement_web_url': 'str'
    }

    attribute_map = {
        'legal_message': 'legalMessage',
        'privacy_policy_web_url': 'privacyPolicyWebUrl',
        'required_for_user_confirmation': 'requiredForUserConfirmation',
        'user_agreement_web_url': 'userAgreementWebUrl'
    }

    def __init__(self, legal_message=None, privacy_policy_web_url=None, required_for_user_confirmation=None, user_agreement_web_url=None):  # noqa: E501
        """PaymentMethodMessage - a model defined in Swagger"""  # noqa: E501
        self._legal_message = None
        self._privacy_policy_web_url = None
        self._required_for_user_confirmation = None
        self._user_agreement_web_url = None
        self.discriminator = None
        if legal_message is not None:
            self.legal_message = legal_message
        if privacy_policy_web_url is not None:
            self.privacy_policy_web_url = privacy_policy_web_url
        if required_for_user_confirmation is not None:
            self.required_for_user_confirmation = required_for_user_confirmation
        if user_agreement_web_url is not None:
            self.user_agreement_web_url = user_agreement_web_url

    @property
    def legal_message(self):
        """Gets the legal_message of this PaymentMethodMessage.  # noqa: E501

        Information that eBay is legally obligated to show to the buyer. This field can be null, in which case do nothing. But if this field is not null, the value of this field must appear on the checkout page. Note: This field is not used for US purchases.  # noqa: E501

        :return: The legal_message of this PaymentMethodMessage.  # noqa: E501
        :rtype: str
        """
        return self._legal_message

    @legal_message.setter
    def legal_message(self, legal_message):
        """Sets the legal_message of this PaymentMethodMessage.

        Information that eBay is legally obligated to show to the buyer. This field can be null, in which case do nothing. But if this field is not null, the value of this field must appear on the checkout page. Note: This field is not used for US purchases.  # noqa: E501

        :param legal_message: The legal_message of this PaymentMethodMessage.  # noqa: E501
        :type: str
        """

        self._legal_message = legal_message

    @property
    def privacy_policy_web_url(self):
        """Gets the privacy_policy_web_url of this PaymentMethodMessage.  # noqa: E501

        Reserved for future use.  # noqa: E501

        :return: The privacy_policy_web_url of this PaymentMethodMessage.  # noqa: E501
        :rtype: str
        """
        return self._privacy_policy_web_url

    @privacy_policy_web_url.setter
    def privacy_policy_web_url(self, privacy_policy_web_url):
        """Sets the privacy_policy_web_url of this PaymentMethodMessage.

        Reserved for future use.  # noqa: E501

        :param privacy_policy_web_url: The privacy_policy_web_url of this PaymentMethodMessage.  # noqa: E501
        :type: str
        """

        self._privacy_policy_web_url = privacy_policy_web_url

    @property
    def required_for_user_confirmation(self):
        """Gets the required_for_user_confirmation of this PaymentMethodMessage.  # noqa: E501

        Reserved for future use.  # noqa: E501

        :return: The required_for_user_confirmation of this PaymentMethodMessage.  # noqa: E501
        :rtype: bool
        """
        return self._required_for_user_confirmation

    @required_for_user_confirmation.setter
    def required_for_user_confirmation(self, required_for_user_confirmation):
        """Sets the required_for_user_confirmation of this PaymentMethodMessage.

        Reserved for future use.  # noqa: E501

        :param required_for_user_confirmation: The required_for_user_confirmation of this PaymentMethodMessage.  # noqa: E501
        :type: bool
        """

        self._required_for_user_confirmation = required_for_user_confirmation

    @property
    def user_agreement_web_url(self):
        """Gets the user_agreement_web_url of this PaymentMethodMessage.  # noqa: E501

        Reserved for future use.  # noqa: E501

        :return: The user_agreement_web_url of this PaymentMethodMessage.  # noqa: E501
        :rtype: str
        """
        return self._user_agreement_web_url

    @user_agreement_web_url.setter
    def user_agreement_web_url(self, user_agreement_web_url):
        """Sets the user_agreement_web_url of this PaymentMethodMessage.

        Reserved for future use.  # noqa: E501

        :param user_agreement_web_url: The user_agreement_web_url of this PaymentMethodMessage.  # noqa: E501
        :type: str
        """

        self._user_agreement_web_url = user_agreement_web_url

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
        if issubclass(PaymentMethodMessage, dict):
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
        if not isinstance(other, PaymentMethodMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other