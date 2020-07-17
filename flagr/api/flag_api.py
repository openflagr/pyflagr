# coding: utf-8

"""
    Flagr

    Flagr is a feature flagging, A/B testing and dynamic configuration microservice. The base path for all the APIs is \"/api/v1\".   # noqa: E501

    OpenAPI spec version: 1.1.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from flagr.api_client import ApiClient


class FlagApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_flag(self, body, **kwargs):  # noqa: E501
        """create_flag  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_flag(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateFlagRequest body: create a flag (required)
        :return: Flag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_flag_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_flag_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_flag_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_flag  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_flag_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateFlagRequest body: create a flag (required)
        :return: Flag
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
                    " to method create_flag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_flag`")  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/flags', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Flag',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_flag(self, flag_id, **kwargs):  # noqa: E501
        """delete_flag  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_flag(flag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int flag_id: numeric ID of the flag (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_flag_with_http_info(flag_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_flag_with_http_info(flag_id, **kwargs)  # noqa: E501
            return data

    def delete_flag_with_http_info(self, flag_id, **kwargs):  # noqa: E501
        """delete_flag  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_flag_with_http_info(flag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int flag_id: numeric ID of the flag (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['flag_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_flag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'flag_id' is set
        if ('flag_id' not in params or
                params['flag_id'] is None):
            raise ValueError("Missing the required parameter `flag_id` when calling `delete_flag`")  # noqa: E501

        if 'flag_id' in params and params['flag_id'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `flag_id` when calling `delete_flag`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'flag_id' in params:
            path_params['flagID'] = params['flag_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/flags/{flagID}', 'DELETE',
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

    def find_flags(self, **kwargs):  # noqa: E501
        """find_flags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_flags(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: the numbers of flags to return
        :param bool enabled: return flags having given enabled status
        :param str description: return flags exactly matching given description
        :param str tags: return flags with the given tags (comma separated)
        :param str description_like: return flags partially matching given description
        :param str key: return flags matching given key
        :param int offset: return flags given the offset, it should usually set together with limit
        :param bool preload: return flags with preloaded segments and variants
        :return: list[Flag]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.find_flags_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.find_flags_with_http_info(**kwargs)  # noqa: E501
            return data

    def find_flags_with_http_info(self, **kwargs):  # noqa: E501
        """find_flags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_flags_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: the numbers of flags to return
        :param bool enabled: return flags having given enabled status
        :param str description: return flags exactly matching given description
        :param str tags: return flags with the given tags (comma separated)
        :param str description_like: return flags partially matching given description
        :param str key: return flags matching given key
        :param int offset: return flags given the offset, it should usually set together with limit
        :param bool preload: return flags with preloaded segments and variants
        :return: list[Flag]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'enabled', 'description', 'tags', 'description_like', 'key', 'offset', 'preload']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_flags" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'enabled' in params:
            query_params.append(('enabled', params['enabled']))  # noqa: E501
        if 'description' in params:
            query_params.append(('description', params['description']))  # noqa: E501
        if 'tags' in params:
            query_params.append(('tags', params['tags']))  # noqa: E501
        if 'description_like' in params:
            query_params.append(('description_like', params['description_like']))  # noqa: E501
        if 'key' in params:
            query_params.append(('key', params['key']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'preload' in params:
            query_params.append(('preload', params['preload']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/flags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Flag]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_flag(self, flag_id, **kwargs):  # noqa: E501
        """get_flag  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_flag(flag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int flag_id: numeric ID of the flag to get (required)
        :return: Flag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_flag_with_http_info(flag_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_flag_with_http_info(flag_id, **kwargs)  # noqa: E501
            return data

    def get_flag_with_http_info(self, flag_id, **kwargs):  # noqa: E501
        """get_flag  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_flag_with_http_info(flag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int flag_id: numeric ID of the flag to get (required)
        :return: Flag
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['flag_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_flag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'flag_id' is set
        if ('flag_id' not in params or
                params['flag_id'] is None):
            raise ValueError("Missing the required parameter `flag_id` when calling `get_flag`")  # noqa: E501

        if 'flag_id' in params and params['flag_id'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `flag_id` when calling `get_flag`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'flag_id' in params:
            path_params['flagID'] = params['flag_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/flags/{flagID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Flag',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_flag_entity_types(self, **kwargs):  # noqa: E501
        """get_flag_entity_types  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_flag_entity_types(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_flag_entity_types_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_flag_entity_types_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_flag_entity_types_with_http_info(self, **kwargs):  # noqa: E501
        """get_flag_entity_types  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_flag_entity_types_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_flag_entity_types" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/flags/entity_types', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_flag_snapshots(self, flag_id, **kwargs):  # noqa: E501
        """get_flag_snapshots  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_flag_snapshots(flag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int flag_id: numeric ID of the flag to get (required)
        :return: list[FlagSnapshot]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_flag_snapshots_with_http_info(flag_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_flag_snapshots_with_http_info(flag_id, **kwargs)  # noqa: E501
            return data

    def get_flag_snapshots_with_http_info(self, flag_id, **kwargs):  # noqa: E501
        """get_flag_snapshots  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_flag_snapshots_with_http_info(flag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int flag_id: numeric ID of the flag to get (required)
        :return: list[FlagSnapshot]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['flag_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_flag_snapshots" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'flag_id' is set
        if ('flag_id' not in params or
                params['flag_id'] is None):
            raise ValueError("Missing the required parameter `flag_id` when calling `get_flag_snapshots`")  # noqa: E501

        if 'flag_id' in params and params['flag_id'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `flag_id` when calling `get_flag_snapshots`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'flag_id' in params:
            path_params['flagID'] = params['flag_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/flags/{flagID}/snapshots', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[FlagSnapshot]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_flag(self, flag_id, body, **kwargs):  # noqa: E501
        """put_flag  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_flag(flag_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int flag_id: numeric ID of the flag to get (required)
        :param PutFlagRequest body: update a flag (required)
        :return: Flag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_flag_with_http_info(flag_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.put_flag_with_http_info(flag_id, body, **kwargs)  # noqa: E501
            return data

    def put_flag_with_http_info(self, flag_id, body, **kwargs):  # noqa: E501
        """put_flag  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_flag_with_http_info(flag_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int flag_id: numeric ID of the flag to get (required)
        :param PutFlagRequest body: update a flag (required)
        :return: Flag
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['flag_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_flag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'flag_id' is set
        if ('flag_id' not in params or
                params['flag_id'] is None):
            raise ValueError("Missing the required parameter `flag_id` when calling `put_flag`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_flag`")  # noqa: E501

        if 'flag_id' in params and params['flag_id'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `flag_id` when calling `put_flag`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'flag_id' in params:
            path_params['flagID'] = params['flag_id']  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/flags/{flagID}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Flag',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_flag_enabled(self, flag_id, body, **kwargs):  # noqa: E501
        """set_flag_enabled  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_flag_enabled(flag_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int flag_id: numeric ID of the flag to get (required)
        :param SetFlagEnabledRequest body: set flag enabled state (required)
        :return: Flag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_flag_enabled_with_http_info(flag_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.set_flag_enabled_with_http_info(flag_id, body, **kwargs)  # noqa: E501
            return data

    def set_flag_enabled_with_http_info(self, flag_id, body, **kwargs):  # noqa: E501
        """set_flag_enabled  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_flag_enabled_with_http_info(flag_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int flag_id: numeric ID of the flag to get (required)
        :param SetFlagEnabledRequest body: set flag enabled state (required)
        :return: Flag
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['flag_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_flag_enabled" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'flag_id' is set
        if ('flag_id' not in params or
                params['flag_id'] is None):
            raise ValueError("Missing the required parameter `flag_id` when calling `set_flag_enabled`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `set_flag_enabled`")  # noqa: E501

        if 'flag_id' in params and params['flag_id'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `flag_id` when calling `set_flag_enabled`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'flag_id' in params:
            path_params['flagID'] = params['flag_id']  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/flags/{flagID}/enabled', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Flag',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
