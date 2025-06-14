# V1LocalSubjectAccessReview

LocalSubjectAccessReview checks whether or not a user or group can perform an action in a given namespace. Having a namespace scoped resource makes it much easier to grant namespace scoped policy that includes permissions checking.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1SubjectAccessReviewSpec**](V1SubjectAccessReviewSpec.md) |  | 
**status** | [**V1SubjectAccessReviewStatus**](V1SubjectAccessReviewStatus.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_local_subject_access_review import V1LocalSubjectAccessReview

# TODO update the JSON string below
json = "{}"
# create an instance of V1LocalSubjectAccessReview from a JSON string
v1_local_subject_access_review_instance = V1LocalSubjectAccessReview.from_json(json)
# print the JSON string representation of the object
print(V1LocalSubjectAccessReview.to_json())

# convert the object into a dict
v1_local_subject_access_review_dict = v1_local_subject_access_review_instance.to_dict()
# create an instance of V1LocalSubjectAccessReview from a dict
v1_local_subject_access_review_from_dict = V1LocalSubjectAccessReview.from_dict(v1_local_subject_access_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


