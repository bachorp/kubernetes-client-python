# V1Probe

Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_exec** | [**V1ExecAction**](V1ExecAction.md) |  | [optional] 
**failure_threshold** | **int** | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. | [optional] 
**grpc** | [**V1GRPCAction**](V1GRPCAction.md) |  | [optional] 
**http_get** | [**V1HTTPGetAction**](V1HTTPGetAction.md) |  | [optional] 
**initial_delay_seconds** | **int** | Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes | [optional] 
**period_seconds** | **int** | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. | [optional] 
**success_threshold** | **int** | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. | [optional] 
**tcp_socket** | [**V1TCPSocketAction**](V1TCPSocketAction.md) |  | [optional] 
**termination_grace_period_seconds** | **int** | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod&#39;s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. | [optional] 
**timeout_seconds** | **int** | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes | [optional] 

## Example

```python
from kubernetes.client.models.v1_probe import V1Probe

# TODO update the JSON string below
json = "{}"
# create an instance of V1Probe from a JSON string
v1_probe_instance = V1Probe.from_json(json)
# print the JSON string representation of the object
print(V1Probe.to_json())

# convert the object into a dict
v1_probe_dict = v1_probe_instance.to_dict()
# create an instance of V1Probe from a dict
v1_probe_from_dict = V1Probe.from_dict(v1_probe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


