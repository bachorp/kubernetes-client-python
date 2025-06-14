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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from kubernetes.client.models.v1_ingress_backend import V1IngressBackend
from kubernetes.client.models.v1_ingress_rule import V1IngressRule
from kubernetes.client.models.v1_ingress_tls import V1IngressTLS
from typing import Optional, Set
from typing_extensions import Self

class V1IngressSpec(BaseModel):
    """
    IngressSpec describes the Ingress the user wishes to exist.
    """ # noqa: E501
    default_backend: Optional[V1IngressBackend] = Field(default=None, alias="defaultBackend")
    ingress_class_name: Optional[StrictStr] = Field(default=None, description="ingressClassName is the name of an IngressClass cluster resource. Ingress controller implementations use this field to know whether they should be serving this Ingress resource, by a transitive connection (controller -> IngressClass -> Ingress resource). Although the `kubernetes.io/ingress.class` annotation (simple constant name) was never formally defined, it was widely supported by Ingress controllers to create a direct binding between Ingress controller and Ingress resources. Newly created Ingress resources should prefer using the field. However, even though the annotation is officially deprecated, for backwards compatibility reasons, ingress controllers should still honor that annotation if present.", alias="ingressClassName")
    rules: Optional[List[V1IngressRule]] = Field(default=None, description="rules is a list of host rules used to configure the Ingress. If unspecified, or no rule matches, all traffic is sent to the default backend.")
    tls: Optional[List[V1IngressTLS]] = Field(default=None, description="tls represents the TLS configuration. Currently the Ingress only supports a single TLS port, 443. If multiple members of this list specify different hosts, they will be multiplexed on the same port according to the hostname specified through the SNI TLS extension, if the ingress controller fulfilling the ingress supports SNI.")
    __properties: ClassVar[List[str]] = ["defaultBackend", "ingressClassName", "rules", "tls"]

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
        """Create an instance of V1IngressSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of default_backend
        if self.default_backend:
            _dict['defaultBackend'] = self.default_backend.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item_rules in self.rules:
                if _item_rules:
                    _items.append(_item_rules.to_dict())
            _dict['rules'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tls (list)
        _items = []
        if self.tls:
            for _item_tls in self.tls:
                if _item_tls:
                    _items.append(_item_tls.to_dict())
            _dict['tls'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1IngressSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "defaultBackend": V1IngressBackend.from_dict(obj["defaultBackend"]) if obj.get("defaultBackend") is not None else None,
            "ingressClassName": obj.get("ingressClassName"),
            "rules": [V1IngressRule.from_dict(_item) for _item in obj["rules"]] if obj.get("rules") is not None else None,
            "tls": [V1IngressTLS.from_dict(_item) for _item in obj["tls"]] if obj.get("tls") is not None else None
        })
        return _obj


