
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import statistics
class transit_traffic_statistics(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/transit-traffic-statistics. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Transit Traffic Statistics
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__in_label','__protocol','__statistics_valid','__statistics',)

  _yang_name = 'transit-traffic-statistics'
  _rest_name = 'transit-traffic-statistics'

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
    self.__in_label = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="in-label", rest_name="in-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__statistics = YANGDynClass(base=statistics.statistics, is_container='container', yang_name="statistics", rest_name="statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-traffic-statistics-statistics-2'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    self.__protocol = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'mpls-protocol-none': {'value': 0}, u'mpls-protocol-ldp': {'value': 1}, u'mpls-protocol-rsvp': {'value': 2}},), is_leaf=True, yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='mpls-protocol', is_config=False)
    self.__statistics_valid = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="statistics-valid", rest_name="statistics-valid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)

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
      return [u'mpls-state', u'transit-traffic-statistics']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'transit-traffic-statistics']

  def _get_in_label(self):
    """
    Getter method for in_label, mapped from YANG variable /mpls_state/transit_traffic_statistics/in_label (uint32)

    YANG Description: In Label
    """
    return self.__in_label
      
  def _set_in_label(self, v, load=False):
    """
    Setter method for in_label, mapped from YANG variable /mpls_state/transit_traffic_statistics/in_label (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_label is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_label() directly.

    YANG Description: In Label
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="in-label", rest_name="in-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_label must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="in-label", rest_name="in-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__in_label = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_label(self):
    self.__in_label = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="in-label", rest_name="in-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_protocol(self):
    """
    Getter method for protocol, mapped from YANG variable /mpls_state/transit_traffic_statistics/protocol (mpls-protocol)

    YANG Description: MPLS protocol
    """
    return self.__protocol
      
  def _set_protocol(self, v, load=False):
    """
    Setter method for protocol, mapped from YANG variable /mpls_state/transit_traffic_statistics/protocol (mpls-protocol)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protocol is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protocol() directly.

    YANG Description: MPLS protocol
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'mpls-protocol-none': {'value': 0}, u'mpls-protocol-ldp': {'value': 1}, u'mpls-protocol-rsvp': {'value': 2}},), is_leaf=True, yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='mpls-protocol', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protocol must be of a type compatible with mpls-protocol""",
          'defined-type': "brocade-mpls-operational:mpls-protocol",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'mpls-protocol-none': {'value': 0}, u'mpls-protocol-ldp': {'value': 1}, u'mpls-protocol-rsvp': {'value': 2}},), is_leaf=True, yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='mpls-protocol', is_config=False)""",
        })

    self.__protocol = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protocol(self):
    self.__protocol = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'mpls-protocol-none': {'value': 0}, u'mpls-protocol-ldp': {'value': 1}, u'mpls-protocol-rsvp': {'value': 2}},), is_leaf=True, yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='mpls-protocol', is_config=False)


  def _get_statistics_valid(self):
    """
    Getter method for statistics_valid, mapped from YANG variable /mpls_state/transit_traffic_statistics/statistics_valid (boolean)

    YANG Description: Statistics are valid
    """
    return self.__statistics_valid
      
  def _set_statistics_valid(self, v, load=False):
    """
    Setter method for statistics_valid, mapped from YANG variable /mpls_state/transit_traffic_statistics/statistics_valid (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_statistics_valid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_statistics_valid() directly.

    YANG Description: Statistics are valid
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="statistics-valid", rest_name="statistics-valid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """statistics_valid must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="statistics-valid", rest_name="statistics-valid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)""",
        })

    self.__statistics_valid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_statistics_valid(self):
    self.__statistics_valid = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="statistics-valid", rest_name="statistics-valid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)


  def _get_statistics(self):
    """
    Getter method for statistics, mapped from YANG variable /mpls_state/transit_traffic_statistics/statistics (container)
    """
    return self.__statistics
      
  def _set_statistics(self, v, load=False):
    """
    Setter method for statistics, mapped from YANG variable /mpls_state/transit_traffic_statistics/statistics (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_statistics is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_statistics() directly.
    """
    try:
      t = YANGDynClass(v,base=statistics.statistics, is_container='container', yang_name="statistics", rest_name="statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-traffic-statistics-statistics-2'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """statistics must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=statistics.statistics, is_container='container', yang_name="statistics", rest_name="statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-traffic-statistics-statistics-2'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)""",
        })

    self.__statistics = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_statistics(self):
    self.__statistics = YANGDynClass(base=statistics.statistics, is_container='container', yang_name="statistics", rest_name="statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-traffic-statistics-statistics-2'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)

  in_label = __builtin__.property(_get_in_label)
  protocol = __builtin__.property(_get_protocol)
  statistics_valid = __builtin__.property(_get_statistics_valid)
  statistics = __builtin__.property(_get_statistics)


  _pyangbind_elements = {'in_label': in_label, 'protocol': protocol, 'statistics_valid': statistics_valid, 'statistics': statistics, }


