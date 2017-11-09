
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import quality
class clock(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ptp-operational - based on the path /ptp-state/clock. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: 
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__type','__identity','__domain','__clock_state','__ptp_port_count','__priority1','__priority2','__offset_from_master','__mpd','__steps_removed','__local_time','__quality',)

  _yang_name = 'clock'
  _rest_name = 'clock'

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
    self.__steps_removed = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="steps-removed", rest_name="steps-removed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    self.__domain = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="domain", rest_name="domain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    self.__quality = YANGDynClass(base=quality.quality, is_container='container', presence=False, yang_name="quality", rest_name="quality", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ptp-clock-quality', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='container', is_config=False)
    self.__mpd = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpd", rest_name="mpd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)
    self.__clock_state = YANGDynClass(base=unicode, is_leaf=True, yang_name="clock-state", rest_name="clock-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)
    self.__priority1 = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="priority1", rest_name="priority1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint8', is_config=False)
    self.__priority2 = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="priority2", rest_name="priority2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint8', is_config=False)
    self.__ptp_port_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ptp-port-count", rest_name="ptp-port-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    self.__local_time = YANGDynClass(base=unicode, is_leaf=True, yang_name="local-time", rest_name="local-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)
    self.__offset_from_master = YANGDynClass(base=unicode, is_leaf=True, yang_name="offset-from-master", rest_name="offset-from-master", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)
    self.__type = YANGDynClass(base=unicode, is_leaf=True, yang_name="type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)
    self.__identity = YANGDynClass(base=unicode, is_leaf=True, yang_name="identity", rest_name="identity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)

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
      return [u'ptp-state', u'clock']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ptp-state', u'clock']

  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /ptp_state/clock/type (string)
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /ptp_state/clock/type (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=unicode, is_leaf=True, yang_name="type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)


  def _get_identity(self):
    """
    Getter method for identity, mapped from YANG variable /ptp_state/clock/identity (string)
    """
    return self.__identity
      
  def _set_identity(self, v, load=False):
    """
    Setter method for identity, mapped from YANG variable /ptp_state/clock/identity (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_identity is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_identity() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="identity", rest_name="identity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """identity must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="identity", rest_name="identity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)""",
        })

    self.__identity = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_identity(self):
    self.__identity = YANGDynClass(base=unicode, is_leaf=True, yang_name="identity", rest_name="identity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)


  def _get_domain(self):
    """
    Getter method for domain, mapped from YANG variable /ptp_state/clock/domain (uint32)
    """
    return self.__domain
      
  def _set_domain(self, v, load=False):
    """
    Setter method for domain, mapped from YANG variable /ptp_state/clock/domain (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_domain is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_domain() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="domain", rest_name="domain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """domain must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="domain", rest_name="domain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)""",
        })

    self.__domain = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_domain(self):
    self.__domain = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="domain", rest_name="domain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)


  def _get_clock_state(self):
    """
    Getter method for clock_state, mapped from YANG variable /ptp_state/clock/clock_state (string)
    """
    return self.__clock_state
      
  def _set_clock_state(self, v, load=False):
    """
    Setter method for clock_state, mapped from YANG variable /ptp_state/clock/clock_state (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_clock_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_clock_state() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="clock-state", rest_name="clock-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """clock_state must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="clock-state", rest_name="clock-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)""",
        })

    self.__clock_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_clock_state(self):
    self.__clock_state = YANGDynClass(base=unicode, is_leaf=True, yang_name="clock-state", rest_name="clock-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)


  def _get_ptp_port_count(self):
    """
    Getter method for ptp_port_count, mapped from YANG variable /ptp_state/clock/ptp_port_count (uint32)
    """
    return self.__ptp_port_count
      
  def _set_ptp_port_count(self, v, load=False):
    """
    Setter method for ptp_port_count, mapped from YANG variable /ptp_state/clock/ptp_port_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ptp_port_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ptp_port_count() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ptp-port-count", rest_name="ptp-port-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ptp_port_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ptp-port-count", rest_name="ptp-port-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)""",
        })

    self.__ptp_port_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ptp_port_count(self):
    self.__ptp_port_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ptp-port-count", rest_name="ptp-port-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)


  def _get_priority1(self):
    """
    Getter method for priority1, mapped from YANG variable /ptp_state/clock/priority1 (uint8)
    """
    return self.__priority1
      
  def _set_priority1(self, v, load=False):
    """
    Setter method for priority1, mapped from YANG variable /ptp_state/clock/priority1 (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority1 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority1() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="priority1", rest_name="priority1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority1 must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="priority1", rest_name="priority1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint8', is_config=False)""",
        })

    self.__priority1 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority1(self):
    self.__priority1 = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="priority1", rest_name="priority1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint8', is_config=False)


  def _get_priority2(self):
    """
    Getter method for priority2, mapped from YANG variable /ptp_state/clock/priority2 (uint8)
    """
    return self.__priority2
      
  def _set_priority2(self, v, load=False):
    """
    Setter method for priority2, mapped from YANG variable /ptp_state/clock/priority2 (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority2 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority2() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="priority2", rest_name="priority2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority2 must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="priority2", rest_name="priority2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint8', is_config=False)""",
        })

    self.__priority2 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority2(self):
    self.__priority2 = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="priority2", rest_name="priority2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint8', is_config=False)


  def _get_offset_from_master(self):
    """
    Getter method for offset_from_master, mapped from YANG variable /ptp_state/clock/offset_from_master (string)
    """
    return self.__offset_from_master
      
  def _set_offset_from_master(self, v, load=False):
    """
    Setter method for offset_from_master, mapped from YANG variable /ptp_state/clock/offset_from_master (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_offset_from_master is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_offset_from_master() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="offset-from-master", rest_name="offset-from-master", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """offset_from_master must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="offset-from-master", rest_name="offset-from-master", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)""",
        })

    self.__offset_from_master = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_offset_from_master(self):
    self.__offset_from_master = YANGDynClass(base=unicode, is_leaf=True, yang_name="offset-from-master", rest_name="offset-from-master", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)


  def _get_mpd(self):
    """
    Getter method for mpd, mapped from YANG variable /ptp_state/clock/mpd (string)
    """
    return self.__mpd
      
  def _set_mpd(self, v, load=False):
    """
    Setter method for mpd, mapped from YANG variable /ptp_state/clock/mpd (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpd is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpd() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mpd", rest_name="mpd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpd must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mpd", rest_name="mpd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)""",
        })

    self.__mpd = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpd(self):
    self.__mpd = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpd", rest_name="mpd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)


  def _get_steps_removed(self):
    """
    Getter method for steps_removed, mapped from YANG variable /ptp_state/clock/steps_removed (uint32)
    """
    return self.__steps_removed
      
  def _set_steps_removed(self, v, load=False):
    """
    Setter method for steps_removed, mapped from YANG variable /ptp_state/clock/steps_removed (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_steps_removed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_steps_removed() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="steps-removed", rest_name="steps-removed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """steps_removed must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="steps-removed", rest_name="steps-removed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)""",
        })

    self.__steps_removed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_steps_removed(self):
    self.__steps_removed = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="steps-removed", rest_name="steps-removed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)


  def _get_local_time(self):
    """
    Getter method for local_time, mapped from YANG variable /ptp_state/clock/local_time (string)
    """
    return self.__local_time
      
  def _set_local_time(self, v, load=False):
    """
    Setter method for local_time, mapped from YANG variable /ptp_state/clock/local_time (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_time() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="local-time", rest_name="local-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_time must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="local-time", rest_name="local-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)""",
        })

    self.__local_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_time(self):
    self.__local_time = YANGDynClass(base=unicode, is_leaf=True, yang_name="local-time", rest_name="local-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)


  def _get_quality(self):
    """
    Getter method for quality, mapped from YANG variable /ptp_state/clock/quality (container)
    """
    return self.__quality
      
  def _set_quality(self, v, load=False):
    """
    Setter method for quality, mapped from YANG variable /ptp_state/clock/quality (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_quality is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_quality() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=quality.quality, is_container='container', presence=False, yang_name="quality", rest_name="quality", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ptp-clock-quality', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """quality must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=quality.quality, is_container='container', presence=False, yang_name="quality", rest_name="quality", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ptp-clock-quality', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='container', is_config=False)""",
        })

    self.__quality = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_quality(self):
    self.__quality = YANGDynClass(base=quality.quality, is_container='container', presence=False, yang_name="quality", rest_name="quality", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ptp-clock-quality', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='container', is_config=False)

  type = __builtin__.property(_get_type)
  identity = __builtin__.property(_get_identity)
  domain = __builtin__.property(_get_domain)
  clock_state = __builtin__.property(_get_clock_state)
  ptp_port_count = __builtin__.property(_get_ptp_port_count)
  priority1 = __builtin__.property(_get_priority1)
  priority2 = __builtin__.property(_get_priority2)
  offset_from_master = __builtin__.property(_get_offset_from_master)
  mpd = __builtin__.property(_get_mpd)
  steps_removed = __builtin__.property(_get_steps_removed)
  local_time = __builtin__.property(_get_local_time)
  quality = __builtin__.property(_get_quality)


  _pyangbind_elements = {'type': type, 'identity': identity, 'domain': domain, 'clock_state': clock_state, 'ptp_port_count': ptp_port_count, 'priority1': priority1, 'priority2': priority2, 'offset_from_master': offset_from_master, 'mpd': mpd, 'steps_removed': steps_removed, 'local_time': local_time, 'quality': quality, }


