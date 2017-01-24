
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class mapping(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/port-channel/switchport/private-vlan/mapping. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Promiscuous mapping
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__promis_pri_pvlan','__oper','__promis_sec_pvlan_range',)

  _yang_name = 'mapping'
  _rest_name = 'mapping'

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
    self.__oper = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'add': {'value': 1}, u'delete': {'value': 2}},), is_leaf=True, yang_name="oper", rest_name="oper", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='secVlan-opp-type', is_config=True)
    self.__promis_pri_pvlan = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="promis-pri-pvlan", rest_name="promis-pri-pvlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Primary vlan id', u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='vlan-type', is_config=True)
    self.__promis_sec_pvlan_range = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?((,(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([3-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="promis-sec-pvlan-range", rest_name="promis-sec-pvlan-range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Secondary vlan range', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-range-8091', is_config=True)

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
      return [u'interface', u'port-channel', u'switchport', u'private-vlan', u'mapping']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Port-channel', u'switchport', u'private-vlan', u'mapping']

  def _get_promis_pri_pvlan(self):
    """
    Getter method for promis_pri_pvlan, mapped from YANG variable /interface/port_channel/switchport/private_vlan/mapping/promis_pri_pvlan (vlan-type)
    """
    return self.__promis_pri_pvlan
      
  def _set_promis_pri_pvlan(self, v, load=False):
    """
    Setter method for promis_pri_pvlan, mapped from YANG variable /interface/port_channel/switchport/private_vlan/mapping/promis_pri_pvlan (vlan-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_promis_pri_pvlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_promis_pri_pvlan() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="promis-pri-pvlan", rest_name="promis-pri-pvlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Primary vlan id', u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='vlan-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """promis_pri_pvlan must be of a type compatible with vlan-type""",
          'defined-type': "brocade-interface:vlan-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="promis-pri-pvlan", rest_name="promis-pri-pvlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Primary vlan id', u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='vlan-type', is_config=True)""",
        })

    self.__promis_pri_pvlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_promis_pri_pvlan(self):
    self.__promis_pri_pvlan = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="promis-pri-pvlan", rest_name="promis-pri-pvlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Primary vlan id', u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='vlan-type', is_config=True)


  def _get_oper(self):
    """
    Getter method for oper, mapped from YANG variable /interface/port_channel/switchport/private_vlan/mapping/oper (secVlan-opp-type)
    """
    return self.__oper
      
  def _set_oper(self, v, load=False):
    """
    Setter method for oper, mapped from YANG variable /interface/port_channel/switchport/private_vlan/mapping/oper (secVlan-opp-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_oper is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_oper() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'add': {'value': 1}, u'delete': {'value': 2}},), is_leaf=True, yang_name="oper", rest_name="oper", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='secVlan-opp-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """oper must be of a type compatible with secVlan-opp-type""",
          'defined-type': "brocade-interface:secVlan-opp-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'add': {'value': 1}, u'delete': {'value': 2}},), is_leaf=True, yang_name="oper", rest_name="oper", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='secVlan-opp-type', is_config=True)""",
        })

    self.__oper = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_oper(self):
    self.__oper = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'add': {'value': 1}, u'delete': {'value': 2}},), is_leaf=True, yang_name="oper", rest_name="oper", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='secVlan-opp-type', is_config=True)


  def _get_promis_sec_pvlan_range(self):
    """
    Getter method for promis_sec_pvlan_range, mapped from YANG variable /interface/port_channel/switchport/private_vlan/mapping/promis_sec_pvlan_range (ui32-range-8091)
    """
    return self.__promis_sec_pvlan_range
      
  def _set_promis_sec_pvlan_range(self, v, load=False):
    """
    Setter method for promis_sec_pvlan_range, mapped from YANG variable /interface/port_channel/switchport/private_vlan/mapping/promis_sec_pvlan_range (ui32-range-8091)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_promis_sec_pvlan_range is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_promis_sec_pvlan_range() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?((,(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([3-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="promis-sec-pvlan-range", rest_name="promis-sec-pvlan-range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Secondary vlan range', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-range-8091', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """promis_sec_pvlan_range must be of a type compatible with ui32-range-8091""",
          'defined-type': "brocade-interface:ui32-range-8091",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?((,(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([3-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="promis-sec-pvlan-range", rest_name="promis-sec-pvlan-range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Secondary vlan range', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-range-8091', is_config=True)""",
        })

    self.__promis_sec_pvlan_range = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_promis_sec_pvlan_range(self):
    self.__promis_sec_pvlan_range = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?((,(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([3-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="promis-sec-pvlan-range", rest_name="promis-sec-pvlan-range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Secondary vlan range', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-range-8091', is_config=True)

  promis_pri_pvlan = __builtin__.property(_get_promis_pri_pvlan, _set_promis_pri_pvlan)
  oper = __builtin__.property(_get_oper, _set_oper)
  promis_sec_pvlan_range = __builtin__.property(_get_promis_sec_pvlan_range, _set_promis_sec_pvlan_range)


  _pyangbind_elements = {'promis_pri_pvlan': promis_pri_pvlan, 'oper': oper, 'promis_sec_pvlan_range': promis_sec_pvlan_range, }


