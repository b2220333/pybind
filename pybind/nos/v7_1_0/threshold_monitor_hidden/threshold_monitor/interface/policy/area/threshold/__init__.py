
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class threshold(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-threshold-monitor - based on the path /threshold-monitor-hidden/threshold-monitor/interface/policy/area/threshold. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__timebase_value','__high_threshold','__low_threshold','__buffer',)

  _yang_name = 'threshold'
  _rest_name = 'threshold'

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
    self.__buffer = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="buffer", rest_name="buffer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Buffer threshold value'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='int32', is_config=True)
    self.__high_threshold = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="high-threshold", rest_name="high-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'High threshold value'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='int32', is_config=True)
    self.__low_threshold = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="low-threshold", rest_name="low-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Low threshold value'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='int32', is_config=True)
    self.__timebase_value = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {'value': 0}, u'hour': {'value': 3}, u'minute': {'value': 2}, u'day': {'value': 4}},), is_leaf=True, yang_name="timebase_value", rest_name="timebase", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure timebase for monitoring', u'alt-name': u'timebase'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='supported-timebase', is_config=True)

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
      return [u'threshold-monitor-hidden', u'threshold-monitor', u'interface', u'policy', u'area', u'threshold']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'threshold-monitor', u'interface', u'policy', u'threshold']

  def _get_timebase_value(self):
    """
    Getter method for timebase_value, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/interface/policy/area/threshold/timebase_value (supported-timebase)
    """
    return self.__timebase_value
      
  def _set_timebase_value(self, v, load=False):
    """
    Setter method for timebase_value, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/interface/policy/area/threshold/timebase_value (supported-timebase)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_timebase_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_timebase_value() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {'value': 0}, u'hour': {'value': 3}, u'minute': {'value': 2}, u'day': {'value': 4}},), is_leaf=True, yang_name="timebase_value", rest_name="timebase", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure timebase for monitoring', u'alt-name': u'timebase'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='supported-timebase', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """timebase_value must be of a type compatible with supported-timebase""",
          'defined-type': "brocade-threshold-monitor:supported-timebase",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {'value': 0}, u'hour': {'value': 3}, u'minute': {'value': 2}, u'day': {'value': 4}},), is_leaf=True, yang_name="timebase_value", rest_name="timebase", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure timebase for monitoring', u'alt-name': u'timebase'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='supported-timebase', is_config=True)""",
        })

    self.__timebase_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_timebase_value(self):
    self.__timebase_value = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {'value': 0}, u'hour': {'value': 3}, u'minute': {'value': 2}, u'day': {'value': 4}},), is_leaf=True, yang_name="timebase_value", rest_name="timebase", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure timebase for monitoring', u'alt-name': u'timebase'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='supported-timebase', is_config=True)


  def _get_high_threshold(self):
    """
    Getter method for high_threshold, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/interface/policy/area/threshold/high_threshold (int32)
    """
    return self.__high_threshold
      
  def _set_high_threshold(self, v, load=False):
    """
    Setter method for high_threshold, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/interface/policy/area/threshold/high_threshold (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_high_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_high_threshold() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="high-threshold", rest_name="high-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'High threshold value'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """high_threshold must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="high-threshold", rest_name="high-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'High threshold value'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='int32', is_config=True)""",
        })

    self.__high_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_high_threshold(self):
    self.__high_threshold = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="high-threshold", rest_name="high-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'High threshold value'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='int32', is_config=True)


  def _get_low_threshold(self):
    """
    Getter method for low_threshold, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/interface/policy/area/threshold/low_threshold (int32)
    """
    return self.__low_threshold
      
  def _set_low_threshold(self, v, load=False):
    """
    Setter method for low_threshold, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/interface/policy/area/threshold/low_threshold (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_low_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_low_threshold() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="low-threshold", rest_name="low-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Low threshold value'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """low_threshold must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="low-threshold", rest_name="low-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Low threshold value'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='int32', is_config=True)""",
        })

    self.__low_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_low_threshold(self):
    self.__low_threshold = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="low-threshold", rest_name="low-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Low threshold value'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='int32', is_config=True)


  def _get_buffer(self):
    """
    Getter method for buffer, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/interface/policy/area/threshold/buffer (int32)
    """
    return self.__buffer
      
  def _set_buffer(self, v, load=False):
    """
    Setter method for buffer, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/interface/policy/area/threshold/buffer (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_buffer is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_buffer() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="buffer", rest_name="buffer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Buffer threshold value'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """buffer must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="buffer", rest_name="buffer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Buffer threshold value'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='int32', is_config=True)""",
        })

    self.__buffer = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_buffer(self):
    self.__buffer = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="buffer", rest_name="buffer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Buffer threshold value'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='int32', is_config=True)

  timebase_value = __builtin__.property(_get_timebase_value, _set_timebase_value)
  high_threshold = __builtin__.property(_get_high_threshold, _set_high_threshold)
  low_threshold = __builtin__.property(_get_low_threshold, _set_low_threshold)
  buffer = __builtin__.property(_get_buffer, _set_buffer)


  _pyangbind_elements = {'timebase_value': timebase_value, 'high_threshold': high_threshold, 'low_threshold': low_threshold, 'buffer': buffer, }


