
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class vlan(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/port-channel/switchport/access-mac-group-vlan-classification/access/vlan. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__access_vlan_id','__access_mac_group',)

  _yang_name = 'vlan'
  _rest_name = 'vlan'

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
    self.__access_mac_group = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..500']}), is_leaf=True, yang_name="access-mac-group", rest_name="mac-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Associate a Mac group with a vlan', u'alt-name': u'mac-group', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='mac-group-id-type', is_config=True)
    self.__access_vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="access-vlan-id", rest_name="access-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'info': u'Set the default VLAN for the interface'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='vlan-type', is_config=True)

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
      return [u'interface', u'port-channel', u'switchport', u'access-mac-group-vlan-classification', u'access', u'vlan']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Port-channel', u'switchport', u'access', u'vlan']

  def _get_access_vlan_id(self):
    """
    Getter method for access_vlan_id, mapped from YANG variable /interface/port_channel/switchport/access_mac_group_vlan_classification/access/vlan/access_vlan_id (vlan-type)

    YANG Description: Set the default VLAN for the interface
    """
    return self.__access_vlan_id
      
  def _set_access_vlan_id(self, v, load=False):
    """
    Setter method for access_vlan_id, mapped from YANG variable /interface/port_channel/switchport/access_mac_group_vlan_classification/access/vlan/access_vlan_id (vlan-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_access_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_access_vlan_id() directly.

    YANG Description: Set the default VLAN for the interface
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="access-vlan-id", rest_name="access-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'info': u'Set the default VLAN for the interface'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='vlan-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """access_vlan_id must be of a type compatible with vlan-type""",
          'defined-type': "brocade-interface:vlan-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="access-vlan-id", rest_name="access-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'info': u'Set the default VLAN for the interface'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='vlan-type', is_config=True)""",
        })

    self.__access_vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_access_vlan_id(self):
    self.__access_vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="access-vlan-id", rest_name="access-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'info': u'Set the default VLAN for the interface'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='vlan-type', is_config=True)


  def _get_access_mac_group(self):
    """
    Getter method for access_mac_group, mapped from YANG variable /interface/port_channel/switchport/access_mac_group_vlan_classification/access/vlan/access_mac_group (mac-group-id-type)

    YANG Description: Associate a Mac group with a vlan
    """
    return self.__access_mac_group
      
  def _set_access_mac_group(self, v, load=False):
    """
    Setter method for access_mac_group, mapped from YANG variable /interface/port_channel/switchport/access_mac_group_vlan_classification/access/vlan/access_mac_group (mac-group-id-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_access_mac_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_access_mac_group() directly.

    YANG Description: Associate a Mac group with a vlan
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..500']}), is_leaf=True, yang_name="access-mac-group", rest_name="mac-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Associate a Mac group with a vlan', u'alt-name': u'mac-group', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='mac-group-id-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """access_mac_group must be of a type compatible with mac-group-id-type""",
          'defined-type': "brocade-interface:mac-group-id-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..500']}), is_leaf=True, yang_name="access-mac-group", rest_name="mac-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Associate a Mac group with a vlan', u'alt-name': u'mac-group', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='mac-group-id-type', is_config=True)""",
        })

    self.__access_mac_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_access_mac_group(self):
    self.__access_mac_group = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..500']}), is_leaf=True, yang_name="access-mac-group", rest_name="mac-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Associate a Mac group with a vlan', u'alt-name': u'mac-group', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='mac-group-id-type', is_config=True)

  access_vlan_id = __builtin__.property(_get_access_vlan_id, _set_access_vlan_id)
  access_mac_group = __builtin__.property(_get_access_mac_group, _set_access_mac_group)


  _pyangbind_elements = {'access_vlan_id': access_vlan_id, 'access_mac_group': access_mac_group, }

