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
from kubernetes.client.models.v1_group_subject import V1GroupSubject
from kubernetes.client.models.v1_service_account_subject import V1ServiceAccountSubject
from kubernetes.client.models.v1_user_subject import V1UserSubject
from typing import Optional, Set
from typing_extensions import Self

class FlowcontrolV1Subject(BaseModel):
    """
    Subject matches the originator of a request, as identified by the request authentication system. There are three ways of matching an originator; by user, group, or service account.
    """ # noqa: E501
    group: Optional[V1GroupSubject] = None
    kind: StrictStr = Field(description="`kind` indicates which one of the other fields is non-empty. Required")
    service_account: Optional[V1ServiceAccountSubject] = Field(default=None, alias="serviceAccount")
    user: Optional[V1UserSubject] = None
    __properties: ClassVar[List[str]] = ["group", "kind", "serviceAccount", "user"]

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
        """Create an instance of FlowcontrolV1Subject from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of group
        if self.group:
            _dict['group'] = self.group.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service_account
        if self.service_account:
            _dict['serviceAccount'] = self.service_account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FlowcontrolV1Subject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "group": V1GroupSubject.from_dict(obj["group"]) if obj.get("group") is not None else None,
            "kind": obj.get("kind"),
            "serviceAccount": V1ServiceAccountSubject.from_dict(obj["serviceAccount"]) if obj.get("serviceAccount") is not None else None,
            "user": V1UserSubject.from_dict(obj["user"]) if obj.get("user") is not None else None
        })
        return _obj


