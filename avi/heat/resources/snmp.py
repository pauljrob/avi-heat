# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from options import *

from options import *


class SnmpTrapServer(object):
    # all schemas
    ip_addr_schema = properties.Schema(
        properties.Schema.MAP,
        _("IP Address of the SNMP trap destination"),
        schema=IpAddr.properties_schema,
        required=True,
    )
    community_schema = properties.Schema(
        properties.Schema.STRING,
        _("The community string to communicate with the trap server."),
        required=True,
    )

    # properties list
    PROPERTIES = (
        'ip_addr',
        'community',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'ip_addr': ip_addr_schema,
        'community': community_schema,
    }


class SnmpConfiguration(object):
    # all schemas
    community_schema = properties.Schema(
        properties.Schema.STRING,
        _("Community string for SNMP v2c"),
        required=True,
    )

    # properties list
    PROPERTIES = (
        'community',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'community': community_schema,
    }


class SnmpTrapProfile(AviResource):
    resource_name = "snmptrapprofile"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("A user-friendly name of the SNMP trap configuration."),
        required=True,
    )
    trap_servers_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=SnmpTrapServer.properties_schema,
        required=True,
    )
    trap_servers_schema = properties.Schema(
        properties.Schema.LIST,
        _("The IP address or hostname of the SNMP trap destination server."),
        schema=trap_servers_item_schema,
        required=False,
    )

    # properties list
    PROPERTIES = (
        'name',
        'trap_servers',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'trap_servers': trap_servers_schema,
    }


def resource_mapping():
    return {
        'Avi::SnmpTrapProfile': SnmpTrapProfile,
    }
