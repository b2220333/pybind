
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import load_balancing
import ipv6_track
class ipv6_local_anycast_gateway(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/interface/ve/ipv6/ipv6-local-anycast-gateway. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__local_ipv6_gw_id','__enable_local','__disable_local','__load_balancing','__ipv6_track',)

  _yang_name = 'ipv6-local-anycast-gateway'
  _rest_name = 'fabric-virtual-gateway'

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
    self.__disable_local = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="disable_local", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable Fabric Virtual Gateway', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='empty', is_config=True)
    self.__local_ipv6_gw_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="local-ipv6-gw-id", rest_name="local-ipv6-gw-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'key-default': u'1'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='uint32', is_config=True)
    self.__enable_local = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable_local", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable Fabric Virtual Gateway', u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='empty', is_config=True)
    self.__load_balancing = YANGDynClass(base=load_balancing.load_balancing, is_container='container', presence=False, yang_name="load-balancing", rest_name="load-balancing", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Load balancing'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='container', is_config=True)
    self.__ipv6_track = YANGDynClass(base=ipv6_track.ipv6_track, is_container='container', presence=False, yang_name="ipv6-track", rest_name="track", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Track', u'alt-name': u'track'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='container', is_config=True)

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
      return [u'routing-system', u'interface', u've', u'ipv6', u'ipv6-local-anycast-gateway']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ve', u'ipv6', u'fabric-virtual-gateway']

  def _get_local_ipv6_gw_id(self):
    """
    Getter method for local_ipv6_gw_id, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_local_anycast_gateway/local_ipv6_gw_id (uint32)
    """
    return self.__local_ipv6_gw_id
      
  def _set_local_ipv6_gw_id(self, v, load=False):
    """
    Setter method for local_ipv6_gw_id, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_local_anycast_gateway/local_ipv6_gw_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_ipv6_gw_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_ipv6_gw_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="local-ipv6-gw-id", rest_name="local-ipv6-gw-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'key-default': u'1'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_ipv6_gw_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="local-ipv6-gw-id", rest_name="local-ipv6-gw-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'key-default': u'1'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='uint32', is_config=True)""",
        })

    self.__local_ipv6_gw_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_ipv6_gw_id(self):
    self.__local_ipv6_gw_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="local-ipv6-gw-id", rest_name="local-ipv6-gw-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'key-default': u'1'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='uint32', is_config=True)


  def _get_enable_local(self):
    """
    Getter method for enable_local, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_local_anycast_gateway/enable_local (empty)
    """
    return self.__enable_local
      
  def _set_enable_local(self, v, load=False):
    """
    Setter method for enable_local, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_local_anycast_gateway/enable_local (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable_local is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable_local() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="enable_local", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable Fabric Virtual Gateway', u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable_local must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable_local", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable Fabric Virtual Gateway', u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='empty', is_config=True)""",
        })

    self.__enable_local = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable_local(self):
    self.__enable_local = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable_local", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable Fabric Virtual Gateway', u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='empty', is_config=True)


  def _get_disable_local(self):
    """
    Getter method for disable_local, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_local_anycast_gateway/disable_local (empty)
    """
    return self.__disable_local
      
  def _set_disable_local(self, v, load=False):
    """
    Setter method for disable_local, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_local_anycast_gateway/disable_local (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_disable_local is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_disable_local() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="disable_local", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable Fabric Virtual Gateway', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """disable_local must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="disable_local", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable Fabric Virtual Gateway', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='empty', is_config=True)""",
        })

    self.__disable_local = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_disable_local(self):
    self.__disable_local = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="disable_local", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable Fabric Virtual Gateway', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='empty', is_config=True)


  def _get_load_balancing(self):
    """
    Getter method for load_balancing, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_local_anycast_gateway/load_balancing (container)
    """
    return self.__load_balancing
      
  def _set_load_balancing(self, v, load=False):
    """
    Setter method for load_balancing, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_local_anycast_gateway/load_balancing (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_load_balancing is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_load_balancing() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=load_balancing.load_balancing, is_container='container', presence=False, yang_name="load-balancing", rest_name="load-balancing", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Load balancing'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """load_balancing must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=load_balancing.load_balancing, is_container='container', presence=False, yang_name="load-balancing", rest_name="load-balancing", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Load balancing'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='container', is_config=True)""",
        })

    self.__load_balancing = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_load_balancing(self):
    self.__load_balancing = YANGDynClass(base=load_balancing.load_balancing, is_container='container', presence=False, yang_name="load-balancing", rest_name="load-balancing", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Load balancing'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='container', is_config=True)


  def _get_ipv6_track(self):
    """
    Getter method for ipv6_track, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_local_anycast_gateway/ipv6_track (container)
    """
    return self.__ipv6_track
      
  def _set_ipv6_track(self, v, load=False):
    """
    Setter method for ipv6_track, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_local_anycast_gateway/ipv6_track (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_track is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_track() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ipv6_track.ipv6_track, is_container='container', presence=False, yang_name="ipv6-track", rest_name="track", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Track', u'alt-name': u'track'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_track must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ipv6_track.ipv6_track, is_container='container', presence=False, yang_name="ipv6-track", rest_name="track", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Track', u'alt-name': u'track'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='container', is_config=True)""",
        })

    self.__ipv6_track = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_track(self):
    self.__ipv6_track = YANGDynClass(base=ipv6_track.ipv6_track, is_container='container', presence=False, yang_name="ipv6-track", rest_name="track", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Track', u'alt-name': u'track'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='container', is_config=True)

  local_ipv6_gw_id = __builtin__.property(_get_local_ipv6_gw_id, _set_local_ipv6_gw_id)
  enable_local = __builtin__.property(_get_enable_local, _set_enable_local)
  disable_local = __builtin__.property(_get_disable_local, _set_disable_local)
  load_balancing = __builtin__.property(_get_load_balancing, _set_load_balancing)
  ipv6_track = __builtin__.property(_get_ipv6_track, _set_ipv6_track)


  _pyangbind_elements = {'local_ipv6_gw_id': local_ipv6_gw_id, 'enable_local': enable_local, 'disable_local': disable_local, 'load_balancing': load_balancing, 'ipv6_track': ipv6_track, }


