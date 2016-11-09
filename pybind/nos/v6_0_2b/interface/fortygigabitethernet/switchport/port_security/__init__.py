
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import port_secutiry_mac_address
import sticky
import allowed_ouis
class port_security(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/fortygigabitethernet/switchport/port-security. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enable port-security feature
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__port_sec_max','__port_sec_violation','__port_secutiry_mac_address','__sticky','__allowed_ouis','__shutdown_time',)

  _yang_name = 'port-security'
  _rest_name = 'port-security'

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
    self.__port_sec_violation = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'restrict': {'value': 1}, u'shutdown': {'value': 2}},), is_leaf=True, yang_name="port-sec-violation", rest_name="violation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the action on violation', u'alt-name': u'violation'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='port-sec-violation', is_config=True)
    self.__shutdown_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..15']}), is_leaf=True, yang_name="shutdown-time", rest_name="shutdown-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shutdown time for port', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='uint32', is_config=True)
    self.__port_sec_max = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..8192']}), is_leaf=True, yang_name="port-sec-max", rest_name="max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Maximum number of allowed MACs', u'alt-name': u'max', u'cli-run-template': u'$(.?:)'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='uint32', is_config=True)
    self.__allowed_ouis = YANGDynClass(base=YANGListType("oui",allowed_ouis.allowed_ouis, yang_name="allowed-ouis", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='oui', extensions={u'tailf-common': {u'info': u'List of allowed OUIs', u'cli-drop-node-name': None, u'cli-suppress-mode': None, u'callpoint': u'interface_portsecurity_oui', u'cli-suppress-list-no': None}}), is_container='list', yang_name="allowed-ouis", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'List of allowed OUIs', u'cli-drop-node-name': None, u'cli-suppress-mode': None, u'callpoint': u'interface_portsecurity_oui', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)
    self.__port_secutiry_mac_address = YANGDynClass(base=YANGListType("mac_address port_sec_vlan",port_secutiry_mac_address.port_secutiry_mac_address, yang_name="port-secutiry-mac-address", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mac-address port-sec-vlan', extensions={u'tailf-common': {u'info': u'Mac Address commands', u'cli-drop-node-name': None, u'cli-suppress-mode': None, u'callpoint': u'interface_portsecurity_mac', u'cli-suppress-list-no': None}}), is_container='list', yang_name="port-secutiry-mac-address", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mac Address commands', u'cli-drop-node-name': None, u'cli-suppress-mode': None, u'callpoint': u'interface_portsecurity_mac', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)
    self.__sticky = YANGDynClass(base=sticky.sticky, is_container='container', yang_name="sticky", rest_name="sticky", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sticky MAC', u'callpoint': u'interface_portsecurity', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)

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
      return [u'interface', u'fortygigabitethernet', u'switchport', u'port-security']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'FortyGigabitEthernet', u'switchport', u'port-security']

  def _get_port_sec_max(self):
    """
    Getter method for port_sec_max, mapped from YANG variable /interface/fortygigabitethernet/switchport/port_security/port_sec_max (uint32)

    YANG Description: Maximum number of allowed MACs
    """
    return self.__port_sec_max
      
  def _set_port_sec_max(self, v, load=False):
    """
    Setter method for port_sec_max, mapped from YANG variable /interface/fortygigabitethernet/switchport/port_security/port_sec_max (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_sec_max is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_sec_max() directly.

    YANG Description: Maximum number of allowed MACs
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..8192']}), is_leaf=True, yang_name="port-sec-max", rest_name="max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Maximum number of allowed MACs', u'alt-name': u'max', u'cli-run-template': u'$(.?:)'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_sec_max must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..8192']}), is_leaf=True, yang_name="port-sec-max", rest_name="max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Maximum number of allowed MACs', u'alt-name': u'max', u'cli-run-template': u'$(.?:)'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='uint32', is_config=True)""",
        })

    self.__port_sec_max = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_sec_max(self):
    self.__port_sec_max = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..8192']}), is_leaf=True, yang_name="port-sec-max", rest_name="max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Maximum number of allowed MACs', u'alt-name': u'max', u'cli-run-template': u'$(.?:)'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='uint32', is_config=True)


  def _get_port_sec_violation(self):
    """
    Getter method for port_sec_violation, mapped from YANG variable /interface/fortygigabitethernet/switchport/port_security/port_sec_violation (port-sec-violation)

    YANG Description: Set the action on violation
    """
    return self.__port_sec_violation
      
  def _set_port_sec_violation(self, v, load=False):
    """
    Setter method for port_sec_violation, mapped from YANG variable /interface/fortygigabitethernet/switchport/port_security/port_sec_violation (port-sec-violation)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_sec_violation is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_sec_violation() directly.

    YANG Description: Set the action on violation
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'restrict': {'value': 1}, u'shutdown': {'value': 2}},), is_leaf=True, yang_name="port-sec-violation", rest_name="violation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the action on violation', u'alt-name': u'violation'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='port-sec-violation', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_sec_violation must be of a type compatible with port-sec-violation""",
          'defined-type': "brocade-interface:port-sec-violation",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'restrict': {'value': 1}, u'shutdown': {'value': 2}},), is_leaf=True, yang_name="port-sec-violation", rest_name="violation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the action on violation', u'alt-name': u'violation'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='port-sec-violation', is_config=True)""",
        })

    self.__port_sec_violation = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_sec_violation(self):
    self.__port_sec_violation = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'restrict': {'value': 1}, u'shutdown': {'value': 2}},), is_leaf=True, yang_name="port-sec-violation", rest_name="violation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the action on violation', u'alt-name': u'violation'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='port-sec-violation', is_config=True)


  def _get_port_secutiry_mac_address(self):
    """
    Getter method for port_secutiry_mac_address, mapped from YANG variable /interface/fortygigabitethernet/switchport/port_security/port_secutiry_mac_address (list)

    YANG Description: Mac Address commands
    """
    return self.__port_secutiry_mac_address
      
  def _set_port_secutiry_mac_address(self, v, load=False):
    """
    Setter method for port_secutiry_mac_address, mapped from YANG variable /interface/fortygigabitethernet/switchport/port_security/port_secutiry_mac_address (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_secutiry_mac_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_secutiry_mac_address() directly.

    YANG Description: Mac Address commands
    """
    try:
      t = YANGDynClass(v,base=YANGListType("mac_address port_sec_vlan",port_secutiry_mac_address.port_secutiry_mac_address, yang_name="port-secutiry-mac-address", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mac-address port-sec-vlan', extensions={u'tailf-common': {u'info': u'Mac Address commands', u'cli-drop-node-name': None, u'cli-suppress-mode': None, u'callpoint': u'interface_portsecurity_mac', u'cli-suppress-list-no': None}}), is_container='list', yang_name="port-secutiry-mac-address", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mac Address commands', u'cli-drop-node-name': None, u'cli-suppress-mode': None, u'callpoint': u'interface_portsecurity_mac', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_secutiry_mac_address must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("mac_address port_sec_vlan",port_secutiry_mac_address.port_secutiry_mac_address, yang_name="port-secutiry-mac-address", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mac-address port-sec-vlan', extensions={u'tailf-common': {u'info': u'Mac Address commands', u'cli-drop-node-name': None, u'cli-suppress-mode': None, u'callpoint': u'interface_portsecurity_mac', u'cli-suppress-list-no': None}}), is_container='list', yang_name="port-secutiry-mac-address", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mac Address commands', u'cli-drop-node-name': None, u'cli-suppress-mode': None, u'callpoint': u'interface_portsecurity_mac', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)""",
        })

    self.__port_secutiry_mac_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_secutiry_mac_address(self):
    self.__port_secutiry_mac_address = YANGDynClass(base=YANGListType("mac_address port_sec_vlan",port_secutiry_mac_address.port_secutiry_mac_address, yang_name="port-secutiry-mac-address", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mac-address port-sec-vlan', extensions={u'tailf-common': {u'info': u'Mac Address commands', u'cli-drop-node-name': None, u'cli-suppress-mode': None, u'callpoint': u'interface_portsecurity_mac', u'cli-suppress-list-no': None}}), is_container='list', yang_name="port-secutiry-mac-address", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mac Address commands', u'cli-drop-node-name': None, u'cli-suppress-mode': None, u'callpoint': u'interface_portsecurity_mac', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)


  def _get_sticky(self):
    """
    Getter method for sticky, mapped from YANG variable /interface/fortygigabitethernet/switchport/port_security/sticky (container)

    YANG Description: Sticky MAC
    """
    return self.__sticky
      
  def _set_sticky(self, v, load=False):
    """
    Setter method for sticky, mapped from YANG variable /interface/fortygigabitethernet/switchport/port_security/sticky (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sticky is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sticky() directly.

    YANG Description: Sticky MAC
    """
    try:
      t = YANGDynClass(v,base=sticky.sticky, is_container='container', yang_name="sticky", rest_name="sticky", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sticky MAC', u'callpoint': u'interface_portsecurity', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sticky must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=sticky.sticky, is_container='container', yang_name="sticky", rest_name="sticky", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sticky MAC', u'callpoint': u'interface_portsecurity', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__sticky = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sticky(self):
    self.__sticky = YANGDynClass(base=sticky.sticky, is_container='container', yang_name="sticky", rest_name="sticky", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sticky MAC', u'callpoint': u'interface_portsecurity', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_allowed_ouis(self):
    """
    Getter method for allowed_ouis, mapped from YANG variable /interface/fortygigabitethernet/switchport/port_security/allowed_ouis (list)

    YANG Description: List of allowed OUIs
    """
    return self.__allowed_ouis
      
  def _set_allowed_ouis(self, v, load=False):
    """
    Setter method for allowed_ouis, mapped from YANG variable /interface/fortygigabitethernet/switchport/port_security/allowed_ouis (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_allowed_ouis is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_allowed_ouis() directly.

    YANG Description: List of allowed OUIs
    """
    try:
      t = YANGDynClass(v,base=YANGListType("oui",allowed_ouis.allowed_ouis, yang_name="allowed-ouis", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='oui', extensions={u'tailf-common': {u'info': u'List of allowed OUIs', u'cli-drop-node-name': None, u'cli-suppress-mode': None, u'callpoint': u'interface_portsecurity_oui', u'cli-suppress-list-no': None}}), is_container='list', yang_name="allowed-ouis", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'List of allowed OUIs', u'cli-drop-node-name': None, u'cli-suppress-mode': None, u'callpoint': u'interface_portsecurity_oui', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """allowed_ouis must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("oui",allowed_ouis.allowed_ouis, yang_name="allowed-ouis", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='oui', extensions={u'tailf-common': {u'info': u'List of allowed OUIs', u'cli-drop-node-name': None, u'cli-suppress-mode': None, u'callpoint': u'interface_portsecurity_oui', u'cli-suppress-list-no': None}}), is_container='list', yang_name="allowed-ouis", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'List of allowed OUIs', u'cli-drop-node-name': None, u'cli-suppress-mode': None, u'callpoint': u'interface_portsecurity_oui', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)""",
        })

    self.__allowed_ouis = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_allowed_ouis(self):
    self.__allowed_ouis = YANGDynClass(base=YANGListType("oui",allowed_ouis.allowed_ouis, yang_name="allowed-ouis", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='oui', extensions={u'tailf-common': {u'info': u'List of allowed OUIs', u'cli-drop-node-name': None, u'cli-suppress-mode': None, u'callpoint': u'interface_portsecurity_oui', u'cli-suppress-list-no': None}}), is_container='list', yang_name="allowed-ouis", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'List of allowed OUIs', u'cli-drop-node-name': None, u'cli-suppress-mode': None, u'callpoint': u'interface_portsecurity_oui', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)


  def _get_shutdown_time(self):
    """
    Getter method for shutdown_time, mapped from YANG variable /interface/fortygigabitethernet/switchport/port_security/shutdown_time (uint32)

    YANG Description: Shutdown time for port
    """
    return self.__shutdown_time
      
  def _set_shutdown_time(self, v, load=False):
    """
    Setter method for shutdown_time, mapped from YANG variable /interface/fortygigabitethernet/switchport/port_security/shutdown_time (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_shutdown_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_shutdown_time() directly.

    YANG Description: Shutdown time for port
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..15']}), is_leaf=True, yang_name="shutdown-time", rest_name="shutdown-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shutdown time for port', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """shutdown_time must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..15']}), is_leaf=True, yang_name="shutdown-time", rest_name="shutdown-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shutdown time for port', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='uint32', is_config=True)""",
        })

    self.__shutdown_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_shutdown_time(self):
    self.__shutdown_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..15']}), is_leaf=True, yang_name="shutdown-time", rest_name="shutdown-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shutdown time for port', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='uint32', is_config=True)

  port_sec_max = __builtin__.property(_get_port_sec_max, _set_port_sec_max)
  port_sec_violation = __builtin__.property(_get_port_sec_violation, _set_port_sec_violation)
  port_secutiry_mac_address = __builtin__.property(_get_port_secutiry_mac_address, _set_port_secutiry_mac_address)
  sticky = __builtin__.property(_get_sticky, _set_sticky)
  allowed_ouis = __builtin__.property(_get_allowed_ouis, _set_allowed_ouis)
  shutdown_time = __builtin__.property(_get_shutdown_time, _set_shutdown_time)


  _pyangbind_elements = {'port_sec_max': port_sec_max, 'port_sec_violation': port_sec_violation, 'port_secutiry_mac_address': port_secutiry_mac_address, 'sticky': sticky, 'allowed_ouis': allowed_ouis, 'shutdown_time': shutdown_time, }


