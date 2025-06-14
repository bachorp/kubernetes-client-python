# V1EndpointAddress

EndpointAddress is a tuple that describes single IP address. Deprecated: This API is deprecated in v1.33+.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | The Hostname of this endpoint | [optional] 
**ip** | **str** | The IP of this endpoint. May not be loopback (127.0.0.0/8 or ::1), link-local (169.254.0.0/16 or fe80::/10), or link-local multicast (224.0.0.0/24 or ff02::/16). | 
**node_name** | **str** | Optional: Node hosting this endpoint. This can be used to determine endpoints local to a node. | [optional] 
**target_ref** | [**V1ObjectReference**](V1ObjectReference.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_endpoint_address import V1EndpointAddress

# TODO update the JSON string below
json = "{}"
# create an instance of V1EndpointAddress from a JSON string
v1_endpoint_address_instance = V1EndpointAddress.from_json(json)
# print the JSON string representation of the object
print(V1EndpointAddress.to_json())

# convert the object into a dict
v1_endpoint_address_dict = v1_endpoint_address_instance.to_dict()
# create an instance of V1EndpointAddress from a dict
v1_endpoint_address_from_dict = V1EndpointAddress.from_dict(v1_endpoint_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


