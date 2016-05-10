
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import community_sets
import ext_community_sets
import as_path_sets
class bgp_defined_sets(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-routing-policy - based on the path /routing-policy/defined-sets/bgp-defined-sets. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: BGP-related set definitions for policy match conditions
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__community_sets','__ext_community_sets','__as_path_sets',)

  _yang_name = 'bgp-defined-sets'

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
    self.__ext_community_sets = YANGDynClass(base=ext_community_sets.ext_community_sets, is_container='container', yang_name="ext-community-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)
    self.__community_sets = YANGDynClass(base=community_sets.community_sets, is_container='container', yang_name="community-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)
    self.__as_path_sets = YANGDynClass(base=as_path_sets.as_path_sets, is_container='container', yang_name="as-path-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)

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
      return [u'routing-policy', u'defined-sets', u'bgp-defined-sets']

  def _get_community_sets(self):
    """
    Getter method for community_sets, mapped from YANG variable /routing_policy/defined_sets/bgp_defined_sets/community_sets (container)

    YANG Description: Enclosing container for list of defined BGP community sets
    """
    return self.__community_sets
      
  def _set_community_sets(self, v, load=False):
    """
    Setter method for community_sets, mapped from YANG variable /routing_policy/defined_sets/bgp_defined_sets/community_sets (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_community_sets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_community_sets() directly.

    YANG Description: Enclosing container for list of defined BGP community sets
    """
    try:
      t = YANGDynClass(v,base=community_sets.community_sets, is_container='container', yang_name="community-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """community_sets must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=community_sets.community_sets, is_container='container', yang_name="community-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)""",
        })

    self.__community_sets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_community_sets(self):
    self.__community_sets = YANGDynClass(base=community_sets.community_sets, is_container='container', yang_name="community-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)


  def _get_ext_community_sets(self):
    """
    Getter method for ext_community_sets, mapped from YANG variable /routing_policy/defined_sets/bgp_defined_sets/ext_community_sets (container)

    YANG Description: Enclosing container for list of extended BGP community
sets
    """
    return self.__ext_community_sets
      
  def _set_ext_community_sets(self, v, load=False):
    """
    Setter method for ext_community_sets, mapped from YANG variable /routing_policy/defined_sets/bgp_defined_sets/ext_community_sets (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ext_community_sets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ext_community_sets() directly.

    YANG Description: Enclosing container for list of extended BGP community
sets
    """
    try:
      t = YANGDynClass(v,base=ext_community_sets.ext_community_sets, is_container='container', yang_name="ext-community-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ext_community_sets must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ext_community_sets.ext_community_sets, is_container='container', yang_name="ext-community-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)""",
        })

    self.__ext_community_sets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ext_community_sets(self):
    self.__ext_community_sets = YANGDynClass(base=ext_community_sets.ext_community_sets, is_container='container', yang_name="ext-community-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)


  def _get_as_path_sets(self):
    """
    Getter method for as_path_sets, mapped from YANG variable /routing_policy/defined_sets/bgp_defined_sets/as_path_sets (container)

    YANG Description: Enclosing container for list of define AS path sets
    """
    return self.__as_path_sets
      
  def _set_as_path_sets(self, v, load=False):
    """
    Setter method for as_path_sets, mapped from YANG variable /routing_policy/defined_sets/bgp_defined_sets/as_path_sets (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_as_path_sets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_as_path_sets() directly.

    YANG Description: Enclosing container for list of define AS path sets
    """
    try:
      t = YANGDynClass(v,base=as_path_sets.as_path_sets, is_container='container', yang_name="as-path-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """as_path_sets must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=as_path_sets.as_path_sets, is_container='container', yang_name="as-path-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)""",
        })

    self.__as_path_sets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_as_path_sets(self):
    self.__as_path_sets = YANGDynClass(base=as_path_sets.as_path_sets, is_container='container', yang_name="as-path-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='container', is_config=True)

  community_sets = property(_get_community_sets, _set_community_sets)
  ext_community_sets = property(_get_ext_community_sets, _set_ext_community_sets)
  as_path_sets = property(_get_as_path_sets, _set_as_path_sets)


  _pyangbind_elements = {'community_sets': community_sets, 'ext_community_sets': ext_community_sets, 'as_path_sets': as_path_sets, }

