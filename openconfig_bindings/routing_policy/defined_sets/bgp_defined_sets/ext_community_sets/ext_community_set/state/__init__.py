
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
  from YANG module openconfig-routing-policy - based on the path /routing-policy/defined-sets/bgp-defined-sets/ext-community-sets/ext-community-set/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for extended BGP community sets
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__ext_community_set_name','__ext_community_member',)

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
    self.__ext_community_member = YANGDynClass(base=TypedListType(allowed_type=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'route\\-target:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'route\\-target:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'route\\-origin:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'route\\-origin:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'}),unicode,]), is_leaf=False, yang_name="ext-community-member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='union', is_config=False)
    self.__ext_community_set_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="ext-community-set-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='string', is_config=False)

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
      return [u'routing-policy', u'defined-sets', u'bgp-defined-sets', u'ext-community-sets', u'ext-community-set', u'state']

  def _get_ext_community_set_name(self):
    """
    Getter method for ext_community_set_name, mapped from YANG variable /routing_policy/defined_sets/bgp_defined_sets/ext_community_sets/ext_community_set/state/ext_community_set_name (string)

    YANG Description: name / label of the extended community set -- this is
used to reference the set in match conditions
    """
    return self.__ext_community_set_name
      
  def _set_ext_community_set_name(self, v, load=False):
    """
    Setter method for ext_community_set_name, mapped from YANG variable /routing_policy/defined_sets/bgp_defined_sets/ext_community_sets/ext_community_set/state/ext_community_set_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ext_community_set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ext_community_set_name() directly.

    YANG Description: name / label of the extended community set -- this is
used to reference the set in match conditions
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="ext-community-set-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ext_community_set_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="ext-community-set-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='string', is_config=False)""",
        })

    self.__ext_community_set_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ext_community_set_name(self):
    self.__ext_community_set_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="ext-community-set-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='string', is_config=False)


  def _get_ext_community_member(self):
    """
    Getter method for ext_community_member, mapped from YANG variable /routing_policy/defined_sets/bgp_defined_sets/ext_community_sets/ext_community_set/state/ext_community_member (union)

    YANG Description: members of the extended community set
    """
    return self.__ext_community_member
      
  def _set_ext_community_member(self, v, load=False):
    """
    Setter method for ext_community_member, mapped from YANG variable /routing_policy/defined_sets/bgp_defined_sets/ext_community_sets/ext_community_set/state/ext_community_member (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ext_community_member is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ext_community_member() directly.

    YANG Description: members of the extended community set
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'route\\-target:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'route\\-target:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'route\\-origin:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'route\\-origin:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'}),unicode,]), is_leaf=False, yang_name="ext-community-member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='union', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ext_community_member must be of a type compatible with union""",
          'defined-type': "openconfig-bgp-policy:union",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'route\\-target:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'route\\-target:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'route\\-origin:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'route\\-origin:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'}),unicode,]), is_leaf=False, yang_name="ext-community-member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='union', is_config=False)""",
        })

    self.__ext_community_member = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ext_community_member(self):
    self.__ext_community_member = YANGDynClass(base=TypedListType(allowed_type=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'route\\-target:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'route\\-target:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'route\\-origin:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'route\\-origin:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'}),unicode,]), is_leaf=False, yang_name="ext-community-member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp-policy', defining_module='openconfig-bgp-policy', yang_type='union', is_config=False)

  ext_community_set_name = property(_get_ext_community_set_name)
  ext_community_member = property(_get_ext_community_member)


  _pyangbind_elements = {'ext_community_set_name': ext_community_set_name, 'ext_community_member': ext_community_member, }


