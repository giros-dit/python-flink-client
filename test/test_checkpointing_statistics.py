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
from flink_client.model.counts import Counts
from flink_client.model.latest_checkpoints import LatestCheckpoints
from flink_client.model.summary import Summary
globals()['CheckpointStatistics'] = CheckpointStatistics
globals()['Counts'] = Counts
globals()['LatestCheckpoints'] = LatestCheckpoints
globals()['Summary'] = Summary
from flink_client.model.checkpointing_statistics import CheckpointingStatistics


class TestCheckpointingStatistics(unittest.TestCase):
    """CheckpointingStatistics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCheckpointingStatistics(self):
        """Test CheckpointingStatistics"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CheckpointingStatistics()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()