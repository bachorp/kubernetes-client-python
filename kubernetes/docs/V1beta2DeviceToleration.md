# V1beta2DeviceToleration

The ResourceClaim this DeviceToleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect** | **str** | Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule and NoExecute. | [optional] 
**key** | **str** | Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. Must be a label name. | [optional] 
**operator** | **str** | Operator represents a key&#39;s relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a ResourceClaim can tolerate all taints of a particular category. | [optional] 
**toleration_seconds** | **int** | TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. If larger than zero, the time when the pod needs to be evicted is calculated as &lt;time when taint was adedd&gt; + &lt;toleration seconds&gt;. | [optional] 
**value** | **str** | Value is the taint value the toleration matches to. If the operator is Exists, the value must be empty, otherwise just a regular string. Must be a label value. | [optional] 

## Example

```python
from kubernetes.client.models.v1beta2_device_toleration import V1beta2DeviceToleration

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2DeviceToleration from a JSON string
v1beta2_device_toleration_instance = V1beta2DeviceToleration.from_json(json)
# print the JSON string representation of the object
print(V1beta2DeviceToleration.to_json())

# convert the object into a dict
v1beta2_device_toleration_dict = v1beta2_device_toleration_instance.to_dict()
# create an instance of V1beta2DeviceToleration from a dict
v1beta2_device_toleration_from_dict = V1beta2DeviceToleration.from_dict(v1beta2_device_toleration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


