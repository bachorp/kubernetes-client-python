# V1LimitedPriorityLevelConfiguration

LimitedPriorityLevelConfiguration specifies how to handle requests that are subject to limits. It addresses two issues:   - How are requests for this priority level limited?   - What should be done with requests that exceed the limit?

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**borrowing_limit_percent** | **int** | &#x60;borrowingLimitPercent&#x60;, if present, configures a limit on how many seats this priority level can borrow from other priority levels. The limit is known as this level&#39;s BorrowingConcurrencyLimit (BorrowingCL) and is a limit on the total number of seats that this level may borrow at any one time. This field holds the ratio of that limit to the level&#39;s nominal concurrency limit. When this field is non-nil, it must hold a non-negative integer and the limit is calculated as follows.  BorrowingCL(i) &#x3D; round( NominalCL(i) * borrowingLimitPercent(i)/100.0 )  The value of this field can be more than 100, implying that this priority level can borrow a number of seats that is greater than its own nominal concurrency limit (NominalCL). When this field is left &#x60;nil&#x60;, the limit is effectively infinite. | [optional] 
**lendable_percent** | **int** | &#x60;lendablePercent&#x60; prescribes the fraction of the level&#39;s NominalCL that can be borrowed by other priority levels. The value of this field must be between 0 and 100, inclusive, and it defaults to 0. The number of seats that other levels can borrow from this level, known as this level&#39;s LendableConcurrencyLimit (LendableCL), is defined as follows.  LendableCL(i) &#x3D; round( NominalCL(i) * lendablePercent(i)/100.0 ) | [optional] 
**limit_response** | [**V1LimitResponse**](V1LimitResponse.md) |  | [optional] 
**nominal_concurrency_shares** | **int** | &#x60;nominalConcurrencyShares&#x60; (NCS) contributes to the computation of the NominalConcurrencyLimit (NominalCL) of this level. This is the number of execution seats available at this priority level. This is used both for requests dispatched from this priority level as well as requests dispatched from other priority levels borrowing seats from this level. The server&#39;s concurrency limit (ServerCL) is divided among the Limited priority levels in proportion to their NCS values:  NominalCL(i)  &#x3D; ceil( ServerCL * NCS(i) / sum_ncs ) sum_ncs &#x3D; sum[priority level k] NCS(k)  Bigger numbers mean a larger nominal concurrency limit, at the expense of every other priority level.  If not specified, this field defaults to a value of 30.  Setting this field to zero supports the construction of a \&quot;jail\&quot; for this priority level that is used to hold some request(s) | [optional] 

## Example

```python
from kubernetes.client.models.v1_limited_priority_level_configuration import V1LimitedPriorityLevelConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of V1LimitedPriorityLevelConfiguration from a JSON string
v1_limited_priority_level_configuration_instance = V1LimitedPriorityLevelConfiguration.from_json(json)
# print the JSON string representation of the object
print(V1LimitedPriorityLevelConfiguration.to_json())

# convert the object into a dict
v1_limited_priority_level_configuration_dict = v1_limited_priority_level_configuration_instance.to_dict()
# create an instance of V1LimitedPriorityLevelConfiguration from a dict
v1_limited_priority_level_configuration_from_dict = V1LimitedPriorityLevelConfiguration.from_dict(v1_limited_priority_level_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


