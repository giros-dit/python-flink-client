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
from flink_client.model.job_result import JobResult
from flink_client.model.queue_status import QueueStatus
globals()['JobResult'] = JobResult
globals()['QueueStatus'] = QueueStatus
from flink_client.model.job_execution_result_response_body import JobExecutionResultResponseBody


class TestJobExecutionResultResponseBody(unittest.TestCase):
    """JobExecutionResultResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testJobExecutionResultResponseBody(self):
        """Test JobExecutionResultResponseBody"""
        # FIXME: construct object with mandatory attributes with example values
        # model = JobExecutionResultResponseBody()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
