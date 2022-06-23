# PendingCheckpointStatistics


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **str** |  | 
**id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**is_savepoint** | **bool** |  | [optional] 
**trigger_timestamp** | **int** |  | [optional] 
**latest_ack_timestamp** | **int** |  | [optional] 
**state_size** | **int** |  | [optional] 
**end_to_end_duration** | **int** |  | [optional] 
**alignment_buffered** | **int** |  | [optional] 
**processed_data** | **int** |  | [optional] 
**persisted_data** | **int** |  | [optional] 
**num_subtasks** | **int** |  | [optional] 
**num_acknowledged_subtasks** | **int** |  | [optional] 
**checkpoint_type** | **str** |  | [optional] 
**tasks** | [**{str: (TaskCheckpointStatistics,)}**](TaskCheckpointStatistics.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


