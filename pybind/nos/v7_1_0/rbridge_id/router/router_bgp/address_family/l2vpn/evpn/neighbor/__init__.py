
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import evpn_peer_group
import evpn_neighbor_ipv4
import evpn_neighbor_ipv6
class neighbor(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/router-bgp/address-family/l2vpn/evpn/neighbor. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__evpn_peer_group','__evpn_neighbor_ipv4','__evpn_neighbor_ipv6',)

  _yang_name = 'neighbor'
  _rest_name = 'neighbor'

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
    self.__evpn_peer_group = YANGDynClass(base=YANGListType("evpn_neighbor_peergroup_name",evpn_peer_group.evpn_peer_group, yang_name="evpn-peer-group", rest_name="evpn-peer-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='evpn-neighbor-peergroup-name', extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfEvpnNeighborPeerGrp'}}), is_container='list', yang_name="evpn-peer-group", rest_name="evpn-peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfEvpnNeighborPeerGrp'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)
    self.__evpn_neighbor_ipv4 = YANGDynClass(base=YANGListType("evpn_neighbor_ipv4_address",evpn_neighbor_ipv4.evpn_neighbor_ipv4, yang_name="evpn-neighbor-ipv4", rest_name="evpn-neighbor-ipv4", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='evpn-neighbor-ipv4-address', extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfEvpnNeighborIpv4Addr'}}), is_container='list', yang_name="evpn-neighbor-ipv4", rest_name="evpn-neighbor-ipv4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfEvpnNeighborIpv4Addr'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)
    self.__evpn_neighbor_ipv6 = YANGDynClass(base=YANGListType("evpn_neighbor_ipv6_address",evpn_neighbor_ipv6.evpn_neighbor_ipv6, yang_name="evpn-neighbor-ipv6", rest_name="evpn-neighbor-ipv6", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='evpn-neighbor-ipv6-address', extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfEvpnNeighborIpv6Addr'}}), is_container='list', yang_name="evpn-neighbor-ipv6", rest_name="evpn-neighbor-ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfEvpnNeighborIpv6Addr'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)

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
      return [u'rbridge-id', u'router', u'router-bgp', u'address-family', u'l2vpn', u'evpn', u'neighbor']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'bgp', u'address-family', u'l2vpn', u'evpn', u'neighbor']

  def _get_evpn_peer_group(self):
    """
    Getter method for evpn_peer_group, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_peer_group (list)
    """
    return self.__evpn_peer_group
      
  def _set_evpn_peer_group(self, v, load=False):
    """
    Setter method for evpn_peer_group, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_peer_group (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_evpn_peer_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_evpn_peer_group() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("evpn_neighbor_peergroup_name",evpn_peer_group.evpn_peer_group, yang_name="evpn-peer-group", rest_name="evpn-peer-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='evpn-neighbor-peergroup-name', extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfEvpnNeighborPeerGrp'}}), is_container='list', yang_name="evpn-peer-group", rest_name="evpn-peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfEvpnNeighborPeerGrp'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """evpn_peer_group must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("evpn_neighbor_peergroup_name",evpn_peer_group.evpn_peer_group, yang_name="evpn-peer-group", rest_name="evpn-peer-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='evpn-neighbor-peergroup-name', extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfEvpnNeighborPeerGrp'}}), is_container='list', yang_name="evpn-peer-group", rest_name="evpn-peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfEvpnNeighborPeerGrp'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)""",
        })

    self.__evpn_peer_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_evpn_peer_group(self):
    self.__evpn_peer_group = YANGDynClass(base=YANGListType("evpn_neighbor_peergroup_name",evpn_peer_group.evpn_peer_group, yang_name="evpn-peer-group", rest_name="evpn-peer-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='evpn-neighbor-peergroup-name', extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfEvpnNeighborPeerGrp'}}), is_container='list', yang_name="evpn-peer-group", rest_name="evpn-peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfEvpnNeighborPeerGrp'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)


  def _get_evpn_neighbor_ipv4(self):
    """
    Getter method for evpn_neighbor_ipv4, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_neighbor_ipv4 (list)
    """
    return self.__evpn_neighbor_ipv4
      
  def _set_evpn_neighbor_ipv4(self, v, load=False):
    """
    Setter method for evpn_neighbor_ipv4, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_neighbor_ipv4 (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_evpn_neighbor_ipv4 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_evpn_neighbor_ipv4() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("evpn_neighbor_ipv4_address",evpn_neighbor_ipv4.evpn_neighbor_ipv4, yang_name="evpn-neighbor-ipv4", rest_name="evpn-neighbor-ipv4", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='evpn-neighbor-ipv4-address', extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfEvpnNeighborIpv4Addr'}}), is_container='list', yang_name="evpn-neighbor-ipv4", rest_name="evpn-neighbor-ipv4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfEvpnNeighborIpv4Addr'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """evpn_neighbor_ipv4 must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("evpn_neighbor_ipv4_address",evpn_neighbor_ipv4.evpn_neighbor_ipv4, yang_name="evpn-neighbor-ipv4", rest_name="evpn-neighbor-ipv4", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='evpn-neighbor-ipv4-address', extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfEvpnNeighborIpv4Addr'}}), is_container='list', yang_name="evpn-neighbor-ipv4", rest_name="evpn-neighbor-ipv4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfEvpnNeighborIpv4Addr'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)""",
        })

    self.__evpn_neighbor_ipv4 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_evpn_neighbor_ipv4(self):
    self.__evpn_neighbor_ipv4 = YANGDynClass(base=YANGListType("evpn_neighbor_ipv4_address",evpn_neighbor_ipv4.evpn_neighbor_ipv4, yang_name="evpn-neighbor-ipv4", rest_name="evpn-neighbor-ipv4", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='evpn-neighbor-ipv4-address', extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfEvpnNeighborIpv4Addr'}}), is_container='list', yang_name="evpn-neighbor-ipv4", rest_name="evpn-neighbor-ipv4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfEvpnNeighborIpv4Addr'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)


  def _get_evpn_neighbor_ipv6(self):
    """
    Getter method for evpn_neighbor_ipv6, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_neighbor_ipv6 (list)
    """
    return self.__evpn_neighbor_ipv6
      
  def _set_evpn_neighbor_ipv6(self, v, load=False):
    """
    Setter method for evpn_neighbor_ipv6, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_neighbor_ipv6 (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_evpn_neighbor_ipv6 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_evpn_neighbor_ipv6() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("evpn_neighbor_ipv6_address",evpn_neighbor_ipv6.evpn_neighbor_ipv6, yang_name="evpn-neighbor-ipv6", rest_name="evpn-neighbor-ipv6", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='evpn-neighbor-ipv6-address', extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfEvpnNeighborIpv6Addr'}}), is_container='list', yang_name="evpn-neighbor-ipv6", rest_name="evpn-neighbor-ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfEvpnNeighborIpv6Addr'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """evpn_neighbor_ipv6 must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("evpn_neighbor_ipv6_address",evpn_neighbor_ipv6.evpn_neighbor_ipv6, yang_name="evpn-neighbor-ipv6", rest_name="evpn-neighbor-ipv6", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='evpn-neighbor-ipv6-address', extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfEvpnNeighborIpv6Addr'}}), is_container='list', yang_name="evpn-neighbor-ipv6", rest_name="evpn-neighbor-ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfEvpnNeighborIpv6Addr'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)""",
        })

    self.__evpn_neighbor_ipv6 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_evpn_neighbor_ipv6(self):
    self.__evpn_neighbor_ipv6 = YANGDynClass(base=YANGListType("evpn_neighbor_ipv6_address",evpn_neighbor_ipv6.evpn_neighbor_ipv6, yang_name="evpn-neighbor-ipv6", rest_name="evpn-neighbor-ipv6", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='evpn-neighbor-ipv6-address', extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfEvpnNeighborIpv6Addr'}}), is_container='list', yang_name="evpn-neighbor-ipv6", rest_name="evpn-neighbor-ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfEvpnNeighborIpv6Addr'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)

  evpn_peer_group = __builtin__.property(_get_evpn_peer_group, _set_evpn_peer_group)
  evpn_neighbor_ipv4 = __builtin__.property(_get_evpn_neighbor_ipv4, _set_evpn_neighbor_ipv4)
  evpn_neighbor_ipv6 = __builtin__.property(_get_evpn_neighbor_ipv6, _set_evpn_neighbor_ipv6)


  _pyangbind_elements = {'evpn_peer_group': evpn_peer_group, 'evpn_neighbor_ipv4': evpn_neighbor_ipv4, 'evpn_neighbor_ipv6': evpn_neighbor_ipv6, }


