# coding: utf-8

"""
    Marketing API

    <p>The <i>Marketing API </i> offers two platforms that sellers can use to promote and advertise their products:</p> <ul><li><b>Promoted Listings</b> is an eBay ad service that lets sellers set up <i>ad campaigns </i> for the products they want to promote. eBay displays the ads in search results and in other marketing modules as <b>SPONSORED</b> listings. If an item in a Promoted Listings campaign sells, the seller is assessed a Promoted Listings fee, which is a seller-specified percentage applied to the sales price. For complete details, see <a href=\"/api-docs/sell/static/marketing/promoted-listings.html\">Promoted Listings</a>.</li>  <li><b>Promotions Manager</b> gives sellers a way to offer discounts on specific items as a way to attract buyers to their inventory. Sellers can set up discounts (such as \"20% off\" and other types of offers) on specific items or on an entire customer order. To further attract buyers, eBay prominently displays promotion <i>teasers</i> throughout buyer flows. For complete details, see <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a>.</li></ul>  <p><b>Marketing reports</b>, on both the Promoted Listings and Promotions Manager platforms, give sellers information that shows the effectiveness of their marketing strategies. The data gives sellers the ability to review and fine tune their marketing efforts.</p> <p class=\"tablenote\"><b>Important!</b> Sellers must have an active eBay Store subscription, and they must accept the <b>Terms and Conditions</b> before they can make requests to these APIs in the Production environment. There are also site-specific listings requirements and restrictions associated with these marketing tools, as listed in the \"requirements and restrictions\" sections for <a href=\"/api-docs/sell/marketing/static/overview.html#PL-requirements\">Promoted Listings</a> and <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager</a>.</p> <p>The table below lists all the Marketing API calls grouped by resource.</p>  # noqa: E501

    OpenAPI spec version: v1.10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ItemPriceMarkdown(object):
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
        'apply_free_shipping': 'bool',
        'auto_select_future_inventory': 'bool',
        'block_price_increase_in_item_revision': 'bool',
        'description': 'str',
        'end_date': 'str',
        'marketplace_id': 'str',
        'name': 'str',
        'priority': 'str',
        'promotion_image_url': 'str',
        'promotion_status': 'str',
        'selected_inventory_discounts': 'list[SelectedInventoryDiscount]',
        'start_date': 'str'
    }

    attribute_map = {
        'apply_free_shipping': 'applyFreeShipping',
        'auto_select_future_inventory': 'autoSelectFutureInventory',
        'block_price_increase_in_item_revision': 'blockPriceIncreaseInItemRevision',
        'description': 'description',
        'end_date': 'endDate',
        'marketplace_id': 'marketplaceId',
        'name': 'name',
        'priority': 'priority',
        'promotion_image_url': 'promotionImageUrl',
        'promotion_status': 'promotionStatus',
        'selected_inventory_discounts': 'selectedInventoryDiscounts',
        'start_date': 'startDate'
    }

    def __init__(self, apply_free_shipping=None, auto_select_future_inventory=None, block_price_increase_in_item_revision=None, description=None, end_date=None, marketplace_id=None, name=None, priority=None, promotion_image_url=None, promotion_status=None, selected_inventory_discounts=None, start_date=None):  # noqa: E501
        """ItemPriceMarkdown - a model defined in Swagger"""  # noqa: E501
        self._apply_free_shipping = None
        self._auto_select_future_inventory = None
        self._block_price_increase_in_item_revision = None
        self._description = None
        self._end_date = None
        self._marketplace_id = None
        self._name = None
        self._priority = None
        self._promotion_image_url = None
        self._promotion_status = None
        self._selected_inventory_discounts = None
        self._start_date = None
        self.discriminator = None
        if apply_free_shipping is not None:
            self.apply_free_shipping = apply_free_shipping
        if auto_select_future_inventory is not None:
            self.auto_select_future_inventory = auto_select_future_inventory
        if block_price_increase_in_item_revision is not None:
            self.block_price_increase_in_item_revision = block_price_increase_in_item_revision
        if description is not None:
            self.description = description
        if end_date is not None:
            self.end_date = end_date
        if marketplace_id is not None:
            self.marketplace_id = marketplace_id
        if name is not None:
            self.name = name
        if priority is not None:
            self.priority = priority
        if promotion_image_url is not None:
            self.promotion_image_url = promotion_image_url
        if promotion_status is not None:
            self.promotion_status = promotion_status
        if selected_inventory_discounts is not None:
            self.selected_inventory_discounts = selected_inventory_discounts
        if start_date is not None:
            self.start_date = start_date

    @property
    def apply_free_shipping(self):
        """Gets the apply_free_shipping of this ItemPriceMarkdown.  # noqa: E501

        If set to true, free shipping is applied to the first shipping service specified for the item. The first domestic shipping option is set to &quot;free shipping,&quot; regardless if the shipping optionType for that service is set to FLAT_RATE, CALCULATED, or NOT_SPECIFIED (freight). This flag essentially adds free shipping as a promotional bonus. Default: false  # noqa: E501

        :return: The apply_free_shipping of this ItemPriceMarkdown.  # noqa: E501
        :rtype: bool
        """
        return self._apply_free_shipping

    @apply_free_shipping.setter
    def apply_free_shipping(self, apply_free_shipping):
        """Sets the apply_free_shipping of this ItemPriceMarkdown.

        If set to true, free shipping is applied to the first shipping service specified for the item. The first domestic shipping option is set to &quot;free shipping,&quot; regardless if the shipping optionType for that service is set to FLAT_RATE, CALCULATED, or NOT_SPECIFIED (freight). This flag essentially adds free shipping as a promotional bonus. Default: false  # noqa: E501

        :param apply_free_shipping: The apply_free_shipping of this ItemPriceMarkdown.  # noqa: E501
        :type: bool
        """

        self._apply_free_shipping = apply_free_shipping

    @property
    def auto_select_future_inventory(self):
        """Gets the auto_select_future_inventory of this ItemPriceMarkdown.  # noqa: E501

        If set to true, eBay will automatically add inventory items to the markdown promotion if they meet the selectedInventoryDiscounts criteria specified for the markdown promotion. Default: false  # noqa: E501

        :return: The auto_select_future_inventory of this ItemPriceMarkdown.  # noqa: E501
        :rtype: bool
        """
        return self._auto_select_future_inventory

    @auto_select_future_inventory.setter
    def auto_select_future_inventory(self, auto_select_future_inventory):
        """Sets the auto_select_future_inventory of this ItemPriceMarkdown.

        If set to true, eBay will automatically add inventory items to the markdown promotion if they meet the selectedInventoryDiscounts criteria specified for the markdown promotion. Default: false  # noqa: E501

        :param auto_select_future_inventory: The auto_select_future_inventory of this ItemPriceMarkdown.  # noqa: E501
        :type: bool
        """

        self._auto_select_future_inventory = auto_select_future_inventory

    @property
    def block_price_increase_in_item_revision(self):
        """Gets the block_price_increase_in_item_revision of this ItemPriceMarkdown.  # noqa: E501

        If set to true, price increases (including removing the free shipping flag) are blocked and an error message is returned if a seller attempts to adjust the price of an item that's partaking in this markdown promotion. If set to false, an item is dropped from the markdown promotion if the seller adjusts the price. Default: false  # noqa: E501

        :return: The block_price_increase_in_item_revision of this ItemPriceMarkdown.  # noqa: E501
        :rtype: bool
        """
        return self._block_price_increase_in_item_revision

    @block_price_increase_in_item_revision.setter
    def block_price_increase_in_item_revision(self, block_price_increase_in_item_revision):
        """Sets the block_price_increase_in_item_revision of this ItemPriceMarkdown.

        If set to true, price increases (including removing the free shipping flag) are blocked and an error message is returned if a seller attempts to adjust the price of an item that's partaking in this markdown promotion. If set to false, an item is dropped from the markdown promotion if the seller adjusts the price. Default: false  # noqa: E501

        :param block_price_increase_in_item_revision: The block_price_increase_in_item_revision of this ItemPriceMarkdown.  # noqa: E501
        :type: bool
        """

        self._block_price_increase_in_item_revision = block_price_increase_in_item_revision

    @property
    def description(self):
        """Gets the description of this ItemPriceMarkdown.  # noqa: E501

        This field is required if you are configuring an MARKDOWN_SALE promotion. This is the seller-defined &quot;tag line&quot; for the offer, such as &quot;Save on designer shoes.&quot; A tag line appears under the &quot;offer-type text&quot; that is generated for the promotion. The text is displayed on the offer tile that is shown on the seller's All Offers page and on the event page for the promotion. Note: Offer-type text is a teaser that's presented throughout the buyer's journey through the sales flow and is generated by eBay. This text is not editable by the seller&mdash;it's derived from the settings in the discountRules and discountSpecification fields&mdash;and can be, for example, &quot;20% off&quot;. Maximum length: 50  # noqa: E501

        :return: The description of this ItemPriceMarkdown.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ItemPriceMarkdown.

        This field is required if you are configuring an MARKDOWN_SALE promotion. This is the seller-defined &quot;tag line&quot; for the offer, such as &quot;Save on designer shoes.&quot; A tag line appears under the &quot;offer-type text&quot; that is generated for the promotion. The text is displayed on the offer tile that is shown on the seller's All Offers page and on the event page for the promotion. Note: Offer-type text is a teaser that's presented throughout the buyer's journey through the sales flow and is generated by eBay. This text is not editable by the seller&mdash;it's derived from the settings in the discountRules and discountSpecification fields&mdash;and can be, for example, &quot;20% off&quot;. Maximum length: 50  # noqa: E501

        :param description: The description of this ItemPriceMarkdown.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def end_date(self):
        """Gets the end_date of this ItemPriceMarkdown.  # noqa: E501

        The date and time the promotion ends, in UTC format (yyyy-MM-ddThh:mm:ssZ). The value supplied for endDate must be at least 24 hours after the value supplied for the startDate of the markdown promotion. If this field is blank (null), it indicates the promotion has no end date. For display purposes, convert this time into the local time of the seller. Max value: 14 days for the AT, CH, DE, ES, FR, IE, IT, and UK, marketplaces. 45 days for all other marketplaces.  # noqa: E501

        :return: The end_date of this ItemPriceMarkdown.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ItemPriceMarkdown.

        The date and time the promotion ends, in UTC format (yyyy-MM-ddThh:mm:ssZ). The value supplied for endDate must be at least 24 hours after the value supplied for the startDate of the markdown promotion. If this field is blank (null), it indicates the promotion has no end date. For display purposes, convert this time into the local time of the seller. Max value: 14 days for the AT, CH, DE, ES, FR, IE, IT, and UK, marketplaces. 45 days for all other marketplaces.  # noqa: E501

        :param end_date: The end_date of this ItemPriceMarkdown.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def marketplace_id(self):
        """Gets the marketplace_id of this ItemPriceMarkdown.  # noqa: E501

        The eBay marketplace ID of the site where the markdown promotion is hosted. Markdown promotions are supported on all eBay marketplaces. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :return: The marketplace_id of this ItemPriceMarkdown.  # noqa: E501
        :rtype: str
        """
        return self._marketplace_id

    @marketplace_id.setter
    def marketplace_id(self, marketplace_id):
        """Sets the marketplace_id of this ItemPriceMarkdown.

        The eBay marketplace ID of the site where the markdown promotion is hosted. Markdown promotions are supported on all eBay marketplaces. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :param marketplace_id: The marketplace_id of this ItemPriceMarkdown.  # noqa: E501
        :type: str
        """

        self._marketplace_id = marketplace_id

    @property
    def name(self):
        """Gets the name of this ItemPriceMarkdown.  # noqa: E501

        The seller-defined name or 'title' of the promotion that the seller can use to identify a promotion. This label is not displayed in end-user flows. Maximum length: 90  # noqa: E501

        :return: The name of this ItemPriceMarkdown.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ItemPriceMarkdown.

        The seller-defined name or 'title' of the promotion that the seller can use to identify a promotion. This label is not displayed in end-user flows. Maximum length: 90  # noqa: E501

        :param name: The name of this ItemPriceMarkdown.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def priority(self):
        """Gets the priority of this ItemPriceMarkdown.  # noqa: E501

        This field is ignored in markdown promotions. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/sme:PromotionPriorityEnum'>eBay API documentation</a>  # noqa: E501

        :return: The priority of this ItemPriceMarkdown.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ItemPriceMarkdown.

        This field is ignored in markdown promotions. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/sme:PromotionPriorityEnum'>eBay API documentation</a>  # noqa: E501

        :param priority: The priority of this ItemPriceMarkdown.  # noqa: E501
        :type: str
        """

        self._priority = priority

    @property
    def promotion_image_url(self):
        """Gets the promotion_image_url of this ItemPriceMarkdown.  # noqa: E501

        Required for MARKDOWN_SALE promotions, populate this field with a URL that points to an image to be used with the promotion. This image is displayed on the seller's All Offers page. The URL must point to either JPEG or PNG image and it must be a minimum of 500x500 pixels in dimension and cannot exceed 12Mb in size.  # noqa: E501

        :return: The promotion_image_url of this ItemPriceMarkdown.  # noqa: E501
        :rtype: str
        """
        return self._promotion_image_url

    @promotion_image_url.setter
    def promotion_image_url(self, promotion_image_url):
        """Sets the promotion_image_url of this ItemPriceMarkdown.

        Required for MARKDOWN_SALE promotions, populate this field with a URL that points to an image to be used with the promotion. This image is displayed on the seller's All Offers page. The URL must point to either JPEG or PNG image and it must be a minimum of 500x500 pixels in dimension and cannot exceed 12Mb in size.  # noqa: E501

        :param promotion_image_url: The promotion_image_url of this ItemPriceMarkdown.  # noqa: E501
        :type: str
        """

        self._promotion_image_url = promotion_image_url

    @property
    def promotion_status(self):
        """Gets the promotion_status of this ItemPriceMarkdown.  # noqa: E501

        The current status of the promotion. When creating a new promotion, you must set this value to either DRAFT or SCHEDULED. Note that you must set this value to SCHEDULED when you update a RUNNING promotion. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/sme:PromotionStatusEnum'>eBay API documentation</a>  # noqa: E501

        :return: The promotion_status of this ItemPriceMarkdown.  # noqa: E501
        :rtype: str
        """
        return self._promotion_status

    @promotion_status.setter
    def promotion_status(self, promotion_status):
        """Sets the promotion_status of this ItemPriceMarkdown.

        The current status of the promotion. When creating a new promotion, you must set this value to either DRAFT or SCHEDULED. Note that you must set this value to SCHEDULED when you update a RUNNING promotion. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/sme:PromotionStatusEnum'>eBay API documentation</a>  # noqa: E501

        :param promotion_status: The promotion_status of this ItemPriceMarkdown.  # noqa: E501
        :type: str
        """

        self._promotion_status = promotion_status

    @property
    def selected_inventory_discounts(self):
        """Gets the selected_inventory_discounts of this ItemPriceMarkdown.  # noqa: E501

        A list that defines the sets of selected items for the markdown promotion and the discount specified for promotion.  # noqa: E501

        :return: The selected_inventory_discounts of this ItemPriceMarkdown.  # noqa: E501
        :rtype: list[SelectedInventoryDiscount]
        """
        return self._selected_inventory_discounts

    @selected_inventory_discounts.setter
    def selected_inventory_discounts(self, selected_inventory_discounts):
        """Sets the selected_inventory_discounts of this ItemPriceMarkdown.

        A list that defines the sets of selected items for the markdown promotion and the discount specified for promotion.  # noqa: E501

        :param selected_inventory_discounts: The selected_inventory_discounts of this ItemPriceMarkdown.  # noqa: E501
        :type: list[SelectedInventoryDiscount]
        """

        self._selected_inventory_discounts = selected_inventory_discounts

    @property
    def start_date(self):
        """Gets the start_date of this ItemPriceMarkdown.  # noqa: E501

        The date and time the promotion starts in UTC format (yyyy-MM-ddThh:mm:ssZ). For display purposes, convert this time into the local time of the seller.  # noqa: E501

        :return: The start_date of this ItemPriceMarkdown.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ItemPriceMarkdown.

        The date and time the promotion starts in UTC format (yyyy-MM-ddThh:mm:ssZ). For display purposes, convert this time into the local time of the seller.  # noqa: E501

        :param start_date: The start_date of this ItemPriceMarkdown.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

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
        if issubclass(ItemPriceMarkdown, dict):
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
        if not isinstance(other, ItemPriceMarkdown):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
