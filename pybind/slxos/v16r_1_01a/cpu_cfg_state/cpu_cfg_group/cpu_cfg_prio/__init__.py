
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class cpu_cfg_prio(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-operational - based on the path /cpu-cfg-state/cpu-cfg-group/cpu-cfg-prio. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: CPU prio shaper/burst/wfq config
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__shaper_rate','__burst_size','__wfq_value','__prio_id',)

  _yang_name = 'cpu-cfg-prio'
  _rest_name = 'cpu-cfg-prio'

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
    self.__wfq_value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="wfq-value", rest_name="wfq-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)
    self.__burst_size = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="burst-size", rest_name="burst-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)
    self.__prio_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="prio-id", rest_name="prio-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='int8', is_config=False)
    self.__shaper_rate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="shaper-rate", rest_name="shaper-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)

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
      return [u'cpu-cfg-state', u'cpu-cfg-group', u'cpu-cfg-prio']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'cpu-cfg-state', u'cpu-cfg-group', u'cpu-cfg-prio']

  def _get_shaper_rate(self):
    """
    Getter method for shaper_rate, mapped from YANG variable /cpu_cfg_state/cpu_cfg_group/cpu_cfg_prio/shaper_rate (uint32)

    YANG Description: QoS CPU shaper rate
    """
    return self.__shaper_rate
      
  def _set_shaper_rate(self, v, load=False):
    """
    Setter method for shaper_rate, mapped from YANG variable /cpu_cfg_state/cpu_cfg_group/cpu_cfg_prio/shaper_rate (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_shaper_rate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_shaper_rate() directly.

    YANG Description: QoS CPU shaper rate
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="shaper-rate", rest_name="shaper-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """shaper_rate must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="shaper-rate", rest_name="shaper-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)""",
        })

    self.__shaper_rate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_shaper_rate(self):
    self.__shaper_rate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="shaper-rate", rest_name="shaper-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)


  def _get_burst_size(self):
    """
    Getter method for burst_size, mapped from YANG variable /cpu_cfg_state/cpu_cfg_group/cpu_cfg_prio/burst_size (uint32)

    YANG Description: QoS CPU shaper burst
    """
    return self.__burst_size
      
  def _set_burst_size(self, v, load=False):
    """
    Setter method for burst_size, mapped from YANG variable /cpu_cfg_state/cpu_cfg_group/cpu_cfg_prio/burst_size (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_burst_size is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_burst_size() directly.

    YANG Description: QoS CPU shaper burst
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="burst-size", rest_name="burst-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """burst_size must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="burst-size", rest_name="burst-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)""",
        })

    self.__burst_size = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_burst_size(self):
    self.__burst_size = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="burst-size", rest_name="burst-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)


  def _get_wfq_value(self):
    """
    Getter method for wfq_value, mapped from YANG variable /cpu_cfg_state/cpu_cfg_group/cpu_cfg_prio/wfq_value (uint32)

    YANG Description: QoS CPU weighted fair queue value
    """
    return self.__wfq_value
      
  def _set_wfq_value(self, v, load=False):
    """
    Setter method for wfq_value, mapped from YANG variable /cpu_cfg_state/cpu_cfg_group/cpu_cfg_prio/wfq_value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_wfq_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_wfq_value() directly.

    YANG Description: QoS CPU weighted fair queue value
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="wfq-value", rest_name="wfq-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """wfq_value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="wfq-value", rest_name="wfq-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)""",
        })

    self.__wfq_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_wfq_value(self):
    self.__wfq_value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="wfq-value", rest_name="wfq-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint32', is_config=False)


  def _get_prio_id(self):
    """
    Getter method for prio_id, mapped from YANG variable /cpu_cfg_state/cpu_cfg_group/cpu_cfg_prio/prio_id (int8)

    YANG Description: CPU Prio ID
    """
    return self.__prio_id
      
  def _set_prio_id(self, v, load=False):
    """
    Setter method for prio_id, mapped from YANG variable /cpu_cfg_state/cpu_cfg_group/cpu_cfg_prio/prio_id (int8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prio_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prio_id() directly.

    YANG Description: CPU Prio ID
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="prio-id", rest_name="prio-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='int8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prio_id must be of a type compatible with int8""",
          'defined-type': "int8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="prio-id", rest_name="prio-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='int8', is_config=False)""",
        })

    self.__prio_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prio_id(self):
    self.__prio_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="prio-id", rest_name="prio-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='int8', is_config=False)

  shaper_rate = __builtin__.property(_get_shaper_rate)
  burst_size = __builtin__.property(_get_burst_size)
  wfq_value = __builtin__.property(_get_wfq_value)
  prio_id = __builtin__.property(_get_prio_id)


  _pyangbind_elements = {'shaper_rate': shaper_rate, 'burst_size': burst_size, 'wfq_value': wfq_value, 'prio_id': prio_id, }


