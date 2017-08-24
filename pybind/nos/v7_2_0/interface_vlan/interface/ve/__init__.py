
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ip
import ipv6
import attach
class ve(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface-vlan/interface/ve. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The list of ve interfaces in the managed device. Each row 
represents a ve interface. User can create/delete an entry in 
to this list.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__gve_name','__global_ve_shutdown','__ip','__ipv6','__attach',)

  _yang_name = 've'
  _rest_name = 'Ve'

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
    self.__ip = YANGDynClass(base=ip.ip, is_container='container', presence=False, yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Internet Protocol (IP).', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__global_ve_shutdown = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="global-ve-shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Shutdown the selected interface', u'cli-show-no': None, u'alt-name': u'shutdown'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    self.__attach = YANGDynClass(base=attach.attach, is_container='container', presence=False, yang_name="attach", rest_name="attach", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure attachments', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='container', is_config=True)
    self.__gve_name = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="gve-name", rest_name="gve-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'cli-custom-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ve-type', is_config=True)
    self.__ipv6 = YANGDynClass(base=ipv6.ipv6, is_container='container', presence=False, yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Internet Protocol version 6(IPv6).', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)

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
      return [u'interface-vlan', u'interface', u've']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ve']

  def _get_gve_name(self):
    """
    Getter method for gve_name, mapped from YANG variable /interface_vlan/interface/ve/gve_name (ve-type)
    """
    return self.__gve_name
      
  def _set_gve_name(self, v, load=False):
    """
    Setter method for gve_name, mapped from YANG variable /interface_vlan/interface/ve/gve_name (ve-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_gve_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_gve_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="gve-name", rest_name="gve-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'cli-custom-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ve-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """gve_name must be of a type compatible with ve-type""",
          'defined-type': "brocade-interface:ve-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="gve-name", rest_name="gve-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'cli-custom-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ve-type', is_config=True)""",
        })

    self.__gve_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_gve_name(self):
    self.__gve_name = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="gve-name", rest_name="gve-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'cli-custom-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ve-type', is_config=True)


  def _get_global_ve_shutdown(self):
    """
    Getter method for global_ve_shutdown, mapped from YANG variable /interface_vlan/interface/ve/global_ve_shutdown (empty)
    """
    return self.__global_ve_shutdown
      
  def _set_global_ve_shutdown(self, v, load=False):
    """
    Setter method for global_ve_shutdown, mapped from YANG variable /interface_vlan/interface/ve/global_ve_shutdown (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_global_ve_shutdown is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_global_ve_shutdown() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="global-ve-shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Shutdown the selected interface', u'cli-show-no': None, u'alt-name': u'shutdown'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """global_ve_shutdown must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="global-ve-shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Shutdown the selected interface', u'cli-show-no': None, u'alt-name': u'shutdown'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)""",
        })

    self.__global_ve_shutdown = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_global_ve_shutdown(self):
    self.__global_ve_shutdown = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="global-ve-shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Shutdown the selected interface', u'cli-show-no': None, u'alt-name': u'shutdown'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)


  def _get_ip(self):
    """
    Getter method for ip, mapped from YANG variable /interface_vlan/interface/ve/ip (container)

    YANG Description: The IP configurations for an interface.
    """
    return self.__ip
      
  def _set_ip(self, v, load=False):
    """
    Setter method for ip, mapped from YANG variable /interface_vlan/interface/ve/ip (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip() directly.

    YANG Description: The IP configurations for an interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ip.ip, is_container='container', presence=False, yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Internet Protocol (IP).', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ip.ip, is_container='container', presence=False, yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Internet Protocol (IP).', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip(self):
    self.__ip = YANGDynClass(base=ip.ip, is_container='container', presence=False, yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Internet Protocol (IP).', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_ipv6(self):
    """
    Getter method for ipv6, mapped from YANG variable /interface_vlan/interface/ve/ipv6 (container)

    YANG Description: The IPv6 configurations for an interface.
    """
    return self.__ipv6
      
  def _set_ipv6(self, v, load=False):
    """
    Setter method for ipv6, mapped from YANG variable /interface_vlan/interface/ve/ipv6 (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6() directly.

    YANG Description: The IPv6 configurations for an interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ipv6.ipv6, is_container='container', presence=False, yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Internet Protocol version 6(IPv6).', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6 must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ipv6.ipv6, is_container='container', presence=False, yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Internet Protocol version 6(IPv6).', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__ipv6 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6(self):
    self.__ipv6 = YANGDynClass(base=ipv6.ipv6, is_container='container', presence=False, yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Internet Protocol version 6(IPv6).', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_attach(self):
    """
    Getter method for attach, mapped from YANG variable /interface_vlan/interface/ve/attach (container)
    """
    return self.__attach
      
  def _set_attach(self, v, load=False):
    """
    Setter method for attach, mapped from YANG variable /interface_vlan/interface/ve/attach (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attach is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attach() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=attach.attach, is_container='container', presence=False, yang_name="attach", rest_name="attach", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure attachments', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attach must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=attach.attach, is_container='container', presence=False, yang_name="attach", rest_name="attach", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure attachments', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='container', is_config=True)""",
        })

    self.__attach = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attach(self):
    self.__attach = YANGDynClass(base=attach.attach, is_container='container', presence=False, yang_name="attach", rest_name="attach", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure attachments', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='container', is_config=True)

  gve_name = __builtin__.property(_get_gve_name, _set_gve_name)
  global_ve_shutdown = __builtin__.property(_get_global_ve_shutdown, _set_global_ve_shutdown)
  ip = __builtin__.property(_get_ip, _set_ip)
  ipv6 = __builtin__.property(_get_ipv6, _set_ipv6)
  attach = __builtin__.property(_get_attach, _set_attach)


  _pyangbind_elements = {'gve_name': gve_name, 'global_ve_shutdown': global_ve_shutdown, 'ip': ip, 'ipv6': ipv6, 'attach': attach, }


