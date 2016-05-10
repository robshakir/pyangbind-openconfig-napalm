
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-routing-policy - based on the path /routing-policy/policy-definitions/policy-definition/statements/statement/conditions/bgp-conditions/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for BGP-specific policy
conditions
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__med_eq','__origin_eq','__next_hop_in','__afi_safi_in','__local_pref_eq','__route_type',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    helper = kwargs.pop("path_helper", None)
    if helper is False:
      self._path_helper = False
    elif helper is not None and isinstance(helper, xpathhelper.YANGPathHelper):
      self._path_helper = helper
    elif hasattr(self, "_parent"):
      helper = getattr(self._parent, "_path_helper", False)
      self._path_helper = helper
    else:
      self._path_helper = False

    self._extmethods = False
    self.__route_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INTERNAL': {}, u'EXTERNAL': {}},), is_leaf=True, yang_name="route-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='enumeration', is_config=False)
    self.__afi_safi_in = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'L3VPN_IPV6_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV4_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L2VPN_EVPN': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV6_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV4_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV6_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV4_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L2VPN_EVPN': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L2VPN_VPLS': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV6_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV4_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L2VPN_VPLS': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}},)), is_leaf=False, yang_name="afi-safi-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='identityref', is_config=False)
    self.__next_hop_in = YANGDynClass(base=TypedListType(allowed_type=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),]), is_leaf=False, yang_name="next-hop-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='inet:ip-address', is_config=False)
    self.__local_pref_eq = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local-pref-eq", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='uint32', is_config=False)
    self.__med_eq = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="med-eq", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='uint32', is_config=False)
    self.__origin_eq = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'EGP': {}, u'INCOMPLETE': {}, u'IGP': {}},), is_leaf=True, yang_name="origin-eq", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='oc-bgp-types:bgp-origin-attr-type', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'routing-policy', u'policy-definitions', u'policy-definition', u'statements', u'statement', u'conditions', u'bgp-conditions', u'state']

  def _get_med_eq(self):
    """
    Getter method for med_eq, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/bgp_conditions/state/med_eq (uint32)

    YANG Description: Condition to check if the received MED value is equal to
the specified value
    """
    return self.__med_eq
      
  def _set_med_eq(self, v, load=False):
    """
    Setter method for med_eq, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/bgp_conditions/state/med_eq (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_med_eq is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_med_eq() directly.

    YANG Description: Condition to check if the received MED value is equal to
the specified value
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="med-eq", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """med_eq must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="med-eq", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='uint32', is_config=False)""",
        })

    self.__med_eq = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_med_eq(self):
    self.__med_eq = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="med-eq", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='uint32', is_config=False)


  def _get_origin_eq(self):
    """
    Getter method for origin_eq, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/bgp_conditions/state/origin_eq (oc-bgp-types:bgp-origin-attr-type)

    YANG Description: Condition to check if the route origin is equal to the
specified value
    """
    return self.__origin_eq
      
  def _set_origin_eq(self, v, load=False):
    """
    Setter method for origin_eq, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/bgp_conditions/state/origin_eq (oc-bgp-types:bgp-origin-attr-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_origin_eq is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_origin_eq() directly.

    YANG Description: Condition to check if the route origin is equal to the
specified value
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'EGP': {}, u'INCOMPLETE': {}, u'IGP': {}},), is_leaf=True, yang_name="origin-eq", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='oc-bgp-types:bgp-origin-attr-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """origin_eq must be of a type compatible with oc-bgp-types:bgp-origin-attr-type""",
          'defined-type': "oc-bgp-types:bgp-origin-attr-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'EGP': {}, u'INCOMPLETE': {}, u'IGP': {}},), is_leaf=True, yang_name="origin-eq", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='oc-bgp-types:bgp-origin-attr-type', is_config=False)""",
        })

    self.__origin_eq = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_origin_eq(self):
    self.__origin_eq = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'EGP': {}, u'INCOMPLETE': {}, u'IGP': {}},), is_leaf=True, yang_name="origin-eq", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='oc-bgp-types:bgp-origin-attr-type', is_config=False)


  def _get_next_hop_in(self):
    """
    Getter method for next_hop_in, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/bgp_conditions/state/next_hop_in (inet:ip-address)

    YANG Description: List of next hop addresses to check for in the route
update
    """
    return self.__next_hop_in
      
  def _set_next_hop_in(self, v, load=False):
    """
    Setter method for next_hop_in, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/bgp_conditions/state/next_hop_in (inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_next_hop_in is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_next_hop_in() directly.

    YANG Description: List of next hop addresses to check for in the route
update
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),]), is_leaf=False, yang_name="next-hop-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='inet:ip-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """next_hop_in must be of a type compatible with inet:ip-address""",
          'defined-type': "inet:ip-address",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),]), is_leaf=False, yang_name="next-hop-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='inet:ip-address', is_config=False)""",
        })

    self.__next_hop_in = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_next_hop_in(self):
    self.__next_hop_in = YANGDynClass(base=TypedListType(allowed_type=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),]), is_leaf=False, yang_name="next-hop-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='inet:ip-address', is_config=False)


  def _get_afi_safi_in(self):
    """
    Getter method for afi_safi_in, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/bgp_conditions/state/afi_safi_in (identityref)

    YANG Description: List of address families which the NLRI may be
within
    """
    return self.__afi_safi_in
      
  def _set_afi_safi_in(self, v, load=False):
    """
    Setter method for afi_safi_in, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/bgp_conditions/state/afi_safi_in (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_afi_safi_in is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_afi_safi_in() directly.

    YANG Description: List of address families which the NLRI may be
within
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'L3VPN_IPV6_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV4_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L2VPN_EVPN': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV6_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV4_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV6_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV4_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L2VPN_EVPN': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L2VPN_VPLS': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV6_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV4_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L2VPN_VPLS': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}},)), is_leaf=False, yang_name="afi-safi-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='identityref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """afi_safi_in must be of a type compatible with identityref""",
          'defined-type': "openconfig-bgp-policy:identityref",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'L3VPN_IPV6_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV4_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L2VPN_EVPN': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV6_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV4_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV6_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV4_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L2VPN_EVPN': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L2VPN_VPLS': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV6_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV4_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L2VPN_VPLS': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}},)), is_leaf=False, yang_name="afi-safi-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='identityref', is_config=False)""",
        })

    self.__afi_safi_in = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_afi_safi_in(self):
    self.__afi_safi_in = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'L3VPN_IPV6_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV4_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L2VPN_EVPN': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV6_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV4_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV6_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L3VPN_IPV4_MULTICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L2VPN_EVPN': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:L2VPN_VPLS': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV6_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV4_LABELED_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'IPV4_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L2VPN_VPLS': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'L3VPN_IPV6_UNICAST': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}},)), is_leaf=False, yang_name="afi-safi-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='identityref', is_config=False)


  def _get_local_pref_eq(self):
    """
    Getter method for local_pref_eq, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/bgp_conditions/state/local_pref_eq (uint32)

    YANG Description: Condition to check if the local pref attribute is equal to
the specified value
    """
    return self.__local_pref_eq
      
  def _set_local_pref_eq(self, v, load=False):
    """
    Setter method for local_pref_eq, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/bgp_conditions/state/local_pref_eq (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_pref_eq is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_pref_eq() directly.

    YANG Description: Condition to check if the local pref attribute is equal to
the specified value
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local-pref-eq", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_pref_eq must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local-pref-eq", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='uint32', is_config=False)""",
        })

    self.__local_pref_eq = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_pref_eq(self):
    self.__local_pref_eq = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local-pref-eq", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='uint32', is_config=False)


  def _get_route_type(self):
    """
    Getter method for route_type, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/bgp_conditions/state/route_type (enumeration)

    YANG Description: Condition to check the route type in the route update
    """
    return self.__route_type
      
  def _set_route_type(self, v, load=False):
    """
    Setter method for route_type, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/bgp_conditions/state/route_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_type() directly.

    YANG Description: Condition to check the route type in the route update
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INTERNAL': {}, u'EXTERNAL': {}},), is_leaf=True, yang_name="route-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_type must be of a type compatible with enumeration""",
          'defined-type': "openconfig-bgp-policy:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INTERNAL': {}, u'EXTERNAL': {}},), is_leaf=True, yang_name="route-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='enumeration', is_config=False)""",
        })

    self.__route_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_type(self):
    self.__route_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INTERNAL': {}, u'EXTERNAL': {}},), is_leaf=True, yang_name="route-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='enumeration', is_config=False)

  med_eq = property(_get_med_eq)
  origin_eq = property(_get_origin_eq)
  next_hop_in = property(_get_next_hop_in)
  afi_safi_in = property(_get_afi_safi_in)
  local_pref_eq = property(_get_local_pref_eq)
  route_type = property(_get_route_type)


  _pyangbind_elements = {'med_eq': med_eq, 'origin_eq': origin_eq, 'next_hop_in': next_hop_in, 'afi_safi_in': afi_safi_in, 'local_pref_eq': local_pref_eq, 'route_type': route_type, }

