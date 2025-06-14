# flake8: noqa

from typing import TYPE_CHECKING

from lazy_imports import LazyModule, as_package, load


if TYPE_CHECKING:
    # import apis into api package
    from kubernetes.client.api.well_known_api import WellKnownApi
    from kubernetes.client.api.admissionregistration_api import AdmissionregistrationApi
    from kubernetes.client.api.admissionregistration_v1_api import AdmissionregistrationV1Api
    from kubernetes.client.api.admissionregistration_v1alpha1_api import AdmissionregistrationV1alpha1Api
    from kubernetes.client.api.admissionregistration_v1beta1_api import AdmissionregistrationV1beta1Api
    from kubernetes.client.api.apiextensions_api import ApiextensionsApi
    from kubernetes.client.api.apiextensions_v1_api import ApiextensionsV1Api
    from kubernetes.client.api.apiregistration_api import ApiregistrationApi
    from kubernetes.client.api.apiregistration_v1_api import ApiregistrationV1Api
    from kubernetes.client.api.apis_api import ApisApi
    from kubernetes.client.api.apps_api import AppsApi
    from kubernetes.client.api.apps_v1_api import AppsV1Api
    from kubernetes.client.api.authentication_api import AuthenticationApi
    from kubernetes.client.api.authentication_v1_api import AuthenticationV1Api
    from kubernetes.client.api.authorization_api import AuthorizationApi
    from kubernetes.client.api.authorization_v1_api import AuthorizationV1Api
    from kubernetes.client.api.autoscaling_api import AutoscalingApi
    from kubernetes.client.api.autoscaling_v1_api import AutoscalingV1Api
    from kubernetes.client.api.autoscaling_v2_api import AutoscalingV2Api
    from kubernetes.client.api.batch_api import BatchApi
    from kubernetes.client.api.batch_v1_api import BatchV1Api
    from kubernetes.client.api.certificates_api import CertificatesApi
    from kubernetes.client.api.certificates_v1_api import CertificatesV1Api
    from kubernetes.client.api.certificates_v1alpha1_api import CertificatesV1alpha1Api
    from kubernetes.client.api.certificates_v1beta1_api import CertificatesV1beta1Api
    from kubernetes.client.api.coordination_api import CoordinationApi
    from kubernetes.client.api.coordination_v1_api import CoordinationV1Api
    from kubernetes.client.api.coordination_v1alpha2_api import CoordinationV1alpha2Api
    from kubernetes.client.api.coordination_v1beta1_api import CoordinationV1beta1Api
    from kubernetes.client.api.core_api import CoreApi
    from kubernetes.client.api.core_v1_api import CoreV1Api
    from kubernetes.client.api.custom_objects_api import CustomObjectsApi
    from kubernetes.client.api.discovery_api import DiscoveryApi
    from kubernetes.client.api.discovery_v1_api import DiscoveryV1Api
    from kubernetes.client.api.events_api import EventsApi
    from kubernetes.client.api.events_v1_api import EventsV1Api
    from kubernetes.client.api.flowcontrol_apiserver_api import FlowcontrolApiserverApi
    from kubernetes.client.api.flowcontrol_apiserver_v1_api import FlowcontrolApiserverV1Api
    from kubernetes.client.api.internal_apiserver_api import InternalApiserverApi
    from kubernetes.client.api.internal_apiserver_v1alpha1_api import InternalApiserverV1alpha1Api
    from kubernetes.client.api.logs_api import LogsApi
    from kubernetes.client.api.networking_api import NetworkingApi
    from kubernetes.client.api.networking_v1_api import NetworkingV1Api
    from kubernetes.client.api.networking_v1beta1_api import NetworkingV1beta1Api
    from kubernetes.client.api.node_api import NodeApi
    from kubernetes.client.api.node_v1_api import NodeV1Api
    from kubernetes.client.api.openid_api import OpenidApi
    from kubernetes.client.api.policy_api import PolicyApi
    from kubernetes.client.api.policy_v1_api import PolicyV1Api
    from kubernetes.client.api.rbac_authorization_api import RbacAuthorizationApi
    from kubernetes.client.api.rbac_authorization_v1_api import RbacAuthorizationV1Api
    from kubernetes.client.api.resource_api import ResourceApi
    from kubernetes.client.api.resource_v1alpha3_api import ResourceV1alpha3Api
    from kubernetes.client.api.resource_v1beta1_api import ResourceV1beta1Api
    from kubernetes.client.api.resource_v1beta2_api import ResourceV1beta2Api
    from kubernetes.client.api.scheduling_api import SchedulingApi
    from kubernetes.client.api.scheduling_v1_api import SchedulingV1Api
    from kubernetes.client.api.storage_api import StorageApi
    from kubernetes.client.api.storage_v1_api import StorageV1Api
    from kubernetes.client.api.storage_v1alpha1_api import StorageV1alpha1Api
    from kubernetes.client.api.storage_v1beta1_api import StorageV1beta1Api
    from kubernetes.client.api.storagemigration_api import StoragemigrationApi
    from kubernetes.client.api.storagemigration_v1alpha1_api import StoragemigrationV1alpha1Api
    from kubernetes.client.api.version_api import VersionApi
    
else:
    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from kubernetes.client.api.well_known_api import WellKnownApi
from kubernetes.client.api.admissionregistration_api import AdmissionregistrationApi
from kubernetes.client.api.admissionregistration_v1_api import AdmissionregistrationV1Api
from kubernetes.client.api.admissionregistration_v1alpha1_api import AdmissionregistrationV1alpha1Api
from kubernetes.client.api.admissionregistration_v1beta1_api import AdmissionregistrationV1beta1Api
from kubernetes.client.api.apiextensions_api import ApiextensionsApi
from kubernetes.client.api.apiextensions_v1_api import ApiextensionsV1Api
from kubernetes.client.api.apiregistration_api import ApiregistrationApi
from kubernetes.client.api.apiregistration_v1_api import ApiregistrationV1Api
from kubernetes.client.api.apis_api import ApisApi
from kubernetes.client.api.apps_api import AppsApi
from kubernetes.client.api.apps_v1_api import AppsV1Api
from kubernetes.client.api.authentication_api import AuthenticationApi
from kubernetes.client.api.authentication_v1_api import AuthenticationV1Api
from kubernetes.client.api.authorization_api import AuthorizationApi
from kubernetes.client.api.authorization_v1_api import AuthorizationV1Api
from kubernetes.client.api.autoscaling_api import AutoscalingApi
from kubernetes.client.api.autoscaling_v1_api import AutoscalingV1Api
from kubernetes.client.api.autoscaling_v2_api import AutoscalingV2Api
from kubernetes.client.api.batch_api import BatchApi
from kubernetes.client.api.batch_v1_api import BatchV1Api
from kubernetes.client.api.certificates_api import CertificatesApi
from kubernetes.client.api.certificates_v1_api import CertificatesV1Api
from kubernetes.client.api.certificates_v1alpha1_api import CertificatesV1alpha1Api
from kubernetes.client.api.certificates_v1beta1_api import CertificatesV1beta1Api
from kubernetes.client.api.coordination_api import CoordinationApi
from kubernetes.client.api.coordination_v1_api import CoordinationV1Api
from kubernetes.client.api.coordination_v1alpha2_api import CoordinationV1alpha2Api
from kubernetes.client.api.coordination_v1beta1_api import CoordinationV1beta1Api
from kubernetes.client.api.core_api import CoreApi
from kubernetes.client.api.core_v1_api import CoreV1Api
from kubernetes.client.api.custom_objects_api import CustomObjectsApi
from kubernetes.client.api.discovery_api import DiscoveryApi
from kubernetes.client.api.discovery_v1_api import DiscoveryV1Api
from kubernetes.client.api.events_api import EventsApi
from kubernetes.client.api.events_v1_api import EventsV1Api
from kubernetes.client.api.flowcontrol_apiserver_api import FlowcontrolApiserverApi
from kubernetes.client.api.flowcontrol_apiserver_v1_api import FlowcontrolApiserverV1Api
from kubernetes.client.api.internal_apiserver_api import InternalApiserverApi
from kubernetes.client.api.internal_apiserver_v1alpha1_api import InternalApiserverV1alpha1Api
from kubernetes.client.api.logs_api import LogsApi
from kubernetes.client.api.networking_api import NetworkingApi
from kubernetes.client.api.networking_v1_api import NetworkingV1Api
from kubernetes.client.api.networking_v1beta1_api import NetworkingV1beta1Api
from kubernetes.client.api.node_api import NodeApi
from kubernetes.client.api.node_v1_api import NodeV1Api
from kubernetes.client.api.openid_api import OpenidApi
from kubernetes.client.api.policy_api import PolicyApi
from kubernetes.client.api.policy_v1_api import PolicyV1Api
from kubernetes.client.api.rbac_authorization_api import RbacAuthorizationApi
from kubernetes.client.api.rbac_authorization_v1_api import RbacAuthorizationV1Api
from kubernetes.client.api.resource_api import ResourceApi
from kubernetes.client.api.resource_v1alpha3_api import ResourceV1alpha3Api
from kubernetes.client.api.resource_v1beta1_api import ResourceV1beta1Api
from kubernetes.client.api.resource_v1beta2_api import ResourceV1beta2Api
from kubernetes.client.api.scheduling_api import SchedulingApi
from kubernetes.client.api.scheduling_v1_api import SchedulingV1Api
from kubernetes.client.api.storage_api import StorageApi
from kubernetes.client.api.storage_v1_api import StorageV1Api
from kubernetes.client.api.storage_v1alpha1_api import StorageV1alpha1Api
from kubernetes.client.api.storage_v1beta1_api import StorageV1beta1Api
from kubernetes.client.api.storagemigration_api import StoragemigrationApi
from kubernetes.client.api.storagemigration_v1alpha1_api import StoragemigrationV1alpha1Api
from kubernetes.client.api.version_api import VersionApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
