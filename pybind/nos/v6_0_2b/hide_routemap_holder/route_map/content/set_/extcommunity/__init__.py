
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import rt
import soo
class extcommunity(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ip-policy - based on the path /hide-routemap-holder/route-map/content/set/extcommunity. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: BGP extended community attribute
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__rt','__soo',)

  _yang_name = 'extcommunity'
  _rest_name = 'extcommunity'

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
    self.__rt = YANGDynClass(base=rt.rt, is_container='container', yang_name="rt", rest_name="rt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route Target extended community'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    self.__soo = YANGDynClass(base=soo.soo, is_container='container', yang_name="soo", rest_name="soo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Site-of-Origin extended community'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)

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
      return [u'hide-routemap-holder', u'route-map', u'content', u'set', u'extcommunity']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'route-map', u'set', u'extcommunity']

  def _get_rt(self):
    """
    Getter method for rt, mapped from YANG variable /hide_routemap_holder/route_map/content/set/extcommunity/rt (container)

    YANG Description: Route Target extended community
    """
    return self.__rt
      
  def _set_rt(self, v, load=False):
    """
    Setter method for rt, mapped from YANG variable /hide_routemap_holder/route_map/content/set/extcommunity/rt (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rt is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rt() directly.

    YANG Description: Route Target extended community
    """
    try:
      t = YANGDynClass(v,base=rt.rt, is_container='container', yang_name="rt", rest_name="rt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route Target extended community'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rt must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=rt.rt, is_container='container', yang_name="rt", rest_name="rt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route Target extended community'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__rt = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rt(self):
    self.__rt = YANGDynClass(base=rt.rt, is_container='container', yang_name="rt", rest_name="rt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route Target extended community'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)


  def _get_soo(self):
    """
    Getter method for soo, mapped from YANG variable /hide_routemap_holder/route_map/content/set/extcommunity/soo (container)

    YANG Description: Site-of-Origin extended community
    """
    return self.__soo
      
  def _set_soo(self, v, load=False):
    """
    Setter method for soo, mapped from YANG variable /hide_routemap_holder/route_map/content/set/extcommunity/soo (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_soo is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_soo() directly.

    YANG Description: Site-of-Origin extended community
    """
    try:
      t = YANGDynClass(v,base=soo.soo, is_container='container', yang_name="soo", rest_name="soo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Site-of-Origin extended community'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """soo must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=soo.soo, is_container='container', yang_name="soo", rest_name="soo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Site-of-Origin extended community'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__soo = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_soo(self):
    self.__soo = YANGDynClass(base=soo.soo, is_container='container', yang_name="soo", rest_name="soo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Site-of-Origin extended community'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)

  rt = __builtin__.property(_get_rt, _set_rt)
  soo = __builtin__.property(_get_soo, _set_soo)


  _pyangbind_elements = {'rt': rt, 'soo': soo, }


