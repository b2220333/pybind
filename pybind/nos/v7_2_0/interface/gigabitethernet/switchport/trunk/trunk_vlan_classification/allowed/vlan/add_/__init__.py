
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class add_(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/gigabitethernet/switchport/trunk/trunk-vlan-classification/allowed/vlan/add. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__trunk_vlan_id','__trunk_ctag_range',)

  _yang_name = 'add'
  _rest_name = 'add'

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
    self.__trunk_vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'4096..8191']}), is_leaf=True, yang_name="trunk-vlan-id", rest_name="trunk-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='non-dot1q-vlan-type', is_config=True)
    self.__trunk_ctag_range = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(409[0-4]))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(409[0-4])))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(409[0-4]))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(409[0-4])))?)?)*', 'length': [u'1..1000']}), is_leaf=True, yang_name="trunk-ctag-range", rest_name="ctag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'ctag'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-ctag-range', is_config=True)

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
      return [u'interface', u'gigabitethernet', u'switchport', u'trunk', u'trunk-vlan-classification', u'allowed', u'vlan', u'add']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'GigabitEthernet', u'switchport', u'trunk', u'allowed', u'vlan', u'add']

  def _get_trunk_vlan_id(self):
    """
    Getter method for trunk_vlan_id, mapped from YANG variable /interface/gigabitethernet/switchport/trunk/trunk_vlan_classification/allowed/vlan/add/trunk_vlan_id (non-dot1q-vlan-type)
    """
    return self.__trunk_vlan_id
      
  def _set_trunk_vlan_id(self, v, load=False):
    """
    Setter method for trunk_vlan_id, mapped from YANG variable /interface/gigabitethernet/switchport/trunk/trunk_vlan_classification/allowed/vlan/add/trunk_vlan_id (non-dot1q-vlan-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk_vlan_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'4096..8191']}), is_leaf=True, yang_name="trunk-vlan-id", rest_name="trunk-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='non-dot1q-vlan-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk_vlan_id must be of a type compatible with non-dot1q-vlan-type""",
          'defined-type': "brocade-interface:non-dot1q-vlan-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'4096..8191']}), is_leaf=True, yang_name="trunk-vlan-id", rest_name="trunk-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='non-dot1q-vlan-type', is_config=True)""",
        })

    self.__trunk_vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk_vlan_id(self):
    self.__trunk_vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'4096..8191']}), is_leaf=True, yang_name="trunk-vlan-id", rest_name="trunk-vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='non-dot1q-vlan-type', is_config=True)


  def _get_trunk_ctag_range(self):
    """
    Getter method for trunk_ctag_range, mapped from YANG variable /interface/gigabitethernet/switchport/trunk/trunk_vlan_classification/allowed/vlan/add/trunk_ctag_range (ui32-ctag-range)
    """
    return self.__trunk_ctag_range
      
  def _set_trunk_ctag_range(self, v, load=False):
    """
    Setter method for trunk_ctag_range, mapped from YANG variable /interface/gigabitethernet/switchport/trunk/trunk_vlan_classification/allowed/vlan/add/trunk_ctag_range (ui32-ctag-range)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk_ctag_range is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk_ctag_range() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(409[0-4]))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(409[0-4])))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(409[0-4]))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(409[0-4])))?)?)*', 'length': [u'1..1000']}), is_leaf=True, yang_name="trunk-ctag-range", rest_name="ctag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'ctag'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-ctag-range', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk_ctag_range must be of a type compatible with ui32-ctag-range""",
          'defined-type': "brocade-interface:ui32-ctag-range",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(409[0-4]))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(409[0-4])))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(409[0-4]))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(409[0-4])))?)?)*', 'length': [u'1..1000']}), is_leaf=True, yang_name="trunk-ctag-range", rest_name="ctag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'ctag'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-ctag-range', is_config=True)""",
        })

    self.__trunk_ctag_range = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk_ctag_range(self):
    self.__trunk_ctag_range = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(409[0-4]))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(409[0-4])))?((,((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(409[0-4]))(-((1[0-9]{1,2})|([2-9][0-9]{0,2})|([1-3][0-9]{3})|(40[0-8][0-9])|(409[0-4])))?)?)*', 'length': [u'1..1000']}), is_leaf=True, yang_name="trunk-ctag-range", rest_name="ctag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'ctag'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-ctag-range', is_config=True)

  trunk_vlan_id = __builtin__.property(_get_trunk_vlan_id, _set_trunk_vlan_id)
  trunk_ctag_range = __builtin__.property(_get_trunk_ctag_range, _set_trunk_ctag_range)


  _pyangbind_elements = {'trunk_vlan_id': trunk_vlan_id, 'trunk_ctag_range': trunk_ctag_range, }


