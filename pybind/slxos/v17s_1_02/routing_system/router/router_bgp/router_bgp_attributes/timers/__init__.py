
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class timers(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/router-bgp-attributes/timers. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__keep_alive','__hold_time',)

  _yang_name = 'timers'
  _rest_name = 'timers'

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
    self.__keep_alive = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="keep-alive", rest_name="keep-alive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Keepalive interval', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='nei-keep-alive', is_config=True)
    self.__hold_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="hold-time", rest_name="hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Hold-time value'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='nei-hold-time', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'router-bgp-attributes', u'timers']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'timers']

  def _get_keep_alive(self):
    """
    Getter method for keep_alive, mapped from YANG variable /routing_system/router/router_bgp/router_bgp_attributes/timers/keep_alive (nei-keep-alive)
    """
    return self.__keep_alive
      
  def _set_keep_alive(self, v, load=False):
    """
    Setter method for keep_alive, mapped from YANG variable /routing_system/router/router_bgp/router_bgp_attributes/timers/keep_alive (nei-keep-alive)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_keep_alive is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_keep_alive() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="keep-alive", rest_name="keep-alive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Keepalive interval', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='nei-keep-alive', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """keep_alive must be of a type compatible with nei-keep-alive""",
          'defined-type': "brocade-bgp:nei-keep-alive",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="keep-alive", rest_name="keep-alive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Keepalive interval', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='nei-keep-alive', is_config=True)""",
        })

    self.__keep_alive = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_keep_alive(self):
    self.__keep_alive = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="keep-alive", rest_name="keep-alive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Keepalive interval', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='nei-keep-alive', is_config=True)


  def _get_hold_time(self):
    """
    Getter method for hold_time, mapped from YANG variable /routing_system/router/router_bgp/router_bgp_attributes/timers/hold_time (nei-hold-time)
    """
    return self.__hold_time
      
  def _set_hold_time(self, v, load=False):
    """
    Setter method for hold_time, mapped from YANG variable /routing_system/router/router_bgp/router_bgp_attributes/timers/hold_time (nei-hold-time)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hold_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hold_time() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="hold-time", rest_name="hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Hold-time value'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='nei-hold-time', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hold_time must be of a type compatible with nei-hold-time""",
          'defined-type': "brocade-bgp:nei-hold-time",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="hold-time", rest_name="hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Hold-time value'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='nei-hold-time', is_config=True)""",
        })

    self.__hold_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hold_time(self):
    self.__hold_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="hold-time", rest_name="hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Hold-time value'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='nei-hold-time', is_config=True)

  keep_alive = __builtin__.property(_get_keep_alive, _set_keep_alive)
  hold_time = __builtin__.property(_get_hold_time, _set_hold_time)


  _pyangbind_elements = {'keep_alive': keep_alive, 'hold_time': hold_time, }


