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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class V1CertificateSigningRequestSpec(BaseModel):
    """
    CertificateSigningRequestSpec contains the certificate request.
    """ # noqa: E501
    expiration_seconds: Optional[StrictInt] = Field(default=None, description="expirationSeconds is the requested duration of validity of the issued certificate. The certificate signer may issue a certificate with a different validity duration so a client must check the delta between the notBefore and and notAfter fields in the issued certificate to determine the actual duration.  The v1.22+ in-tree implementations of the well-known Kubernetes signers will honor this field as long as the requested duration is not greater than the maximum duration they will honor per the --cluster-signing-duration CLI flag to the Kubernetes controller manager.  Certificate signers may not honor this field for various reasons:    1. Old signer that is unaware of the field (such as the in-tree      implementations prior to v1.22)   2. Signer whose configured maximum is shorter than the requested duration   3. Signer whose configured minimum is longer than the requested duration  The minimum valid value for expirationSeconds is 600, i.e. 10 minutes.", alias="expirationSeconds")
    extra: Optional[Dict[str, List[StrictStr]]] = Field(default=None, description="extra contains extra attributes of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.")
    groups: Optional[List[StrictStr]] = Field(default=None, description="groups contains group membership of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.")
    request: Union[Annotated[bytes, Field(strict=True)], Annotated[str, Field(strict=True)]] = Field(description="request contains an x509 certificate signing request encoded in a \"CERTIFICATE REQUEST\" PEM block. When serialized as JSON or YAML, the data is additionally base64-encoded.")
    signer_name: StrictStr = Field(description="signerName indicates the requested signer, and is a qualified name.  List/watch requests for CertificateSigningRequests can filter on this field using a \"spec.signerName=NAME\" fieldSelector.  Well-known Kubernetes signers are:  1. \"kubernetes.io/kube-apiserver-client\": issues client certificates that can be used to authenticate to kube-apiserver.   Requests for this signer are never auto-approved by kube-controller-manager, can be issued by the \"csrsigning\" controller in kube-controller-manager.  2. \"kubernetes.io/kube-apiserver-client-kubelet\": issues client certificates that kubelets use to authenticate to kube-apiserver.   Requests for this signer can be auto-approved by the \"csrapproving\" controller in kube-controller-manager, and can be issued by the \"csrsigning\" controller in kube-controller-manager.  3. \"kubernetes.io/kubelet-serving\" issues serving certificates that kubelets use to serve TLS endpoints, which kube-apiserver can connect to securely.   Requests for this signer are never auto-approved by kube-controller-manager, and can be issued by the \"csrsigning\" controller in kube-controller-manager.  More details are available at https://k8s.io/docs/reference/access-authn-authz/certificate-signing-requests/#kubernetes-signers  Custom signerNames can also be specified. The signer defines:  1. Trust distribution: how trust (CA bundles) are distributed.  2. Permitted subjects: and behavior when a disallowed subject is requested.  3. Required, permitted, or forbidden x509 extensions in the request (including whether subjectAltNames are allowed, which types, restrictions on allowed values) and behavior when a disallowed extension is requested.  4. Required, permitted, or forbidden key usages / extended key usages.  5. Expiration/certificate lifetime: whether it is fixed by the signer, configurable by the admin.  6. Whether or not requests for CA certificates are allowed.", alias="signerName")
    uid: Optional[StrictStr] = Field(default=None, description="uid contains the uid of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.")
    usages: Optional[List[StrictStr]] = Field(default=None, description="usages specifies a set of key usages requested in the issued certificate.  Requests for TLS client certificates typically request: \"digital signature\", \"key encipherment\", \"client auth\".  Requests for TLS serving certificates typically request: \"key encipherment\", \"digital signature\", \"server auth\".  Valid values are:  \"signing\", \"digital signature\", \"content commitment\",  \"key encipherment\", \"key agreement\", \"data encipherment\",  \"cert sign\", \"crl sign\", \"encipher only\", \"decipher only\", \"any\",  \"server auth\", \"client auth\",  \"code signing\", \"email protection\", \"s/mime\",  \"ipsec end system\", \"ipsec tunnel\", \"ipsec user\",  \"timestamping\", \"ocsp signing\", \"microsoft sgc\", \"netscape sgc\"")
    username: Optional[StrictStr] = Field(default=None, description="username contains the name of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.")
    __properties: ClassVar[List[str]] = ["expirationSeconds", "extra", "groups", "request", "signerName", "uid", "usages", "username"]

    @field_validator('request')
    def request_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$", value):
            raise ValueError(r"must validate the regular expression /^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/")
        return value

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
        """Create an instance of V1CertificateSigningRequestSpec from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1CertificateSigningRequestSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "expirationSeconds": obj.get("expirationSeconds"),
            "extra": obj.get("extra"),
            "groups": obj.get("groups"),
            "request": obj.get("request"),
            "signerName": obj.get("signerName"),
            "uid": obj.get("uid"),
            "usages": obj.get("usages"),
            "username": obj.get("username")
        })
        return _obj


