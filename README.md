# flink-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1/1.15-SNAPSHOT
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import flink_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import flink_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import flink_client
from pprint import pprint
from flink_client.api import default_api
from flink_client.model.asynchronous_operation_result import AsynchronousOperationResult
from flink_client.model.checkpoint_config_info import CheckpointConfigInfo
from flink_client.model.checkpoint_statistics import CheckpointStatistics
from flink_client.model.checkpointing_statistics import CheckpointingStatistics
from flink_client.model.cluster_configuration_info_entry import ClusterConfigurationInfoEntry
from flink_client.model.cluster_data_set_list_response_body import ClusterDataSetListResponseBody
from flink_client.model.cluster_overview_with_version import ClusterOverviewWithVersion
from flink_client.model.dashboard_configuration import DashboardConfiguration
from flink_client.model.jar_list_info import JarListInfo
from flink_client.model.jar_plan_request_body import JarPlanRequestBody
from flink_client.model.jar_run_request_body import JarRunRequestBody
from flink_client.model.jar_run_response_body import JarRunResponseBody
from flink_client.model.jar_upload_response_body import JarUploadResponseBody
from flink_client.model.job_accumulators_info import JobAccumulatorsInfo
from flink_client.model.job_config_info import JobConfigInfo
from flink_client.model.job_details_info import JobDetailsInfo
from flink_client.model.job_exceptions_info_with_history import JobExceptionsInfoWithHistory
from flink_client.model.job_execution_result_response_body import JobExecutionResultResponseBody
from flink_client.model.job_ids_with_status_overview import JobIdsWithStatusOverview
from flink_client.model.job_plan_info import JobPlanInfo
from flink_client.model.job_submit_request_body import JobSubmitRequestBody
from flink_client.model.job_submit_response_body import JobSubmitResponseBody
from flink_client.model.job_vertex_accumulators_info import JobVertexAccumulatorsInfo
from flink_client.model.job_vertex_back_pressure_info import JobVertexBackPressureInfo
from flink_client.model.job_vertex_details_info import JobVertexDetailsInfo
from flink_client.model.job_vertex_flame_graph import JobVertexFlameGraph
from flink_client.model.job_vertex_task_managers_info import JobVertexTaskManagersInfo
from flink_client.model.log_list_info import LogListInfo
from flink_client.model.metric_collection_response_body import MetricCollectionResponseBody
from flink_client.model.multiple_jobs_details import MultipleJobsDetails
from flink_client.model.savepoint_disposal_request import SavepointDisposalRequest
from flink_client.model.savepoint_trigger_request_body import SavepointTriggerRequestBody
from flink_client.model.stop_with_savepoint_request_body import StopWithSavepointRequestBody
from flink_client.model.subtask_execution_attempt_accumulators_info import SubtaskExecutionAttemptAccumulatorsInfo
from flink_client.model.subtask_execution_attempt_details_info import SubtaskExecutionAttemptDetailsInfo
from flink_client.model.subtasks_all_accumulators_info import SubtasksAllAccumulatorsInfo
from flink_client.model.subtasks_times_info import SubtasksTimesInfo
from flink_client.model.task_checkpoint_statistics_with_subtask_details import TaskCheckpointStatisticsWithSubtaskDetails
from flink_client.model.task_manager_details_info import TaskManagerDetailsInfo
from flink_client.model.task_managers_info import TaskManagersInfo
from flink_client.model.thread_dump_info import ThreadDumpInfo
from flink_client.model.trigger_response import TriggerResponse
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with flink_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    try:
        api_instance.cluster_delete()
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->cluster_delete: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**cluster_delete**](docs/DefaultApi.md#cluster_delete) | **DELETE** /cluster | 
*DefaultApi* | [**config_get**](docs/DefaultApi.md#config_get) | **GET** /config | 
*DefaultApi* | [**datasets_datasetid_delete**](docs/DefaultApi.md#datasets_datasetid_delete) | **DELETE** /datasets/{datasetid} | 
*DefaultApi* | [**datasets_delete_triggerid_get**](docs/DefaultApi.md#datasets_delete_triggerid_get) | **GET** /datasets/delete/{triggerid} | 
*DefaultApi* | [**datasets_get**](docs/DefaultApi.md#datasets_get) | **GET** /datasets | 
*DefaultApi* | [**jars_get**](docs/DefaultApi.md#jars_get) | **GET** /jars | 
*DefaultApi* | [**jars_jarid_delete**](docs/DefaultApi.md#jars_jarid_delete) | **DELETE** /jars/{jarid} | 
*DefaultApi* | [**jars_jarid_plan_get**](docs/DefaultApi.md#jars_jarid_plan_get) | **GET** /jars/{jarid}/plan | 
*DefaultApi* | [**jars_jarid_plan_post**](docs/DefaultApi.md#jars_jarid_plan_post) | **POST** /jars/{jarid}/plan | 
*DefaultApi* | [**jars_jarid_run_post**](docs/DefaultApi.md#jars_jarid_run_post) | **POST** /jars/{jarid}/run | 
*DefaultApi* | [**jars_upload_post**](docs/DefaultApi.md#jars_upload_post) | **POST** /jars/upload | 
*DefaultApi* | [**jobmanager_config_get**](docs/DefaultApi.md#jobmanager_config_get) | **GET** /jobmanager/config | 
*DefaultApi* | [**jobmanager_logs_get**](docs/DefaultApi.md#jobmanager_logs_get) | **GET** /jobmanager/logs | 
*DefaultApi* | [**jobmanager_metrics_get**](docs/DefaultApi.md#jobmanager_metrics_get) | **GET** /jobmanager/metrics | 
*DefaultApi* | [**jobmanager_thread_dump_get**](docs/DefaultApi.md#jobmanager_thread_dump_get) | **GET** /jobmanager/thread-dump | 
*DefaultApi* | [**jobs_get**](docs/DefaultApi.md#jobs_get) | **GET** /jobs | 
*DefaultApi* | [**jobs_jobid_accumulators_get**](docs/DefaultApi.md#jobs_jobid_accumulators_get) | **GET** /jobs/{jobid}/accumulators | 
*DefaultApi* | [**jobs_jobid_checkpoints_config_get**](docs/DefaultApi.md#jobs_jobid_checkpoints_config_get) | **GET** /jobs/{jobid}/checkpoints/config | 
*DefaultApi* | [**jobs_jobid_checkpoints_details_checkpointid_get**](docs/DefaultApi.md#jobs_jobid_checkpoints_details_checkpointid_get) | **GET** /jobs/{jobid}/checkpoints/details/{checkpointid} | 
*DefaultApi* | [**jobs_jobid_checkpoints_details_checkpointid_subtasks_vertexid_get**](docs/DefaultApi.md#jobs_jobid_checkpoints_details_checkpointid_subtasks_vertexid_get) | **GET** /jobs/{jobid}/checkpoints/details/{checkpointid}/subtasks/{vertexid} | 
*DefaultApi* | [**jobs_jobid_checkpoints_get**](docs/DefaultApi.md#jobs_jobid_checkpoints_get) | **GET** /jobs/{jobid}/checkpoints | 
*DefaultApi* | [**jobs_jobid_config_get**](docs/DefaultApi.md#jobs_jobid_config_get) | **GET** /jobs/{jobid}/config | 
*DefaultApi* | [**jobs_jobid_exceptions_get**](docs/DefaultApi.md#jobs_jobid_exceptions_get) | **GET** /jobs/{jobid}/exceptions | 
*DefaultApi* | [**jobs_jobid_execution_result_get**](docs/DefaultApi.md#jobs_jobid_execution_result_get) | **GET** /jobs/{jobid}/execution-result | 
*DefaultApi* | [**jobs_jobid_get**](docs/DefaultApi.md#jobs_jobid_get) | **GET** /jobs/{jobid} | 
*DefaultApi* | [**jobs_jobid_metrics_get**](docs/DefaultApi.md#jobs_jobid_metrics_get) | **GET** /jobs/{jobid}/metrics | 
*DefaultApi* | [**jobs_jobid_patch**](docs/DefaultApi.md#jobs_jobid_patch) | **PATCH** /jobs/{jobid} | 
*DefaultApi* | [**jobs_jobid_plan_get**](docs/DefaultApi.md#jobs_jobid_plan_get) | **GET** /jobs/{jobid}/plan | 
*DefaultApi* | [**jobs_jobid_rescaling_patch**](docs/DefaultApi.md#jobs_jobid_rescaling_patch) | **PATCH** /jobs/{jobid}/rescaling | 
*DefaultApi* | [**jobs_jobid_rescaling_triggerid_get**](docs/DefaultApi.md#jobs_jobid_rescaling_triggerid_get) | **GET** /jobs/{jobid}/rescaling/{triggerid} | 
*DefaultApi* | [**jobs_jobid_savepoints_post**](docs/DefaultApi.md#jobs_jobid_savepoints_post) | **POST** /jobs/{jobid}/savepoints | 
*DefaultApi* | [**jobs_jobid_savepoints_triggerid_get**](docs/DefaultApi.md#jobs_jobid_savepoints_triggerid_get) | **GET** /jobs/{jobid}/savepoints/{triggerid} | 
*DefaultApi* | [**jobs_jobid_stop_post**](docs/DefaultApi.md#jobs_jobid_stop_post) | **POST** /jobs/{jobid}/stop | 
*DefaultApi* | [**jobs_jobid_vertices_vertexid_accumulators_get**](docs/DefaultApi.md#jobs_jobid_vertices_vertexid_accumulators_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/accumulators | 
*DefaultApi* | [**jobs_jobid_vertices_vertexid_backpressure_get**](docs/DefaultApi.md#jobs_jobid_vertices_vertexid_backpressure_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/backpressure | 
*DefaultApi* | [**jobs_jobid_vertices_vertexid_flamegraph_get**](docs/DefaultApi.md#jobs_jobid_vertices_vertexid_flamegraph_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/flamegraph | 
*DefaultApi* | [**jobs_jobid_vertices_vertexid_get**](docs/DefaultApi.md#jobs_jobid_vertices_vertexid_get) | **GET** /jobs/{jobid}/vertices/{vertexid} | 
*DefaultApi* | [**jobs_jobid_vertices_vertexid_metrics_get**](docs/DefaultApi.md#jobs_jobid_vertices_vertexid_metrics_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/metrics | 
*DefaultApi* | [**jobs_jobid_vertices_vertexid_subtasks_accumulators_get**](docs/DefaultApi.md#jobs_jobid_vertices_vertexid_subtasks_accumulators_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/subtasks/accumulators | 
*DefaultApi* | [**jobs_jobid_vertices_vertexid_subtasks_metrics_get**](docs/DefaultApi.md#jobs_jobid_vertices_vertexid_subtasks_metrics_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/subtasks/metrics | 
*DefaultApi* | [**jobs_jobid_vertices_vertexid_subtasks_subtaskindex_attempts_attempt_accumulators_get**](docs/DefaultApi.md#jobs_jobid_vertices_vertexid_subtasks_subtaskindex_attempts_attempt_accumulators_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/subtasks/{subtaskindex}/attempts/{attempt}/accumulators | 
*DefaultApi* | [**jobs_jobid_vertices_vertexid_subtasks_subtaskindex_attempts_attempt_get**](docs/DefaultApi.md#jobs_jobid_vertices_vertexid_subtasks_subtaskindex_attempts_attempt_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/subtasks/{subtaskindex}/attempts/{attempt} | 
*DefaultApi* | [**jobs_jobid_vertices_vertexid_subtasks_subtaskindex_get**](docs/DefaultApi.md#jobs_jobid_vertices_vertexid_subtasks_subtaskindex_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/subtasks/{subtaskindex} | 
*DefaultApi* | [**jobs_jobid_vertices_vertexid_subtasks_subtaskindex_metrics_get**](docs/DefaultApi.md#jobs_jobid_vertices_vertexid_subtasks_subtaskindex_metrics_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/subtasks/{subtaskindex}/metrics | 
*DefaultApi* | [**jobs_jobid_vertices_vertexid_subtasktimes_get**](docs/DefaultApi.md#jobs_jobid_vertices_vertexid_subtasktimes_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/subtasktimes | 
*DefaultApi* | [**jobs_jobid_vertices_vertexid_taskmanagers_get**](docs/DefaultApi.md#jobs_jobid_vertices_vertexid_taskmanagers_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/taskmanagers | 
*DefaultApi* | [**jobs_jobid_vertices_vertexid_watermarks_get**](docs/DefaultApi.md#jobs_jobid_vertices_vertexid_watermarks_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/watermarks | 
*DefaultApi* | [**jobs_metrics_get**](docs/DefaultApi.md#jobs_metrics_get) | **GET** /jobs/metrics | 
*DefaultApi* | [**jobs_overview_get**](docs/DefaultApi.md#jobs_overview_get) | **GET** /jobs/overview | 
*DefaultApi* | [**jobs_post**](docs/DefaultApi.md#jobs_post) | **POST** /jobs | 
*DefaultApi* | [**overview_get**](docs/DefaultApi.md#overview_get) | **GET** /overview | 
*DefaultApi* | [**savepoint_disposal_post**](docs/DefaultApi.md#savepoint_disposal_post) | **POST** /savepoint-disposal | 
*DefaultApi* | [**savepoint_disposal_triggerid_get**](docs/DefaultApi.md#savepoint_disposal_triggerid_get) | **GET** /savepoint-disposal/{triggerid} | 
*DefaultApi* | [**taskmanagers_get**](docs/DefaultApi.md#taskmanagers_get) | **GET** /taskmanagers | 
*DefaultApi* | [**taskmanagers_metrics_get**](docs/DefaultApi.md#taskmanagers_metrics_get) | **GET** /taskmanagers/metrics | 
*DefaultApi* | [**taskmanagers_taskmanagerid_get**](docs/DefaultApi.md#taskmanagers_taskmanagerid_get) | **GET** /taskmanagers/{taskmanagerid} | 
*DefaultApi* | [**taskmanagers_taskmanagerid_logs_get**](docs/DefaultApi.md#taskmanagers_taskmanagerid_logs_get) | **GET** /taskmanagers/{taskmanagerid}/logs | 
*DefaultApi* | [**taskmanagers_taskmanagerid_metrics_get**](docs/DefaultApi.md#taskmanagers_taskmanagerid_metrics_get) | **GET** /taskmanagers/{taskmanagerid}/metrics | 
*DefaultApi* | [**taskmanagers_taskmanagerid_thread_dump_get**](docs/DefaultApi.md#taskmanagers_taskmanagerid_thread_dump_get) | **GET** /taskmanagers/{taskmanagerid}/thread-dump | 


## Documentation For Models

 - [AsynchronousOperationInfo](docs/AsynchronousOperationInfo.md)
 - [AsynchronousOperationResult](docs/AsynchronousOperationResult.md)
 - [AsynchronousOperationResultOperation](docs/AsynchronousOperationResultOperation.md)
 - [CheckpointAlignment](docs/CheckpointAlignment.md)
 - [CheckpointConfigInfo](docs/CheckpointConfigInfo.md)
 - [CheckpointDuration](docs/CheckpointDuration.md)
 - [CheckpointStatistics](docs/CheckpointStatistics.md)
 - [CheckpointingStatistics](docs/CheckpointingStatistics.md)
 - [ClusterConfigurationInfo](docs/ClusterConfigurationInfo.md)
 - [ClusterConfigurationInfoEntry](docs/ClusterConfigurationInfoEntry.md)
 - [ClusterDataSetEntry](docs/ClusterDataSetEntry.md)
 - [ClusterDataSetListResponseBody](docs/ClusterDataSetListResponseBody.md)
 - [ClusterOverviewWithVersion](docs/ClusterOverviewWithVersion.md)
 - [CompletedCheckpointStatistics](docs/CompletedCheckpointStatistics.md)
 - [CompletedCheckpointStatisticsAllOf](docs/CompletedCheckpointStatisticsAllOf.md)
 - [CompletedSubtaskCheckpointStatistics](docs/CompletedSubtaskCheckpointStatistics.md)
 - [CompletedSubtaskCheckpointStatisticsAllOf](docs/CompletedSubtaskCheckpointStatisticsAllOf.md)
 - [Counts](docs/Counts.md)
 - [DashboardConfiguration](docs/DashboardConfiguration.md)
 - [DistributedCacheFile](docs/DistributedCacheFile.md)
 - [ExceptionInfo](docs/ExceptionInfo.md)
 - [ExecutionConfigInfo](docs/ExecutionConfigInfo.md)
 - [ExecutionExceptionInfo](docs/ExecutionExceptionInfo.md)
 - [ExternalizedCheckpointInfo](docs/ExternalizedCheckpointInfo.md)
 - [FailedCheckpointStatistics](docs/FailedCheckpointStatistics.md)
 - [FailedCheckpointStatisticsAllOf](docs/FailedCheckpointStatisticsAllOf.md)
 - [Features](docs/Features.md)
 - [GarbageCollectorInfo](docs/GarbageCollectorInfo.md)
 - [HardwareDescription](docs/HardwareDescription.md)
 - [IOMetricsInfo](docs/IOMetricsInfo.md)
 - [IntermediateDataSetID](docs/IntermediateDataSetID.md)
 - [JarEntryInfo](docs/JarEntryInfo.md)
 - [JarFileInfo](docs/JarFileInfo.md)
 - [JarListInfo](docs/JarListInfo.md)
 - [JarPlanRequestBody](docs/JarPlanRequestBody.md)
 - [JarRunRequestBody](docs/JarRunRequestBody.md)
 - [JarRunResponseBody](docs/JarRunResponseBody.md)
 - [JarUploadResponseBody](docs/JarUploadResponseBody.md)
 - [JobAccumulatorsInfo](docs/JobAccumulatorsInfo.md)
 - [JobConfigInfo](docs/JobConfigInfo.md)
 - [JobDetails](docs/JobDetails.md)
 - [JobDetailsInfo](docs/JobDetailsInfo.md)
 - [JobExceptionHistory](docs/JobExceptionHistory.md)
 - [JobExceptionsInfoWithHistory](docs/JobExceptionsInfoWithHistory.md)
 - [JobExecutionResultResponseBody](docs/JobExecutionResultResponseBody.md)
 - [JobID](docs/JobID.md)
 - [JobIdWithStatus](docs/JobIdWithStatus.md)
 - [JobIdsWithStatusOverview](docs/JobIdsWithStatusOverview.md)
 - [JobPlanInfo](docs/JobPlanInfo.md)
 - [JobResult](docs/JobResult.md)
 - [JobSubmitRequestBody](docs/JobSubmitRequestBody.md)
 - [JobSubmitResponseBody](docs/JobSubmitResponseBody.md)
 - [JobVertexAccumulatorsInfo](docs/JobVertexAccumulatorsInfo.md)
 - [JobVertexBackPressureInfo](docs/JobVertexBackPressureInfo.md)
 - [JobVertexDetailsInfo](docs/JobVertexDetailsInfo.md)
 - [JobVertexFlameGraph](docs/JobVertexFlameGraph.md)
 - [JobVertexID](docs/JobVertexID.md)
 - [JobVertexTaskManagersInfo](docs/JobVertexTaskManagersInfo.md)
 - [JobsGetRequest](docs/JobsGetRequest.md)
 - [LatestCheckpoints](docs/LatestCheckpoints.md)
 - [LogInfo](docs/LogInfo.md)
 - [LogListInfo](docs/LogListInfo.md)
 - [Metric](docs/Metric.md)
 - [MetricCollectionResponseBody](docs/MetricCollectionResponseBody.md)
 - [MultipleJobsDetails](docs/MultipleJobsDetails.md)
 - [Node](docs/Node.md)
 - [PendingCheckpointStatistics](docs/PendingCheckpointStatistics.md)
 - [PendingSubtaskCheckpointStatistics](docs/PendingSubtaskCheckpointStatistics.md)
 - [QueueStatus](docs/QueueStatus.md)
 - [ResourceID](docs/ResourceID.md)
 - [ResourceProfileInfo](docs/ResourceProfileInfo.md)
 - [RestoredCheckpointStatistics](docs/RestoredCheckpointStatistics.md)
 - [RootExceptionInfo](docs/RootExceptionInfo.md)
 - [SavepointDisposalRequest](docs/SavepointDisposalRequest.md)
 - [SavepointInfo](docs/SavepointInfo.md)
 - [SavepointTriggerRequestBody](docs/SavepointTriggerRequestBody.md)
 - [SerializedThrowable](docs/SerializedThrowable.md)
 - [SerializedValueOptionalFailureObject](docs/SerializedValueOptionalFailureObject.md)
 - [SlotInfo](docs/SlotInfo.md)
 - [StatsSummaryDto](docs/StatsSummaryDto.md)
 - [StopWithSavepointRequestBody](docs/StopWithSavepointRequestBody.md)
 - [SubtaskAccumulatorsInfo](docs/SubtaskAccumulatorsInfo.md)
 - [SubtaskBackPressureInfo](docs/SubtaskBackPressureInfo.md)
 - [SubtaskCheckpointStatistics](docs/SubtaskCheckpointStatistics.md)
 - [SubtaskExecutionAttemptAccumulatorsInfo](docs/SubtaskExecutionAttemptAccumulatorsInfo.md)
 - [SubtaskExecutionAttemptDetailsInfo](docs/SubtaskExecutionAttemptDetailsInfo.md)
 - [SubtaskTimeInfo](docs/SubtaskTimeInfo.md)
 - [SubtasksAllAccumulatorsInfo](docs/SubtasksAllAccumulatorsInfo.md)
 - [SubtasksTimesInfo](docs/SubtasksTimesInfo.md)
 - [Summary](docs/Summary.md)
 - [TaskCheckpointStatistics](docs/TaskCheckpointStatistics.md)
 - [TaskCheckpointStatisticsWithSubtaskDetails](docs/TaskCheckpointStatisticsWithSubtaskDetails.md)
 - [TaskExecutorMemoryConfiguration](docs/TaskExecutorMemoryConfiguration.md)
 - [TaskManagerDetailsInfo](docs/TaskManagerDetailsInfo.md)
 - [TaskManagerInfo](docs/TaskManagerInfo.md)
 - [TaskManagerMetricsInfo](docs/TaskManagerMetricsInfo.md)
 - [TaskManagersInfo](docs/TaskManagersInfo.md)
 - [ThreadDumpInfo](docs/ThreadDumpInfo.md)
 - [ThreadInfo](docs/ThreadInfo.md)
 - [TriggerId](docs/TriggerId.md)
 - [TriggerResponse](docs/TriggerResponse.md)
 - [UserAccumulator](docs/UserAccumulator.md)
 - [UserTaskAccumulator](docs/UserTaskAccumulator.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author

user@flink.apache.org


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in flink_client.apis and flink_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from flink_client.api.default_api import DefaultApi`
- `from flink_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import flink_client
from flink_client.apis import *
from flink_client.models import *
```
