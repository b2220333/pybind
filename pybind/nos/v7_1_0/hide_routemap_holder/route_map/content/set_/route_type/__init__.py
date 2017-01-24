
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class route_type(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ip-policy - based on the path /hide-routemap-holder/route-map/content/set/route-type. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Route type
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__route_type_rms',)

  _yang_name = 'route-type'
  _rest_name = 'route-type'

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
    self.__route_type_rms = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'type-1': {'value': 2}, u'internal': {'value': 1}, u'type-2': {'value': 3}},), is_leaf=True, yang_name="route-type-rms", rest_name="route-type-rms", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='set-route-type-t', is_config=True)

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
      return [u'hide-routemap-holder', u'route-map', u'content', u'set', u'route-type']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'route-map', u'set', u'route-type']

  def _get_route_type_rms(self):
    """
    Getter method for route_type_rms, mapped from YANG variable /hide_routemap_holder/route_map/content/set/route_type/route_type_rms (set-route-type-t)
    """
    return self.__route_type_rms
      
  def _set_route_type_rms(self, v, load=False):
    """
    Setter method for route_type_rms, mapped from YANG variable /hide_routemap_holder/route_map/content/set/route_type/route_type_rms (set-route-type-t)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_type_rms is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_type_rms() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'type-1': {'value': 2}, u'internal': {'value': 1}, u'type-2': {'value': 3}},), is_leaf=True, yang_name="route-type-rms", rest_name="route-type-rms", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='set-route-type-t', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_type_rms must be of a type compatible with set-route-type-t""",
          'defined-type': "brocade-ip-policy:set-route-type-t",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'type-1': {'value': 2}, u'internal': {'value': 1}, u'type-2': {'value': 3}},), is_leaf=True, yang_name="route-type-rms", rest_name="route-type-rms", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='set-route-type-t', is_config=True)""",
        })

    self.__route_type_rms = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_type_rms(self):
    self.__route_type_rms = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'type-1': {'value': 2}, u'internal': {'value': 1}, u'type-2': {'value': 3}},), is_leaf=True, yang_name="route-type-rms", rest_name="route-type-rms", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='set-route-type-t', is_config=True)

  route_type_rms = __builtin__.property(_get_route_type_rms, _set_route_type_rms)


  _pyangbind_elements = {'route_type_rms': route_type_rms, }


