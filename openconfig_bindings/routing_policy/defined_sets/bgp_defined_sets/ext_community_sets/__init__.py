
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import ext_community_set
class ext_community_sets(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-routing-policy - based on the path /routing-policy/defined-sets/bgp-defined-sets/ext-community-sets. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for list of extended BGP community
sets
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__ext_community_set',)

  _yang_name = 'ext-community-sets'

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
    self.__ext_community_set = YANGDynClass(base=YANGListType("ext_community_set_name",ext_community_set.ext_community_set, yang_name="ext-community-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ext-community-set-name'), is_container='list', yang_name="ext-community-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='list', is_config=True)

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
      return [u'routing-policy', u'defined-sets', u'bgp-defined-sets', u'ext-community-sets']

  def _get_ext_community_set(self):
    """
    Getter method for ext_community_set, mapped from YANG variable /routing_policy/defined_sets/bgp_defined_sets/ext_community_sets/ext_community_set (list)

    YANG Description: List of defined extended BGP community sets
    """
    return self.__ext_community_set
      
  def _set_ext_community_set(self, v, load=False):
    """
    Setter method for ext_community_set, mapped from YANG variable /routing_policy/defined_sets/bgp_defined_sets/ext_community_sets/ext_community_set (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ext_community_set is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ext_community_set() directly.

    YANG Description: List of defined extended BGP community sets
    """
    try:
      t = YANGDynClass(v,base=YANGListType("ext_community_set_name",ext_community_set.ext_community_set, yang_name="ext-community-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ext-community-set-name'), is_container='list', yang_name="ext-community-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ext_community_set must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ext_community_set_name",ext_community_set.ext_community_set, yang_name="ext-community-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ext-community-set-name'), is_container='list', yang_name="ext-community-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='list', is_config=True)""",
        })

    self.__ext_community_set = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ext_community_set(self):
    self.__ext_community_set = YANGDynClass(base=YANGListType("ext_community_set_name",ext_community_set.ext_community_set, yang_name="ext-community-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ext-community-set-name'), is_container='list', yang_name="ext-community-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='list', is_config=True)

  ext_community_set = property(_get_ext_community_set, _set_ext_community_set)


  _pyangbind_elements = {'ext_community_set': ext_community_set, }

