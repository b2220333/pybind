
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class time_property(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ptp-operational - based on the path /ptp-state/time-property. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: 
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__utc_offset_valid','__utc_offset','__leap59','__leap61','__time_traceable','__frequency_traceable','__timescale','__timesource',)

  _yang_name = 'time-property'
  _rest_name = 'time-property'

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
    self.__utc_offset = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="utc-offset", rest_name="utc-offset", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    self.__frequency_traceable = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="frequency-traceable", rest_name="frequency-traceable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    self.__timesource = YANGDynClass(base=unicode, is_leaf=True, yang_name="timesource", rest_name="timesource", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)
    self.__timescale = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="timescale", rest_name="timescale", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    self.__utc_offset_valid = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="utc-offset-valid", rest_name="utc-offset-valid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    self.__time_traceable = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="time-traceable", rest_name="time-traceable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    self.__leap59 = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="leap59", rest_name="leap59", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    self.__leap61 = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="leap61", rest_name="leap61", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)

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
      return [u'ptp-state', u'time-property']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ptp-state', u'time-property']

  def _get_utc_offset_valid(self):
    """
    Getter method for utc_offset_valid, mapped from YANG variable /ptp_state/time_property/utc_offset_valid (uint32)
    """
    return self.__utc_offset_valid
      
  def _set_utc_offset_valid(self, v, load=False):
    """
    Setter method for utc_offset_valid, mapped from YANG variable /ptp_state/time_property/utc_offset_valid (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_utc_offset_valid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_utc_offset_valid() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="utc-offset-valid", rest_name="utc-offset-valid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """utc_offset_valid must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="utc-offset-valid", rest_name="utc-offset-valid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)""",
        })

    self.__utc_offset_valid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_utc_offset_valid(self):
    self.__utc_offset_valid = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="utc-offset-valid", rest_name="utc-offset-valid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)


  def _get_utc_offset(self):
    """
    Getter method for utc_offset, mapped from YANG variable /ptp_state/time_property/utc_offset (uint32)
    """
    return self.__utc_offset
      
  def _set_utc_offset(self, v, load=False):
    """
    Setter method for utc_offset, mapped from YANG variable /ptp_state/time_property/utc_offset (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_utc_offset is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_utc_offset() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="utc-offset", rest_name="utc-offset", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """utc_offset must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="utc-offset", rest_name="utc-offset", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)""",
        })

    self.__utc_offset = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_utc_offset(self):
    self.__utc_offset = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="utc-offset", rest_name="utc-offset", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)


  def _get_leap59(self):
    """
    Getter method for leap59, mapped from YANG variable /ptp_state/time_property/leap59 (uint32)
    """
    return self.__leap59
      
  def _set_leap59(self, v, load=False):
    """
    Setter method for leap59, mapped from YANG variable /ptp_state/time_property/leap59 (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_leap59 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_leap59() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="leap59", rest_name="leap59", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """leap59 must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="leap59", rest_name="leap59", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)""",
        })

    self.__leap59 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_leap59(self):
    self.__leap59 = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="leap59", rest_name="leap59", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)


  def _get_leap61(self):
    """
    Getter method for leap61, mapped from YANG variable /ptp_state/time_property/leap61 (uint32)
    """
    return self.__leap61
      
  def _set_leap61(self, v, load=False):
    """
    Setter method for leap61, mapped from YANG variable /ptp_state/time_property/leap61 (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_leap61 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_leap61() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="leap61", rest_name="leap61", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """leap61 must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="leap61", rest_name="leap61", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)""",
        })

    self.__leap61 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_leap61(self):
    self.__leap61 = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="leap61", rest_name="leap61", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)


  def _get_time_traceable(self):
    """
    Getter method for time_traceable, mapped from YANG variable /ptp_state/time_property/time_traceable (uint32)
    """
    return self.__time_traceable
      
  def _set_time_traceable(self, v, load=False):
    """
    Setter method for time_traceable, mapped from YANG variable /ptp_state/time_property/time_traceable (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_time_traceable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_time_traceable() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="time-traceable", rest_name="time-traceable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """time_traceable must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="time-traceable", rest_name="time-traceable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)""",
        })

    self.__time_traceable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_time_traceable(self):
    self.__time_traceable = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="time-traceable", rest_name="time-traceable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)


  def _get_frequency_traceable(self):
    """
    Getter method for frequency_traceable, mapped from YANG variable /ptp_state/time_property/frequency_traceable (uint32)
    """
    return self.__frequency_traceable
      
  def _set_frequency_traceable(self, v, load=False):
    """
    Setter method for frequency_traceable, mapped from YANG variable /ptp_state/time_property/frequency_traceable (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_frequency_traceable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_frequency_traceable() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="frequency-traceable", rest_name="frequency-traceable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """frequency_traceable must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="frequency-traceable", rest_name="frequency-traceable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)""",
        })

    self.__frequency_traceable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_frequency_traceable(self):
    self.__frequency_traceable = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="frequency-traceable", rest_name="frequency-traceable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)


  def _get_timescale(self):
    """
    Getter method for timescale, mapped from YANG variable /ptp_state/time_property/timescale (uint32)
    """
    return self.__timescale
      
  def _set_timescale(self, v, load=False):
    """
    Setter method for timescale, mapped from YANG variable /ptp_state/time_property/timescale (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_timescale is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_timescale() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="timescale", rest_name="timescale", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """timescale must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="timescale", rest_name="timescale", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)""",
        })

    self.__timescale = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_timescale(self):
    self.__timescale = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="timescale", rest_name="timescale", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='uint32', is_config=False)


  def _get_timesource(self):
    """
    Getter method for timesource, mapped from YANG variable /ptp_state/time_property/timesource (string)
    """
    return self.__timesource
      
  def _set_timesource(self, v, load=False):
    """
    Setter method for timesource, mapped from YANG variable /ptp_state/time_property/timesource (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_timesource is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_timesource() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="timesource", rest_name="timesource", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """timesource must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="timesource", rest_name="timesource", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)""",
        })

    self.__timesource = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_timesource(self):
    self.__timesource = YANGDynClass(base=unicode, is_leaf=True, yang_name="timesource", rest_name="timesource", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)

  utc_offset_valid = __builtin__.property(_get_utc_offset_valid)
  utc_offset = __builtin__.property(_get_utc_offset)
  leap59 = __builtin__.property(_get_leap59)
  leap61 = __builtin__.property(_get_leap61)
  time_traceable = __builtin__.property(_get_time_traceable)
  frequency_traceable = __builtin__.property(_get_frequency_traceable)
  timescale = __builtin__.property(_get_timescale)
  timesource = __builtin__.property(_get_timesource)


  _pyangbind_elements = {'utc_offset_valid': utc_offset_valid, 'utc_offset': utc_offset, 'leap59': leap59, 'leap61': leap61, 'time_traceable': time_traceable, 'frequency_traceable': frequency_traceable, 'timescale': timescale, 'timesource': timesource, }


