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

class LineItemFulfillmentInstructions(object):
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
        'guaranteed_delivery': 'bool',
        'max_estimated_delivery_date': 'str',
        'min_estimated_delivery_date': 'str',
        'ship_by_date': 'str'
    }

    attribute_map = {
        'guaranteed_delivery': 'guaranteedDelivery',
        'max_estimated_delivery_date': 'maxEstimatedDeliveryDate',
        'min_estimated_delivery_date': 'minEstimatedDeliveryDate',
        'ship_by_date': 'shipByDate'
    }

    def __init__(self, guaranteed_delivery=None, max_estimated_delivery_date=None, min_estimated_delivery_date=None, ship_by_date=None):  # noqa: E501
        """LineItemFulfillmentInstructions - a model defined in Swagger"""  # noqa: E501
        self._guaranteed_delivery = None
        self._max_estimated_delivery_date = None
        self._min_estimated_delivery_date = None
        self._ship_by_date = None
        self.discriminator = None
        if guaranteed_delivery is not None:
            self.guaranteed_delivery = guaranteed_delivery
        if max_estimated_delivery_date is not None:
            self.max_estimated_delivery_date = max_estimated_delivery_date
        if min_estimated_delivery_date is not None:
            self.min_estimated_delivery_date = min_estimated_delivery_date
        if ship_by_date is not None:
            self.ship_by_date = ship_by_date

    @property
    def guaranteed_delivery(self):
        """Gets the guaranteed_delivery of this LineItemFulfillmentInstructions.  # noqa: E501

        This field is returned as true if the order line item is qualified for eBay Guaranteed Delivery, or false if it is not eligible. Only domestic shipments are available for eBay Guaranteed Delivery. At this time, eBay Guaranteed Delivery is only available to a select number of sellers on the US and Australia sites, but this feature will be enabled on more eBay sites in 2019. There are two different eBay Guaranteed Delivery options - 'Handling time' option and 'Door-to-Door' option. With both options, the seller is commiting to getting the order delivered to the buyer within three business days after purchase. With the 'Handling time' option, the seller's stated handling time for a listing must be 'same-day' or '1-day', and at least one of the available shipping service options should have a shipping time that guarantees that the buyer receives the order on time. With this option, eBay will set the 'ship-by date' and expected delivery window for the seller, and the seller should just make sure they physically ship the order by the shipToDate. With the 'Door-to-door' option, the seller must create regional shipping rate tables (with shipping costs and delivery times based on destination regions), and then apply these regional shipping rates/delivery times to the listing. If a 'Door-to-door' order does not arrive on time, the seller must refund the buyer the full shipping cost (if any), and the buyer also has the option of returning the item for a full refund, and the seller will also have to pay the return shipping cost. With 'Handling time' option, as long as the seller meets the stated handling time, and ships using the correct shipping service option, eBay will refund the buyer the shipping cost and pay for return shipping label (if buyer wants to return item) if the order arrives after the expected delivery time. For more information on the details and requirements of eBay Guaranteed Delivery, see the Offering eBay Guaranteed Delivery help topic. This field will always be returned regardless of whether the listing site offers eBay Guaranteed Delivery or if the seller is opted in to the feature.  # noqa: E501

        :return: The guaranteed_delivery of this LineItemFulfillmentInstructions.  # noqa: E501
        :rtype: bool
        """
        return self._guaranteed_delivery

    @guaranteed_delivery.setter
    def guaranteed_delivery(self, guaranteed_delivery):
        """Sets the guaranteed_delivery of this LineItemFulfillmentInstructions.

        This field is returned as true if the order line item is qualified for eBay Guaranteed Delivery, or false if it is not eligible. Only domestic shipments are available for eBay Guaranteed Delivery. At this time, eBay Guaranteed Delivery is only available to a select number of sellers on the US and Australia sites, but this feature will be enabled on more eBay sites in 2019. There are two different eBay Guaranteed Delivery options - 'Handling time' option and 'Door-to-Door' option. With both options, the seller is commiting to getting the order delivered to the buyer within three business days after purchase. With the 'Handling time' option, the seller's stated handling time for a listing must be 'same-day' or '1-day', and at least one of the available shipping service options should have a shipping time that guarantees that the buyer receives the order on time. With this option, eBay will set the 'ship-by date' and expected delivery window for the seller, and the seller should just make sure they physically ship the order by the shipToDate. With the 'Door-to-door' option, the seller must create regional shipping rate tables (with shipping costs and delivery times based on destination regions), and then apply these regional shipping rates/delivery times to the listing. If a 'Door-to-door' order does not arrive on time, the seller must refund the buyer the full shipping cost (if any), and the buyer also has the option of returning the item for a full refund, and the seller will also have to pay the return shipping cost. With 'Handling time' option, as long as the seller meets the stated handling time, and ships using the correct shipping service option, eBay will refund the buyer the shipping cost and pay for return shipping label (if buyer wants to return item) if the order arrives after the expected delivery time. For more information on the details and requirements of eBay Guaranteed Delivery, see the Offering eBay Guaranteed Delivery help topic. This field will always be returned regardless of whether the listing site offers eBay Guaranteed Delivery or if the seller is opted in to the feature.  # noqa: E501

        :param guaranteed_delivery: The guaranteed_delivery of this LineItemFulfillmentInstructions.  # noqa: E501
        :type: bool
        """

        self._guaranteed_delivery = guaranteed_delivery

    @property
    def max_estimated_delivery_date(self):
        """Gets the max_estimated_delivery_date of this LineItemFulfillmentInstructions.  # noqa: E501

        The estimated latest date and time that the buyer can expect to receive the line item based on the seller's stated handling time and the transit times of the available shipping service options. If the listing is eligible for eBay Guaranteed Delivery (value of guaranteedDelivery field is true, the seller must pay extra attention to this date, as a failure to deliver by this date/time can result in a 'Late shipment' seller defect, and can affect seller level and Top-Rated Seller status. In addition to the seller defect, buyers will be eligible for a shipping cost refund, and will also be eligible to return the item for a full refund (with no return shipping charge) if they choose. Note: This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. Format: [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z Example: 2015-08-04T19:09:02.768Z  # noqa: E501

        :return: The max_estimated_delivery_date of this LineItemFulfillmentInstructions.  # noqa: E501
        :rtype: str
        """
        return self._max_estimated_delivery_date

    @max_estimated_delivery_date.setter
    def max_estimated_delivery_date(self, max_estimated_delivery_date):
        """Sets the max_estimated_delivery_date of this LineItemFulfillmentInstructions.

        The estimated latest date and time that the buyer can expect to receive the line item based on the seller's stated handling time and the transit times of the available shipping service options. If the listing is eligible for eBay Guaranteed Delivery (value of guaranteedDelivery field is true, the seller must pay extra attention to this date, as a failure to deliver by this date/time can result in a 'Late shipment' seller defect, and can affect seller level and Top-Rated Seller status. In addition to the seller defect, buyers will be eligible for a shipping cost refund, and will also be eligible to return the item for a full refund (with no return shipping charge) if they choose. Note: This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. Format: [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z Example: 2015-08-04T19:09:02.768Z  # noqa: E501

        :param max_estimated_delivery_date: The max_estimated_delivery_date of this LineItemFulfillmentInstructions.  # noqa: E501
        :type: str
        """

        self._max_estimated_delivery_date = max_estimated_delivery_date

    @property
    def min_estimated_delivery_date(self):
        """Gets the min_estimated_delivery_date of this LineItemFulfillmentInstructions.  # noqa: E501

        The estimated earliest date and time that the buyer can expect to receive the line item based on the seller's stated handling time and the transit times of the available shipping service options. Note: This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. Format: [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z Example: 2015-08-04T19:09:02.768Z  # noqa: E501

        :return: The min_estimated_delivery_date of this LineItemFulfillmentInstructions.  # noqa: E501
        :rtype: str
        """
        return self._min_estimated_delivery_date

    @min_estimated_delivery_date.setter
    def min_estimated_delivery_date(self, min_estimated_delivery_date):
        """Sets the min_estimated_delivery_date of this LineItemFulfillmentInstructions.

        The estimated earliest date and time that the buyer can expect to receive the line item based on the seller's stated handling time and the transit times of the available shipping service options. Note: This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. Format: [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z Example: 2015-08-04T19:09:02.768Z  # noqa: E501

        :param min_estimated_delivery_date: The min_estimated_delivery_date of this LineItemFulfillmentInstructions.  # noqa: E501
        :type: str
        """

        self._min_estimated_delivery_date = min_estimated_delivery_date

    @property
    def ship_by_date(self):
        """Gets the ship_by_date of this LineItemFulfillmentInstructions.  # noqa: E501

        The latest date and time by which the seller should ship line item in order to meet the expected delivery window. This timestamp will be set by eBay based on time of purchase and the seller's stated handling time. If the listing is eligible for eBay Guaranteed Delivery (value of guaranteedDelivery field is true, the seller must pay extra attention to this date, as a failure to physically ship the line item by this date/time can result in a 'Late shipment' seller defect, and can affect seller level and Top-Rated Seller status. In addition to the seller defect, buyers will be eligible for a shipping cost refund, and will also be eligible to return the item for a full refund (with no return shipping charge) if they choose. Note: This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. Format: [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z Example: 2015-08-04T19:09:02.768Z  # noqa: E501

        :return: The ship_by_date of this LineItemFulfillmentInstructions.  # noqa: E501
        :rtype: str
        """
        return self._ship_by_date

    @ship_by_date.setter
    def ship_by_date(self, ship_by_date):
        """Sets the ship_by_date of this LineItemFulfillmentInstructions.

        The latest date and time by which the seller should ship line item in order to meet the expected delivery window. This timestamp will be set by eBay based on time of purchase and the seller's stated handling time. If the listing is eligible for eBay Guaranteed Delivery (value of guaranteedDelivery field is true, the seller must pay extra attention to this date, as a failure to physically ship the line item by this date/time can result in a 'Late shipment' seller defect, and can affect seller level and Top-Rated Seller status. In addition to the seller defect, buyers will be eligible for a shipping cost refund, and will also be eligible to return the item for a full refund (with no return shipping charge) if they choose. Note: This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. Format: [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z Example: 2015-08-04T19:09:02.768Z  # noqa: E501

        :param ship_by_date: The ship_by_date of this LineItemFulfillmentInstructions.  # noqa: E501
        :type: str
        """

        self._ship_by_date = ship_by_date

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
        if issubclass(LineItemFulfillmentInstructions, dict):
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
        if not isinstance(other, LineItemFulfillmentInstructions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
