# V1Toleration

The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect** | **str** | Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute. | [optional] 
**key** | **str** | Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. | [optional] 
**operator** | **str** | Operator represents a key&#39;s relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category. | [optional] 
**toleration_seconds** | **int** | TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. | [optional] 
**value** | **str** | Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string. | [optional] 

## Example

```python
from kubernetes.client.models.v1_toleration import V1Toleration

# TODO update the JSON string below
json = "{}"
# create an instance of V1Toleration from a JSON string
v1_toleration_instance = V1Toleration.from_json(json)
# print the JSON string representation of the object
print(V1Toleration.to_json())

# convert the object into a dict
v1_toleration_dict = v1_toleration_instance.to_dict()
# create an instance of V1Toleration from a dict
v1_toleration_from_dict = V1Toleration.from_dict(v1_toleration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


