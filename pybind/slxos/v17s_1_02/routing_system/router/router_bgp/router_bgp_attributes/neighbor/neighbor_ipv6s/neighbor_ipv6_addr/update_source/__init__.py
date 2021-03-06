
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ethernet_interface
class update_source(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/router-bgp-attributes/neighbor/neighbor-ipv6s/neighbor-ipv6-addr/update-source. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__sip_ipv6_address','__ethernet_interface','__port_channel','__loopback','__ve_interface',)

  _yang_name = 'update-source'
  _rest_name = 'update-source'

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
    self.__ve_interface = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4096']}), is_leaf=True, yang_name="ve-interface", rest_name="ve-interface", parent=self, choice=(u'ch-update-source', u'ca-ve'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Virtual Interface'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='interface:ve-type', is_config=True)
    self.__sip_ipv6_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="sip-ipv6-address", rest_name="sip-ipv6-address", parent=self, choice=(u'ch-update-source', u'ca-ipv6'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='sip-ipv6-address', is_config=True)
    self.__loopback = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="loopback", rest_name="loopback", parent=self, choice=(u'ch-update-source', u'ca-loopback'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Loopback Interface'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='loopback-interface', is_config=True)
    self.__port_channel = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1024']}), is_leaf=True, yang_name="port-channel", rest_name="port-channel", parent=self, choice=(u'ch-update-source', u'ca-port-channel'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Port-channel Interface'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='interface:portchannel-type', is_config=True)
    self.__ethernet_interface = YANGDynClass(base=ethernet_interface.ethernet_interface, is_container='container', presence=False, yang_name="ethernet-interface", rest_name="", parent=self, choice=(u'ch-update-source', u'ca-eth'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'router-bgp-attributes', u'neighbor', u'neighbor-ipv6s', u'neighbor-ipv6-addr', u'update-source']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'neighbor', u'neighbor-ipv6-addr', u'update-source']

  def _get_sip_ipv6_address(self):
    """
    Getter method for sip_ipv6_address, mapped from YANG variable /routing_system/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s/neighbor_ipv6_addr/update_source/sip_ipv6_address (sip-ipv6-address)
    """
    return self.__sip_ipv6_address
      
  def _set_sip_ipv6_address(self, v, load=False):
    """
    Setter method for sip_ipv6_address, mapped from YANG variable /routing_system/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s/neighbor_ipv6_addr/update_source/sip_ipv6_address (sip-ipv6-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sip_ipv6_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sip_ipv6_address() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="sip-ipv6-address", rest_name="sip-ipv6-address", parent=self, choice=(u'ch-update-source', u'ca-ipv6'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='sip-ipv6-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sip_ipv6_address must be of a type compatible with sip-ipv6-address""",
          'defined-type': "brocade-bgp:sip-ipv6-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="sip-ipv6-address", rest_name="sip-ipv6-address", parent=self, choice=(u'ch-update-source', u'ca-ipv6'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='sip-ipv6-address', is_config=True)""",
        })

    self.__sip_ipv6_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sip_ipv6_address(self):
    self.__sip_ipv6_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="sip-ipv6-address", rest_name="sip-ipv6-address", parent=self, choice=(u'ch-update-source', u'ca-ipv6'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='sip-ipv6-address', is_config=True)


  def _get_ethernet_interface(self):
    """
    Getter method for ethernet_interface, mapped from YANG variable /routing_system/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s/neighbor_ipv6_addr/update_source/ethernet_interface (container)
    """
    return self.__ethernet_interface
      
  def _set_ethernet_interface(self, v, load=False):
    """
    Setter method for ethernet_interface, mapped from YANG variable /routing_system/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s/neighbor_ipv6_addr/update_source/ethernet_interface (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ethernet_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ethernet_interface() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ethernet_interface.ethernet_interface, is_container='container', presence=False, yang_name="ethernet-interface", rest_name="", parent=self, choice=(u'ch-update-source', u'ca-eth'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ethernet_interface must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ethernet_interface.ethernet_interface, is_container='container', presence=False, yang_name="ethernet-interface", rest_name="", parent=self, choice=(u'ch-update-source', u'ca-eth'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__ethernet_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ethernet_interface(self):
    self.__ethernet_interface = YANGDynClass(base=ethernet_interface.ethernet_interface, is_container='container', presence=False, yang_name="ethernet-interface", rest_name="", parent=self, choice=(u'ch-update-source', u'ca-eth'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_port_channel(self):
    """
    Getter method for port_channel, mapped from YANG variable /routing_system/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s/neighbor_ipv6_addr/update_source/port_channel (interface:portchannel-type)
    """
    return self.__port_channel
      
  def _set_port_channel(self, v, load=False):
    """
    Setter method for port_channel, mapped from YANG variable /routing_system/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s/neighbor_ipv6_addr/update_source/port_channel (interface:portchannel-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_channel is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_channel() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1024']}), is_leaf=True, yang_name="port-channel", rest_name="port-channel", parent=self, choice=(u'ch-update-source', u'ca-port-channel'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Port-channel Interface'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='interface:portchannel-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_channel must be of a type compatible with interface:portchannel-type""",
          'defined-type': "interface:portchannel-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1024']}), is_leaf=True, yang_name="port-channel", rest_name="port-channel", parent=self, choice=(u'ch-update-source', u'ca-port-channel'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Port-channel Interface'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='interface:portchannel-type', is_config=True)""",
        })

    self.__port_channel = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_channel(self):
    self.__port_channel = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1024']}), is_leaf=True, yang_name="port-channel", rest_name="port-channel", parent=self, choice=(u'ch-update-source', u'ca-port-channel'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Port-channel Interface'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='interface:portchannel-type', is_config=True)


  def _get_loopback(self):
    """
    Getter method for loopback, mapped from YANG variable /routing_system/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s/neighbor_ipv6_addr/update_source/loopback (loopback-interface)
    """
    return self.__loopback
      
  def _set_loopback(self, v, load=False):
    """
    Setter method for loopback, mapped from YANG variable /routing_system/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s/neighbor_ipv6_addr/update_source/loopback (loopback-interface)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_loopback is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_loopback() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="loopback", rest_name="loopback", parent=self, choice=(u'ch-update-source', u'ca-loopback'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Loopback Interface'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='loopback-interface', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """loopback must be of a type compatible with loopback-interface""",
          'defined-type': "brocade-bgp:loopback-interface",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="loopback", rest_name="loopback", parent=self, choice=(u'ch-update-source', u'ca-loopback'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Loopback Interface'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='loopback-interface', is_config=True)""",
        })

    self.__loopback = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_loopback(self):
    self.__loopback = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="loopback", rest_name="loopback", parent=self, choice=(u'ch-update-source', u'ca-loopback'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Loopback Interface'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='loopback-interface', is_config=True)


  def _get_ve_interface(self):
    """
    Getter method for ve_interface, mapped from YANG variable /routing_system/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s/neighbor_ipv6_addr/update_source/ve_interface (interface:ve-type)
    """
    return self.__ve_interface
      
  def _set_ve_interface(self, v, load=False):
    """
    Setter method for ve_interface, mapped from YANG variable /routing_system/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s/neighbor_ipv6_addr/update_source/ve_interface (interface:ve-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ve_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ve_interface() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4096']}), is_leaf=True, yang_name="ve-interface", rest_name="ve-interface", parent=self, choice=(u'ch-update-source', u'ca-ve'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Virtual Interface'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='interface:ve-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ve_interface must be of a type compatible with interface:ve-type""",
          'defined-type': "interface:ve-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4096']}), is_leaf=True, yang_name="ve-interface", rest_name="ve-interface", parent=self, choice=(u'ch-update-source', u'ca-ve'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Virtual Interface'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='interface:ve-type', is_config=True)""",
        })

    self.__ve_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ve_interface(self):
    self.__ve_interface = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4096']}), is_leaf=True, yang_name="ve-interface", rest_name="ve-interface", parent=self, choice=(u'ch-update-source', u'ca-ve'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Virtual Interface'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='interface:ve-type', is_config=True)

  sip_ipv6_address = __builtin__.property(_get_sip_ipv6_address, _set_sip_ipv6_address)
  ethernet_interface = __builtin__.property(_get_ethernet_interface, _set_ethernet_interface)
  port_channel = __builtin__.property(_get_port_channel, _set_port_channel)
  loopback = __builtin__.property(_get_loopback, _set_loopback)
  ve_interface = __builtin__.property(_get_ve_interface, _set_ve_interface)

  __choices__ = {u'ch-update-source': {u'ca-eth': [u'ethernet_interface'], u'ca-ipv6': [u'sip_ipv6_address'], u'ca-ve': [u've_interface'], u'ca-port-channel': [u'port_channel'], u'ca-loopback': [u'loopback']}}
  _pyangbind_elements = {'sip_ipv6_address': sip_ipv6_address, 'ethernet_interface': ethernet_interface, 'port_channel': port_channel, 'loopback': loopback, 've_interface': ve_interface, }


