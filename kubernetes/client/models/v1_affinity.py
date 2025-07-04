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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from kubernetes.client.models.v1_node_affinity import V1NodeAffinity
from kubernetes.client.models.v1_pod_affinity import V1PodAffinity
from kubernetes.client.models.v1_pod_anti_affinity import V1PodAntiAffinity
from typing import Optional, Set
from typing_extensions import Self

class V1Affinity(BaseModel):
    """
    Affinity is a group of affinity scheduling rules.
    """ # noqa: E501
    node_affinity: Optional[V1NodeAffinity] = Field(default=None, alias="nodeAffinity")
    pod_affinity: Optional[V1PodAffinity] = Field(default=None, alias="podAffinity")
    pod_anti_affinity: Optional[V1PodAntiAffinity] = Field(default=None, alias="podAntiAffinity")
    __properties: ClassVar[List[str]] = ["nodeAffinity", "podAffinity", "podAntiAffinity"]

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
        """Create an instance of V1Affinity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of node_affinity
        if self.node_affinity:
            _dict['nodeAffinity'] = self.node_affinity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pod_affinity
        if self.pod_affinity:
            _dict['podAffinity'] = self.pod_affinity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pod_anti_affinity
        if self.pod_anti_affinity:
            _dict['podAntiAffinity'] = self.pod_anti_affinity.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1Affinity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "nodeAffinity": V1NodeAffinity.from_dict(obj["nodeAffinity"]) if obj.get("nodeAffinity") is not None else None,
            "podAffinity": V1PodAffinity.from_dict(obj["podAffinity"]) if obj.get("podAffinity") is not None else None,
            "podAntiAffinity": V1PodAntiAffinity.from_dict(obj["podAntiAffinity"]) if obj.get("podAntiAffinity") is not None else None
        })
        return _obj


