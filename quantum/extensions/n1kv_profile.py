# Copyright (c) 2012 OpenStack, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from quantum.api.v2 import attributes

PROFILE_ID = 'n1kv:profile_id'
MULTICAST_IP = 'n1kv:multicast_ip'

EXTENDED_ATTRIBUTES_2_0 = {
    'networks': {
        PROFILE_ID: {'allow_post': True, 'allow_put': True,
                       'validate': {'type:regex': attributes.UUID_PATTERN},
                       'default': attributes.ATTR_NOT_SPECIFIED,
                       'is_visible': True},
        MULTICAST_IP: {'allow_post': True, 'allow_put': True,
                       'default': attributes.ATTR_NOT_SPECIFIED,
                       'is_visible': True},
    },
    'ports': {
        PROFILE_ID: {'allow_post': True, 'allow_put': True,
                       'validate': {'type:regex': attributes.UUID_PATTERN},
                       'default': attributes.ATTR_NOT_SPECIFIED,
                       'is_visible': True}
    }
}


class N1KvProfile(object):
    """Extension class supporting provider networks.

    This class is used by quantum's extension framework to make
    metadata about the n1kv profile extension available to
    clients. No new resources are defined by this extension. Instead,
    the existing network resource's request and response messages are
    extended with attributes in the n1kv profile namespace.

    To create a network based on n1kv profile using the CLI with admin rights:

       (shell) net-create --tenant_id <tenant-id> <net-name> \
       --n1kv:profile_id id
       (shell) port-create --tenant_id <tenant-id> <net-name> \
       --n1kv:profile_id id


    With admin rights, network dictionaries returned from CLI commands
    will also include n1kv profile attributes.
    """

    @classmethod
    def get_name(cls):
        return "n1kv_profile"

    @classmethod
    def get_alias(cls):
        return "n1kv_profile"

    @classmethod
    def get_description(cls):
        return "Expose network profile"

    @classmethod
    def get_namespace(cls):
        return "http://docs.openstack.org/ext/n1kv_profile/api/v1.0"

    @classmethod
    def get_updated(cls):
        return "2012-11-15T10:00:00-00:00"

    def get_extended_resources(self, version):
        if version == "2.0":
            return EXTENDED_ATTRIBUTES_2_0
        else:
            return {}