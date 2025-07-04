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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from kubernetes.client.models.v2_horizontal_pod_autoscaler_condition import V2HorizontalPodAutoscalerCondition
from kubernetes.client.models.v2_metric_status import V2MetricStatus
from typing import Optional, Set
from typing_extensions import Self

class V2HorizontalPodAutoscalerStatus(BaseModel):
    """
    HorizontalPodAutoscalerStatus describes the current status of a horizontal pod autoscaler.
    """ # noqa: E501
    conditions: Optional[List[V2HorizontalPodAutoscalerCondition]] = Field(default=None, description="conditions is the set of conditions required for this autoscaler to scale its target, and indicates whether or not those conditions are met.")
    current_metrics: Optional[List[V2MetricStatus]] = Field(default=None, description="currentMetrics is the last read state of the metrics used by this autoscaler.", alias="currentMetrics")
    current_replicas: Optional[StrictInt] = Field(default=None, description="currentReplicas is current number of replicas of pods managed by this autoscaler, as last seen by the autoscaler.", alias="currentReplicas")
    desired_replicas: StrictInt = Field(description="desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as last calculated by the autoscaler.", alias="desiredReplicas")
    last_scale_time: Optional[datetime] = Field(default=None, description="lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used by the autoscaler to control how often the number of pods is changed.", alias="lastScaleTime")
    observed_generation: Optional[StrictInt] = Field(default=None, description="observedGeneration is the most recent generation observed by this autoscaler.", alias="observedGeneration")
    __properties: ClassVar[List[str]] = ["conditions", "currentMetrics", "currentReplicas", "desiredReplicas", "lastScaleTime", "observedGeneration"]

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
        """Create an instance of V2HorizontalPodAutoscalerStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in current_metrics (list)
        _items = []
        if self.current_metrics:
            for _item_current_metrics in self.current_metrics:
                if _item_current_metrics:
                    _items.append(_item_current_metrics.to_dict())
            _dict['currentMetrics'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V2HorizontalPodAutoscalerStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "conditions": [V2HorizontalPodAutoscalerCondition.from_dict(_item) for _item in obj["conditions"]] if obj.get("conditions") is not None else None,
            "currentMetrics": [V2MetricStatus.from_dict(_item) for _item in obj["currentMetrics"]] if obj.get("currentMetrics") is not None else None,
            "currentReplicas": obj.get("currentReplicas"),
            "desiredReplicas": obj.get("desiredReplicas"),
            "lastScaleTime": obj.get("lastScaleTime"),
            "observedGeneration": obj.get("observedGeneration")
        })
        return _obj


