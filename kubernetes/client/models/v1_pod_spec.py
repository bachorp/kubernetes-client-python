# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.33
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from kubernetes.client.models.v1_affinity import V1Affinity
from kubernetes.client.models.v1_container import V1Container
from kubernetes.client.models.v1_ephemeral_container import V1EphemeralContainer
from kubernetes.client.models.v1_host_alias import V1HostAlias
from kubernetes.client.models.v1_local_object_reference import V1LocalObjectReference
from kubernetes.client.models.v1_pod_dns_config import V1PodDNSConfig
from kubernetes.client.models.v1_pod_os import V1PodOS
from kubernetes.client.models.v1_pod_readiness_gate import V1PodReadinessGate
from kubernetes.client.models.v1_pod_resource_claim import V1PodResourceClaim
from kubernetes.client.models.v1_pod_scheduling_gate import V1PodSchedulingGate
from kubernetes.client.models.v1_pod_security_context import V1PodSecurityContext
from kubernetes.client.models.v1_resource_requirements import V1ResourceRequirements
from kubernetes.client.models.v1_toleration import V1Toleration
from kubernetes.client.models.v1_topology_spread_constraint import V1TopologySpreadConstraint
from kubernetes.client.models.v1_volume import V1Volume
from typing import Optional, Set
from typing_extensions import Self

class V1PodSpec(BaseModel):
    """
    PodSpec is a description of a pod.
    """ # noqa: E501
    active_deadline_seconds: Optional[StrictInt] = Field(default=None, description="Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer.", alias="activeDeadlineSeconds")
    affinity: Optional[V1Affinity] = None
    automount_service_account_token: Optional[StrictBool] = Field(default=None, description="AutomountServiceAccountToken indicates whether a service account token should be automatically mounted.", alias="automountServiceAccountToken")
    containers: List[V1Container] = Field(description="List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated.")
    dns_config: Optional[V1PodDNSConfig] = Field(default=None, alias="dnsConfig")
    dns_policy: Optional[StrictStr] = Field(default=None, description="Set DNS policy for the pod. Defaults to \"ClusterFirst\". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'.", alias="dnsPolicy")
    enable_service_links: Optional[StrictBool] = Field(default=None, description="EnableServiceLinks indicates whether information about services should be injected into pod's environment variables, matching the syntax of Docker links. Optional: Defaults to true.", alias="enableServiceLinks")
    ephemeral_containers: Optional[List[V1EphemeralContainer]] = Field(default=None, description="List of ephemeral containers run in this pod. Ephemeral containers may be run in an existing pod to perform user-initiated actions such as debugging. This list cannot be specified when creating a pod, and it cannot be modified by updating the pod spec. In order to add an ephemeral container to an existing pod, use the pod's ephemeralcontainers subresource.", alias="ephemeralContainers")
    host_aliases: Optional[List[V1HostAlias]] = Field(default=None, description="HostAliases is an optional list of hosts and IPs that will be injected into the pod's hosts file if specified.", alias="hostAliases")
    host_ipc: Optional[StrictBool] = Field(default=None, description="Use the host's ipc namespace. Optional: Default to false.", alias="hostIPC")
    host_network: Optional[StrictBool] = Field(default=None, description="Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false.", alias="hostNetwork")
    host_pid: Optional[StrictBool] = Field(default=None, description="Use the host's pid namespace. Optional: Default to false.", alias="hostPID")
    host_users: Optional[StrictBool] = Field(default=None, description="Use the host's user namespace. Optional: Default to true. If set to true or not present, the pod will be run in the host user namespace, useful for when the pod needs a feature only available to the host user namespace, such as loading a kernel module with CAP_SYS_MODULE. When set to false, a new userns is created for the pod. Setting false is useful for mitigating container breakout vulnerabilities even allowing users to run their containers as root without actually having root privileges on the host. This field is alpha-level and is only honored by servers that enable the UserNamespacesSupport feature.", alias="hostUsers")
    hostname: Optional[StrictStr] = Field(default=None, description="Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value.")
    image_pull_secrets: Optional[List[V1LocalObjectReference]] = Field(default=None, description="ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. More info: https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod", alias="imagePullSecrets")
    init_containers: Optional[List[V1Container]] = Field(default=None, description="List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added or removed. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/", alias="initContainers")
    node_name: Optional[StrictStr] = Field(default=None, description="NodeName indicates in which node this pod is scheduled. If empty, this pod is a candidate for scheduling by the scheduler defined in schedulerName. Once this field is set, the kubelet for this node becomes responsible for the lifecycle of this pod. This field should not be used to express a desire for the pod to be scheduled on a specific node. https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodename", alias="nodeName")
    node_selector: Optional[Dict[str, StrictStr]] = Field(default=None, description="NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/", alias="nodeSelector")
    os: Optional[V1PodOS] = None
    overhead: Optional[Dict[str, StrictStr]] = Field(default=None, description="Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. This field will be autopopulated at admission time by the RuntimeClass admission controller. If the RuntimeClass admission controller is enabled, overhead must not be set in Pod create requests. The RuntimeClass admission controller will reject Pod create requests which have the overhead already set. If RuntimeClass is configured and selected in the PodSpec, Overhead will be set to the value defined in the corresponding RuntimeClass, otherwise it will remain unset and treated as zero. More info: https://git.k8s.io/enhancements/keps/sig-node/688-pod-overhead/README.md")
    preemption_policy: Optional[StrictStr] = Field(default=None, description="PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset.", alias="preemptionPolicy")
    priority: Optional[StrictInt] = Field(default=None, description="The priority value. Various system components use this field to find the priority of the pod. When Priority Admission Controller is enabled, it prevents users from setting this field. The admission controller populates this field from PriorityClassName. The higher the value, the higher the priority.")
    priority_class_name: Optional[StrictStr] = Field(default=None, description="If specified, indicates the pod's priority. \"system-node-critical\" and \"system-cluster-critical\" are two special keywords which indicate the highest priorities with the former being the highest priority. Any other name must be defined by creating a PriorityClass object with that name. If not specified, the pod priority will be default or zero if there is no default.", alias="priorityClassName")
    readiness_gates: Optional[List[V1PodReadinessGate]] = Field(default=None, description="If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when all its containers are ready AND all conditions specified in the readiness gates have status equal to \"True\" More info: https://git.k8s.io/enhancements/keps/sig-network/580-pod-readiness-gates", alias="readinessGates")
    resource_claims: Optional[List[V1PodResourceClaim]] = Field(default=None, description="ResourceClaims defines which ResourceClaims must be allocated and reserved before the Pod is allowed to start. The resources will be made available to those containers which consume them by name.  This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.  This field is immutable.", alias="resourceClaims")
    resources: Optional[V1ResourceRequirements] = None
    restart_policy: Optional[StrictStr] = Field(default=None, description="Restart policy for all containers within the pod. One of Always, OnFailure, Never. In some contexts, only a subset of those values may be permitted. Default to Always. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy", alias="restartPolicy")
    runtime_class_name: Optional[StrictStr] = Field(default=None, description="RuntimeClassName refers to a RuntimeClass object in the node.k8s.io group, which should be used to run this pod.  If no RuntimeClass resource matches the named class, the pod will not be run. If unset or empty, the \"legacy\" RuntimeClass will be used, which is an implicit class with an empty definition that uses the default runtime handler. More info: https://git.k8s.io/enhancements/keps/sig-node/585-runtime-class", alias="runtimeClassName")
    scheduler_name: Optional[StrictStr] = Field(default=None, description="If specified, the pod will be dispatched by specified scheduler. If not specified, the pod will be dispatched by default scheduler.", alias="schedulerName")
    scheduling_gates: Optional[List[V1PodSchedulingGate]] = Field(default=None, description="SchedulingGates is an opaque list of values that if specified will block scheduling the pod. If schedulingGates is not empty, the pod will stay in the SchedulingGated state and the scheduler will not attempt to schedule the pod.  SchedulingGates can only be set at pod creation time, and be removed only afterwards.", alias="schedulingGates")
    security_context: Optional[V1PodSecurityContext] = Field(default=None, alias="securityContext")
    service_account: Optional[StrictStr] = Field(default=None, description="DeprecatedServiceAccount is a deprecated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead.", alias="serviceAccount")
    service_account_name: Optional[StrictStr] = Field(default=None, description="ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/", alias="serviceAccountName")
    set_hostname_as_fqdn: Optional[StrictBool] = Field(default=None, description="If true the pod's hostname will be configured as the pod's FQDN, rather than the leaf name (the default). In Linux containers, this means setting the FQDN in the hostname field of the kernel (the nodename field of struct utsname). In Windows containers, this means setting the registry value of hostname for the registry key HKEY_LOCAL_MACHINE\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\Tcpip\\\\Parameters to FQDN. If a pod does not have FQDN, this has no effect. Default to false.", alias="setHostnameAsFQDN")
    share_process_namespace: Optional[StrictBool] = Field(default=None, description="Share a single process namespace between all of the containers in a pod. When this is set containers will be able to view and signal processes from other containers in the same pod, and the first process in each container will not be assigned PID 1. HostPID and ShareProcessNamespace cannot both be set. Optional: Default to false.", alias="shareProcessNamespace")
    subdomain: Optional[StrictStr] = Field(default=None, description="If specified, the fully qualified Pod hostname will be \"<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>\". If not specified, the pod will not have a domainname at all.")
    termination_grace_period_seconds: Optional[StrictInt] = Field(default=None, description="Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.", alias="terminationGracePeriodSeconds")
    tolerations: Optional[List[V1Toleration]] = Field(default=None, description="If specified, the pod's tolerations.")
    topology_spread_constraints: Optional[List[V1TopologySpreadConstraint]] = Field(default=None, description="TopologySpreadConstraints describes how a group of pods ought to spread across topology domains. Scheduler will schedule pods in a way which abides by the constraints. All topologySpreadConstraints are ANDed.", alias="topologySpreadConstraints")
    volumes: Optional[List[V1Volume]] = Field(default=None, description="List of volumes that can be mounted by containers belonging to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes")
    __properties: ClassVar[List[str]] = ["activeDeadlineSeconds", "affinity", "automountServiceAccountToken", "containers", "dnsConfig", "dnsPolicy", "enableServiceLinks", "ephemeralContainers", "hostAliases", "hostIPC", "hostNetwork", "hostPID", "hostUsers", "hostname", "imagePullSecrets", "initContainers", "nodeName", "nodeSelector", "os", "overhead", "preemptionPolicy", "priority", "priorityClassName", "readinessGates", "resourceClaims", "resources", "restartPolicy", "runtimeClassName", "schedulerName", "schedulingGates", "securityContext", "serviceAccount", "serviceAccountName", "setHostnameAsFQDN", "shareProcessNamespace", "subdomain", "terminationGracePeriodSeconds", "tolerations", "topologySpreadConstraints", "volumes"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of V1PodSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of affinity
        if self.affinity:
            _dict['affinity'] = self.affinity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in containers (list)
        _items = []
        if self.containers:
            for _item_containers in self.containers:
                if _item_containers:
                    _items.append(_item_containers.to_dict())
            _dict['containers'] = _items
        # override the default output from pydantic by calling `to_dict()` of dns_config
        if self.dns_config:
            _dict['dnsConfig'] = self.dns_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in ephemeral_containers (list)
        _items = []
        if self.ephemeral_containers:
            for _item_ephemeral_containers in self.ephemeral_containers:
                if _item_ephemeral_containers:
                    _items.append(_item_ephemeral_containers.to_dict())
            _dict['ephemeralContainers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in host_aliases (list)
        _items = []
        if self.host_aliases:
            for _item_host_aliases in self.host_aliases:
                if _item_host_aliases:
                    _items.append(_item_host_aliases.to_dict())
            _dict['hostAliases'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in image_pull_secrets (list)
        _items = []
        if self.image_pull_secrets:
            for _item_image_pull_secrets in self.image_pull_secrets:
                if _item_image_pull_secrets:
                    _items.append(_item_image_pull_secrets.to_dict())
            _dict['imagePullSecrets'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in init_containers (list)
        _items = []
        if self.init_containers:
            for _item_init_containers in self.init_containers:
                if _item_init_containers:
                    _items.append(_item_init_containers.to_dict())
            _dict['initContainers'] = _items
        # override the default output from pydantic by calling `to_dict()` of os
        if self.os:
            _dict['os'] = self.os.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in readiness_gates (list)
        _items = []
        if self.readiness_gates:
            for _item_readiness_gates in self.readiness_gates:
                if _item_readiness_gates:
                    _items.append(_item_readiness_gates.to_dict())
            _dict['readinessGates'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in resource_claims (list)
        _items = []
        if self.resource_claims:
            for _item_resource_claims in self.resource_claims:
                if _item_resource_claims:
                    _items.append(_item_resource_claims.to_dict())
            _dict['resourceClaims'] = _items
        # override the default output from pydantic by calling `to_dict()` of resources
        if self.resources:
            _dict['resources'] = self.resources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in scheduling_gates (list)
        _items = []
        if self.scheduling_gates:
            for _item_scheduling_gates in self.scheduling_gates:
                if _item_scheduling_gates:
                    _items.append(_item_scheduling_gates.to_dict())
            _dict['schedulingGates'] = _items
        # override the default output from pydantic by calling `to_dict()` of security_context
        if self.security_context:
            _dict['securityContext'] = self.security_context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tolerations (list)
        _items = []
        if self.tolerations:
            for _item_tolerations in self.tolerations:
                if _item_tolerations:
                    _items.append(_item_tolerations.to_dict())
            _dict['tolerations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in topology_spread_constraints (list)
        _items = []
        if self.topology_spread_constraints:
            for _item_topology_spread_constraints in self.topology_spread_constraints:
                if _item_topology_spread_constraints:
                    _items.append(_item_topology_spread_constraints.to_dict())
            _dict['topologySpreadConstraints'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in volumes (list)
        _items = []
        if self.volumes:
            for _item_volumes in self.volumes:
                if _item_volumes:
                    _items.append(_item_volumes.to_dict())
            _dict['volumes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1PodSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "activeDeadlineSeconds": obj.get("activeDeadlineSeconds"),
            "affinity": V1Affinity.from_dict(obj["affinity"]) if obj.get("affinity") is not None else None,
            "automountServiceAccountToken": obj.get("automountServiceAccountToken"),
            "containers": [V1Container.from_dict(_item) for _item in obj["containers"]] if obj.get("containers") is not None else None,
            "dnsConfig": V1PodDNSConfig.from_dict(obj["dnsConfig"]) if obj.get("dnsConfig") is not None else None,
            "dnsPolicy": obj.get("dnsPolicy"),
            "enableServiceLinks": obj.get("enableServiceLinks"),
            "ephemeralContainers": [V1EphemeralContainer.from_dict(_item) for _item in obj["ephemeralContainers"]] if obj.get("ephemeralContainers") is not None else None,
            "hostAliases": [V1HostAlias.from_dict(_item) for _item in obj["hostAliases"]] if obj.get("hostAliases") is not None else None,
            "hostIPC": obj.get("hostIPC"),
            "hostNetwork": obj.get("hostNetwork"),
            "hostPID": obj.get("hostPID"),
            "hostUsers": obj.get("hostUsers"),
            "hostname": obj.get("hostname"),
            "imagePullSecrets": [V1LocalObjectReference.from_dict(_item) for _item in obj["imagePullSecrets"]] if obj.get("imagePullSecrets") is not None else None,
            "initContainers": [V1Container.from_dict(_item) for _item in obj["initContainers"]] if obj.get("initContainers") is not None else None,
            "nodeName": obj.get("nodeName"),
            "nodeSelector": obj.get("nodeSelector"),
            "os": V1PodOS.from_dict(obj["os"]) if obj.get("os") is not None else None,
            "overhead": obj.get("overhead"),
            "preemptionPolicy": obj.get("preemptionPolicy"),
            "priority": obj.get("priority"),
            "priorityClassName": obj.get("priorityClassName"),
            "readinessGates": [V1PodReadinessGate.from_dict(_item) for _item in obj["readinessGates"]] if obj.get("readinessGates") is not None else None,
            "resourceClaims": [V1PodResourceClaim.from_dict(_item) for _item in obj["resourceClaims"]] if obj.get("resourceClaims") is not None else None,
            "resources": V1ResourceRequirements.from_dict(obj["resources"]) if obj.get("resources") is not None else None,
            "restartPolicy": obj.get("restartPolicy"),
            "runtimeClassName": obj.get("runtimeClassName"),
            "schedulerName": obj.get("schedulerName"),
            "schedulingGates": [V1PodSchedulingGate.from_dict(_item) for _item in obj["schedulingGates"]] if obj.get("schedulingGates") is not None else None,
            "securityContext": V1PodSecurityContext.from_dict(obj["securityContext"]) if obj.get("securityContext") is not None else None,
            "serviceAccount": obj.get("serviceAccount"),
            "serviceAccountName": obj.get("serviceAccountName"),
            "setHostnameAsFQDN": obj.get("setHostnameAsFQDN"),
            "shareProcessNamespace": obj.get("shareProcessNamespace"),
            "subdomain": obj.get("subdomain"),
            "terminationGracePeriodSeconds": obj.get("terminationGracePeriodSeconds"),
            "tolerations": [V1Toleration.from_dict(_item) for _item in obj["tolerations"]] if obj.get("tolerations") is not None else None,
            "topologySpreadConstraints": [V1TopologySpreadConstraint.from_dict(_item) for _item in obj["topologySpreadConstraints"]] if obj.get("topologySpreadConstraints") is not None else None,
            "volumes": [V1Volume.from_dict(_item) for _item in obj["volumes"]] if obj.get("volumes") is not None else None
        })
        return _obj


