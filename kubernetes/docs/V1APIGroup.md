# V1APIGroup

APIGroup contains the name, the supported versions, and the preferred version of a group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**name** | **str** | name is the name of the group. | 
**preferred_version** | [**V1GroupVersionForDiscovery**](V1GroupVersionForDiscovery.md) |  | [optional] 
**server_address_by_client_cidrs** | [**List[V1ServerAddressByClientCIDR]**](V1ServerAddressByClientCIDR.md) | a map of kubernetes.client CIDR to server address that is serving this group. This is to help kubernetes.clients reach servers in the most network-efficient way possible. Clients can use the appropriate server address as per the CIDR that they match. In case of multiple matches, kubernetes.clients should use the longest matching CIDR. The server returns only those CIDRs that it thinks that the kubernetes.client can match. For example: the master will return an internal IP CIDR only, if the kubernetes.client reaches the server using an internal IP. Server looks at X-Forwarded-For header or X-Real-Ip header or request.RemoteAddr (in that order) to get the kubernetes.client IP. | [optional] 
**versions** | [**List[V1GroupVersionForDiscovery]**](V1GroupVersionForDiscovery.md) | versions are the versions supported in this group. | 

## Example

```python
from kubernetes.client.models.v1_api_group import V1APIGroup

# TODO update the JSON string below
json = "{}"
# create an instance of V1APIGroup from a JSON string
v1_api_group_instance = V1APIGroup.from_json(json)
# print the JSON string representation of the object
print(V1APIGroup.to_json())

# convert the object into a dict
v1_api_group_dict = v1_api_group_instance.to_dict()
# create an instance of V1APIGroup from a dict
v1_api_group_from_dict = V1APIGroup.from_dict(v1_api_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


