# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (eBay business policies and seller-defined custom policies), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br/><br/>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SetFulfillmentPolicyResponse(object):
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
        'category_types': 'list[CategoryType]',
        'description': 'str',
        'freight_shipping': 'bool',
        'fulfillment_policy_id': 'str',
        'global_shipping': 'bool',
        'handling_time': 'TimeDuration',
        'local_pickup': 'bool',
        'marketplace_id': 'str',
        'name': 'str',
        'pickup_drop_off': 'bool',
        'shipping_options': 'list[ShippingOption]',
        'ship_to_locations': 'RegionSet',
        'warnings': 'list[Error]'
    }

    attribute_map = {
        'category_types': 'categoryTypes',
        'description': 'description',
        'freight_shipping': 'freightShipping',
        'fulfillment_policy_id': 'fulfillmentPolicyId',
        'global_shipping': 'globalShipping',
        'handling_time': 'handlingTime',
        'local_pickup': 'localPickup',
        'marketplace_id': 'marketplaceId',
        'name': 'name',
        'pickup_drop_off': 'pickupDropOff',
        'shipping_options': 'shippingOptions',
        'ship_to_locations': 'shipToLocations',
        'warnings': 'warnings'
    }

    def __init__(self, category_types=None, description=None, freight_shipping=None, fulfillment_policy_id=None, global_shipping=None, handling_time=None, local_pickup=None, marketplace_id=None, name=None, pickup_drop_off=None, shipping_options=None, ship_to_locations=None, warnings=None):  # noqa: E501
        """SetFulfillmentPolicyResponse - a model defined in Swagger"""  # noqa: E501
        self._category_types = None
        self._description = None
        self._freight_shipping = None
        self._fulfillment_policy_id = None
        self._global_shipping = None
        self._handling_time = None
        self._local_pickup = None
        self._marketplace_id = None
        self._name = None
        self._pickup_drop_off = None
        self._shipping_options = None
        self._ship_to_locations = None
        self._warnings = None
        self.discriminator = None
        if category_types is not None:
            self.category_types = category_types
        if description is not None:
            self.description = description
        if freight_shipping is not None:
            self.freight_shipping = freight_shipping
        if fulfillment_policy_id is not None:
            self.fulfillment_policy_id = fulfillment_policy_id
        if global_shipping is not None:
            self.global_shipping = global_shipping
        if handling_time is not None:
            self.handling_time = handling_time
        if local_pickup is not None:
            self.local_pickup = local_pickup
        if marketplace_id is not None:
            self.marketplace_id = marketplace_id
        if name is not None:
            self.name = name
        if pickup_drop_off is not None:
            self.pickup_drop_off = pickup_drop_off
        if shipping_options is not None:
            self.shipping_options = shipping_options
        if ship_to_locations is not None:
            self.ship_to_locations = ship_to_locations
        if warnings is not None:
            self.warnings = warnings

    @property
    def category_types(self):
        """Gets the category_types of this SetFulfillmentPolicyResponse.  # noqa: E501

        This container indicates whether the fulfillment business policy applies to motor vehicle listings, or if it applies to non-motor vehicle listings.  # noqa: E501

        :return: The category_types of this SetFulfillmentPolicyResponse.  # noqa: E501
        :rtype: list[CategoryType]
        """
        return self._category_types

    @category_types.setter
    def category_types(self, category_types):
        """Sets the category_types of this SetFulfillmentPolicyResponse.

        This container indicates whether the fulfillment business policy applies to motor vehicle listings, or if it applies to non-motor vehicle listings.  # noqa: E501

        :param category_types: The category_types of this SetFulfillmentPolicyResponse.  # noqa: E501
        :type: list[CategoryType]
        """

        self._category_types = category_types

    @property
    def description(self):
        """Gets the description of this SetFulfillmentPolicyResponse.  # noqa: E501

        A seller-defined description of the fulfillment policy. This description is only for the seller's use, and is not exposed on any eBay pages. This field is returned if set for the policy. <br/><br/><b>Max length</b>: 250  # noqa: E501

        :return: The description of this SetFulfillmentPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SetFulfillmentPolicyResponse.

        A seller-defined description of the fulfillment policy. This description is only for the seller's use, and is not exposed on any eBay pages. This field is returned if set for the policy. <br/><br/><b>Max length</b>: 250  # noqa: E501

        :param description: The description of this SetFulfillmentPolicyResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def freight_shipping(self):
        """Gets the freight_shipping of this SetFulfillmentPolicyResponse.  # noqa: E501

        If returned as <code>true</code>, the seller offers freight shipping. Freight shipping can be used for large items over 150 lbs.  # noqa: E501

        :return: The freight_shipping of this SetFulfillmentPolicyResponse.  # noqa: E501
        :rtype: bool
        """
        return self._freight_shipping

    @freight_shipping.setter
    def freight_shipping(self, freight_shipping):
        """Sets the freight_shipping of this SetFulfillmentPolicyResponse.

        If returned as <code>true</code>, the seller offers freight shipping. Freight shipping can be used for large items over 150 lbs.  # noqa: E501

        :param freight_shipping: The freight_shipping of this SetFulfillmentPolicyResponse.  # noqa: E501
        :type: bool
        """

        self._freight_shipping = freight_shipping

    @property
    def fulfillment_policy_id(self):
        """Gets the fulfillment_policy_id of this SetFulfillmentPolicyResponse.  # noqa: E501

        A unique eBay-assigned ID for a fulfillment business policy. This ID is generated when the policy is created.  # noqa: E501

        :return: The fulfillment_policy_id of this SetFulfillmentPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._fulfillment_policy_id

    @fulfillment_policy_id.setter
    def fulfillment_policy_id(self, fulfillment_policy_id):
        """Sets the fulfillment_policy_id of this SetFulfillmentPolicyResponse.

        A unique eBay-assigned ID for a fulfillment business policy. This ID is generated when the policy is created.  # noqa: E501

        :param fulfillment_policy_id: The fulfillment_policy_id of this SetFulfillmentPolicyResponse.  # noqa: E501
        :type: str
        """

        self._fulfillment_policy_id = fulfillment_policy_id

    @property
    def global_shipping(self):
        """Gets the global_shipping of this SetFulfillmentPolicyResponse.  # noqa: E501

        If returned as <code>true</code>, eBay's Global Shipping Program will be used by the seller to ship items to international locations.  # noqa: E501

        :return: The global_shipping of this SetFulfillmentPolicyResponse.  # noqa: E501
        :rtype: bool
        """
        return self._global_shipping

    @global_shipping.setter
    def global_shipping(self, global_shipping):
        """Sets the global_shipping of this SetFulfillmentPolicyResponse.

        If returned as <code>true</code>, eBay's Global Shipping Program will be used by the seller to ship items to international locations.  # noqa: E501

        :param global_shipping: The global_shipping of this SetFulfillmentPolicyResponse.  # noqa: E501
        :type: bool
        """

        self._global_shipping = global_shipping

    @property
    def handling_time(self):
        """Gets the handling_time of this SetFulfillmentPolicyResponse.  # noqa: E501


        :return: The handling_time of this SetFulfillmentPolicyResponse.  # noqa: E501
        :rtype: TimeDuration
        """
        return self._handling_time

    @handling_time.setter
    def handling_time(self, handling_time):
        """Sets the handling_time of this SetFulfillmentPolicyResponse.


        :param handling_time: The handling_time of this SetFulfillmentPolicyResponse.  # noqa: E501
        :type: TimeDuration
        """

        self._handling_time = handling_time

    @property
    def local_pickup(self):
        """Gets the local_pickup of this SetFulfillmentPolicyResponse.  # noqa: E501

        If returned as <code>true</code>, local pickup is available for this policy.  # noqa: E501

        :return: The local_pickup of this SetFulfillmentPolicyResponse.  # noqa: E501
        :rtype: bool
        """
        return self._local_pickup

    @local_pickup.setter
    def local_pickup(self, local_pickup):
        """Sets the local_pickup of this SetFulfillmentPolicyResponse.

        If returned as <code>true</code>, local pickup is available for this policy.  # noqa: E501

        :param local_pickup: The local_pickup of this SetFulfillmentPolicyResponse.  # noqa: E501
        :type: bool
        """

        self._local_pickup = local_pickup

    @property
    def marketplace_id(self):
        """Gets the marketplace_id of this SetFulfillmentPolicyResponse.  # noqa: E501

        The ID of the eBay marketplace to which this fulfillment business policy applies. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :return: The marketplace_id of this SetFulfillmentPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._marketplace_id

    @marketplace_id.setter
    def marketplace_id(self, marketplace_id):
        """Sets the marketplace_id of this SetFulfillmentPolicyResponse.

        The ID of the eBay marketplace to which this fulfillment business policy applies. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :param marketplace_id: The marketplace_id of this SetFulfillmentPolicyResponse.  # noqa: E501
        :type: str
        """

        self._marketplace_id = marketplace_id

    @property
    def name(self):
        """Gets the name of this SetFulfillmentPolicyResponse.  # noqa: E501

        A seller-defined name for this fulfillment business policy. Names must be unique for policies assigned to the same marketplace. <br/><br/><b>Max length</b>: 64  # noqa: E501

        :return: The name of this SetFulfillmentPolicyResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SetFulfillmentPolicyResponse.

        A seller-defined name for this fulfillment business policy. Names must be unique for policies assigned to the same marketplace. <br/><br/><b>Max length</b>: 64  # noqa: E501

        :param name: The name of this SetFulfillmentPolicyResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pickup_drop_off(self):
        """Gets the pickup_drop_off of this SetFulfillmentPolicyResponse.  # noqa: E501

        If returned as <code>true</code>, the seller offers the \"Click and Collect\" option. <br/><br/>Currently, \"Click and Collect\" is available only to large retail merchants the eBay AU and UK marketplaces.  # noqa: E501

        :return: The pickup_drop_off of this SetFulfillmentPolicyResponse.  # noqa: E501
        :rtype: bool
        """
        return self._pickup_drop_off

    @pickup_drop_off.setter
    def pickup_drop_off(self, pickup_drop_off):
        """Sets the pickup_drop_off of this SetFulfillmentPolicyResponse.

        If returned as <code>true</code>, the seller offers the \"Click and Collect\" option. <br/><br/>Currently, \"Click and Collect\" is available only to large retail merchants the eBay AU and UK marketplaces.  # noqa: E501

        :param pickup_drop_off: The pickup_drop_off of this SetFulfillmentPolicyResponse.  # noqa: E501
        :type: bool
        """

        self._pickup_drop_off = pickup_drop_off

    @property
    def shipping_options(self):
        """Gets the shipping_options of this SetFulfillmentPolicyResponse.  # noqa: E501

        This array is used to provide detailed information on the domestic and international shipping options available for the policy. A separate <b>ShippingOption</b> object covers domestic shipping service options and international shipping service options (if the seller ships to international locations). The <b>optionType</b> field indicates whether the <b>ShippingOption</b> object applies to domestic or international shipping, and the <b>costType</b> field indicates whether flat-rate shipping or calculated shipping will be used. <p>A separate <b>ShippingServices</b> object is used to specify cost and other details for every available domestic and international shipping service option. </p>  # noqa: E501

        :return: The shipping_options of this SetFulfillmentPolicyResponse.  # noqa: E501
        :rtype: list[ShippingOption]
        """
        return self._shipping_options

    @shipping_options.setter
    def shipping_options(self, shipping_options):
        """Sets the shipping_options of this SetFulfillmentPolicyResponse.

        This array is used to provide detailed information on the domestic and international shipping options available for the policy. A separate <b>ShippingOption</b> object covers domestic shipping service options and international shipping service options (if the seller ships to international locations). The <b>optionType</b> field indicates whether the <b>ShippingOption</b> object applies to domestic or international shipping, and the <b>costType</b> field indicates whether flat-rate shipping or calculated shipping will be used. <p>A separate <b>ShippingServices</b> object is used to specify cost and other details for every available domestic and international shipping service option. </p>  # noqa: E501

        :param shipping_options: The shipping_options of this SetFulfillmentPolicyResponse.  # noqa: E501
        :type: list[ShippingOption]
        """

        self._shipping_options = shipping_options

    @property
    def ship_to_locations(self):
        """Gets the ship_to_locations of this SetFulfillmentPolicyResponse.  # noqa: E501


        :return: The ship_to_locations of this SetFulfillmentPolicyResponse.  # noqa: E501
        :rtype: RegionSet
        """
        return self._ship_to_locations

    @ship_to_locations.setter
    def ship_to_locations(self, ship_to_locations):
        """Sets the ship_to_locations of this SetFulfillmentPolicyResponse.


        :param ship_to_locations: The ship_to_locations of this SetFulfillmentPolicyResponse.  # noqa: E501
        :type: RegionSet
        """

        self._ship_to_locations = ship_to_locations

    @property
    def warnings(self):
        """Gets the warnings of this SetFulfillmentPolicyResponse.  # noqa: E501

        An array of one or more errors or warnings that were generated during the processing of the request. If there were no issues with the request, this array will return empty.  # noqa: E501

        :return: The warnings of this SetFulfillmentPolicyResponse.  # noqa: E501
        :rtype: list[Error]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this SetFulfillmentPolicyResponse.

        An array of one or more errors or warnings that were generated during the processing of the request. If there were no issues with the request, this array will return empty.  # noqa: E501

        :param warnings: The warnings of this SetFulfillmentPolicyResponse.  # noqa: E501
        :type: list[Error]
        """

        self._warnings = warnings

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
        if issubclass(SetFulfillmentPolicyResponse, dict):
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
        if not isinstance(other, SetFulfillmentPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
