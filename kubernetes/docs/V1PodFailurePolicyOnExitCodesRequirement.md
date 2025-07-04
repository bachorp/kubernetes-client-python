# V1PodFailurePolicyOnExitCodesRequirement

PodFailurePolicyOnExitCodesRequirement describes the requirement for handling a failed pod based on its container exit codes. In particular, it lookups the .state.terminated.exitCode for each app container and init container status, represented by the .status.containerStatuses and .status.initContainerStatuses fields in the Pod status, respectively. Containers completed with success (exit code 0) are excluded from the requirement check.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_name** | **str** | Restricts the check for exit codes to the container with the specified name. When null, the rule applies to all containers. When specified, it should match one the container or initContainer names in the pod template. | [optional] 
**operator** | **str** | Represents the relationship between the container exit code(s) and the specified values. Containers completed with success (exit code 0) are excluded from the requirement check. Possible values are:  - In: the requirement is satisfied if at least one container exit code   (might be multiple if there are multiple containers not restricted   by the &#39;containerName&#39; field) is in the set of specified values. - NotIn: the requirement is satisfied if at least one container exit code   (might be multiple if there are multiple containers not restricted   by the &#39;containerName&#39; field) is not in the set of specified values. Additional values are considered to be added in the future. Clients should react to an unknown operator by assuming the requirement is not satisfied. | 
**values** | **List[int]** | Specifies the set of values. Each returned container exit code (might be multiple in case of multiple containers) is checked against this set of values with respect to the operator. The list of values must be ordered and must not contain duplicates. Value &#39;0&#39; cannot be used for the In operator. At least one element is required. At most 255 elements are allowed. | 

## Example

```python
from kubernetes.client.models.v1_pod_failure_policy_on_exit_codes_requirement import V1PodFailurePolicyOnExitCodesRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of V1PodFailurePolicyOnExitCodesRequirement from a JSON string
v1_pod_failure_policy_on_exit_codes_requirement_instance = V1PodFailurePolicyOnExitCodesRequirement.from_json(json)
# print the JSON string representation of the object
print(V1PodFailurePolicyOnExitCodesRequirement.to_json())

# convert the object into a dict
v1_pod_failure_policy_on_exit_codes_requirement_dict = v1_pod_failure_policy_on_exit_codes_requirement_instance.to_dict()
# create an instance of V1PodFailurePolicyOnExitCodesRequirement from a dict
v1_pod_failure_policy_on_exit_codes_requirement_from_dict = V1PodFailurePolicyOnExitCodesRequirement.from_dict(v1_pod_failure_policy_on_exit_codes_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


