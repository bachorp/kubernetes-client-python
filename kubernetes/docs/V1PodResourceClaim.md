# V1PodResourceClaim

PodResourceClaim references exactly one ResourceClaim, either directly or by naming a ResourceClaimTemplate which is then turned into a ResourceClaim for the pod.  It adds a name to it that uniquely identifies the ResourceClaim inside the Pod. Containers that need access to the ResourceClaim reference it with this name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name uniquely identifies this resource claim inside the pod. This must be a DNS_LABEL. | 
**resource_claim_name** | **str** | ResourceClaimName is the name of a ResourceClaim object in the same namespace as this pod.  Exactly one of ResourceClaimName and ResourceClaimTemplateName must be set. | [optional] 
**resource_claim_template_name** | **str** | ResourceClaimTemplateName is the name of a ResourceClaimTemplate object in the same namespace as this pod.  The template will be used to create a new ResourceClaim, which will be bound to this pod. When this pod is deleted, the ResourceClaim will also be deleted. The pod name and resource name, along with a generated component, will be used to form a unique name for the ResourceClaim, which will be recorded in pod.status.resourceClaimStatuses.  This field is immutable and no changes will be made to the corresponding ResourceClaim by the control plane after creating the ResourceClaim.  Exactly one of ResourceClaimName and ResourceClaimTemplateName must be set. | [optional] 

## Example

```python
from kubernetes.client.models.v1_pod_resource_claim import V1PodResourceClaim

# TODO update the JSON string below
json = "{}"
# create an instance of V1PodResourceClaim from a JSON string
v1_pod_resource_claim_instance = V1PodResourceClaim.from_json(json)
# print the JSON string representation of the object
print(V1PodResourceClaim.to_json())

# convert the object into a dict
v1_pod_resource_claim_dict = v1_pod_resource_claim_instance.to_dict()
# create an instance of V1PodResourceClaim from a dict
v1_pod_resource_claim_from_dict = V1PodResourceClaim.from_dict(v1_pod_resource_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


