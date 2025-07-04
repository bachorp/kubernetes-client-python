# V1PodDisruptionBudgetStatus

PodDisruptionBudgetStatus represents information about the status of a PodDisruptionBudget. Status may trail the actual state of a system.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[V1Condition]**](V1Condition.md) | Conditions contain conditions for PDB. The disruption controller sets the DisruptionAllowed condition. The following are known values for the reason field (additional reasons could be added in the future): - SyncFailed: The controller encountered an error and wasn&#39;t able to compute               the number of allowed disruptions. Therefore no disruptions are               allowed and the status of the condition will be False. - InsufficientPods: The number of pods are either at or below the number                     required by the PodDisruptionBudget. No disruptions are                     allowed and the status of the condition will be False. - SufficientPods: There are more pods than required by the PodDisruptionBudget.                   The condition will be True, and the number of allowed                   disruptions are provided by the disruptionsAllowed property. | [optional] 
**current_healthy** | **int** | current number of healthy pods | 
**desired_healthy** | **int** | minimum desired number of healthy pods | 
**disrupted_pods** | **Dict[str, datetime]** | DisruptedPods contains information about pods whose eviction was processed by the API server eviction subresource handler but has not yet been observed by the PodDisruptionBudget controller. A pod will be in this map from the time when the API server processed the eviction request to the time when the pod is seen by PDB controller as having been marked for deletion (or after a timeout). The key in the map is the name of the pod and the value is the time when the API server processed the eviction request. If the deletion didn&#39;t occur and a pod is still there it will be removed from the list automatically by PodDisruptionBudget controller after some time. If everything goes smooth this map should be empty for the most of the time. Large number of entries in the map may indicate problems with pod deletions. | [optional] 
**disruptions_allowed** | **int** | Number of pod disruptions that are currently allowed. | 
**expected_pods** | **int** | total number of pods counted by this disruption budget | 
**observed_generation** | **int** | Most recent generation observed when updating this PDB status. DisruptionsAllowed and other status information is valid only if observedGeneration equals to PDB&#39;s object generation. | [optional] 

## Example

```python
from kubernetes.client.models.v1_pod_disruption_budget_status import V1PodDisruptionBudgetStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1PodDisruptionBudgetStatus from a JSON string
v1_pod_disruption_budget_status_instance = V1PodDisruptionBudgetStatus.from_json(json)
# print the JSON string representation of the object
print(V1PodDisruptionBudgetStatus.to_json())

# convert the object into a dict
v1_pod_disruption_budget_status_dict = v1_pod_disruption_budget_status_instance.to_dict()
# create an instance of V1PodDisruptionBudgetStatus from a dict
v1_pod_disruption_budget_status_from_dict = V1PodDisruptionBudgetStatus.from_dict(v1_pod_disruption_budget_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


