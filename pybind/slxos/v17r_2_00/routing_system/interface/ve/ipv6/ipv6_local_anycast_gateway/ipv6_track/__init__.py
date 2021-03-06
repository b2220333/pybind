
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ipv6_interface
import ipv6_network
import ipv6_next_hop
class ipv6_track(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/interface/ve/ipv6/ipv6-local-anycast-gateway/ipv6-track. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ipv6_interface','__ipv6_network','__ipv6_next_hop',)

  _yang_name = 'ipv6-track'
  _rest_name = 'track'

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
    self.__ipv6_next_hop = YANGDynClass(base=YANGListType("ipv6_next_hop_address",ipv6_next_hop.ipv6_next_hop, yang_name="ipv6-next-hop", rest_name="next-hop", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-next-hop-address', extensions={u'tailf-common': {u'callpoint': u'AnycastGatewayLocalIpv6TrackNextHopConfig', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'next-hop', u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}), is_container='list', yang_name="ipv6-next-hop", rest_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'AnycastGatewayLocalIpv6TrackNextHopConfig', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'next-hop', u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)
    self.__ipv6_network = YANGDynClass(base=YANGListType("ipv6_network_address",ipv6_network.ipv6_network, yang_name="ipv6-network", rest_name="network", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-network-address', extensions={u'tailf-common': {u'callpoint': u'AnycastGatewayLocalIpv6TrackNetworkConfig', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'network', u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}), is_container='list', yang_name="ipv6-network", rest_name="network", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'AnycastGatewayLocalIpv6TrackNetworkConfig', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'network', u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)
    self.__ipv6_interface = YANGDynClass(base=YANGListType("ipv6_interface_type ipv6_interface_name",ipv6_interface.ipv6_interface, yang_name="ipv6-interface", rest_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-interface-type ipv6-interface-name', extensions={u'tailf-common': {u'callpoint': u'AnycastGatewayLocalIpv6TrackInterfaceConfig', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'interface', u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}), is_container='list', yang_name="ipv6-interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'AnycastGatewayLocalIpv6TrackInterfaceConfig', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'interface', u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)

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
      return [u'routing-system', u'interface', u've', u'ipv6', u'ipv6-local-anycast-gateway', u'ipv6-track']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ve', u'ipv6', u'fabric-virtual-gateway', u'track']

  def _get_ipv6_interface(self):
    """
    Getter method for ipv6_interface, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_local_anycast_gateway/ipv6_track/ipv6_interface (list)
    """
    return self.__ipv6_interface
      
  def _set_ipv6_interface(self, v, load=False):
    """
    Setter method for ipv6_interface, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_local_anycast_gateway/ipv6_track/ipv6_interface (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_interface() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("ipv6_interface_type ipv6_interface_name",ipv6_interface.ipv6_interface, yang_name="ipv6-interface", rest_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-interface-type ipv6-interface-name', extensions={u'tailf-common': {u'callpoint': u'AnycastGatewayLocalIpv6TrackInterfaceConfig', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'interface', u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}), is_container='list', yang_name="ipv6-interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'AnycastGatewayLocalIpv6TrackInterfaceConfig', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'interface', u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_interface must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ipv6_interface_type ipv6_interface_name",ipv6_interface.ipv6_interface, yang_name="ipv6-interface", rest_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-interface-type ipv6-interface-name', extensions={u'tailf-common': {u'callpoint': u'AnycastGatewayLocalIpv6TrackInterfaceConfig', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'interface', u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}), is_container='list', yang_name="ipv6-interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'AnycastGatewayLocalIpv6TrackInterfaceConfig', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'interface', u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)""",
        })

    self.__ipv6_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_interface(self):
    self.__ipv6_interface = YANGDynClass(base=YANGListType("ipv6_interface_type ipv6_interface_name",ipv6_interface.ipv6_interface, yang_name="ipv6-interface", rest_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-interface-type ipv6-interface-name', extensions={u'tailf-common': {u'callpoint': u'AnycastGatewayLocalIpv6TrackInterfaceConfig', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'interface', u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}), is_container='list', yang_name="ipv6-interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'AnycastGatewayLocalIpv6TrackInterfaceConfig', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'interface', u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)


  def _get_ipv6_network(self):
    """
    Getter method for ipv6_network, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_local_anycast_gateway/ipv6_track/ipv6_network (list)
    """
    return self.__ipv6_network
      
  def _set_ipv6_network(self, v, load=False):
    """
    Setter method for ipv6_network, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_local_anycast_gateway/ipv6_track/ipv6_network (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_network is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_network() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("ipv6_network_address",ipv6_network.ipv6_network, yang_name="ipv6-network", rest_name="network", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-network-address', extensions={u'tailf-common': {u'callpoint': u'AnycastGatewayLocalIpv6TrackNetworkConfig', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'network', u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}), is_container='list', yang_name="ipv6-network", rest_name="network", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'AnycastGatewayLocalIpv6TrackNetworkConfig', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'network', u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_network must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ipv6_network_address",ipv6_network.ipv6_network, yang_name="ipv6-network", rest_name="network", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-network-address', extensions={u'tailf-common': {u'callpoint': u'AnycastGatewayLocalIpv6TrackNetworkConfig', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'network', u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}), is_container='list', yang_name="ipv6-network", rest_name="network", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'AnycastGatewayLocalIpv6TrackNetworkConfig', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'network', u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)""",
        })

    self.__ipv6_network = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_network(self):
    self.__ipv6_network = YANGDynClass(base=YANGListType("ipv6_network_address",ipv6_network.ipv6_network, yang_name="ipv6-network", rest_name="network", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-network-address', extensions={u'tailf-common': {u'callpoint': u'AnycastGatewayLocalIpv6TrackNetworkConfig', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'network', u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}), is_container='list', yang_name="ipv6-network", rest_name="network", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'AnycastGatewayLocalIpv6TrackNetworkConfig', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'network', u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)


  def _get_ipv6_next_hop(self):
    """
    Getter method for ipv6_next_hop, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_local_anycast_gateway/ipv6_track/ipv6_next_hop (list)
    """
    return self.__ipv6_next_hop
      
  def _set_ipv6_next_hop(self, v, load=False):
    """
    Setter method for ipv6_next_hop, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_local_anycast_gateway/ipv6_track/ipv6_next_hop (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_next_hop is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_next_hop() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("ipv6_next_hop_address",ipv6_next_hop.ipv6_next_hop, yang_name="ipv6-next-hop", rest_name="next-hop", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-next-hop-address', extensions={u'tailf-common': {u'callpoint': u'AnycastGatewayLocalIpv6TrackNextHopConfig', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'next-hop', u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}), is_container='list', yang_name="ipv6-next-hop", rest_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'AnycastGatewayLocalIpv6TrackNextHopConfig', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'next-hop', u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_next_hop must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ipv6_next_hop_address",ipv6_next_hop.ipv6_next_hop, yang_name="ipv6-next-hop", rest_name="next-hop", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-next-hop-address', extensions={u'tailf-common': {u'callpoint': u'AnycastGatewayLocalIpv6TrackNextHopConfig', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'next-hop', u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}), is_container='list', yang_name="ipv6-next-hop", rest_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'AnycastGatewayLocalIpv6TrackNextHopConfig', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'next-hop', u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)""",
        })

    self.__ipv6_next_hop = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_next_hop(self):
    self.__ipv6_next_hop = YANGDynClass(base=YANGListType("ipv6_next_hop_address",ipv6_next_hop.ipv6_next_hop, yang_name="ipv6-next-hop", rest_name="next-hop", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-next-hop-address', extensions={u'tailf-common': {u'callpoint': u'AnycastGatewayLocalIpv6TrackNextHopConfig', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'next-hop', u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}), is_container='list', yang_name="ipv6-next-hop", rest_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'AnycastGatewayLocalIpv6TrackNextHopConfig', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'next-hop', u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)

  ipv6_interface = __builtin__.property(_get_ipv6_interface, _set_ipv6_interface)
  ipv6_network = __builtin__.property(_get_ipv6_network, _set_ipv6_network)
  ipv6_next_hop = __builtin__.property(_get_ipv6_next_hop, _set_ipv6_next_hop)


  _pyangbind_elements = {'ipv6_interface': ipv6_interface, 'ipv6_network': ipv6_network, 'ipv6_next_hop': ipv6_next_hop, }


