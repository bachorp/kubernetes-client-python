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
from kubernetes.client.models.v1beta2_device_class_configuration import V1beta2DeviceClassConfiguration
from kubernetes.client.models.v1beta2_device_selector import V1beta2DeviceSelector
from typing import Optional, Set
from typing_extensions import Self

class V1beta2DeviceClassSpec(BaseModel):
    """
    DeviceClassSpec is used in a [DeviceClass] to define what can be allocated and how to configure it.
    """ # noqa: E501
    config: Optional[List[V1beta2DeviceClassConfiguration]] = Field(default=None, description="Config defines configuration parameters that apply to each device that is claimed via this class. Some classses may potentially be satisfied by multiple drivers, so each instance of a vendor configuration applies to exactly one driver.  They are passed to the driver, but are not considered while allocating the claim.")
    selectors: Optional[List[V1beta2DeviceSelector]] = Field(default=None, description="Each selector must be satisfied by a device which is claimed via this class.")
    __properties: ClassVar[List[str]] = ["config", "selectors"]

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
        """Create an instance of V1beta2DeviceClassSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in config (list)
        _items = []
        if self.config:
            for _item_config in self.config:
                if _item_config:
                    _items.append(_item_config.to_dict())
            _dict['config'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in selectors (list)
        _items = []
        if self.selectors:
            for _item_selectors in self.selectors:
                if _item_selectors:
                    _items.append(_item_selectors.to_dict())
            _dict['selectors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1beta2DeviceClassSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "config": [V1beta2DeviceClassConfiguration.from_dict(_item) for _item in obj["config"]] if obj.get("config") is not None else None,
            "selectors": [V1beta2DeviceSelector.from_dict(_item) for _item in obj["selectors"]] if obj.get("selectors") is not None else None
        })
        return _obj


