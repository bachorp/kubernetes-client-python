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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from kubernetes.client.models.v1_replication_controller_condition import V1ReplicationControllerCondition
from typing import Optional, Set
from typing_extensions import Self

class V1ReplicationControllerStatus(BaseModel):
    """
    ReplicationControllerStatus represents the current status of a replication controller.
    """ # noqa: E501
    available_replicas: Optional[StrictInt] = Field(default=None, description="The number of available replicas (ready for at least minReadySeconds) for this replication controller.", alias="availableReplicas")
    conditions: Optional[List[V1ReplicationControllerCondition]] = Field(default=None, description="Represents the latest available observations of a replication controller's current state.")
    fully_labeled_replicas: Optional[StrictInt] = Field(default=None, description="The number of pods that have labels matching the labels of the pod template of the replication controller.", alias="fullyLabeledReplicas")
    observed_generation: Optional[StrictInt] = Field(default=None, description="ObservedGeneration reflects the generation of the most recently observed replication controller.", alias="observedGeneration")
    ready_replicas: Optional[StrictInt] = Field(default=None, description="The number of ready replicas for this replication controller.", alias="readyReplicas")
    replicas: StrictInt = Field(description="Replicas is the most recently observed number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller")
    __properties: ClassVar[List[str]] = ["availableReplicas", "conditions", "fullyLabeledReplicas", "observedGeneration", "readyReplicas", "replicas"]

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
        """Create an instance of V1ReplicationControllerStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in conditions (list)
        _items = []
        if self.conditions:
            for _item_conditions in self.conditions:
                if _item_conditions:
                    _items.append(_item_conditions.to_dict())
            _dict['conditions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1ReplicationControllerStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "availableReplicas": obj.get("availableReplicas"),
            "conditions": [V1ReplicationControllerCondition.from_dict(_item) for _item in obj["conditions"]] if obj.get("conditions") is not None else None,
            "fullyLabeledReplicas": obj.get("fullyLabeledReplicas"),
            "observedGeneration": obj.get("observedGeneration"),
            "readyReplicas": obj.get("readyReplicas"),
            "replicas": obj.get("replicas")
        })
        return _obj


