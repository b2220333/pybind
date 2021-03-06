
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import route_target
class evpn_bd(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/evpn-config/evpn/evpn-instance/bridge-domain/evpn-bd. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: EVPN instance bridge domain config
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__bd_number','__rd','__route_target',)

  _yang_name = 'evpn-bd'
  _rest_name = 'evpn-bd'

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
    self.__rd = YANGDynClass(base=unicode, is_leaf=True, yang_name="rd", rest_name="rd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RD for the bridge domain.', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rd-type', is_config=True)
    self.__route_target = YANGDynClass(base=route_target.route_target, is_container='container', presence=False, yang_name="route-target", rest_name="route-target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'configure target vpn extended communities', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__bd_number = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="bd-number", rest_name="bd-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bridge-domain:bridge-domain-id-type', is_config=True)

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
      return [u'routing-system', u'evpn-config', u'evpn', u'evpn-instance', u'bridge-domain', u'evpn-bd']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'evpn', u'evpn-instance', u'bridge-domain', u'evpn-bd']

  def _get_bd_number(self):
    """
    Getter method for bd_number, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/bridge_domain/evpn_bd/bd_number (bridge-domain:bridge-domain-id-type)
    """
    return self.__bd_number
      
  def _set_bd_number(self, v, load=False):
    """
    Setter method for bd_number, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/bridge_domain/evpn_bd/bd_number (bridge-domain:bridge-domain-id-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bd_number is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bd_number() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="bd-number", rest_name="bd-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bridge-domain:bridge-domain-id-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bd_number must be of a type compatible with bridge-domain:bridge-domain-id-type""",
          'defined-type': "bridge-domain:bridge-domain-id-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="bd-number", rest_name="bd-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bridge-domain:bridge-domain-id-type', is_config=True)""",
        })

    self.__bd_number = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bd_number(self):
    self.__bd_number = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="bd-number", rest_name="bd-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bridge-domain:bridge-domain-id-type', is_config=True)


  def _get_rd(self):
    """
    Getter method for rd, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/bridge_domain/evpn_bd/rd (rd-type)
    """
    return self.__rd
      
  def _set_rd(self, v, load=False):
    """
    Setter method for rd, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/bridge_domain/evpn_bd/rd (rd-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rd is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rd() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="rd", rest_name="rd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RD for the bridge domain.', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rd-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rd must be of a type compatible with rd-type""",
          'defined-type': "brocade-bgp:rd-type",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="rd", rest_name="rd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RD for the bridge domain.', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rd-type', is_config=True)""",
        })

    self.__rd = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rd(self):
    self.__rd = YANGDynClass(base=unicode, is_leaf=True, yang_name="rd", rest_name="rd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RD for the bridge domain.', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rd-type', is_config=True)


  def _get_route_target(self):
    """
    Getter method for route_target, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/bridge_domain/evpn_bd/route_target (container)
    """
    return self.__route_target
      
  def _set_route_target(self, v, load=False):
    """
    Setter method for route_target, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/bridge_domain/evpn_bd/route_target (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_target is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_target() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=route_target.route_target, is_container='container', presence=False, yang_name="route-target", rest_name="route-target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'configure target vpn extended communities', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_target must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=route_target.route_target, is_container='container', presence=False, yang_name="route-target", rest_name="route-target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'configure target vpn extended communities', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__route_target = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_target(self):
    self.__route_target = YANGDynClass(base=route_target.route_target, is_container='container', presence=False, yang_name="route-target", rest_name="route-target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'configure target vpn extended communities', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

  bd_number = __builtin__.property(_get_bd_number, _set_bd_number)
  rd = __builtin__.property(_get_rd, _set_rd)
  route_target = __builtin__.property(_get_route_target, _set_route_target)


  _pyangbind_elements = {'bd_number': bd_number, 'rd': rd, 'route_target': route_target, }


