
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ipv6_config
import interface_phy_dhcp_conf
import icmpv6
import access_group
import policy
import ipv6_nd_ra
import ipv6_phy_intf_cmds
import interface_ospfv3_conf
class ipv6(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/hundredgigabitethernet/ipv6. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The IPv6 configurations for an interface.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__raguard','__ipv6_config','__interface_phy_dhcp_conf','__icmpv6','__access_group','__policy','__ipv6_nd_ra','__ipv6_phy_intf_cmds','__interface_ospfv3_conf',)

  _yang_name = 'ipv6'
  _rest_name = 'ipv6'

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
    self.__ipv6_nd_ra = YANGDynClass(base=ipv6_nd_ra.ipv6_nd_ra, is_container='container', yang_name="ipv6-nd-ra", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'IpV6NdRaPhyIntf'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='container', is_config=True)
    self.__ipv6_phy_intf_cmds = YANGDynClass(base=ipv6_phy_intf_cmds.ipv6_phy_intf_cmds, is_container='container', yang_name="ipv6-phy-intf-cmds", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6 mlds phy interface commands', u'cli-drop-node-name': None, u'callpoint': u'MldsPhy'}}, namespace='urn:brocade.com:mgmt:brocade-mld-snooping', defining_module='brocade-mld-snooping', yang_type='container', is_config=True)
    self.__raguard = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="raguard", rest_name="raguard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IPv6 Router advertisement guard configuration'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    self.__icmpv6 = YANGDynClass(base=icmpv6.icmpv6, is_container='container', yang_name="icmpv6", rest_name="icmpv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Control Message Protocol(ICMP6)', u'sort-priority': u'111', u'display-when': u'/vcsmode/vcs-mode = "true"', u'cli-incomplete-no': None, u'callpoint': u'Icmp6PhyIntfConfigCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='container', is_config=True)
    self.__access_group = YANGDynClass(base=YANGListType("ipv6_access_list ip_direction",access_group.access_group, yang_name="access-group", rest_name="access-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-access-list ip-direction', extensions={u'tailf-common': {u'info': u'Configure IP Access group', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_ACL_CONFIG', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'Ip6aclAccessgroupIntHuCP'}}), is_container='list', yang_name="access-group", rest_name="access-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IP Access group', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_ACL_CONFIG', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'Ip6aclAccessgroupIntHuCP'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-access-list', defining_module='brocade-ipv6-access-list', yang_type='list', is_config=True)
    self.__policy = YANGDynClass(base=policy.policy, is_container='container', yang_name="policy", rest_name="policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure PBR', u'callpoint': u'PBRIntHuCP'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    self.__interface_ospfv3_conf = YANGDynClass(base=interface_ospfv3_conf.interface_ospfv3_conf, is_container='container', yang_name="interface-ospfv3-conf", rest_name="ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Open Shortest Path First version 3 (OSPFv3)', u'display-when': u'/vcsmode/vcs-mode = "true"', u'cli-incomplete-no': None, u'alt-name': u'ospf', u'cli-incomplete-command': None, u'sort-priority': u'113', u'callpoint': u'Ospfv3InterfaceConfig'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    self.__interface_phy_dhcp_conf = YANGDynClass(base=interface_phy_dhcp_conf.interface_phy_dhcp_conf, is_container='container', yang_name="interface-phy-dhcp-conf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'Dhcpv6RelayPhyInterface'}}, namespace='urn:brocade.com:mgmt:brocade-dhcpv6', defining_module='brocade-dhcpv6', yang_type='container', is_config=True)
    self.__ipv6_config = YANGDynClass(base=ipv6_config.ipv6_config, is_container='container', yang_name="ipv6-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the IPv6 address of an interface', u'cli-drop-node-name': None, u'callpoint': u'phy-intf-ipv6-cfg-cp', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='container', is_config=True)

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
      return [u'interface', u'hundredgigabitethernet', u'ipv6']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'HundredGigabitEthernet', u'ipv6']

  def _get_raguard(self):
    """
    Getter method for raguard, mapped from YANG variable /interface/hundredgigabitethernet/ipv6/raguard (empty)
    """
    return self.__raguard
      
  def _set_raguard(self, v, load=False):
    """
    Setter method for raguard, mapped from YANG variable /interface/hundredgigabitethernet/ipv6/raguard (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_raguard is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_raguard() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="raguard", rest_name="raguard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IPv6 Router advertisement guard configuration'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """raguard must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="raguard", rest_name="raguard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IPv6 Router advertisement guard configuration'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)""",
        })

    self.__raguard = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_raguard(self):
    self.__raguard = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="raguard", rest_name="raguard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IPv6 Router advertisement guard configuration'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)


  def _get_ipv6_config(self):
    """
    Getter method for ipv6_config, mapped from YANG variable /interface/hundredgigabitethernet/ipv6/ipv6_config (container)
    """
    return self.__ipv6_config
      
  def _set_ipv6_config(self, v, load=False):
    """
    Setter method for ipv6_config, mapped from YANG variable /interface/hundredgigabitethernet/ipv6/ipv6_config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_config() directly.
    """
    try:
      t = YANGDynClass(v,base=ipv6_config.ipv6_config, is_container='container', yang_name="ipv6-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the IPv6 address of an interface', u'cli-drop-node-name': None, u'callpoint': u'phy-intf-ipv6-cfg-cp', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ipv6_config.ipv6_config, is_container='container', yang_name="ipv6-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the IPv6 address of an interface', u'cli-drop-node-name': None, u'callpoint': u'phy-intf-ipv6-cfg-cp', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='container', is_config=True)""",
        })

    self.__ipv6_config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_config(self):
    self.__ipv6_config = YANGDynClass(base=ipv6_config.ipv6_config, is_container='container', yang_name="ipv6-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the IPv6 address of an interface', u'cli-drop-node-name': None, u'callpoint': u'phy-intf-ipv6-cfg-cp', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='container', is_config=True)


  def _get_interface_phy_dhcp_conf(self):
    """
    Getter method for interface_phy_dhcp_conf, mapped from YANG variable /interface/hundredgigabitethernet/ipv6/interface_phy_dhcp_conf (container)
    """
    return self.__interface_phy_dhcp_conf
      
  def _set_interface_phy_dhcp_conf(self, v, load=False):
    """
    Setter method for interface_phy_dhcp_conf, mapped from YANG variable /interface/hundredgigabitethernet/ipv6/interface_phy_dhcp_conf (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_phy_dhcp_conf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_phy_dhcp_conf() directly.
    """
    try:
      t = YANGDynClass(v,base=interface_phy_dhcp_conf.interface_phy_dhcp_conf, is_container='container', yang_name="interface-phy-dhcp-conf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'Dhcpv6RelayPhyInterface'}}, namespace='urn:brocade.com:mgmt:brocade-dhcpv6', defining_module='brocade-dhcpv6', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_phy_dhcp_conf must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface_phy_dhcp_conf.interface_phy_dhcp_conf, is_container='container', yang_name="interface-phy-dhcp-conf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'Dhcpv6RelayPhyInterface'}}, namespace='urn:brocade.com:mgmt:brocade-dhcpv6', defining_module='brocade-dhcpv6', yang_type='container', is_config=True)""",
        })

    self.__interface_phy_dhcp_conf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_phy_dhcp_conf(self):
    self.__interface_phy_dhcp_conf = YANGDynClass(base=interface_phy_dhcp_conf.interface_phy_dhcp_conf, is_container='container', yang_name="interface-phy-dhcp-conf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'Dhcpv6RelayPhyInterface'}}, namespace='urn:brocade.com:mgmt:brocade-dhcpv6', defining_module='brocade-dhcpv6', yang_type='container', is_config=True)


  def _get_icmpv6(self):
    """
    Getter method for icmpv6, mapped from YANG variable /interface/hundredgigabitethernet/ipv6/icmpv6 (container)
    """
    return self.__icmpv6
      
  def _set_icmpv6(self, v, load=False):
    """
    Setter method for icmpv6, mapped from YANG variable /interface/hundredgigabitethernet/ipv6/icmpv6 (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_icmpv6 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_icmpv6() directly.
    """
    try:
      t = YANGDynClass(v,base=icmpv6.icmpv6, is_container='container', yang_name="icmpv6", rest_name="icmpv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Control Message Protocol(ICMP6)', u'sort-priority': u'111', u'display-when': u'/vcsmode/vcs-mode = "true"', u'cli-incomplete-no': None, u'callpoint': u'Icmp6PhyIntfConfigCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """icmpv6 must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=icmpv6.icmpv6, is_container='container', yang_name="icmpv6", rest_name="icmpv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Control Message Protocol(ICMP6)', u'sort-priority': u'111', u'display-when': u'/vcsmode/vcs-mode = "true"', u'cli-incomplete-no': None, u'callpoint': u'Icmp6PhyIntfConfigCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='container', is_config=True)""",
        })

    self.__icmpv6 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_icmpv6(self):
    self.__icmpv6 = YANGDynClass(base=icmpv6.icmpv6, is_container='container', yang_name="icmpv6", rest_name="icmpv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Control Message Protocol(ICMP6)', u'sort-priority': u'111', u'display-when': u'/vcsmode/vcs-mode = "true"', u'cli-incomplete-no': None, u'callpoint': u'Icmp6PhyIntfConfigCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='container', is_config=True)


  def _get_access_group(self):
    """
    Getter method for access_group, mapped from YANG variable /interface/hundredgigabitethernet/ipv6/access_group (list)
    """
    return self.__access_group
      
  def _set_access_group(self, v, load=False):
    """
    Setter method for access_group, mapped from YANG variable /interface/hundredgigabitethernet/ipv6/access_group (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_access_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_access_group() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("ipv6_access_list ip_direction",access_group.access_group, yang_name="access-group", rest_name="access-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-access-list ip-direction', extensions={u'tailf-common': {u'info': u'Configure IP Access group', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_ACL_CONFIG', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'Ip6aclAccessgroupIntHuCP'}}), is_container='list', yang_name="access-group", rest_name="access-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IP Access group', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_ACL_CONFIG', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'Ip6aclAccessgroupIntHuCP'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-access-list', defining_module='brocade-ipv6-access-list', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """access_group must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ipv6_access_list ip_direction",access_group.access_group, yang_name="access-group", rest_name="access-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-access-list ip-direction', extensions={u'tailf-common': {u'info': u'Configure IP Access group', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_ACL_CONFIG', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'Ip6aclAccessgroupIntHuCP'}}), is_container='list', yang_name="access-group", rest_name="access-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IP Access group', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_ACL_CONFIG', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'Ip6aclAccessgroupIntHuCP'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-access-list', defining_module='brocade-ipv6-access-list', yang_type='list', is_config=True)""",
        })

    self.__access_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_access_group(self):
    self.__access_group = YANGDynClass(base=YANGListType("ipv6_access_list ip_direction",access_group.access_group, yang_name="access-group", rest_name="access-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-access-list ip-direction', extensions={u'tailf-common': {u'info': u'Configure IP Access group', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_ACL_CONFIG', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'Ip6aclAccessgroupIntHuCP'}}), is_container='list', yang_name="access-group", rest_name="access-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IP Access group', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_ACL_CONFIG', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'Ip6aclAccessgroupIntHuCP'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-access-list', defining_module='brocade-ipv6-access-list', yang_type='list', is_config=True)


  def _get_policy(self):
    """
    Getter method for policy, mapped from YANG variable /interface/hundredgigabitethernet/ipv6/policy (container)

    YANG Description: Configure PBR
    """
    return self.__policy
      
  def _set_policy(self, v, load=False):
    """
    Setter method for policy, mapped from YANG variable /interface/hundredgigabitethernet/ipv6/policy (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_policy() directly.

    YANG Description: Configure PBR
    """
    try:
      t = YANGDynClass(v,base=policy.policy, is_container='container', yang_name="policy", rest_name="policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure PBR', u'callpoint': u'PBRIntHuCP'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """policy must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=policy.policy, is_container='container', yang_name="policy", rest_name="policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure PBR', u'callpoint': u'PBRIntHuCP'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_policy(self):
    self.__policy = YANGDynClass(base=policy.policy, is_container='container', yang_name="policy", rest_name="policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure PBR', u'callpoint': u'PBRIntHuCP'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)


  def _get_ipv6_nd_ra(self):
    """
    Getter method for ipv6_nd_ra, mapped from YANG variable /interface/hundredgigabitethernet/ipv6/ipv6_nd_ra (container)
    """
    return self.__ipv6_nd_ra
      
  def _set_ipv6_nd_ra(self, v, load=False):
    """
    Setter method for ipv6_nd_ra, mapped from YANG variable /interface/hundredgigabitethernet/ipv6/ipv6_nd_ra (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_nd_ra is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_nd_ra() directly.
    """
    try:
      t = YANGDynClass(v,base=ipv6_nd_ra.ipv6_nd_ra, is_container='container', yang_name="ipv6-nd-ra", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'IpV6NdRaPhyIntf'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_nd_ra must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ipv6_nd_ra.ipv6_nd_ra, is_container='container', yang_name="ipv6-nd-ra", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'IpV6NdRaPhyIntf'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='container', is_config=True)""",
        })

    self.__ipv6_nd_ra = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_nd_ra(self):
    self.__ipv6_nd_ra = YANGDynClass(base=ipv6_nd_ra.ipv6_nd_ra, is_container='container', yang_name="ipv6-nd-ra", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'IpV6NdRaPhyIntf'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='container', is_config=True)


  def _get_ipv6_phy_intf_cmds(self):
    """
    Getter method for ipv6_phy_intf_cmds, mapped from YANG variable /interface/hundredgigabitethernet/ipv6/ipv6_phy_intf_cmds (container)
    """
    return self.__ipv6_phy_intf_cmds
      
  def _set_ipv6_phy_intf_cmds(self, v, load=False):
    """
    Setter method for ipv6_phy_intf_cmds, mapped from YANG variable /interface/hundredgigabitethernet/ipv6/ipv6_phy_intf_cmds (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_phy_intf_cmds is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_phy_intf_cmds() directly.
    """
    try:
      t = YANGDynClass(v,base=ipv6_phy_intf_cmds.ipv6_phy_intf_cmds, is_container='container', yang_name="ipv6-phy-intf-cmds", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6 mlds phy interface commands', u'cli-drop-node-name': None, u'callpoint': u'MldsPhy'}}, namespace='urn:brocade.com:mgmt:brocade-mld-snooping', defining_module='brocade-mld-snooping', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_phy_intf_cmds must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ipv6_phy_intf_cmds.ipv6_phy_intf_cmds, is_container='container', yang_name="ipv6-phy-intf-cmds", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6 mlds phy interface commands', u'cli-drop-node-name': None, u'callpoint': u'MldsPhy'}}, namespace='urn:brocade.com:mgmt:brocade-mld-snooping', defining_module='brocade-mld-snooping', yang_type='container', is_config=True)""",
        })

    self.__ipv6_phy_intf_cmds = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_phy_intf_cmds(self):
    self.__ipv6_phy_intf_cmds = YANGDynClass(base=ipv6_phy_intf_cmds.ipv6_phy_intf_cmds, is_container='container', yang_name="ipv6-phy-intf-cmds", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6 mlds phy interface commands', u'cli-drop-node-name': None, u'callpoint': u'MldsPhy'}}, namespace='urn:brocade.com:mgmt:brocade-mld-snooping', defining_module='brocade-mld-snooping', yang_type='container', is_config=True)


  def _get_interface_ospfv3_conf(self):
    """
    Getter method for interface_ospfv3_conf, mapped from YANG variable /interface/hundredgigabitethernet/ipv6/interface_ospfv3_conf (container)

    YANG Description: Open Shortest Path First version 3 (OSPFv3)
    """
    return self.__interface_ospfv3_conf
      
  def _set_interface_ospfv3_conf(self, v, load=False):
    """
    Setter method for interface_ospfv3_conf, mapped from YANG variable /interface/hundredgigabitethernet/ipv6/interface_ospfv3_conf (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_ospfv3_conf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_ospfv3_conf() directly.

    YANG Description: Open Shortest Path First version 3 (OSPFv3)
    """
    try:
      t = YANGDynClass(v,base=interface_ospfv3_conf.interface_ospfv3_conf, is_container='container', yang_name="interface-ospfv3-conf", rest_name="ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Open Shortest Path First version 3 (OSPFv3)', u'display-when': u'/vcsmode/vcs-mode = "true"', u'cli-incomplete-no': None, u'alt-name': u'ospf', u'cli-incomplete-command': None, u'sort-priority': u'113', u'callpoint': u'Ospfv3InterfaceConfig'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_ospfv3_conf must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface_ospfv3_conf.interface_ospfv3_conf, is_container='container', yang_name="interface-ospfv3-conf", rest_name="ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Open Shortest Path First version 3 (OSPFv3)', u'display-when': u'/vcsmode/vcs-mode = "true"', u'cli-incomplete-no': None, u'alt-name': u'ospf', u'cli-incomplete-command': None, u'sort-priority': u'113', u'callpoint': u'Ospfv3InterfaceConfig'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)""",
        })

    self.__interface_ospfv3_conf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_ospfv3_conf(self):
    self.__interface_ospfv3_conf = YANGDynClass(base=interface_ospfv3_conf.interface_ospfv3_conf, is_container='container', yang_name="interface-ospfv3-conf", rest_name="ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Open Shortest Path First version 3 (OSPFv3)', u'display-when': u'/vcsmode/vcs-mode = "true"', u'cli-incomplete-no': None, u'alt-name': u'ospf', u'cli-incomplete-command': None, u'sort-priority': u'113', u'callpoint': u'Ospfv3InterfaceConfig'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)

  raguard = __builtin__.property(_get_raguard, _set_raguard)
  ipv6_config = __builtin__.property(_get_ipv6_config, _set_ipv6_config)
  interface_phy_dhcp_conf = __builtin__.property(_get_interface_phy_dhcp_conf, _set_interface_phy_dhcp_conf)
  icmpv6 = __builtin__.property(_get_icmpv6, _set_icmpv6)
  access_group = __builtin__.property(_get_access_group, _set_access_group)
  policy = __builtin__.property(_get_policy, _set_policy)
  ipv6_nd_ra = __builtin__.property(_get_ipv6_nd_ra, _set_ipv6_nd_ra)
  ipv6_phy_intf_cmds = __builtin__.property(_get_ipv6_phy_intf_cmds, _set_ipv6_phy_intf_cmds)
  interface_ospfv3_conf = __builtin__.property(_get_interface_ospfv3_conf, _set_interface_ospfv3_conf)


  _pyangbind_elements = {'raguard': raguard, 'ipv6_config': ipv6_config, 'interface_phy_dhcp_conf': interface_phy_dhcp_conf, 'icmpv6': icmpv6, 'access_group': access_group, 'policy': policy, 'ipv6_nd_ra': ipv6_nd_ra, 'ipv6_phy_intf_cmds': ipv6_phy_intf_cmds, 'interface_ospfv3_conf': interface_ospfv3_conf, }


