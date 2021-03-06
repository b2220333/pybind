
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ldp_session(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /mpls-config/router/mpls/mpls-cmds-holder/ldp/ldp-holder/ldp-session. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ldp_session_ip','__ldp_session_fec_filter_out','__ldp_session_auth_key',)

  _yang_name = 'ldp-session'
  _rest_name = 'session'

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
    self.__ldp_session_fec_filter_out = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="ldp-session-fec-filter-out", rest_name="filter-fec-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Apply filtering on outbound FECs', u'cli-full-no': None, u'alt-name': u'filter-fec-out'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__ldp_session_auth_key = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..80']}), is_leaf=True, yang_name="ldp-session-auth-key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable TCP-MD5 authentication', u'cli-full-no': None, u'alt-name': u'key'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__ldp_session_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-session-ip", rest_name="ldp-session-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Define LDP peer ip address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)

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
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'ldp', u'ldp-holder', u'ldp-session']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'mpls', u'ldp', u'session']

  def _get_ldp_session_ip(self):
    """
    Getter method for ldp_session_ip, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/ldp/ldp_holder/ldp_session/ldp_session_ip (inet:ipv4-address)
    """
    return self.__ldp_session_ip
      
  def _set_ldp_session_ip(self, v, load=False):
    """
    Setter method for ldp_session_ip, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/ldp/ldp_holder/ldp_session/ldp_session_ip (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_session_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_session_ip() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-session-ip", rest_name="ldp-session-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Define LDP peer ip address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_session_ip must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-session-ip", rest_name="ldp-session-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Define LDP peer ip address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__ldp_session_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_session_ip(self):
    self.__ldp_session_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-session-ip", rest_name="ldp-session-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Define LDP peer ip address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)


  def _get_ldp_session_fec_filter_out(self):
    """
    Getter method for ldp_session_fec_filter_out, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/ldp/ldp_holder/ldp_session/ldp_session_fec_filter_out (string)
    """
    return self.__ldp_session_fec_filter_out
      
  def _set_ldp_session_fec_filter_out(self, v, load=False):
    """
    Setter method for ldp_session_fec_filter_out, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/ldp/ldp_holder/ldp_session/ldp_session_fec_filter_out (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_session_fec_filter_out is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_session_fec_filter_out() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="ldp-session-fec-filter-out", rest_name="filter-fec-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Apply filtering on outbound FECs', u'cli-full-no': None, u'alt-name': u'filter-fec-out'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_session_fec_filter_out must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="ldp-session-fec-filter-out", rest_name="filter-fec-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Apply filtering on outbound FECs', u'cli-full-no': None, u'alt-name': u'filter-fec-out'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__ldp_session_fec_filter_out = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_session_fec_filter_out(self):
    self.__ldp_session_fec_filter_out = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="ldp-session-fec-filter-out", rest_name="filter-fec-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Apply filtering on outbound FECs', u'cli-full-no': None, u'alt-name': u'filter-fec-out'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_ldp_session_auth_key(self):
    """
    Getter method for ldp_session_auth_key, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/ldp/ldp_holder/ldp_session/ldp_session_auth_key (string)
    """
    return self.__ldp_session_auth_key
      
  def _set_ldp_session_auth_key(self, v, load=False):
    """
    Setter method for ldp_session_auth_key, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/ldp/ldp_holder/ldp_session/ldp_session_auth_key (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_session_auth_key is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_session_auth_key() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..80']}), is_leaf=True, yang_name="ldp-session-auth-key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable TCP-MD5 authentication', u'cli-full-no': None, u'alt-name': u'key'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_session_auth_key must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..80']}), is_leaf=True, yang_name="ldp-session-auth-key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable TCP-MD5 authentication', u'cli-full-no': None, u'alt-name': u'key'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__ldp_session_auth_key = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_session_auth_key(self):
    self.__ldp_session_auth_key = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..80']}), is_leaf=True, yang_name="ldp-session-auth-key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable TCP-MD5 authentication', u'cli-full-no': None, u'alt-name': u'key'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)

  ldp_session_ip = __builtin__.property(_get_ldp_session_ip, _set_ldp_session_ip)
  ldp_session_fec_filter_out = __builtin__.property(_get_ldp_session_fec_filter_out, _set_ldp_session_fec_filter_out)
  ldp_session_auth_key = __builtin__.property(_get_ldp_session_auth_key, _set_ldp_session_auth_key)


  _pyangbind_elements = {'ldp_session_ip': ldp_session_ip, 'ldp_session_fec_filter_out': ldp_session_fec_filter_out, 'ldp_session_auth_key': ldp_session_auth_key, }


