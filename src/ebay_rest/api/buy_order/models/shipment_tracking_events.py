# coding: utf-8

"""
    Order API

    The Order API provides interfaces that lets shoppers pay for items (for both eBay guest and eBay member buyers). It also returns payment and shipping status of the order. It enables eBay partners to use accept payment without being <a href=\"https://www.pcisecuritystandards.org/\">PCI compliant</a> and use the <a href=\"/api-docs/buy/static/api-order.html#Post\">Post Order API</a> for returns and cancellations for eBay member buyers.   <p>The Order API has the following resources:  </p>  <ul>  <li><b>checkout_session:</b> Lets eBay members purchase items using PayPal or a credit card.</li>  <li><b>guest_checkout_session:</b> Lets eBay guests purchase items using a credit card or the <a href=\"/api-docs/buy/static/api-order.html#spb-checkout\">PayPal Smart Button</a>.</li>   <li><b>proxy_guest_checkout_session:</b> Lets eBay guests purchase items through a <a href=\"/api-docs/buy/static/api-order.html#vsp-checkout\">vault service provider</a> (VSP). &nbsp;&nbsp;<b>*Note:* </b>Due to the requirement of having a VSP, this resource is not available in the eBay <a href=\"https://developer.ebay.com/my/api_test_tool?index=0\">API Explorer</a>.</li>  <li><b>guest_purchase_order</b> and <b>purchase_order:</b> Lets eBay partners track the payment status and show the buyers their purchase order. </li> </ul>  # noqa: E501

    OpenAPI spec version: v1_beta.29.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ShipmentTrackingEvents(object):
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
        'description': 'str',
        'event_date': 'str',
        'event_type': 'str',
        'location': 'EventLocation'
    }

    attribute_map = {
        'description': 'description',
        'event_date': 'eventDate',
        'event_type': 'eventType',
        'location': 'location'
    }

    def __init__(self, description=None, event_date=None, event_type=None, location=None):  # noqa: E501
        """ShipmentTrackingEvents - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._event_date = None
        self._event_type = None
        self._location = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if event_date is not None:
            self.event_date = event_date
        if event_type is not None:
            self.event_type = event_type
        if location is not None:
            self.location = location

    @property
    def description(self):
        """Gets the description of this ShipmentTrackingEvents.  # noqa: E501

        A string describing the tracking event. For example: On FedEx vehicle for delivery  # noqa: E501

        :return: The description of this ShipmentTrackingEvents.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShipmentTrackingEvents.

        A string describing the tracking event. For example: On FedEx vehicle for delivery  # noqa: E501

        :param description: The description of this ShipmentTrackingEvents.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def event_date(self):
        """Gets the event_date of this ShipmentTrackingEvents.  # noqa: E501

        The date of the shipment tracking event. UTC Format: yyyy-MM-ddThh:00:00.000Z For example: 2019-03-01T12:12:00.000Z  # noqa: E501

        :return: The event_date of this ShipmentTrackingEvents.  # noqa: E501
        :rtype: str
        """
        return self._event_date

    @event_date.setter
    def event_date(self, event_date):
        """Sets the event_date of this ShipmentTrackingEvents.

        The date of the shipment tracking event. UTC Format: yyyy-MM-ddThh:00:00.000Z For example: 2019-03-01T12:12:00.000Z  # noqa: E501

        :param event_date: The event_date of this ShipmentTrackingEvents.  # noqa: E501
        :type: str
        """

        self._event_date = event_date

    @property
    def event_type(self):
        """Gets the event_type of this ShipmentTrackingEvents.  # noqa: E501

        A normalized string for shipment tracking event. For example: OUT_FOR_DELIVERY  # noqa: E501

        :return: The event_type of this ShipmentTrackingEvents.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this ShipmentTrackingEvents.

        A normalized string for shipment tracking event. For example: OUT_FOR_DELIVERY  # noqa: E501

        :param event_type: The event_type of this ShipmentTrackingEvents.  # noqa: E501
        :type: str
        """

        self._event_type = event_type

    @property
    def location(self):
        """Gets the location of this ShipmentTrackingEvents.  # noqa: E501


        :return: The location of this ShipmentTrackingEvents.  # noqa: E501
        :rtype: EventLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ShipmentTrackingEvents.


        :param location: The location of this ShipmentTrackingEvents.  # noqa: E501
        :type: EventLocation
        """

        self._location = location

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
        if issubclass(ShipmentTrackingEvents, dict):
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
        if not isinstance(other, ShipmentTrackingEvents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other