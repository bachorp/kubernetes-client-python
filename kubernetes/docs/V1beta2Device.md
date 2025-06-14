# V1beta2Device

Device represents one individual hardware instance that can be selected based on its attributes. Besides the name, exactly one field must be set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_nodes** | **bool** | AllNodes indicates that all nodes have access to the device.  Must only be set if Spec.PerDeviceNodeSelection is set to true. At most one of NodeName, NodeSelector and AllNodes can be set. | [optional] 
**attributes** | [**Dict[str, V1beta2DeviceAttribute]**](V1beta2DeviceAttribute.md) | Attributes defines the set of attributes for this device. The name of each attribute must be unique in that set.  The maximum number of attributes and capacities combined is 32. | [optional] 
**capacity** | [**Dict[str, V1beta2DeviceCapacity]**](V1beta2DeviceCapacity.md) | Capacity defines the set of capacities for this device. The name of each capacity must be unique in that set.  The maximum number of attributes and capacities combined is 32. | [optional] 
**consumes_counters** | [**List[V1beta2DeviceCounterConsumption]**](V1beta2DeviceCounterConsumption.md) | ConsumesCounters defines a list of references to sharedCounters and the set of counters that the device will consume from those counter sets.  There can only be a single entry per counterSet.  The total number of device counter consumption entries must be &lt;&#x3D; 32. In addition, the total number in the entire ResourceSlice must be &lt;&#x3D; 1024 (for example, 64 devices with 16 counters each). | [optional] 
**name** | **str** | Name is unique identifier among all devices managed by the driver in the pool. It must be a DNS label. | 
**node_name** | **str** | NodeName identifies the node where the device is available.  Must only be set if Spec.PerDeviceNodeSelection is set to true. At most one of NodeName, NodeSelector and AllNodes can be set. | [optional] 
**node_selector** | [**V1NodeSelector**](V1NodeSelector.md) |  | [optional] 
**taints** | [**List[V1beta2DeviceTaint]**](V1beta2DeviceTaint.md) | If specified, these are the driver-defined taints.  The maximum number of taints is 4.  This is an alpha field and requires enabling the DRADeviceTaints feature gate. | [optional] 

## Example

```python
from kubernetes.client.models.v1beta2_device import V1beta2Device

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2Device from a JSON string
v1beta2_device_instance = V1beta2Device.from_json(json)
# print the JSON string representation of the object
print(V1beta2Device.to_json())

# convert the object into a dict
v1beta2_device_dict = v1beta2_device_instance.to_dict()
# create an instance of V1beta2Device from a dict
v1beta2_device_from_dict = V1beta2Device.from_dict(v1beta2_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


