
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class bpdu_drop(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/gigabitethernet/bpdu-drop. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__enable','__direction',)

  _yang_name = 'bpdu-drop'
  _rest_name = 'bpdu-drop'

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
    self.__direction = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'all': {'value': 3}, u'rx': {'value': 1}, u'tx': {'value': 2}},), default=unicode("rx"), is_leaf=True, yang_name="direction", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='enumeration', is_config=True)
    self.__enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Drop all STP/RSTP/MSTP and PVST/RPVST incoming BPDUs'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='empty', is_config=True)

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
      return [u'interface', u'gigabitethernet', u'bpdu-drop']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'GigabitEthernet', u'bpdu-drop']

  def _get_enable(self):
    """
    Getter method for enable, mapped from YANG variable /interface/gigabitethernet/bpdu_drop/enable (empty)
    """
    return self.__enable
      
  def _set_enable(self, v, load=False):
    """
    Setter method for enable, mapped from YANG variable /interface/gigabitethernet/bpdu_drop/enable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Drop all STP/RSTP/MSTP and PVST/RPVST incoming BPDUs'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Drop all STP/RSTP/MSTP and PVST/RPVST incoming BPDUs'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='empty', is_config=True)""",
        })

    self.__enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable(self):
    self.__enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Drop all STP/RSTP/MSTP and PVST/RPVST incoming BPDUs'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='empty', is_config=True)


  def _get_direction(self):
    """
    Getter method for direction, mapped from YANG variable /interface/gigabitethernet/bpdu_drop/direction (enumeration)
    """
    return self.__direction
      
  def _set_direction(self, v, load=False):
    """
    Setter method for direction, mapped from YANG variable /interface/gigabitethernet/bpdu_drop/direction (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_direction is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_direction() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'all': {'value': 3}, u'rx': {'value': 1}, u'tx': {'value': 2}},), default=unicode("rx"), is_leaf=True, yang_name="direction", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """direction must be of a type compatible with enumeration""",
          'defined-type': "brocade-xstp:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'all': {'value': 3}, u'rx': {'value': 1}, u'tx': {'value': 2}},), default=unicode("rx"), is_leaf=True, yang_name="direction", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='enumeration', is_config=True)""",
        })

    self.__direction = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_direction(self):
    self.__direction = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'all': {'value': 3}, u'rx': {'value': 1}, u'tx': {'value': 2}},), default=unicode("rx"), is_leaf=True, yang_name="direction", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='enumeration', is_config=True)

  enable = __builtin__.property(_get_enable, _set_enable)
  direction = __builtin__.property(_get_direction, _set_direction)


  _pyangbind_elements = {'enable': enable, 'direction': direction, }


