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
from flink_client.model.subtask_checkpoint_statistics import SubtaskCheckpointStatistics
from flink_client.model.summary import Summary
globals()['SubtaskCheckpointStatistics'] = SubtaskCheckpointStatistics
globals()['Summary'] = Summary
from flink_client.model.task_checkpoint_statistics_with_subtask_details import TaskCheckpointStatisticsWithSubtaskDetails


class TestTaskCheckpointStatisticsWithSubtaskDetails(unittest.TestCase):
    """TaskCheckpointStatisticsWithSubtaskDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTaskCheckpointStatisticsWithSubtaskDetails(self):
        """Test TaskCheckpointStatisticsWithSubtaskDetails"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TaskCheckpointStatisticsWithSubtaskDetails()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
