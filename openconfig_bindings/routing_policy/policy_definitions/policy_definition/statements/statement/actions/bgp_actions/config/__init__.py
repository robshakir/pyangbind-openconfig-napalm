
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-routing-policy - based on the path /routing-policy/policy-definitions/policy-definition/statements/statement/actions/bgp-actions/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for BGP-specific actions
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__set_route_origin','__set_local_pref','__set_next_hop','__set_med',)

  _yang_name = 'config'

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
    self.__set_med = YANGDynClass(base=[RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^[+-][0-9]+'}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'IGP': {}},),], is_leaf=True, yang_name="set-med", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='bgp-set-med-type', is_config=True)
    self.__set_next_hop = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'SELF': {}},),], is_leaf=True, yang_name="set-next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='bgp-next-hop-type', is_config=True)
    self.__set_local_pref = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="set-local-pref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='uint32', is_config=True)
    self.__set_route_origin = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'EGP': {}, u'INCOMPLETE': {}, u'IGP': {}},), is_leaf=True, yang_name="set-route-origin", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='oc-bgp-types:bgp-origin-attr-type', is_config=True)

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
      return [u'routing-policy', u'policy-definitions', u'policy-definition', u'statements', u'statement', u'actions', u'bgp-actions', u'config']

  def _get_set_route_origin(self):
    """
    Getter method for set_route_origin, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/config/set_route_origin (oc-bgp-types:bgp-origin-attr-type)

    YANG Description: set the origin attribute to the specified
value
    """
    return self.__set_route_origin
      
  def _set_set_route_origin(self, v, load=False):
    """
    Setter method for set_route_origin, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/config/set_route_origin (oc-bgp-types:bgp-origin-attr-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_route_origin is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_route_origin() directly.

    YANG Description: set the origin attribute to the specified
value
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'EGP': {}, u'INCOMPLETE': {}, u'IGP': {}},), is_leaf=True, yang_name="set-route-origin", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='oc-bgp-types:bgp-origin-attr-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_route_origin must be of a type compatible with oc-bgp-types:bgp-origin-attr-type""",
          'defined-type': "oc-bgp-types:bgp-origin-attr-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'EGP': {}, u'INCOMPLETE': {}, u'IGP': {}},), is_leaf=True, yang_name="set-route-origin", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='oc-bgp-types:bgp-origin-attr-type', is_config=True)""",
        })

    self.__set_route_origin = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_route_origin(self):
    self.__set_route_origin = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'EGP': {}, u'INCOMPLETE': {}, u'IGP': {}},), is_leaf=True, yang_name="set-route-origin", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='oc-bgp-types:bgp-origin-attr-type', is_config=True)


  def _get_set_local_pref(self):
    """
    Getter method for set_local_pref, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/config/set_local_pref (uint32)

    YANG Description: set the local pref attribute on the route
update
    """
    return self.__set_local_pref
      
  def _set_set_local_pref(self, v, load=False):
    """
    Setter method for set_local_pref, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/config/set_local_pref (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_local_pref is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_local_pref() directly.

    YANG Description: set the local pref attribute on the route
update
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="set-local-pref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_local_pref must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="set-local-pref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='uint32', is_config=True)""",
        })

    self.__set_local_pref = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_local_pref(self):
    self.__set_local_pref = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="set-local-pref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='uint32', is_config=True)


  def _get_set_next_hop(self):
    """
    Getter method for set_next_hop, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/config/set_next_hop (bgp-next-hop-type)

    YANG Description: set the next-hop attribute in the route update
    """
    return self.__set_next_hop
      
  def _set_set_next_hop(self, v, load=False):
    """
    Setter method for set_next_hop, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/config/set_next_hop (bgp-next-hop-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_next_hop is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_next_hop() directly.

    YANG Description: set the next-hop attribute in the route update
    """
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'SELF': {}},),], is_leaf=True, yang_name="set-next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='bgp-next-hop-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_next_hop must be of a type compatible with bgp-next-hop-type""",
          'defined-type': "openconfig-bgp-policy:bgp-next-hop-type",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'SELF': {}},),], is_leaf=True, yang_name="set-next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='bgp-next-hop-type', is_config=True)""",
        })

    self.__set_next_hop = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_next_hop(self):
    self.__set_next_hop = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'SELF': {}},),], is_leaf=True, yang_name="set-next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='bgp-next-hop-type', is_config=True)


  def _get_set_med(self):
    """
    Getter method for set_med, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/config/set_med (bgp-set-med-type)

    YANG Description: set the med metric attribute in the route
update
    """
    return self.__set_med
      
  def _set_set_med(self, v, load=False):
    """
    Setter method for set_med, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/bgp_actions/config/set_med (bgp-set-med-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_med is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_med() directly.

    YANG Description: set the med metric attribute in the route
update
    """
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^[+-][0-9]+'}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'IGP': {}},),], is_leaf=True, yang_name="set-med", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='bgp-set-med-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_med must be of a type compatible with bgp-set-med-type""",
          'defined-type': "openconfig-bgp-policy:bgp-set-med-type",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^[+-][0-9]+'}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'IGP': {}},),], is_leaf=True, yang_name="set-med", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='bgp-set-med-type', is_config=True)""",
        })

    self.__set_med = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_med(self):
    self.__set_med = YANGDynClass(base=[RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^[+-][0-9]+'}),RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'IGP': {}},),], is_leaf=True, yang_name="set-med", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='bgp-set-med-type', is_config=True)

  set_route_origin = property(_get_set_route_origin, _set_set_route_origin)
  set_local_pref = property(_get_set_local_pref, _set_set_local_pref)
  set_next_hop = property(_get_set_next_hop, _set_set_next_hop)
  set_med = property(_get_set_med, _set_set_med)


  _pyangbind_elements = {'set_route_origin': set_route_origin, 'set_local_pref': set_local_pref, 'set_next_hop': set_next_hop, 'set_med': set_med, }

