"""
    Flink JobManager REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1/1.15-SNAPSHOT
    Contact: user@flink.apache.org
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import flink_client
from flink_client.model.serialized_value_optional_failure_object import SerializedValueOptionalFailureObject
from flink_client.model.user_task_accumulator import UserTaskAccumulator
globals()['SerializedValueOptionalFailureObject'] = SerializedValueOptionalFailureObject
globals()['UserTaskAccumulator'] = UserTaskAccumulator
from flink_client.model.job_accumulators_info import JobAccumulatorsInfo


class TestJobAccumulatorsInfo(unittest.TestCase):
    """JobAccumulatorsInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testJobAccumulatorsInfo(self):
        """Test JobAccumulatorsInfo"""
        # FIXME: construct object with mandatory attributes with example values
        # model = JobAccumulatorsInfo()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
