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
from flink_client.model.job_id import JobID
globals()['JobID'] = JobID
from flink_client.model.job_details import JobDetails


class TestJobDetails(unittest.TestCase):
    """JobDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testJobDetails(self):
        """Test JobDetails"""
        # FIXME: construct object with mandatory attributes with example values
        # model = JobDetails()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
