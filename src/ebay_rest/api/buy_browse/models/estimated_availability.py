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

class EstimatedAvailability(object):
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
        'availability_threshold': 'int',
        'availability_threshold_type': 'str',
        'delivery_options': 'list[str]',
        'estimated_availability_status': 'str',
        'estimated_available_quantity': 'int',
        'estimated_sold_quantity': 'int'
    }

    attribute_map = {
        'availability_threshold': 'availabilityThreshold',
        'availability_threshold_type': 'availabilityThresholdType',
        'delivery_options': 'deliveryOptions',
        'estimated_availability_status': 'estimatedAvailabilityStatus',
        'estimated_available_quantity': 'estimatedAvailableQuantity',
        'estimated_sold_quantity': 'estimatedSoldQuantity'
    }

    def __init__(self, availability_threshold=None, availability_threshold_type=None, delivery_options=None, estimated_availability_status=None, estimated_available_quantity=None, estimated_sold_quantity=None):  # noqa: E501
        """EstimatedAvailability - a model defined in Swagger"""  # noqa: E501
        self._availability_threshold = None
        self._availability_threshold_type = None
        self._delivery_options = None
        self._estimated_availability_status = None
        self._estimated_available_quantity = None
        self._estimated_sold_quantity = None
        self.discriminator = None
        if availability_threshold is not None:
            self.availability_threshold = availability_threshold
        if availability_threshold_type is not None:
            self.availability_threshold_type = availability_threshold_type
        if delivery_options is not None:
            self.delivery_options = delivery_options
        if estimated_availability_status is not None:
            self.estimated_availability_status = estimated_availability_status
        if estimated_available_quantity is not None:
            self.estimated_available_quantity = estimated_available_quantity
        if estimated_sold_quantity is not None:
            self.estimated_sold_quantity = estimated_sold_quantity

    @property
    def availability_threshold(self):
        """Gets the availability_threshold of this EstimatedAvailability.  # noqa: E501

        This field is return only when the seller sets their '<a href=\"#display-item-quantity\">display item quantity</a>' preference to <b> Display \"More than 10 available\" in your listing (if applicable)</b>. The value of this field will be \"10\", which is the threshold value. <br /><br />Code so that your app gracefully handles any future changes to this value.  # noqa: E501

        :return: The availability_threshold of this EstimatedAvailability.  # noqa: E501
        :rtype: int
        """
        return self._availability_threshold

    @availability_threshold.setter
    def availability_threshold(self, availability_threshold):
        """Sets the availability_threshold of this EstimatedAvailability.

        This field is return only when the seller sets their '<a href=\"#display-item-quantity\">display item quantity</a>' preference to <b> Display \"More than 10 available\" in your listing (if applicable)</b>. The value of this field will be \"10\", which is the threshold value. <br /><br />Code so that your app gracefully handles any future changes to this value.  # noqa: E501

        :param availability_threshold: The availability_threshold of this EstimatedAvailability.  # noqa: E501
        :type: int
        """

        self._availability_threshold = availability_threshold

    @property
    def availability_threshold_type(self):
        """Gets the availability_threshold_type of this EstimatedAvailability.  # noqa: E501

        <a name=\"display-item-quantity\"></a> This field is return only when the seller sets their <b> Display Item Quantity</b> preference to <b> Display \"More than 10 available\" in your listing (if applicable)</b>. The value of this field will be <code> MORE_THAN</code>. This indicates that the seller has more than the 'quantity display preference', which is 10, in stock for this item.    <br /><br /> The following are the display item quantity preferences the seller can set. <br /><ul><li> <b> Display \"More than 10 available\" in your listing (if applicable) </b><ul> <li>If the seller enables this preference, this field is returned as long as there are more than 10 of this item in inventory.</li>  <li> If the quantity is equal to 10 or drops below 10, this field is not returned and the estimated quantity of the item is returned in the <b> estimatedAvailableQuantity</b> field.</li></ul> </li> <li> <b> Display the exact quantity in your items</b> <br />If the seller enables this preference, the <b> availabilityThresholdType</b> and <b> availabilityThreshold</b> fields are not returned and the estimated quantity of the item is returned in the <b> estimatedAvailableQuantity</b> field.<br /><br /><b> Note: </b> Because the quantity of an item can change several times within a second, it is impossible to return the exact quantity. </li></ul>   <br />Code so that your app gracefully handles any future changes to these preferences. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:AvailabilityThresholdEnum'>eBay API documentation</a>  # noqa: E501

        :return: The availability_threshold_type of this EstimatedAvailability.  # noqa: E501
        :rtype: str
        """
        return self._availability_threshold_type

    @availability_threshold_type.setter
    def availability_threshold_type(self, availability_threshold_type):
        """Sets the availability_threshold_type of this EstimatedAvailability.

        <a name=\"display-item-quantity\"></a> This field is return only when the seller sets their <b> Display Item Quantity</b> preference to <b> Display \"More than 10 available\" in your listing (if applicable)</b>. The value of this field will be <code> MORE_THAN</code>. This indicates that the seller has more than the 'quantity display preference', which is 10, in stock for this item.    <br /><br /> The following are the display item quantity preferences the seller can set. <br /><ul><li> <b> Display \"More than 10 available\" in your listing (if applicable) </b><ul> <li>If the seller enables this preference, this field is returned as long as there are more than 10 of this item in inventory.</li>  <li> If the quantity is equal to 10 or drops below 10, this field is not returned and the estimated quantity of the item is returned in the <b> estimatedAvailableQuantity</b> field.</li></ul> </li> <li> <b> Display the exact quantity in your items</b> <br />If the seller enables this preference, the <b> availabilityThresholdType</b> and <b> availabilityThreshold</b> fields are not returned and the estimated quantity of the item is returned in the <b> estimatedAvailableQuantity</b> field.<br /><br /><b> Note: </b> Because the quantity of an item can change several times within a second, it is impossible to return the exact quantity. </li></ul>   <br />Code so that your app gracefully handles any future changes to these preferences. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:AvailabilityThresholdEnum'>eBay API documentation</a>  # noqa: E501

        :param availability_threshold_type: The availability_threshold_type of this EstimatedAvailability.  # noqa: E501
        :type: str
        """

        self._availability_threshold_type = availability_threshold_type

    @property
    def delivery_options(self):
        """Gets the delivery_options of this EstimatedAvailability.  # noqa: E501

        An array of available delivery options. <br><br><b> Valid Values: </b> SHIP_TO_HOME, SELLER_ARRANGED_LOCAL_PICKUP, IN_STORE_PICKUP, PICKUP_DROP_OFF, or DIGITAL_DELIVERY <br /><br />Code so that your app gracefully handles any future changes to this list.   # noqa: E501

        :return: The delivery_options of this EstimatedAvailability.  # noqa: E501
        :rtype: list[str]
        """
        return self._delivery_options

    @delivery_options.setter
    def delivery_options(self, delivery_options):
        """Sets the delivery_options of this EstimatedAvailability.

        An array of available delivery options. <br><br><b> Valid Values: </b> SHIP_TO_HOME, SELLER_ARRANGED_LOCAL_PICKUP, IN_STORE_PICKUP, PICKUP_DROP_OFF, or DIGITAL_DELIVERY <br /><br />Code so that your app gracefully handles any future changes to this list.   # noqa: E501

        :param delivery_options: The delivery_options of this EstimatedAvailability.  # noqa: E501
        :type: list[str]
        """

        self._delivery_options = delivery_options

    @property
    def estimated_availability_status(self):
        """Gets the estimated_availability_status of this EstimatedAvailability.  # noqa: E501

        An enumeration value representing the inventory status of this item.<br /><br /><span class=\"tablenote\"><b> Note: </b>Be sure to review the <b>itemEndDate</b> field to determine whether the item is available for purchase.</span><br><br><b> Valid Values: </b> IN_STOCK, LIMITED_STOCK, or OUT_OF_STOCK <br /><br />Code so that your app gracefully handles any future changes to this list. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:AvailabilityStatusEnum'>eBay API documentation</a>  # noqa: E501

        :return: The estimated_availability_status of this EstimatedAvailability.  # noqa: E501
        :rtype: str
        """
        return self._estimated_availability_status

    @estimated_availability_status.setter
    def estimated_availability_status(self, estimated_availability_status):
        """Sets the estimated_availability_status of this EstimatedAvailability.

        An enumeration value representing the inventory status of this item.<br /><br /><span class=\"tablenote\"><b> Note: </b>Be sure to review the <b>itemEndDate</b> field to determine whether the item is available for purchase.</span><br><br><b> Valid Values: </b> IN_STOCK, LIMITED_STOCK, or OUT_OF_STOCK <br /><br />Code so that your app gracefully handles any future changes to this list. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:AvailabilityStatusEnum'>eBay API documentation</a>  # noqa: E501

        :param estimated_availability_status: The estimated_availability_status of this EstimatedAvailability.  # noqa: E501
        :type: str
        """

        self._estimated_availability_status = estimated_availability_status

    @property
    def estimated_available_quantity(self):
        """Gets the estimated_available_quantity of this EstimatedAvailability.  # noqa: E501

        The estimated number of this item that are available for purchase. Because the quantity of an item can change several times within a second, it is impossible to return the exact quantity. So instead of returning quantity, the estimated availability of the item is returned.  # noqa: E501

        :return: The estimated_available_quantity of this EstimatedAvailability.  # noqa: E501
        :rtype: int
        """
        return self._estimated_available_quantity

    @estimated_available_quantity.setter
    def estimated_available_quantity(self, estimated_available_quantity):
        """Sets the estimated_available_quantity of this EstimatedAvailability.

        The estimated number of this item that are available for purchase. Because the quantity of an item can change several times within a second, it is impossible to return the exact quantity. So instead of returning quantity, the estimated availability of the item is returned.  # noqa: E501

        :param estimated_available_quantity: The estimated_available_quantity of this EstimatedAvailability.  # noqa: E501
        :type: int
        """

        self._estimated_available_quantity = estimated_available_quantity

    @property
    def estimated_sold_quantity(self):
        """Gets the estimated_sold_quantity of this EstimatedAvailability.  # noqa: E501

        The estimated number of this item that have been sold.  # noqa: E501

        :return: The estimated_sold_quantity of this EstimatedAvailability.  # noqa: E501
        :rtype: int
        """
        return self._estimated_sold_quantity

    @estimated_sold_quantity.setter
    def estimated_sold_quantity(self, estimated_sold_quantity):
        """Sets the estimated_sold_quantity of this EstimatedAvailability.

        The estimated number of this item that have been sold.  # noqa: E501

        :param estimated_sold_quantity: The estimated_sold_quantity of this EstimatedAvailability.  # noqa: E501
        :type: int
        """

        self._estimated_sold_quantity = estimated_sold_quantity

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
        if issubclass(EstimatedAvailability, dict):
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
        if not isinstance(other, EstimatedAvailability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
