# V1ProjectedVolumeSource

Represents a projected volume source

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_mode** | **int** | defaultMode are the mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. | [optional] 
**sources** | [**List[V1VolumeProjection]**](V1VolumeProjection.md) | sources is the list of volume projections. Each entry in this list handles one source. | [optional] 

## Example

```python
from kubernetes.client.models.v1_projected_volume_source import V1ProjectedVolumeSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1ProjectedVolumeSource from a JSON string
v1_projected_volume_source_instance = V1ProjectedVolumeSource.from_json(json)
# print the JSON string representation of the object
print(V1ProjectedVolumeSource.to_json())

# convert the object into a dict
v1_projected_volume_source_dict = v1_projected_volume_source_instance.to_dict()
# create an instance of V1ProjectedVolumeSource from a dict
v1_projected_volume_source_from_dict = V1ProjectedVolumeSource.from_dict(v1_projected_volume_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


