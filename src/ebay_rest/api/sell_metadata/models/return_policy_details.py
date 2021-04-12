# coding: utf-8

"""
    Metadata API

    The Metadata API has operations that retrieve configuration details pertaining to the different eBay marketplaces. In addition to marketplace information, the API also has operations that get information that helps sellers list items on eBay.  # noqa: E501

    OpenAPI spec version: v1.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ReturnPolicyDetails(object):
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
        'policy_description_enabled': 'bool',
        'refund_methods': 'list[str]',
        'return_methods': 'list[str]',
        'return_periods': 'list[TimeDuration]',
        'returns_acceptance_enabled': 'bool',
        'return_shipping_cost_payers': 'list[str]'
    }

    attribute_map = {
        'policy_description_enabled': 'policyDescriptionEnabled',
        'refund_methods': 'refundMethods',
        'return_methods': 'returnMethods',
        'return_periods': 'returnPeriods',
        'returns_acceptance_enabled': 'returnsAcceptanceEnabled',
        'return_shipping_cost_payers': 'returnShippingCostPayers'
    }

    def __init__(self, policy_description_enabled=None, refund_methods=None, return_methods=None, return_periods=None, returns_acceptance_enabled=None, return_shipping_cost_payers=None):  # noqa: E501
        """ReturnPolicyDetails - a model defined in Swagger"""  # noqa: E501
        self._policy_description_enabled = None
        self._refund_methods = None
        self._return_methods = None
        self._return_periods = None
        self._returns_acceptance_enabled = None
        self._return_shipping_cost_payers = None
        self.discriminator = None
        if policy_description_enabled is not None:
            self.policy_description_enabled = policy_description_enabled
        if refund_methods is not None:
            self.refund_methods = refund_methods
        if return_methods is not None:
            self.return_methods = return_methods
        if return_periods is not None:
            self.return_periods = return_periods
        if returns_acceptance_enabled is not None:
            self.returns_acceptance_enabled = returns_acceptance_enabled
        if return_shipping_cost_payers is not None:
            self.return_shipping_cost_payers = return_shipping_cost_payers

    @property
    def policy_description_enabled(self):
        """Gets the policy_description_enabled of this ReturnPolicyDetails.  # noqa: E501

        If set to true, this flag indicates you can supply a detailed return policy description within your return policy (for example, by populating the returnInstructions field in the Account API's createReturnPolicy). User-supplied return policy details are allowed only in the DE, ES, FR, and IT marketplaces.  # noqa: E501

        :return: The policy_description_enabled of this ReturnPolicyDetails.  # noqa: E501
        :rtype: bool
        """
        return self._policy_description_enabled

    @policy_description_enabled.setter
    def policy_description_enabled(self, policy_description_enabled):
        """Sets the policy_description_enabled of this ReturnPolicyDetails.

        If set to true, this flag indicates you can supply a detailed return policy description within your return policy (for example, by populating the returnInstructions field in the Account API's createReturnPolicy). User-supplied return policy details are allowed only in the DE, ES, FR, and IT marketplaces.  # noqa: E501

        :param policy_description_enabled: The policy_description_enabled of this ReturnPolicyDetails.  # noqa: E501
        :type: bool
        """

        self._policy_description_enabled = policy_description_enabled

    @property
    def refund_methods(self):
        """Gets the refund_methods of this ReturnPolicyDetails.  # noqa: E501

        A list of refund methods allowed for the associated category.  # noqa: E501

        :return: The refund_methods of this ReturnPolicyDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._refund_methods

    @refund_methods.setter
    def refund_methods(self, refund_methods):
        """Sets the refund_methods of this ReturnPolicyDetails.

        A list of refund methods allowed for the associated category.  # noqa: E501

        :param refund_methods: The refund_methods of this ReturnPolicyDetails.  # noqa: E501
        :type: list[str]
        """

        self._refund_methods = refund_methods

    @property
    def return_methods(self):
        """Gets the return_methods of this ReturnPolicyDetails.  # noqa: E501

        A list of return methods allowed for the associated category.  # noqa: E501

        :return: The return_methods of this ReturnPolicyDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._return_methods

    @return_methods.setter
    def return_methods(self, return_methods):
        """Sets the return_methods of this ReturnPolicyDetails.

        A list of return methods allowed for the associated category.  # noqa: E501

        :param return_methods: The return_methods of this ReturnPolicyDetails.  # noqa: E501
        :type: list[str]
        """

        self._return_methods = return_methods

    @property
    def return_periods(self):
        """Gets the return_periods of this ReturnPolicyDetails.  # noqa: E501

        A list of return periods allowed for the associated category. Note that different APIs require you to enter the return period in different ways. For example, the Account API uses the complex TimeDuration type, which takes two values (a unit and a value), whereas the Trading API takes a single value (such as Days_30).  # noqa: E501

        :return: The return_periods of this ReturnPolicyDetails.  # noqa: E501
        :rtype: list[TimeDuration]
        """
        return self._return_periods

    @return_periods.setter
    def return_periods(self, return_periods):
        """Sets the return_periods of this ReturnPolicyDetails.

        A list of return periods allowed for the associated category. Note that different APIs require you to enter the return period in different ways. For example, the Account API uses the complex TimeDuration type, which takes two values (a unit and a value), whereas the Trading API takes a single value (such as Days_30).  # noqa: E501

        :param return_periods: The return_periods of this ReturnPolicyDetails.  # noqa: E501
        :type: list[TimeDuration]
        """

        self._return_periods = return_periods

    @property
    def returns_acceptance_enabled(self):
        """Gets the returns_acceptance_enabled of this ReturnPolicyDetails.  # noqa: E501

        If set to true, this flag indicates the seller can configure how they handle domestic returns.  # noqa: E501

        :return: The returns_acceptance_enabled of this ReturnPolicyDetails.  # noqa: E501
        :rtype: bool
        """
        return self._returns_acceptance_enabled

    @returns_acceptance_enabled.setter
    def returns_acceptance_enabled(self, returns_acceptance_enabled):
        """Sets the returns_acceptance_enabled of this ReturnPolicyDetails.

        If set to true, this flag indicates the seller can configure how they handle domestic returns.  # noqa: E501

        :param returns_acceptance_enabled: The returns_acceptance_enabled of this ReturnPolicyDetails.  # noqa: E501
        :type: bool
        """

        self._returns_acceptance_enabled = returns_acceptance_enabled

    @property
    def return_shipping_cost_payers(self):
        """Gets the return_shipping_cost_payers of this ReturnPolicyDetails.  # noqa: E501

        A list of allowed values for who pays for the return shipping cost. Note that for SNAD returns, the seller is always responsible for the return shipping cost.  # noqa: E501

        :return: The return_shipping_cost_payers of this ReturnPolicyDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._return_shipping_cost_payers

    @return_shipping_cost_payers.setter
    def return_shipping_cost_payers(self, return_shipping_cost_payers):
        """Sets the return_shipping_cost_payers of this ReturnPolicyDetails.

        A list of allowed values for who pays for the return shipping cost. Note that for SNAD returns, the seller is always responsible for the return shipping cost.  # noqa: E501

        :param return_shipping_cost_payers: The return_shipping_cost_payers of this ReturnPolicyDetails.  # noqa: E501
        :type: list[str]
        """

        self._return_shipping_cost_payers = return_shipping_cost_payers

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
        if issubclass(ReturnPolicyDetails, dict):
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
        if not isinstance(other, ReturnPolicyDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other