# V1beta1ServiceCIDR

ServiceCIDR defines a range of IP addresses using CIDR format (e.g. 192.168.0.0/24 or 2001:db2::/64). This range is used to allocate ClusterIPs to Service objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1beta1ServiceCIDRSpec**](V1beta1ServiceCIDRSpec.md) |  | [optional] 
**status** | [**V1beta1ServiceCIDRStatus**](V1beta1ServiceCIDRStatus.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1beta1_service_cidr import V1beta1ServiceCIDR

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1ServiceCIDR from a JSON string
v1beta1_service_cidr_instance = V1beta1ServiceCIDR.from_json(json)
# print the JSON string representation of the object
print(V1beta1ServiceCIDR.to_json())

# convert the object into a dict
v1beta1_service_cidr_dict = v1beta1_service_cidr_instance.to_dict()
# create an instance of V1beta1ServiceCIDR from a dict
v1beta1_service_cidr_from_dict = V1beta1ServiceCIDR.from_dict(v1beta1_service_cidr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


