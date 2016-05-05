
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
  from YANG module openconfig-bgp - based on the path /bgp/neighbors/neighbor/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the BGP neighbor or
group
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__peer_as','__local_as','__peer_type','__auth_password','__remove_private_as','__route_flap_damping','__send_community','__description','__peer_group','__neighbor_address','__enabled',)

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
    self.__route_flap_damping = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="route-flap-damping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)
    self.__description = YANGDynClass(base=unicode, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='string', is_config=True)
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)
    self.__peer_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INTERNAL': {}, u'EXTERNAL': {}},), is_leaf=True, yang_name="peer-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='oc-bgp-types:peer-type', is_config=True)
    self.__local_as = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='inet:as-number', is_config=True)
    self.__peer_group = YANGDynClass(base=ReferenceType(referenced_path='/bgp/peer-groups/peer-group/peer-group-name', caller=self._path() + ['peer-group'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='leafref', is_config=True)
    self.__send_community = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'BOTH': {}, u'NONE': {}, u'EXTENDED': {}, u'STANDARD': {}},), default=unicode("NONE"), is_leaf=True, yang_name="send-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='oc-bgp-types:community-type', is_config=True)
    self.__peer_as = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peer-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='inet:as-number', is_config=True)
    self.__remove_private_as = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-bgp-types:PRIVATE_AS_REPLACE_ALL': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:PRIVATE_AS_REMOVE_ALL': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:PRIVATE_AS_REMOVE_ALL': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'PRIVATE_AS_REPLACE_ALL': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:PRIVATE_AS_REPLACE_ALL': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'PRIVATE_AS_REMOVE_ALL': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}},), is_leaf=True, yang_name="remove-private-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='oc-bgp-types:remove-private-as-option', is_config=True)
    self.__auth_password = YANGDynClass(base=unicode, is_leaf=True, yang_name="auth-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='string', is_config=True)
    self.__neighbor_address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="neighbor-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='inet:ip-address', is_config=True)

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
      return [u'bgp', u'neighbors', u'neighbor', u'config']

  def _get_peer_as(self):
    """
    Getter method for peer_as, mapped from YANG variable /bgp/neighbors/neighbor/config/peer_as (inet:as-number)

    YANG Description: AS number of the peer.
    """
    return self.__peer_as
      
  def _set_peer_as(self, v, load=False):
    """
    Setter method for peer_as, mapped from YANG variable /bgp/neighbors/neighbor/config/peer_as (inet:as-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_as is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_as() directly.

    YANG Description: AS number of the peer.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peer-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='inet:as-number', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_as must be of a type compatible with inet:as-number""",
          'defined-type': "inet:as-number",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peer-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='inet:as-number', is_config=True)""",
        })

    self.__peer_as = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_as(self):
    self.__peer_as = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peer-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='inet:as-number', is_config=True)


  def _get_local_as(self):
    """
    Getter method for local_as, mapped from YANG variable /bgp/neighbors/neighbor/config/local_as (inet:as-number)

    YANG Description: The local autonomous system number that is to be used
when establishing sessions with the remote peer or peer
group, if this differs from the global BGP router
autonomous system number.
    """
    return self.__local_as
      
  def _set_local_as(self, v, load=False):
    """
    Setter method for local_as, mapped from YANG variable /bgp/neighbors/neighbor/config/local_as (inet:as-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_as is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_as() directly.

    YANG Description: The local autonomous system number that is to be used
when establishing sessions with the remote peer or peer
group, if this differs from the global BGP router
autonomous system number.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='inet:as-number', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_as must be of a type compatible with inet:as-number""",
          'defined-type': "inet:as-number",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='inet:as-number', is_config=True)""",
        })

    self.__local_as = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_as(self):
    self.__local_as = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='inet:as-number', is_config=True)


  def _get_peer_type(self):
    """
    Getter method for peer_type, mapped from YANG variable /bgp/neighbors/neighbor/config/peer_type (oc-bgp-types:peer-type)

    YANG Description: Explicitly designate the peer or peer group as internal
(iBGP) or external (eBGP).
    """
    return self.__peer_type
      
  def _set_peer_type(self, v, load=False):
    """
    Setter method for peer_type, mapped from YANG variable /bgp/neighbors/neighbor/config/peer_type (oc-bgp-types:peer-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_type() directly.

    YANG Description: Explicitly designate the peer or peer group as internal
(iBGP) or external (eBGP).
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INTERNAL': {}, u'EXTERNAL': {}},), is_leaf=True, yang_name="peer-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='oc-bgp-types:peer-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_type must be of a type compatible with oc-bgp-types:peer-type""",
          'defined-type': "oc-bgp-types:peer-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INTERNAL': {}, u'EXTERNAL': {}},), is_leaf=True, yang_name="peer-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='oc-bgp-types:peer-type', is_config=True)""",
        })

    self.__peer_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_type(self):
    self.__peer_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INTERNAL': {}, u'EXTERNAL': {}},), is_leaf=True, yang_name="peer-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='oc-bgp-types:peer-type', is_config=True)


  def _get_auth_password(self):
    """
    Getter method for auth_password, mapped from YANG variable /bgp/neighbors/neighbor/config/auth_password (string)

    YANG Description: Configures an MD5 authentication password for use with
neighboring devices.
    """
    return self.__auth_password
      
  def _set_auth_password(self, v, load=False):
    """
    Setter method for auth_password, mapped from YANG variable /bgp/neighbors/neighbor/config/auth_password (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth_password is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth_password() directly.

    YANG Description: Configures an MD5 authentication password for use with
neighboring devices.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="auth-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth_password must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="auth-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='string', is_config=True)""",
        })

    self.__auth_password = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth_password(self):
    self.__auth_password = YANGDynClass(base=unicode, is_leaf=True, yang_name="auth-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='string', is_config=True)


  def _get_remove_private_as(self):
    """
    Getter method for remove_private_as, mapped from YANG variable /bgp/neighbors/neighbor/config/remove_private_as (oc-bgp-types:remove-private-as-option)

    YANG Description: Remove private AS numbers from updates sent to peers - when
this leaf is not specified, the AS_PATH attribute should be
sent to the peer unchanged
    """
    return self.__remove_private_as
      
  def _set_remove_private_as(self, v, load=False):
    """
    Setter method for remove_private_as, mapped from YANG variable /bgp/neighbors/neighbor/config/remove_private_as (oc-bgp-types:remove-private-as-option)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remove_private_as is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remove_private_as() directly.

    YANG Description: Remove private AS numbers from updates sent to peers - when
this leaf is not specified, the AS_PATH attribute should be
sent to the peer unchanged
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-bgp-types:PRIVATE_AS_REPLACE_ALL': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:PRIVATE_AS_REMOVE_ALL': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:PRIVATE_AS_REMOVE_ALL': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'PRIVATE_AS_REPLACE_ALL': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:PRIVATE_AS_REPLACE_ALL': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'PRIVATE_AS_REMOVE_ALL': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}},), is_leaf=True, yang_name="remove-private-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='oc-bgp-types:remove-private-as-option', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remove_private_as must be of a type compatible with oc-bgp-types:remove-private-as-option""",
          'defined-type': "oc-bgp-types:remove-private-as-option",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-bgp-types:PRIVATE_AS_REPLACE_ALL': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:PRIVATE_AS_REMOVE_ALL': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:PRIVATE_AS_REMOVE_ALL': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'PRIVATE_AS_REPLACE_ALL': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:PRIVATE_AS_REPLACE_ALL': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'PRIVATE_AS_REMOVE_ALL': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}},), is_leaf=True, yang_name="remove-private-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='oc-bgp-types:remove-private-as-option', is_config=True)""",
        })

    self.__remove_private_as = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remove_private_as(self):
    self.__remove_private_as = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-bgp-types:PRIVATE_AS_REPLACE_ALL': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:PRIVATE_AS_REMOVE_ALL': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'oc-bgp-types:PRIVATE_AS_REMOVE_ALL': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'PRIVATE_AS_REPLACE_ALL': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'openconfig-bgp-types:PRIVATE_AS_REPLACE_ALL': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}, u'PRIVATE_AS_REMOVE_ALL': {'@module': u'openconfig-bgp-types', '@namespace': u'http://openconfig.net/yang/bgp-types'}},), is_leaf=True, yang_name="remove-private-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='oc-bgp-types:remove-private-as-option', is_config=True)


  def _get_route_flap_damping(self):
    """
    Getter method for route_flap_damping, mapped from YANG variable /bgp/neighbors/neighbor/config/route_flap_damping (boolean)

    YANG Description: Enable route flap damping.
    """
    return self.__route_flap_damping
      
  def _set_route_flap_damping(self, v, load=False):
    """
    Setter method for route_flap_damping, mapped from YANG variable /bgp/neighbors/neighbor/config/route_flap_damping (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_flap_damping is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_flap_damping() directly.

    YANG Description: Enable route flap damping.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="route-flap-damping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_flap_damping must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="route-flap-damping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)""",
        })

    self.__route_flap_damping = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_flap_damping(self):
    self.__route_flap_damping = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="route-flap-damping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)


  def _get_send_community(self):
    """
    Getter method for send_community, mapped from YANG variable /bgp/neighbors/neighbor/config/send_community (oc-bgp-types:community-type)

    YANG Description: Specify which types of community should be sent to the
neighbor or group. The default is to not send the
community attribute
    """
    return self.__send_community
      
  def _set_send_community(self, v, load=False):
    """
    Setter method for send_community, mapped from YANG variable /bgp/neighbors/neighbor/config/send_community (oc-bgp-types:community-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_send_community is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_send_community() directly.

    YANG Description: Specify which types of community should be sent to the
neighbor or group. The default is to not send the
community attribute
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'BOTH': {}, u'NONE': {}, u'EXTENDED': {}, u'STANDARD': {}},), default=unicode("NONE"), is_leaf=True, yang_name="send-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='oc-bgp-types:community-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """send_community must be of a type compatible with oc-bgp-types:community-type""",
          'defined-type': "oc-bgp-types:community-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'BOTH': {}, u'NONE': {}, u'EXTENDED': {}, u'STANDARD': {}},), default=unicode("NONE"), is_leaf=True, yang_name="send-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='oc-bgp-types:community-type', is_config=True)""",
        })

    self.__send_community = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_send_community(self):
    self.__send_community = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'BOTH': {}, u'NONE': {}, u'EXTENDED': {}, u'STANDARD': {}},), default=unicode("NONE"), is_leaf=True, yang_name="send-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='oc-bgp-types:community-type', is_config=True)


  def _get_description(self):
    """
    Getter method for description, mapped from YANG variable /bgp/neighbors/neighbor/config/description (string)

    YANG Description: An optional textual description (intended primarily for use
with a peer or group
    """
    return self.__description
      
  def _set_description(self, v, load=False):
    """
    Setter method for description, mapped from YANG variable /bgp/neighbors/neighbor/config/description (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_description is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_description() directly.

    YANG Description: An optional textual description (intended primarily for use
with a peer or group
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """description must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='string', is_config=True)""",
        })

    self.__description = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_description(self):
    self.__description = YANGDynClass(base=unicode, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='string', is_config=True)


  def _get_peer_group(self):
    """
    Getter method for peer_group, mapped from YANG variable /bgp/neighbors/neighbor/config/peer_group (leafref)

    YANG Description: The peer-group with which this neighbor is associated
    """
    return self.__peer_group
      
  def _set_peer_group(self, v, load=False):
    """
    Setter method for peer_group, mapped from YANG variable /bgp/neighbors/neighbor/config/peer_group (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_group() directly.

    YANG Description: The peer-group with which this neighbor is associated
    """
    try:
      t = YANGDynClass(v,base=ReferenceType(referenced_path='/bgp/peer-groups/peer-group/peer-group-name', caller=self._path() + ['peer-group'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_group must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=ReferenceType(referenced_path='/bgp/peer-groups/peer-group/peer-group-name', caller=self._path() + ['peer-group'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='leafref', is_config=True)""",
        })

    self.__peer_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_group(self):
    self.__peer_group = YANGDynClass(base=ReferenceType(referenced_path='/bgp/peer-groups/peer-group/peer-group-name', caller=self._path() + ['peer-group'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='leafref', is_config=True)


  def _get_neighbor_address(self):
    """
    Getter method for neighbor_address, mapped from YANG variable /bgp/neighbors/neighbor/config/neighbor_address (inet:ip-address)

    YANG Description: Address of the BGP peer, either in IPv4 or IPv6
    """
    return self.__neighbor_address
      
  def _set_neighbor_address(self, v, load=False):
    """
    Setter method for neighbor_address, mapped from YANG variable /bgp/neighbors/neighbor/config/neighbor_address (inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor_address() directly.

    YANG Description: Address of the BGP peer, either in IPv4 or IPv6
    """
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="neighbor-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='inet:ip-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor_address must be of a type compatible with inet:ip-address""",
          'defined-type': "inet:ip-address",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="neighbor-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='inet:ip-address', is_config=True)""",
        })

    self.__neighbor_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor_address(self):
    self.__neighbor_address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="neighbor-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='inet:ip-address', is_config=True)


  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /bgp/neighbors/neighbor/config/enabled (boolean)

    YANG Description: Whether the BGP peer is enabled. In cases where the
enabled leaf is set to false, the local system should not
initiate connections to the neighbor, and should not
respond to TCP connections attempts from the neighbor. If
the state of the BGP session is ESTABLISHED at the time
that this leaf is set to false, the BGP session should be
ceased.
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /bgp/neighbors/neighbor/config/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: Whether the BGP peer is enabled. In cases where the
enabled leaf is set to false, the local system should not
initiate connections to the neighbor, and should not
respond to TCP connections attempts from the neighbor. If
the state of the BGP session is ESTABLISHED at the time
that this leaf is set to false, the BGP session should be
ceased.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)

  peer_as = property(_get_peer_as, _set_peer_as)
  local_as = property(_get_local_as, _set_local_as)
  peer_type = property(_get_peer_type, _set_peer_type)
  auth_password = property(_get_auth_password, _set_auth_password)
  remove_private_as = property(_get_remove_private_as, _set_remove_private_as)
  route_flap_damping = property(_get_route_flap_damping, _set_route_flap_damping)
  send_community = property(_get_send_community, _set_send_community)
  description = property(_get_description, _set_description)
  peer_group = property(_get_peer_group, _set_peer_group)
  neighbor_address = property(_get_neighbor_address, _set_neighbor_address)
  enabled = property(_get_enabled, _set_enabled)


  _pyangbind_elements = {'peer_as': peer_as, 'local_as': local_as, 'peer_type': peer_type, 'auth_password': auth_password, 'remove_private_as': remove_private_as, 'route_flap_damping': route_flap_damping, 'send_community': send_community, 'description': description, 'peer_group': peer_group, 'neighbor_address': neighbor_address, 'enabled': enabled, }


