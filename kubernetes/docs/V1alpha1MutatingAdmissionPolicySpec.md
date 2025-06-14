# V1alpha1MutatingAdmissionPolicySpec

MutatingAdmissionPolicySpec is the specification of the desired behavior of the admission policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failure_policy** | **str** | failurePolicy defines how to handle failures for the admission policy. Failures can occur from CEL expression parse errors, type check errors, runtime errors and invalid or mis-configured policy definitions or bindings.  A policy is invalid if paramKind refers to a non-existent Kind. A binding is invalid if paramRef.name refers to a non-existent resource.  failurePolicy does not define how validations that evaluate to false are handled.  Allowed values are Ignore or Fail. Defaults to Fail. | [optional] 
**match_conditions** | [**List[V1alpha1MatchCondition]**](V1alpha1MatchCondition.md) | matchConditions is a list of conditions that must be met for a request to be validated. Match conditions filter requests that have already been matched by the matchConstraints. An empty list of matchConditions matches all requests. There are a maximum of 64 match conditions allowed.  If a parameter object is provided, it can be accessed via the &#x60;params&#x60; handle in the same manner as validation expressions.  The exact matching logic is (in order):   1. If ANY matchCondition evaluates to FALSE, the policy is skipped.   2. If ALL matchConditions evaluate to TRUE, the policy is evaluated.   3. If any matchCondition evaluates to an error (but none are FALSE):      - If failurePolicy&#x3D;Fail, reject the request      - If failurePolicy&#x3D;Ignore, the policy is skipped | [optional] 
**match_constraints** | [**V1alpha1MatchResources**](V1alpha1MatchResources.md) |  | [optional] 
**mutations** | [**List[V1alpha1Mutation]**](V1alpha1Mutation.md) | mutations contain operations to perform on matching objects. mutations may not be empty; a minimum of one mutation is required. mutations are evaluated in order, and are reinvoked according to the reinvocationPolicy. The mutations of a policy are invoked for each binding of this policy and reinvocation of mutations occurs on a per binding basis. | [optional] 
**param_kind** | [**V1alpha1ParamKind**](V1alpha1ParamKind.md) |  | [optional] 
**reinvocation_policy** | **str** | reinvocationPolicy indicates whether mutations may be called multiple times per MutatingAdmissionPolicyBinding as part of a single admission evaluation. Allowed values are \&quot;Never\&quot; and \&quot;IfNeeded\&quot;.  Never: These mutations will not be called more than once per binding in a single admission evaluation.  IfNeeded: These mutations may be invoked more than once per binding for a single admission request and there is no guarantee of order with respect to other admission plugins, admission webhooks, bindings of this policy and admission policies.  Mutations are only reinvoked when mutations change the object after this mutation is invoked. Required. | [optional] 
**variables** | [**List[V1alpha1Variable]**](V1alpha1Variable.md) | variables contain definitions of variables that can be used in composition of other expressions. Each variable is defined as a named CEL expression. The variables defined here will be available under &#x60;variables&#x60; in other expressions of the policy except matchConditions because matchConditions are evaluated before the rest of the policy.  The expression of a variable can refer to other variables defined earlier in the list but not those after. Thus, variables must be sorted by the order of first appearance and acyclic. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha1_mutating_admission_policy_spec import V1alpha1MutatingAdmissionPolicySpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1MutatingAdmissionPolicySpec from a JSON string
v1alpha1_mutating_admission_policy_spec_instance = V1alpha1MutatingAdmissionPolicySpec.from_json(json)
# print the JSON string representation of the object
print(V1alpha1MutatingAdmissionPolicySpec.to_json())

# convert the object into a dict
v1alpha1_mutating_admission_policy_spec_dict = v1alpha1_mutating_admission_policy_spec_instance.to_dict()
# create an instance of V1alpha1MutatingAdmissionPolicySpec from a dict
v1alpha1_mutating_admission_policy_spec_from_dict = V1alpha1MutatingAdmissionPolicySpec.from_dict(v1alpha1_mutating_admission_policy_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


