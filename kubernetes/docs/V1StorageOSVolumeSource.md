# V1StorageOSVolumeSource

Represents a StorageOS persistent volume resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_type** | **str** | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. | [optional] 
**read_only** | **bool** | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. | [optional] 
**secret_ref** | [**V1LocalObjectReference**](V1LocalObjectReference.md) |  | [optional] 
**volume_name** | **str** | volumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace. | [optional] 
**volume_namespace** | **str** | volumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod&#39;s namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to \&quot;default\&quot; if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created. | [optional] 

## Example

```python
from kubernetes.client.models.v1_storage_os_volume_source import V1StorageOSVolumeSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1StorageOSVolumeSource from a JSON string
v1_storage_os_volume_source_instance = V1StorageOSVolumeSource.from_json(json)
# print the JSON string representation of the object
print(V1StorageOSVolumeSource.to_json())

# convert the object into a dict
v1_storage_os_volume_source_dict = v1_storage_os_volume_source_instance.to_dict()
# create an instance of V1StorageOSVolumeSource from a dict
v1_storage_os_volume_source_from_dict = V1StorageOSVolumeSource.from_dict(v1_storage_os_volume_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


