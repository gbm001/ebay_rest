# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.16.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ListingPolicies(object):
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
        'best_offer_terms': 'BestOffer',
        'e_bay_plus_if_eligible': 'bool',
        'fulfillment_policy_id': 'str',
        'payment_policy_id': 'str',
        'product_compliance_policy_ids': 'list[str]',
        'return_policy_id': 'str',
        'shipping_cost_overrides': 'list[ShippingCostOverride]',
        'take_back_policy_id': 'str'
    }

    attribute_map = {
        'best_offer_terms': 'bestOfferTerms',
        'e_bay_plus_if_eligible': 'eBayPlusIfEligible',
        'fulfillment_policy_id': 'fulfillmentPolicyId',
        'payment_policy_id': 'paymentPolicyId',
        'product_compliance_policy_ids': 'productCompliancePolicyIds',
        'return_policy_id': 'returnPolicyId',
        'shipping_cost_overrides': 'shippingCostOverrides',
        'take_back_policy_id': 'takeBackPolicyId'
    }

    def __init__(self, best_offer_terms=None, e_bay_plus_if_eligible=None, fulfillment_policy_id=None, payment_policy_id=None, product_compliance_policy_ids=None, return_policy_id=None, shipping_cost_overrides=None, take_back_policy_id=None):  # noqa: E501
        """ListingPolicies - a model defined in Swagger"""  # noqa: E501
        self._best_offer_terms = None
        self._e_bay_plus_if_eligible = None
        self._fulfillment_policy_id = None
        self._payment_policy_id = None
        self._product_compliance_policy_ids = None
        self._return_policy_id = None
        self._shipping_cost_overrides = None
        self._take_back_policy_id = None
        self.discriminator = None
        if best_offer_terms is not None:
            self.best_offer_terms = best_offer_terms
        if e_bay_plus_if_eligible is not None:
            self.e_bay_plus_if_eligible = e_bay_plus_if_eligible
        if fulfillment_policy_id is not None:
            self.fulfillment_policy_id = fulfillment_policy_id
        if payment_policy_id is not None:
            self.payment_policy_id = payment_policy_id
        if product_compliance_policy_ids is not None:
            self.product_compliance_policy_ids = product_compliance_policy_ids
        if return_policy_id is not None:
            self.return_policy_id = return_policy_id
        if shipping_cost_overrides is not None:
            self.shipping_cost_overrides = shipping_cost_overrides
        if take_back_policy_id is not None:
            self.take_back_policy_id = take_back_policy_id

    @property
    def best_offer_terms(self):
        """Gets the best_offer_terms of this ListingPolicies.  # noqa: E501


        :return: The best_offer_terms of this ListingPolicies.  # noqa: E501
        :rtype: BestOffer
        """
        return self._best_offer_terms

    @best_offer_terms.setter
    def best_offer_terms(self, best_offer_terms):
        """Sets the best_offer_terms of this ListingPolicies.


        :param best_offer_terms: The best_offer_terms of this ListingPolicies.  # noqa: E501
        :type: BestOffer
        """

        self._best_offer_terms = best_offer_terms

    @property
    def e_bay_plus_if_eligible(self):
        """Gets the e_bay_plus_if_eligible of this ListingPolicies.  # noqa: E501

        This field is included in an offer and set to <code>true</code> if a Top-Rated seller is opted in to the eBay Plus program. With the eBay Plus program, qualified sellers must commit to next-day delivery of the item, and the buyers must have an eBay Plus subscription to be eligible to receive the benefits of this program, which are free, next-day delivery, as well as free returns.<br><br>Currently, this program is only available on the Germany and Australian sites.<br/><br/>This field will be returned in the <strong>getOffer</strong> and <strong>getOffers</strong> calls if set for the offer.  # noqa: E501

        :return: The e_bay_plus_if_eligible of this ListingPolicies.  # noqa: E501
        :rtype: bool
        """
        return self._e_bay_plus_if_eligible

    @e_bay_plus_if_eligible.setter
    def e_bay_plus_if_eligible(self, e_bay_plus_if_eligible):
        """Sets the e_bay_plus_if_eligible of this ListingPolicies.

        This field is included in an offer and set to <code>true</code> if a Top-Rated seller is opted in to the eBay Plus program. With the eBay Plus program, qualified sellers must commit to next-day delivery of the item, and the buyers must have an eBay Plus subscription to be eligible to receive the benefits of this program, which are free, next-day delivery, as well as free returns.<br><br>Currently, this program is only available on the Germany and Australian sites.<br/><br/>This field will be returned in the <strong>getOffer</strong> and <strong>getOffers</strong> calls if set for the offer.  # noqa: E501

        :param e_bay_plus_if_eligible: The e_bay_plus_if_eligible of this ListingPolicies.  # noqa: E501
        :type: bool
        """

        self._e_bay_plus_if_eligible = e_bay_plus_if_eligible

    @property
    def fulfillment_policy_id(self):
        """Gets the fulfillment_policy_id of this ListingPolicies.  # noqa: E501

        This unique identifier indicates the fulfillment business policy that will be used once an offer is published and converted to an eBay listing. This fulfillment business policy will set all fulfillment-related settings for the eBay listing.<br/><br/>Business policies are not immediately required for offers, but are required before an offer can be published. The seller should review the fulfillment business policy before assigning it to the offer to make sure it is compatible with the inventory item and the offer settings. The seller may also want to review the shipping service costs in the fulfillment policy, and that seller might decide to override the shipping costs for one or more shipping service options by using the <strong>shippingCostOverrides</strong> container.<br/><br/>Business policies can be created and managed in My eBay or with the <strong>Account API</strong>. To get a list of all return policies associated with a seller's account on a specific eBay Marketplace, use the Account API's <strong>getFulfillmentPolicies</strong> call. There are also calls in the <strong>Account API</strong> to retrieve a fulfillment policy by policy ID or policy name.<br/><br/>This field will be returned in the <strong>getOffer</strong> and <strong>getOffers</strong> calls if set for the offer.  # noqa: E501

        :return: The fulfillment_policy_id of this ListingPolicies.  # noqa: E501
        :rtype: str
        """
        return self._fulfillment_policy_id

    @fulfillment_policy_id.setter
    def fulfillment_policy_id(self, fulfillment_policy_id):
        """Sets the fulfillment_policy_id of this ListingPolicies.

        This unique identifier indicates the fulfillment business policy that will be used once an offer is published and converted to an eBay listing. This fulfillment business policy will set all fulfillment-related settings for the eBay listing.<br/><br/>Business policies are not immediately required for offers, but are required before an offer can be published. The seller should review the fulfillment business policy before assigning it to the offer to make sure it is compatible with the inventory item and the offer settings. The seller may also want to review the shipping service costs in the fulfillment policy, and that seller might decide to override the shipping costs for one or more shipping service options by using the <strong>shippingCostOverrides</strong> container.<br/><br/>Business policies can be created and managed in My eBay or with the <strong>Account API</strong>. To get a list of all return policies associated with a seller's account on a specific eBay Marketplace, use the Account API's <strong>getFulfillmentPolicies</strong> call. There are also calls in the <strong>Account API</strong> to retrieve a fulfillment policy by policy ID or policy name.<br/><br/>This field will be returned in the <strong>getOffer</strong> and <strong>getOffers</strong> calls if set for the offer.  # noqa: E501

        :param fulfillment_policy_id: The fulfillment_policy_id of this ListingPolicies.  # noqa: E501
        :type: str
        """

        self._fulfillment_policy_id = fulfillment_policy_id

    @property
    def payment_policy_id(self):
        """Gets the payment_policy_id of this ListingPolicies.  # noqa: E501

        This unique identifier indicates the payment business policy that will be used once an offer is published and converted to an eBay listing. This payment business policy will set all payment-related settings for the eBay listing.<br/><br/>Business policies are not immediately required for offers, but are required before an offer can be published. The seller should review the payment business policy to make sure that it is compatible with the marketplace and listing category before assigning it to the offer.<br /><br />Business policies can be created and managed in My eBay or with the <strong>Account API</strong>. To get a list of all payment policies associated with a seller's account on a specific eBay Marketplace, use the Account API's <strong>getPaymentPolicies</strong> call. There are also calls in the <strong>Account API</strong> to retrieve a payment policy by policy ID or policy name.<br/><br/>This field will be returned in the <strong>getOffer</strong> and <strong>getOffers</strong> calls if set for the offer.  # noqa: E501

        :return: The payment_policy_id of this ListingPolicies.  # noqa: E501
        :rtype: str
        """
        return self._payment_policy_id

    @payment_policy_id.setter
    def payment_policy_id(self, payment_policy_id):
        """Sets the payment_policy_id of this ListingPolicies.

        This unique identifier indicates the payment business policy that will be used once an offer is published and converted to an eBay listing. This payment business policy will set all payment-related settings for the eBay listing.<br/><br/>Business policies are not immediately required for offers, but are required before an offer can be published. The seller should review the payment business policy to make sure that it is compatible with the marketplace and listing category before assigning it to the offer.<br /><br />Business policies can be created and managed in My eBay or with the <strong>Account API</strong>. To get a list of all payment policies associated with a seller's account on a specific eBay Marketplace, use the Account API's <strong>getPaymentPolicies</strong> call. There are also calls in the <strong>Account API</strong> to retrieve a payment policy by policy ID or policy name.<br/><br/>This field will be returned in the <strong>getOffer</strong> and <strong>getOffers</strong> calls if set for the offer.  # noqa: E501

        :param payment_policy_id: The payment_policy_id of this ListingPolicies.  # noqa: E501
        :type: str
        """

        self._payment_policy_id = payment_policy_id

    @property
    def product_compliance_policy_ids(self):
        """Gets the product_compliance_policy_ids of this ListingPolicies.  # noqa: E501

        This field contains an array of up to five IDs specifying the seller created compliance policies for the listing. Custom policies provide buyers with important information and disclosures about products. For example, if you sell batteries and specific disclosures are required, your compliance policy could contain the required disclosures. See <a href=\"https://www.ebay.com/help/selling/custom-policies/custom-policies?id=5311\" target=\"_blank\">Custom Policies</a> for more information. Up to five different compliance policies can be applied to each listing. Refer to the <a href=\"/api-docs/sell/account/resources/methods#h2-custom_policy \">custom_policy</a> resource (in the <strong>Sell Account API</strong>) to create and manage custom policies.  # noqa: E501

        :return: The product_compliance_policy_ids of this ListingPolicies.  # noqa: E501
        :rtype: list[str]
        """
        return self._product_compliance_policy_ids

    @product_compliance_policy_ids.setter
    def product_compliance_policy_ids(self, product_compliance_policy_ids):
        """Sets the product_compliance_policy_ids of this ListingPolicies.

        This field contains an array of up to five IDs specifying the seller created compliance policies for the listing. Custom policies provide buyers with important information and disclosures about products. For example, if you sell batteries and specific disclosures are required, your compliance policy could contain the required disclosures. See <a href=\"https://www.ebay.com/help/selling/custom-policies/custom-policies?id=5311\" target=\"_blank\">Custom Policies</a> for more information. Up to five different compliance policies can be applied to each listing. Refer to the <a href=\"/api-docs/sell/account/resources/methods#h2-custom_policy \">custom_policy</a> resource (in the <strong>Sell Account API</strong>) to create and manage custom policies.  # noqa: E501

        :param product_compliance_policy_ids: The product_compliance_policy_ids of this ListingPolicies.  # noqa: E501
        :type: list[str]
        """

        self._product_compliance_policy_ids = product_compliance_policy_ids

    @property
    def return_policy_id(self):
        """Gets the return_policy_id of this ListingPolicies.  # noqa: E501

        This unique identifier indicates the return business policy that will be used once an offer is published and converted to an eBay listing. This return business policy will set all return policy settings for the eBay listing.<br/><br/>Business policies are not immediately required for offers, but are required before an offer can be published. The seller should review the return business policy before assigning it to the offer to make sure it is compatible with the inventory item and the offer settings.<br/><br/>Business policies can be created and managed in My eBay or with the <strong>Account API</strong>. To get a list of all return policies associated with a seller's account on a specific eBay Marketplace, use the Account API's <strong>getReturnPolicies</strong> call. There are also calls in the <strong>Account API</strong> to retrieve a return policy by policy ID or policy name.<br/><br/>This field will be returned in the <strong>getOffer</strong> and <strong>getOffers</strong> calls if set for the offer.  # noqa: E501

        :return: The return_policy_id of this ListingPolicies.  # noqa: E501
        :rtype: str
        """
        return self._return_policy_id

    @return_policy_id.setter
    def return_policy_id(self, return_policy_id):
        """Sets the return_policy_id of this ListingPolicies.

        This unique identifier indicates the return business policy that will be used once an offer is published and converted to an eBay listing. This return business policy will set all return policy settings for the eBay listing.<br/><br/>Business policies are not immediately required for offers, but are required before an offer can be published. The seller should review the return business policy before assigning it to the offer to make sure it is compatible with the inventory item and the offer settings.<br/><br/>Business policies can be created and managed in My eBay or with the <strong>Account API</strong>. To get a list of all return policies associated with a seller's account on a specific eBay Marketplace, use the Account API's <strong>getReturnPolicies</strong> call. There are also calls in the <strong>Account API</strong> to retrieve a return policy by policy ID or policy name.<br/><br/>This field will be returned in the <strong>getOffer</strong> and <strong>getOffers</strong> calls if set for the offer.  # noqa: E501

        :param return_policy_id: The return_policy_id of this ListingPolicies.  # noqa: E501
        :type: str
        """

        self._return_policy_id = return_policy_id

    @property
    def shipping_cost_overrides(self):
        """Gets the shipping_cost_overrides of this ListingPolicies.  # noqa: E501

        This container is used if the seller wishes to override the shipping costs or surcharge for one or more domestic or international shipping service options defined in the fulfillment listing policy. To override the costs of a specific domestic or international shipping service option, the seller must know the priority/order of that shipping service in the fulfillment listing policy. The name of a shipping service option can be found in the <strong>shippingOptions.shippingServices.shippingServiceCode</strong> field of the fulfillment policy, and the priority/order of that shipping service option is found in the <strong>shippingOptions.shippingServices.sortOrderId</strong> field. Both of these values can be retrieved by searching for that fulfillment policy with the <strong>getFulfillmentPolicies</strong> or <strong>getFulfillmentPolicyByName</strong> calls of the <strong>Account API</strong>. The <strong>shippingCostOverrides.priority</strong> value should match the <strong>shippingOptions.shippingServices.sortOrderId</strong> in order to override the shipping costs for that shipping service option. The seller must also ensure that the <strong>shippingServiceType</strong> value is set to <code>DOMESTIC</code> to override a domestic shipping service option, or to <code>INTERNATIONAL</code> to override an international shipping service option.<br/><br/>A separate <strong>ShippingCostOverrides</strong> node is needed for each shipping service option whose costs are being overridden. All defined fields of the <strong>shippingCostOverrides</strong> container should be included, even if the shipping costs and surcharge values are not changing.<br/><br/>The <strong>shippingCostOverrides</strong> container is returned in the <strong>getOffer</strong> and <strong>getOffers</strong> calls if one or more shipping cost overrides are being applied to the fulfillment policy.  # noqa: E501

        :return: The shipping_cost_overrides of this ListingPolicies.  # noqa: E501
        :rtype: list[ShippingCostOverride]
        """
        return self._shipping_cost_overrides

    @shipping_cost_overrides.setter
    def shipping_cost_overrides(self, shipping_cost_overrides):
        """Sets the shipping_cost_overrides of this ListingPolicies.

        This container is used if the seller wishes to override the shipping costs or surcharge for one or more domestic or international shipping service options defined in the fulfillment listing policy. To override the costs of a specific domestic or international shipping service option, the seller must know the priority/order of that shipping service in the fulfillment listing policy. The name of a shipping service option can be found in the <strong>shippingOptions.shippingServices.shippingServiceCode</strong> field of the fulfillment policy, and the priority/order of that shipping service option is found in the <strong>shippingOptions.shippingServices.sortOrderId</strong> field. Both of these values can be retrieved by searching for that fulfillment policy with the <strong>getFulfillmentPolicies</strong> or <strong>getFulfillmentPolicyByName</strong> calls of the <strong>Account API</strong>. The <strong>shippingCostOverrides.priority</strong> value should match the <strong>shippingOptions.shippingServices.sortOrderId</strong> in order to override the shipping costs for that shipping service option. The seller must also ensure that the <strong>shippingServiceType</strong> value is set to <code>DOMESTIC</code> to override a domestic shipping service option, or to <code>INTERNATIONAL</code> to override an international shipping service option.<br/><br/>A separate <strong>ShippingCostOverrides</strong> node is needed for each shipping service option whose costs are being overridden. All defined fields of the <strong>shippingCostOverrides</strong> container should be included, even if the shipping costs and surcharge values are not changing.<br/><br/>The <strong>shippingCostOverrides</strong> container is returned in the <strong>getOffer</strong> and <strong>getOffers</strong> calls if one or more shipping cost overrides are being applied to the fulfillment policy.  # noqa: E501

        :param shipping_cost_overrides: The shipping_cost_overrides of this ListingPolicies.  # noqa: E501
        :type: list[ShippingCostOverride]
        """

        self._shipping_cost_overrides = shipping_cost_overrides

    @property
    def take_back_policy_id(self):
        """Gets the take_back_policy_id of this ListingPolicies.  # noqa: E501

        This field specifies the ID of the seller created take-back policy. The law in some countries may require sellers to take back a used product when the buyer buys a new product. See <a href=\"https://www.ebay.com/help/selling/custom-policies/custom-policies?id=5311\" target=\"_blank\">Custom Policies</a> for more information. One take-back policy ID can be specified for each listing. Refer to the <a href=\"/api-docs/sell/account/resources/methods#h2-custom_policy \">custom_policy</a> resource (in the <strong>Sell Account API</strong>) to create and manage takeback policies.  # noqa: E501

        :return: The take_back_policy_id of this ListingPolicies.  # noqa: E501
        :rtype: str
        """
        return self._take_back_policy_id

    @take_back_policy_id.setter
    def take_back_policy_id(self, take_back_policy_id):
        """Sets the take_back_policy_id of this ListingPolicies.

        This field specifies the ID of the seller created take-back policy. The law in some countries may require sellers to take back a used product when the buyer buys a new product. See <a href=\"https://www.ebay.com/help/selling/custom-policies/custom-policies?id=5311\" target=\"_blank\">Custom Policies</a> for more information. One take-back policy ID can be specified for each listing. Refer to the <a href=\"/api-docs/sell/account/resources/methods#h2-custom_policy \">custom_policy</a> resource (in the <strong>Sell Account API</strong>) to create and manage takeback policies.  # noqa: E501

        :param take_back_policy_id: The take_back_policy_id of this ListingPolicies.  # noqa: E501
        :type: str
        """

        self._take_back_policy_id = take_back_policy_id

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
        if issubclass(ListingPolicies, dict):
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
        if not isinstance(other, ListingPolicies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
