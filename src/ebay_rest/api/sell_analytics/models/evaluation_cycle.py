# coding: utf-8

"""
     Seller Service Metrics API 

    The <i>Analytics API</i> provides data and information about a seller and their eBay business.  <br><br>The resources and methods in this API let sellers review information on their listing performance, metrics on their customer service performance, and details on their eBay seller performance rating.  <br><br>The three resources in the Analytics API provide the following data and information: <ul><li><b>Customer Service Metric</b> &ndash; Returns data on a seller's customer service performance as compared to other seller's in the same peer group.</li> <li><b>Traffic Report</b> &ndash; Returns data that shows how buyers are engaging with a seller's listings.</li> <li><b>Seller Standards Profile</b> &ndash; Returns data pertaining to a seller's performance rating.</li></ul> Sellers can use the data and information returned by the various Analytics API methods to determine where they can make improvements to increase sales and how they might improve their seller status as viewed by eBay buyers.  <br><br>For details on using this API, see <a href=\"/api-docs/sell/static/performance/analyzing-performance.html\" title=\"Selling Integration Guide\">Analyzing seller performance</a>.  # noqa: E501

    OpenAPI spec version: 1.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EvaluationCycle(object):
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
        'end_date': 'str',
        'evaluation_date': 'str',
        'evaluation_type': 'str',
        'start_date': 'str'
    }

    attribute_map = {
        'end_date': 'endDate',
        'evaluation_date': 'evaluationDate',
        'evaluation_type': 'evaluationType',
        'start_date': 'startDate'
    }

    def __init__(self, end_date=None, evaluation_date=None, evaluation_type=None, start_date=None):  # noqa: E501
        """EvaluationCycle - a model defined in Swagger"""  # noqa: E501
        self._end_date = None
        self._evaluation_date = None
        self._evaluation_type = None
        self._start_date = None
        self.discriminator = None
        if end_date is not None:
            self.end_date = end_date
        if evaluation_date is not None:
            self.evaluation_date = evaluation_date
        if evaluation_type is not None:
            self.evaluation_type = evaluation_type
        if start_date is not None:
            self.start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this EvaluationCycle.  # noqa: E501

        End date and time of the transaction lookback range. All timestamps are based on Mountain Standard Time (MST). The timestamp is formatted as an ISO 8601 string, which is based on the 24-hour Coordinated Universal Time (UTC) clock.  # noqa: E501

        :return: The end_date of this EvaluationCycle.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this EvaluationCycle.

        End date and time of the transaction lookback range. All timestamps are based on Mountain Standard Time (MST). The timestamp is formatted as an ISO 8601 string, which is based on the 24-hour Coordinated Universal Time (UTC) clock.  # noqa: E501

        :param end_date: The end_date of this EvaluationCycle.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def evaluation_date(self):
        """Gets the evaluation_date of this EvaluationCycle.  # noqa: E501

        The ISO-8601 date and time at which the seller was evaluated for this customer service metric rating.  # noqa: E501

        :return: The evaluation_date of this EvaluationCycle.  # noqa: E501
        :rtype: str
        """
        return self._evaluation_date

    @evaluation_date.setter
    def evaluation_date(self, evaluation_date):
        """Sets the evaluation_date of this EvaluationCycle.

        The ISO-8601 date and time at which the seller was evaluated for this customer service metric rating.  # noqa: E501

        :param evaluation_date: The evaluation_date of this EvaluationCycle.  # noqa: E501
        :type: str
        """

        self._evaluation_date = evaluation_date

    @property
    def evaluation_type(self):
        """Gets the evaluation_type of this EvaluationCycle.  # noqa: E501

        This field specifies the transaction lookback period used for the evaluation. The evaluation_type value specified in the request is returned in this field. There are two possible values: CURRENT &ndash; A monthly evaluation that occurs on the 20th of every month. PROJECTED &ndash; A daily evaluation that provides a projection of how the seller is currently performing with regards to the upcoming evaluation period. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/analytics/types/api:EvaluationTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The evaluation_type of this EvaluationCycle.  # noqa: E501
        :rtype: str
        """
        return self._evaluation_type

    @evaluation_type.setter
    def evaluation_type(self, evaluation_type):
        """Sets the evaluation_type of this EvaluationCycle.

        This field specifies the transaction lookback period used for the evaluation. The evaluation_type value specified in the request is returned in this field. There are two possible values: CURRENT &ndash; A monthly evaluation that occurs on the 20th of every month. PROJECTED &ndash; A daily evaluation that provides a projection of how the seller is currently performing with regards to the upcoming evaluation period. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/analytics/types/api:EvaluationTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param evaluation_type: The evaluation_type of this EvaluationCycle.  # noqa: E501
        :type: str
        """

        self._evaluation_type = evaluation_type

    @property
    def start_date(self):
        """Gets the start_date of this EvaluationCycle.  # noqa: E501

        The start date and time of the transaction lookback range. All timestamps are based on Mountain Standard Time (MST). The timestamp is formatted as an ISO 8601 string, which is based on the 24-hour Coordinated Universal Time (UTC) clock. Format: [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z Example: 2018-08-04T07:09:00.000Z  # noqa: E501

        :return: The start_date of this EvaluationCycle.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this EvaluationCycle.

        The start date and time of the transaction lookback range. All timestamps are based on Mountain Standard Time (MST). The timestamp is formatted as an ISO 8601 string, which is based on the 24-hour Coordinated Universal Time (UTC) clock. Format: [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z Example: 2018-08-04T07:09:00.000Z  # noqa: E501

        :param start_date: The start_date of this EvaluationCycle.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

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
        if issubclass(EvaluationCycle, dict):
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
        if not isinstance(other, EvaluationCycle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other