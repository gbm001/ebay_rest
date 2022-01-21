# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.16.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InventoryItemGroup(object):
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
        'aspects': 'str',
        'description': 'str',
        'image_urls': 'list[str]',
        'inventory_item_group_key': 'str',
        'subtitle': 'str',
        'title': 'str',
        'variant_sk_us': 'list[str]',
        'varies_by': 'VariesBy',
        'video_ids': 'list[str]'
    }

    attribute_map = {
        'aspects': 'aspects',
        'description': 'description',
        'image_urls': 'imageUrls',
        'inventory_item_group_key': 'inventoryItemGroupKey',
        'subtitle': 'subtitle',
        'title': 'title',
        'variant_sk_us': 'variantSKUs',
        'varies_by': 'variesBy',
        'video_ids': 'videoIds'
    }

    def __init__(self, aspects=None, description=None, image_urls=None, inventory_item_group_key=None, subtitle=None, title=None, variant_sk_us=None, varies_by=None, video_ids=None):  # noqa: E501
        """InventoryItemGroup - a model defined in Swagger"""  # noqa: E501
        self._aspects = None
        self._description = None
        self._image_urls = None
        self._inventory_item_group_key = None
        self._subtitle = None
        self._title = None
        self._variant_sk_us = None
        self._varies_by = None
        self._video_ids = None
        self.discriminator = None
        if aspects is not None:
            self.aspects = aspects
        if description is not None:
            self.description = description
        if image_urls is not None:
            self.image_urls = image_urls
        if inventory_item_group_key is not None:
            self.inventory_item_group_key = inventory_item_group_key
        if subtitle is not None:
            self.subtitle = subtitle
        if title is not None:
            self.title = title
        if variant_sk_us is not None:
            self.variant_sk_us = variant_sk_us
        if varies_by is not None:
            self.varies_by = varies_by
        if video_ids is not None:
            self.video_ids = video_ids

    @property
    def aspects(self):
        """Gets the aspects of this InventoryItemGroup.  # noqa: E501

        This is a collection of item specifics (aka product aspects) name-value pairs that are shared by all product variations within the inventory item group. Common aspects for the inventory item group are not immediately required upon creating an inventory item group, but these aspects will be required before the first offer of the group is published. Common aspects for a men's t-shirt might be pattern and sleeve length. Below is an example of the proper JSON syntax to use when manually inputting item specifics. Note that one item specific name, such as 'Features', can have more than one value. If an item specific name has more than one value, each value is delimited with a comma.<br/> <pre><code>\"aspects\": {<br/> \"pattern\": [\"solid\"],<br/> \"sleeves\": [\"short\"]<br/> }</code></pre>This container is always returned if one or more offers associated with the inventory item group have been published, and is only returned if set for an inventory item group if that group has yet to have any offers published.<br/>  # noqa: E501

        :return: The aspects of this InventoryItemGroup.  # noqa: E501
        :rtype: str
        """
        return self._aspects

    @aspects.setter
    def aspects(self, aspects):
        """Sets the aspects of this InventoryItemGroup.

        This is a collection of item specifics (aka product aspects) name-value pairs that are shared by all product variations within the inventory item group. Common aspects for the inventory item group are not immediately required upon creating an inventory item group, but these aspects will be required before the first offer of the group is published. Common aspects for a men's t-shirt might be pattern and sleeve length. Below is an example of the proper JSON syntax to use when manually inputting item specifics. Note that one item specific name, such as 'Features', can have more than one value. If an item specific name has more than one value, each value is delimited with a comma.<br/> <pre><code>\"aspects\": {<br/> \"pattern\": [\"solid\"],<br/> \"sleeves\": [\"short\"]<br/> }</code></pre>This container is always returned if one or more offers associated with the inventory item group have been published, and is only returned if set for an inventory item group if that group has yet to have any offers published.<br/>  # noqa: E501

        :param aspects: The aspects of this InventoryItemGroup.  # noqa: E501
        :type: str
        """

        self._aspects = aspects

    @property
    def description(self):
        """Gets the description of this InventoryItemGroup.  # noqa: E501

        The description of the inventory item group. This description should fully describe the product and the variations of the product that are available in the inventory item group, since this description will ultimately become the listing description once the first offer of the group is published. This field is not initially required when first creating an inventory item group, but will be required before the first offer of the group is published. <br><br><span class=\"tablenote\"> <strong>Note:</strong> Since this description will ultimately  become the listing description in a multiple-variation listing, the seller should omit the <strong>listingDescription</strong> field when creating the offers for each variation. If they include the <strong>listingDescription</strong> field for the individual offer(s) in an item group, the text in that field for a published offer will overwrite the text provided in this <strong>description</strong> field for the inventory item group.</span><br/><br/>HTML tags and markup can be used in this field, but each character counts toward the max length limit.<br/><br/><span class=\"tablenote\"> <strong>Note:</strong> To ensure that their short listing description is optimized when viewed on mobile devices, sellers should strongly consider using eBay's <a href=\"https://pages.ebay.com/sell/itemdescription/customizeyoursummary.html\" target=\"_blank\">View Item description summary feature</a> when listing their items. Keep in mind that the 'short' listing description is what prospective buyers first see when they view the listing on a mobile device. The 'full' listing description is also available to mobile users when they click on the short listing description, but the full description is not automatically optimized for viewing in mobile devices, and many users won't even drill down to the full description.<br><br> Using HTML div and span tag attributes, this feature allows sellers to customize and fully control the short listing description that is displayed to prospective buyers when viewing the listing on a mobile device. The short listing description on mobile devices is limited to 800 characters, and whenever the full listing description (provided in this field, in UI, or seller tool) exceeds this limit, eBay uses a special algorithm to derive the best possible short listing description within the 800-character limit. However, due to some short listing description content being removed, it is definitely not ideal for the seller, and could lead to a bad buyer experience and possibly to a Significantly not as described (SNAD) case, since the buyer may not get complete details on the item when viewing the short listing description. See the eBay help page for more details on using the HTML div and span tags.</span><br/><br/>This field is always returned if one or more offers associated with the inventory item group have been published, and is only returned if set for an inventory item group if that group has yet to have any offers published.<br/><br/><strong>Max Length</strong>: 500000 (which includes HTML markup/tags)<br>  # noqa: E501

        :return: The description of this InventoryItemGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InventoryItemGroup.

        The description of the inventory item group. This description should fully describe the product and the variations of the product that are available in the inventory item group, since this description will ultimately become the listing description once the first offer of the group is published. This field is not initially required when first creating an inventory item group, but will be required before the first offer of the group is published. <br><br><span class=\"tablenote\"> <strong>Note:</strong> Since this description will ultimately  become the listing description in a multiple-variation listing, the seller should omit the <strong>listingDescription</strong> field when creating the offers for each variation. If they include the <strong>listingDescription</strong> field for the individual offer(s) in an item group, the text in that field for a published offer will overwrite the text provided in this <strong>description</strong> field for the inventory item group.</span><br/><br/>HTML tags and markup can be used in this field, but each character counts toward the max length limit.<br/><br/><span class=\"tablenote\"> <strong>Note:</strong> To ensure that their short listing description is optimized when viewed on mobile devices, sellers should strongly consider using eBay's <a href=\"https://pages.ebay.com/sell/itemdescription/customizeyoursummary.html\" target=\"_blank\">View Item description summary feature</a> when listing their items. Keep in mind that the 'short' listing description is what prospective buyers first see when they view the listing on a mobile device. The 'full' listing description is also available to mobile users when they click on the short listing description, but the full description is not automatically optimized for viewing in mobile devices, and many users won't even drill down to the full description.<br><br> Using HTML div and span tag attributes, this feature allows sellers to customize and fully control the short listing description that is displayed to prospective buyers when viewing the listing on a mobile device. The short listing description on mobile devices is limited to 800 characters, and whenever the full listing description (provided in this field, in UI, or seller tool) exceeds this limit, eBay uses a special algorithm to derive the best possible short listing description within the 800-character limit. However, due to some short listing description content being removed, it is definitely not ideal for the seller, and could lead to a bad buyer experience and possibly to a Significantly not as described (SNAD) case, since the buyer may not get complete details on the item when viewing the short listing description. See the eBay help page for more details on using the HTML div and span tags.</span><br/><br/>This field is always returned if one or more offers associated with the inventory item group have been published, and is only returned if set for an inventory item group if that group has yet to have any offers published.<br/><br/><strong>Max Length</strong>: 500000 (which includes HTML markup/tags)<br>  # noqa: E501

        :param description: The description of this InventoryItemGroup.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def image_urls(self):
        """Gets the image_urls of this InventoryItemGroup.  # noqa: E501

        An array of one or more links to images for the inventory item group. URLs must use the \"HTTPS\" protocol. Images can be self-hosted by the seller, or sellers can use the <a href=\"https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/UploadSiteHostedPictures.html\" target=\"_blank\">UploadSiteHostedPictures</a> call of the Trading API to upload images to an eBay Picture Server. If successful, the response of the <a href=\"https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/UploadSiteHostedPictures.html\" target=\"_blank\">UploadSiteHostedPictures</a> call will contain a full URL to the image on an eBay Picture Server. This is the URL that will be passed in through the <strong>imageUrls</strong> array. <br/><br/> Before any offer can be published, at least one image must exist for the offer. Links to images can either be passed in through this <strong>imageUrls</strong> container, or they can be passed in through the <strong>product.imageUrls</strong> container when creating each inventory item in the group. If the <strong>variesBy.aspectsImageVariesBy</strong> field is used to specify the main product aspect where the variations vary, the links to the images must be passed in through this <strong>imageUrls</strong> container, and there should be a picture for each variation. So, if the <strong>variesBy.aspectsImageVariesBy</strong> field is set to <code>Color</code>, a link should be included to an image demonstrating each available color in the group.<br><br> Most eBay sites support up to 12 pictures free of charge, and eBay Motors listings can have up to 24 pictures.<br/><br/> This container will always be returned for an inventory item group that has at least one published offer since a published offer will always have at least one picture, but this container will only be returned if defined for inventory item groups that have yet to have any published offers.  # noqa: E501

        :return: The image_urls of this InventoryItemGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._image_urls

    @image_urls.setter
    def image_urls(self, image_urls):
        """Sets the image_urls of this InventoryItemGroup.

        An array of one or more links to images for the inventory item group. URLs must use the \"HTTPS\" protocol. Images can be self-hosted by the seller, or sellers can use the <a href=\"https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/UploadSiteHostedPictures.html\" target=\"_blank\">UploadSiteHostedPictures</a> call of the Trading API to upload images to an eBay Picture Server. If successful, the response of the <a href=\"https://developer.ebay.com/Devzone/XML/docs/Reference/eBay/UploadSiteHostedPictures.html\" target=\"_blank\">UploadSiteHostedPictures</a> call will contain a full URL to the image on an eBay Picture Server. This is the URL that will be passed in through the <strong>imageUrls</strong> array. <br/><br/> Before any offer can be published, at least one image must exist for the offer. Links to images can either be passed in through this <strong>imageUrls</strong> container, or they can be passed in through the <strong>product.imageUrls</strong> container when creating each inventory item in the group. If the <strong>variesBy.aspectsImageVariesBy</strong> field is used to specify the main product aspect where the variations vary, the links to the images must be passed in through this <strong>imageUrls</strong> container, and there should be a picture for each variation. So, if the <strong>variesBy.aspectsImageVariesBy</strong> field is set to <code>Color</code>, a link should be included to an image demonstrating each available color in the group.<br><br> Most eBay sites support up to 12 pictures free of charge, and eBay Motors listings can have up to 24 pictures.<br/><br/> This container will always be returned for an inventory item group that has at least one published offer since a published offer will always have at least one picture, but this container will only be returned if defined for inventory item groups that have yet to have any published offers.  # noqa: E501

        :param image_urls: The image_urls of this InventoryItemGroup.  # noqa: E501
        :type: list[str]
        """

        self._image_urls = image_urls

    @property
    def inventory_item_group_key(self):
        """Gets the inventory_item_group_key of this InventoryItemGroup.  # noqa: E501

        This is the unique identifier of the inventory item group. This identifier is created by the seller when an inventory item group is created. This field is only applicable to the <strong>getInventoryItemGroup</strong> call and not to the <strong>createOrReplaceInventoryItemGroup</strong> call. In the <strong>createOrReplaceInventoryItemGroup</strong> call, the <strong>inventoryItemGroupKey</strong> value is passed into the end of the call URI instead.   # noqa: E501

        :return: The inventory_item_group_key of this InventoryItemGroup.  # noqa: E501
        :rtype: str
        """
        return self._inventory_item_group_key

    @inventory_item_group_key.setter
    def inventory_item_group_key(self, inventory_item_group_key):
        """Sets the inventory_item_group_key of this InventoryItemGroup.

        This is the unique identifier of the inventory item group. This identifier is created by the seller when an inventory item group is created. This field is only applicable to the <strong>getInventoryItemGroup</strong> call and not to the <strong>createOrReplaceInventoryItemGroup</strong> call. In the <strong>createOrReplaceInventoryItemGroup</strong> call, the <strong>inventoryItemGroupKey</strong> value is passed into the end of the call URI instead.   # noqa: E501

        :param inventory_item_group_key: The inventory_item_group_key of this InventoryItemGroup.  # noqa: E501
        :type: str
        """

        self._inventory_item_group_key = inventory_item_group_key

    @property
    def subtitle(self):
        """Gets the subtitle of this InventoryItemGroup.  # noqa: E501

        A subtitle is an optional listing feature that allows the seller to provide more information about the product, possibly including keywords that may assist with search results. An additional listing fee will be charged to the seller if a subtitle is used. For more information on using listing subtitles on the US site, see the <a href=\"https://pages.ebay.com/help/sell/itemsubtitle.html\" target=\"_blank\">Adding a subtitle to your listings</a> help page. <br><br><span class=\"tablenote\"> <strong>Note:</strong> Since this subtitle will ultimately  become the subtitle in a multiple-variation listing, the seller should not include the <strong>subtitle</strong> field when creating the inventory items that are members of the group. If they do include the <strong>subtitle</strong> field in an inventory item record, the text in that field will overwrite the text provided in this <strong>subtitle</strong> field for each inventory item in the group that is published.</span><br/><br/>This field will only be returned if set for an inventory item.<br/><br/><strong>Max Length</strong>: 55<br/>  # noqa: E501

        :return: The subtitle of this InventoryItemGroup.  # noqa: E501
        :rtype: str
        """
        return self._subtitle

    @subtitle.setter
    def subtitle(self, subtitle):
        """Sets the subtitle of this InventoryItemGroup.

        A subtitle is an optional listing feature that allows the seller to provide more information about the product, possibly including keywords that may assist with search results. An additional listing fee will be charged to the seller if a subtitle is used. For more information on using listing subtitles on the US site, see the <a href=\"https://pages.ebay.com/help/sell/itemsubtitle.html\" target=\"_blank\">Adding a subtitle to your listings</a> help page. <br><br><span class=\"tablenote\"> <strong>Note:</strong> Since this subtitle will ultimately  become the subtitle in a multiple-variation listing, the seller should not include the <strong>subtitle</strong> field when creating the inventory items that are members of the group. If they do include the <strong>subtitle</strong> field in an inventory item record, the text in that field will overwrite the text provided in this <strong>subtitle</strong> field for each inventory item in the group that is published.</span><br/><br/>This field will only be returned if set for an inventory item.<br/><br/><strong>Max Length</strong>: 55<br/>  # noqa: E501

        :param subtitle: The subtitle of this InventoryItemGroup.  # noqa: E501
        :type: str
        """

        self._subtitle = subtitle

    @property
    def title(self):
        """Gets the title of this InventoryItemGroup.  # noqa: E501

        The title of the inventory item group. This title will ultimately become the listing title once the first offer of the group is published. This field is not initially required when first creating an inventory item group, but will be required before the first offer of the group is published.<br><br><span class=\"tablenote\"> <strong>Note:</strong> Since this title will ultimately  become the listing title in a multiple-variation listing, the seller should omit the <strong>title</strong> field when creating the inventory items that are members of the group. If they do include the <strong>title</strong> field in an inventory item record, the text in that field will overwrite the text provided in this <strong>title</strong> field for each inventory item in the group that is published.</span><br/><br/> This field is always returned if one or more offers associated with the inventory item group have been published, and is only returned if set for an inventory item group if that group has yet to have any offers published.<br/><br/><strong>Max Length</strong>: 80 <br/>  # noqa: E501

        :return: The title of this InventoryItemGroup.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this InventoryItemGroup.

        The title of the inventory item group. This title will ultimately become the listing title once the first offer of the group is published. This field is not initially required when first creating an inventory item group, but will be required before the first offer of the group is published.<br><br><span class=\"tablenote\"> <strong>Note:</strong> Since this title will ultimately  become the listing title in a multiple-variation listing, the seller should omit the <strong>title</strong> field when creating the inventory items that are members of the group. If they do include the <strong>title</strong> field in an inventory item record, the text in that field will overwrite the text provided in this <strong>title</strong> field for each inventory item in the group that is published.</span><br/><br/> This field is always returned if one or more offers associated with the inventory item group have been published, and is only returned if set for an inventory item group if that group has yet to have any offers published.<br/><br/><strong>Max Length</strong>: 80 <br/>  # noqa: E501

        :param title: The title of this InventoryItemGroup.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def variant_sk_us(self):
        """Gets the variant_sk_us of this InventoryItemGroup.  # noqa: E501

        This required container is used to assign individual inventory items to the inventory item group. Multiple SKU values are passed in to this container. If updating an existing inventory item group, the seller should make sure that all member SKU values are passed in, as long as the seller wants that SKU to remain in the group.<br><br> It is also possible to add or remove SKUs with a <strong>createOrReplaceInventoryItemGroup</strong> call. If the seller wants to remove a SKU from the group, that seller will just omit that SKU value from this container to remove that inventory item/SKU from the inventory item group and any published, multiple-variation listing. However, a variation cannot be removed from the group if that variation has one or more sales for that listing. A workaround for this is to set that variation's quantity to <code>0</code> and it will be 'grayed out' in the View Item page.<br><br>This container is always returned.  # noqa: E501

        :return: The variant_sk_us of this InventoryItemGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._variant_sk_us

    @variant_sk_us.setter
    def variant_sk_us(self, variant_sk_us):
        """Sets the variant_sk_us of this InventoryItemGroup.

        This required container is used to assign individual inventory items to the inventory item group. Multiple SKU values are passed in to this container. If updating an existing inventory item group, the seller should make sure that all member SKU values are passed in, as long as the seller wants that SKU to remain in the group.<br><br> It is also possible to add or remove SKUs with a <strong>createOrReplaceInventoryItemGroup</strong> call. If the seller wants to remove a SKU from the group, that seller will just omit that SKU value from this container to remove that inventory item/SKU from the inventory item group and any published, multiple-variation listing. However, a variation cannot be removed from the group if that variation has one or more sales for that listing. A workaround for this is to set that variation's quantity to <code>0</code> and it will be 'grayed out' in the View Item page.<br><br>This container is always returned.  # noqa: E501

        :param variant_sk_us: The variant_sk_us of this InventoryItemGroup.  # noqa: E501
        :type: list[str]
        """

        self._variant_sk_us = variant_sk_us

    @property
    def varies_by(self):
        """Gets the varies_by of this InventoryItemGroup.  # noqa: E501


        :return: The varies_by of this InventoryItemGroup.  # noqa: E501
        :rtype: VariesBy
        """
        return self._varies_by

    @varies_by.setter
    def varies_by(self, varies_by):
        """Sets the varies_by of this InventoryItemGroup.


        :param varies_by: The varies_by of this InventoryItemGroup.  # noqa: E501
        :type: VariesBy
        """

        self._varies_by = varies_by

    @property
    def video_ids(self):
        """Gets the video_ids of this InventoryItemGroup.  # noqa: E501

        An array of one or more VideoId values for the inventory item group. A VideoId is a unique identifier that is automatically created by eBay when a seller successfully uploads a video to eBay using the  <a href=\"https://developer.ebay.com/api-docs/commerce/media/resources/video/methods/uploadVideo\" target=\"_blank\">uploadVideo</a> method of the <a href=\"https://developer.ebay.com/api-docs/commerce/media/overview.html\" target=\"_blank\">Media API</a>. <br /><br />For information on supported marketplaces and platforms, as well as other requirements and limitations of video support, please refer to <a href=\"https://developer.ebay.com/api-docs/sell/static/inventory/managing-video-media.html\" target=\"_blank\">Managing videos</a>.  # noqa: E501

        :return: The video_ids of this InventoryItemGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._video_ids

    @video_ids.setter
    def video_ids(self, video_ids):
        """Sets the video_ids of this InventoryItemGroup.

        An array of one or more VideoId values for the inventory item group. A VideoId is a unique identifier that is automatically created by eBay when a seller successfully uploads a video to eBay using the  <a href=\"https://developer.ebay.com/api-docs/commerce/media/resources/video/methods/uploadVideo\" target=\"_blank\">uploadVideo</a> method of the <a href=\"https://developer.ebay.com/api-docs/commerce/media/overview.html\" target=\"_blank\">Media API</a>. <br /><br />For information on supported marketplaces and platforms, as well as other requirements and limitations of video support, please refer to <a href=\"https://developer.ebay.com/api-docs/sell/static/inventory/managing-video-media.html\" target=\"_blank\">Managing videos</a>.  # noqa: E501

        :param video_ids: The video_ids of this InventoryItemGroup.  # noqa: E501
        :type: list[str]
        """

        self._video_ids = video_ids

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
        if issubclass(InventoryItemGroup, dict):
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
        if not isinstance(other, InventoryItemGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
