# flink_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cluster_delete**](DefaultApi.md#cluster_delete) | **DELETE** /cluster | 
[**config_get**](DefaultApi.md#config_get) | **GET** /config | 
[**datasets_datasetid_delete**](DefaultApi.md#datasets_datasetid_delete) | **DELETE** /datasets/{datasetid} | 
[**datasets_delete_triggerid_get**](DefaultApi.md#datasets_delete_triggerid_get) | **GET** /datasets/delete/{triggerid} | 
[**datasets_get**](DefaultApi.md#datasets_get) | **GET** /datasets | 
[**jars_get**](DefaultApi.md#jars_get) | **GET** /jars | 
[**jars_jarid_delete**](DefaultApi.md#jars_jarid_delete) | **DELETE** /jars/{jarid} | 
[**jars_jarid_plan_get**](DefaultApi.md#jars_jarid_plan_get) | **GET** /jars/{jarid}/plan | 
[**jars_jarid_plan_post**](DefaultApi.md#jars_jarid_plan_post) | **POST** /jars/{jarid}/plan | 
[**jars_jarid_run_post**](DefaultApi.md#jars_jarid_run_post) | **POST** /jars/{jarid}/run | 
[**jars_upload_post**](DefaultApi.md#jars_upload_post) | **POST** /jars/upload | 
[**jobmanager_config_get**](DefaultApi.md#jobmanager_config_get) | **GET** /jobmanager/config | 
[**jobmanager_logs_get**](DefaultApi.md#jobmanager_logs_get) | **GET** /jobmanager/logs | 
[**jobmanager_metrics_get**](DefaultApi.md#jobmanager_metrics_get) | **GET** /jobmanager/metrics | 
[**jobmanager_thread_dump_get**](DefaultApi.md#jobmanager_thread_dump_get) | **GET** /jobmanager/thread-dump | 
[**jobs_get**](DefaultApi.md#jobs_get) | **GET** /jobs | 
[**jobs_jobid_accumulators_get**](DefaultApi.md#jobs_jobid_accumulators_get) | **GET** /jobs/{jobid}/accumulators | 
[**jobs_jobid_checkpoints_config_get**](DefaultApi.md#jobs_jobid_checkpoints_config_get) | **GET** /jobs/{jobid}/checkpoints/config | 
[**jobs_jobid_checkpoints_details_checkpointid_get**](DefaultApi.md#jobs_jobid_checkpoints_details_checkpointid_get) | **GET** /jobs/{jobid}/checkpoints/details/{checkpointid} | 
[**jobs_jobid_checkpoints_details_checkpointid_subtasks_vertexid_get**](DefaultApi.md#jobs_jobid_checkpoints_details_checkpointid_subtasks_vertexid_get) | **GET** /jobs/{jobid}/checkpoints/details/{checkpointid}/subtasks/{vertexid} | 
[**jobs_jobid_checkpoints_get**](DefaultApi.md#jobs_jobid_checkpoints_get) | **GET** /jobs/{jobid}/checkpoints | 
[**jobs_jobid_config_get**](DefaultApi.md#jobs_jobid_config_get) | **GET** /jobs/{jobid}/config | 
[**jobs_jobid_exceptions_get**](DefaultApi.md#jobs_jobid_exceptions_get) | **GET** /jobs/{jobid}/exceptions | 
[**jobs_jobid_execution_result_get**](DefaultApi.md#jobs_jobid_execution_result_get) | **GET** /jobs/{jobid}/execution-result | 
[**jobs_jobid_get**](DefaultApi.md#jobs_jobid_get) | **GET** /jobs/{jobid} | 
[**jobs_jobid_metrics_get**](DefaultApi.md#jobs_jobid_metrics_get) | **GET** /jobs/{jobid}/metrics | 
[**jobs_jobid_patch**](DefaultApi.md#jobs_jobid_patch) | **PATCH** /jobs/{jobid} | 
[**jobs_jobid_plan_get**](DefaultApi.md#jobs_jobid_plan_get) | **GET** /jobs/{jobid}/plan | 
[**jobs_jobid_rescaling_patch**](DefaultApi.md#jobs_jobid_rescaling_patch) | **PATCH** /jobs/{jobid}/rescaling | 
[**jobs_jobid_rescaling_triggerid_get**](DefaultApi.md#jobs_jobid_rescaling_triggerid_get) | **GET** /jobs/{jobid}/rescaling/{triggerid} | 
[**jobs_jobid_savepoints_post**](DefaultApi.md#jobs_jobid_savepoints_post) | **POST** /jobs/{jobid}/savepoints | 
[**jobs_jobid_savepoints_triggerid_get**](DefaultApi.md#jobs_jobid_savepoints_triggerid_get) | **GET** /jobs/{jobid}/savepoints/{triggerid} | 
[**jobs_jobid_stop_post**](DefaultApi.md#jobs_jobid_stop_post) | **POST** /jobs/{jobid}/stop | 
[**jobs_jobid_vertices_vertexid_accumulators_get**](DefaultApi.md#jobs_jobid_vertices_vertexid_accumulators_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/accumulators | 
[**jobs_jobid_vertices_vertexid_backpressure_get**](DefaultApi.md#jobs_jobid_vertices_vertexid_backpressure_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/backpressure | 
[**jobs_jobid_vertices_vertexid_flamegraph_get**](DefaultApi.md#jobs_jobid_vertices_vertexid_flamegraph_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/flamegraph | 
[**jobs_jobid_vertices_vertexid_get**](DefaultApi.md#jobs_jobid_vertices_vertexid_get) | **GET** /jobs/{jobid}/vertices/{vertexid} | 
[**jobs_jobid_vertices_vertexid_metrics_get**](DefaultApi.md#jobs_jobid_vertices_vertexid_metrics_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/metrics | 
[**jobs_jobid_vertices_vertexid_subtasks_accumulators_get**](DefaultApi.md#jobs_jobid_vertices_vertexid_subtasks_accumulators_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/subtasks/accumulators | 
[**jobs_jobid_vertices_vertexid_subtasks_metrics_get**](DefaultApi.md#jobs_jobid_vertices_vertexid_subtasks_metrics_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/subtasks/metrics | 
[**jobs_jobid_vertices_vertexid_subtasks_subtaskindex_attempts_attempt_accumulators_get**](DefaultApi.md#jobs_jobid_vertices_vertexid_subtasks_subtaskindex_attempts_attempt_accumulators_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/subtasks/{subtaskindex}/attempts/{attempt}/accumulators | 
[**jobs_jobid_vertices_vertexid_subtasks_subtaskindex_attempts_attempt_get**](DefaultApi.md#jobs_jobid_vertices_vertexid_subtasks_subtaskindex_attempts_attempt_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/subtasks/{subtaskindex}/attempts/{attempt} | 
[**jobs_jobid_vertices_vertexid_subtasks_subtaskindex_get**](DefaultApi.md#jobs_jobid_vertices_vertexid_subtasks_subtaskindex_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/subtasks/{subtaskindex} | 
[**jobs_jobid_vertices_vertexid_subtasks_subtaskindex_metrics_get**](DefaultApi.md#jobs_jobid_vertices_vertexid_subtasks_subtaskindex_metrics_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/subtasks/{subtaskindex}/metrics | 
[**jobs_jobid_vertices_vertexid_subtasktimes_get**](DefaultApi.md#jobs_jobid_vertices_vertexid_subtasktimes_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/subtasktimes | 
[**jobs_jobid_vertices_vertexid_taskmanagers_get**](DefaultApi.md#jobs_jobid_vertices_vertexid_taskmanagers_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/taskmanagers | 
[**jobs_jobid_vertices_vertexid_watermarks_get**](DefaultApi.md#jobs_jobid_vertices_vertexid_watermarks_get) | **GET** /jobs/{jobid}/vertices/{vertexid}/watermarks | 
[**jobs_metrics_get**](DefaultApi.md#jobs_metrics_get) | **GET** /jobs/metrics | 
[**jobs_overview_get**](DefaultApi.md#jobs_overview_get) | **GET** /jobs/overview | 
[**jobs_post**](DefaultApi.md#jobs_post) | **POST** /jobs | 
[**overview_get**](DefaultApi.md#overview_get) | **GET** /overview | 
[**savepoint_disposal_post**](DefaultApi.md#savepoint_disposal_post) | **POST** /savepoint-disposal | 
[**savepoint_disposal_triggerid_get**](DefaultApi.md#savepoint_disposal_triggerid_get) | **GET** /savepoint-disposal/{triggerid} | 
[**taskmanagers_get**](DefaultApi.md#taskmanagers_get) | **GET** /taskmanagers | 
[**taskmanagers_metrics_get**](DefaultApi.md#taskmanagers_metrics_get) | **GET** /taskmanagers/metrics | 
[**taskmanagers_taskmanagerid_get**](DefaultApi.md#taskmanagers_taskmanagerid_get) | **GET** /taskmanagers/{taskmanagerid} | 
[**taskmanagers_taskmanagerid_logs_get**](DefaultApi.md#taskmanagers_taskmanagerid_logs_get) | **GET** /taskmanagers/{taskmanagerid}/logs | 
[**taskmanagers_taskmanagerid_metrics_get**](DefaultApi.md#taskmanagers_taskmanagerid_metrics_get) | **GET** /taskmanagers/{taskmanagerid}/metrics | 
[**taskmanagers_taskmanagerid_thread_dump_get**](DefaultApi.md#taskmanagers_taskmanagerid_thread_dump_get) | **GET** /taskmanagers/{taskmanagerid}/thread-dump | 


# **cluster_delete**
> cluster_delete()



Shuts down the cluster

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.cluster_delete()
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->cluster_delete: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_get**
> DashboardConfiguration config_get()



Returns the configuration of the WebUI.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.dashboard_configuration import DashboardConfiguration
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.config_get()
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->config_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DashboardConfiguration**](DashboardConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_datasetid_delete**
> TriggerResponse datasets_datasetid_delete(datasetid)



Triggers the deletion of a cluster data set. This async operation would return a 'triggerid' for further query identifier.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.trigger_response import TriggerResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    datasetid = IntermediateDataSetID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a cluster data set.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.datasets_datasetid_delete(datasetid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->datasets_datasetid_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasetid** | **str**| 32-character hexadecimal string value that identifies a cluster data set. |

### Return type

[**TriggerResponse**](TriggerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_delete_triggerid_get**
> AsynchronousOperationResult datasets_delete_triggerid_get(triggerid)



Returns the status for the delete operation of a cluster data set.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.asynchronous_operation_result import AsynchronousOperationResult
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    triggerid = TriggerId("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string that identifies an asynchronous operation trigger ID. The ID was returned then the operation was triggered.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.datasets_delete_triggerid_get(triggerid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->datasets_delete_triggerid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **triggerid** | **str**| 32-character hexadecimal string that identifies an asynchronous operation trigger ID. The ID was returned then the operation was triggered. |

### Return type

[**AsynchronousOperationResult**](AsynchronousOperationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_get**
> ClusterDataSetListResponseBody datasets_get()



Returns all cluster data sets.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.cluster_data_set_list_response_body import ClusterDataSetListResponseBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.datasets_get()
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->datasets_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterDataSetListResponseBody**](ClusterDataSetListResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jars_get**
> JarListInfo jars_get()



Returns a list of all jars previously uploaded via '/jars/upload'.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.jar_list_info import JarListInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.jars_get()
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jars_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**JarListInfo**](JarListInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jars_jarid_delete**
> jars_jarid_delete(jarid)



Deletes a jar previously uploaded via '/jars/upload'.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jarid = "jarid_example" # str | String value that identifies a jar. When uploading the jar a path is returned, where the filename is the ID. This value is equivalent to the `id` field in the list of uploaded jars (/jars).

    # example passing only required values which don't have defaults set
    try:
        api_instance.jars_jarid_delete(jarid)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jars_jarid_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jarid** | **str**| String value that identifies a jar. When uploading the jar a path is returned, where the filename is the ID. This value is equivalent to the &#x60;id&#x60; field in the list of uploaded jars (/jars). |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jars_jarid_plan_get**
> JobPlanInfo jars_jarid_plan_get(jarid)



Returns the dataflow plan of a job contained in a jar previously uploaded via '/jars/upload'. Program arguments can be passed both via the JSON request (recommended) or query parameters.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.job_plan_info import JobPlanInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jarid = "jarid_example" # str | String value that identifies a jar. When uploading the jar a path is returned, where the filename is the ID. This value is equivalent to the `id` field in the list of uploaded jars (/jars).
    program_args = "program-args_example" # str | Deprecated, please use 'programArg' instead. String value that specifies the arguments for the program or plan (optional)
    program_arg = "programArg_example" # str | Comma-separated list of program arguments. (optional)
    entry_class = "entry-class_example" # str | String value that specifies the fully qualified name of the entry point class. Overrides the class defined in the jar file manifest. (optional)
    parallelism = 1 # int | Positive integer value that specifies the desired parallelism for the job. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jars_jarid_plan_get(jarid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jars_jarid_plan_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.jars_jarid_plan_get(jarid, program_args=program_args, program_arg=program_arg, entry_class=entry_class, parallelism=parallelism)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jars_jarid_plan_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jarid** | **str**| String value that identifies a jar. When uploading the jar a path is returned, where the filename is the ID. This value is equivalent to the &#x60;id&#x60; field in the list of uploaded jars (/jars). |
 **program_args** | **str**| Deprecated, please use &#39;programArg&#39; instead. String value that specifies the arguments for the program or plan | [optional]
 **program_arg** | **str**| Comma-separated list of program arguments. | [optional]
 **entry_class** | **str**| String value that specifies the fully qualified name of the entry point class. Overrides the class defined in the jar file manifest. | [optional]
 **parallelism** | **int**| Positive integer value that specifies the desired parallelism for the job. | [optional]

### Return type

[**JobPlanInfo**](JobPlanInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jars_jarid_plan_post**
> JobPlanInfo jars_jarid_plan_post(jarid)



Returns the dataflow plan of a job contained in a jar previously uploaded via '/jars/upload'. Program arguments can be passed both via the JSON request (recommended) or query parameters.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.jar_plan_request_body import JarPlanRequestBody
from flink_client.model.job_plan_info import JobPlanInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jarid = "jarid_example" # str | String value that identifies a jar. When uploading the jar a path is returned, where the filename is the ID. This value is equivalent to the `id` field in the list of uploaded jars (/jars).
    program_args = "program-args_example" # str | Deprecated, please use 'programArg' instead. String value that specifies the arguments for the program or plan (optional)
    program_arg = "programArg_example" # str | Comma-separated list of program arguments. (optional)
    entry_class = "entry-class_example" # str | String value that specifies the fully qualified name of the entry point class. Overrides the class defined in the jar file manifest. (optional)
    parallelism = 1 # int | Positive integer value that specifies the desired parallelism for the job. (optional)
    jar_plan_request_body = JarPlanRequestBody(
        entry_class="entry_class_example",
        program_args="program_args_example",
        program_args_list=[
            "program_args_list_example",
        ],
        parallelism=1,
        job_id=JobID("bf325375e030fccba00917317c574773"),
    ) # JarPlanRequestBody |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jars_jarid_plan_post(jarid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jars_jarid_plan_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.jars_jarid_plan_post(jarid, program_args=program_args, program_arg=program_arg, entry_class=entry_class, parallelism=parallelism, jar_plan_request_body=jar_plan_request_body)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jars_jarid_plan_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jarid** | **str**| String value that identifies a jar. When uploading the jar a path is returned, where the filename is the ID. This value is equivalent to the &#x60;id&#x60; field in the list of uploaded jars (/jars). |
 **program_args** | **str**| Deprecated, please use &#39;programArg&#39; instead. String value that specifies the arguments for the program or plan | [optional]
 **program_arg** | **str**| Comma-separated list of program arguments. | [optional]
 **entry_class** | **str**| String value that specifies the fully qualified name of the entry point class. Overrides the class defined in the jar file manifest. | [optional]
 **parallelism** | **int**| Positive integer value that specifies the desired parallelism for the job. | [optional]
 **jar_plan_request_body** | [**JarPlanRequestBody**](JarPlanRequestBody.md)|  | [optional]

### Return type

[**JobPlanInfo**](JobPlanInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jars_jarid_run_post**
> JarRunResponseBody jars_jarid_run_post(jarid)



Submits a job by running a jar previously uploaded via '/jars/upload'. Program arguments can be passed both via the JSON request (recommended) or query parameters.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.jar_run_request_body import JarRunRequestBody
from flink_client.model.jar_run_response_body import JarRunResponseBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jarid = "jarid_example" # str | String value that identifies a jar. When uploading the jar a path is returned, where the filename is the ID. This value is equivalent to the `id` field in the list of uploaded jars (/jars).
    allow_non_restored_state = True # bool | Boolean value that specifies whether the job submission should be rejected if the savepoint contains state that cannot be mapped back to the job. (optional)
    savepoint_path = "savepointPath_example" # str | String value that specifies the path of the savepoint to restore the job from. (optional)
    program_args = "program-args_example" # str | Deprecated, please use 'programArg' instead. String value that specifies the arguments for the program or plan (optional)
    program_arg = "programArg_example" # str | Comma-separated list of program arguments. (optional)
    entry_class = "entry-class_example" # str | String value that specifies the fully qualified name of the entry point class. Overrides the class defined in the jar file manifest. (optional)
    parallelism = 1 # int | Positive integer value that specifies the desired parallelism for the job. (optional)
    jar_run_request_body = JarRunRequestBody(
        entry_class="entry_class_example",
        program_args="program_args_example",
        program_args_list=[
            "program_args_list_example",
        ],
        parallelism=1,
        job_id=JobID("bf325375e030fccba00917317c574773"),
        allow_non_restored_state=True,
        savepoint_path="savepoint_path_example",
        restore_mode="CLAIM",
    ) # JarRunRequestBody |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jars_jarid_run_post(jarid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jars_jarid_run_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.jars_jarid_run_post(jarid, allow_non_restored_state=allow_non_restored_state, savepoint_path=savepoint_path, program_args=program_args, program_arg=program_arg, entry_class=entry_class, parallelism=parallelism, jar_run_request_body=jar_run_request_body)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jars_jarid_run_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jarid** | **str**| String value that identifies a jar. When uploading the jar a path is returned, where the filename is the ID. This value is equivalent to the &#x60;id&#x60; field in the list of uploaded jars (/jars). |
 **allow_non_restored_state** | **bool**| Boolean value that specifies whether the job submission should be rejected if the savepoint contains state that cannot be mapped back to the job. | [optional]
 **savepoint_path** | **str**| String value that specifies the path of the savepoint to restore the job from. | [optional]
 **program_args** | **str**| Deprecated, please use &#39;programArg&#39; instead. String value that specifies the arguments for the program or plan | [optional]
 **program_arg** | **str**| Comma-separated list of program arguments. | [optional]
 **entry_class** | **str**| String value that specifies the fully qualified name of the entry point class. Overrides the class defined in the jar file manifest. | [optional]
 **parallelism** | **int**| Positive integer value that specifies the desired parallelism for the job. | [optional]
 **jar_run_request_body** | [**JarRunRequestBody**](JarRunRequestBody.md)|  | [optional]

### Return type

[**JarRunResponseBody**](JarRunResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jars_upload_post**
> JarUploadResponseBody jars_upload_post(body)



Uploads a jar to the cluster. The jar must be sent as multi-part data. Make sure that the \"Content-Type\" header is set to \"application/x-java-archive\", as some http libraries do not add the header by default. Using 'curl' you can upload a jar via 'curl -X POST -H \"Expect:\" -F \"jarfile=@path/to/flink-job.jar\" http://hostname:port/jars/upload'.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.jar_upload_response_body import JarUploadResponseBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jars_upload_post(body)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jars_upload_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**JarUploadResponseBody**](JarUploadResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-java-archive
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobmanager_config_get**
> [ClusterConfigurationInfoEntry] jobmanager_config_get()



Returns the cluster configuration.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.cluster_configuration_info_entry import ClusterConfigurationInfoEntry
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.jobmanager_config_get()
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobmanager_config_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[ClusterConfigurationInfoEntry]**](ClusterConfigurationInfoEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobmanager_logs_get**
> LogListInfo jobmanager_logs_get()



Returns the list of log files on the JobManager.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.log_list_info import LogListInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.jobmanager_logs_get()
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobmanager_logs_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**LogListInfo**](LogListInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobmanager_metrics_get**
> MetricCollectionResponseBody jobmanager_metrics_get()



Provides access to job manager metrics.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.metric_collection_response_body import MetricCollectionResponseBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    get = "get_example" # str | Comma-separated list of string values to select specific metrics. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.jobmanager_metrics_get(get=get)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobmanager_metrics_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get** | **str**| Comma-separated list of string values to select specific metrics. | [optional]

### Return type

[**MetricCollectionResponseBody**](MetricCollectionResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobmanager_thread_dump_get**
> ThreadDumpInfo jobmanager_thread_dump_get()



Returns the thread dump of the JobManager.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.thread_dump_info import ThreadDumpInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.jobmanager_thread_dump_get()
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobmanager_thread_dump_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ThreadDumpInfo**](ThreadDumpInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_get**
> JobIdsWithStatusOverview jobs_get()



Returns an overview over all jobs and their current state.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.job_ids_with_status_overview import JobIdsWithStatusOverview
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.jobs_get()
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**JobIdsWithStatusOverview**](JobIdsWithStatusOverview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_accumulators_get**
> JobAccumulatorsInfo jobs_jobid_accumulators_get(jobid)



Returns the accumulators for all tasks of a job, aggregated across the respective subtasks.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.job_accumulators_info import JobAccumulatorsInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    include_serialized_value = True # bool | Boolean value that specifies whether serialized user task accumulators should be included in the response. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_accumulators_get(jobid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_accumulators_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.jobs_jobid_accumulators_get(jobid, include_serialized_value=include_serialized_value)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_accumulators_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **include_serialized_value** | **bool**| Boolean value that specifies whether serialized user task accumulators should be included in the response. | [optional]

### Return type

[**JobAccumulatorsInfo**](JobAccumulatorsInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_checkpoints_config_get**
> CheckpointConfigInfo jobs_jobid_checkpoints_config_get(jobid)



Returns the checkpointing configuration.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.checkpoint_config_info import CheckpointConfigInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_checkpoints_config_get(jobid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_checkpoints_config_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |

### Return type

[**CheckpointConfigInfo**](CheckpointConfigInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_checkpoints_details_checkpointid_get**
> CheckpointStatistics jobs_jobid_checkpoints_details_checkpointid_get(jobid, checkpointid)



Returns details for a checkpoint.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.checkpoint_statistics import CheckpointStatistics
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    checkpointid = 1 # int | Long value that identifies a checkpoint.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_checkpoints_details_checkpointid_get(jobid, checkpointid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_checkpoints_details_checkpointid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **checkpointid** | **int**| Long value that identifies a checkpoint. |

### Return type

[**CheckpointStatistics**](CheckpointStatistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_checkpoints_details_checkpointid_subtasks_vertexid_get**
> TaskCheckpointStatisticsWithSubtaskDetails jobs_jobid_checkpoints_details_checkpointid_subtasks_vertexid_get(jobid, checkpointid, vertexid)



Returns checkpoint statistics for a task and its subtasks.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.task_checkpoint_statistics_with_subtask_details import TaskCheckpointStatisticsWithSubtaskDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    checkpointid = 1 # int | Long value that identifies a checkpoint.
    vertexid = JobVertexID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job vertex.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_checkpoints_details_checkpointid_subtasks_vertexid_get(jobid, checkpointid, vertexid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_checkpoints_details_checkpointid_subtasks_vertexid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **checkpointid** | **int**| Long value that identifies a checkpoint. |
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex. |

### Return type

[**TaskCheckpointStatisticsWithSubtaskDetails**](TaskCheckpointStatisticsWithSubtaskDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_checkpoints_get**
> CheckpointingStatistics jobs_jobid_checkpoints_get(jobid)



Returns checkpointing statistics for a job.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.checkpointing_statistics import CheckpointingStatistics
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_checkpoints_get(jobid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_checkpoints_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |

### Return type

[**CheckpointingStatistics**](CheckpointingStatistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_config_get**
> JobConfigInfo jobs_jobid_config_get(jobid)



Returns the configuration of a job.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.job_config_info import JobConfigInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_config_get(jobid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_config_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |

### Return type

[**JobConfigInfo**](JobConfigInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_exceptions_get**
> JobExceptionsInfoWithHistory jobs_jobid_exceptions_get(jobid)



Returns the most recent exceptions that have been handled by Flink for this job. The 'exceptionHistory.truncated' flag defines whether exceptions were filtered out through the GET parameter. The backend collects only a specific amount of most recent exceptions per job. This can be configured through web.exception-history-size in the Flink configuration. The following first-level members are deprecated: 'root-exception', 'timestamp', 'all-exceptions', and 'truncated'. Use the data provided through 'exceptionHistory', instead.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.job_exceptions_info_with_history import JobExceptionsInfoWithHistory
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    max_exceptions = 1 # int | Comma-separated list of integer values that specifies the upper limit of exceptions to return. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_exceptions_get(jobid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_exceptions_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.jobs_jobid_exceptions_get(jobid, max_exceptions=max_exceptions)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_exceptions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **max_exceptions** | **int**| Comma-separated list of integer values that specifies the upper limit of exceptions to return. | [optional]

### Return type

[**JobExceptionsInfoWithHistory**](JobExceptionsInfoWithHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_execution_result_get**
> JobExecutionResultResponseBody jobs_jobid_execution_result_get(jobid)



Returns the result of a job execution. Gives access to the execution time of the job and to all accumulators created by this job.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.job_execution_result_response_body import JobExecutionResultResponseBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_execution_result_get(jobid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_execution_result_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |

### Return type

[**JobExecutionResultResponseBody**](JobExecutionResultResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_get**
> JobDetailsInfo jobs_jobid_get(jobid)



Returns details of a job.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.job_details_info import JobDetailsInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_get(jobid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |

### Return type

[**JobDetailsInfo**](JobDetailsInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_metrics_get**
> MetricCollectionResponseBody jobs_jobid_metrics_get(jobid)



Provides access to job metrics.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.metric_collection_response_body import MetricCollectionResponseBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    get = "get_example" # str | Comma-separated list of string values to select specific metrics. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_metrics_get(jobid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_metrics_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.jobs_jobid_metrics_get(jobid, get=get)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_metrics_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **get** | **str**| Comma-separated list of string values to select specific metrics. | [optional]

### Return type

[**MetricCollectionResponseBody**](MetricCollectionResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_patch**
> jobs_jobid_patch(jobid)



Terminates a job.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    mode = "CANCEL" # str | String value that specifies the termination mode. The only supported value is: \"cancel\". (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.jobs_jobid_patch(jobid)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.jobs_jobid_patch(jobid, mode=mode)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **mode** | **str**| String value that specifies the termination mode. The only supported value is: \&quot;cancel\&quot;. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_plan_get**
> JobPlanInfo jobs_jobid_plan_get(jobid)



Returns the dataflow plan of a job.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.job_plan_info import JobPlanInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_plan_get(jobid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_plan_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |

### Return type

[**JobPlanInfo**](JobPlanInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_rescaling_patch**
> TriggerResponse jobs_jobid_rescaling_patch(jobid, parallelism)



Triggers the rescaling of a job. This async operation would return a 'triggerid' for further query identifier.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.trigger_response import TriggerResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    parallelism = 1 # int | Positive integer value that specifies the desired parallelism.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_rescaling_patch(jobid, parallelism)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_rescaling_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **parallelism** | **int**| Positive integer value that specifies the desired parallelism. |

### Return type

[**TriggerResponse**](TriggerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_rescaling_triggerid_get**
> AsynchronousOperationResult jobs_jobid_rescaling_triggerid_get(jobid, triggerid)



Returns the status of a rescaling operation.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.asynchronous_operation_result import AsynchronousOperationResult
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    triggerid = TriggerId("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string that identifies an asynchronous operation trigger ID. The ID was returned then the operation was triggered.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_rescaling_triggerid_get(jobid, triggerid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_rescaling_triggerid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **triggerid** | **str**| 32-character hexadecimal string that identifies an asynchronous operation trigger ID. The ID was returned then the operation was triggered. |

### Return type

[**AsynchronousOperationResult**](AsynchronousOperationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_savepoints_post**
> TriggerResponse jobs_jobid_savepoints_post(jobid)



Triggers a savepoint, and optionally cancels the job afterwards. This async operation would return a 'triggerid' for further query identifier.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.trigger_response import TriggerResponse
from flink_client.model.savepoint_trigger_request_body import SavepointTriggerRequestBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    savepoint_trigger_request_body = SavepointTriggerRequestBody(
        target_directory="target_directory_example",
        cancel_job=True,
        trigger_id=TriggerId("bf325375e030fccba00917317c574773"),
    ) # SavepointTriggerRequestBody |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_savepoints_post(jobid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_savepoints_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.jobs_jobid_savepoints_post(jobid, savepoint_trigger_request_body=savepoint_trigger_request_body)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_savepoints_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **savepoint_trigger_request_body** | [**SavepointTriggerRequestBody**](SavepointTriggerRequestBody.md)|  | [optional]

### Return type

[**TriggerResponse**](TriggerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_savepoints_triggerid_get**
> AsynchronousOperationResult jobs_jobid_savepoints_triggerid_get(jobid, triggerid)



Returns the status of a savepoint operation.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.asynchronous_operation_result import AsynchronousOperationResult
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    triggerid = TriggerId("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string that identifies an asynchronous operation trigger ID. The ID was returned then the operation was triggered.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_savepoints_triggerid_get(jobid, triggerid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_savepoints_triggerid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **triggerid** | **str**| 32-character hexadecimal string that identifies an asynchronous operation trigger ID. The ID was returned then the operation was triggered. |

### Return type

[**AsynchronousOperationResult**](AsynchronousOperationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_stop_post**
> TriggerResponse jobs_jobid_stop_post(jobid)



Stops a job with a savepoint. Optionally, it can also emit a MAX_WATERMARK before taking the savepoint to flush out any state waiting for timers to fire. This async operation would return a 'triggerid' for further query identifier.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.trigger_response import TriggerResponse
from flink_client.model.stop_with_savepoint_request_body import StopWithSavepointRequestBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    stop_with_savepoint_request_body = StopWithSavepointRequestBody(
        target_directory="target_directory_example",
        drain=True,
        trigger_id=TriggerId("bf325375e030fccba00917317c574773"),
    ) # StopWithSavepointRequestBody |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_stop_post(jobid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_stop_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.jobs_jobid_stop_post(jobid, stop_with_savepoint_request_body=stop_with_savepoint_request_body)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_stop_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **stop_with_savepoint_request_body** | [**StopWithSavepointRequestBody**](StopWithSavepointRequestBody.md)|  | [optional]

### Return type

[**TriggerResponse**](TriggerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_vertices_vertexid_accumulators_get**
> JobVertexAccumulatorsInfo jobs_jobid_vertices_vertexid_accumulators_get(jobid, vertexid)



Returns user-defined accumulators of a task, aggregated across all subtasks.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.job_vertex_accumulators_info import JobVertexAccumulatorsInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    vertexid = JobVertexID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job vertex.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_vertices_vertexid_accumulators_get(jobid, vertexid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_vertices_vertexid_accumulators_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex. |

### Return type

[**JobVertexAccumulatorsInfo**](JobVertexAccumulatorsInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_vertices_vertexid_backpressure_get**
> JobVertexBackPressureInfo jobs_jobid_vertices_vertexid_backpressure_get(jobid, vertexid)



Returns back-pressure information for a job, and may initiate back-pressure sampling if necessary.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.job_vertex_back_pressure_info import JobVertexBackPressureInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    vertexid = JobVertexID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job vertex.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_vertices_vertexid_backpressure_get(jobid, vertexid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_vertices_vertexid_backpressure_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex. |

### Return type

[**JobVertexBackPressureInfo**](JobVertexBackPressureInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_vertices_vertexid_flamegraph_get**
> JobVertexFlameGraph jobs_jobid_vertices_vertexid_flamegraph_get(jobid, vertexid)



Returns flame graph information for a vertex, and may initiate flame graph sampling if necessary.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.job_vertex_flame_graph import JobVertexFlameGraph
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    vertexid = JobVertexID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job vertex.
    type = "FULL" # str | String value that specifies the Flame Graph type. Supported options are: \"[FULL, ON_CPU, OFF_CPU]\". (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_vertices_vertexid_flamegraph_get(jobid, vertexid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_vertices_vertexid_flamegraph_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.jobs_jobid_vertices_vertexid_flamegraph_get(jobid, vertexid, type=type)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_vertices_vertexid_flamegraph_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex. |
 **type** | **str**| String value that specifies the Flame Graph type. Supported options are: \&quot;[FULL, ON_CPU, OFF_CPU]\&quot;. | [optional]

### Return type

[**JobVertexFlameGraph**](JobVertexFlameGraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_vertices_vertexid_get**
> JobVertexDetailsInfo jobs_jobid_vertices_vertexid_get(jobid, vertexid)



Returns details for a task, with a summary for each of its subtasks.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.job_vertex_details_info import JobVertexDetailsInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    vertexid = JobVertexID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job vertex.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_vertices_vertexid_get(jobid, vertexid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_vertices_vertexid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex. |

### Return type

[**JobVertexDetailsInfo**](JobVertexDetailsInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_vertices_vertexid_metrics_get**
> MetricCollectionResponseBody jobs_jobid_vertices_vertexid_metrics_get(jobid, vertexid)



Provides access to task metrics.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.metric_collection_response_body import MetricCollectionResponseBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    vertexid = JobVertexID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job vertex.
    get = "get_example" # str | Comma-separated list of string values to select specific metrics. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_vertices_vertexid_metrics_get(jobid, vertexid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_vertices_vertexid_metrics_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.jobs_jobid_vertices_vertexid_metrics_get(jobid, vertexid, get=get)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_vertices_vertexid_metrics_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex. |
 **get** | **str**| Comma-separated list of string values to select specific metrics. | [optional]

### Return type

[**MetricCollectionResponseBody**](MetricCollectionResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_vertices_vertexid_subtasks_accumulators_get**
> SubtasksAllAccumulatorsInfo jobs_jobid_vertices_vertexid_subtasks_accumulators_get(jobid, vertexid)



Returns all user-defined accumulators for all subtasks of a task.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.subtasks_all_accumulators_info import SubtasksAllAccumulatorsInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    vertexid = JobVertexID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job vertex.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_vertices_vertexid_subtasks_accumulators_get(jobid, vertexid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_vertices_vertexid_subtasks_accumulators_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex. |

### Return type

[**SubtasksAllAccumulatorsInfo**](SubtasksAllAccumulatorsInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_vertices_vertexid_subtasks_metrics_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} jobs_jobid_vertices_vertexid_subtasks_metrics_get(jobid, vertexid)



Provides access to aggregated subtask metrics.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    vertexid = JobVertexID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job vertex.
    get = "get_example" # str | Comma-separated list of string values to select specific metrics. (optional)
    agg = "MIN" # str | Comma-separated list of aggregation modes which should be calculated. Available aggregations are: \"min, max, sum, avg\". (optional)
    subtasks = "subtasks_example" # str | Comma-separated list of integer ranges (e.g. \"1,3,5-9\") to select specific subtasks. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_vertices_vertexid_subtasks_metrics_get(jobid, vertexid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_vertices_vertexid_subtasks_metrics_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.jobs_jobid_vertices_vertexid_subtasks_metrics_get(jobid, vertexid, get=get, agg=agg, subtasks=subtasks)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_vertices_vertexid_subtasks_metrics_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex. |
 **get** | **str**| Comma-separated list of string values to select specific metrics. | [optional]
 **agg** | **str**| Comma-separated list of aggregation modes which should be calculated. Available aggregations are: \&quot;min, max, sum, avg\&quot;. | [optional]
 **subtasks** | **str**| Comma-separated list of integer ranges (e.g. \&quot;1,3,5-9\&quot;) to select specific subtasks. | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_vertices_vertexid_subtasks_subtaskindex_attempts_attempt_accumulators_get**
> SubtaskExecutionAttemptAccumulatorsInfo jobs_jobid_vertices_vertexid_subtasks_subtaskindex_attempts_attempt_accumulators_get(jobid, vertexid, subtaskindex, attempt)



Returns the accumulators of an execution attempt of a subtask. Multiple execution attempts happen in case of failure/recovery.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.subtask_execution_attempt_accumulators_info import SubtaskExecutionAttemptAccumulatorsInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    vertexid = JobVertexID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job vertex.
    subtaskindex = 1 # int | Positive integer value that identifies a subtask.
    attempt = 1 # int | Positive integer value that identifies an execution attempt.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_vertices_vertexid_subtasks_subtaskindex_attempts_attempt_accumulators_get(jobid, vertexid, subtaskindex, attempt)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_vertices_vertexid_subtasks_subtaskindex_attempts_attempt_accumulators_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex. |
 **subtaskindex** | **int**| Positive integer value that identifies a subtask. |
 **attempt** | **int**| Positive integer value that identifies an execution attempt. |

### Return type

[**SubtaskExecutionAttemptAccumulatorsInfo**](SubtaskExecutionAttemptAccumulatorsInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_vertices_vertexid_subtasks_subtaskindex_attempts_attempt_get**
> SubtaskExecutionAttemptDetailsInfo jobs_jobid_vertices_vertexid_subtasks_subtaskindex_attempts_attempt_get(jobid, vertexid, subtaskindex, attempt)



Returns details of an execution attempt of a subtask. Multiple execution attempts happen in case of failure/recovery.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.subtask_execution_attempt_details_info import SubtaskExecutionAttemptDetailsInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    vertexid = JobVertexID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job vertex.
    subtaskindex = 1 # int | Positive integer value that identifies a subtask.
    attempt = 1 # int | Positive integer value that identifies an execution attempt.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_vertices_vertexid_subtasks_subtaskindex_attempts_attempt_get(jobid, vertexid, subtaskindex, attempt)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_vertices_vertexid_subtasks_subtaskindex_attempts_attempt_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex. |
 **subtaskindex** | **int**| Positive integer value that identifies a subtask. |
 **attempt** | **int**| Positive integer value that identifies an execution attempt. |

### Return type

[**SubtaskExecutionAttemptDetailsInfo**](SubtaskExecutionAttemptDetailsInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_vertices_vertexid_subtasks_subtaskindex_get**
> SubtaskExecutionAttemptDetailsInfo jobs_jobid_vertices_vertexid_subtasks_subtaskindex_get(jobid, vertexid, subtaskindex)



Returns details of the current or latest execution attempt of a subtask.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.subtask_execution_attempt_details_info import SubtaskExecutionAttemptDetailsInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    vertexid = JobVertexID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job vertex.
    subtaskindex = 1 # int | Positive integer value that identifies a subtask.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_vertices_vertexid_subtasks_subtaskindex_get(jobid, vertexid, subtaskindex)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_vertices_vertexid_subtasks_subtaskindex_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex. |
 **subtaskindex** | **int**| Positive integer value that identifies a subtask. |

### Return type

[**SubtaskExecutionAttemptDetailsInfo**](SubtaskExecutionAttemptDetailsInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_vertices_vertexid_subtasks_subtaskindex_metrics_get**
> MetricCollectionResponseBody jobs_jobid_vertices_vertexid_subtasks_subtaskindex_metrics_get(jobid, vertexid, subtaskindex)



Provides access to subtask metrics.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.metric_collection_response_body import MetricCollectionResponseBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    vertexid = JobVertexID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job vertex.
    subtaskindex = 1 # int | Positive integer value that identifies a subtask.
    get = "get_example" # str | Comma-separated list of string values to select specific metrics. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_vertices_vertexid_subtasks_subtaskindex_metrics_get(jobid, vertexid, subtaskindex)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_vertices_vertexid_subtasks_subtaskindex_metrics_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.jobs_jobid_vertices_vertexid_subtasks_subtaskindex_metrics_get(jobid, vertexid, subtaskindex, get=get)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_vertices_vertexid_subtasks_subtaskindex_metrics_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex. |
 **subtaskindex** | **int**| Positive integer value that identifies a subtask. |
 **get** | **str**| Comma-separated list of string values to select specific metrics. | [optional]

### Return type

[**MetricCollectionResponseBody**](MetricCollectionResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_vertices_vertexid_subtasktimes_get**
> SubtasksTimesInfo jobs_jobid_vertices_vertexid_subtasktimes_get(jobid, vertexid)



Returns time-related information for all subtasks of a task.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.subtasks_times_info import SubtasksTimesInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    vertexid = JobVertexID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job vertex.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_vertices_vertexid_subtasktimes_get(jobid, vertexid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_vertices_vertexid_subtasktimes_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex. |

### Return type

[**SubtasksTimesInfo**](SubtasksTimesInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_vertices_vertexid_taskmanagers_get**
> JobVertexTaskManagersInfo jobs_jobid_vertices_vertexid_taskmanagers_get(jobid, vertexid)



Returns task information aggregated by task manager.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.job_vertex_task_managers_info import JobVertexTaskManagersInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    vertexid = JobVertexID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job vertex.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_vertices_vertexid_taskmanagers_get(jobid, vertexid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_vertices_vertexid_taskmanagers_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex. |

### Return type

[**JobVertexTaskManagersInfo**](JobVertexTaskManagersInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobid_vertices_vertexid_watermarks_get**
> MetricCollectionResponseBody jobs_jobid_vertices_vertexid_watermarks_get(jobid, vertexid)



Returns the watermarks for all subtasks of a task.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.metric_collection_response_body import MetricCollectionResponseBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    jobid = JobID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job.
    vertexid = JobVertexID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string value that identifies a job vertex.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_jobid_vertices_vertexid_watermarks_get(jobid, vertexid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_jobid_vertices_vertexid_watermarks_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job. |
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex. |

### Return type

[**MetricCollectionResponseBody**](MetricCollectionResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_metrics_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} jobs_metrics_get()



Provides access to aggregated job metrics.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    get = "get_example" # str | Comma-separated list of string values to select specific metrics. (optional)
    agg = "MIN" # str | Comma-separated list of aggregation modes which should be calculated. Available aggregations are: \"min, max, sum, avg\". (optional)
    jobs = JobID("bf325375e030fccba00917317c574773") # str | Comma-separated list of 32-character hexadecimal strings to select specific jobs. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.jobs_metrics_get(get=get, agg=agg, jobs=jobs)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_metrics_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get** | **str**| Comma-separated list of string values to select specific metrics. | [optional]
 **agg** | **str**| Comma-separated list of aggregation modes which should be calculated. Available aggregations are: \&quot;min, max, sum, avg\&quot;. | [optional]
 **jobs** | **str**| Comma-separated list of 32-character hexadecimal strings to select specific jobs. | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_overview_get**
> MultipleJobsDetails jobs_overview_get()



Returns an overview over all jobs.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.multiple_jobs_details import MultipleJobsDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.jobs_overview_get()
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_overview_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MultipleJobsDetails**](MultipleJobsDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_post**
> JobSubmitResponseBody jobs_post()



Submits a job. This call is primarily intended to be used by the Flink client. This call expects a multipart/form-data request that consists of file uploads for the serialized JobGraph, jars and distributed cache artifacts and an attribute named \"request\" for the JSON payload.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.job_submit_request_body import JobSubmitRequestBody
from flink_client.model.job_submit_response_body import JobSubmitResponseBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    request = JobSubmitRequestBody(
        job_graph_file_name="job_graph_file_name_example",
        job_jar_file_names=[
            "job_jar_file_names_example",
        ],
        job_artifact_file_names=[
            DistributedCacheFile(
                entry_name="entry_name_example",
                file_name="file_name_example",
            ),
        ],
    ) # JobSubmitRequestBody |  (optional)
    filename = [
        open('/path/to/file', 'rb'),
    ] # [file_type] |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.jobs_post(request=request, filename=filename)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->jobs_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**JobSubmitRequestBody**](JobSubmitRequestBody.md)|  | [optional]
 **filename** | **[file_type]**|  | [optional]

### Return type

[**JobSubmitResponseBody**](JobSubmitResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **overview_get**
> ClusterOverviewWithVersion overview_get()



Returns an overview over the Flink cluster.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.cluster_overview_with_version import ClusterOverviewWithVersion
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.overview_get()
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->overview_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterOverviewWithVersion**](ClusterOverviewWithVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **savepoint_disposal_post**
> TriggerResponse savepoint_disposal_post()



Triggers the desposal of a savepoint. This async operation would return a 'triggerid' for further query identifier.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.savepoint_disposal_request import SavepointDisposalRequest
from flink_client.model.trigger_response import TriggerResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    savepoint_disposal_request = SavepointDisposalRequest(
        savepoint_path="savepoint_path_example",
    ) # SavepointDisposalRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.savepoint_disposal_post(savepoint_disposal_request=savepoint_disposal_request)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->savepoint_disposal_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **savepoint_disposal_request** | [**SavepointDisposalRequest**](SavepointDisposalRequest.md)|  | [optional]

### Return type

[**TriggerResponse**](TriggerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **savepoint_disposal_triggerid_get**
> AsynchronousOperationResult savepoint_disposal_triggerid_get(triggerid)



Returns the status of a savepoint disposal operation.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.asynchronous_operation_result import AsynchronousOperationResult
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    triggerid = TriggerId("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string that identifies an asynchronous operation trigger ID. The ID was returned then the operation was triggered.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.savepoint_disposal_triggerid_get(triggerid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->savepoint_disposal_triggerid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **triggerid** | **str**| 32-character hexadecimal string that identifies an asynchronous operation trigger ID. The ID was returned then the operation was triggered. |

### Return type

[**AsynchronousOperationResult**](AsynchronousOperationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **taskmanagers_get**
> TaskManagersInfo taskmanagers_get()



Returns an overview over all task managers.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.task_managers_info import TaskManagersInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.taskmanagers_get()
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->taskmanagers_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TaskManagersInfo**](TaskManagersInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **taskmanagers_metrics_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} taskmanagers_metrics_get()



Provides access to aggregated task manager metrics.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    get = "get_example" # str | Comma-separated list of string values to select specific metrics. (optional)
    agg = "MIN" # str | Comma-separated list of aggregation modes which should be calculated. Available aggregations are: \"min, max, sum, avg\". (optional)
    taskmanagers = ResourceID("bf325375e030fccba00917317c574773") # str | Comma-separated list of 32-character hexadecimal strings to select specific task managers. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.taskmanagers_metrics_get(get=get, agg=agg, taskmanagers=taskmanagers)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->taskmanagers_metrics_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get** | **str**| Comma-separated list of string values to select specific metrics. | [optional]
 **agg** | **str**| Comma-separated list of aggregation modes which should be calculated. Available aggregations are: \&quot;min, max, sum, avg\&quot;. | [optional]
 **taskmanagers** | **str**| Comma-separated list of 32-character hexadecimal strings to select specific task managers. | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **taskmanagers_taskmanagerid_get**
> TaskManagerDetailsInfo taskmanagers_taskmanagerid_get(taskmanagerid)



Returns details for a task manager. \"metrics.memorySegmentsAvailable\" and \"metrics.memorySegmentsTotal\" are deprecated. Please use \"metrics.nettyShuffleMemorySegmentsAvailable\" and \"metrics.nettyShuffleMemorySegmentsTotal\" instead.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.task_manager_details_info import TaskManagerDetailsInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    taskmanagerid = ResourceID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string that identifies a task manager.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.taskmanagers_taskmanagerid_get(taskmanagerid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->taskmanagers_taskmanagerid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taskmanagerid** | **str**| 32-character hexadecimal string that identifies a task manager. |

### Return type

[**TaskManagerDetailsInfo**](TaskManagerDetailsInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **taskmanagers_taskmanagerid_logs_get**
> LogListInfo taskmanagers_taskmanagerid_logs_get(taskmanagerid)



Returns the list of log files on a TaskManager.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.log_list_info import LogListInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    taskmanagerid = ResourceID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string that identifies a task manager.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.taskmanagers_taskmanagerid_logs_get(taskmanagerid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->taskmanagers_taskmanagerid_logs_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taskmanagerid** | **str**| 32-character hexadecimal string that identifies a task manager. |

### Return type

[**LogListInfo**](LogListInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **taskmanagers_taskmanagerid_metrics_get**
> MetricCollectionResponseBody taskmanagers_taskmanagerid_metrics_get(taskmanagerid)



Provides access to task manager metrics.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.metric_collection_response_body import MetricCollectionResponseBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    taskmanagerid = ResourceID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string that identifies a task manager.
    get = "get_example" # str | Comma-separated list of string values to select specific metrics. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.taskmanagers_taskmanagerid_metrics_get(taskmanagerid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->taskmanagers_taskmanagerid_metrics_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.taskmanagers_taskmanagerid_metrics_get(taskmanagerid, get=get)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->taskmanagers_taskmanagerid_metrics_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taskmanagerid** | **str**| 32-character hexadecimal string that identifies a task manager. |
 **get** | **str**| Comma-separated list of string values to select specific metrics. | [optional]

### Return type

[**MetricCollectionResponseBody**](MetricCollectionResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **taskmanagers_taskmanagerid_thread_dump_get**
> ThreadDumpInfo taskmanagers_taskmanagerid_thread_dump_get(taskmanagerid)



Returns the thread dump of the requested TaskManager.

### Example


```python
import time
import flink_client
from flink_client.api import default_api
from flink_client.model.thread_dump_info import ThreadDumpInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flink_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flink_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    taskmanagerid = ResourceID("bf325375e030fccba00917317c574773") # str | 32-character hexadecimal string that identifies a task manager.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.taskmanagers_taskmanagerid_thread_dump_get(taskmanagerid)
        pprint(api_response)
    except flink_client.ApiException as e:
        print("Exception when calling DefaultApi->taskmanagers_taskmanagerid_thread_dump_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taskmanagerid** | **str**| 32-character hexadecimal string that identifies a task manager. |

### Return type

[**ThreadDumpInfo**](ThreadDumpInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

