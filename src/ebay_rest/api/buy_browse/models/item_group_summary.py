# coding: utf-8

"""
    Browse API

    <p>The Browse API has the following resources:</p>   <ul> <li><b> item_summary: </b> Lets shoppers search for specific items by keyword, GTIN, category, charity, product, or item aspects and refine the results by using filters, such as aspects, compatibility, and fields values.</li>  <li><b> search_by_image: </b><a href=\"https://developer.ebay.com/api-docs/static/versioning.html#API\" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />&nbsp;(Experimental)</a> Lets shoppers search for specific items by image. You can refine the results by using URI parameters and filters.</li>   <li><b> item: </b> <ul><li>Lets you retrieve the details of a specific item or all the items in an item group, which is an item with variations such as color and size and check if a product is compatible with the specified item, such as if a specific car is compatible with a specific part.</li> <li>Provides a bridge between the eBay legacy APIs, such as <b> Finding</b>, and the RESTful APIs, which use different formats for the item IDs.</li>  </ul> </li>  <li> <b> shopping_cart: </b> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#API\" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />&nbsp;(Experimental)</a> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#Limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> Provides the ability for eBay members to see the contents of their eBay cart, and add, remove, and change the quantity of items in their eBay cart.&nbsp;&nbsp;<b> Note: </b> This resource is not available in the eBay API Explorer.</li></ul>       <p>The <b> item_summary</b>, <b> search_by_image</b>, and <b> item</b> resource calls require an <a href=\"/api-docs/static/oauth-client-credentials-grant.html\">Application access token</a>. The <b> shopping_cart</b> resource calls require a <a href=\"/api-docs/static/oauth-authorization-code-grant.html\">User access token</a>.</p>  # noqa: E501

    OpenAPI spec version: v1.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ItemGroupSummary(object):
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
        'item_group_additional_images': 'list[Image]',
        'item_group_href': 'str',
        'item_group_id': 'str',
        'item_group_image': 'Image',
        'item_group_title': 'str',
        'item_group_type': 'str'
    }

    attribute_map = {
        'item_group_additional_images': 'itemGroupAdditionalImages',
        'item_group_href': 'itemGroupHref',
        'item_group_id': 'itemGroupId',
        'item_group_image': 'itemGroupImage',
        'item_group_title': 'itemGroupTitle',
        'item_group_type': 'itemGroupType'
    }

    def __init__(self, item_group_additional_images=None, item_group_href=None, item_group_id=None, item_group_image=None, item_group_title=None, item_group_type=None):  # noqa: E501
        """ItemGroupSummary - a model defined in Swagger"""  # noqa: E501
        self._item_group_additional_images = None
        self._item_group_href = None
        self._item_group_id = None
        self._item_group_image = None
        self._item_group_title = None
        self._item_group_type = None
        self.discriminator = None
        if item_group_additional_images is not None:
            self.item_group_additional_images = item_group_additional_images
        if item_group_href is not None:
            self.item_group_href = item_group_href
        if item_group_id is not None:
            self.item_group_id = item_group_id
        if item_group_image is not None:
            self.item_group_image = item_group_image
        if item_group_title is not None:
            self.item_group_title = item_group_title
        if item_group_type is not None:
            self.item_group_type = item_group_type

    @property
    def item_group_additional_images(self):
        """Gets the item_group_additional_images of this ItemGroupSummary.  # noqa: E501

        An array of containers with the URLs for images that are in addition to the primary image of the item group. The primary image is returned in the itemGroupImage field.  # noqa: E501

        :return: The item_group_additional_images of this ItemGroupSummary.  # noqa: E501
        :rtype: list[Image]
        """
        return self._item_group_additional_images

    @item_group_additional_images.setter
    def item_group_additional_images(self, item_group_additional_images):
        """Sets the item_group_additional_images of this ItemGroupSummary.

        An array of containers with the URLs for images that are in addition to the primary image of the item group. The primary image is returned in the itemGroupImage field.  # noqa: E501

        :param item_group_additional_images: The item_group_additional_images of this ItemGroupSummary.  # noqa: E501
        :type: list[Image]
        """

        self._item_group_additional_images = item_group_additional_images

    @property
    def item_group_href(self):
        """Gets the item_group_href of this ItemGroupSummary.  # noqa: E501

        The HATEOAS reference of the parent page of the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.  # noqa: E501

        :return: The item_group_href of this ItemGroupSummary.  # noqa: E501
        :rtype: str
        """
        return self._item_group_href

    @item_group_href.setter
    def item_group_href(self, item_group_href):
        """Sets the item_group_href of this ItemGroupSummary.

        The HATEOAS reference of the parent page of the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.  # noqa: E501

        :param item_group_href: The item_group_href of this ItemGroupSummary.  # noqa: E501
        :type: str
        """

        self._item_group_href = item_group_href

    @property
    def item_group_id(self):
        """Gets the item_group_id of this ItemGroupSummary.  # noqa: E501

        The unique identifier for the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.  # noqa: E501

        :return: The item_group_id of this ItemGroupSummary.  # noqa: E501
        :rtype: str
        """
        return self._item_group_id

    @item_group_id.setter
    def item_group_id(self, item_group_id):
        """Sets the item_group_id of this ItemGroupSummary.

        The unique identifier for the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.  # noqa: E501

        :param item_group_id: The item_group_id of this ItemGroupSummary.  # noqa: E501
        :type: str
        """

        self._item_group_id = item_group_id

    @property
    def item_group_image(self):
        """Gets the item_group_image of this ItemGroupSummary.  # noqa: E501


        :return: The item_group_image of this ItemGroupSummary.  # noqa: E501
        :rtype: Image
        """
        return self._item_group_image

    @item_group_image.setter
    def item_group_image(self, item_group_image):
        """Sets the item_group_image of this ItemGroupSummary.


        :param item_group_image: The item_group_image of this ItemGroupSummary.  # noqa: E501
        :type: Image
        """

        self._item_group_image = item_group_image

    @property
    def item_group_title(self):
        """Gets the item_group_title of this ItemGroupSummary.  # noqa: E501

        The title of the item that appears on the item group page. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.  # noqa: E501

        :return: The item_group_title of this ItemGroupSummary.  # noqa: E501
        :rtype: str
        """
        return self._item_group_title

    @item_group_title.setter
    def item_group_title(self, item_group_title):
        """Sets the item_group_title of this ItemGroupSummary.

        The title of the item that appears on the item group page. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc.  # noqa: E501

        :param item_group_title: The item_group_title of this ItemGroupSummary.  # noqa: E501
        :type: str
        """

        self._item_group_title = item_group_title

    @property
    def item_group_type(self):
        """Gets the item_group_type of this ItemGroupSummary.  # noqa: E501

        An enumeration value that indicates the type of the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:ItemGroupTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The item_group_type of this ItemGroupSummary.  # noqa: E501
        :rtype: str
        """
        return self._item_group_type

    @item_group_type.setter
    def item_group_type(self, item_group_type):
        """Sets the item_group_type of this ItemGroupSummary.

        An enumeration value that indicates the type of the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:ItemGroupTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param item_group_type: The item_group_type of this ItemGroupSummary.  # noqa: E501
        :type: str
        """

        self._item_group_type = item_group_type

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
        if issubclass(ItemGroupSummary, dict):
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
        if not isinstance(other, ItemGroupSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
