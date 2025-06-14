# V1ComponentStatus

ComponentStatus (and ComponentStatusList) holds the cluster validation info. Deprecated: This API is deprecated in v1.19+

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**conditions** | [**List[V1ComponentCondition]**](V1ComponentCondition.md) | List of component conditions observed | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_component_status import V1ComponentStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1ComponentStatus from a JSON string
v1_component_status_instance = V1ComponentStatus.from_json(json)
# print the JSON string representation of the object
print(V1ComponentStatus.to_json())

# convert the object into a dict
v1_component_status_dict = v1_component_status_instance.to_dict()
# create an instance of V1ComponentStatus from a dict
v1_component_status_from_dict = V1ComponentStatus.from_dict(v1_component_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


