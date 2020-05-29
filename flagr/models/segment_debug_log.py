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


class SegmentDebugLog(object):
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
        'segment_id': 'int',
        'msg': 'str'
    }

    attribute_map = {
        'segment_id': 'segmentID',
        'msg': 'msg'
    }

    def __init__(self, segment_id=None, msg=None):  # noqa: E501
        """SegmentDebugLog - a model defined in Swagger"""  # noqa: E501

        self._segment_id = None
        self._msg = None
        self.discriminator = None

        if segment_id is not None:
            self.segment_id = segment_id
        if msg is not None:
            self.msg = msg

    @property
    def segment_id(self):
        """Gets the segment_id of this SegmentDebugLog.  # noqa: E501


        :return: The segment_id of this SegmentDebugLog.  # noqa: E501
        :rtype: int
        """
        return self._segment_id

    @segment_id.setter
    def segment_id(self, segment_id):
        """Sets the segment_id of this SegmentDebugLog.


        :param segment_id: The segment_id of this SegmentDebugLog.  # noqa: E501
        :type: int
        """
        if segment_id is not None and segment_id < 1:  # noqa: E501
            raise ValueError("Invalid value for `segment_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._segment_id = segment_id

    @property
    def msg(self):
        """Gets the msg of this SegmentDebugLog.  # noqa: E501


        :return: The msg of this SegmentDebugLog.  # noqa: E501
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this SegmentDebugLog.


        :param msg: The msg of this SegmentDebugLog.  # noqa: E501
        :type: str
        """

        self._msg = msg

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
        if issubclass(SegmentDebugLog, dict):
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
        if not isinstance(other, SegmentDebugLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
