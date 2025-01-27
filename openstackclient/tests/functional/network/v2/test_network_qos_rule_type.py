# Copyright (c) 2016, Intel Corporation.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from openstackclient.tests.functional.network.v2 import common


class NetworkQosRuleTypeTests(common.NetworkTests):
    """Functional tests for Network QoS rule type. """

    AVAILABLE_RULE_TYPES = ['dscp_marking',
                            'bandwidth_limit']

    def setUp(self):
        super(NetworkQosRuleTypeTests, self).setUp()
        # Nothing in this class works with Nova Network
        if not self.haz_network:
            self.skipTest("No Network service present")

    def test_qos_rule_type_list(self):
        cmd_output = self.openstack(
            'network qos rule type list -f json',
            parse_output=True,
        )
        for rule_type in self.AVAILABLE_RULE_TYPES:
            self.assertIn(rule_type, [x['Type'] for x in cmd_output])

    def test_qos_rule_type_details(self):
        for rule_type in self.AVAILABLE_RULE_TYPES:
            cmd_output = self.openstack(
                'network qos rule type show %s -f json' % rule_type,
                parse_output=True,
            )
            self.assertEqual(rule_type, cmd_output['rule_type_name'])
            self.assertIn("drivers", cmd_output.keys())
