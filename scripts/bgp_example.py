#!/usr/bin/env python

from __future__ import unicode_literals, print_function
import os
import sys
sys.path.append(os.path.realpath(os.path.join(__file__, "..", "..")))
import openconfig_bindings
from pyangbind.lib.xpathhelper import YANGPathHelper
import pyangbind.lib.pybindJSON as pbJ

# An XPATH helper object which helps us track XPATH references
# in the OpenConfig Models
yph = YANGPathHelper()

ocbgp = openconfig_bindings.openconfig_bgp(path_helper=yph)
ocbgp.bgp.global_.config.as_ = 6643
ocbgp.bgp.global_.config.router_id = "192.0.2.1"

ipv4_unicast = ocbgp.bgp.global_.afi_safis.afi_safi.add("IPV4_UNICAST")
ipv4_unicast.config.enabled = True
ipv4_unicast.use_multiple_paths.ebgp.config.maximum_paths = 8

ipv6_unicast = ocbgp.bgp.global_.afi_safis.afi_safi.add("IPV6_UNICAST")
ipv6_unicast.config.enabled = True
ipv6_unicast.use_multiple_paths.ebgp.config.maximum_paths = 8

neighbor = ocbgp.bgp.neighbors.neighbor.add("192.0.2.2")
neighbor.config.peer_as = 54113
neighbor.config.description = ":a=54413:d=Fastly:"
ipv4 = neighbor.afi_safis.afi_safi.add("IPV4_UNICAST")
ipv4.config.enabled = True
ipv6_lu = neighbor.afi_safis.afi_safi.add("IPV6_LABELED_UNICAST")
ipv6_lu.config.enabled = True

neighbor_two = ocbgp.bgp.neighbors.neighbor.add("2001:db8::1")
neighbor_two.config.peer_as = 6643
neighbor_two.config.description = ":a=6643:d=Jive:"
ipv6 = neighbor_two.afi_safis.afi_safi.add("IPV6_UNICAST")
ipv6.config.enabled=  True
neighbor_two.ebgp_multihop.config.enabled = True
neighbor_two.ebgp_multihop.config.multihop_ttl = 255

pbJ.dump(ocbgp, os.path.realpath(os.path.join(__file__, "..", "..", "examples", "bgp_global.json")), mode="ietf")

