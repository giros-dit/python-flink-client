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
from flink_client.model.execution_config_info import ExecutionConfigInfo
from flink_client.model.job_id import JobID
globals()['ExecutionConfigInfo'] = ExecutionConfigInfo
globals()['JobID'] = JobID
from flink_client.model.job_config_info import JobConfigInfo


class TestJobConfigInfo(unittest.TestCase):
    """JobConfigInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testJobConfigInfo(self):
        """Test JobConfigInfo"""
        # FIXME: construct object with mandatory attributes with example values
        # model = JobConfigInfo()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
