# V1CertificateSigningRequestCondition

CertificateSigningRequestCondition describes a condition of a CertificateSigningRequest object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transition_time** | **datetime** | lastTransitionTime is the time the condition last transitioned from one status to another. If unset, when a new condition type is added or an existing condition&#39;s status is changed, the server defaults this to the current time. | [optional] 
**last_update_time** | **datetime** | lastUpdateTime is the time of the last update to this condition | [optional] 
**message** | **str** | message contains a human readable message with details about the request state | [optional] 
**reason** | **str** | reason indicates a brief reason for the request state | [optional] 
**status** | **str** | status of the condition, one of True, False, Unknown. Approved, Denied, and Failed conditions may not be \&quot;False\&quot; or \&quot;Unknown\&quot;. | 
**type** | **str** | type of the condition. Known conditions are \&quot;Approved\&quot;, \&quot;Denied\&quot;, and \&quot;Failed\&quot;.  An \&quot;Approved\&quot; condition is added via the /approval subresource, indicating the request was approved and should be issued by the signer.  A \&quot;Denied\&quot; condition is added via the /approval subresource, indicating the request was denied and should not be issued by the signer.  A \&quot;Failed\&quot; condition is added via the /status subresource, indicating the signer failed to issue the certificate.  Approved and Denied conditions are mutually exclusive. Approved, Denied, and Failed conditions cannot be removed once added.  Only one condition of a given type is allowed. | 

## Example

```python
from kubernetes.client.models.v1_certificate_signing_request_condition import V1CertificateSigningRequestCondition

# TODO update the JSON string below
json = "{}"
# create an instance of V1CertificateSigningRequestCondition from a JSON string
v1_certificate_signing_request_condition_instance = V1CertificateSigningRequestCondition.from_json(json)
# print the JSON string representation of the object
print(V1CertificateSigningRequestCondition.to_json())

# convert the object into a dict
v1_certificate_signing_request_condition_dict = v1_certificate_signing_request_condition_instance.to_dict()
# create an instance of V1CertificateSigningRequestCondition from a dict
v1_certificate_signing_request_condition_from_dict = V1CertificateSigningRequestCondition.from_dict(v1_certificate_signing_request_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


