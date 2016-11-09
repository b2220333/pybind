
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class import_(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/vrf/address-family/ip/unicast/import. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__map_import','__evpn_import',)

  _yang_name = 'import'
  _rest_name = 'import'

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
    self.__evpn_import = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="evpn-import", rest_name="evpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Filter routes from EVPN', u'cli-full-no': None, u'alt-name': u'evpn'}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='empty', is_config=True)
    self.__map_import = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="map-import", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route-map filter to be applied on import route', u'alt-name': u'map', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='route-map-type', is_config=True)

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
      return [u'rbridge-id', u'vrf', u'address-family', u'ip', u'unicast', u'import']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'vrf', u'address-family', u'ipv4', u'unicast', u'import']

  def _get_map_import(self):
    """
    Getter method for map_import, mapped from YANG variable /rbridge_id/vrf/address_family/ip/unicast/import/map_import (route-map-type)
    """
    return self.__map_import
      
  def _set_map_import(self, v, load=False):
    """
    Setter method for map_import, mapped from YANG variable /rbridge_id/vrf/address_family/ip/unicast/import/map_import (route-map-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_import is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_import() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="map-import", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route-map filter to be applied on import route', u'alt-name': u'map', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='route-map-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_import must be of a type compatible with route-map-type""",
          'defined-type': "brocade-vrf:route-map-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="map-import", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route-map filter to be applied on import route', u'alt-name': u'map', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='route-map-type', is_config=True)""",
        })

    self.__map_import = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_import(self):
    self.__map_import = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="map-import", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route-map filter to be applied on import route', u'alt-name': u'map', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='route-map-type', is_config=True)


  def _get_evpn_import(self):
    """
    Getter method for evpn_import, mapped from YANG variable /rbridge_id/vrf/address_family/ip/unicast/import/evpn_import (empty)
    """
    return self.__evpn_import
      
  def _set_evpn_import(self, v, load=False):
    """
    Setter method for evpn_import, mapped from YANG variable /rbridge_id/vrf/address_family/ip/unicast/import/evpn_import (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_evpn_import is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_evpn_import() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="evpn-import", rest_name="evpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Filter routes from EVPN', u'cli-full-no': None, u'alt-name': u'evpn'}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """evpn_import must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="evpn-import", rest_name="evpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Filter routes from EVPN', u'cli-full-no': None, u'alt-name': u'evpn'}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='empty', is_config=True)""",
        })

    self.__evpn_import = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_evpn_import(self):
    self.__evpn_import = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="evpn-import", rest_name="evpn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Filter routes from EVPN', u'cli-full-no': None, u'alt-name': u'evpn'}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='empty', is_config=True)

  map_import = __builtin__.property(_get_map_import, _set_map_import)
  evpn_import = __builtin__.property(_get_evpn_import, _set_evpn_import)


  _pyangbind_elements = {'map_import': map_import, 'evpn_import': evpn_import, }


