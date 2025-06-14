# V1PodFailurePolicyRule

PodFailurePolicyRule describes how a pod failure is handled when the requirements are met. One of onExitCodes and onPodConditions, but not both, can be used in each rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies the action taken on a pod failure when the requirements are satisfied. Possible values are:  - FailJob: indicates that the pod&#39;s job is marked as Failed and all   running pods are terminated. - FailIndex: indicates that the pod&#39;s index is marked as Failed and will   not be restarted. - Ignore: indicates that the counter towards the .backoffLimit is not   incremented and a replacement pod is created. - Count: indicates that the pod is handled in the default way - the   counter towards the .backoffLimit is incremented. Additional values are considered to be added in the future. Clients should react to an unknown action by skipping the rule. | 
**on_exit_codes** | [**V1PodFailurePolicyOnExitCodesRequirement**](V1PodFailurePolicyOnExitCodesRequirement.md) |  | [optional] 
**on_pod_conditions** | [**List[V1PodFailurePolicyOnPodConditionsPattern]**](V1PodFailurePolicyOnPodConditionsPattern.md) | Represents the requirement on the pod conditions. The requirement is represented as a list of pod condition patterns. The requirement is satisfied if at least one pattern matches an actual pod condition. At most 20 elements are allowed. | [optional] 

## Example

```python
from kubernetes.client.models.v1_pod_failure_policy_rule import V1PodFailurePolicyRule

# TODO update the JSON string below
json = "{}"
# create an instance of V1PodFailurePolicyRule from a JSON string
v1_pod_failure_policy_rule_instance = V1PodFailurePolicyRule.from_json(json)
# print the JSON string representation of the object
print(V1PodFailurePolicyRule.to_json())

# convert the object into a dict
v1_pod_failure_policy_rule_dict = v1_pod_failure_policy_rule_instance.to_dict()
# create an instance of V1PodFailurePolicyRule from a dict
v1_pod_failure_policy_rule_from_dict = V1PodFailurePolicyRule.from_dict(v1_pod_failure_policy_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


