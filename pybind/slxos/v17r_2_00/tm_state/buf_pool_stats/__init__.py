
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class buf_pool_stats(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-sysdiag-operational - based on the path /tm-state/buf-pool-stats. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: TM buf pool stats per slot
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__slot','__tower','__dram_size','__bd_occ_core0','__buf_occ_bytes_core0','__bd_occ_core1','__buf_occ_bytes_core1',)

  _yang_name = 'buf-pool-stats'
  _rest_name = 'buf-pool-stats'

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
    self.__slot = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="slot", rest_name="slot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    self.__buf_occ_bytes_core1 = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="buf-occ-bytes-core1", rest_name="buf-occ-bytes-core1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    self.__buf_occ_bytes_core0 = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="buf-occ-bytes-core0", rest_name="buf-occ-bytes-core0", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    self.__bd_occ_core1 = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bd-occ-core1", rest_name="bd-occ-core1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    self.__bd_occ_core0 = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bd-occ-core0", rest_name="bd-occ-core0", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    self.__dram_size = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="dram-size", rest_name="dram-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    self.__tower = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tower", rest_name="tower", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)

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
      return [u'tm-state', u'buf-pool-stats']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'tm-state', u'buf-pool-stats']

  def _get_slot(self):
    """
    Getter method for slot, mapped from YANG variable /tm_state/buf_pool_stats/slot (uint16)

    YANG Description: slot id to get buf pool stats
    """
    return self.__slot
      
  def _set_slot(self, v, load=False):
    """
    Setter method for slot, mapped from YANG variable /tm_state/buf_pool_stats/slot (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_slot is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_slot() directly.

    YANG Description: slot id to get buf pool stats
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="slot", rest_name="slot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """slot must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="slot", rest_name="slot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)""",
        })

    self.__slot = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_slot(self):
    self.__slot = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="slot", rest_name="slot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)


  def _get_tower(self):
    """
    Getter method for tower, mapped from YANG variable /tm_state/buf_pool_stats/tower (uint16)

    YANG Description: tower id to get buf pool stats
    """
    return self.__tower
      
  def _set_tower(self, v, load=False):
    """
    Setter method for tower, mapped from YANG variable /tm_state/buf_pool_stats/tower (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tower is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tower() directly.

    YANG Description: tower id to get buf pool stats
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tower", rest_name="tower", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tower must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tower", rest_name="tower", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)""",
        })

    self.__tower = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tower(self):
    self.__tower = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tower", rest_name="tower", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)


  def _get_dram_size(self):
    """
    Getter method for dram_size, mapped from YANG variable /tm_state/buf_pool_stats/dram_size (uint16)

    YANG Description: dram size in GB
    """
    return self.__dram_size
      
  def _set_dram_size(self, v, load=False):
    """
    Setter method for dram_size, mapped from YANG variable /tm_state/buf_pool_stats/dram_size (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dram_size is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dram_size() directly.

    YANG Description: dram size in GB
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="dram-size", rest_name="dram-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dram_size must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="dram-size", rest_name="dram-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)""",
        })

    self.__dram_size = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dram_size(self):
    self.__dram_size = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="dram-size", rest_name="dram-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)


  def _get_bd_occ_core0(self):
    """
    Getter method for bd_occ_core0, mapped from YANG variable /tm_state/buf_pool_stats/bd_occ_core0 (uint64)

    YANG Description: Occ BD count for Core 0
    """
    return self.__bd_occ_core0
      
  def _set_bd_occ_core0(self, v, load=False):
    """
    Setter method for bd_occ_core0, mapped from YANG variable /tm_state/buf_pool_stats/bd_occ_core0 (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bd_occ_core0 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bd_occ_core0() directly.

    YANG Description: Occ BD count for Core 0
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bd-occ-core0", rest_name="bd-occ-core0", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bd_occ_core0 must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bd-occ-core0", rest_name="bd-occ-core0", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)""",
        })

    self.__bd_occ_core0 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bd_occ_core0(self):
    self.__bd_occ_core0 = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bd-occ-core0", rest_name="bd-occ-core0", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)


  def _get_buf_occ_bytes_core0(self):
    """
    Getter method for buf_occ_bytes_core0, mapped from YANG variable /tm_state/buf_pool_stats/buf_occ_bytes_core0 (uint64)

    YANG Description: Occ Bytes count for core 0
    """
    return self.__buf_occ_bytes_core0
      
  def _set_buf_occ_bytes_core0(self, v, load=False):
    """
    Setter method for buf_occ_bytes_core0, mapped from YANG variable /tm_state/buf_pool_stats/buf_occ_bytes_core0 (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_buf_occ_bytes_core0 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_buf_occ_bytes_core0() directly.

    YANG Description: Occ Bytes count for core 0
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="buf-occ-bytes-core0", rest_name="buf-occ-bytes-core0", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """buf_occ_bytes_core0 must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="buf-occ-bytes-core0", rest_name="buf-occ-bytes-core0", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)""",
        })

    self.__buf_occ_bytes_core0 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_buf_occ_bytes_core0(self):
    self.__buf_occ_bytes_core0 = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="buf-occ-bytes-core0", rest_name="buf-occ-bytes-core0", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)


  def _get_bd_occ_core1(self):
    """
    Getter method for bd_occ_core1, mapped from YANG variable /tm_state/buf_pool_stats/bd_occ_core1 (uint64)

    YANG Description: Occ BD count for core 1
    """
    return self.__bd_occ_core1
      
  def _set_bd_occ_core1(self, v, load=False):
    """
    Setter method for bd_occ_core1, mapped from YANG variable /tm_state/buf_pool_stats/bd_occ_core1 (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bd_occ_core1 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bd_occ_core1() directly.

    YANG Description: Occ BD count for core 1
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bd-occ-core1", rest_name="bd-occ-core1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bd_occ_core1 must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bd-occ-core1", rest_name="bd-occ-core1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)""",
        })

    self.__bd_occ_core1 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bd_occ_core1(self):
    self.__bd_occ_core1 = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bd-occ-core1", rest_name="bd-occ-core1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)


  def _get_buf_occ_bytes_core1(self):
    """
    Getter method for buf_occ_bytes_core1, mapped from YANG variable /tm_state/buf_pool_stats/buf_occ_bytes_core1 (uint64)

    YANG Description: Occ Bytes count for Core 1
    """
    return self.__buf_occ_bytes_core1
      
  def _set_buf_occ_bytes_core1(self, v, load=False):
    """
    Setter method for buf_occ_bytes_core1, mapped from YANG variable /tm_state/buf_pool_stats/buf_occ_bytes_core1 (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_buf_occ_bytes_core1 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_buf_occ_bytes_core1() directly.

    YANG Description: Occ Bytes count for Core 1
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="buf-occ-bytes-core1", rest_name="buf-occ-bytes-core1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """buf_occ_bytes_core1 must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="buf-occ-bytes-core1", rest_name="buf-occ-bytes-core1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)""",
        })

    self.__buf_occ_bytes_core1 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_buf_occ_bytes_core1(self):
    self.__buf_occ_bytes_core1 = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="buf-occ-bytes-core1", rest_name="buf-occ-bytes-core1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)

  slot = __builtin__.property(_get_slot)
  tower = __builtin__.property(_get_tower)
  dram_size = __builtin__.property(_get_dram_size)
  bd_occ_core0 = __builtin__.property(_get_bd_occ_core0)
  buf_occ_bytes_core0 = __builtin__.property(_get_buf_occ_bytes_core0)
  bd_occ_core1 = __builtin__.property(_get_bd_occ_core1)
  buf_occ_bytes_core1 = __builtin__.property(_get_buf_occ_bytes_core1)


  _pyangbind_elements = {'slot': slot, 'tower': tower, 'dram_size': dram_size, 'bd_occ_core0': bd_occ_core0, 'buf_occ_bytes_core0': buf_occ_bytes_core0, 'bd_occ_core1': bd_occ_core1, 'buf_occ_bytes_core1': buf_occ_bytes_core1, }


