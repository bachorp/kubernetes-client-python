# V1Volume

Volume represents a named volume in a pod that may be accessed by any container in the pod.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_elastic_block_store** | [**V1AWSElasticBlockStoreVolumeSource**](V1AWSElasticBlockStoreVolumeSource.md) |  | [optional] 
**azure_disk** | [**V1AzureDiskVolumeSource**](V1AzureDiskVolumeSource.md) |  | [optional] 
**azure_file** | [**V1AzureFileVolumeSource**](V1AzureFileVolumeSource.md) |  | [optional] 
**cephfs** | [**V1CephFSVolumeSource**](V1CephFSVolumeSource.md) |  | [optional] 
**cinder** | [**V1CinderVolumeSource**](V1CinderVolumeSource.md) |  | [optional] 
**config_map** | [**V1ConfigMapVolumeSource**](V1ConfigMapVolumeSource.md) |  | [optional] 
**csi** | [**V1CSIVolumeSource**](V1CSIVolumeSource.md) |  | [optional] 
**downward_api** | [**V1DownwardAPIVolumeSource**](V1DownwardAPIVolumeSource.md) |  | [optional] 
**empty_dir** | [**V1EmptyDirVolumeSource**](V1EmptyDirVolumeSource.md) |  | [optional] 
**ephemeral** | [**V1EphemeralVolumeSource**](V1EphemeralVolumeSource.md) |  | [optional] 
**fc** | [**V1FCVolumeSource**](V1FCVolumeSource.md) |  | [optional] 
**flex_volume** | [**V1FlexVolumeSource**](V1FlexVolumeSource.md) |  | [optional] 
**flocker** | [**V1FlockerVolumeSource**](V1FlockerVolumeSource.md) |  | [optional] 
**gce_persistent_disk** | [**V1GCEPersistentDiskVolumeSource**](V1GCEPersistentDiskVolumeSource.md) |  | [optional] 
**git_repo** | [**V1GitRepoVolumeSource**](V1GitRepoVolumeSource.md) |  | [optional] 
**glusterfs** | [**V1GlusterfsVolumeSource**](V1GlusterfsVolumeSource.md) |  | [optional] 
**host_path** | [**V1HostPathVolumeSource**](V1HostPathVolumeSource.md) |  | [optional] 
**image** | [**V1ImageVolumeSource**](V1ImageVolumeSource.md) |  | [optional] 
**iscsi** | [**V1ISCSIVolumeSource**](V1ISCSIVolumeSource.md) |  | [optional] 
**name** | **str** | name of the volume. Must be a DNS_LABEL and unique within the pod. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | 
**nfs** | [**V1NFSVolumeSource**](V1NFSVolumeSource.md) |  | [optional] 
**persistent_volume_claim** | [**V1PersistentVolumeClaimVolumeSource**](V1PersistentVolumeClaimVolumeSource.md) |  | [optional] 
**photon_persistent_disk** | [**V1PhotonPersistentDiskVolumeSource**](V1PhotonPersistentDiskVolumeSource.md) |  | [optional] 
**portworx_volume** | [**V1PortworxVolumeSource**](V1PortworxVolumeSource.md) |  | [optional] 
**projected** | [**V1ProjectedVolumeSource**](V1ProjectedVolumeSource.md) |  | [optional] 
**quobyte** | [**V1QuobyteVolumeSource**](V1QuobyteVolumeSource.md) |  | [optional] 
**rbd** | [**V1RBDVolumeSource**](V1RBDVolumeSource.md) |  | [optional] 
**scale_io** | [**V1ScaleIOVolumeSource**](V1ScaleIOVolumeSource.md) |  | [optional] 
**secret** | [**V1SecretVolumeSource**](V1SecretVolumeSource.md) |  | [optional] 
**storageos** | [**V1StorageOSVolumeSource**](V1StorageOSVolumeSource.md) |  | [optional] 
**vsphere_volume** | [**V1VsphereVirtualDiskVolumeSource**](V1VsphereVirtualDiskVolumeSource.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_volume import V1Volume

# TODO update the JSON string below
json = "{}"
# create an instance of V1Volume from a JSON string
v1_volume_instance = V1Volume.from_json(json)
# print the JSON string representation of the object
print(V1Volume.to_json())

# convert the object into a dict
v1_volume_dict = v1_volume_instance.to_dict()
# create an instance of V1Volume from a dict
v1_volume_from_dict = V1Volume.from_dict(v1_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


