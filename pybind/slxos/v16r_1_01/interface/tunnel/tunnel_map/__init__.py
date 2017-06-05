
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class tunnel_map(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/tunnel/tunnel-map. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__map_vlan','__map_bd','__map_vni',)

  _yang_name = 'tunnel-map'
  _rest_name = 'map'

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
    self.__map_bd = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 4096']}), is_leaf=True, yang_name="map-bd", rest_name="bd", parent=self, choice=(u'map-vlan-bd', u'ca-map-bd'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'bd id range 1 to 4096', u'alt-name': u'bd', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-gre-vxlan', defining_module='brocade-gre-vxlan', yang_type='uint32', is_config=True)
    self.__map_vni = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 16777216']}), is_leaf=True, yang_name="map-vni", rest_name="vni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'vni id range 1 to 16777216', u'alt-name': u'vni'}}, namespace='urn:brocade.com:mgmt:brocade-gre-vxlan', defining_module='brocade-gre-vxlan', yang_type='uint32', is_config=True)
    self.__map_vlan = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 4096']}), is_leaf=True, yang_name="map-vlan", rest_name="vlan", parent=self, choice=(u'map-vlan-bd', u'ca-map-vlan'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'vlan id range 1 to 4096', u'alt-name': u'vlan', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-gre-vxlan', defining_module='brocade-gre-vxlan', yang_type='uint32', is_config=True)

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
      return [u'interface', u'tunnel', u'tunnel-map']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'tunnel', u'map']

  def _get_map_vlan(self):
    """
    Getter method for map_vlan, mapped from YANG variable /interface/tunnel/tunnel_map/map_vlan (uint32)
    """
    return self.__map_vlan
      
  def _set_map_vlan(self, v, load=False):
    """
    Setter method for map_vlan, mapped from YANG variable /interface/tunnel/tunnel_map/map_vlan (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_vlan() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 4096']}), is_leaf=True, yang_name="map-vlan", rest_name="vlan", parent=self, choice=(u'map-vlan-bd', u'ca-map-vlan'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'vlan id range 1 to 4096', u'alt-name': u'vlan', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-gre-vxlan', defining_module='brocade-gre-vxlan', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_vlan must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 4096']}), is_leaf=True, yang_name="map-vlan", rest_name="vlan", parent=self, choice=(u'map-vlan-bd', u'ca-map-vlan'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'vlan id range 1 to 4096', u'alt-name': u'vlan', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-gre-vxlan', defining_module='brocade-gre-vxlan', yang_type='uint32', is_config=True)""",
        })

    self.__map_vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_vlan(self):
    self.__map_vlan = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 4096']}), is_leaf=True, yang_name="map-vlan", rest_name="vlan", parent=self, choice=(u'map-vlan-bd', u'ca-map-vlan'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'vlan id range 1 to 4096', u'alt-name': u'vlan', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-gre-vxlan', defining_module='brocade-gre-vxlan', yang_type='uint32', is_config=True)


  def _get_map_bd(self):
    """
    Getter method for map_bd, mapped from YANG variable /interface/tunnel/tunnel_map/map_bd (uint32)
    """
    return self.__map_bd
      
  def _set_map_bd(self, v, load=False):
    """
    Setter method for map_bd, mapped from YANG variable /interface/tunnel/tunnel_map/map_bd (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_bd is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_bd() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 4096']}), is_leaf=True, yang_name="map-bd", rest_name="bd", parent=self, choice=(u'map-vlan-bd', u'ca-map-bd'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'bd id range 1 to 4096', u'alt-name': u'bd', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-gre-vxlan', defining_module='brocade-gre-vxlan', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_bd must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 4096']}), is_leaf=True, yang_name="map-bd", rest_name="bd", parent=self, choice=(u'map-vlan-bd', u'ca-map-bd'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'bd id range 1 to 4096', u'alt-name': u'bd', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-gre-vxlan', defining_module='brocade-gre-vxlan', yang_type='uint32', is_config=True)""",
        })

    self.__map_bd = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_bd(self):
    self.__map_bd = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 4096']}), is_leaf=True, yang_name="map-bd", rest_name="bd", parent=self, choice=(u'map-vlan-bd', u'ca-map-bd'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'bd id range 1 to 4096', u'alt-name': u'bd', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-gre-vxlan', defining_module='brocade-gre-vxlan', yang_type='uint32', is_config=True)


  def _get_map_vni(self):
    """
    Getter method for map_vni, mapped from YANG variable /interface/tunnel/tunnel_map/map_vni (uint32)
    """
    return self.__map_vni
      
  def _set_map_vni(self, v, load=False):
    """
    Setter method for map_vni, mapped from YANG variable /interface/tunnel/tunnel_map/map_vni (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_vni is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_vni() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 16777216']}), is_leaf=True, yang_name="map-vni", rest_name="vni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'vni id range 1 to 16777216', u'alt-name': u'vni'}}, namespace='urn:brocade.com:mgmt:brocade-gre-vxlan', defining_module='brocade-gre-vxlan', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_vni must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 16777216']}), is_leaf=True, yang_name="map-vni", rest_name="vni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'vni id range 1 to 16777216', u'alt-name': u'vni'}}, namespace='urn:brocade.com:mgmt:brocade-gre-vxlan', defining_module='brocade-gre-vxlan', yang_type='uint32', is_config=True)""",
        })

    self.__map_vni = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_vni(self):
    self.__map_vni = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 16777216']}), is_leaf=True, yang_name="map-vni", rest_name="vni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'vni id range 1 to 16777216', u'alt-name': u'vni'}}, namespace='urn:brocade.com:mgmt:brocade-gre-vxlan', defining_module='brocade-gre-vxlan', yang_type='uint32', is_config=True)

  map_vlan = __builtin__.property(_get_map_vlan, _set_map_vlan)
  map_bd = __builtin__.property(_get_map_bd, _set_map_bd)
  map_vni = __builtin__.property(_get_map_vni, _set_map_vni)

  __choices__ = {u'map-vlan-bd': {u'ca-map-bd': [u'map_bd'], u'ca-map-vlan': [u'map_vlan']}}
  _pyangbind_elements = {'map_vlan': map_vlan, 'map_bd': map_bd, 'map_vni': map_vni, }


