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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from kubernetes.client.models.v1_label_selector import V1LabelSelector
from kubernetes.client.models.v1_persistent_volume_claim import V1PersistentVolumeClaim
from kubernetes.client.models.v1_pod_template_spec import V1PodTemplateSpec
from kubernetes.client.models.v1_stateful_set_ordinals import V1StatefulSetOrdinals
from kubernetes.client.models.v1_stateful_set_persistent_volume_claim_retention_policy import V1StatefulSetPersistentVolumeClaimRetentionPolicy
from kubernetes.client.models.v1_stateful_set_update_strategy import V1StatefulSetUpdateStrategy
from typing import Optional, Set
from typing_extensions import Self

class V1StatefulSetSpec(BaseModel):
    """
    A StatefulSetSpec is the specification of a StatefulSet.
    """ # noqa: E501
    min_ready_seconds: Optional[StrictInt] = Field(default=None, description="Minimum number of seconds for which a newly created pod should be ready without any of its container crashing for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)", alias="minReadySeconds")
    ordinals: Optional[V1StatefulSetOrdinals] = None
    persistent_volume_claim_retention_policy: Optional[V1StatefulSetPersistentVolumeClaimRetentionPolicy] = Field(default=None, alias="persistentVolumeClaimRetentionPolicy")
    pod_management_policy: Optional[StrictStr] = Field(default=None, description="podManagementPolicy controls how pods are created during initial scale up, when replacing pods on nodes, or when scaling down. The default policy is `OrderedReady`, where pods are created in increasing order (pod-0, then pod-1, etc) and the controller will wait until each pod is ready before continuing. When scaling down, the pods are removed in the opposite order. The alternative policy is `Parallel` which will create pods in parallel to match the desired scale without waiting, and on scale down will delete all pods at once.", alias="podManagementPolicy")
    replicas: Optional[StrictInt] = Field(default=None, description="replicas is the desired number of replicas of the given Template. These are replicas in the sense that they are instantiations of the same Template, but individual replicas also have a consistent identity. If unspecified, defaults to 1.")
    revision_history_limit: Optional[StrictInt] = Field(default=None, description="revisionHistoryLimit is the maximum number of revisions that will be maintained in the StatefulSet's revision history. The revision history consists of all revisions not represented by a currently applied StatefulSetSpec version. The default value is 10.", alias="revisionHistoryLimit")
    selector: V1LabelSelector
    service_name: Optional[StrictStr] = Field(default=None, description="serviceName is the name of the service that governs this StatefulSet. This service must exist before the StatefulSet, and is responsible for the network identity of the set. Pods get DNS/hostnames that follow the pattern: pod-specific-string.serviceName.default.svc.cluster.local where \"pod-specific-string\" is managed by the StatefulSet controller.", alias="serviceName")
    template: V1PodTemplateSpec
    update_strategy: Optional[V1StatefulSetUpdateStrategy] = Field(default=None, alias="updateStrategy")
    volume_claim_templates: Optional[List[V1PersistentVolumeClaim]] = Field(default=None, description="volumeClaimTemplates is a list of claims that pods are allowed to reference. The StatefulSet controller is responsible for mapping network identities to claims in a way that maintains the identity of a pod. Every claim in this list must have at least one matching (by name) volumeMount in one container in the template. A claim in this list takes precedence over any volumes in the template, with the same name.", alias="volumeClaimTemplates")
    __properties: ClassVar[List[str]] = ["minReadySeconds", "ordinals", "persistentVolumeClaimRetentionPolicy", "podManagementPolicy", "replicas", "revisionHistoryLimit", "selector", "serviceName", "template", "updateStrategy", "volumeClaimTemplates"]

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
        """Create an instance of V1StatefulSetSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ordinals
        if self.ordinals:
            _dict['ordinals'] = self.ordinals.to_dict()
        # override the default output from pydantic by calling `to_dict()` of persistent_volume_claim_retention_policy
        if self.persistent_volume_claim_retention_policy:
            _dict['persistentVolumeClaimRetentionPolicy'] = self.persistent_volume_claim_retention_policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of selector
        if self.selector:
            _dict['selector'] = self.selector.to_dict()
        # override the default output from pydantic by calling `to_dict()` of template
        if self.template:
            _dict['template'] = self.template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of update_strategy
        if self.update_strategy:
            _dict['updateStrategy'] = self.update_strategy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in volume_claim_templates (list)
        _items = []
        if self.volume_claim_templates:
            for _item_volume_claim_templates in self.volume_claim_templates:
                if _item_volume_claim_templates:
                    _items.append(_item_volume_claim_templates.to_dict())
            _dict['volumeClaimTemplates'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1StatefulSetSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "minReadySeconds": obj.get("minReadySeconds"),
            "ordinals": V1StatefulSetOrdinals.from_dict(obj["ordinals"]) if obj.get("ordinals") is not None else None,
            "persistentVolumeClaimRetentionPolicy": V1StatefulSetPersistentVolumeClaimRetentionPolicy.from_dict(obj["persistentVolumeClaimRetentionPolicy"]) if obj.get("persistentVolumeClaimRetentionPolicy") is not None else None,
            "podManagementPolicy": obj.get("podManagementPolicy"),
            "replicas": obj.get("replicas"),
            "revisionHistoryLimit": obj.get("revisionHistoryLimit"),
            "selector": V1LabelSelector.from_dict(obj["selector"]) if obj.get("selector") is not None else None,
            "serviceName": obj.get("serviceName"),
            "template": V1PodTemplateSpec.from_dict(obj["template"]) if obj.get("template") is not None else None,
            "updateStrategy": V1StatefulSetUpdateStrategy.from_dict(obj["updateStrategy"]) if obj.get("updateStrategy") is not None else None,
            "volumeClaimTemplates": [V1PersistentVolumeClaim.from_dict(_item) for _item in obj["volumeClaimTemplates"]] if obj.get("volumeClaimTemplates") is not None else None
        })
        return _obj


