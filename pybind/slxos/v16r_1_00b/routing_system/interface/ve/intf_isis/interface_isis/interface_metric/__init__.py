
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class interface_metric(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/interface/ve/intf-isis/interface-isis/interface-metric. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__interface_metric_level','__interface_metric_val',)

  _yang_name = 'interface-metric'
  _rest_name = 'metric'

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
    self.__interface_metric_val = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16777215']}), is_leaf=True, yang_name="interface-metric-val", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)
    self.__interface_metric_level = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'level-2': {'value': 2}, u'level-1': {'value': 1}},), is_leaf=True, yang_name="interface-metric-level", rest_name="interface-metric-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='enumeration', is_config=True)

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
      return [u'routing-system', u'interface', u've', u'intf-isis', u'interface-isis', u'interface-metric']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ve', u'isis', u'metric']

  def _get_interface_metric_level(self):
    """
    Getter method for interface_metric_level, mapped from YANG variable /routing_system/interface/ve/intf_isis/interface_isis/interface_metric/interface_metric_level (enumeration)
    """
    return self.__interface_metric_level
      
  def _set_interface_metric_level(self, v, load=False):
    """
    Setter method for interface_metric_level, mapped from YANG variable /routing_system/interface/ve/intf_isis/interface_isis/interface_metric/interface_metric_level (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_metric_level is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_metric_level() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'level-2': {'value': 2}, u'level-1': {'value': 1}},), is_leaf=True, yang_name="interface-metric-level", rest_name="interface-metric-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_metric_level must be of a type compatible with enumeration""",
          'defined-type': "brocade-isis:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'level-2': {'value': 2}, u'level-1': {'value': 1}},), is_leaf=True, yang_name="interface-metric-level", rest_name="interface-metric-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='enumeration', is_config=True)""",
        })

    self.__interface_metric_level = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_metric_level(self):
    self.__interface_metric_level = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'level-2': {'value': 2}, u'level-1': {'value': 1}},), is_leaf=True, yang_name="interface-metric-level", rest_name="interface-metric-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='enumeration', is_config=True)


  def _get_interface_metric_val(self):
    """
    Getter method for interface_metric_val, mapped from YANG variable /routing_system/interface/ve/intf_isis/interface_isis/interface_metric/interface_metric_val (uint32)
    """
    return self.__interface_metric_val
      
  def _set_interface_metric_val(self, v, load=False):
    """
    Setter method for interface_metric_val, mapped from YANG variable /routing_system/interface/ve/intf_isis/interface_isis/interface_metric/interface_metric_val (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_metric_val is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_metric_val() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16777215']}), is_leaf=True, yang_name="interface-metric-val", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_metric_val must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16777215']}), is_leaf=True, yang_name="interface-metric-val", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)""",
        })

    self.__interface_metric_val = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_metric_val(self):
    self.__interface_metric_val = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16777215']}), is_leaf=True, yang_name="interface-metric-val", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)

  interface_metric_level = __builtin__.property(_get_interface_metric_level, _set_interface_metric_level)
  interface_metric_val = __builtin__.property(_get_interface_metric_val, _set_interface_metric_val)


  _pyangbind_elements = {'interface_metric_level': interface_metric_level, 'interface_metric_val': interface_metric_val, }


