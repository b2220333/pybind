
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class l2_auth_profile(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-isis-operational - based on the path /isis-state/router-isis-config/l2-auth-profile. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: IS-IS Authentication profile for incoming Level-2 PDUs for LSPs, CSNPs and PSNPs
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__auth_check','__auth_mode','__auth_key',)

  _yang_name = 'l2-auth-profile'
  _rest_name = 'l2-auth-profile'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    path_helper_ = kwargs.pop("path_helper", None)
    if path_helper_ is False:
      self._path_helper = False
    elif path_helper_ is not None and isinstance(path_helper_, xpathhelper.YANGPathHelper):
      self._path_helper = path_helper_
    elif hasattr(self, "_parent"):
      path_helper_ = getattr(self._parent, "_path_helper", False)
      self._path_helper = path_helper_
    else:
      self._path_helper = False

    extmethods = kwargs.pop("extmethods", None)
    if extmethods is False:
      self._extmethods = False
    elif extmethods is not None and isinstance(extmethods, dict):
      self._extmethods = extmethods
    elif hasattr(self, "_parent"):
      extmethods = getattr(self._parent, "_extmethods", None)
      self._extmethods = extmethods
    else:
      self._extmethods = False
    self.__auth_check = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="auth-check", rest_name="auth-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)
    self.__auth_key = YANGDynClass(base=unicode, is_leaf=True, yang_name="auth-key", rest_name="auth-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)
    self.__auth_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {'value': 0}, u'cleartext': {'value': 1}, u'md5': {'value': 2}},), is_leaf=True, yang_name="auth-mode", rest_name="auth-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='auth-mode', is_config=False)

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
      return [u'isis-state', u'router-isis-config', u'l2-auth-profile']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'isis-state', u'router-isis-config', u'l2-auth-profile']

  def _get_auth_check(self):
    """
    Getter method for auth_check, mapped from YANG variable /isis_state/router_isis_config/l2_auth_profile/auth_check (isis-status)

    YANG Description: If authentication enabled on incoming IS-IS PDUs
    """
    return self.__auth_check
      
  def _set_auth_check(self, v, load=False):
    """
    Setter method for auth_check, mapped from YANG variable /isis_state/router_isis_config/l2_auth_profile/auth_check (isis-status)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth_check is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth_check() directly.

    YANG Description: If authentication enabled on incoming IS-IS PDUs
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="auth-check", rest_name="auth-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth_check must be of a type compatible with isis-status""",
          'defined-type': "brocade-isis-operational:isis-status",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="auth-check", rest_name="auth-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)""",
        })

    self.__auth_check = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth_check(self):
    self.__auth_check = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="auth-check", rest_name="auth-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)


  def _get_auth_mode(self):
    """
    Getter method for auth_mode, mapped from YANG variable /isis_state/router_isis_config/l2_auth_profile/auth_mode (auth-mode)

    YANG Description: IS-IS authentication mode
    """
    return self.__auth_mode
      
  def _set_auth_mode(self, v, load=False):
    """
    Setter method for auth_mode, mapped from YANG variable /isis_state/router_isis_config/l2_auth_profile/auth_mode (auth-mode)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth_mode() directly.

    YANG Description: IS-IS authentication mode
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {'value': 0}, u'cleartext': {'value': 1}, u'md5': {'value': 2}},), is_leaf=True, yang_name="auth-mode", rest_name="auth-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='auth-mode', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth_mode must be of a type compatible with auth-mode""",
          'defined-type': "brocade-isis-operational:auth-mode",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {'value': 0}, u'cleartext': {'value': 1}, u'md5': {'value': 2}},), is_leaf=True, yang_name="auth-mode", rest_name="auth-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='auth-mode', is_config=False)""",
        })

    self.__auth_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth_mode(self):
    self.__auth_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {'value': 0}, u'cleartext': {'value': 1}, u'md5': {'value': 2}},), is_leaf=True, yang_name="auth-mode", rest_name="auth-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='auth-mode', is_config=False)


  def _get_auth_key(self):
    """
    Getter method for auth_key, mapped from YANG variable /isis_state/router_isis_config/l2_auth_profile/auth_key (string)

    YANG Description: IS-IS authentication key
    """
    return self.__auth_key
      
  def _set_auth_key(self, v, load=False):
    """
    Setter method for auth_key, mapped from YANG variable /isis_state/router_isis_config/l2_auth_profile/auth_key (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth_key is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth_key() directly.

    YANG Description: IS-IS authentication key
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="auth-key", rest_name="auth-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth_key must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="auth-key", rest_name="auth-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)""",
        })

    self.__auth_key = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth_key(self):
    self.__auth_key = YANGDynClass(base=unicode, is_leaf=True, yang_name="auth-key", rest_name="auth-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)

  auth_check = __builtin__.property(_get_auth_check)
  auth_mode = __builtin__.property(_get_auth_mode)
  auth_key = __builtin__.property(_get_auth_key)


  _pyangbind_elements = {'auth_check': auth_check, 'auth_mode': auth_mode, 'auth_key': auth_key, }


