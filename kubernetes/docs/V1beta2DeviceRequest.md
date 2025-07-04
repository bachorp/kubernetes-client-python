# V1beta2DeviceRequest

DeviceRequest is a request for devices required for a claim. This is typically a request for a single resource like a device, but can also ask for several identical devices. With FirstAvailable it is also possible to provide a prioritized list of requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exactly** | [**V1beta2ExactDeviceRequest**](V1beta2ExactDeviceRequest.md) |  | [optional] 
**first_available** | [**List[V1beta2DeviceSubRequest]**](V1beta2DeviceSubRequest.md) | FirstAvailable contains subrequests, of which exactly one will be selected by the scheduler. It tries to satisfy them in the order in which they are listed here. So if there are two entries in the list, the scheduler will only check the second one if it determines that the first one can not be used.  DRA does not yet implement scoring, so the scheduler will select the first set of devices that satisfies all the requests in the claim. And if the requirements can be satisfied on more than one node, other scheduling features will determine which node is chosen. This means that the set of devices allocated to a claim might not be the optimal set available to the cluster. Scoring will be implemented later. | [optional] 
**name** | **str** | Name can be used to reference this request in a pod.spec.containers[].resources.claims entry and in a constraint of the claim.  References using the name in the DeviceRequest will uniquely identify a request when the Exactly field is set. When the FirstAvailable field is set, a reference to the name of the DeviceRequest will match whatever subrequest is chosen by the scheduler.  Must be a DNS label. | 

## Example

```python
from kubernetes.client.models.v1beta2_device_request import V1beta2DeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2DeviceRequest from a JSON string
v1beta2_device_request_instance = V1beta2DeviceRequest.from_json(json)
# print the JSON string representation of the object
print(V1beta2DeviceRequest.to_json())

# convert the object into a dict
v1beta2_device_request_dict = v1beta2_device_request_instance.to_dict()
# create an instance of V1beta2DeviceRequest from a dict
v1beta2_device_request_from_dict = V1beta2DeviceRequest.from_dict(v1beta2_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


