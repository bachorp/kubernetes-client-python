# V1ConfigMap

ConfigMap holds configuration data for pods to consume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**binary_data** | **Dict[str, bytearray]** | BinaryData contains the binary data. Each key must consist of alphanumeric characters, &#39;-&#39;, &#39;_&#39; or &#39;.&#39;. BinaryData can contain byte sequences that are not in the UTF-8 range. The keys stored in BinaryData must not overlap with the ones in the Data field, this is enforced during validation process. Using this field will require 1.10+ apiserver and kubelet. | [optional] 
**data** | **Dict[str, str]** | Data contains the configuration data. Each key must consist of alphanumeric characters, &#39;-&#39;, &#39;_&#39; or &#39;.&#39;. Values with non-UTF-8 byte sequences must use the BinaryData field. The keys stored in Data must not overlap with the keys in the BinaryData field, this is enforced during validation process. | [optional] 
**immutable** | **bool** | Immutable, if set to true, ensures that data stored in the ConfigMap cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil. | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_config_map import V1ConfigMap

# TODO update the JSON string below
json = "{}"
# create an instance of V1ConfigMap from a JSON string
v1_config_map_instance = V1ConfigMap.from_json(json)
# print the JSON string representation of the object
print(V1ConfigMap.to_json())

# convert the object into a dict
v1_config_map_dict = v1_config_map_instance.to_dict()
# create an instance of V1ConfigMap from a dict
v1_config_map_from_dict = V1ConfigMap.from_dict(v1_config_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


