# V1PodSecurityContext

PodSecurityContext holds pod-level security attributes and common container settings. Some fields are also present in container.securityContext.  Field values of container.securityContext take precedence over field values of PodSecurityContext.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_armor_profile** | [**V1AppArmorProfile**](V1AppArmorProfile.md) |  | [optional] 
**fs_group** | **int** | A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod:  1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR&#39;d with rw-rw----  If unset, the Kubelet will not modify the ownership and permissions of any volume. Note that this field cannot be set when spec.os.name is windows. | [optional] 
**fs_group_change_policy** | **str** | fsGroupChangePolicy defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Valid values are \&quot;OnRootMismatch\&quot; and \&quot;Always\&quot;. If not specified, \&quot;Always\&quot; is used. Note that this field cannot be set when spec.os.name is windows. | [optional] 
**run_as_group** | **int** | The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows. | [optional] 
**run_as_non_root** | **bool** | Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. | [optional] 
**run_as_user** | **int** | The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows. | [optional] 
**se_linux_change_policy** | **str** | seLinuxChangePolicy defines how the container&#39;s SELinux label is applied to all volumes used by the Pod. It has no effect on nodes that do not support SELinux or to volumes does not support SELinux. Valid values are \&quot;MountOption\&quot; and \&quot;Recursive\&quot;.  \&quot;Recursive\&quot; means relabeling of all files on all Pod volumes by the container runtime. This may be slow for large volumes, but allows mixing privileged and unprivileged Pods sharing the same volume on the same node.  \&quot;MountOption\&quot; mounts all eligible Pod volumes with &#x60;-o context&#x60; mount option. This requires all Pods that share the same volume to use the same SELinux label. It is not possible to share the same volume among privileged and unprivileged Pods. Eligible volumes are in-tree FibreChannel and iSCSI volumes, and all CSI volumes whose CSI driver announces SELinux support by setting spec.seLinuxMount: true in their CSIDriver instance. Other volumes are always re-labelled recursively. \&quot;MountOption\&quot; value is allowed only when SELinuxMount feature gate is enabled.  If not specified and SELinuxMount feature gate is enabled, \&quot;MountOption\&quot; is used. If not specified and SELinuxMount feature gate is disabled, \&quot;MountOption\&quot; is used for ReadWriteOncePod volumes and \&quot;Recursive\&quot; for all other volumes.  This field affects only Pods that have SELinux label set, either in PodSecurityContext or in SecurityContext of all containers.  All Pods that use the same volume should use the same seLinuxChangePolicy, otherwise some pods can get stuck in ContainerCreating state. Note that this field cannot be set when spec.os.name is windows. | [optional] 
**se_linux_options** | [**V1SELinuxOptions**](V1SELinuxOptions.md) |  | [optional] 
**seccomp_profile** | [**V1SeccompProfile**](V1SeccompProfile.md) |  | [optional] 
**supplemental_groups** | **List[int]** | A list of groups applied to the first process run in each container, in addition to the container&#39;s primary GID and fsGroup (if specified).  If the SupplementalGroupsPolicy feature is enabled, the supplementalGroupsPolicy field determines whether these are in addition to or instead of any group memberships defined in the container image. If unspecified, no additional groups are added, though group memberships defined in the container image may still be used, depending on the supplementalGroupsPolicy field. Note that this field cannot be set when spec.os.name is windows. | [optional] 
**supplemental_groups_policy** | **str** | Defines how supplemental groups of the first container processes are calculated. Valid values are \&quot;Merge\&quot; and \&quot;Strict\&quot;. If not specified, \&quot;Merge\&quot; is used. (Alpha) Using the field requires the SupplementalGroupsPolicy feature gate to be enabled and the container runtime must implement support for this feature. Note that this field cannot be set when spec.os.name is windows. | [optional] 
**sysctls** | [**List[V1Sysctl]**](V1Sysctl.md) | Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Note that this field cannot be set when spec.os.name is windows. | [optional] 
**windows_options** | [**V1WindowsSecurityContextOptions**](V1WindowsSecurityContextOptions.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_pod_security_context import V1PodSecurityContext

# TODO update the JSON string below
json = "{}"
# create an instance of V1PodSecurityContext from a JSON string
v1_pod_security_context_instance = V1PodSecurityContext.from_json(json)
# print the JSON string representation of the object
print(V1PodSecurityContext.to_json())

# convert the object into a dict
v1_pod_security_context_dict = v1_pod_security_context_instance.to_dict()
# create an instance of V1PodSecurityContext from a dict
v1_pod_security_context_from_dict = V1PodSecurityContext.from_dict(v1_pod_security_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


