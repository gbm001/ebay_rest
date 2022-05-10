# coding: utf-8

"""
    Browse API

    <p>The Browse API has the following resources:</p>   <ul> <li><b> item_summary: </b> Lets shoppers search for specific items by keyword, GTIN, category, charity, product, or item aspects and refine the results by using filters, such as aspects, compatibility, and fields values.</li>  <li><b> search_by_image: </b><a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />&nbsp;(Experimental)</a> Lets shoppers search for specific items by image. You can refine the results by using URI parameters and filters.</li>   <li><b> item: </b> <ul><li>Lets you retrieve the details of a specific item or all the items in an item group, which is an item with variations such as color and size and check if a product is compatible with the specified item, such as if a specific car is compatible with a specific part.</li> <li>Provides a bridge between the eBay legacy APIs, such as <b> Finding</b>, and the RESTful APIs, which use different formats for the item IDs.</li>  </ul> </li>  <li> <b> shopping_cart: </b> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />&nbsp;(Experimental)</a> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited \" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> Provides the ability for eBay members to see the contents of their eBay cart, and add, remove, and change the quantity of items in their eBay cart.&nbsp;&nbsp;<b> Note: </b> This resource is not available in the eBay API Explorer.</li></ul>       <p>The <b> item_summary</b>, <b> search_by_image</b>, and <b> item</b> resource calls require an <a href=\"/api-docs/static/oauth-client-credentials-grant.html\">Application access token</a>. The <b> shopping_cart</b> resource calls require a <a href=\"/api-docs/static/oauth-authorization-code-grant.html\">User access token</a>.</p>  # noqa: E501

    OpenAPI spec version: v1.16.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ShipToRegion(object):
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
        'region_id': 'str',
        'region_name': 'str',
        'region_type': 'str'
    }

    attribute_map = {
        'region_id': 'regionId',
        'region_name': 'regionName',
        'region_type': 'regionType'
    }

    def __init__(self, region_id=None, region_name=None, region_type=None):  # noqa: E501
        """ShipToRegion - a model defined in Swagger"""  # noqa: E501
        self._region_id = None
        self._region_name = None
        self._region_type = None
        self.discriminator = None
        if region_id is not None:
            self.region_id = region_id
        if region_name is not None:
            self.region_name = region_name
        if region_type is not None:
            self.region_type = region_type

    @property
    def region_id(self):
        """Gets the region_id of this ShipToRegion.  # noqa: E501

        The unique identifier of the shipping region. The value returned here is dependent on the corresponding <b>regionType</b> value. The <b>regionId</b> value for a region does not vary based on the eBay marketplace. However, the corresponding <b>regionName</b> value for a region is a localized, text-based description of the shipping region. <br><br> If the <b>regionType</b> value is <code>WORLDWIDE</code>, the <b>regionId</b> value will also be <code>WORLDWIDE</code>.<br><br> If the <b>regionType</b> value is <code>WORLD_REGION</code>, the <b>regionId</b> value will be one of the following: <code>AFRICA</code>, <code>AMERICAS</code>, <code>ASIA</code>, <code>AUSTRALIA</code>, <code>CENTRAL_AMERICA_AND_CARIBBEAN</code>, <code>EUROPE</code>, <code>EUROPEAN_UNION</code>, <code>GREATER_CHINA</code>, <code>MIDDLE_EAST</code>, <code>NORTH_AMERICA</code>, <code>OCEANIA</code>, <code>SOUTH_AMERICA</code>, <code>SOUTHEAST_ASIA</code> or <code>CHANNEL_ISLANDS</code>.<br><br>If the <b>regionType</b> value is <code>COUNTRY</code>, the <b>regionId</b> value will be the two-letter code for the country, as defined in the <a href=\"https://www.iso.org/iso-3166-country-codes.html \" target=\"_blank\">ISO 3166</a> standard.<br><br>If the <b>regionType</b> value is <code>STATE_OR_PROVINCE</code>, the <b>regionId</b> value will either be the two-letter code for US states and DC (as defined on this <a href=\"https://www.ssa.gov/international/coc-docs/states.html \" target=\"_blank\">Social Security Administration</a> page), or the two-letter code for Canadian provinces (as defined by this <a href=\"https://www.canadapost.ca/tools/pg/manual/PGaddress-e.asp?ecid=murl10006450#1442131 \" target=\"_blank\">Canada Post</a> page).<br><br>If the <b>regionType</b> value is <code>COUNTRY_REGION</code>, the <b>regionId</b> value may be one of following: <code>_AH</code> (if a seller is not willing to ship to Alaska/Hawaii), <code>_PR</code> (if the seller is not willing to ship to US Protectorates), <code>_AP</code> (if seller is not willing to ship to a US Army or Fleet Post Office), and <code>PO_BOX</code> (if the seller is not willing to ship to a Post Office Box).  # noqa: E501

        :return: The region_id of this ShipToRegion.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ShipToRegion.

        The unique identifier of the shipping region. The value returned here is dependent on the corresponding <b>regionType</b> value. The <b>regionId</b> value for a region does not vary based on the eBay marketplace. However, the corresponding <b>regionName</b> value for a region is a localized, text-based description of the shipping region. <br><br> If the <b>regionType</b> value is <code>WORLDWIDE</code>, the <b>regionId</b> value will also be <code>WORLDWIDE</code>.<br><br> If the <b>regionType</b> value is <code>WORLD_REGION</code>, the <b>regionId</b> value will be one of the following: <code>AFRICA</code>, <code>AMERICAS</code>, <code>ASIA</code>, <code>AUSTRALIA</code>, <code>CENTRAL_AMERICA_AND_CARIBBEAN</code>, <code>EUROPE</code>, <code>EUROPEAN_UNION</code>, <code>GREATER_CHINA</code>, <code>MIDDLE_EAST</code>, <code>NORTH_AMERICA</code>, <code>OCEANIA</code>, <code>SOUTH_AMERICA</code>, <code>SOUTHEAST_ASIA</code> or <code>CHANNEL_ISLANDS</code>.<br><br>If the <b>regionType</b> value is <code>COUNTRY</code>, the <b>regionId</b> value will be the two-letter code for the country, as defined in the <a href=\"https://www.iso.org/iso-3166-country-codes.html \" target=\"_blank\">ISO 3166</a> standard.<br><br>If the <b>regionType</b> value is <code>STATE_OR_PROVINCE</code>, the <b>regionId</b> value will either be the two-letter code for US states and DC (as defined on this <a href=\"https://www.ssa.gov/international/coc-docs/states.html \" target=\"_blank\">Social Security Administration</a> page), or the two-letter code for Canadian provinces (as defined by this <a href=\"https://www.canadapost.ca/tools/pg/manual/PGaddress-e.asp?ecid=murl10006450#1442131 \" target=\"_blank\">Canada Post</a> page).<br><br>If the <b>regionType</b> value is <code>COUNTRY_REGION</code>, the <b>regionId</b> value may be one of following: <code>_AH</code> (if a seller is not willing to ship to Alaska/Hawaii), <code>_PR</code> (if the seller is not willing to ship to US Protectorates), <code>_AP</code> (if seller is not willing to ship to a US Army or Fleet Post Office), and <code>PO_BOX</code> (if the seller is not willing to ship to a Post Office Box).  # noqa: E501

        :param region_id: The region_id of this ShipToRegion.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

    @property
    def region_name(self):
        """Gets the region_name of this ShipToRegion.  # noqa: E501

        A localized text string that indicates the name of the shipping region. The value returned here is dependent on the corresponding <b>regionType</b> value. <br><br> If the <b>regionType</b> value is <code>WORLDWIDE</code>, the <b>regionName</b> value will show <code>Worldwide</code>.<br><br> If the <b>regionType</b> value is <code>WORLD_REGION</code>, the <b>regionName</b> value will be a localized text string for one of the following large geographical regions: Africa, Americas, Asia, Australia, Central America and Caribbean, Europe, European Union, Greater China, Middle East, North America, Oceania, South America, Southeast Asia, or Channel Islands.<br><br>If the <b>regionType</b> value is <code>COUNTRY</code>, the <b>regionName</b> value will be a localized text string for any country in the world.<br><br>If the <b>regionType</b> value is <code>STATE_OR_PROVINCE</code>, the <b>regionName</b> value will be a localized text string for any US state or Canadian province. <br><br>If the <b>regionType</b> value is <code>COUNTRY_REGION</code>, the <b>regionName</b> value may be a localized version of one of the following: Alaska/Hawaii, US Protectorates, APO/FPO (Army or Fleet Post Office), or PO BOX.  # noqa: E501

        :return: The region_name of this ShipToRegion.  # noqa: E501
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this ShipToRegion.

        A localized text string that indicates the name of the shipping region. The value returned here is dependent on the corresponding <b>regionType</b> value. <br><br> If the <b>regionType</b> value is <code>WORLDWIDE</code>, the <b>regionName</b> value will show <code>Worldwide</code>.<br><br> If the <b>regionType</b> value is <code>WORLD_REGION</code>, the <b>regionName</b> value will be a localized text string for one of the following large geographical regions: Africa, Americas, Asia, Australia, Central America and Caribbean, Europe, European Union, Greater China, Middle East, North America, Oceania, South America, Southeast Asia, or Channel Islands.<br><br>If the <b>regionType</b> value is <code>COUNTRY</code>, the <b>regionName</b> value will be a localized text string for any country in the world.<br><br>If the <b>regionType</b> value is <code>STATE_OR_PROVINCE</code>, the <b>regionName</b> value will be a localized text string for any US state or Canadian province. <br><br>If the <b>regionType</b> value is <code>COUNTRY_REGION</code>, the <b>regionName</b> value may be a localized version of one of the following: Alaska/Hawaii, US Protectorates, APO/FPO (Army or Fleet Post Office), or PO BOX.  # noqa: E501

        :param region_name: The region_name of this ShipToRegion.  # noqa: E501
        :type: str
        """

        self._region_name = region_name

    @property
    def region_type(self):
        """Gets the region_type of this ShipToRegion.  # noqa: E501

        An enumeration value that indicates the level or type of shipping region. <br><br><b> Valid Values: </b> <ul><li><b> COUNTRY_REGION </b> - Indicates the region is a domestic region or special location within a country.</li><li><b> STATE_OR_PROVINCE </b> - Indicates the region is a state or province within a country, such as California or New York in the US, or Ontario or Alberta in Canada.</li><li><b> COUNTRY </b> - Indicates the region is a single country.</li><li><b> WORLD_REGION </b> - Indicates the region is a world region, such as Africa, the Middle East, or Southeast Asia.</li><li><b> WORLDWIDE </b> - Indicates the region is the entire world. This value is only applicable for included shiping regions, and not excluded shipping regions.</li></ul> For more detail on the actual <b>regionName</b>/<b>regionId</b> values that will be returned based on the <b>regionType</b> value, see the <a href=\"/api-docs/buy/browse/resources/item/methods/getItem#response.shipToLocations.regionExcluded.regionId\">regionId</a> and/or <a href=\"/api-docs/buy/browse/resources/item/methods/getItem#response.shipToLocations.regionExcluded.regionName\">regionName</a> field descriptions.<br><br> Code so that your app gracefully handles any future changes to this list. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/ba:RegionTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The region_type of this ShipToRegion.  # noqa: E501
        :rtype: str
        """
        return self._region_type

    @region_type.setter
    def region_type(self, region_type):
        """Sets the region_type of this ShipToRegion.

        An enumeration value that indicates the level or type of shipping region. <br><br><b> Valid Values: </b> <ul><li><b> COUNTRY_REGION </b> - Indicates the region is a domestic region or special location within a country.</li><li><b> STATE_OR_PROVINCE </b> - Indicates the region is a state or province within a country, such as California or New York in the US, or Ontario or Alberta in Canada.</li><li><b> COUNTRY </b> - Indicates the region is a single country.</li><li><b> WORLD_REGION </b> - Indicates the region is a world region, such as Africa, the Middle East, or Southeast Asia.</li><li><b> WORLDWIDE </b> - Indicates the region is the entire world. This value is only applicable for included shiping regions, and not excluded shipping regions.</li></ul> For more detail on the actual <b>regionName</b>/<b>regionId</b> values that will be returned based on the <b>regionType</b> value, see the <a href=\"/api-docs/buy/browse/resources/item/methods/getItem#response.shipToLocations.regionExcluded.regionId\">regionId</a> and/or <a href=\"/api-docs/buy/browse/resources/item/methods/getItem#response.shipToLocations.regionExcluded.regionName\">regionName</a> field descriptions.<br><br> Code so that your app gracefully handles any future changes to this list. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/ba:RegionTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param region_type: The region_type of this ShipToRegion.  # noqa: E501
        :type: str
        """

        self._region_type = region_type

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
        if issubclass(ShipToRegion, dict):
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
        if not isinstance(other, ShipToRegion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
