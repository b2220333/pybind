
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class dns_server_global(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /ipv6/ipv6-global-cmds/nd-global/dns-server-global. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__dns_server_prefix_global','__dns_server_lifetime_global',)

  _yang_name = 'dns-server-global'
  _rest_name = 'ra-dns-server'

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
    self.__dns_server_prefix_global = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="dns-server-prefix-global", rest_name="dns-server-prefix-global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='inet:ipv6-address', is_config=True)
    self.__dns_server_lifetime_global = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..200']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(100), is_leaf=True, yang_name="dns-server-lifetime-global", rest_name="lifetime-multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Lifetime multiplier for the Recursive DNS Server option', u'cli-full-command': None, u'alt-name': u'lifetime-multiplier', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='uint32', is_config=True)

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
      return [u'ipv6', u'ipv6-global-cmds', u'nd-global', u'dns-server-global']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ipv6', u'nd', u'ra-dns-server']

  def _get_dns_server_prefix_global(self):
    """
    Getter method for dns_server_prefix_global, mapped from YANG variable /ipv6/ipv6_global_cmds/nd_global/dns_server_global/dns_server_prefix_global (inet:ipv6-address)
    """
    return self.__dns_server_prefix_global
      
  def _set_dns_server_prefix_global(self, v, load=False):
    """
    Setter method for dns_server_prefix_global, mapped from YANG variable /ipv6/ipv6_global_cmds/nd_global/dns_server_global/dns_server_prefix_global (inet:ipv6-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dns_server_prefix_global is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dns_server_prefix_global() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="dns-server-prefix-global", rest_name="dns-server-prefix-global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='inet:ipv6-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dns_server_prefix_global must be of a type compatible with inet:ipv6-address""",
          'defined-type': "inet:ipv6-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="dns-server-prefix-global", rest_name="dns-server-prefix-global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='inet:ipv6-address', is_config=True)""",
        })

    self.__dns_server_prefix_global = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dns_server_prefix_global(self):
    self.__dns_server_prefix_global = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="dns-server-prefix-global", rest_name="dns-server-prefix-global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='inet:ipv6-address', is_config=True)


  def _get_dns_server_lifetime_global(self):
    """
    Getter method for dns_server_lifetime_global, mapped from YANG variable /ipv6/ipv6_global_cmds/nd_global/dns_server_global/dns_server_lifetime_global (uint32)
    """
    return self.__dns_server_lifetime_global
      
  def _set_dns_server_lifetime_global(self, v, load=False):
    """
    Setter method for dns_server_lifetime_global, mapped from YANG variable /ipv6/ipv6_global_cmds/nd_global/dns_server_global/dns_server_lifetime_global (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dns_server_lifetime_global is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dns_server_lifetime_global() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..200']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(100), is_leaf=True, yang_name="dns-server-lifetime-global", rest_name="lifetime-multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Lifetime multiplier for the Recursive DNS Server option', u'cli-full-command': None, u'alt-name': u'lifetime-multiplier', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dns_server_lifetime_global must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..200']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(100), is_leaf=True, yang_name="dns-server-lifetime-global", rest_name="lifetime-multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Lifetime multiplier for the Recursive DNS Server option', u'cli-full-command': None, u'alt-name': u'lifetime-multiplier', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='uint32', is_config=True)""",
        })

    self.__dns_server_lifetime_global = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dns_server_lifetime_global(self):
    self.__dns_server_lifetime_global = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..200']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(100), is_leaf=True, yang_name="dns-server-lifetime-global", rest_name="lifetime-multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Lifetime multiplier for the Recursive DNS Server option', u'cli-full-command': None, u'alt-name': u'lifetime-multiplier', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='uint32', is_config=True)

  dns_server_prefix_global = __builtin__.property(_get_dns_server_prefix_global, _set_dns_server_prefix_global)
  dns_server_lifetime_global = __builtin__.property(_get_dns_server_lifetime_global, _set_dns_server_lifetime_global)


  _pyangbind_elements = {'dns_server_prefix_global': dns_server_prefix_global, 'dns_server_lifetime_global': dns_server_lifetime_global, }


