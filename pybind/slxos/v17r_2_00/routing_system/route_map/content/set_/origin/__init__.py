
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class origin(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/route-map/content/set/origin. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: BGP origin code
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__origin_igp','__origin_incomplete',)

  _yang_name = 'origin'
  _rest_name = 'origin'

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
    self.__origin_incomplete = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="origin-incomplete", rest_name="incomplete", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'unknown heritage', u'alt-name': u'incomplete'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)
    self.__origin_igp = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="origin-igp", rest_name="igp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'local IGP', u'alt-name': u'igp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'route-map', u'content', u'set', u'origin']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'route-map', u'set', u'origin']

  def _get_origin_igp(self):
    """
    Getter method for origin_igp, mapped from YANG variable /routing_system/route_map/content/set/origin/origin_igp (empty)
    """
    return self.__origin_igp
      
  def _set_origin_igp(self, v, load=False):
    """
    Setter method for origin_igp, mapped from YANG variable /routing_system/route_map/content/set/origin/origin_igp (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_origin_igp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_origin_igp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="origin-igp", rest_name="igp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'local IGP', u'alt-name': u'igp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """origin_igp must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="origin-igp", rest_name="igp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'local IGP', u'alt-name': u'igp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)""",
        })

    self.__origin_igp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_origin_igp(self):
    self.__origin_igp = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="origin-igp", rest_name="igp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'local IGP', u'alt-name': u'igp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)


  def _get_origin_incomplete(self):
    """
    Getter method for origin_incomplete, mapped from YANG variable /routing_system/route_map/content/set/origin/origin_incomplete (empty)
    """
    return self.__origin_incomplete
      
  def _set_origin_incomplete(self, v, load=False):
    """
    Setter method for origin_incomplete, mapped from YANG variable /routing_system/route_map/content/set/origin/origin_incomplete (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_origin_incomplete is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_origin_incomplete() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="origin-incomplete", rest_name="incomplete", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'unknown heritage', u'alt-name': u'incomplete'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """origin_incomplete must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="origin-incomplete", rest_name="incomplete", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'unknown heritage', u'alt-name': u'incomplete'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)""",
        })

    self.__origin_incomplete = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_origin_incomplete(self):
    self.__origin_incomplete = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="origin-incomplete", rest_name="incomplete", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'unknown heritage', u'alt-name': u'incomplete'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)

  origin_igp = __builtin__.property(_get_origin_igp, _set_origin_igp)
  origin_incomplete = __builtin__.property(_get_origin_incomplete, _set_origin_incomplete)


  _pyangbind_elements = {'origin_igp': origin_igp, 'origin_incomplete': origin_incomplete, }


