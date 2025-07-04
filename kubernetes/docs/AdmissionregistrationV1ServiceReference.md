# AdmissionregistrationV1ServiceReference

ServiceReference holds a reference to Service.legacy.k8s.io

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | &#x60;name&#x60; is the name of the service. Required | 
**namespace** | **str** | &#x60;namespace&#x60; is the namespace of the service. Required | 
**path** | **str** | &#x60;path&#x60; is an optional URL path which will be sent in any request to this service. | [optional] 
**port** | **int** | If specified, the port on the service that hosting webhook. Default to 443 for backward compatibility. &#x60;port&#x60; should be a valid port number (1-65535, inclusive). | [optional] 

## Example

```python
from kubernetes.client.models.admissionregistration_v1_service_reference import AdmissionregistrationV1ServiceReference

# TODO update the JSON string below
json = "{}"
# create an instance of AdmissionregistrationV1ServiceReference from a JSON string
admissionregistration_v1_service_reference_instance = AdmissionregistrationV1ServiceReference.from_json(json)
# print the JSON string representation of the object
print(AdmissionregistrationV1ServiceReference.to_json())

# convert the object into a dict
admissionregistration_v1_service_reference_dict = admissionregistration_v1_service_reference_instance.to_dict()
# create an instance of AdmissionregistrationV1ServiceReference from a dict
admissionregistration_v1_service_reference_from_dict = AdmissionregistrationV1ServiceReference.from_dict(admissionregistration_v1_service_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


