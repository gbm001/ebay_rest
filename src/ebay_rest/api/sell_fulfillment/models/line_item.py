# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LineItem(object):
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
        'applied_promotions': 'list[AppliedPromotion]',
        'delivery_cost': 'DeliveryCost',
        'discounted_line_item_cost': 'Amount',
        'ebay_collect_and_remit_taxes': 'list[EbayCollectAndRemitTax]',
        'gift_details': 'GiftDetails',
        'item_location': 'ItemLocation',
        'legacy_item_id': 'str',
        'legacy_variation_id': 'str',
        'line_item_cost': 'Amount',
        'line_item_fulfillment_instructions': 'LineItemFulfillmentInstructions',
        'line_item_fulfillment_status': 'str',
        'line_item_id': 'str',
        'listing_marketplace_id': 'str',
        'properties': 'LineItemProperties',
        'purchase_marketplace_id': 'str',
        'quantity': 'int',
        'refunds': 'list[LineItemRefund]',
        'sku': 'str',
        'sold_format': 'str',
        'taxes': 'list[Tax]',
        'title': 'str',
        'total': 'Amount'
    }

    attribute_map = {
        'applied_promotions': 'appliedPromotions',
        'delivery_cost': 'deliveryCost',
        'discounted_line_item_cost': 'discountedLineItemCost',
        'ebay_collect_and_remit_taxes': 'ebayCollectAndRemitTaxes',
        'gift_details': 'giftDetails',
        'item_location': 'itemLocation',
        'legacy_item_id': 'legacyItemId',
        'legacy_variation_id': 'legacyVariationId',
        'line_item_cost': 'lineItemCost',
        'line_item_fulfillment_instructions': 'lineItemFulfillmentInstructions',
        'line_item_fulfillment_status': 'lineItemFulfillmentStatus',
        'line_item_id': 'lineItemId',
        'listing_marketplace_id': 'listingMarketplaceId',
        'properties': 'properties',
        'purchase_marketplace_id': 'purchaseMarketplaceId',
        'quantity': 'quantity',
        'refunds': 'refunds',
        'sku': 'sku',
        'sold_format': 'soldFormat',
        'taxes': 'taxes',
        'title': 'title',
        'total': 'total'
    }

    def __init__(self, applied_promotions=None, delivery_cost=None, discounted_line_item_cost=None, ebay_collect_and_remit_taxes=None, gift_details=None, item_location=None, legacy_item_id=None, legacy_variation_id=None, line_item_cost=None, line_item_fulfillment_instructions=None, line_item_fulfillment_status=None, line_item_id=None, listing_marketplace_id=None, properties=None, purchase_marketplace_id=None, quantity=None, refunds=None, sku=None, sold_format=None, taxes=None, title=None, total=None):  # noqa: E501
        """LineItem - a model defined in Swagger"""  # noqa: E501
        self._applied_promotions = None
        self._delivery_cost = None
        self._discounted_line_item_cost = None
        self._ebay_collect_and_remit_taxes = None
        self._gift_details = None
        self._item_location = None
        self._legacy_item_id = None
        self._legacy_variation_id = None
        self._line_item_cost = None
        self._line_item_fulfillment_instructions = None
        self._line_item_fulfillment_status = None
        self._line_item_id = None
        self._listing_marketplace_id = None
        self._properties = None
        self._purchase_marketplace_id = None
        self._quantity = None
        self._refunds = None
        self._sku = None
        self._sold_format = None
        self._taxes = None
        self._title = None
        self._total = None
        self.discriminator = None
        if applied_promotions is not None:
            self.applied_promotions = applied_promotions
        if delivery_cost is not None:
            self.delivery_cost = delivery_cost
        if discounted_line_item_cost is not None:
            self.discounted_line_item_cost = discounted_line_item_cost
        if ebay_collect_and_remit_taxes is not None:
            self.ebay_collect_and_remit_taxes = ebay_collect_and_remit_taxes
        if gift_details is not None:
            self.gift_details = gift_details
        if item_location is not None:
            self.item_location = item_location
        if legacy_item_id is not None:
            self.legacy_item_id = legacy_item_id
        if legacy_variation_id is not None:
            self.legacy_variation_id = legacy_variation_id
        if line_item_cost is not None:
            self.line_item_cost = line_item_cost
        if line_item_fulfillment_instructions is not None:
            self.line_item_fulfillment_instructions = line_item_fulfillment_instructions
        if line_item_fulfillment_status is not None:
            self.line_item_fulfillment_status = line_item_fulfillment_status
        if line_item_id is not None:
            self.line_item_id = line_item_id
        if listing_marketplace_id is not None:
            self.listing_marketplace_id = listing_marketplace_id
        if properties is not None:
            self.properties = properties
        if purchase_marketplace_id is not None:
            self.purchase_marketplace_id = purchase_marketplace_id
        if quantity is not None:
            self.quantity = quantity
        if refunds is not None:
            self.refunds = refunds
        if sku is not None:
            self.sku = sku
        if sold_format is not None:
            self.sold_format = sold_format
        if taxes is not None:
            self.taxes = taxes
        if title is not None:
            self.title = title
        if total is not None:
            self.total = total

    @property
    def applied_promotions(self):
        """Gets the applied_promotions of this LineItem.  # noqa: E501

        This array contains information about one or more sales promotions or discounts applied to the line item. It is always returned, but will be returned as an empty array if no special sales promotions or discounts apply to the order line item.  # noqa: E501

        :return: The applied_promotions of this LineItem.  # noqa: E501
        :rtype: list[AppliedPromotion]
        """
        return self._applied_promotions

    @applied_promotions.setter
    def applied_promotions(self, applied_promotions):
        """Sets the applied_promotions of this LineItem.

        This array contains information about one or more sales promotions or discounts applied to the line item. It is always returned, but will be returned as an empty array if no special sales promotions or discounts apply to the order line item.  # noqa: E501

        :param applied_promotions: The applied_promotions of this LineItem.  # noqa: E501
        :type: list[AppliedPromotion]
        """

        self._applied_promotions = applied_promotions

    @property
    def delivery_cost(self):
        """Gets the delivery_cost of this LineItem.  # noqa: E501


        :return: The delivery_cost of this LineItem.  # noqa: E501
        :rtype: DeliveryCost
        """
        return self._delivery_cost

    @delivery_cost.setter
    def delivery_cost(self, delivery_cost):
        """Sets the delivery_cost of this LineItem.


        :param delivery_cost: The delivery_cost of this LineItem.  # noqa: E501
        :type: DeliveryCost
        """

        self._delivery_cost = delivery_cost

    @property
    def discounted_line_item_cost(self):
        """Gets the discounted_line_item_cost of this LineItem.  # noqa: E501


        :return: The discounted_line_item_cost of this LineItem.  # noqa: E501
        :rtype: Amount
        """
        return self._discounted_line_item_cost

    @discounted_line_item_cost.setter
    def discounted_line_item_cost(self, discounted_line_item_cost):
        """Sets the discounted_line_item_cost of this LineItem.


        :param discounted_line_item_cost: The discounted_line_item_cost of this LineItem.  # noqa: E501
        :type: Amount
        """

        self._discounted_line_item_cost = discounted_line_item_cost

    @property
    def ebay_collect_and_remit_taxes(self):
        """Gets the ebay_collect_and_remit_taxes of this LineItem.  # noqa: E501

        This container will be returned if the order line item is subject to a 'Collect and Remit' tax that eBay will collect and remit to the proper taxing authority on the buyer's behalf. 'Collect and Remit' tax includes US state-mandated sales tax, 'Goods and Services' tax in Australia or New Zealand, and VAT collected for UK and EU countries. The amount of this tax is shown in the amount field, and the type of tax is shown in the taxType field. eBay will display the tax type and amount during checkout in accordance with the buyer's address, and handle collection and remittance of the tax without requiring the seller to take any action.  # noqa: E501

        :return: The ebay_collect_and_remit_taxes of this LineItem.  # noqa: E501
        :rtype: list[EbayCollectAndRemitTax]
        """
        return self._ebay_collect_and_remit_taxes

    @ebay_collect_and_remit_taxes.setter
    def ebay_collect_and_remit_taxes(self, ebay_collect_and_remit_taxes):
        """Sets the ebay_collect_and_remit_taxes of this LineItem.

        This container will be returned if the order line item is subject to a 'Collect and Remit' tax that eBay will collect and remit to the proper taxing authority on the buyer's behalf. 'Collect and Remit' tax includes US state-mandated sales tax, 'Goods and Services' tax in Australia or New Zealand, and VAT collected for UK and EU countries. The amount of this tax is shown in the amount field, and the type of tax is shown in the taxType field. eBay will display the tax type and amount during checkout in accordance with the buyer's address, and handle collection and remittance of the tax without requiring the seller to take any action.  # noqa: E501

        :param ebay_collect_and_remit_taxes: The ebay_collect_and_remit_taxes of this LineItem.  # noqa: E501
        :type: list[EbayCollectAndRemitTax]
        """

        self._ebay_collect_and_remit_taxes = ebay_collect_and_remit_taxes

    @property
    def gift_details(self):
        """Gets the gift_details of this LineItem.  # noqa: E501


        :return: The gift_details of this LineItem.  # noqa: E501
        :rtype: GiftDetails
        """
        return self._gift_details

    @gift_details.setter
    def gift_details(self, gift_details):
        """Sets the gift_details of this LineItem.


        :param gift_details: The gift_details of this LineItem.  # noqa: E501
        :type: GiftDetails
        """

        self._gift_details = gift_details

    @property
    def item_location(self):
        """Gets the item_location of this LineItem.  # noqa: E501


        :return: The item_location of this LineItem.  # noqa: E501
        :rtype: ItemLocation
        """
        return self._item_location

    @item_location.setter
    def item_location(self, item_location):
        """Sets the item_location of this LineItem.


        :param item_location: The item_location of this LineItem.  # noqa: E501
        :type: ItemLocation
        """

        self._item_location = item_location

    @property
    def legacy_item_id(self):
        """Gets the legacy_item_id of this LineItem.  # noqa: E501

        The eBay-generated legacy listing item ID of the listing. Note that the unique identifier of a listing in REST-based APIs is called the listingId instead.  # noqa: E501

        :return: The legacy_item_id of this LineItem.  # noqa: E501
        :rtype: str
        """
        return self._legacy_item_id

    @legacy_item_id.setter
    def legacy_item_id(self, legacy_item_id):
        """Sets the legacy_item_id of this LineItem.

        The eBay-generated legacy listing item ID of the listing. Note that the unique identifier of a listing in REST-based APIs is called the listingId instead.  # noqa: E501

        :param legacy_item_id: The legacy_item_id of this LineItem.  # noqa: E501
        :type: str
        """

        self._legacy_item_id = legacy_item_id

    @property
    def legacy_variation_id(self):
        """Gets the legacy_variation_id of this LineItem.  # noqa: E501

        The unique identifier of a single variation within a multiple-variation listing. This field is only returned if the line item purchased was from a multiple-variation listing.  # noqa: E501

        :return: The legacy_variation_id of this LineItem.  # noqa: E501
        :rtype: str
        """
        return self._legacy_variation_id

    @legacy_variation_id.setter
    def legacy_variation_id(self, legacy_variation_id):
        """Sets the legacy_variation_id of this LineItem.

        The unique identifier of a single variation within a multiple-variation listing. This field is only returned if the line item purchased was from a multiple-variation listing.  # noqa: E501

        :param legacy_variation_id: The legacy_variation_id of this LineItem.  # noqa: E501
        :type: str
        """

        self._legacy_variation_id = legacy_variation_id

    @property
    def line_item_cost(self):
        """Gets the line_item_cost of this LineItem.  # noqa: E501


        :return: The line_item_cost of this LineItem.  # noqa: E501
        :rtype: Amount
        """
        return self._line_item_cost

    @line_item_cost.setter
    def line_item_cost(self, line_item_cost):
        """Sets the line_item_cost of this LineItem.


        :param line_item_cost: The line_item_cost of this LineItem.  # noqa: E501
        :type: Amount
        """

        self._line_item_cost = line_item_cost

    @property
    def line_item_fulfillment_instructions(self):
        """Gets the line_item_fulfillment_instructions of this LineItem.  # noqa: E501


        :return: The line_item_fulfillment_instructions of this LineItem.  # noqa: E501
        :rtype: LineItemFulfillmentInstructions
        """
        return self._line_item_fulfillment_instructions

    @line_item_fulfillment_instructions.setter
    def line_item_fulfillment_instructions(self, line_item_fulfillment_instructions):
        """Sets the line_item_fulfillment_instructions of this LineItem.


        :param line_item_fulfillment_instructions: The line_item_fulfillment_instructions of this LineItem.  # noqa: E501
        :type: LineItemFulfillmentInstructions
        """

        self._line_item_fulfillment_instructions = line_item_fulfillment_instructions

    @property
    def line_item_fulfillment_status(self):
        """Gets the line_item_fulfillment_status of this LineItem.  # noqa: E501

        This enumeration value indicates the current fulfillment status of the line item. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:LineItemFulfillmentStatusEnum'>eBay API documentation</a>  # noqa: E501

        :return: The line_item_fulfillment_status of this LineItem.  # noqa: E501
        :rtype: str
        """
        return self._line_item_fulfillment_status

    @line_item_fulfillment_status.setter
    def line_item_fulfillment_status(self, line_item_fulfillment_status):
        """Sets the line_item_fulfillment_status of this LineItem.

        This enumeration value indicates the current fulfillment status of the line item. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:LineItemFulfillmentStatusEnum'>eBay API documentation</a>  # noqa: E501

        :param line_item_fulfillment_status: The line_item_fulfillment_status of this LineItem.  # noqa: E501
        :type: str
        """

        self._line_item_fulfillment_status = line_item_fulfillment_status

    @property
    def line_item_id(self):
        """Gets the line_item_id of this LineItem.  # noqa: E501

        This is the unique identifier of an eBay order line item. This field is created as soon as there is a commitment to buy from the seller.  # noqa: E501

        :return: The line_item_id of this LineItem.  # noqa: E501
        :rtype: str
        """
        return self._line_item_id

    @line_item_id.setter
    def line_item_id(self, line_item_id):
        """Sets the line_item_id of this LineItem.

        This is the unique identifier of an eBay order line item. This field is created as soon as there is a commitment to buy from the seller.  # noqa: E501

        :param line_item_id: The line_item_id of this LineItem.  # noqa: E501
        :type: str
        """

        self._line_item_id = line_item_id

    @property
    def listing_marketplace_id(self):
        """Gets the listing_marketplace_id of this LineItem.  # noqa: E501

        The unique identifier of the eBay marketplace where the line item was listed. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :return: The listing_marketplace_id of this LineItem.  # noqa: E501
        :rtype: str
        """
        return self._listing_marketplace_id

    @listing_marketplace_id.setter
    def listing_marketplace_id(self, listing_marketplace_id):
        """Sets the listing_marketplace_id of this LineItem.

        The unique identifier of the eBay marketplace where the line item was listed. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :param listing_marketplace_id: The listing_marketplace_id of this LineItem.  # noqa: E501
        :type: str
        """

        self._listing_marketplace_id = listing_marketplace_id

    @property
    def properties(self):
        """Gets the properties of this LineItem.  # noqa: E501


        :return: The properties of this LineItem.  # noqa: E501
        :rtype: LineItemProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this LineItem.


        :param properties: The properties of this LineItem.  # noqa: E501
        :type: LineItemProperties
        """

        self._properties = properties

    @property
    def purchase_marketplace_id(self):
        """Gets the purchase_marketplace_id of this LineItem.  # noqa: E501

        The unique identifier of the eBay marketplace where the line item was listed. Often, the listingMarketplaceId and the purchaseMarketplaceId identifier are the same, but there are occasions when an item will surface on multiple eBay marketplaces. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :return: The purchase_marketplace_id of this LineItem.  # noqa: E501
        :rtype: str
        """
        return self._purchase_marketplace_id

    @purchase_marketplace_id.setter
    def purchase_marketplace_id(self, purchase_marketplace_id):
        """Sets the purchase_marketplace_id of this LineItem.

        The unique identifier of the eBay marketplace where the line item was listed. Often, the listingMarketplaceId and the purchaseMarketplaceId identifier are the same, but there are occasions when an item will surface on multiple eBay marketplaces. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :param purchase_marketplace_id: The purchase_marketplace_id of this LineItem.  # noqa: E501
        :type: str
        """

        self._purchase_marketplace_id = purchase_marketplace_id

    @property
    def quantity(self):
        """Gets the quantity of this LineItem.  # noqa: E501

        The number of units of the line item in the order. These are represented as a group by a single lineItemId.  # noqa: E501

        :return: The quantity of this LineItem.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this LineItem.

        The number of units of the line item in the order. These are represented as a group by a single lineItemId.  # noqa: E501

        :param quantity: The quantity of this LineItem.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def refunds(self):
        """Gets the refunds of this LineItem.  # noqa: E501

        This array is always returned, but is returned as an empty array unless the seller has submitted a partial or full refund to the buyer for the order. If a refund has occurred, the refund amount and refund date will be shown for each refund.  # noqa: E501

        :return: The refunds of this LineItem.  # noqa: E501
        :rtype: list[LineItemRefund]
        """
        return self._refunds

    @refunds.setter
    def refunds(self, refunds):
        """Sets the refunds of this LineItem.

        This array is always returned, but is returned as an empty array unless the seller has submitted a partial or full refund to the buyer for the order. If a refund has occurred, the refund amount and refund date will be shown for each refund.  # noqa: E501

        :param refunds: The refunds of this LineItem.  # noqa: E501
        :type: list[LineItemRefund]
        """

        self._refunds = refunds

    @property
    def sku(self):
        """Gets the sku of this LineItem.  # noqa: E501

        Seller-defined Stock-Keeping Unit (SKU). This inventory identifier must be unique within the seller's eBay inventory. SKUs are optional when listing in the legacy/Trading API system, but SKUs are required when listing items through the Inventory API model.  # noqa: E501

        :return: The sku of this LineItem.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this LineItem.

        Seller-defined Stock-Keeping Unit (SKU). This inventory identifier must be unique within the seller's eBay inventory. SKUs are optional when listing in the legacy/Trading API system, but SKUs are required when listing items through the Inventory API model.  # noqa: E501

        :param sku: The sku of this LineItem.  # noqa: E501
        :type: str
        """

        self._sku = sku

    @property
    def sold_format(self):
        """Gets the sold_format of this LineItem.  # noqa: E501

        The eBay listing type of the line item. The most common listing types are AUCTION and FIXED_PRICE. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:SoldFormatEnum'>eBay API documentation</a>  # noqa: E501

        :return: The sold_format of this LineItem.  # noqa: E501
        :rtype: str
        """
        return self._sold_format

    @sold_format.setter
    def sold_format(self, sold_format):
        """Sets the sold_format of this LineItem.

        The eBay listing type of the line item. The most common listing types are AUCTION and FIXED_PRICE. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:SoldFormatEnum'>eBay API documentation</a>  # noqa: E501

        :param sold_format: The sold_format of this LineItem.  # noqa: E501
        :type: str
        """

        self._sold_format = sold_format

    @property
    def taxes(self):
        """Gets the taxes of this LineItem.  # noqa: E501

        Contains a list of taxes applied to the line item, if any. This array is always returned, but will be returned as empty if no taxes are applicable to the line item.  # noqa: E501

        :return: The taxes of this LineItem.  # noqa: E501
        :rtype: list[Tax]
        """
        return self._taxes

    @taxes.setter
    def taxes(self, taxes):
        """Sets the taxes of this LineItem.

        Contains a list of taxes applied to the line item, if any. This array is always returned, but will be returned as empty if no taxes are applicable to the line item.  # noqa: E501

        :param taxes: The taxes of this LineItem.  # noqa: E501
        :type: list[Tax]
        """

        self._taxes = taxes

    @property
    def title(self):
        """Gets the title of this LineItem.  # noqa: E501

        The title of the listing.  # noqa: E501

        :return: The title of this LineItem.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LineItem.

        The title of the listing.  # noqa: E501

        :param title: The title of this LineItem.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def total(self):
        """Gets the total of this LineItem.  # noqa: E501


        :return: The total of this LineItem.  # noqa: E501
        :rtype: Amount
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this LineItem.


        :param total: The total of this LineItem.  # noqa: E501
        :type: Amount
        """

        self._total = total

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
        if issubclass(LineItem, dict):
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
        if not isinstance(other, LineItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
