
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class cpu(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/resource-monitor/cpu. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__enable_cpu','__threshold_cpu','__action_cpu','__sample_rate_cpu','__logging_rate_cpu','__grace_period_cpu','__offset_cpu',)

  _yang_name = 'cpu'
  _rest_name = 'cpu'

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
    self.__action_cpu = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'raslog': {'value': 1}},), is_leaf=True, yang_name="action-cpu", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Action to take when CPU usage exceeds threshold', u'hidden': u'debug', u'alt-name': u'action', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='resource-monitor-actiontype', is_config=True)
    self.__enable_cpu = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable-cpu", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable monitoring CPU usage', u'cli-show-no': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='empty', is_config=True)
    self.__sample_rate_cpu = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 20']}), is_leaf=True, yang_name="sample-rate-cpu", rest_name="sample-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sampling rate for CPU usage monitoring', u'hidden': u'debug', u'alt-name': u'sample-rate', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='uint32', is_config=True)
    self.__threshold_cpu = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'70 .. 100']}), is_leaf=True, yang_name="threshold-cpu", rest_name="threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Threshold for high CPU usage', u'hidden': u'debug', u'alt-name': u'threshold', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='uint32', is_config=True)
    self.__logging_rate_cpu = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'20 .. 60']}), is_leaf=True, yang_name="logging-rate-cpu", rest_name="logging-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Logging rate for CPU usage monitoring', u'hidden': u'debug', u'alt-name': u'logging-rate', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='uint32', is_config=True)
    self.__offset_cpu = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 70']}), is_leaf=True, yang_name="offset-cpu", rest_name="thresh-offset", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Offset to CPU threshold for testing', u'hidden': u'debug', u'alt-name': u'thresh-offset', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='uint32', is_config=True)
    self.__grace_period_cpu = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 720']}), is_leaf=True, yang_name="grace-period-cpu", rest_name="grace-period", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Grace period after CPU usage threshold exceeded', u'hidden': u'debug', u'alt-name': u'grace-period', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='uint32', is_config=True)

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
      return [u'rbridge-id', u'resource-monitor', u'cpu']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'resource-monitor', u'cpu']

  def _get_enable_cpu(self):
    """
    Getter method for enable_cpu, mapped from YANG variable /rbridge_id/resource_monitor/cpu/enable_cpu (empty)
    """
    return self.__enable_cpu
      
  def _set_enable_cpu(self, v, load=False):
    """
    Setter method for enable_cpu, mapped from YANG variable /rbridge_id/resource_monitor/cpu/enable_cpu (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable_cpu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable_cpu() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="enable-cpu", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable monitoring CPU usage', u'cli-show-no': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable_cpu must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable-cpu", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable monitoring CPU usage', u'cli-show-no': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='empty', is_config=True)""",
        })

    self.__enable_cpu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable_cpu(self):
    self.__enable_cpu = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable-cpu", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable monitoring CPU usage', u'cli-show-no': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='empty', is_config=True)


  def _get_threshold_cpu(self):
    """
    Getter method for threshold_cpu, mapped from YANG variable /rbridge_id/resource_monitor/cpu/threshold_cpu (uint32)
    """
    return self.__threshold_cpu
      
  def _set_threshold_cpu(self, v, load=False):
    """
    Setter method for threshold_cpu, mapped from YANG variable /rbridge_id/resource_monitor/cpu/threshold_cpu (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_threshold_cpu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_threshold_cpu() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'70 .. 100']}), is_leaf=True, yang_name="threshold-cpu", rest_name="threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Threshold for high CPU usage', u'hidden': u'debug', u'alt-name': u'threshold', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """threshold_cpu must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'70 .. 100']}), is_leaf=True, yang_name="threshold-cpu", rest_name="threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Threshold for high CPU usage', u'hidden': u'debug', u'alt-name': u'threshold', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='uint32', is_config=True)""",
        })

    self.__threshold_cpu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_threshold_cpu(self):
    self.__threshold_cpu = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'70 .. 100']}), is_leaf=True, yang_name="threshold-cpu", rest_name="threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Threshold for high CPU usage', u'hidden': u'debug', u'alt-name': u'threshold', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='uint32', is_config=True)


  def _get_action_cpu(self):
    """
    Getter method for action_cpu, mapped from YANG variable /rbridge_id/resource_monitor/cpu/action_cpu (resource-monitor-actiontype)
    """
    return self.__action_cpu
      
  def _set_action_cpu(self, v, load=False):
    """
    Setter method for action_cpu, mapped from YANG variable /rbridge_id/resource_monitor/cpu/action_cpu (resource-monitor-actiontype)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_action_cpu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_action_cpu() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'raslog': {'value': 1}},), is_leaf=True, yang_name="action-cpu", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Action to take when CPU usage exceeds threshold', u'hidden': u'debug', u'alt-name': u'action', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='resource-monitor-actiontype', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """action_cpu must be of a type compatible with resource-monitor-actiontype""",
          'defined-type': "brocade-resource-monitor:resource-monitor-actiontype",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'raslog': {'value': 1}},), is_leaf=True, yang_name="action-cpu", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Action to take when CPU usage exceeds threshold', u'hidden': u'debug', u'alt-name': u'action', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='resource-monitor-actiontype', is_config=True)""",
        })

    self.__action_cpu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_action_cpu(self):
    self.__action_cpu = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'raslog': {'value': 1}},), is_leaf=True, yang_name="action-cpu", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Action to take when CPU usage exceeds threshold', u'hidden': u'debug', u'alt-name': u'action', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='resource-monitor-actiontype', is_config=True)


  def _get_sample_rate_cpu(self):
    """
    Getter method for sample_rate_cpu, mapped from YANG variable /rbridge_id/resource_monitor/cpu/sample_rate_cpu (uint32)
    """
    return self.__sample_rate_cpu
      
  def _set_sample_rate_cpu(self, v, load=False):
    """
    Setter method for sample_rate_cpu, mapped from YANG variable /rbridge_id/resource_monitor/cpu/sample_rate_cpu (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sample_rate_cpu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sample_rate_cpu() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 20']}), is_leaf=True, yang_name="sample-rate-cpu", rest_name="sample-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sampling rate for CPU usage monitoring', u'hidden': u'debug', u'alt-name': u'sample-rate', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sample_rate_cpu must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 20']}), is_leaf=True, yang_name="sample-rate-cpu", rest_name="sample-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sampling rate for CPU usage monitoring', u'hidden': u'debug', u'alt-name': u'sample-rate', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='uint32', is_config=True)""",
        })

    self.__sample_rate_cpu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sample_rate_cpu(self):
    self.__sample_rate_cpu = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 20']}), is_leaf=True, yang_name="sample-rate-cpu", rest_name="sample-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sampling rate for CPU usage monitoring', u'hidden': u'debug', u'alt-name': u'sample-rate', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='uint32', is_config=True)


  def _get_logging_rate_cpu(self):
    """
    Getter method for logging_rate_cpu, mapped from YANG variable /rbridge_id/resource_monitor/cpu/logging_rate_cpu (uint32)
    """
    return self.__logging_rate_cpu
      
  def _set_logging_rate_cpu(self, v, load=False):
    """
    Setter method for logging_rate_cpu, mapped from YANG variable /rbridge_id/resource_monitor/cpu/logging_rate_cpu (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_logging_rate_cpu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_logging_rate_cpu() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'20 .. 60']}), is_leaf=True, yang_name="logging-rate-cpu", rest_name="logging-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Logging rate for CPU usage monitoring', u'hidden': u'debug', u'alt-name': u'logging-rate', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """logging_rate_cpu must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'20 .. 60']}), is_leaf=True, yang_name="logging-rate-cpu", rest_name="logging-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Logging rate for CPU usage monitoring', u'hidden': u'debug', u'alt-name': u'logging-rate', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='uint32', is_config=True)""",
        })

    self.__logging_rate_cpu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_logging_rate_cpu(self):
    self.__logging_rate_cpu = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'20 .. 60']}), is_leaf=True, yang_name="logging-rate-cpu", rest_name="logging-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Logging rate for CPU usage monitoring', u'hidden': u'debug', u'alt-name': u'logging-rate', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='uint32', is_config=True)


  def _get_grace_period_cpu(self):
    """
    Getter method for grace_period_cpu, mapped from YANG variable /rbridge_id/resource_monitor/cpu/grace_period_cpu (uint32)
    """
    return self.__grace_period_cpu
      
  def _set_grace_period_cpu(self, v, load=False):
    """
    Setter method for grace_period_cpu, mapped from YANG variable /rbridge_id/resource_monitor/cpu/grace_period_cpu (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_grace_period_cpu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_grace_period_cpu() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 720']}), is_leaf=True, yang_name="grace-period-cpu", rest_name="grace-period", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Grace period after CPU usage threshold exceeded', u'hidden': u'debug', u'alt-name': u'grace-period', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """grace_period_cpu must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 720']}), is_leaf=True, yang_name="grace-period-cpu", rest_name="grace-period", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Grace period after CPU usage threshold exceeded', u'hidden': u'debug', u'alt-name': u'grace-period', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='uint32', is_config=True)""",
        })

    self.__grace_period_cpu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_grace_period_cpu(self):
    self.__grace_period_cpu = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 720']}), is_leaf=True, yang_name="grace-period-cpu", rest_name="grace-period", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Grace period after CPU usage threshold exceeded', u'hidden': u'debug', u'alt-name': u'grace-period', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='uint32', is_config=True)


  def _get_offset_cpu(self):
    """
    Getter method for offset_cpu, mapped from YANG variable /rbridge_id/resource_monitor/cpu/offset_cpu (uint32)
    """
    return self.__offset_cpu
      
  def _set_offset_cpu(self, v, load=False):
    """
    Setter method for offset_cpu, mapped from YANG variable /rbridge_id/resource_monitor/cpu/offset_cpu (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_offset_cpu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_offset_cpu() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 70']}), is_leaf=True, yang_name="offset-cpu", rest_name="thresh-offset", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Offset to CPU threshold for testing', u'hidden': u'debug', u'alt-name': u'thresh-offset', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """offset_cpu must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 70']}), is_leaf=True, yang_name="offset-cpu", rest_name="thresh-offset", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Offset to CPU threshold for testing', u'hidden': u'debug', u'alt-name': u'thresh-offset', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='uint32', is_config=True)""",
        })

    self.__offset_cpu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_offset_cpu(self):
    self.__offset_cpu = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 70']}), is_leaf=True, yang_name="offset-cpu", rest_name="thresh-offset", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Offset to CPU threshold for testing', u'hidden': u'debug', u'alt-name': u'thresh-offset', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-resource-monitor', defining_module='brocade-resource-monitor', yang_type='uint32', is_config=True)

  enable_cpu = __builtin__.property(_get_enable_cpu, _set_enable_cpu)
  threshold_cpu = __builtin__.property(_get_threshold_cpu, _set_threshold_cpu)
  action_cpu = __builtin__.property(_get_action_cpu, _set_action_cpu)
  sample_rate_cpu = __builtin__.property(_get_sample_rate_cpu, _set_sample_rate_cpu)
  logging_rate_cpu = __builtin__.property(_get_logging_rate_cpu, _set_logging_rate_cpu)
  grace_period_cpu = __builtin__.property(_get_grace_period_cpu, _set_grace_period_cpu)
  offset_cpu = __builtin__.property(_get_offset_cpu, _set_offset_cpu)


  _pyangbind_elements = {'enable_cpu': enable_cpu, 'threshold_cpu': threshold_cpu, 'action_cpu': action_cpu, 'sample_rate_cpu': sample_rate_cpu, 'logging_rate_cpu': logging_rate_cpu, 'grace_period_cpu': grace_period_cpu, 'offset_cpu': offset_cpu, }


