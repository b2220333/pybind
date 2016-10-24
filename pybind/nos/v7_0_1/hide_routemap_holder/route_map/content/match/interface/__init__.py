
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ip-policy - based on the path /hide-routemap-holder/route-map/content/match/interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Interface name, maxinum 3 values in '[]'
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__tengigabitethernet_rmm','__gigabitethernet_rmm','__fortygigabitethernet_rmm','__hundredgigabitethernet_rmm','__port_channel_rmm','__vlan_rmm','__loopback','__ve',)

  _yang_name = 'interface'
  _rest_name = 'interface'

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
    self.__ve = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']})), is_leaf=False, yang_name="ve", rest_name="ve", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Virtual port'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:ve-type', is_config=True)
    self.__vlan_rmm = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']})), is_leaf=False, yang_name="vlan-rmm", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Vlan', u'hidden': u'full', u'alt-name': u'vlan'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:vlan-type', is_config=True)
    self.__loopback = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']})), is_leaf=False, yang_name="loopback", rest_name="loopback", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Loopback port'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='loopback-intf:intf-loopback-port-type', is_config=True)
    self.__tengigabitethernet_rmm = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']})), is_leaf=False, yang_name="tengigabitethernet-rmm", rest_name="tengigabitethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'TengigabitEthernet', u'alt-name': u'tengigabitethernet'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:interface-type', is_config=True)
    self.__fortygigabitethernet_rmm = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']})), is_leaf=False, yang_name="fortygigabitethernet-rmm", rest_name="fortygigabitethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'FortygigabitEthernet', u'alt-name': u'fortygigabitethernet'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:interface-type', is_config=True)
    self.__port_channel_rmm = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..6144']})), is_leaf=False, yang_name="port-channel-rmm", rest_name="port-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Port_channel', u'alt-name': u'port-channel'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:portchannel-type', is_config=True)
    self.__hundredgigabitethernet_rmm = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']})), is_leaf=False, yang_name="hundredgigabitethernet-rmm", rest_name="hundredgigabitethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'HundredgigabitEthernet', u'alt-name': u'hundredgigabitethernet'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:interface-type', is_config=True)
    self.__gigabitethernet_rmm = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']})), is_leaf=False, yang_name="gigabitethernet-rmm", rest_name="gigabitethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'GigabitEthernet', u'alt-name': u'gigabitethernet'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:interface-type', is_config=True)

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
      return [u'hide-routemap-holder', u'route-map', u'content', u'match', u'interface']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'route-map', u'match', u'interface']

  def _get_tengigabitethernet_rmm(self):
    """
    Getter method for tengigabitethernet_rmm, mapped from YANG variable /hide_routemap_holder/route_map/content/match/interface/tengigabitethernet_rmm (interface:interface-type)

    YANG Description: TengigabitEthernet
    """
    return self.__tengigabitethernet_rmm
      
  def _set_tengigabitethernet_rmm(self, v, load=False):
    """
    Setter method for tengigabitethernet_rmm, mapped from YANG variable /hide_routemap_holder/route_map/content/match/interface/tengigabitethernet_rmm (interface:interface-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tengigabitethernet_rmm is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tengigabitethernet_rmm() directly.

    YANG Description: TengigabitEthernet
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']})), is_leaf=False, yang_name="tengigabitethernet-rmm", rest_name="tengigabitethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'TengigabitEthernet', u'alt-name': u'tengigabitethernet'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:interface-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tengigabitethernet_rmm must be of a type compatible with interface:interface-type""",
          'defined-type': "interface:interface-type",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']})), is_leaf=False, yang_name="tengigabitethernet-rmm", rest_name="tengigabitethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'TengigabitEthernet', u'alt-name': u'tengigabitethernet'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:interface-type', is_config=True)""",
        })

    self.__tengigabitethernet_rmm = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tengigabitethernet_rmm(self):
    self.__tengigabitethernet_rmm = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']})), is_leaf=False, yang_name="tengigabitethernet-rmm", rest_name="tengigabitethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'TengigabitEthernet', u'alt-name': u'tengigabitethernet'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:interface-type', is_config=True)


  def _get_gigabitethernet_rmm(self):
    """
    Getter method for gigabitethernet_rmm, mapped from YANG variable /hide_routemap_holder/route_map/content/match/interface/gigabitethernet_rmm (interface:interface-type)

    YANG Description: GigabitEthernet
    """
    return self.__gigabitethernet_rmm
      
  def _set_gigabitethernet_rmm(self, v, load=False):
    """
    Setter method for gigabitethernet_rmm, mapped from YANG variable /hide_routemap_holder/route_map/content/match/interface/gigabitethernet_rmm (interface:interface-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_gigabitethernet_rmm is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_gigabitethernet_rmm() directly.

    YANG Description: GigabitEthernet
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']})), is_leaf=False, yang_name="gigabitethernet-rmm", rest_name="gigabitethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'GigabitEthernet', u'alt-name': u'gigabitethernet'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:interface-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """gigabitethernet_rmm must be of a type compatible with interface:interface-type""",
          'defined-type': "interface:interface-type",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']})), is_leaf=False, yang_name="gigabitethernet-rmm", rest_name="gigabitethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'GigabitEthernet', u'alt-name': u'gigabitethernet'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:interface-type', is_config=True)""",
        })

    self.__gigabitethernet_rmm = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_gigabitethernet_rmm(self):
    self.__gigabitethernet_rmm = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']})), is_leaf=False, yang_name="gigabitethernet-rmm", rest_name="gigabitethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'GigabitEthernet', u'alt-name': u'gigabitethernet'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:interface-type', is_config=True)


  def _get_fortygigabitethernet_rmm(self):
    """
    Getter method for fortygigabitethernet_rmm, mapped from YANG variable /hide_routemap_holder/route_map/content/match/interface/fortygigabitethernet_rmm (interface:interface-type)

    YANG Description: FortygigabitEthernet
    """
    return self.__fortygigabitethernet_rmm
      
  def _set_fortygigabitethernet_rmm(self, v, load=False):
    """
    Setter method for fortygigabitethernet_rmm, mapped from YANG variable /hide_routemap_holder/route_map/content/match/interface/fortygigabitethernet_rmm (interface:interface-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fortygigabitethernet_rmm is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fortygigabitethernet_rmm() directly.

    YANG Description: FortygigabitEthernet
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']})), is_leaf=False, yang_name="fortygigabitethernet-rmm", rest_name="fortygigabitethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'FortygigabitEthernet', u'alt-name': u'fortygigabitethernet'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:interface-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fortygigabitethernet_rmm must be of a type compatible with interface:interface-type""",
          'defined-type': "interface:interface-type",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']})), is_leaf=False, yang_name="fortygigabitethernet-rmm", rest_name="fortygigabitethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'FortygigabitEthernet', u'alt-name': u'fortygigabitethernet'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:interface-type', is_config=True)""",
        })

    self.__fortygigabitethernet_rmm = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fortygigabitethernet_rmm(self):
    self.__fortygigabitethernet_rmm = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']})), is_leaf=False, yang_name="fortygigabitethernet-rmm", rest_name="fortygigabitethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'FortygigabitEthernet', u'alt-name': u'fortygigabitethernet'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:interface-type', is_config=True)


  def _get_hundredgigabitethernet_rmm(self):
    """
    Getter method for hundredgigabitethernet_rmm, mapped from YANG variable /hide_routemap_holder/route_map/content/match/interface/hundredgigabitethernet_rmm (interface:interface-type)

    YANG Description: HundredgigabitEthernet
    """
    return self.__hundredgigabitethernet_rmm
      
  def _set_hundredgigabitethernet_rmm(self, v, load=False):
    """
    Setter method for hundredgigabitethernet_rmm, mapped from YANG variable /hide_routemap_holder/route_map/content/match/interface/hundredgigabitethernet_rmm (interface:interface-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hundredgigabitethernet_rmm is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hundredgigabitethernet_rmm() directly.

    YANG Description: HundredgigabitEthernet
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']})), is_leaf=False, yang_name="hundredgigabitethernet-rmm", rest_name="hundredgigabitethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'HundredgigabitEthernet', u'alt-name': u'hundredgigabitethernet'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:interface-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hundredgigabitethernet_rmm must be of a type compatible with interface:interface-type""",
          'defined-type': "interface:interface-type",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']})), is_leaf=False, yang_name="hundredgigabitethernet-rmm", rest_name="hundredgigabitethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'HundredgigabitEthernet', u'alt-name': u'hundredgigabitethernet'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:interface-type', is_config=True)""",
        })

    self.__hundredgigabitethernet_rmm = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hundredgigabitethernet_rmm(self):
    self.__hundredgigabitethernet_rmm = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']})), is_leaf=False, yang_name="hundredgigabitethernet-rmm", rest_name="hundredgigabitethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'HundredgigabitEthernet', u'alt-name': u'hundredgigabitethernet'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:interface-type', is_config=True)


  def _get_port_channel_rmm(self):
    """
    Getter method for port_channel_rmm, mapped from YANG variable /hide_routemap_holder/route_map/content/match/interface/port_channel_rmm (interface:portchannel-type)

    YANG Description: Port_channel
    """
    return self.__port_channel_rmm
      
  def _set_port_channel_rmm(self, v, load=False):
    """
    Setter method for port_channel_rmm, mapped from YANG variable /hide_routemap_holder/route_map/content/match/interface/port_channel_rmm (interface:portchannel-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_channel_rmm is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_channel_rmm() directly.

    YANG Description: Port_channel
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..6144']})), is_leaf=False, yang_name="port-channel-rmm", rest_name="port-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Port_channel', u'alt-name': u'port-channel'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:portchannel-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_channel_rmm must be of a type compatible with interface:portchannel-type""",
          'defined-type': "interface:portchannel-type",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..6144']})), is_leaf=False, yang_name="port-channel-rmm", rest_name="port-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Port_channel', u'alt-name': u'port-channel'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:portchannel-type', is_config=True)""",
        })

    self.__port_channel_rmm = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_channel_rmm(self):
    self.__port_channel_rmm = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..6144']})), is_leaf=False, yang_name="port-channel-rmm", rest_name="port-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Port_channel', u'alt-name': u'port-channel'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:portchannel-type', is_config=True)


  def _get_vlan_rmm(self):
    """
    Getter method for vlan_rmm, mapped from YANG variable /hide_routemap_holder/route_map/content/match/interface/vlan_rmm (interface:vlan-type)

    YANG Description: Vlan
    """
    return self.__vlan_rmm
      
  def _set_vlan_rmm(self, v, load=False):
    """
    Setter method for vlan_rmm, mapped from YANG variable /hide_routemap_holder/route_map/content/match/interface/vlan_rmm (interface:vlan-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_rmm is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_rmm() directly.

    YANG Description: Vlan
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']})), is_leaf=False, yang_name="vlan-rmm", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Vlan', u'hidden': u'full', u'alt-name': u'vlan'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:vlan-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_rmm must be of a type compatible with interface:vlan-type""",
          'defined-type': "interface:vlan-type",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']})), is_leaf=False, yang_name="vlan-rmm", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Vlan', u'hidden': u'full', u'alt-name': u'vlan'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:vlan-type', is_config=True)""",
        })

    self.__vlan_rmm = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_rmm(self):
    self.__vlan_rmm = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']})), is_leaf=False, yang_name="vlan-rmm", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Vlan', u'hidden': u'full', u'alt-name': u'vlan'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:vlan-type', is_config=True)


  def _get_loopback(self):
    """
    Getter method for loopback, mapped from YANG variable /hide_routemap_holder/route_map/content/match/interface/loopback (loopback-intf:intf-loopback-port-type)

    YANG Description: Loopback port
    """
    return self.__loopback
      
  def _set_loopback(self, v, load=False):
    """
    Setter method for loopback, mapped from YANG variable /hide_routemap_holder/route_map/content/match/interface/loopback (loopback-intf:intf-loopback-port-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_loopback is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_loopback() directly.

    YANG Description: Loopback port
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']})), is_leaf=False, yang_name="loopback", rest_name="loopback", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Loopback port'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='loopback-intf:intf-loopback-port-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """loopback must be of a type compatible with loopback-intf:intf-loopback-port-type""",
          'defined-type': "loopback-intf:intf-loopback-port-type",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']})), is_leaf=False, yang_name="loopback", rest_name="loopback", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Loopback port'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='loopback-intf:intf-loopback-port-type', is_config=True)""",
        })

    self.__loopback = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_loopback(self):
    self.__loopback = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']})), is_leaf=False, yang_name="loopback", rest_name="loopback", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Loopback port'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='loopback-intf:intf-loopback-port-type', is_config=True)


  def _get_ve(self):
    """
    Getter method for ve, mapped from YANG variable /hide_routemap_holder/route_map/content/match/interface/ve (interface:ve-type)

    YANG Description: Virtual port
    """
    return self.__ve
      
  def _set_ve(self, v, load=False):
    """
    Setter method for ve, mapped from YANG variable /hide_routemap_holder/route_map/content/match/interface/ve (interface:ve-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ve is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ve() directly.

    YANG Description: Virtual port
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']})), is_leaf=False, yang_name="ve", rest_name="ve", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Virtual port'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:ve-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ve must be of a type compatible with interface:ve-type""",
          'defined-type': "interface:ve-type",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']})), is_leaf=False, yang_name="ve", rest_name="ve", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Virtual port'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:ve-type', is_config=True)""",
        })

    self.__ve = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ve(self):
    self.__ve = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']})), is_leaf=False, yang_name="ve", rest_name="ve", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Virtual port'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:ve-type', is_config=True)

  tengigabitethernet_rmm = __builtin__.property(_get_tengigabitethernet_rmm, _set_tengigabitethernet_rmm)
  gigabitethernet_rmm = __builtin__.property(_get_gigabitethernet_rmm, _set_gigabitethernet_rmm)
  fortygigabitethernet_rmm = __builtin__.property(_get_fortygigabitethernet_rmm, _set_fortygigabitethernet_rmm)
  hundredgigabitethernet_rmm = __builtin__.property(_get_hundredgigabitethernet_rmm, _set_hundredgigabitethernet_rmm)
  port_channel_rmm = __builtin__.property(_get_port_channel_rmm, _set_port_channel_rmm)
  vlan_rmm = __builtin__.property(_get_vlan_rmm, _set_vlan_rmm)
  loopback = __builtin__.property(_get_loopback, _set_loopback)
  ve = __builtin__.property(_get_ve, _set_ve)


  _pyangbind_elements = {'tengigabitethernet_rmm': tengigabitethernet_rmm, 'gigabitethernet_rmm': gigabitethernet_rmm, 'fortygigabitethernet_rmm': fortygigabitethernet_rmm, 'hundredgigabitethernet_rmm': hundredgigabitethernet_rmm, 'port_channel_rmm': port_channel_rmm, 'vlan_rmm': vlan_rmm, 'loopback': loopback, 've': ve, }


