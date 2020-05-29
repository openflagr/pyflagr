# coding: utf-8

"""
    Flagr

    Flagr is a feature flagging, A/B testing and dynamic configuration microservice. The base path for all the APIs is \"/api/v1\".   # noqa: E501

    OpenAPI spec version: 1.1.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PutSegmentReorderRequest(object):
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
        'segment_i_ds': 'list[int]'
    }

    attribute_map = {
        'segment_i_ds': 'segmentIDs'
    }

    def __init__(self, segment_i_ds=None):  # noqa: E501
        """PutSegmentReorderRequest - a model defined in Swagger"""  # noqa: E501

        self._segment_i_ds = None
        self.discriminator = None

        self.segment_i_ds = segment_i_ds

    @property
    def segment_i_ds(self):
        """Gets the segment_i_ds of this PutSegmentReorderRequest.  # noqa: E501


        :return: The segment_i_ds of this PutSegmentReorderRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._segment_i_ds

    @segment_i_ds.setter
    def segment_i_ds(self, segment_i_ds):
        """Sets the segment_i_ds of this PutSegmentReorderRequest.


        :param segment_i_ds: The segment_i_ds of this PutSegmentReorderRequest.  # noqa: E501
        :type: list[int]
        """
        if segment_i_ds is None:
            raise ValueError("Invalid value for `segment_i_ds`, must not be `None`")  # noqa: E501

        self._segment_i_ds = segment_i_ds

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
        if issubclass(PutSegmentReorderRequest, dict):
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
        if not isinstance(other, PutSegmentReorderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
