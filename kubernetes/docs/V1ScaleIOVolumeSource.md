# V1ScaleIOVolumeSource

ScaleIOVolumeSource represents a persistent ScaleIO volume

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_type** | **str** | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Default is \&quot;xfs\&quot;. | [optional] 
**gateway** | **str** | gateway is the host address of the ScaleIO API Gateway. | 
**protection_domain** | **str** | protectionDomain is the name of the ScaleIO Protection Domain for the configured storage. | [optional] 
**read_only** | **bool** | readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. | [optional] 
**secret_ref** | [**V1LocalObjectReference**](V1LocalObjectReference.md) |  | 
**ssl_enabled** | **bool** | sslEnabled Flag enable/disable SSL communication with Gateway, default false | [optional] 
**storage_mode** | **str** | storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned. | [optional] 
**storage_pool** | **str** | storagePool is the ScaleIO Storage Pool associated with the protection domain. | [optional] 
**system** | **str** | system is the name of the storage system as configured in ScaleIO. | 
**volume_name** | **str** | volumeName is the name of a volume already created in the ScaleIO system that is associated with this volume source. | [optional] 

## Example

```python
from kubernetes.client.models.v1_scale_io_volume_source import V1ScaleIOVolumeSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1ScaleIOVolumeSource from a JSON string
v1_scale_io_volume_source_instance = V1ScaleIOVolumeSource.from_json(json)
# print the JSON string representation of the object
print(V1ScaleIOVolumeSource.to_json())

# convert the object into a dict
v1_scale_io_volume_source_dict = v1_scale_io_volume_source_instance.to_dict()
# create an instance of V1ScaleIOVolumeSource from a dict
v1_scale_io_volume_source_from_dict = V1ScaleIOVolumeSource.from_dict(v1_scale_io_volume_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


