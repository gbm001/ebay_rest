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

class Dimension(object):
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
        'annotation_keys': 'list[str]',
        'dimension_key': 'str'
    }

    attribute_map = {
        'annotation_keys': 'annotationKeys',
        'dimension_key': 'dimensionKey'
    }

    def __init__(self, annotation_keys=None, dimension_key=None):  # noqa: E501
        """Dimension - a model defined in Swagger"""  # noqa: E501
        self._annotation_keys = None
        self._dimension_key = None
        self.discriminator = None
        if annotation_keys is not None:
            self.annotation_keys = annotation_keys
        if dimension_key is not None:
            self.dimension_key = dimension_key

    @property
    def annotation_keys(self):
        """Gets the annotation_keys of this Dimension.  # noqa: E501

        A list of annotations associated with the dimension of the report.  # noqa: E501

        :return: The annotation_keys of this Dimension.  # noqa: E501
        :rtype: list[str]
        """
        return self._annotation_keys

    @annotation_keys.setter
    def annotation_keys(self, annotation_keys):
        """Sets the annotation_keys of this Dimension.

        A list of annotations associated with the dimension of the report.  # noqa: E501

        :param annotation_keys: The annotation_keys of this Dimension.  # noqa: E501
        :type: list[str]
        """

        self._annotation_keys = annotation_keys

    @property
    def dimension_key(self):
        """Gets the dimension_key of this Dimension.  # noqa: E501

        The name of the dimension on which the report is based. A dimension is an attribute to which the report data applies.  # noqa: E501

        :return: The dimension_key of this Dimension.  # noqa: E501
        :rtype: str
        """
        return self._dimension_key

    @dimension_key.setter
    def dimension_key(self, dimension_key):
        """Sets the dimension_key of this Dimension.

        The name of the dimension on which the report is based. A dimension is an attribute to which the report data applies.  # noqa: E501

        :param dimension_key: The dimension_key of this Dimension.  # noqa: E501
        :type: str
        """

        self._dimension_key = dimension_key

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
        if issubclass(Dimension, dict):
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
        if not isinstance(other, Dimension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
