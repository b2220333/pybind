
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class port_secutiry_mac_address(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/tengigabitethernet/switchport/port-security/sticky/port-secutiry-mac-address. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Mac Address commands
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mac_address','__port_sec_vlan',)

  _yang_name = 'port-secutiry-mac-address'
  _rest_name = 'port-secutiry-mac-address'

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
    self.__port_sec_vlan = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="port-sec-vlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Forwarding vlan', u'alt-name': u'vlan', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='vlan-type', is_config=True)
    self.__mac_address = YANGDynClass(base=unicode, is_leaf=True, yang_name="mac-address", rest_name="mac-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mac Address', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='mac-address-type', is_config=True)

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
      return [u'interface', u'tengigabitethernet', u'switchport', u'port-security', u'sticky', u'port-secutiry-mac-address']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'TenGigabitEthernet', u'switchport', u'port-security', u'sticky', u'port-secutiry-mac-address']

  def _get_mac_address(self):
    """
    Getter method for mac_address, mapped from YANG variable /interface/tengigabitethernet/switchport/port_security/sticky/port_secutiry_mac_address/mac_address (mac-address-type)

    YANG Description: Mac Address
    """
    return self.__mac_address
      
  def _set_mac_address(self, v, load=False):
    """
    Setter method for mac_address, mapped from YANG variable /interface/tengigabitethernet/switchport/port_security/sticky/port_secutiry_mac_address/mac_address (mac-address-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_address() directly.

    YANG Description: Mac Address
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mac-address", rest_name="mac-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mac Address', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='mac-address-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_address must be of a type compatible with mac-address-type""",
          'defined-type': "brocade-interface:mac-address-type",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mac-address", rest_name="mac-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mac Address', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='mac-address-type', is_config=True)""",
        })

    self.__mac_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_address(self):
    self.__mac_address = YANGDynClass(base=unicode, is_leaf=True, yang_name="mac-address", rest_name="mac-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mac Address', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='mac-address-type', is_config=True)


  def _get_port_sec_vlan(self):
    """
    Getter method for port_sec_vlan, mapped from YANG variable /interface/tengigabitethernet/switchport/port_security/sticky/port_secutiry_mac_address/port_sec_vlan (vlan-type)

    YANG Description: Forwarding vlan
    """
    return self.__port_sec_vlan
      
  def _set_port_sec_vlan(self, v, load=False):
    """
    Setter method for port_sec_vlan, mapped from YANG variable /interface/tengigabitethernet/switchport/port_security/sticky/port_secutiry_mac_address/port_sec_vlan (vlan-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_sec_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_sec_vlan() directly.

    YANG Description: Forwarding vlan
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="port-sec-vlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Forwarding vlan', u'alt-name': u'vlan', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='vlan-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_sec_vlan must be of a type compatible with vlan-type""",
          'defined-type': "brocade-interface:vlan-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="port-sec-vlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Forwarding vlan', u'alt-name': u'vlan', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='vlan-type', is_config=True)""",
        })

    self.__port_sec_vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_sec_vlan(self):
    self.__port_sec_vlan = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="port-sec-vlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Forwarding vlan', u'alt-name': u'vlan', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='vlan-type', is_config=True)

  mac_address = __builtin__.property(_get_mac_address, _set_mac_address)
  port_sec_vlan = __builtin__.property(_get_port_sec_vlan, _set_port_sec_vlan)


  _pyangbind_elements = {'mac_address': mac_address, 'port_sec_vlan': port_sec_vlan, }


