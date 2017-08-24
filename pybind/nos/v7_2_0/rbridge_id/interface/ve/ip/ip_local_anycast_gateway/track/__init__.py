
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import interface
import network
import next_hop
class track(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/interface/ve/ip/ip-local-anycast-gateway/track. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__interface','__network','__next_hop',)

  _yang_name = 'track'
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
    self.__interface = YANGDynClass(base=YANGListType("interface_type interface_name",interface.interface, yang_name="interface", rest_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-type interface-name', extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'AnycastGatewayLocalIpv4TrackInterfaceConfig'}}), is_container='list', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'AnycastGatewayLocalIpv4TrackInterfaceConfig'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)
    self.__next_hop = YANGDynClass(base=YANGListType("next_hop_address",next_hop.next_hop, yang_name="next-hop", rest_name="next-hop", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='next-hop-address', extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'AnycastGatewayLocalIpv4TrackNextHopConfig'}}), is_container='list', yang_name="next-hop", rest_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'AnycastGatewayLocalIpv4TrackNextHopConfig'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)
    self.__network = YANGDynClass(base=YANGListType("network_address",network.network, yang_name="network", rest_name="network", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='network-address', extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'AnycastGatewayLocalIpv4TrackNetworkConfig'}}), is_container='list', yang_name="network", rest_name="network", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'AnycastGatewayLocalIpv4TrackNetworkConfig'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)

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
      return [u'rbridge-id', u'interface', u've', u'ip', u'ip-local-anycast-gateway', u'track']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'interface', u'Ve', u'ip', u'fabric-virtual-gateway', u'track']

  def _get_interface(self):
    """
    Getter method for interface, mapped from YANG variable /rbridge_id/interface/ve/ip/ip_local_anycast_gateway/track/interface (list)
    """
    return self.__interface
      
  def _set_interface(self, v, load=False):
    """
    Setter method for interface, mapped from YANG variable /rbridge_id/interface/ve/ip/ip_local_anycast_gateway/track/interface (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("interface_type interface_name",interface.interface, yang_name="interface", rest_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-type interface-name', extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'AnycastGatewayLocalIpv4TrackInterfaceConfig'}}), is_container='list', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'AnycastGatewayLocalIpv4TrackInterfaceConfig'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("interface_type interface_name",interface.interface, yang_name="interface", rest_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-type interface-name', extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'AnycastGatewayLocalIpv4TrackInterfaceConfig'}}), is_container='list', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'AnycastGatewayLocalIpv4TrackInterfaceConfig'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)""",
        })

    self.__interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface(self):
    self.__interface = YANGDynClass(base=YANGListType("interface_type interface_name",interface.interface, yang_name="interface", rest_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-type interface-name', extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'AnycastGatewayLocalIpv4TrackInterfaceConfig'}}), is_container='list', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'AnycastGatewayLocalIpv4TrackInterfaceConfig'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)


  def _get_network(self):
    """
    Getter method for network, mapped from YANG variable /rbridge_id/interface/ve/ip/ip_local_anycast_gateway/track/network (list)
    """
    return self.__network
      
  def _set_network(self, v, load=False):
    """
    Setter method for network, mapped from YANG variable /rbridge_id/interface/ve/ip/ip_local_anycast_gateway/track/network (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_network is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_network() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("network_address",network.network, yang_name="network", rest_name="network", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='network-address', extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'AnycastGatewayLocalIpv4TrackNetworkConfig'}}), is_container='list', yang_name="network", rest_name="network", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'AnycastGatewayLocalIpv4TrackNetworkConfig'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """network must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("network_address",network.network, yang_name="network", rest_name="network", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='network-address', extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'AnycastGatewayLocalIpv4TrackNetworkConfig'}}), is_container='list', yang_name="network", rest_name="network", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'AnycastGatewayLocalIpv4TrackNetworkConfig'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)""",
        })

    self.__network = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_network(self):
    self.__network = YANGDynClass(base=YANGListType("network_address",network.network, yang_name="network", rest_name="network", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='network-address', extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'AnycastGatewayLocalIpv4TrackNetworkConfig'}}), is_container='list', yang_name="network", rest_name="network", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'AnycastGatewayLocalIpv4TrackNetworkConfig'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)


  def _get_next_hop(self):
    """
    Getter method for next_hop, mapped from YANG variable /rbridge_id/interface/ve/ip/ip_local_anycast_gateway/track/next_hop (list)
    """
    return self.__next_hop
      
  def _set_next_hop(self, v, load=False):
    """
    Setter method for next_hop, mapped from YANG variable /rbridge_id/interface/ve/ip/ip_local_anycast_gateway/track/next_hop (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_next_hop is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_next_hop() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("next_hop_address",next_hop.next_hop, yang_name="next-hop", rest_name="next-hop", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='next-hop-address', extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'AnycastGatewayLocalIpv4TrackNextHopConfig'}}), is_container='list', yang_name="next-hop", rest_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'AnycastGatewayLocalIpv4TrackNextHopConfig'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """next_hop must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("next_hop_address",next_hop.next_hop, yang_name="next-hop", rest_name="next-hop", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='next-hop-address', extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'AnycastGatewayLocalIpv4TrackNextHopConfig'}}), is_container='list', yang_name="next-hop", rest_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'AnycastGatewayLocalIpv4TrackNextHopConfig'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)""",
        })

    self.__next_hop = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_next_hop(self):
    self.__next_hop = YANGDynClass(base=YANGListType("next_hop_address",next_hop.next_hop, yang_name="next-hop", rest_name="next-hop", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='next-hop-address', extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'AnycastGatewayLocalIpv4TrackNextHopConfig'}}), is_container='list', yang_name="next-hop", rest_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'AnycastGatewayLocalIpv4TrackNextHopConfig'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)

  interface = __builtin__.property(_get_interface, _set_interface)
  network = __builtin__.property(_get_network, _set_network)
  next_hop = __builtin__.property(_get_next_hop, _set_next_hop)


  _pyangbind_elements = {'interface': interface, 'network': network, 'next_hop': next_hop, }


