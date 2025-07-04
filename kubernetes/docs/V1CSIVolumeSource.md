# V1CSIVolumeSource

Represents a source location of a volume to mount, managed by an external CSI driver

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver** | **str** | driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster. | 
**fs_type** | **str** | fsType to mount. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply. | [optional] 
**node_publish_secret_ref** | [**V1LocalObjectReference**](V1LocalObjectReference.md) |  | [optional] 
**read_only** | **bool** | readOnly specifies a read-only configuration for the volume. Defaults to false (read/write). | [optional] 
**volume_attributes** | **Dict[str, str]** | volumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver&#39;s documentation for supported values. | [optional] 

## Example

```python
from kubernetes.client.models.v1_csi_volume_source import V1CSIVolumeSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1CSIVolumeSource from a JSON string
v1_csi_volume_source_instance = V1CSIVolumeSource.from_json(json)
# print the JSON string representation of the object
print(V1CSIVolumeSource.to_json())

# convert the object into a dict
v1_csi_volume_source_dict = v1_csi_volume_source_instance.to_dict()
# create an instance of V1CSIVolumeSource from a dict
v1_csi_volume_source_from_dict = V1CSIVolumeSource.from_dict(v1_csi_volume_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


