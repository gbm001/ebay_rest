# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (the Fulfillment Policy, Payment Policy, and Return Policy), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br><br>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.6.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ShippingOption(object):
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
        'cost_type': 'str',
        'insurance_fee': 'Amount',
        'insurance_offered': 'bool',
        'option_type': 'str',
        'package_handling_cost': 'Amount',
        'rate_table_id': 'str',
        'shipping_services': 'list[ShippingService]'
    }

    attribute_map = {
        'cost_type': 'costType',
        'insurance_fee': 'insuranceFee',
        'insurance_offered': 'insuranceOffered',
        'option_type': 'optionType',
        'package_handling_cost': 'packageHandlingCost',
        'rate_table_id': 'rateTableId',
        'shipping_services': 'shippingServices'
    }

    def __init__(self, cost_type=None, insurance_fee=None, insurance_offered=None, option_type=None, package_handling_cost=None, rate_table_id=None, shipping_services=None):  # noqa: E501
        """ShippingOption - a model defined in Swagger"""  # noqa: E501
        self._cost_type = None
        self._insurance_fee = None
        self._insurance_offered = None
        self._option_type = None
        self._package_handling_cost = None
        self._rate_table_id = None
        self._shipping_services = None
        self.discriminator = None
        if cost_type is not None:
            self.cost_type = cost_type
        if insurance_fee is not None:
            self.insurance_fee = insurance_fee
        if insurance_offered is not None:
            self.insurance_offered = insurance_offered
        if option_type is not None:
            self.option_type = option_type
        if package_handling_cost is not None:
            self.package_handling_cost = package_handling_cost
        if rate_table_id is not None:
            self.rate_table_id = rate_table_id
        if shipping_services is not None:
            self.shipping_services = shipping_services

    @property
    def cost_type(self):
        """Gets the cost_type of this ShippingOption.  # noqa: E501

        Defines whether the shipping cost is FLAT_RATE (the same rate for all buyers), CALCULATED (the shipping rate varies by the ship-to location and size and weight of the package, as defined by the item), or NOT_SPECIFIED (for use with local pickup). Required if the policy offers shipping options using a shippingOptions container. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:ShippingCostTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The cost_type of this ShippingOption.  # noqa: E501
        :rtype: str
        """
        return self._cost_type

    @cost_type.setter
    def cost_type(self, cost_type):
        """Sets the cost_type of this ShippingOption.

        Defines whether the shipping cost is FLAT_RATE (the same rate for all buyers), CALCULATED (the shipping rate varies by the ship-to location and size and weight of the package, as defined by the item), or NOT_SPECIFIED (for use with local pickup). Required if the policy offers shipping options using a shippingOptions container. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:ShippingCostTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param cost_type: The cost_type of this ShippingOption.  # noqa: E501
        :type: str
        """

        self._cost_type = cost_type

    @property
    def insurance_fee(self):
        """Gets the insurance_fee of this ShippingOption.  # noqa: E501


        :return: The insurance_fee of this ShippingOption.  # noqa: E501
        :rtype: Amount
        """
        return self._insurance_fee

    @insurance_fee.setter
    def insurance_fee(self, insurance_fee):
        """Sets the insurance_fee of this ShippingOption.


        :param insurance_fee: The insurance_fee of this ShippingOption.  # noqa: E501
        :type: Amount
        """

        self._insurance_fee = insurance_fee

    @property
    def insurance_offered(self):
        """Gets the insurance_offered of this ShippingOption.  # noqa: E501

        This field has been deprecated. Shipping insurance is offered only via a shipping carrier's shipping services and is no longer available via eBay shipping policies.  # noqa: E501

        :return: The insurance_offered of this ShippingOption.  # noqa: E501
        :rtype: bool
        """
        return self._insurance_offered

    @insurance_offered.setter
    def insurance_offered(self, insurance_offered):
        """Sets the insurance_offered of this ShippingOption.

        This field has been deprecated. Shipping insurance is offered only via a shipping carrier's shipping services and is no longer available via eBay shipping policies.  # noqa: E501

        :param insurance_offered: The insurance_offered of this ShippingOption.  # noqa: E501
        :type: bool
        """

        self._insurance_offered = insurance_offered

    @property
    def option_type(self):
        """Gets the option_type of this ShippingOption.  # noqa: E501

        Use this field to set the ShippingOption element to either DOMESTIC or INTERNATIONAL. Required if the policy offers shipping options using a shippingOptions container. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:ShippingOptionTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The option_type of this ShippingOption.  # noqa: E501
        :rtype: str
        """
        return self._option_type

    @option_type.setter
    def option_type(self, option_type):
        """Sets the option_type of this ShippingOption.

        Use this field to set the ShippingOption element to either DOMESTIC or INTERNATIONAL. Required if the policy offers shipping options using a shippingOptions container. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:ShippingOptionTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param option_type: The option_type of this ShippingOption.  # noqa: E501
        :type: str
        """

        self._option_type = option_type

    @property
    def package_handling_cost(self):
        """Gets the package_handling_cost of this ShippingOption.  # noqa: E501


        :return: The package_handling_cost of this ShippingOption.  # noqa: E501
        :rtype: Amount
        """
        return self._package_handling_cost

    @package_handling_cost.setter
    def package_handling_cost(self, package_handling_cost):
        """Sets the package_handling_cost of this ShippingOption.


        :param package_handling_cost: The package_handling_cost of this ShippingOption.  # noqa: E501
        :type: Amount
        """

        self._package_handling_cost = package_handling_cost

    @property
    def rate_table_id(self):
        """Gets the rate_table_id of this ShippingOption.  # noqa: E501

        A unique eBay-assigned ID associated with a user-created shipping rate table. The locality of a shipping rate table can be either DOMESTIC or INTERNATIONAL and you must ensure the value specified in this field references a shipping rate table that matches the type specified in the shippingOptions.optionType field. If you mismatch the types, eBay responds with a 20403 error. Call getRateTable to retrieve information (including rateTableId values) on the rate tables configured by a seller. For information on creating rate tables, see Using shipping rate tables.  # noqa: E501

        :return: The rate_table_id of this ShippingOption.  # noqa: E501
        :rtype: str
        """
        return self._rate_table_id

    @rate_table_id.setter
    def rate_table_id(self, rate_table_id):
        """Sets the rate_table_id of this ShippingOption.

        A unique eBay-assigned ID associated with a user-created shipping rate table. The locality of a shipping rate table can be either DOMESTIC or INTERNATIONAL and you must ensure the value specified in this field references a shipping rate table that matches the type specified in the shippingOptions.optionType field. If you mismatch the types, eBay responds with a 20403 error. Call getRateTable to retrieve information (including rateTableId values) on the rate tables configured by a seller. For information on creating rate tables, see Using shipping rate tables.  # noqa: E501

        :param rate_table_id: The rate_table_id of this ShippingOption.  # noqa: E501
        :type: str
        """

        self._rate_table_id = rate_table_id

    @property
    def shipping_services(self):
        """Gets the shipping_services of this ShippingOption.  # noqa: E501

        Contains a list of shipping services offered for either DOMESTIC or INTERNATIONAL shipments. Sellers can specify up to four domestic shipping services and up to five international shipping services by using separate shippingService containers for each. Note that if the seller is opted in to the Global Shipping Program, they can specify only four other international shipping services, regardless of whether or not Global Shipping is offered as one of the services. Required if the policy offers shipping options using a shippingOptions container.  # noqa: E501

        :return: The shipping_services of this ShippingOption.  # noqa: E501
        :rtype: list[ShippingService]
        """
        return self._shipping_services

    @shipping_services.setter
    def shipping_services(self, shipping_services):
        """Sets the shipping_services of this ShippingOption.

        Contains a list of shipping services offered for either DOMESTIC or INTERNATIONAL shipments. Sellers can specify up to four domestic shipping services and up to five international shipping services by using separate shippingService containers for each. Note that if the seller is opted in to the Global Shipping Program, they can specify only four other international shipping services, regardless of whether or not Global Shipping is offered as one of the services. Required if the policy offers shipping options using a shippingOptions container.  # noqa: E501

        :param shipping_services: The shipping_services of this ShippingOption.  # noqa: E501
        :type: list[ShippingService]
        """

        self._shipping_services = shipping_services

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
        if issubclass(ShippingOption, dict):
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
        if not isinstance(other, ShippingOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
