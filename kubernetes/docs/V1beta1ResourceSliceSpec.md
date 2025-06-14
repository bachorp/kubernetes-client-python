# V1beta1ResourceSliceSpec

ResourceSliceSpec contains the information published by the driver in one ResourceSlice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_nodes** | **bool** | AllNodes indicates that all nodes have access to the resources in the pool.  Exactly one of NodeName, NodeSelector, AllNodes, and PerDeviceNodeSelection must be set. | [optional] 
**devices** | [**List[V1beta1Device]**](V1beta1Device.md) | Devices lists some or all of the devices in this pool.  Must not have more than 128 entries. | [optional] 
**driver** | **str** | Driver identifies the DRA driver providing the capacity information. A field selector can be used to list only ResourceSlice objects with a certain driver name.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. This field is immutable. | 
**node_name** | **str** | NodeName identifies the node which provides the resources in this pool. A field selector can be used to list only ResourceSlice objects belonging to a certain node.  This field can be used to limit access from nodes to ResourceSlices with the same node name. It also indicates to autoscalers that adding new nodes of the same type as some old node might also make new resources available.  Exactly one of NodeName, NodeSelector, AllNodes, and PerDeviceNodeSelection must be set. This field is immutable. | [optional] 
**node_selector** | [**V1NodeSelector**](V1NodeSelector.md) |  | [optional] 
**per_device_node_selection** | **bool** | PerDeviceNodeSelection defines whether the access from nodes to resources in the pool is set on the ResourceSlice level or on each device. If it is set to true, every device defined the ResourceSlice must specify this individually.  Exactly one of NodeName, NodeSelector, AllNodes, and PerDeviceNodeSelection must be set. | [optional] 
**pool** | [**V1beta1ResourcePool**](V1beta1ResourcePool.md) |  | 
**shared_counters** | [**List[V1beta1CounterSet]**](V1beta1CounterSet.md) | SharedCounters defines a list of counter sets, each of which has a name and a list of counters available.  The names of the SharedCounters must be unique in the ResourceSlice.  The maximum number of SharedCounters is 32. | [optional] 

## Example

```python
from kubernetes.client.models.v1beta1_resource_slice_spec import V1beta1ResourceSliceSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1ResourceSliceSpec from a JSON string
v1beta1_resource_slice_spec_instance = V1beta1ResourceSliceSpec.from_json(json)
# print the JSON string representation of the object
print(V1beta1ResourceSliceSpec.to_json())

# convert the object into a dict
v1beta1_resource_slice_spec_dict = v1beta1_resource_slice_spec_instance.to_dict()
# create an instance of V1beta1ResourceSliceSpec from a dict
v1beta1_resource_slice_spec_from_dict = V1beta1ResourceSliceSpec.from_dict(v1beta1_resource_slice_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


