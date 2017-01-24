
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class queue_size(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/ethernet/qos/rx-queue/multicast/queue-size. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__traffic_class','__min_queue_size','__max_queue_size',)

  _yang_name = 'queue-size'
  _rest_name = 'queue-size'

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
    self.__traffic_class = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="traffic-class", rest_name="traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Traffic class to configure multicast queue size', u'cli-full-no': None, u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='traffic-class-id-type', is_config=True)
    self.__max_queue_size = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 6142']}), is_leaf=True, yang_name="max-queue-size", rest_name="max-queue-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure maximum queue size'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='max-queue-size-type', is_config=True)
    self.__min_queue_size = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 1024']}), is_leaf=True, yang_name="min-queue-size", rest_name="min-queue-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure minimum queue size', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='min-queue-size-type', is_config=True)

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
      return [u'interface', u'ethernet', u'qos', u'rx-queue', u'multicast', u'queue-size']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ethernet', u'qos', u'rx-queue', u'multicast', u'queue-size']

  def _get_traffic_class(self):
    """
    Getter method for traffic_class, mapped from YANG variable /interface/ethernet/qos/rx_queue/multicast/queue_size/traffic_class (traffic-class-id-type)
    """
    return self.__traffic_class
      
  def _set_traffic_class(self, v, load=False):
    """
    Setter method for traffic_class, mapped from YANG variable /interface/ethernet/qos/rx_queue/multicast/queue_size/traffic_class (traffic-class-id-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_traffic_class is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_traffic_class() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="traffic-class", rest_name="traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Traffic class to configure multicast queue size', u'cli-full-no': None, u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='traffic-class-id-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """traffic_class must be of a type compatible with traffic-class-id-type""",
          'defined-type': "brocade-qos-mls:traffic-class-id-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="traffic-class", rest_name="traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Traffic class to configure multicast queue size', u'cli-full-no': None, u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='traffic-class-id-type', is_config=True)""",
        })

    self.__traffic_class = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_traffic_class(self):
    self.__traffic_class = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="traffic-class", rest_name="traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Traffic class to configure multicast queue size', u'cli-full-no': None, u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='traffic-class-id-type', is_config=True)


  def _get_min_queue_size(self):
    """
    Getter method for min_queue_size, mapped from YANG variable /interface/ethernet/qos/rx_queue/multicast/queue_size/min_queue_size (min-queue-size-type)
    """
    return self.__min_queue_size
      
  def _set_min_queue_size(self, v, load=False):
    """
    Setter method for min_queue_size, mapped from YANG variable /interface/ethernet/qos/rx_queue/multicast/queue_size/min_queue_size (min-queue-size-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_min_queue_size is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_min_queue_size() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 1024']}), is_leaf=True, yang_name="min-queue-size", rest_name="min-queue-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure minimum queue size', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='min-queue-size-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """min_queue_size must be of a type compatible with min-queue-size-type""",
          'defined-type': "brocade-qos-mls:min-queue-size-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 1024']}), is_leaf=True, yang_name="min-queue-size", rest_name="min-queue-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure minimum queue size', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='min-queue-size-type', is_config=True)""",
        })

    self.__min_queue_size = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_min_queue_size(self):
    self.__min_queue_size = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 1024']}), is_leaf=True, yang_name="min-queue-size", rest_name="min-queue-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure minimum queue size', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='min-queue-size-type', is_config=True)


  def _get_max_queue_size(self):
    """
    Getter method for max_queue_size, mapped from YANG variable /interface/ethernet/qos/rx_queue/multicast/queue_size/max_queue_size (max-queue-size-type)
    """
    return self.__max_queue_size
      
  def _set_max_queue_size(self, v, load=False):
    """
    Setter method for max_queue_size, mapped from YANG variable /interface/ethernet/qos/rx_queue/multicast/queue_size/max_queue_size (max-queue-size-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_queue_size is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_queue_size() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 6142']}), is_leaf=True, yang_name="max-queue-size", rest_name="max-queue-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure maximum queue size'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='max-queue-size-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_queue_size must be of a type compatible with max-queue-size-type""",
          'defined-type': "brocade-qos-mls:max-queue-size-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 6142']}), is_leaf=True, yang_name="max-queue-size", rest_name="max-queue-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure maximum queue size'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='max-queue-size-type', is_config=True)""",
        })

    self.__max_queue_size = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_queue_size(self):
    self.__max_queue_size = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 6142']}), is_leaf=True, yang_name="max-queue-size", rest_name="max-queue-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure maximum queue size'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='max-queue-size-type', is_config=True)

  traffic_class = __builtin__.property(_get_traffic_class, _set_traffic_class)
  min_queue_size = __builtin__.property(_get_min_queue_size, _set_min_queue_size)
  max_queue_size = __builtin__.property(_get_max_queue_size, _set_max_queue_size)


  _pyangbind_elements = {'traffic_class': traffic_class, 'min_queue_size': min_queue_size, 'max_queue_size': max_queue_size, }


