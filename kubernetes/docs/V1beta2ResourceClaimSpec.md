# V1beta2ResourceClaimSpec

ResourceClaimSpec defines what is being requested in a ResourceClaim and how to configure it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**V1beta2DeviceClaim**](V1beta2DeviceClaim.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1beta2_resource_claim_spec import V1beta2ResourceClaimSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2ResourceClaimSpec from a JSON string
v1beta2_resource_claim_spec_instance = V1beta2ResourceClaimSpec.from_json(json)
# print the JSON string representation of the object
print(V1beta2ResourceClaimSpec.to_json())

# convert the object into a dict
v1beta2_resource_claim_spec_dict = v1beta2_resource_claim_spec_instance.to_dict()
# create an instance of V1beta2ResourceClaimSpec from a dict
v1beta2_resource_claim_spec_from_dict = V1beta2ResourceClaimSpec.from_dict(v1beta2_resource_claim_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


