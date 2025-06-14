# V1PersistentVolumeClaimStatus

PersistentVolumeClaimStatus is the current status of a persistent volume claim.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_modes** | **List[str]** | accessModes contains the actual access modes the volume backing the PVC has. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1 | [optional] 
**allocated_resource_statuses** | **Dict[str, str]** | allocatedResourceStatuses stores status of resource being resized for the given PVC. Key names follow standard Kubernetes label syntax. Valid values are either:  * Un-prefixed keys:   - storage - the capacity of the volume.  * Custom resources must use implementation-defined prefixed names such as \&quot;example.com/my-custom-resource\&quot; Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.  ClaimResourceStatus can be in any of following states:  - ControllerResizeInProgress:   State set when resize controller starts resizing the volume in control-plane.  - ControllerResizeFailed:   State set when resize has failed in resize controller with a terminal error.  - NodeResizePending:   State set when resize controller has finished resizing the volume but further resizing of   volume is needed on the node.  - NodeResizeInProgress:   State set when kubelet starts resizing the volume.  - NodeResizeFailed:   State set when resizing has failed in kubelet with a terminal error. Transient errors don&#39;t set   NodeResizeFailed. For example: if expanding a PVC for more capacity - this field can be one of the following states:  - pvc.status.allocatedResourceStatus[&#39;storage&#39;] &#x3D; \&quot;ControllerResizeInProgress\&quot;      - pvc.status.allocatedResourceStatus[&#39;storage&#39;] &#x3D; \&quot;ControllerResizeFailed\&quot;      - pvc.status.allocatedResourceStatus[&#39;storage&#39;] &#x3D; \&quot;NodeResizePending\&quot;      - pvc.status.allocatedResourceStatus[&#39;storage&#39;] &#x3D; \&quot;NodeResizeInProgress\&quot;      - pvc.status.allocatedResourceStatus[&#39;storage&#39;] &#x3D; \&quot;NodeResizeFailed\&quot; When this field is not set, it means that no resize operation is in progress for the given PVC.  A controller that receives PVC update with previously unknown resourceName or ClaimResourceStatus should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.  This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature. | [optional] 
**allocated_resources** | **Dict[str, str]** | allocatedResources tracks the resources allocated to a PVC including its capacity. Key names follow standard Kubernetes label syntax. Valid values are either:  * Un-prefixed keys:   - storage - the capacity of the volume.  * Custom resources must use implementation-defined prefixed names such as \&quot;example.com/my-custom-resource\&quot; Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.  Capacity reported here may be larger than the actual capacity when a volume expansion operation is requested. For storage quota, the larger value from allocatedResources and PVC.spec.resources is used. If allocatedResources is not set, PVC.spec.resources alone is used for quota calculation. If a volume expansion capacity request is lowered, allocatedResources is only lowered if there are no expansion operations in progress and if the actual volume capacity is equal or lower than the requested capacity.  A controller that receives PVC update with previously unknown resourceName should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.  This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature. | [optional] 
**capacity** | **Dict[str, str]** | capacity represents the actual resources of the underlying volume. | [optional] 
**conditions** | [**List[V1PersistentVolumeClaimCondition]**](V1PersistentVolumeClaimCondition.md) | conditions is the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to &#39;Resizing&#39;. | [optional] 
**current_volume_attributes_class_name** | **str** | currentVolumeAttributesClassName is the current name of the VolumeAttributesClass the PVC is using. When unset, there is no VolumeAttributeClass applied to this PersistentVolumeClaim This is a beta field and requires enabling VolumeAttributesClass feature (off by default). | [optional] 
**modify_volume_status** | [**V1ModifyVolumeStatus**](V1ModifyVolumeStatus.md) |  | [optional] 
**phase** | **str** | phase represents the current phase of PersistentVolumeClaim. | [optional] 

## Example

```python
from kubernetes.client.models.v1_persistent_volume_claim_status import V1PersistentVolumeClaimStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1PersistentVolumeClaimStatus from a JSON string
v1_persistent_volume_claim_status_instance = V1PersistentVolumeClaimStatus.from_json(json)
# print the JSON string representation of the object
print(V1PersistentVolumeClaimStatus.to_json())

# convert the object into a dict
v1_persistent_volume_claim_status_dict = v1_persistent_volume_claim_status_instance.to_dict()
# create an instance of V1PersistentVolumeClaimStatus from a dict
v1_persistent_volume_claim_status_from_dict = V1PersistentVolumeClaimStatus.from_dict(v1_persistent_volume_claim_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


