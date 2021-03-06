# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from avi.heat.avi_resource import AviNestedResource
from options import *

from options import *


class IpAddrRange(object):
    # all schemas
    begin_schema = properties.Schema(
        properties.Schema.MAP,
        _("Starting IP address of the range"),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=True,
    )
    end_schema = properties.Schema(
        properties.Schema.MAP,
        _("Ending IP address of the range"),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'begin',
        'end',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'begin': begin_schema,
        'end': end_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'begin': getattr(IpAddr, 'field_references', {}),
        'end': getattr(IpAddr, 'field_references', {}),
    }



class CustomParams(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    value_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    is_sensitive_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    is_dynamic_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'value',
        'is_sensitive',
        'is_dynamic',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'value': value_schema,
        'is_sensitive': is_sensitive_schema,
        'is_dynamic': is_dynamic_schema,
    }




class PortRange(object):
    # all schemas
    start_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("TCP/UDP port range start (inclusive)."),
        required=True,
        update_allowed=True,
    )
    end_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("TCP/UDP port range end (inclusive)."),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'start',
        'end',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'start': start_schema,
        'end': end_schema,
    }




class TenantConfiguration(object):
    # all schemas
    tenant_vrf_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("When 'Per Tenant IP Domain' is selected, each tenant gets its own routing domain that is not shared with any other tenant. When 'Share IP Domain across all tenants' is selected, all tenants share the same routing domain."),
        required=False,
        update_allowed=True,
    )
    se_in_provider_context_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Controls the ownership of ServiceEngines. Service Engines can either be exclusively owned by each tenant or owned by the administrator and shared by all tenants. When ServiceEngines are owned by the administrator, each tenant can have either read access or no access to their Service Engines."),
        required=False,
        update_allowed=True,
    )
    tenant_access_to_provider_se_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'tenant_vrf',
        'se_in_provider_context',
        'tenant_access_to_provider_se',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'tenant_vrf': tenant_vrf_schema,
        'se_in_provider_context': se_in_provider_context_schema,
        'tenant_access_to_provider_se': tenant_access_to_provider_se_schema,
    }




class Tag(object):
    # all schemas
    value_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['VCENTER_DEFINED', 'AVI_DEFINED', 'USER_DEFINED']),
        ],
    )

    # properties list
    PROPERTIES = (
        'value',
        'type',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'value': value_schema,
        'type': type_schema,
    }




class TimeStamp(object):
    # all schemas
    secs_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    usecs_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'secs',
        'usecs',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'secs': secs_schema,
        'usecs': usecs_schema,
    }




class IpAddrPort(object):
    # all schemas
    ip_schema = properties.Schema(
        properties.Schema.MAP,
        _("IP Address of host. One of IP address or hostname should be set"),
        schema=IpAddr.properties_schema,
        required=False,
        update_allowed=True,
    )
    port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Port number of server"),
        required=True,
        update_allowed=True,
    )
    hostname_schema = properties.Schema(
        properties.Schema.STRING,
        _("Hostname of server. One of IP address or hostname should be set"),
        required=False,
        update_allowed=True,
    )
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'ip',
        'port',
        'hostname',
        'name',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'ip': ip_schema,
        'port': port_schema,
        'hostname': hostname_schema,
        'name': name_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'ip': getattr(IpAddr, 'field_references', {}),
    }



class HTTPLocalFile(object):
    # all schemas
    content_type_schema = properties.Schema(
        properties.Schema.STRING,
        _("Mime-type of the content in the file."),
        required=True,
        update_allowed=True,
    )
    file_content_schema = properties.Schema(
        properties.Schema.STRING,
        _("File content to used in the local HTTP response body."),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'content_type',
        'file_content',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'content_type': content_type_schema,
        'file_content': file_content_schema,
    }


