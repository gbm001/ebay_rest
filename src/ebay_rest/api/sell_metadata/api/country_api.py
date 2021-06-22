# coding: utf-8

"""
    Metadata API

    The Metadata API has operations that retrieve configuration details pertaining to the different eBay marketplaces. In addition to marketplace information, the API also has operations that get information that helps sellers list items on eBay.  # noqa: E501

    OpenAPI spec version: v1.4.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ...sell_metadata.api_client import ApiClient


class CountryApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_sales_tax_jurisdictions(self, country_code, **kwargs):  # noqa: E501
        """get_sales_tax_jurisdictions  # noqa: E501

        This method retrieves all the sales tax jurisdictions for the country that you specify in the countryCode path parameter. Countries with valid sales tax jurisdictions are Canada and the US. The response from this call tells you the jurisdictions for which a seller can configure tax tables. Although setting up tax tables is optional, you can use the createOrReplaceSalesTax in the Account API call to configure the tax tables for the jurisdictions you sell to.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sales_tax_jurisdictions(country_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country_code: This path parameter specifies the two-letter ISO 3166 country code for the country whose jurisdictions you want to retrieve. eBay provides sales tax jurisdiction information for Canada and the United States.Valid values for this path parameter are CA and US. (required)
        :return: SalesTaxJurisdictions
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sales_tax_jurisdictions_with_http_info(country_code, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sales_tax_jurisdictions_with_http_info(country_code, **kwargs)  # noqa: E501
            return data

    def get_sales_tax_jurisdictions_with_http_info(self, country_code, **kwargs):  # noqa: E501
        """get_sales_tax_jurisdictions  # noqa: E501

        This method retrieves all the sales tax jurisdictions for the country that you specify in the countryCode path parameter. Countries with valid sales tax jurisdictions are Canada and the US. The response from this call tells you the jurisdictions for which a seller can configure tax tables. Although setting up tax tables is optional, you can use the createOrReplaceSalesTax in the Account API call to configure the tax tables for the jurisdictions you sell to.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sales_tax_jurisdictions_with_http_info(country_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country_code: This path parameter specifies the two-letter ISO 3166 country code for the country whose jurisdictions you want to retrieve. eBay provides sales tax jurisdiction information for Canada and the United States.Valid values for this path parameter are CA and US. (required)
        :return: SalesTaxJurisdictions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sales_tax_jurisdictions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'country_code' is set
        if ('country_code' not in params or
                params['country_code'] is None):
            raise ValueError("Missing the required parameter `country_code` when calling `get_sales_tax_jurisdictions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'country_code' in params:
            path_params['countryCode'] = params['country_code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/country/{countryCode}/sales_tax_jurisdiction', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SalesTaxJurisdictions',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
