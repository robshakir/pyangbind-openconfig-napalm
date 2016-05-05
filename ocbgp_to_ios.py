#!/usr/bin/env python

from __future__ import unicode_literals, print_function
import os
import sys
import pyangbind.lib.pybindJSON as pbJ
from pyangbind.lib.xpathhelper import YANGPathHelper
sys.path.append(os.path.realpath(os.path.join(__file__, "..", "..")))
import openconfig_bindings
import jinja2
from bitarray import bitarray

def isdefault(o):
  if not o._changed() and not o.default():
    return True
  if o == o.default():
    return True
  return False

def openconfig_to_cisco_af(value):
  if ":" in value:
    value = value.split(":")[1]

  mapd = {
    'IPV4_UNICAST':               "ipv4 unicast",
    'IPV6_UNICAST':               "ipv6 unicast",
    'IPV4_LABELED_UNICAST':       "ipv4 unicast",
    'IPV6_LABELED_UNICAST':       "ipv6 unicast",
    'L3VPN_IPV4_UNICAST':         "vpnv4",
    'L3VPN_IPV6_UNICAST':         "vpnv6",
  }
  return mapd[value]

yph = YANGPathHelper()

example_file_path = os.path.realpath(os.path.join(__file__, "..", "examples", "bgp_global.json"))
ocbgp = pbJ.load_ietf(example_file_path, openconfig_bindings, 'openconfig_bgp', path_helper=yph)

this_dir = os.path.dirname(os.path.realpath(__file__))
tenv = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(this_dir, "templates")), trim_blocks=True, lstrip_blocks=True)

tenv.filters['to_cisco_address_family'] = openconfig_to_cisco_af
tenv.filters['isdefault'] = isdefault

t = tenv.get_template('cisco-ios-xe-bgp.tmpl')
print(t.render(instance=ocbgp.bgp))