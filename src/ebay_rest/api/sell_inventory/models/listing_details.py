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

class ListingDetails(object):
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
        'listing_id': 'str',
        'listing_status': 'str',
        'sold_quantity': 'int'
    }

    attribute_map = {
        'listing_id': 'listingId',
        'listing_status': 'listingStatus',
        'sold_quantity': 'soldQuantity'
    }

    def __init__(self, listing_id=None, listing_status=None, sold_quantity=None):  # noqa: E501
        """ListingDetails - a model defined in Swagger"""  # noqa: E501
        self._listing_id = None
        self._listing_status = None
        self._sold_quantity = None
        self.discriminator = None
        if listing_id is not None:
            self.listing_id = listing_id
        if listing_status is not None:
            self.listing_status = listing_status
        if sold_quantity is not None:
            self.sold_quantity = sold_quantity

    @property
    def listing_id(self):
        """Gets the listing_id of this ListingDetails.  # noqa: E501

        The unique identifier of the eBay listing that is associated with the published offer.   # noqa: E501

        :return: The listing_id of this ListingDetails.  # noqa: E501
        :rtype: str
        """
        return self._listing_id

    @listing_id.setter
    def listing_id(self, listing_id):
        """Sets the listing_id of this ListingDetails.

        The unique identifier of the eBay listing that is associated with the published offer.   # noqa: E501

        :param listing_id: The listing_id of this ListingDetails.  # noqa: E501
        :type: str
        """

        self._listing_id = listing_id

    @property
    def listing_status(self):
        """Gets the listing_status of this ListingDetails.  # noqa: E501

        The enumeration value returned in this field indicates the status of the listing that is associated with the published offer. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:ListingStatusEnum'>eBay API documentation</a>  # noqa: E501

        :return: The listing_status of this ListingDetails.  # noqa: E501
        :rtype: str
        """
        return self._listing_status

    @listing_status.setter
    def listing_status(self, listing_status):
        """Sets the listing_status of this ListingDetails.

        The enumeration value returned in this field indicates the status of the listing that is associated with the published offer. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:ListingStatusEnum'>eBay API documentation</a>  # noqa: E501

        :param listing_status: The listing_status of this ListingDetails.  # noqa: E501
        :type: str
        """

        self._listing_status = listing_status

    @property
    def sold_quantity(self):
        """Gets the sold_quantity of this ListingDetails.  # noqa: E501

        This integer value indicates the quantity of the product that has been sold for the published offer.  # noqa: E501

        :return: The sold_quantity of this ListingDetails.  # noqa: E501
        :rtype: int
        """
        return self._sold_quantity

    @sold_quantity.setter
    def sold_quantity(self, sold_quantity):
        """Sets the sold_quantity of this ListingDetails.

        This integer value indicates the quantity of the product that has been sold for the published offer.  # noqa: E501

        :param sold_quantity: The sold_quantity of this ListingDetails.  # noqa: E501
        :type: int
        """

        self._sold_quantity = sold_quantity

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
        if issubclass(ListingDetails, dict):
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
        if not isinstance(other, ListingDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
