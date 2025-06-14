# V1TypedObjectReference

TypedObjectReference contains enough information to let you locate the typed referenced object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_group** | **str** | APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. | [optional] 
**kind** | **str** | Kind is the type of resource being referenced | 
**name** | **str** | Name is the name of resource being referenced | 
**namespace** | **str** | Namespace is the namespace of resource being referenced Note that when a namespace is specified, a gateway.networking.k8s.io/ReferenceGrant object is required in the referent namespace to allow that namespace&#39;s owner to accept the reference. See the ReferenceGrant documentation for details. (Alpha) This field requires the CrossNamespaceVolumeDataSource feature gate to be enabled. | [optional] 

## Example

```python
from kubernetes.client.models.v1_typed_object_reference import V1TypedObjectReference

# TODO update the JSON string below
json = "{}"
# create an instance of V1TypedObjectReference from a JSON string
v1_typed_object_reference_instance = V1TypedObjectReference.from_json(json)
# print the JSON string representation of the object
print(V1TypedObjectReference.to_json())

# convert the object into a dict
v1_typed_object_reference_dict = v1_typed_object_reference_instance.to_dict()
# create an instance of V1TypedObjectReference from a dict
v1_typed_object_reference_from_dict = V1TypedObjectReference.from_dict(v1_typed_object_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


