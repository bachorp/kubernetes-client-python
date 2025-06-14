# V1StatusCause

StatusCause provides more information about an api.Status failure, including cases when multiple errors are encountered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The field of the resource that has caused this error, as named by its JSON serialization. May include dot and postfix notation for nested attributes. Arrays are zero-indexed.  Fields may appear more than once in an array of causes due to fields having multiple errors. Optional.  Examples:   \&quot;name\&quot; - the field \&quot;name\&quot; on the current resource   \&quot;items[0].name\&quot; - the field \&quot;name\&quot; on the first array entry in \&quot;items\&quot; | [optional] 
**message** | **str** | A human-readable description of the cause of the error.  This field may be presented as-is to a reader. | [optional] 
**reason** | **str** | A machine-readable description of the cause of the error. If this value is empty there is no information available. | [optional] 

## Example

```python
from kubernetes.client.models.v1_status_cause import V1StatusCause

# TODO update the JSON string below
json = "{}"
# create an instance of V1StatusCause from a JSON string
v1_status_cause_instance = V1StatusCause.from_json(json)
# print the JSON string representation of the object
print(V1StatusCause.to_json())

# convert the object into a dict
v1_status_cause_dict = v1_status_cause_instance.to_dict()
# create an instance of V1StatusCause from a dict
v1_status_cause_from_dict = V1StatusCause.from_dict(v1_status_cause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


