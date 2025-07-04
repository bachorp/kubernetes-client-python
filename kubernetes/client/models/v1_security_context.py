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
from kubernetes.client.models.v1_app_armor_profile import V1AppArmorProfile
from kubernetes.client.models.v1_capabilities import V1Capabilities
from kubernetes.client.models.v1_se_linux_options import V1SELinuxOptions
from kubernetes.client.models.v1_seccomp_profile import V1SeccompProfile
from kubernetes.client.models.v1_windows_security_context_options import V1WindowsSecurityContextOptions
from typing import Optional, Set
from typing_extensions import Self

class V1SecurityContext(BaseModel):
    """
    SecurityContext holds security configuration that will be applied to a container. Some fields are present in both SecurityContext and PodSecurityContext.  When both are set, the values in SecurityContext take precedence.
    """ # noqa: E501
    allow_privilege_escalation: Optional[StrictBool] = Field(default=None, description="AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN Note that this field cannot be set when spec.os.name is windows.", alias="allowPrivilegeEscalation")
    app_armor_profile: Optional[V1AppArmorProfile] = Field(default=None, alias="appArmorProfile")
    capabilities: Optional[V1Capabilities] = None
    privileged: Optional[StrictBool] = Field(default=None, description="Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. Note that this field cannot be set when spec.os.name is windows.")
    proc_mount: Optional[StrictStr] = Field(default=None, description="procMount denotes the type of proc mount to use for the containers. The default value is Default which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled. Note that this field cannot be set when spec.os.name is windows.", alias="procMount")
    read_only_root_filesystem: Optional[StrictBool] = Field(default=None, description="Whether this container has a read-only root filesystem. Default is false. Note that this field cannot be set when spec.os.name is windows.", alias="readOnlyRootFilesystem")
    run_as_group: Optional[StrictInt] = Field(default=None, description="The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.", alias="runAsGroup")
    run_as_non_root: Optional[StrictBool] = Field(default=None, description="Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.", alias="runAsNonRoot")
    run_as_user: Optional[StrictInt] = Field(default=None, description="The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.", alias="runAsUser")
    se_linux_options: Optional[V1SELinuxOptions] = Field(default=None, alias="seLinuxOptions")
    seccomp_profile: Optional[V1SeccompProfile] = Field(default=None, alias="seccompProfile")
    windows_options: Optional[V1WindowsSecurityContextOptions] = Field(default=None, alias="windowsOptions")
    __properties: ClassVar[List[str]] = ["allowPrivilegeEscalation", "appArmorProfile", "capabilities", "privileged", "procMount", "readOnlyRootFilesystem", "runAsGroup", "runAsNonRoot", "runAsUser", "seLinuxOptions", "seccompProfile", "windowsOptions"]

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
        """Create an instance of V1SecurityContext from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of app_armor_profile
        if self.app_armor_profile:
            _dict['appArmorProfile'] = self.app_armor_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of capabilities
        if self.capabilities:
            _dict['capabilities'] = self.capabilities.to_dict()
        # override the default output from pydantic by calling `to_dict()` of se_linux_options
        if self.se_linux_options:
            _dict['seLinuxOptions'] = self.se_linux_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of seccomp_profile
        if self.seccomp_profile:
            _dict['seccompProfile'] = self.seccomp_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of windows_options
        if self.windows_options:
            _dict['windowsOptions'] = self.windows_options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1SecurityContext from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowPrivilegeEscalation": obj.get("allowPrivilegeEscalation"),
            "appArmorProfile": V1AppArmorProfile.from_dict(obj["appArmorProfile"]) if obj.get("appArmorProfile") is not None else None,
            "capabilities": V1Capabilities.from_dict(obj["capabilities"]) if obj.get("capabilities") is not None else None,
            "privileged": obj.get("privileged"),
            "procMount": obj.get("procMount"),
            "readOnlyRootFilesystem": obj.get("readOnlyRootFilesystem"),
            "runAsGroup": obj.get("runAsGroup"),
            "runAsNonRoot": obj.get("runAsNonRoot"),
            "runAsUser": obj.get("runAsUser"),
            "seLinuxOptions": V1SELinuxOptions.from_dict(obj["seLinuxOptions"]) if obj.get("seLinuxOptions") is not None else None,
            "seccompProfile": V1SeccompProfile.from_dict(obj["seccompProfile"]) if obj.get("seccompProfile") is not None else None,
            "windowsOptions": V1WindowsSecurityContextOptions.from_dict(obj["windowsOptions"]) if obj.get("windowsOptions") is not None else None
        })
        return _obj


