# V1beta1IPAddress

IPAddress represents a single IP of a single IP Family. The object is designed to be used by APIs that operate on IP addresses. The object is used by the Service core API for allocation of IP addresses. An IP address can be represented in different formats, to guarantee the uniqueness of the IP, the name of the object is the IP address in canonical format, four decimal digits separated by dots suppressing leading zeros for IPv4 and the representation defined by RFC 5952 for IPv6. Valid: 192.168.1.5 or 2001:db8::1 or 2001:db8:aaaa:bbbb:cccc:dddd:eeee:1 Invalid: 10.01.2.3 or 2001:db8:0:0:0::1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1beta1IPAddressSpec**](V1beta1IPAddressSpec.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1beta1_ip_address import V1beta1IPAddress

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1IPAddress from a JSON string
v1beta1_ip_address_instance = V1beta1IPAddress.from_json(json)
# print the JSON string representation of the object
print(V1beta1IPAddress.to_json())

# convert the object into a dict
v1beta1_ip_address_dict = v1beta1_ip_address_instance.to_dict()
# create an instance of V1beta1IPAddress from a dict
v1beta1_ip_address_from_dict = V1beta1IPAddress.from_dict(v1beta1_ip_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


