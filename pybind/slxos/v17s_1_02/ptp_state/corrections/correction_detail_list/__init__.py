
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class correction_detail_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ptp-operational - based on the path /ptp-state/corrections/correction-detail-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: 
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__slave_port','__sup_time','__correction',)

  _yang_name = 'correction-detail-list'
  _rest_name = 'correction-detail-list'

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
    self.__sup_time = YANGDynClass(base=unicode, is_leaf=True, yang_name="sup-time", rest_name="sup-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)
    self.__correction = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="correction", rest_name="correction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='int32', is_config=False)
    self.__slave_port = YANGDynClass(base=unicode, is_leaf=True, yang_name="slave-port", rest_name="slave-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)

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
      return [u'ptp-state', u'corrections', u'correction-detail-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ptp-state', u'corrections', u'correction-detail-list']

  def _get_slave_port(self):
    """
    Getter method for slave_port, mapped from YANG variable /ptp_state/corrections/correction_detail_list/slave_port (string)
    """
    return self.__slave_port
      
  def _set_slave_port(self, v, load=False):
    """
    Setter method for slave_port, mapped from YANG variable /ptp_state/corrections/correction_detail_list/slave_port (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_slave_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_slave_port() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="slave-port", rest_name="slave-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """slave_port must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="slave-port", rest_name="slave-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)""",
        })

    self.__slave_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_slave_port(self):
    self.__slave_port = YANGDynClass(base=unicode, is_leaf=True, yang_name="slave-port", rest_name="slave-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)


  def _get_sup_time(self):
    """
    Getter method for sup_time, mapped from YANG variable /ptp_state/corrections/correction_detail_list/sup_time (string)
    """
    return self.__sup_time
      
  def _set_sup_time(self, v, load=False):
    """
    Setter method for sup_time, mapped from YANG variable /ptp_state/corrections/correction_detail_list/sup_time (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sup_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sup_time() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="sup-time", rest_name="sup-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sup_time must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="sup-time", rest_name="sup-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)""",
        })

    self.__sup_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sup_time(self):
    self.__sup_time = YANGDynClass(base=unicode, is_leaf=True, yang_name="sup-time", rest_name="sup-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='string', is_config=False)


  def _get_correction(self):
    """
    Getter method for correction, mapped from YANG variable /ptp_state/corrections/correction_detail_list/correction (int32)
    """
    return self.__correction
      
  def _set_correction(self, v, load=False):
    """
    Setter method for correction, mapped from YANG variable /ptp_state/corrections/correction_detail_list/correction (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_correction is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_correction() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="correction", rest_name="correction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='int32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """correction must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="correction", rest_name="correction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='int32', is_config=False)""",
        })

    self.__correction = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_correction(self):
    self.__correction = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="correction", rest_name="correction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ptp-operational', defining_module='brocade-ptp-operational', yang_type='int32', is_config=False)

  slave_port = __builtin__.property(_get_slave_port)
  sup_time = __builtin__.property(_get_sup_time)
  correction = __builtin__.property(_get_correction)


  _pyangbind_elements = {'slave_port': slave_port, 'sup_time': sup_time, 'correction': correction, }


