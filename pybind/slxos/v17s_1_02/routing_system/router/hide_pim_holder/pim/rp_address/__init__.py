
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class rp_address(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/hide-pim-holder/pim/rp-address. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__rp_ip_addr','__rp_addr_prefix_list',)

  _yang_name = 'rp-address'
  _rest_name = 'rp-address'

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
    self.__rp_addr_prefix_list = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="rp-addr-prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Prefix list', u'cli-drop-node-name': None, u'alt-name': u'prefix-list', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='common-def:name-string63', is_config=True)
    self.__rp_ip_addr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="rp-ip-addr", rest_name="rp-ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='inet:ipv4-address', is_config=True)

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
      return [u'routing-system', u'router', u'hide-pim-holder', u'pim', u'rp-address']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'pim', u'rp-address']

  def _get_rp_ip_addr(self):
    """
    Getter method for rp_ip_addr, mapped from YANG variable /routing_system/router/hide_pim_holder/pim/rp_address/rp_ip_addr (inet:ipv4-address)
    """
    return self.__rp_ip_addr
      
  def _set_rp_ip_addr(self, v, load=False):
    """
    Setter method for rp_ip_addr, mapped from YANG variable /routing_system/router/hide_pim_holder/pim/rp_address/rp_ip_addr (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rp_ip_addr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rp_ip_addr() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="rp-ip-addr", rest_name="rp-ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rp_ip_addr must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="rp-ip-addr", rest_name="rp-ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__rp_ip_addr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rp_ip_addr(self):
    self.__rp_ip_addr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="rp-ip-addr", rest_name="rp-ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='inet:ipv4-address', is_config=True)


  def _get_rp_addr_prefix_list(self):
    """
    Getter method for rp_addr_prefix_list, mapped from YANG variable /routing_system/router/hide_pim_holder/pim/rp_address/rp_addr_prefix_list (common-def:name-string63)
    """
    return self.__rp_addr_prefix_list
      
  def _set_rp_addr_prefix_list(self, v, load=False):
    """
    Setter method for rp_addr_prefix_list, mapped from YANG variable /routing_system/router/hide_pim_holder/pim/rp_address/rp_addr_prefix_list (common-def:name-string63)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rp_addr_prefix_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rp_addr_prefix_list() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="rp-addr-prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Prefix list', u'cli-drop-node-name': None, u'alt-name': u'prefix-list', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='common-def:name-string63', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rp_addr_prefix_list must be of a type compatible with common-def:name-string63""",
          'defined-type': "common-def:name-string63",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="rp-addr-prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Prefix list', u'cli-drop-node-name': None, u'alt-name': u'prefix-list', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='common-def:name-string63', is_config=True)""",
        })

    self.__rp_addr_prefix_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rp_addr_prefix_list(self):
    self.__rp_addr_prefix_list = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="rp-addr-prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Prefix list', u'cli-drop-node-name': None, u'alt-name': u'prefix-list', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='common-def:name-string63', is_config=True)

  rp_ip_addr = __builtin__.property(_get_rp_ip_addr, _set_rp_ip_addr)
  rp_addr_prefix_list = __builtin__.property(_get_rp_addr_prefix_list, _set_rp_addr_prefix_list)


  _pyangbind_elements = {'rp_ip_addr': rp_ip_addr, 'rp_addr_prefix_list': rp_addr_prefix_list, }


