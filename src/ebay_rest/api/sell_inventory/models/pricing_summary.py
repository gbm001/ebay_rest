# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.16.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PricingSummary(object):
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
        'auction_reserve_price': 'Amount',
        'auction_start_price': 'Amount',
        'minimum_advertised_price': 'Amount',
        'originally_sold_for_retail_price_on': 'str',
        'original_retail_price': 'Amount',
        'price': 'Amount',
        'pricing_visibility': 'str'
    }

    attribute_map = {
        'auction_reserve_price': 'auctionReservePrice',
        'auction_start_price': 'auctionStartPrice',
        'minimum_advertised_price': 'minimumAdvertisedPrice',
        'originally_sold_for_retail_price_on': 'originallySoldForRetailPriceOn',
        'original_retail_price': 'originalRetailPrice',
        'price': 'price',
        'pricing_visibility': 'pricingVisibility'
    }

    def __init__(self, auction_reserve_price=None, auction_start_price=None, minimum_advertised_price=None, originally_sold_for_retail_price_on=None, original_retail_price=None, price=None, pricing_visibility=None):  # noqa: E501
        """PricingSummary - a model defined in Swagger"""  # noqa: E501
        self._auction_reserve_price = None
        self._auction_start_price = None
        self._minimum_advertised_price = None
        self._originally_sold_for_retail_price_on = None
        self._original_retail_price = None
        self._price = None
        self._pricing_visibility = None
        self.discriminator = None
        if auction_reserve_price is not None:
            self.auction_reserve_price = auction_reserve_price
        if auction_start_price is not None:
            self.auction_start_price = auction_start_price
        if minimum_advertised_price is not None:
            self.minimum_advertised_price = minimum_advertised_price
        if originally_sold_for_retail_price_on is not None:
            self.originally_sold_for_retail_price_on = originally_sold_for_retail_price_on
        if original_retail_price is not None:
            self.original_retail_price = original_retail_price
        if price is not None:
            self.price = price
        if pricing_visibility is not None:
            self.pricing_visibility = pricing_visibility

    @property
    def auction_reserve_price(self):
        """Gets the auction_reserve_price of this PricingSummary.  # noqa: E501


        :return: The auction_reserve_price of this PricingSummary.  # noqa: E501
        :rtype: Amount
        """
        return self._auction_reserve_price

    @auction_reserve_price.setter
    def auction_reserve_price(self, auction_reserve_price):
        """Sets the auction_reserve_price of this PricingSummary.


        :param auction_reserve_price: The auction_reserve_price of this PricingSummary.  # noqa: E501
        :type: Amount
        """

        self._auction_reserve_price = auction_reserve_price

    @property
    def auction_start_price(self):
        """Gets the auction_start_price of this PricingSummary.  # noqa: E501


        :return: The auction_start_price of this PricingSummary.  # noqa: E501
        :rtype: Amount
        """
        return self._auction_start_price

    @auction_start_price.setter
    def auction_start_price(self, auction_start_price):
        """Sets the auction_start_price of this PricingSummary.


        :param auction_start_price: The auction_start_price of this PricingSummary.  # noqa: E501
        :type: Amount
        """

        self._auction_start_price = auction_start_price

    @property
    def minimum_advertised_price(self):
        """Gets the minimum_advertised_price of this PricingSummary.  # noqa: E501


        :return: The minimum_advertised_price of this PricingSummary.  # noqa: E501
        :rtype: Amount
        """
        return self._minimum_advertised_price

    @minimum_advertised_price.setter
    def minimum_advertised_price(self, minimum_advertised_price):
        """Sets the minimum_advertised_price of this PricingSummary.


        :param minimum_advertised_price: The minimum_advertised_price of this PricingSummary.  # noqa: E501
        :type: Amount
        """

        self._minimum_advertised_price = minimum_advertised_price

    @property
    def originally_sold_for_retail_price_on(self):
        """Gets the originally_sold_for_retail_price_on of this PricingSummary.  # noqa: E501

        This field is needed if the Strikethrough Pricing (STP) feature will be used in the offer. This field indicates that the product was sold for the price in the <strong>originalRetailPrice</strong> field on an eBay site, or sold for that price by a third-party retailer. When using the <strong>createOffer</strong> or <strong>updateOffer</strong> calls, the seller will pass in a value of <code>ON_EBAY</code> to indicate that the product was sold for the <strong>originalRetailPrice</strong> on an eBay site, or the seller will pass in a value of <code>OFF_EBAY</code> to indicate that the product was sold for the <strong>originalRetailPrice</strong> through a third-party retailer. This field and the <strong>originalRetailPrice</strong> field are only applicable if the seller and listing are eligible to use the Strikethrough Pricing feature, a feature which is limited to the US (core site and Motors), UK, Germany, Canada (English and French versions), France, Italy, and Spain sites.<br/><br/>This field will be returned if set for the offer. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:SoldOnEnum'>eBay API documentation</a>  # noqa: E501

        :return: The originally_sold_for_retail_price_on of this PricingSummary.  # noqa: E501
        :rtype: str
        """
        return self._originally_sold_for_retail_price_on

    @originally_sold_for_retail_price_on.setter
    def originally_sold_for_retail_price_on(self, originally_sold_for_retail_price_on):
        """Sets the originally_sold_for_retail_price_on of this PricingSummary.

        This field is needed if the Strikethrough Pricing (STP) feature will be used in the offer. This field indicates that the product was sold for the price in the <strong>originalRetailPrice</strong> field on an eBay site, or sold for that price by a third-party retailer. When using the <strong>createOffer</strong> or <strong>updateOffer</strong> calls, the seller will pass in a value of <code>ON_EBAY</code> to indicate that the product was sold for the <strong>originalRetailPrice</strong> on an eBay site, or the seller will pass in a value of <code>OFF_EBAY</code> to indicate that the product was sold for the <strong>originalRetailPrice</strong> through a third-party retailer. This field and the <strong>originalRetailPrice</strong> field are only applicable if the seller and listing are eligible to use the Strikethrough Pricing feature, a feature which is limited to the US (core site and Motors), UK, Germany, Canada (English and French versions), France, Italy, and Spain sites.<br/><br/>This field will be returned if set for the offer. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:SoldOnEnum'>eBay API documentation</a>  # noqa: E501

        :param originally_sold_for_retail_price_on: The originally_sold_for_retail_price_on of this PricingSummary.  # noqa: E501
        :type: str
        """

        self._originally_sold_for_retail_price_on = originally_sold_for_retail_price_on

    @property
    def original_retail_price(self):
        """Gets the original_retail_price of this PricingSummary.  # noqa: E501


        :return: The original_retail_price of this PricingSummary.  # noqa: E501
        :rtype: Amount
        """
        return self._original_retail_price

    @original_retail_price.setter
    def original_retail_price(self, original_retail_price):
        """Sets the original_retail_price of this PricingSummary.


        :param original_retail_price: The original_retail_price of this PricingSummary.  # noqa: E501
        :type: Amount
        """

        self._original_retail_price = original_retail_price

    @property
    def price(self):
        """Gets the price of this PricingSummary.  # noqa: E501


        :return: The price of this PricingSummary.  # noqa: E501
        :rtype: Amount
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this PricingSummary.


        :param price: The price of this PricingSummary.  # noqa: E501
        :type: Amount
        """

        self._price = price

    @property
    def pricing_visibility(self):
        """Gets the pricing_visibility of this PricingSummary.  # noqa: E501

        This field is needed if the Minimum Advertised Price (MAP) feature will be used in the offer. This field is only applicable if an eligible US seller is using the Minimum Advertised Price (MAP) feature and a <strong>minimumAdvertisedPrice</strong> has been specified. The value set in this field will determine whether the MAP price is shown to a prospective buyer prior to checkout through a pop-up window accessed from the View Item page, or if the MAP price is not shown until the checkout flow after the buyer has already committed to buying the item. To show the MAP price prior to checkout, the seller will set this value to <code>PRE_CHECKOUT</code>. To show the MAP price after the buyer already commits to buy the item, the seller will set this value to <code>DURING_CHECKOUT</code>. This field will be ignored if the seller and/or the listing is not eligible for the MAP feature.<br/><br/>This field will be returned if set for the offer. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:MinimumAdvertisedPriceHandlingEnum'>eBay API documentation</a>  # noqa: E501

        :return: The pricing_visibility of this PricingSummary.  # noqa: E501
        :rtype: str
        """
        return self._pricing_visibility

    @pricing_visibility.setter
    def pricing_visibility(self, pricing_visibility):
        """Sets the pricing_visibility of this PricingSummary.

        This field is needed if the Minimum Advertised Price (MAP) feature will be used in the offer. This field is only applicable if an eligible US seller is using the Minimum Advertised Price (MAP) feature and a <strong>minimumAdvertisedPrice</strong> has been specified. The value set in this field will determine whether the MAP price is shown to a prospective buyer prior to checkout through a pop-up window accessed from the View Item page, or if the MAP price is not shown until the checkout flow after the buyer has already committed to buying the item. To show the MAP price prior to checkout, the seller will set this value to <code>PRE_CHECKOUT</code>. To show the MAP price after the buyer already commits to buy the item, the seller will set this value to <code>DURING_CHECKOUT</code>. This field will be ignored if the seller and/or the listing is not eligible for the MAP feature.<br/><br/>This field will be returned if set for the offer. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:MinimumAdvertisedPriceHandlingEnum'>eBay API documentation</a>  # noqa: E501

        :param pricing_visibility: The pricing_visibility of this PricingSummary.  # noqa: E501
        :type: str
        """

        self._pricing_visibility = pricing_visibility

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
        if issubclass(PricingSummary, dict):
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
        if not isinstance(other, PricingSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
