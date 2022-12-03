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

class PackageWeightAndSize(object):
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
        'dimensions': 'Dimension',
        'package_type': 'str',
        'weight': 'Weight'
    }

    attribute_map = {
        'dimensions': 'dimensions',
        'package_type': 'packageType',
        'weight': 'weight'
    }

    def __init__(self, dimensions=None, package_type=None, weight=None):  # noqa: E501
        """PackageWeightAndSize - a model defined in Swagger"""  # noqa: E501
        self._dimensions = None
        self._package_type = None
        self._weight = None
        self.discriminator = None
        if dimensions is not None:
            self.dimensions = dimensions
        if package_type is not None:
            self.package_type = package_type
        if weight is not None:
            self.weight = weight

    @property
    def dimensions(self):
        """Gets the dimensions of this PackageWeightAndSize.  # noqa: E501


        :return: The dimensions of this PackageWeightAndSize.  # noqa: E501
        :rtype: Dimension
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this PackageWeightAndSize.


        :param dimensions: The dimensions of this PackageWeightAndSize.  # noqa: E501
        :type: Dimension
        """

        self._dimensions = dimensions

    @property
    def package_type(self):
        """Gets the package_type of this PackageWeightAndSize.  # noqa: E501

        This enumeration value indicates the type of shipping package used to ship the inventory item. The supported values for this field can be found in the <a href=\"/api-docs/sell/inventory/types/slr:PackageTypeEnum\">PackageTypeEnum</a> type.<br/><br/>This field will be returned if the package type is set for the inventory item.<br /><br /><span class=\"tablenote\"> <strong>Note:</strong> You can use the <a href=\"/Devzone/XML/docs/Reference/eBay/GeteBayDetails.html#Response.ShippingPackageDetails\">GeteBayDetails</a> Trading API call to retrieve a list of supported package types for a specific marketplace.</span> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:PackageTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The package_type of this PackageWeightAndSize.  # noqa: E501
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """Sets the package_type of this PackageWeightAndSize.

        This enumeration value indicates the type of shipping package used to ship the inventory item. The supported values for this field can be found in the <a href=\"/api-docs/sell/inventory/types/slr:PackageTypeEnum\">PackageTypeEnum</a> type.<br/><br/>This field will be returned if the package type is set for the inventory item.<br /><br /><span class=\"tablenote\"> <strong>Note:</strong> You can use the <a href=\"/Devzone/XML/docs/Reference/eBay/GeteBayDetails.html#Response.ShippingPackageDetails\">GeteBayDetails</a> Trading API call to retrieve a list of supported package types for a specific marketplace.</span> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:PackageTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param package_type: The package_type of this PackageWeightAndSize.  # noqa: E501
        :type: str
        """

        self._package_type = package_type

    @property
    def weight(self):
        """Gets the weight of this PackageWeightAndSize.  # noqa: E501


        :return: The weight of this PackageWeightAndSize.  # noqa: E501
        :rtype: Weight
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this PackageWeightAndSize.


        :param weight: The weight of this PackageWeightAndSize.  # noqa: E501
        :type: Weight
        """

        self._weight = weight

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
        if issubclass(PackageWeightAndSize, dict):
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
        if not isinstance(other, PackageWeightAndSize):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
