# V1GlusterfsPersistentVolumeSource

Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support ownership management or SELinux relabeling.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoints** | **str** | endpoints is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod | 
**endpoints_namespace** | **str** | endpointsNamespace is the namespace that contains Glusterfs endpoint. If this field is empty, the EndpointNamespace defaults to the same namespace as the bound PVC. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod | [optional] 
**path** | **str** | path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod | 
**read_only** | **bool** | readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod | [optional] 

## Example

```python
from kubernetes.client.models.v1_glusterfs_persistent_volume_source import V1GlusterfsPersistentVolumeSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlusterfsPersistentVolumeSource from a JSON string
v1_glusterfs_persistent_volume_source_instance = V1GlusterfsPersistentVolumeSource.from_json(json)
# print the JSON string representation of the object
print(V1GlusterfsPersistentVolumeSource.to_json())

# convert the object into a dict
v1_glusterfs_persistent_volume_source_dict = v1_glusterfs_persistent_volume_source_instance.to_dict()
# create an instance of V1GlusterfsPersistentVolumeSource from a dict
v1_glusterfs_persistent_volume_source_from_dict = V1GlusterfsPersistentVolumeSource.from_dict(v1_glusterfs_persistent_volume_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


