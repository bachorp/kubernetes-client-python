# V1SecretProjection

Adapts a secret into a projected volume.  The contents of the target Secret's Data field will be presented in a projected volume as files using the keys in the Data field as the file names. Note that this is identical to a secret volume source without the default mode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[V1KeyToPath]**](V1KeyToPath.md) | items if unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the &#39;..&#39; path or start with &#39;..&#39;. | [optional] 
**name** | **str** | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | [optional] 
**optional** | **bool** | optional field specify whether the Secret or its key must be defined | [optional] 

## Example

```python
from kubernetes.client.models.v1_secret_projection import V1SecretProjection

# TODO update the JSON string below
json = "{}"
# create an instance of V1SecretProjection from a JSON string
v1_secret_projection_instance = V1SecretProjection.from_json(json)
# print the JSON string representation of the object
print(V1SecretProjection.to_json())

# convert the object into a dict
v1_secret_projection_dict = v1_secret_projection_instance.to_dict()
# create an instance of V1SecretProjection from a dict
v1_secret_projection_from_dict = V1SecretProjection.from_dict(v1_secret_projection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


