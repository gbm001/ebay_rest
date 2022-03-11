# coding: utf-8

"""
    Browse API

    <p>The Browse API has the following resources:</p>   <ul> <li><b> item_summary: </b> Lets shoppers search for specific items by keyword, GTIN, category, charity, product, or item aspects and refine the results by using filters, such as aspects, compatibility, and fields values.</li>  <li><b> search_by_image: </b><a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />&nbsp;(Experimental)</a> Lets shoppers search for specific items by image. You can refine the results by using URI parameters and filters.</li>   <li><b> item: </b> <ul><li>Lets you retrieve the details of a specific item or all the items in an item group, which is an item with variations such as color and size and check if a product is compatible with the specified item, such as if a specific car is compatible with a specific part.</li> <li>Provides a bridge between the eBay legacy APIs, such as <b> Finding</b>, and the RESTful APIs, which use different formats for the item IDs.</li>  </ul> </li>  <li> <b> shopping_cart: </b> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />&nbsp;(Experimental)</a> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited \" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> Provides the ability for eBay members to see the contents of their eBay cart, and add, remove, and change the quantity of items in their eBay cart.&nbsp;&nbsp;<b> Note: </b> This resource is not available in the eBay API Explorer.</li></ul>       <p>The <b> item_summary</b>, <b> search_by_image</b>, and <b> item</b> resource calls require an <a href=\"/api-docs/static/oauth-client-credentials-grant.html\">Application access token</a>. The <b> shopping_cart</b> resource calls require a <a href=\"/api-docs/static/oauth-authorization-code-grant.html\">User access token</a>.</p>  # noqa: E501

    OpenAPI spec version: v1.13.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AddonService(object):
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
        'selection': 'str',
        'service_fee': 'ConvertedAmount',
        'service_id': 'str',
        'service_type': 'str'
    }

    attribute_map = {
        'selection': 'selection',
        'service_fee': 'serviceFee',
        'service_id': 'serviceId',
        'service_type': 'serviceType'
    }

    def __init__(self, selection=None, service_fee=None, service_id=None, service_type=None):  # noqa: E501
        """AddonService - a model defined in Swagger"""  # noqa: E501
        self._selection = None
        self._service_fee = None
        self._service_id = None
        self._service_type = None
        self.discriminator = None
        if selection is not None:
            self.selection = selection
        if service_fee is not None:
            self.service_fee = service_fee
        if service_id is not None:
            self.service_id = service_id
        if service_type is not None:
            self.service_type = service_type

    @property
    def selection(self):
        """Gets the selection of this AddonService.  # noqa: E501

        This field indicates whether the add-on service must be selected for the item. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:AddonServiceSelectionEnum'>eBay API documentation</a>  # noqa: E501

        :return: The selection of this AddonService.  # noqa: E501
        :rtype: str
        """
        return self._selection

    @selection.setter
    def selection(self, selection):
        """Sets the selection of this AddonService.

        This field indicates whether the add-on service must be selected for the item. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:AddonServiceSelectionEnum'>eBay API documentation</a>  # noqa: E501

        :param selection: The selection of this AddonService.  # noqa: E501
        :type: str
        """

        self._selection = selection

    @property
    def service_fee(self):
        """Gets the service_fee of this AddonService.  # noqa: E501


        :return: The service_fee of this AddonService.  # noqa: E501
        :rtype: ConvertedAmount
        """
        return self._service_fee

    @service_fee.setter
    def service_fee(self, service_fee):
        """Sets the service_fee of this AddonService.


        :param service_fee: The service_fee of this AddonService.  # noqa: E501
        :type: ConvertedAmount
        """

        self._service_fee = service_fee

    @property
    def service_id(self):
        """Gets the service_id of this AddonService.  # noqa: E501

        The ID number of the add-on service.  # noqa: E501

        :return: The service_id of this AddonService.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this AddonService.

        The ID number of the add-on service.  # noqa: E501

        :param service_id: The service_id of this AddonService.  # noqa: E501
        :type: str
        """

        self._service_id = service_id

    @property
    def service_type(self):
        """Gets the service_type of this AddonService.  # noqa: E501

        The type of add-on service, such as AUTHENTICITY_GUARANTEE. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:AddonServiceTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The service_type of this AddonService.  # noqa: E501
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this AddonService.

        The type of add-on service, such as AUTHENTICITY_GUARANTEE. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:AddonServiceTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param service_type: The service_type of this AddonService.  # noqa: E501
        :type: str
        """

        self._service_type = service_type

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
        if issubclass(AddonService, dict):
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
        if not isinstance(other, AddonService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
