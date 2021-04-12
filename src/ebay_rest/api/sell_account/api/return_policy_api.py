# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (the Fulfillment Policy, Payment Policy, and Return Policy), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br><br>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.6.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from sell_account.api_client import ApiClient


class ReturnPolicyApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_return_policy(self, body, **kwargs):  # noqa: E501
        """create_return_policy  # noqa: E501

        This method creates a new return policy where the policy encapsulates seller's terms for returning items. Use the Metadata API method getReturnPolicies to determine which categories require you to supply a return policy for the marketplace(s) into which you list. Each policy targets a marketplaceId and categoryTypes.name combination and you can create multiple policies for each combination. A successful request returns the URI to the new policy in the Location response header and the ID for the new policy is returned in the response payload. Tip: For details on creating and using the business policies supported by the Account API, see eBay business policies. Marketplaces and locales Policy instructions can be localized by providing a locale in the Accept-Language HTTP request header. For example, the following setting displays field values from the request body in German: Accept-Language: de-DE. Target the specific locale of a marketplace that supports multiple locales using the Content-Language request header. For example, target the French locale of the Canadian marketplace by specifying the fr-CA locale for Content-Language. Likewise, target the Dutch locale of the Belgium marketplace by setting Content-Language: nl-BE. Tip: For details on headers, see HTTP request headers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_return_policy(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ReturnPolicyRequest body: Return policy request (required)
        :return: SetReturnPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_return_policy_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_return_policy_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_return_policy_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_return_policy  # noqa: E501

        This method creates a new return policy where the policy encapsulates seller's terms for returning items. Use the Metadata API method getReturnPolicies to determine which categories require you to supply a return policy for the marketplace(s) into which you list. Each policy targets a marketplaceId and categoryTypes.name combination and you can create multiple policies for each combination. A successful request returns the URI to the new policy in the Location response header and the ID for the new policy is returned in the response payload. Tip: For details on creating and using the business policies supported by the Account API, see eBay business policies. Marketplaces and locales Policy instructions can be localized by providing a locale in the Accept-Language HTTP request header. For example, the following setting displays field values from the request body in German: Accept-Language: de-DE. Target the specific locale of a marketplace that supports multiple locales using the Content-Language request header. For example, target the French locale of the Canadian marketplace by specifying the fr-CA locale for Content-Language. Likewise, target the Dutch locale of the Belgium marketplace by setting Content-Language: nl-BE. Tip: For details on headers, see HTTP request headers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_return_policy_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ReturnPolicyRequest body: Return policy request (required)
        :return: SetReturnPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_return_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_return_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/return_policy', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SetReturnPolicyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_return_policy(self, return_policy_id, **kwargs):  # noqa: E501
        """delete_return_policy  # noqa: E501

        This method deletes a return policy. Supply the ID of the policy you want to delete in the returnPolicyId path parameter. Note that you cannot delete the default return policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_return_policy(return_policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str return_policy_id: This path parameter specifies the ID of the return policy you want to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_return_policy_with_http_info(return_policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_return_policy_with_http_info(return_policy_id, **kwargs)  # noqa: E501
            return data

    def delete_return_policy_with_http_info(self, return_policy_id, **kwargs):  # noqa: E501
        """delete_return_policy  # noqa: E501

        This method deletes a return policy. Supply the ID of the policy you want to delete in the returnPolicyId path parameter. Note that you cannot delete the default return policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_return_policy_with_http_info(return_policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str return_policy_id: This path parameter specifies the ID of the return policy you want to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['return_policy_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_return_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'return_policy_id' is set
        if ('return_policy_id' not in params or
                params['return_policy_id'] is None):
            raise ValueError("Missing the required parameter `return_policy_id` when calling `delete_return_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'return_policy_id' in params:
            path_params['return_policy_id'] = params['return_policy_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/return_policy/{return_policy_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_return_policies(self, marketplace_id, **kwargs):  # noqa: E501
        """get_return_policies  # noqa: E501

        This method retrieves all the return policies configured for the marketplace you specify using the marketplace_id query parameter. Marketplaces and locales Get the correct policies for a marketplace that supports multiple locales using the Content-Language request header. For example, get the policies for the French locale of the Canadian marketplace by specifying fr-CA for the Content-Language header. Likewise, target the Dutch locale of the Belgium marketplace by setting Content-Language: nl-BE. For details on header values, see HTTP request headers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_return_policies(marketplace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str marketplace_id: This query parameter specifies the ID of the eBay marketplace of the policy you want to retrieve. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum (required)
        :return: ReturnPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_return_policies_with_http_info(marketplace_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_return_policies_with_http_info(marketplace_id, **kwargs)  # noqa: E501
            return data

    def get_return_policies_with_http_info(self, marketplace_id, **kwargs):  # noqa: E501
        """get_return_policies  # noqa: E501

        This method retrieves all the return policies configured for the marketplace you specify using the marketplace_id query parameter. Marketplaces and locales Get the correct policies for a marketplace that supports multiple locales using the Content-Language request header. For example, get the policies for the French locale of the Canadian marketplace by specifying fr-CA for the Content-Language header. Likewise, target the Dutch locale of the Belgium marketplace by setting Content-Language: nl-BE. For details on header values, see HTTP request headers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_return_policies_with_http_info(marketplace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str marketplace_id: This query parameter specifies the ID of the eBay marketplace of the policy you want to retrieve. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum (required)
        :return: ReturnPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['marketplace_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_return_policies" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'marketplace_id' is set
        if ('marketplace_id' not in params or
                params['marketplace_id'] is None):
            raise ValueError("Missing the required parameter `marketplace_id` when calling `get_return_policies`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marketplace_id' in params:
            query_params.append(('marketplace_id', params['marketplace_id']))  # noqa: E501

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
            '/return_policy', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReturnPolicyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_return_policy(self, return_policy_id, **kwargs):  # noqa: E501
        """get_return_policy  # noqa: E501

        This method retrieves the complete details of the return policy specified by the returnPolicyId path parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_return_policy(return_policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str return_policy_id: This path parameter specifies the of the return policy you want to retrieve. (required)
        :return: ReturnPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_return_policy_with_http_info(return_policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_return_policy_with_http_info(return_policy_id, **kwargs)  # noqa: E501
            return data

    def get_return_policy_with_http_info(self, return_policy_id, **kwargs):  # noqa: E501
        """get_return_policy  # noqa: E501

        This method retrieves the complete details of the return policy specified by the returnPolicyId path parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_return_policy_with_http_info(return_policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str return_policy_id: This path parameter specifies the of the return policy you want to retrieve. (required)
        :return: ReturnPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['return_policy_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_return_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'return_policy_id' is set
        if ('return_policy_id' not in params or
                params['return_policy_id'] is None):
            raise ValueError("Missing the required parameter `return_policy_id` when calling `get_return_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'return_policy_id' in params:
            path_params['return_policy_id'] = params['return_policy_id']  # noqa: E501

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
            '/return_policy/{return_policy_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReturnPolicy',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_return_policy_by_name(self, marketplace_id, name, **kwargs):  # noqa: E501
        """get_return_policy_by_name  # noqa: E501

        This method retrieves the complete details of a single return policy. Supply both the policy name and its associated marketplace_id in the request query parameters. Marketplaces and locales Get the correct policy for a marketplace that supports multiple locales using the Content-Language request header. For example, get a policy for the French locale of the Canadian marketplace by specifying fr-CA for the Content-Language header. Likewise, target the Dutch locale of the Belgium marketplace by setting Content-Language: nl-BE. For details on header values, see HTTP request headers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_return_policy_by_name(marketplace_id, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str marketplace_id: This query parameter specifies the ID of the eBay marketplace of the policy you want to retrieve. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum (required)
        :param str name: This query parameter specifies the user-defined name of the return policy you want to retrieve. (required)
        :return: ReturnPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_return_policy_by_name_with_http_info(marketplace_id, name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_return_policy_by_name_with_http_info(marketplace_id, name, **kwargs)  # noqa: E501
            return data

    def get_return_policy_by_name_with_http_info(self, marketplace_id, name, **kwargs):  # noqa: E501
        """get_return_policy_by_name  # noqa: E501

        This method retrieves the complete details of a single return policy. Supply both the policy name and its associated marketplace_id in the request query parameters. Marketplaces and locales Get the correct policy for a marketplace that supports multiple locales using the Content-Language request header. For example, get a policy for the French locale of the Canadian marketplace by specifying fr-CA for the Content-Language header. Likewise, target the Dutch locale of the Belgium marketplace by setting Content-Language: nl-BE. For details on header values, see HTTP request headers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_return_policy_by_name_with_http_info(marketplace_id, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str marketplace_id: This query parameter specifies the ID of the eBay marketplace of the policy you want to retrieve. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum (required)
        :param str name: This query parameter specifies the user-defined name of the return policy you want to retrieve. (required)
        :return: ReturnPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['marketplace_id', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_return_policy_by_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'marketplace_id' is set
        if ('marketplace_id' not in params or
                params['marketplace_id'] is None):
            raise ValueError("Missing the required parameter `marketplace_id` when calling `get_return_policy_by_name`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_return_policy_by_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marketplace_id' in params:
            query_params.append(('marketplace_id', params['marketplace_id']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501

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
            '/return_policy/get_by_policy_name', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReturnPolicy',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_return_policy(self, body, return_policy_id, **kwargs):  # noqa: E501
        """update_return_policy  # noqa: E501

        This method updates an existing return policy. Specify the policy you want to update using the return_policy_id path parameter. Supply a complete policy payload with the updates you want to make; this call overwrites the existing policy with the new details specified in the payload.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_return_policy(body, return_policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ReturnPolicyRequest body: Container for a return policy request. (required)
        :param str return_policy_id: This path parameter specifies the ID of the return policy you want to update. (required)
        :return: SetReturnPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_return_policy_with_http_info(body, return_policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_return_policy_with_http_info(body, return_policy_id, **kwargs)  # noqa: E501
            return data

    def update_return_policy_with_http_info(self, body, return_policy_id, **kwargs):  # noqa: E501
        """update_return_policy  # noqa: E501

        This method updates an existing return policy. Specify the policy you want to update using the return_policy_id path parameter. Supply a complete policy payload with the updates you want to make; this call overwrites the existing policy with the new details specified in the payload.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_return_policy_with_http_info(body, return_policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ReturnPolicyRequest body: Container for a return policy request. (required)
        :param str return_policy_id: This path parameter specifies the ID of the return policy you want to update. (required)
        :return: SetReturnPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'return_policy_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_return_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_return_policy`")  # noqa: E501
        # verify the required parameter 'return_policy_id' is set
        if ('return_policy_id' not in params or
                params['return_policy_id'] is None):
            raise ValueError("Missing the required parameter `return_policy_id` when calling `update_return_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'return_policy_id' in params:
            path_params['return_policy_id'] = params['return_policy_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/return_policy/{return_policy_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SetReturnPolicyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)