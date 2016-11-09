
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import arp
import address
import unnumbered
class ip_config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/port-channel/ip/ip-config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mtu','__directed_broadcast','__proxy_arp','__arp','__arp_aging_timeout','__address','__unnumbered',)

  _yang_name = 'ip-config'
  _rest_name = ''

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
    self.__arp = YANGDynClass(base=arp.arp, is_container='container', yang_name="arp", rest_name="arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ARP'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='container', is_config=True)
    self.__arp_aging_timeout = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..35790']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(240), is_leaf=True, yang_name="arp-aging-timeout", rest_name="arp-aging-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set arp age timeout value to interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='uint32', is_config=True)
    self.__directed_broadcast = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="directed-broadcast", rest_name="directed-broadcast", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable directed IP broadcasts forwarding'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='empty', is_config=True)
    self.__mtu = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1300..9100']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1500), is_leaf=True, yang_name="mtu", rest_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set ip mtu value to interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='uint32', is_config=True)
    self.__address = YANGDynClass(base=YANGListType("address",address.address, yang_name="address", rest_name="address", parent=self, is_container='list', user_ordered=True, path_helper=self._path_helper, yang_keys='address', extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-mode': None, u'callpoint': u'intf-po-ip-addr-cp', u'info': u'Set the IP address of an interface'}}), is_container='list', yang_name="address", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-mode': None, u'callpoint': u'intf-po-ip-addr-cp', u'info': u'Set the IP address of an interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='list', is_config=True)
    self.__unnumbered = YANGDynClass(base=unnumbered.unnumbered, is_container='container', yang_name="unnumbered", rest_name="unnumbered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Unnumbered Interface configuration.', u'cli-sequence-commands': None, u'cli-full-no': None, u'callpoint': u'nsm-ip-unnumbered-po-cpworker'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='container', is_config=True)
    self.__proxy_arp = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="proxy-arp", rest_name="proxy-arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Proxy-Arp on the interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='empty', is_config=True)

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
      return [u'interface', u'port-channel', u'ip', u'ip-config']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Port-channel', u'ip']

  def _get_mtu(self):
    """
    Getter method for mtu, mapped from YANG variable /interface/port_channel/ip/ip_config/mtu (uint32)
    """
    return self.__mtu
      
  def _set_mtu(self, v, load=False):
    """
    Setter method for mtu, mapped from YANG variable /interface/port_channel/ip/ip_config/mtu (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mtu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mtu() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1300..9100']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1500), is_leaf=True, yang_name="mtu", rest_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set ip mtu value to interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mtu must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1300..9100']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1500), is_leaf=True, yang_name="mtu", rest_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set ip mtu value to interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='uint32', is_config=True)""",
        })

    self.__mtu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mtu(self):
    self.__mtu = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1300..9100']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1500), is_leaf=True, yang_name="mtu", rest_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set ip mtu value to interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='uint32', is_config=True)


  def _get_directed_broadcast(self):
    """
    Getter method for directed_broadcast, mapped from YANG variable /interface/port_channel/ip/ip_config/directed_broadcast (empty)
    """
    return self.__directed_broadcast
      
  def _set_directed_broadcast(self, v, load=False):
    """
    Setter method for directed_broadcast, mapped from YANG variable /interface/port_channel/ip/ip_config/directed_broadcast (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_directed_broadcast is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_directed_broadcast() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="directed-broadcast", rest_name="directed-broadcast", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable directed IP broadcasts forwarding'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """directed_broadcast must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="directed-broadcast", rest_name="directed-broadcast", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable directed IP broadcasts forwarding'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='empty', is_config=True)""",
        })

    self.__directed_broadcast = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_directed_broadcast(self):
    self.__directed_broadcast = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="directed-broadcast", rest_name="directed-broadcast", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable directed IP broadcasts forwarding'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='empty', is_config=True)


  def _get_proxy_arp(self):
    """
    Getter method for proxy_arp, mapped from YANG variable /interface/port_channel/ip/ip_config/proxy_arp (empty)
    """
    return self.__proxy_arp
      
  def _set_proxy_arp(self, v, load=False):
    """
    Setter method for proxy_arp, mapped from YANG variable /interface/port_channel/ip/ip_config/proxy_arp (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_proxy_arp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_proxy_arp() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="proxy-arp", rest_name="proxy-arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Proxy-Arp on the interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """proxy_arp must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="proxy-arp", rest_name="proxy-arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Proxy-Arp on the interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='empty', is_config=True)""",
        })

    self.__proxy_arp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_proxy_arp(self):
    self.__proxy_arp = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="proxy-arp", rest_name="proxy-arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Proxy-Arp on the interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='empty', is_config=True)


  def _get_arp(self):
    """
    Getter method for arp, mapped from YANG variable /interface/port_channel/ip/ip_config/arp (container)
    """
    return self.__arp
      
  def _set_arp(self, v, load=False):
    """
    Setter method for arp, mapped from YANG variable /interface/port_channel/ip/ip_config/arp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_arp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_arp() directly.
    """
    try:
      t = YANGDynClass(v,base=arp.arp, is_container='container', yang_name="arp", rest_name="arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ARP'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """arp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=arp.arp, is_container='container', yang_name="arp", rest_name="arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ARP'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='container', is_config=True)""",
        })

    self.__arp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_arp(self):
    self.__arp = YANGDynClass(base=arp.arp, is_container='container', yang_name="arp", rest_name="arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ARP'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='container', is_config=True)


  def _get_arp_aging_timeout(self):
    """
    Getter method for arp_aging_timeout, mapped from YANG variable /interface/port_channel/ip/ip_config/arp_aging_timeout (uint32)
    """
    return self.__arp_aging_timeout
      
  def _set_arp_aging_timeout(self, v, load=False):
    """
    Setter method for arp_aging_timeout, mapped from YANG variable /interface/port_channel/ip/ip_config/arp_aging_timeout (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_arp_aging_timeout is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_arp_aging_timeout() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..35790']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(240), is_leaf=True, yang_name="arp-aging-timeout", rest_name="arp-aging-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set arp age timeout value to interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """arp_aging_timeout must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..35790']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(240), is_leaf=True, yang_name="arp-aging-timeout", rest_name="arp-aging-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set arp age timeout value to interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='uint32', is_config=True)""",
        })

    self.__arp_aging_timeout = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_arp_aging_timeout(self):
    self.__arp_aging_timeout = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..35790']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(240), is_leaf=True, yang_name="arp-aging-timeout", rest_name="arp-aging-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set arp age timeout value to interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='uint32', is_config=True)


  def _get_address(self):
    """
    Getter method for address, mapped from YANG variable /interface/port_channel/ip/ip_config/address (list)
    """
    return self.__address
      
  def _set_address(self, v, load=False):
    """
    Setter method for address, mapped from YANG variable /interface/port_channel/ip/ip_config/address (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("address",address.address, yang_name="address", rest_name="address", parent=self, is_container='list', user_ordered=True, path_helper=self._path_helper, yang_keys='address', extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-mode': None, u'callpoint': u'intf-po-ip-addr-cp', u'info': u'Set the IP address of an interface'}}), is_container='list', yang_name="address", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-mode': None, u'callpoint': u'intf-po-ip-addr-cp', u'info': u'Set the IP address of an interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("address",address.address, yang_name="address", rest_name="address", parent=self, is_container='list', user_ordered=True, path_helper=self._path_helper, yang_keys='address', extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-mode': None, u'callpoint': u'intf-po-ip-addr-cp', u'info': u'Set the IP address of an interface'}}), is_container='list', yang_name="address", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-mode': None, u'callpoint': u'intf-po-ip-addr-cp', u'info': u'Set the IP address of an interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='list', is_config=True)""",
        })

    self.__address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address(self):
    self.__address = YANGDynClass(base=YANGListType("address",address.address, yang_name="address", rest_name="address", parent=self, is_container='list', user_ordered=True, path_helper=self._path_helper, yang_keys='address', extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-mode': None, u'callpoint': u'intf-po-ip-addr-cp', u'info': u'Set the IP address of an interface'}}), is_container='list', yang_name="address", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-mode': None, u'callpoint': u'intf-po-ip-addr-cp', u'info': u'Set the IP address of an interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='list', is_config=True)


  def _get_unnumbered(self):
    """
    Getter method for unnumbered, mapped from YANG variable /interface/port_channel/ip/ip_config/unnumbered (container)
    """
    return self.__unnumbered
      
  def _set_unnumbered(self, v, load=False):
    """
    Setter method for unnumbered, mapped from YANG variable /interface/port_channel/ip/ip_config/unnumbered (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unnumbered is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unnumbered() directly.
    """
    try:
      t = YANGDynClass(v,base=unnumbered.unnumbered, is_container='container', yang_name="unnumbered", rest_name="unnumbered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Unnumbered Interface configuration.', u'cli-sequence-commands': None, u'cli-full-no': None, u'callpoint': u'nsm-ip-unnumbered-po-cpworker'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unnumbered must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=unnumbered.unnumbered, is_container='container', yang_name="unnumbered", rest_name="unnumbered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Unnumbered Interface configuration.', u'cli-sequence-commands': None, u'cli-full-no': None, u'callpoint': u'nsm-ip-unnumbered-po-cpworker'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='container', is_config=True)""",
        })

    self.__unnumbered = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unnumbered(self):
    self.__unnumbered = YANGDynClass(base=unnumbered.unnumbered, is_container='container', yang_name="unnumbered", rest_name="unnumbered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Unnumbered Interface configuration.', u'cli-sequence-commands': None, u'cli-full-no': None, u'callpoint': u'nsm-ip-unnumbered-po-cpworker'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='container', is_config=True)

  mtu = __builtin__.property(_get_mtu, _set_mtu)
  directed_broadcast = __builtin__.property(_get_directed_broadcast, _set_directed_broadcast)
  proxy_arp = __builtin__.property(_get_proxy_arp, _set_proxy_arp)
  arp = __builtin__.property(_get_arp, _set_arp)
  arp_aging_timeout = __builtin__.property(_get_arp_aging_timeout, _set_arp_aging_timeout)
  address = __builtin__.property(_get_address, _set_address)
  unnumbered = __builtin__.property(_get_unnumbered, _set_unnumbered)


  _pyangbind_elements = {'mtu': mtu, 'directed_broadcast': directed_broadcast, 'proxy_arp': proxy_arp, 'arp': arp, 'arp_aging_timeout': arp_aging_timeout, 'address': address, 'unnumbered': unnumbered, }


