# coding: utf-8

"""
    Flagr

    Flagr is a feature flagging, A/B testing and dynamic configuration microservice. The base path for all the APIs is \"/api/v1\".   # noqa: E501

    OpenAPI spec version: 1.1.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import flagr
from flagr.models.create_tag_request import CreateTagRequest  # noqa: E501
from flagr.rest import ApiException


class TestCreateTagRequest(unittest.TestCase):
    """CreateTagRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateTagRequest(self):
        """Test CreateTagRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = flagr.models.create_tag_request.CreateTagRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()