# V1NodeSystemInfo

NodeSystemInfo is a set of ids/uuids to uniquely identify the node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** | The Architecture reported by the node | 
**boot_id** | **str** | Boot ID reported by the node. | 
**container_runtime_version** | **str** | ContainerRuntime Version reported by the node through runtime remote API (e.g. containerd://1.4.2). | 
**kernel_version** | **str** | Kernel Version reported by the node from &#39;uname -r&#39; (e.g. 3.16.0-0.bpo.4-amd64). | 
**kube_proxy_version** | **str** | Deprecated: KubeProxy Version reported by the node. | 
**kubelet_version** | **str** | Kubelet Version reported by the node. | 
**machine_id** | **str** | MachineID reported by the node. For unique machine identification in the cluster this field is preferred. Learn more from man(5) machine-id: http://man7.org/linux/man-pages/man5/machine-id.5.html | 
**operating_system** | **str** | The Operating System reported by the node | 
**os_image** | **str** | OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)). | 
**swap** | [**V1NodeSwapStatus**](V1NodeSwapStatus.md) |  | [optional] 
**system_uuid** | **str** | SystemUUID reported by the node. For unique machine identification MachineID is preferred. This field is specific to Red Hat hosts https://access.redhat.com/documentation/en-us/red_hat_subscription_management/1/html/rhsm/uuid | 

## Example

```python
from kubernetes.client.models.v1_node_system_info import V1NodeSystemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V1NodeSystemInfo from a JSON string
v1_node_system_info_instance = V1NodeSystemInfo.from_json(json)
# print the JSON string representation of the object
print(V1NodeSystemInfo.to_json())

# convert the object into a dict
v1_node_system_info_dict = v1_node_system_info_instance.to_dict()
# create an instance of V1NodeSystemInfo from a dict
v1_node_system_info_from_dict = V1NodeSystemInfo.from_dict(v1_node_system_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


