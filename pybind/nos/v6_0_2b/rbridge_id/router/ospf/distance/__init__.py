
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class distance(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/ospf/distance. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__route_type','__dist_value',)

  _yang_name = 'distance'
  _rest_name = 'distance'

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
    self.__route_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'intra-area': {'value': 3}, u'external': {'value': 1}, u'inter-area': {'value': 2}},), is_leaf=True, yang_name="route-type", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The type of route propogation', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='route-type-enum', is_config=True)
    self.__dist_value = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="dist-value", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'The distance for a given type of route'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)

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
      return [u'rbridge-id', u'router', u'ospf', u'distance']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'ospf', u'distance']

  def _get_route_type(self):
    """
    Getter method for route_type, mapped from YANG variable /rbridge_id/router/ospf/distance/route_type (route-type-enum)
    """
    return self.__route_type
      
  def _set_route_type(self, v, load=False):
    """
    Setter method for route_type, mapped from YANG variable /rbridge_id/router/ospf/distance/route_type (route-type-enum)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_type() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'intra-area': {'value': 3}, u'external': {'value': 1}, u'inter-area': {'value': 2}},), is_leaf=True, yang_name="route-type", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The type of route propogation', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='route-type-enum', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_type must be of a type compatible with route-type-enum""",
          'defined-type': "brocade-ospf:route-type-enum",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'intra-area': {'value': 3}, u'external': {'value': 1}, u'inter-area': {'value': 2}},), is_leaf=True, yang_name="route-type", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The type of route propogation', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='route-type-enum', is_config=True)""",
        })

    self.__route_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_type(self):
    self.__route_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'intra-area': {'value': 3}, u'external': {'value': 1}, u'inter-area': {'value': 2}},), is_leaf=True, yang_name="route-type", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The type of route propogation', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='route-type-enum', is_config=True)


  def _get_dist_value(self):
    """
    Getter method for dist_value, mapped from YANG variable /rbridge_id/router/ospf/distance/dist_value (uint32)
    """
    return self.__dist_value
      
  def _set_dist_value(self, v, load=False):
    """
    Setter method for dist_value, mapped from YANG variable /rbridge_id/router/ospf/distance/dist_value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dist_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dist_value() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="dist-value", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'The distance for a given type of route'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dist_value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="dist-value", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'The distance for a given type of route'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)""",
        })

    self.__dist_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dist_value(self):
    self.__dist_value = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="dist-value", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'The distance for a given type of route'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)

  route_type = __builtin__.property(_get_route_type, _set_route_type)
  dist_value = __builtin__.property(_get_dist_value, _set_dist_value)


  _pyangbind_elements = {'route_type': route_type, 'dist_value': dist_value, }


