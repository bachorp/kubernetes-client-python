# V1PersistentVolumeClaimSpec

PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_modes** | **List[str]** | accessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1 | [optional] 
**data_source** | [**V1TypedLocalObjectReference**](V1TypedLocalObjectReference.md) |  | [optional] 
**data_source_ref** | [**V1TypedObjectReference**](V1TypedObjectReference.md) |  | [optional] 
**resources** | [**V1VolumeResourceRequirements**](V1VolumeResourceRequirements.md) |  | [optional] 
**selector** | [**V1LabelSelector**](V1LabelSelector.md) |  | [optional] 
**storage_class_name** | **str** | storageClassName is the name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1 | [optional] 
**volume_attributes_class_name** | **str** | volumeAttributesClassName may be used to set the VolumeAttributesClass used by this claim. If specified, the CSI driver will create or update the volume with the attributes defined in the corresponding VolumeAttributesClass. This has a different purpose than storageClassName, it can be changed after the claim is created. An empty string value means that no VolumeAttributesClass will be applied to the claim but it&#39;s not allowed to reset this field to empty string once it is set. If unspecified and the PersistentVolumeClaim is unbound, the default VolumeAttributesClass will be set by the persistentvolume controller if it exists. If the resource referred to by volumeAttributesClass does not exist, this PersistentVolumeClaim will be set to a Pending state, as reflected by the modifyVolumeStatus field, until such as a resource exists. More info: https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/ (Beta) Using this field requires the VolumeAttributesClass feature gate to be enabled (off by default). | [optional] 
**volume_mode** | **str** | volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec. | [optional] 
**volume_name** | **str** | volumeName is the binding reference to the PersistentVolume backing this claim. | [optional] 

## Example

```python
from kubernetes.client.models.v1_persistent_volume_claim_spec import V1PersistentVolumeClaimSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1PersistentVolumeClaimSpec from a JSON string
v1_persistent_volume_claim_spec_instance = V1PersistentVolumeClaimSpec.from_json(json)
# print the JSON string representation of the object
print(V1PersistentVolumeClaimSpec.to_json())

# convert the object into a dict
v1_persistent_volume_claim_spec_dict = v1_persistent_volume_claim_spec_instance.to_dict()
# create an instance of V1PersistentVolumeClaimSpec from a dict
v1_persistent_volume_claim_spec_from_dict = V1PersistentVolumeClaimSpec.from_dict(v1_persistent_volume_claim_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


