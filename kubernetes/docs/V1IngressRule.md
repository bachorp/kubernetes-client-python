# V1IngressRule

IngressRule represents the rules mapping the paths under a specified host to the related backend services. Incoming requests are first evaluated for a host match, then routed to the backend associated with the matching IngressRuleValue.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | host is the fully qualified domain name of a network host, as defined by RFC 3986. Note the following deviations from the \&quot;host\&quot; part of the URI as defined in RFC 3986: 1. IPs are not allowed. Currently an IngressRuleValue can only apply to    the IP in the Spec of the parent Ingress. 2. The &#x60;:&#x60; delimiter is not respected because ports are not allowed.    Currently the port of an Ingress is implicitly :80 for http and    :443 for https. Both these may change in the future. Incoming requests are matched against the host before the IngressRuleValue. If the host is unspecified, the Ingress routes all traffic based on the specified IngressRuleValue.  host can be \&quot;precise\&quot; which is a domain name without the terminating dot of a network host (e.g. \&quot;foo.bar.com\&quot;) or \&quot;wildcard\&quot;, which is a domain name prefixed with a single wildcard label (e.g. \&quot;*.foo.com\&quot;). The wildcard character &#39;*&#39; must appear by itself as the first DNS label and matches only a single label. You cannot have a wildcard label by itself (e.g. Host &#x3D;&#x3D; \&quot;*\&quot;). Requests will be matched against the Host field in the following way: 1. If host is precise, the request matches this rule if the http host header is equal to Host. 2. If host is a wildcard, then the request matches this rule if the http host header is to equal to the suffix (removing the first label) of the wildcard rule. | [optional] 
**http** | [**V1HTTPIngressRuleValue**](V1HTTPIngressRuleValue.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_ingress_rule import V1IngressRule

# TODO update the JSON string below
json = "{}"
# create an instance of V1IngressRule from a JSON string
v1_ingress_rule_instance = V1IngressRule.from_json(json)
# print the JSON string representation of the object
print(V1IngressRule.to_json())

# convert the object into a dict
v1_ingress_rule_dict = v1_ingress_rule_instance.to_dict()
# create an instance of V1IngressRule from a dict
v1_ingress_rule_from_dict = V1IngressRule.from_dict(v1_ingress_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


