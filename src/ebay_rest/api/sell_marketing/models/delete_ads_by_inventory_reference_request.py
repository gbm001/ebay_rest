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

class DeleteAdsByInventoryReferenceRequest(object):
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
        'inventory_reference_id': 'str',
        'inventory_reference_type': 'str'
    }

    attribute_map = {
        'inventory_reference_id': 'inventoryReferenceId',
        'inventory_reference_type': 'inventoryReferenceType'
    }

    def __init__(self, inventory_reference_id=None, inventory_reference_type=None):  # noqa: E501
        """DeleteAdsByInventoryReferenceRequest - a model defined in Swagger"""  # noqa: E501
        self._inventory_reference_id = None
        self._inventory_reference_type = None
        self.discriminator = None
        if inventory_reference_id is not None:
            self.inventory_reference_id = inventory_reference_id
        if inventory_reference_type is not None:
            self.inventory_reference_type = inventory_reference_type

    @property
    def inventory_reference_id(self):
        """Gets the inventory_reference_id of this DeleteAdsByInventoryReferenceRequest.  # noqa: E501

        An ID that identifies an a single-item listing or multiple-variation listing that is managed with the Inventory API. The inventory reference ID is a seller-defined value that can be either an SKU for a single-item listing or an inventoryItemGroupKey for a multiple-value listing.  # noqa: E501

        :return: The inventory_reference_id of this DeleteAdsByInventoryReferenceRequest.  # noqa: E501
        :rtype: str
        """
        return self._inventory_reference_id

    @inventory_reference_id.setter
    def inventory_reference_id(self, inventory_reference_id):
        """Sets the inventory_reference_id of this DeleteAdsByInventoryReferenceRequest.

        An ID that identifies an a single-item listing or multiple-variation listing that is managed with the Inventory API. The inventory reference ID is a seller-defined value that can be either an SKU for a single-item listing or an inventoryItemGroupKey for a multiple-value listing.  # noqa: E501

        :param inventory_reference_id: The inventory_reference_id of this DeleteAdsByInventoryReferenceRequest.  # noqa: E501
        :type: str
        """

        self._inventory_reference_id = inventory_reference_id

    @property
    def inventory_reference_type(self):
        """Gets the inventory_reference_type of this DeleteAdsByInventoryReferenceRequest.  # noqa: E501

        Indicates the type of item the inventoryReferenceId references. The item can be either an INVENTORY_ITEM or INVENTORY_ITEM_GROUP. You must always pair an inventoryReferenceId with and inventoryReferenceType. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/pls:InventoryReferenceTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The inventory_reference_type of this DeleteAdsByInventoryReferenceRequest.  # noqa: E501
        :rtype: str
        """
        return self._inventory_reference_type

    @inventory_reference_type.setter
    def inventory_reference_type(self, inventory_reference_type):
        """Sets the inventory_reference_type of this DeleteAdsByInventoryReferenceRequest.

        Indicates the type of item the inventoryReferenceId references. The item can be either an INVENTORY_ITEM or INVENTORY_ITEM_GROUP. You must always pair an inventoryReferenceId with and inventoryReferenceType. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/pls:InventoryReferenceTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param inventory_reference_type: The inventory_reference_type of this DeleteAdsByInventoryReferenceRequest.  # noqa: E501
        :type: str
        """

        self._inventory_reference_type = inventory_reference_type

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
        if issubclass(DeleteAdsByInventoryReferenceRequest, dict):
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
        if not isinstance(other, DeleteAdsByInventoryReferenceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
