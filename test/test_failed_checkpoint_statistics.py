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
from flink_client.model.checkpoint_statistics import CheckpointStatistics
from flink_client.model.failed_checkpoint_statistics_all_of import FailedCheckpointStatisticsAllOf
from flink_client.model.task_checkpoint_statistics import TaskCheckpointStatistics
globals()['CheckpointStatistics'] = CheckpointStatistics
globals()['FailedCheckpointStatisticsAllOf'] = FailedCheckpointStatisticsAllOf
globals()['TaskCheckpointStatistics'] = TaskCheckpointStatistics
from flink_client.model.failed_checkpoint_statistics import FailedCheckpointStatistics


class TestFailedCheckpointStatistics(unittest.TestCase):
    """FailedCheckpointStatistics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFailedCheckpointStatistics(self):
        """Test FailedCheckpointStatistics"""
        # FIXME: construct object with mandatory attributes with example values
        # model = FailedCheckpointStatistics()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()