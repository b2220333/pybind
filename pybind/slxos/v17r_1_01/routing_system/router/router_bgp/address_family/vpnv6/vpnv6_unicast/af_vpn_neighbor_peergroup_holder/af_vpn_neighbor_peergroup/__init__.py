
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import af_neighbor_capability
import send_community
import neighbor_route_map
import prefix_list
import filter_list
class af_vpn_neighbor_peergroup(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/vpnv6/vpnv6-unicast/af-vpn-neighbor-peergroup-holder/af-vpn-neighbor-peergroup. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__af_vpn_neighbor_peergroup_address','__af_neighbor_capability','__send_community','__activate','__weight','__route_reflector_client','__neighbor_route_map','__prefix_list','__filter_list',)

  _yang_name = 'af-vpn-neighbor-peergroup'
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
    self.__activate = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Activate the neighbor', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__af_neighbor_capability = YANGDynClass(base=af_neighbor_capability.af_neighbor_capability, is_container='container', presence=False, yang_name="af-neighbor-capability", rest_name="capability", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise capability to the peer', u'alt-name': u'capability', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__weight = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="weight", rest_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set default weight for routes from this neighbor', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='nei-weight', is_config=True)
    self.__filter_list = YANGDynClass(base=filter_list.filter_list, is_container='container', presence=False, yang_name="filter-list", rest_name="filter-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Establish BGP filters', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__neighbor_route_map = YANGDynClass(base=neighbor_route_map.neighbor_route_map, is_container='container', presence=False, yang_name="neighbor-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Apply route map to neighbor', u'alt-name': u'route-map', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__send_community = YANGDynClass(base=send_community.send_community, is_container='container', presence=False, yang_name="send-community", rest_name="send-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Send community attribute to this neighbor', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__route_reflector_client = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="route-reflector-client", rest_name="route-reflector-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a neighbor as Route Reflector client', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__prefix_list = YANGDynClass(base=prefix_list.prefix_list, is_container='container', presence=False, yang_name="prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Prefix List for filtering routes', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__af_vpn_neighbor_peergroup_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="af-vpn-neighbor-peergroup-address", rest_name="af-vpn-neighbor-peergroup-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Word:1-63;;Peer Group Name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bgp-peergroup', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'vpnv6', u'vpnv6-unicast', u'af-vpn-neighbor-peergroup-holder', u'af-vpn-neighbor-peergroup']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'address-family', u'vpnv6', u'unicast', u'neighbor']

  def _get_af_vpn_neighbor_peergroup_address(self):
    """
    Getter method for af_vpn_neighbor_peergroup_address, mapped from YANG variable /routing_system/router/router_bgp/address_family/vpnv6/vpnv6_unicast/af_vpn_neighbor_peergroup_holder/af_vpn_neighbor_peergroup/af_vpn_neighbor_peergroup_address (bgp-peergroup)
    """
    return self.__af_vpn_neighbor_peergroup_address
      
  def _set_af_vpn_neighbor_peergroup_address(self, v, load=False):
    """
    Setter method for af_vpn_neighbor_peergroup_address, mapped from YANG variable /routing_system/router/router_bgp/address_family/vpnv6/vpnv6_unicast/af_vpn_neighbor_peergroup_holder/af_vpn_neighbor_peergroup/af_vpn_neighbor_peergroup_address (bgp-peergroup)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_af_vpn_neighbor_peergroup_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_af_vpn_neighbor_peergroup_address() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="af-vpn-neighbor-peergroup-address", rest_name="af-vpn-neighbor-peergroup-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Word:1-63;;Peer Group Name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bgp-peergroup', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """af_vpn_neighbor_peergroup_address must be of a type compatible with bgp-peergroup""",
          'defined-type': "brocade-bgp:bgp-peergroup",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="af-vpn-neighbor-peergroup-address", rest_name="af-vpn-neighbor-peergroup-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Word:1-63;;Peer Group Name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bgp-peergroup', is_config=True)""",
        })

    self.__af_vpn_neighbor_peergroup_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_af_vpn_neighbor_peergroup_address(self):
    self.__af_vpn_neighbor_peergroup_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="af-vpn-neighbor-peergroup-address", rest_name="af-vpn-neighbor-peergroup-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Word:1-63;;Peer Group Name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bgp-peergroup', is_config=True)


  def _get_af_neighbor_capability(self):
    """
    Getter method for af_neighbor_capability, mapped from YANG variable /routing_system/router/router_bgp/address_family/vpnv6/vpnv6_unicast/af_vpn_neighbor_peergroup_holder/af_vpn_neighbor_peergroup/af_neighbor_capability (container)
    """
    return self.__af_neighbor_capability
      
  def _set_af_neighbor_capability(self, v, load=False):
    """
    Setter method for af_neighbor_capability, mapped from YANG variable /routing_system/router/router_bgp/address_family/vpnv6/vpnv6_unicast/af_vpn_neighbor_peergroup_holder/af_vpn_neighbor_peergroup/af_neighbor_capability (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_af_neighbor_capability is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_af_neighbor_capability() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=af_neighbor_capability.af_neighbor_capability, is_container='container', presence=False, yang_name="af-neighbor-capability", rest_name="capability", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise capability to the peer', u'alt-name': u'capability', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """af_neighbor_capability must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=af_neighbor_capability.af_neighbor_capability, is_container='container', presence=False, yang_name="af-neighbor-capability", rest_name="capability", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise capability to the peer', u'alt-name': u'capability', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__af_neighbor_capability = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_af_neighbor_capability(self):
    self.__af_neighbor_capability = YANGDynClass(base=af_neighbor_capability.af_neighbor_capability, is_container='container', presence=False, yang_name="af-neighbor-capability", rest_name="capability", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise capability to the peer', u'alt-name': u'capability', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_send_community(self):
    """
    Getter method for send_community, mapped from YANG variable /routing_system/router/router_bgp/address_family/vpnv6/vpnv6_unicast/af_vpn_neighbor_peergroup_holder/af_vpn_neighbor_peergroup/send_community (container)
    """
    return self.__send_community
      
  def _set_send_community(self, v, load=False):
    """
    Setter method for send_community, mapped from YANG variable /routing_system/router/router_bgp/address_family/vpnv6/vpnv6_unicast/af_vpn_neighbor_peergroup_holder/af_vpn_neighbor_peergroup/send_community (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_send_community is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_send_community() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=send_community.send_community, is_container='container', presence=False, yang_name="send-community", rest_name="send-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Send community attribute to this neighbor', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """send_community must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=send_community.send_community, is_container='container', presence=False, yang_name="send-community", rest_name="send-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Send community attribute to this neighbor', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__send_community = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_send_community(self):
    self.__send_community = YANGDynClass(base=send_community.send_community, is_container='container', presence=False, yang_name="send-community", rest_name="send-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Send community attribute to this neighbor', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_activate(self):
    """
    Getter method for activate, mapped from YANG variable /routing_system/router/router_bgp/address_family/vpnv6/vpnv6_unicast/af_vpn_neighbor_peergroup_holder/af_vpn_neighbor_peergroup/activate (empty)
    """
    return self.__activate
      
  def _set_activate(self, v, load=False):
    """
    Setter method for activate, mapped from YANG variable /routing_system/router/router_bgp/address_family/vpnv6/vpnv6_unicast/af_vpn_neighbor_peergroup_holder/af_vpn_neighbor_peergroup/activate (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_activate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_activate() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Activate the neighbor', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """activate must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Activate the neighbor', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__activate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_activate(self):
    self.__activate = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Activate the neighbor', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_weight(self):
    """
    Getter method for weight, mapped from YANG variable /routing_system/router/router_bgp/address_family/vpnv6/vpnv6_unicast/af_vpn_neighbor_peergroup_holder/af_vpn_neighbor_peergroup/weight (nei-weight)
    """
    return self.__weight
      
  def _set_weight(self, v, load=False):
    """
    Setter method for weight, mapped from YANG variable /routing_system/router/router_bgp/address_family/vpnv6/vpnv6_unicast/af_vpn_neighbor_peergroup_holder/af_vpn_neighbor_peergroup/weight (nei-weight)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_weight is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_weight() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="weight", rest_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set default weight for routes from this neighbor', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='nei-weight', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """weight must be of a type compatible with nei-weight""",
          'defined-type': "brocade-bgp:nei-weight",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="weight", rest_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set default weight for routes from this neighbor', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='nei-weight', is_config=True)""",
        })

    self.__weight = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_weight(self):
    self.__weight = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="weight", rest_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set default weight for routes from this neighbor', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='nei-weight', is_config=True)


  def _get_route_reflector_client(self):
    """
    Getter method for route_reflector_client, mapped from YANG variable /routing_system/router/router_bgp/address_family/vpnv6/vpnv6_unicast/af_vpn_neighbor_peergroup_holder/af_vpn_neighbor_peergroup/route_reflector_client (empty)
    """
    return self.__route_reflector_client
      
  def _set_route_reflector_client(self, v, load=False):
    """
    Setter method for route_reflector_client, mapped from YANG variable /routing_system/router/router_bgp/address_family/vpnv6/vpnv6_unicast/af_vpn_neighbor_peergroup_holder/af_vpn_neighbor_peergroup/route_reflector_client (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_reflector_client is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_reflector_client() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="route-reflector-client", rest_name="route-reflector-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a neighbor as Route Reflector client', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_reflector_client must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="route-reflector-client", rest_name="route-reflector-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a neighbor as Route Reflector client', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__route_reflector_client = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_reflector_client(self):
    self.__route_reflector_client = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="route-reflector-client", rest_name="route-reflector-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a neighbor as Route Reflector client', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_neighbor_route_map(self):
    """
    Getter method for neighbor_route_map, mapped from YANG variable /routing_system/router/router_bgp/address_family/vpnv6/vpnv6_unicast/af_vpn_neighbor_peergroup_holder/af_vpn_neighbor_peergroup/neighbor_route_map (container)
    """
    return self.__neighbor_route_map
      
  def _set_neighbor_route_map(self, v, load=False):
    """
    Setter method for neighbor_route_map, mapped from YANG variable /routing_system/router/router_bgp/address_family/vpnv6/vpnv6_unicast/af_vpn_neighbor_peergroup_holder/af_vpn_neighbor_peergroup/neighbor_route_map (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor_route_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor_route_map() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=neighbor_route_map.neighbor_route_map, is_container='container', presence=False, yang_name="neighbor-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Apply route map to neighbor', u'alt-name': u'route-map', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor_route_map must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=neighbor_route_map.neighbor_route_map, is_container='container', presence=False, yang_name="neighbor-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Apply route map to neighbor', u'alt-name': u'route-map', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__neighbor_route_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor_route_map(self):
    self.__neighbor_route_map = YANGDynClass(base=neighbor_route_map.neighbor_route_map, is_container='container', presence=False, yang_name="neighbor-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Apply route map to neighbor', u'alt-name': u'route-map', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_prefix_list(self):
    """
    Getter method for prefix_list, mapped from YANG variable /routing_system/router/router_bgp/address_family/vpnv6/vpnv6_unicast/af_vpn_neighbor_peergroup_holder/af_vpn_neighbor_peergroup/prefix_list (container)

    YANG Description: either prefix list or distribution-list
    """
    return self.__prefix_list
      
  def _set_prefix_list(self, v, load=False):
    """
    Setter method for prefix_list, mapped from YANG variable /routing_system/router/router_bgp/address_family/vpnv6/vpnv6_unicast/af_vpn_neighbor_peergroup_holder/af_vpn_neighbor_peergroup/prefix_list (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_list() directly.

    YANG Description: either prefix list or distribution-list
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=prefix_list.prefix_list, is_container='container', presence=False, yang_name="prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Prefix List for filtering routes', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_list must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=prefix_list.prefix_list, is_container='container', presence=False, yang_name="prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Prefix List for filtering routes', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__prefix_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_list(self):
    self.__prefix_list = YANGDynClass(base=prefix_list.prefix_list, is_container='container', presence=False, yang_name="prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Prefix List for filtering routes', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_filter_list(self):
    """
    Getter method for filter_list, mapped from YANG variable /routing_system/router/router_bgp/address_family/vpnv6/vpnv6_unicast/af_vpn_neighbor_peergroup_holder/af_vpn_neighbor_peergroup/filter_list (container)
    """
    return self.__filter_list
      
  def _set_filter_list(self, v, load=False):
    """
    Setter method for filter_list, mapped from YANG variable /routing_system/router/router_bgp/address_family/vpnv6/vpnv6_unicast/af_vpn_neighbor_peergroup_holder/af_vpn_neighbor_peergroup/filter_list (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_filter_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_filter_list() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=filter_list.filter_list, is_container='container', presence=False, yang_name="filter-list", rest_name="filter-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Establish BGP filters', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """filter_list must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=filter_list.filter_list, is_container='container', presence=False, yang_name="filter-list", rest_name="filter-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Establish BGP filters', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__filter_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_filter_list(self):
    self.__filter_list = YANGDynClass(base=filter_list.filter_list, is_container='container', presence=False, yang_name="filter-list", rest_name="filter-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Establish BGP filters', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

  af_vpn_neighbor_peergroup_address = __builtin__.property(_get_af_vpn_neighbor_peergroup_address, _set_af_vpn_neighbor_peergroup_address)
  af_neighbor_capability = __builtin__.property(_get_af_neighbor_capability, _set_af_neighbor_capability)
  send_community = __builtin__.property(_get_send_community, _set_send_community)
  activate = __builtin__.property(_get_activate, _set_activate)
  weight = __builtin__.property(_get_weight, _set_weight)
  route_reflector_client = __builtin__.property(_get_route_reflector_client, _set_route_reflector_client)
  neighbor_route_map = __builtin__.property(_get_neighbor_route_map, _set_neighbor_route_map)
  prefix_list = __builtin__.property(_get_prefix_list, _set_prefix_list)
  filter_list = __builtin__.property(_get_filter_list, _set_filter_list)


  _pyangbind_elements = {'af_vpn_neighbor_peergroup_address': af_vpn_neighbor_peergroup_address, 'af_neighbor_capability': af_neighbor_capability, 'send_community': send_community, 'activate': activate, 'weight': weight, 'route_reflector_client': route_reflector_client, 'neighbor_route_map': neighbor_route_map, 'prefix_list': prefix_list, 'filter_list': filter_list, }


