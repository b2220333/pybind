
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class arp_entry(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-arp - based on the path /hide-arp-holder/arp-entry. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__arp_ip_address','__mac_address_value','__interfacename','__GigabitEthernet','__TenGigabitEthernet','__FortyGigabitEthernet','__HundredGigabitEthernet','__Ve',)

  _yang_name = 'arp-entry'
  _rest_name = 'arp'

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
    self.__mac_address_value = YANGDynClass(base=unicode, is_leaf=True, yang_name="mac-address-value", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='mac-access-list:mac-address-type', is_config=True)
    self.__interfacename = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'interface': {}},), is_leaf=True, yang_name="interfacename", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='enumeration', is_config=True)
    self.__FortyGigabitEthernet = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="FortyGigabitEthernet", rest_name="FortyGigabitEthernet", parent=self, choice=(u'interfacetype', u'FortyGigabitEthernet'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='interface:interface-type', is_config=True)
    self.__GigabitEthernet = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="GigabitEthernet", rest_name="GigabitEthernet", parent=self, choice=(u'interfacetype', u'GigabitEthernet'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='interface:interface-type', is_config=True)
    self.__TenGigabitEthernet = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="TenGigabitEthernet", rest_name="TenGigabitEthernet", parent=self, choice=(u'interfacetype', u'TenGigabitEthernet'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='interface:interface-type', is_config=True)
    self.__arp_ip_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="arp-ip-address", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A.B.C.D;; IP address of the ARP entry', u'cli-drop-node-name': None, u'cli-full-no': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='inet:ipv4-address', is_config=True)
    self.__HundredGigabitEthernet = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="HundredGigabitEthernet", rest_name="HundredGigabitEthernet", parent=self, choice=(u'interfacetype', u'HundredGigabitEthernet'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='interface:interface-type', is_config=True)
    self.__Ve = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="Ve", rest_name="Ve", parent=self, choice=(u'interfacetype', u'Ve'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='interface:vlan-type', is_config=True)

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
      return [u'hide-arp-holder', u'arp-entry']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'arp']

  def _get_arp_ip_address(self):
    """
    Getter method for arp_ip_address, mapped from YANG variable /hide_arp_holder/arp_entry/arp_ip_address (inet:ipv4-address)

    YANG Description: IPv4 Address
    """
    return self.__arp_ip_address
      
  def _set_arp_ip_address(self, v, load=False):
    """
    Setter method for arp_ip_address, mapped from YANG variable /hide_arp_holder/arp_entry/arp_ip_address (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_arp_ip_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_arp_ip_address() directly.

    YANG Description: IPv4 Address
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="arp-ip-address", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A.B.C.D;; IP address of the ARP entry', u'cli-drop-node-name': None, u'cli-full-no': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """arp_ip_address must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="arp-ip-address", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A.B.C.D;; IP address of the ARP entry', u'cli-drop-node-name': None, u'cli-full-no': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__arp_ip_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_arp_ip_address(self):
    self.__arp_ip_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="arp-ip-address", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A.B.C.D;; IP address of the ARP entry', u'cli-drop-node-name': None, u'cli-full-no': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='inet:ipv4-address', is_config=True)


  def _get_mac_address_value(self):
    """
    Getter method for mac_address_value, mapped from YANG variable /hide_arp_holder/arp_entry/mac_address_value (mac-access-list:mac-address-type)
    """
    return self.__mac_address_value
      
  def _set_mac_address_value(self, v, load=False):
    """
    Setter method for mac_address_value, mapped from YANG variable /hide_arp_holder/arp_entry/mac_address_value (mac-access-list:mac-address-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_address_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_address_value() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mac-address-value", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='mac-access-list:mac-address-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_address_value must be of a type compatible with mac-access-list:mac-address-type""",
          'defined-type': "mac-access-list:mac-address-type",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mac-address-value", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='mac-access-list:mac-address-type', is_config=True)""",
        })

    self.__mac_address_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_address_value(self):
    self.__mac_address_value = YANGDynClass(base=unicode, is_leaf=True, yang_name="mac-address-value", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='mac-access-list:mac-address-type', is_config=True)


  def _get_interfacename(self):
    """
    Getter method for interfacename, mapped from YANG variable /hide_arp_holder/arp_entry/interfacename (enumeration)
    """
    return self.__interfacename
      
  def _set_interfacename(self, v, load=False):
    """
    Setter method for interfacename, mapped from YANG variable /hide_arp_holder/arp_entry/interfacename (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interfacename is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interfacename() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'interface': {}},), is_leaf=True, yang_name="interfacename", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interfacename must be of a type compatible with enumeration""",
          'defined-type': "brocade-arp:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'interface': {}},), is_leaf=True, yang_name="interfacename", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='enumeration', is_config=True)""",
        })

    self.__interfacename = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interfacename(self):
    self.__interfacename = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'interface': {}},), is_leaf=True, yang_name="interfacename", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='enumeration', is_config=True)


  def _get_GigabitEthernet(self):
    """
    Getter method for GigabitEthernet, mapped from YANG variable /hide_arp_holder/arp_entry/GigabitEthernet (interface:interface-type)

    YANG Description: GigabitEthernet
    """
    return self.__GigabitEthernet
      
  def _set_GigabitEthernet(self, v, load=False):
    """
    Setter method for GigabitEthernet, mapped from YANG variable /hide_arp_holder/arp_entry/GigabitEthernet (interface:interface-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_GigabitEthernet is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_GigabitEthernet() directly.

    YANG Description: GigabitEthernet
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="GigabitEthernet", rest_name="GigabitEthernet", parent=self, choice=(u'interfacetype', u'GigabitEthernet'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='interface:interface-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """GigabitEthernet must be of a type compatible with interface:interface-type""",
          'defined-type': "interface:interface-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="GigabitEthernet", rest_name="GigabitEthernet", parent=self, choice=(u'interfacetype', u'GigabitEthernet'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='interface:interface-type', is_config=True)""",
        })

    self.__GigabitEthernet = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_GigabitEthernet(self):
    self.__GigabitEthernet = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="GigabitEthernet", rest_name="GigabitEthernet", parent=self, choice=(u'interfacetype', u'GigabitEthernet'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='interface:interface-type', is_config=True)


  def _get_TenGigabitEthernet(self):
    """
    Getter method for TenGigabitEthernet, mapped from YANG variable /hide_arp_holder/arp_entry/TenGigabitEthernet (interface:interface-type)

    YANG Description: TenGigabitEthernet
    """
    return self.__TenGigabitEthernet
      
  def _set_TenGigabitEthernet(self, v, load=False):
    """
    Setter method for TenGigabitEthernet, mapped from YANG variable /hide_arp_holder/arp_entry/TenGigabitEthernet (interface:interface-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_TenGigabitEthernet is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_TenGigabitEthernet() directly.

    YANG Description: TenGigabitEthernet
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="TenGigabitEthernet", rest_name="TenGigabitEthernet", parent=self, choice=(u'interfacetype', u'TenGigabitEthernet'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='interface:interface-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """TenGigabitEthernet must be of a type compatible with interface:interface-type""",
          'defined-type': "interface:interface-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="TenGigabitEthernet", rest_name="TenGigabitEthernet", parent=self, choice=(u'interfacetype', u'TenGigabitEthernet'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='interface:interface-type', is_config=True)""",
        })

    self.__TenGigabitEthernet = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_TenGigabitEthernet(self):
    self.__TenGigabitEthernet = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="TenGigabitEthernet", rest_name="TenGigabitEthernet", parent=self, choice=(u'interfacetype', u'TenGigabitEthernet'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='interface:interface-type', is_config=True)


  def _get_FortyGigabitEthernet(self):
    """
    Getter method for FortyGigabitEthernet, mapped from YANG variable /hide_arp_holder/arp_entry/FortyGigabitEthernet (interface:interface-type)

    YANG Description: FortyGigabitEthernet
    """
    return self.__FortyGigabitEthernet
      
  def _set_FortyGigabitEthernet(self, v, load=False):
    """
    Setter method for FortyGigabitEthernet, mapped from YANG variable /hide_arp_holder/arp_entry/FortyGigabitEthernet (interface:interface-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_FortyGigabitEthernet is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_FortyGigabitEthernet() directly.

    YANG Description: FortyGigabitEthernet
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="FortyGigabitEthernet", rest_name="FortyGigabitEthernet", parent=self, choice=(u'interfacetype', u'FortyGigabitEthernet'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='interface:interface-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """FortyGigabitEthernet must be of a type compatible with interface:interface-type""",
          'defined-type': "interface:interface-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="FortyGigabitEthernet", rest_name="FortyGigabitEthernet", parent=self, choice=(u'interfacetype', u'FortyGigabitEthernet'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='interface:interface-type', is_config=True)""",
        })

    self.__FortyGigabitEthernet = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_FortyGigabitEthernet(self):
    self.__FortyGigabitEthernet = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="FortyGigabitEthernet", rest_name="FortyGigabitEthernet", parent=self, choice=(u'interfacetype', u'FortyGigabitEthernet'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='interface:interface-type', is_config=True)


  def _get_HundredGigabitEthernet(self):
    """
    Getter method for HundredGigabitEthernet, mapped from YANG variable /hide_arp_holder/arp_entry/HundredGigabitEthernet (interface:interface-type)

    YANG Description: HundredGigabitEthernet
    """
    return self.__HundredGigabitEthernet
      
  def _set_HundredGigabitEthernet(self, v, load=False):
    """
    Setter method for HundredGigabitEthernet, mapped from YANG variable /hide_arp_holder/arp_entry/HundredGigabitEthernet (interface:interface-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_HundredGigabitEthernet is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_HundredGigabitEthernet() directly.

    YANG Description: HundredGigabitEthernet
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="HundredGigabitEthernet", rest_name="HundredGigabitEthernet", parent=self, choice=(u'interfacetype', u'HundredGigabitEthernet'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='interface:interface-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """HundredGigabitEthernet must be of a type compatible with interface:interface-type""",
          'defined-type': "interface:interface-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="HundredGigabitEthernet", rest_name="HundredGigabitEthernet", parent=self, choice=(u'interfacetype', u'HundredGigabitEthernet'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='interface:interface-type', is_config=True)""",
        })

    self.__HundredGigabitEthernet = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_HundredGigabitEthernet(self):
    self.__HundredGigabitEthernet = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="HundredGigabitEthernet", rest_name="HundredGigabitEthernet", parent=self, choice=(u'interfacetype', u'HundredGigabitEthernet'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='interface:interface-type', is_config=True)


  def _get_Ve(self):
    """
    Getter method for Ve, mapped from YANG variable /hide_arp_holder/arp_entry/Ve (interface:vlan-type)

    YANG Description: Ve
    """
    return self.__Ve
      
  def _set_Ve(self, v, load=False):
    """
    Setter method for Ve, mapped from YANG variable /hide_arp_holder/arp_entry/Ve (interface:vlan-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_Ve is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_Ve() directly.

    YANG Description: Ve
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="Ve", rest_name="Ve", parent=self, choice=(u'interfacetype', u'Ve'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='interface:vlan-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """Ve must be of a type compatible with interface:vlan-type""",
          'defined-type': "interface:vlan-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="Ve", rest_name="Ve", parent=self, choice=(u'interfacetype', u'Ve'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='interface:vlan-type', is_config=True)""",
        })

    self.__Ve = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_Ve(self):
    self.__Ve = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="Ve", rest_name="Ve", parent=self, choice=(u'interfacetype', u'Ve'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='interface:vlan-type', is_config=True)

  arp_ip_address = __builtin__.property(_get_arp_ip_address, _set_arp_ip_address)
  mac_address_value = __builtin__.property(_get_mac_address_value, _set_mac_address_value)
  interfacename = __builtin__.property(_get_interfacename, _set_interfacename)
  GigabitEthernet = __builtin__.property(_get_GigabitEthernet, _set_GigabitEthernet)
  TenGigabitEthernet = __builtin__.property(_get_TenGigabitEthernet, _set_TenGigabitEthernet)
  FortyGigabitEthernet = __builtin__.property(_get_FortyGigabitEthernet, _set_FortyGigabitEthernet)
  HundredGigabitEthernet = __builtin__.property(_get_HundredGigabitEthernet, _set_HundredGigabitEthernet)
  Ve = __builtin__.property(_get_Ve, _set_Ve)

  __choices__ = {u'interfacetype': {u'FortyGigabitEthernet': [u'FortyGigabitEthernet'], u'GigabitEthernet': [u'GigabitEthernet'], u'TenGigabitEthernet': [u'TenGigabitEthernet'], u'HundredGigabitEthernet': [u'HundredGigabitEthernet'], u'Ve': [u'Ve']}}
  _pyangbind_elements = {'arp_ip_address': arp_ip_address, 'mac_address_value': mac_address_value, 'interfacename': interfacename, 'GigabitEthernet': GigabitEthernet, 'TenGigabitEthernet': TenGigabitEthernet, 'FortyGigabitEthernet': FortyGigabitEthernet, 'HundredGigabitEthernet': HundredGigabitEthernet, 'Ve': Ve, }


