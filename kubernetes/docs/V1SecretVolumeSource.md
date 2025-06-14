# V1SecretVolumeSource

Adapts a Secret into a volume.  The contents of the target Secret's Data field will be presented in a volume as files using the keys in the Data field as the file names. Secret volumes support ownership management and SELinux relabeling.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_mode** | **int** | defaultMode is Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. | [optional] 
**items** | [**List[V1KeyToPath]**](V1KeyToPath.md) | items If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the &#39;..&#39; path or start with &#39;..&#39;. | [optional] 
**optional** | **bool** | optional field specify whether the Secret or its keys must be defined | [optional] 
**secret_name** | **str** | secretName is the name of the secret in the pod&#39;s namespace to use. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret | [optional] 

## Example

```python
from kubernetes.client.models.v1_secret_volume_source import V1SecretVolumeSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1SecretVolumeSource from a JSON string
v1_secret_volume_source_instance = V1SecretVolumeSource.from_json(json)
# print the JSON string representation of the object
print(V1SecretVolumeSource.to_json())

# convert the object into a dict
v1_secret_volume_source_dict = v1_secret_volume_source_instance.to_dict()
# create an instance of V1SecretVolumeSource from a dict
v1_secret_volume_source_from_dict = V1SecretVolumeSource.from_dict(v1_secret_volume_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


