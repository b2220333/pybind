
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class parent_port_detail(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ptp-operational - based on the path /ptp-state/parent-port-detail. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: 
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__parent_clock_identity','__parent_port_number','__parent_ip_address','__parent_offset','__parent_cpcr','__grandparent_identity','__grandparent_quality_class','__grandparent_quality_accuracy','__grandparent_quality_oslv','__grandparent_quality_priority1','__grandparent_quality_priority2',)

  _yang_name = 'parent-port-detail'
  _rest_name = 'parent-port-detail'

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
    self.__parent_clock_identity = YANGDynClass(base=unicode, is_leaf=True, yang_name="parent-clock-identity", rest_name="parent-clock-identity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)
    self.__grandparent_identity = YANGDynClass(base=unicode, is_leaf=True, yang_name="grandparent-identity", rest_name="grandparent-identity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)
    self.__grandparent_quality_class = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="grandparent-quality-class", rest_name="grandparent-quality-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    self.__grandparent_quality_oslv = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="grandparent-quality-oslv", rest_name="grandparent-quality-oslv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    self.__parent_cpcr = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="parent-cpcr", rest_name="parent-cpcr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='int32', is_config=False)
    self.__parent_port_number = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="parent-port-number", rest_name="parent-port-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    self.__grandparent_quality_accuracy = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="grandparent-quality-accuracy", rest_name="grandparent-quality-accuracy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    self.__parent_ip_address = YANGDynClass(base=unicode, is_leaf=True, yang_name="parent-ip-address", rest_name="parent-ip-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)
    self.__parent_offset = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="parent-offset", rest_name="parent-offset", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='int32', is_config=False)
    self.__grandparent_quality_priority1 = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="grandparent-quality-priority1", rest_name="grandparent-quality-priority1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    self.__grandparent_quality_priority2 = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="grandparent-quality-priority2", rest_name="grandparent-quality-priority2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)

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
      return [u'ptp-state', u'parent-port-detail']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ptp-state', u'parent-port-detail']

  def _get_parent_clock_identity(self):
    """
    Getter method for parent_clock_identity, mapped from YANG variable /ptp_state/parent_port_detail/parent_clock_identity (string)
    """
    return self.__parent_clock_identity
      
  def _set_parent_clock_identity(self, v, load=False):
    """
    Setter method for parent_clock_identity, mapped from YANG variable /ptp_state/parent_port_detail/parent_clock_identity (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_parent_clock_identity is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_parent_clock_identity() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="parent-clock-identity", rest_name="parent-clock-identity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """parent_clock_identity must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="parent-clock-identity", rest_name="parent-clock-identity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)""",
        })

    self.__parent_clock_identity = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_parent_clock_identity(self):
    self.__parent_clock_identity = YANGDynClass(base=unicode, is_leaf=True, yang_name="parent-clock-identity", rest_name="parent-clock-identity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)


  def _get_parent_port_number(self):
    """
    Getter method for parent_port_number, mapped from YANG variable /ptp_state/parent_port_detail/parent_port_number (uint32)
    """
    return self.__parent_port_number
      
  def _set_parent_port_number(self, v, load=False):
    """
    Setter method for parent_port_number, mapped from YANG variable /ptp_state/parent_port_detail/parent_port_number (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_parent_port_number is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_parent_port_number() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="parent-port-number", rest_name="parent-port-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """parent_port_number must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="parent-port-number", rest_name="parent-port-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)""",
        })

    self.__parent_port_number = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_parent_port_number(self):
    self.__parent_port_number = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="parent-port-number", rest_name="parent-port-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)


  def _get_parent_ip_address(self):
    """
    Getter method for parent_ip_address, mapped from YANG variable /ptp_state/parent_port_detail/parent_ip_address (string)
    """
    return self.__parent_ip_address
      
  def _set_parent_ip_address(self, v, load=False):
    """
    Setter method for parent_ip_address, mapped from YANG variable /ptp_state/parent_port_detail/parent_ip_address (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_parent_ip_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_parent_ip_address() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="parent-ip-address", rest_name="parent-ip-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """parent_ip_address must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="parent-ip-address", rest_name="parent-ip-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)""",
        })

    self.__parent_ip_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_parent_ip_address(self):
    self.__parent_ip_address = YANGDynClass(base=unicode, is_leaf=True, yang_name="parent-ip-address", rest_name="parent-ip-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)


  def _get_parent_offset(self):
    """
    Getter method for parent_offset, mapped from YANG variable /ptp_state/parent_port_detail/parent_offset (int32)
    """
    return self.__parent_offset
      
  def _set_parent_offset(self, v, load=False):
    """
    Setter method for parent_offset, mapped from YANG variable /ptp_state/parent_port_detail/parent_offset (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_parent_offset is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_parent_offset() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="parent-offset", rest_name="parent-offset", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='int32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """parent_offset must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="parent-offset", rest_name="parent-offset", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='int32', is_config=False)""",
        })

    self.__parent_offset = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_parent_offset(self):
    self.__parent_offset = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="parent-offset", rest_name="parent-offset", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='int32', is_config=False)


  def _get_parent_cpcr(self):
    """
    Getter method for parent_cpcr, mapped from YANG variable /ptp_state/parent_port_detail/parent_cpcr (int32)
    """
    return self.__parent_cpcr
      
  def _set_parent_cpcr(self, v, load=False):
    """
    Setter method for parent_cpcr, mapped from YANG variable /ptp_state/parent_port_detail/parent_cpcr (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_parent_cpcr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_parent_cpcr() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="parent-cpcr", rest_name="parent-cpcr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='int32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """parent_cpcr must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="parent-cpcr", rest_name="parent-cpcr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='int32', is_config=False)""",
        })

    self.__parent_cpcr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_parent_cpcr(self):
    self.__parent_cpcr = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="parent-cpcr", rest_name="parent-cpcr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='int32', is_config=False)


  def _get_grandparent_identity(self):
    """
    Getter method for grandparent_identity, mapped from YANG variable /ptp_state/parent_port_detail/grandparent_identity (string)
    """
    return self.__grandparent_identity
      
  def _set_grandparent_identity(self, v, load=False):
    """
    Setter method for grandparent_identity, mapped from YANG variable /ptp_state/parent_port_detail/grandparent_identity (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_grandparent_identity is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_grandparent_identity() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="grandparent-identity", rest_name="grandparent-identity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """grandparent_identity must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="grandparent-identity", rest_name="grandparent-identity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)""",
        })

    self.__grandparent_identity = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_grandparent_identity(self):
    self.__grandparent_identity = YANGDynClass(base=unicode, is_leaf=True, yang_name="grandparent-identity", rest_name="grandparent-identity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)


  def _get_grandparent_quality_class(self):
    """
    Getter method for grandparent_quality_class, mapped from YANG variable /ptp_state/parent_port_detail/grandparent_quality_class (uint32)
    """
    return self.__grandparent_quality_class
      
  def _set_grandparent_quality_class(self, v, load=False):
    """
    Setter method for grandparent_quality_class, mapped from YANG variable /ptp_state/parent_port_detail/grandparent_quality_class (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_grandparent_quality_class is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_grandparent_quality_class() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="grandparent-quality-class", rest_name="grandparent-quality-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """grandparent_quality_class must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="grandparent-quality-class", rest_name="grandparent-quality-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)""",
        })

    self.__grandparent_quality_class = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_grandparent_quality_class(self):
    self.__grandparent_quality_class = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="grandparent-quality-class", rest_name="grandparent-quality-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)


  def _get_grandparent_quality_accuracy(self):
    """
    Getter method for grandparent_quality_accuracy, mapped from YANG variable /ptp_state/parent_port_detail/grandparent_quality_accuracy (uint32)
    """
    return self.__grandparent_quality_accuracy
      
  def _set_grandparent_quality_accuracy(self, v, load=False):
    """
    Setter method for grandparent_quality_accuracy, mapped from YANG variable /ptp_state/parent_port_detail/grandparent_quality_accuracy (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_grandparent_quality_accuracy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_grandparent_quality_accuracy() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="grandparent-quality-accuracy", rest_name="grandparent-quality-accuracy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """grandparent_quality_accuracy must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="grandparent-quality-accuracy", rest_name="grandparent-quality-accuracy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)""",
        })

    self.__grandparent_quality_accuracy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_grandparent_quality_accuracy(self):
    self.__grandparent_quality_accuracy = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="grandparent-quality-accuracy", rest_name="grandparent-quality-accuracy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)


  def _get_grandparent_quality_oslv(self):
    """
    Getter method for grandparent_quality_oslv, mapped from YANG variable /ptp_state/parent_port_detail/grandparent_quality_oslv (uint32)
    """
    return self.__grandparent_quality_oslv
      
  def _set_grandparent_quality_oslv(self, v, load=False):
    """
    Setter method for grandparent_quality_oslv, mapped from YANG variable /ptp_state/parent_port_detail/grandparent_quality_oslv (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_grandparent_quality_oslv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_grandparent_quality_oslv() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="grandparent-quality-oslv", rest_name="grandparent-quality-oslv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """grandparent_quality_oslv must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="grandparent-quality-oslv", rest_name="grandparent-quality-oslv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)""",
        })

    self.__grandparent_quality_oslv = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_grandparent_quality_oslv(self):
    self.__grandparent_quality_oslv = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="grandparent-quality-oslv", rest_name="grandparent-quality-oslv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)


  def _get_grandparent_quality_priority1(self):
    """
    Getter method for grandparent_quality_priority1, mapped from YANG variable /ptp_state/parent_port_detail/grandparent_quality_priority1 (uint32)
    """
    return self.__grandparent_quality_priority1
      
  def _set_grandparent_quality_priority1(self, v, load=False):
    """
    Setter method for grandparent_quality_priority1, mapped from YANG variable /ptp_state/parent_port_detail/grandparent_quality_priority1 (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_grandparent_quality_priority1 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_grandparent_quality_priority1() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="grandparent-quality-priority1", rest_name="grandparent-quality-priority1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """grandparent_quality_priority1 must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="grandparent-quality-priority1", rest_name="grandparent-quality-priority1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)""",
        })

    self.__grandparent_quality_priority1 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_grandparent_quality_priority1(self):
    self.__grandparent_quality_priority1 = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="grandparent-quality-priority1", rest_name="grandparent-quality-priority1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)


  def _get_grandparent_quality_priority2(self):
    """
    Getter method for grandparent_quality_priority2, mapped from YANG variable /ptp_state/parent_port_detail/grandparent_quality_priority2 (uint32)
    """
    return self.__grandparent_quality_priority2
      
  def _set_grandparent_quality_priority2(self, v, load=False):
    """
    Setter method for grandparent_quality_priority2, mapped from YANG variable /ptp_state/parent_port_detail/grandparent_quality_priority2 (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_grandparent_quality_priority2 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_grandparent_quality_priority2() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="grandparent-quality-priority2", rest_name="grandparent-quality-priority2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """grandparent_quality_priority2 must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="grandparent-quality-priority2", rest_name="grandparent-quality-priority2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)""",
        })

    self.__grandparent_quality_priority2 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_grandparent_quality_priority2(self):
    self.__grandparent_quality_priority2 = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="grandparent-quality-priority2", rest_name="grandparent-quality-priority2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)

  parent_clock_identity = __builtin__.property(_get_parent_clock_identity)
  parent_port_number = __builtin__.property(_get_parent_port_number)
  parent_ip_address = __builtin__.property(_get_parent_ip_address)
  parent_offset = __builtin__.property(_get_parent_offset)
  parent_cpcr = __builtin__.property(_get_parent_cpcr)
  grandparent_identity = __builtin__.property(_get_grandparent_identity)
  grandparent_quality_class = __builtin__.property(_get_grandparent_quality_class)
  grandparent_quality_accuracy = __builtin__.property(_get_grandparent_quality_accuracy)
  grandparent_quality_oslv = __builtin__.property(_get_grandparent_quality_oslv)
  grandparent_quality_priority1 = __builtin__.property(_get_grandparent_quality_priority1)
  grandparent_quality_priority2 = __builtin__.property(_get_grandparent_quality_priority2)


  _pyangbind_elements = {'parent_clock_identity': parent_clock_identity, 'parent_port_number': parent_port_number, 'parent_ip_address': parent_ip_address, 'parent_offset': parent_offset, 'parent_cpcr': parent_cpcr, 'grandparent_identity': grandparent_identity, 'grandparent_quality_class': grandparent_quality_class, 'grandparent_quality_accuracy': grandparent_quality_accuracy, 'grandparent_quality_oslv': grandparent_quality_oslv, 'grandparent_quality_priority1': grandparent_quality_priority1, 'grandparent_quality_priority2': grandparent_quality_priority2, }


