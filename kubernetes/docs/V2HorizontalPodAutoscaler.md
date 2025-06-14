# V2HorizontalPodAutoscaler

HorizontalPodAutoscaler is the configuration for a horizontal pod autoscaler, which automatically manages the replica count of any resource implementing the scale subresource based on the metrics specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V2HorizontalPodAutoscalerSpec**](V2HorizontalPodAutoscalerSpec.md) |  | [optional] 
**status** | [**V2HorizontalPodAutoscalerStatus**](V2HorizontalPodAutoscalerStatus.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v2_horizontal_pod_autoscaler import V2HorizontalPodAutoscaler

# TODO update the JSON string below
json = "{}"
# create an instance of V2HorizontalPodAutoscaler from a JSON string
v2_horizontal_pod_autoscaler_instance = V2HorizontalPodAutoscaler.from_json(json)
# print the JSON string representation of the object
print(V2HorizontalPodAutoscaler.to_json())

# convert the object into a dict
v2_horizontal_pod_autoscaler_dict = v2_horizontal_pod_autoscaler_instance.to_dict()
# create an instance of V2HorizontalPodAutoscaler from a dict
v2_horizontal_pod_autoscaler_from_dict = V2HorizontalPodAutoscaler.from_dict(v2_horizontal_pod_autoscaler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


