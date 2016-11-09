
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
  from YANG module brocade-interface - based on the path /interface/fortygigabitethernet/ipv6/interface-phy-dhcp-conf/dhcp/relay/servers/interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Interface.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__interface_type','__interface_name',)

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
    self.__interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'fortygigabitethernet': {'value': 2}, u'gigabitethernet': {'value': 0}, u'tengigabitethernet': {'value': 1}, u'hundredgigabitethernet': {'value': 3}, u'Ve': {'value': 4}},), is_leaf=True, yang_name="interface-type", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface type', u'cli-drop-node-name': None, u'alt-name': u'interface', u'cli-incomplete-command': None, u'cli-run-template': u'ipv6 dhcp relay address$(relay-ip-addr) $($(server-vrf-name)==.?: use-vrf $(server-vrf-name))\n'}}, namespace='urn:brocade.com:mgmt:brocade-dhcpv6', defining_module='brocade-dhcpv6', yang_type='dhcpv6-iftype', is_config=True)
    self.__interface_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(((([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-3][0-9])/)?(([0-9]|1[0-6]))/([1-9]|[1-9][0-9])(:[1-4])?)|([1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-7][0-9]{3}|8[0-1][0-9][0-1]))'}), is_leaf=True, yang_name="interface-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface name', u'cli-drop-node-name': None, u'cli-run-template': u'ipv6 dhcp relay address$(relay-ip-addr) $($(server-vrf-name)==.?: use-vrf $(server-vrf-name))\n'}}, namespace='urn:brocade.com:mgmt:brocade-dhcpv6', defining_module='brocade-dhcpv6', yang_type='dhcpv6-ifname', is_config=True)

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
      return [u'interface', u'fortygigabitethernet', u'ipv6', u'interface-phy-dhcp-conf', u'dhcp', u'relay', u'servers', u'interface']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'FortyGigabitEthernet', u'ipv6', u'dhcp', u'relay', u'interface']

  def _get_interface_type(self):
    """
    Getter method for interface_type, mapped from YANG variable /interface/fortygigabitethernet/ipv6/interface_phy_dhcp_conf/dhcp/relay/servers/interface/interface_type (dhcpv6-iftype)

    YANG Description: Interface type
    """
    return self.__interface_type
      
  def _set_interface_type(self, v, load=False):
    """
    Setter method for interface_type, mapped from YANG variable /interface/fortygigabitethernet/ipv6/interface_phy_dhcp_conf/dhcp/relay/servers/interface/interface_type (dhcpv6-iftype)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_type() directly.

    YANG Description: Interface type
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'fortygigabitethernet': {'value': 2}, u'gigabitethernet': {'value': 0}, u'tengigabitethernet': {'value': 1}, u'hundredgigabitethernet': {'value': 3}, u'Ve': {'value': 4}},), is_leaf=True, yang_name="interface-type", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface type', u'cli-drop-node-name': None, u'alt-name': u'interface', u'cli-incomplete-command': None, u'cli-run-template': u'ipv6 dhcp relay address$(relay-ip-addr) $($(server-vrf-name)==.?: use-vrf $(server-vrf-name))\n'}}, namespace='urn:brocade.com:mgmt:brocade-dhcpv6', defining_module='brocade-dhcpv6', yang_type='dhcpv6-iftype', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_type must be of a type compatible with dhcpv6-iftype""",
          'defined-type': "brocade-dhcpv6:dhcpv6-iftype",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'fortygigabitethernet': {'value': 2}, u'gigabitethernet': {'value': 0}, u'tengigabitethernet': {'value': 1}, u'hundredgigabitethernet': {'value': 3}, u'Ve': {'value': 4}},), is_leaf=True, yang_name="interface-type", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface type', u'cli-drop-node-name': None, u'alt-name': u'interface', u'cli-incomplete-command': None, u'cli-run-template': u'ipv6 dhcp relay address$(relay-ip-addr) $($(server-vrf-name)==.?: use-vrf $(server-vrf-name))\n'}}, namespace='urn:brocade.com:mgmt:brocade-dhcpv6', defining_module='brocade-dhcpv6', yang_type='dhcpv6-iftype', is_config=True)""",
        })

    self.__interface_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_type(self):
    self.__interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'fortygigabitethernet': {'value': 2}, u'gigabitethernet': {'value': 0}, u'tengigabitethernet': {'value': 1}, u'hundredgigabitethernet': {'value': 3}, u'Ve': {'value': 4}},), is_leaf=True, yang_name="interface-type", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface type', u'cli-drop-node-name': None, u'alt-name': u'interface', u'cli-incomplete-command': None, u'cli-run-template': u'ipv6 dhcp relay address$(relay-ip-addr) $($(server-vrf-name)==.?: use-vrf $(server-vrf-name))\n'}}, namespace='urn:brocade.com:mgmt:brocade-dhcpv6', defining_module='brocade-dhcpv6', yang_type='dhcpv6-iftype', is_config=True)


  def _get_interface_name(self):
    """
    Getter method for interface_name, mapped from YANG variable /interface/fortygigabitethernet/ipv6/interface_phy_dhcp_conf/dhcp/relay/servers/interface/interface_name (dhcpv6-ifname)

    YANG Description: Interface name
    """
    return self.__interface_name
      
  def _set_interface_name(self, v, load=False):
    """
    Setter method for interface_name, mapped from YANG variable /interface/fortygigabitethernet/ipv6/interface_phy_dhcp_conf/dhcp/relay/servers/interface/interface_name (dhcpv6-ifname)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_name() directly.

    YANG Description: Interface name
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(((([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-3][0-9])/)?(([0-9]|1[0-6]))/([1-9]|[1-9][0-9])(:[1-4])?)|([1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-7][0-9]{3}|8[0-1][0-9][0-1]))'}), is_leaf=True, yang_name="interface-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface name', u'cli-drop-node-name': None, u'cli-run-template': u'ipv6 dhcp relay address$(relay-ip-addr) $($(server-vrf-name)==.?: use-vrf $(server-vrf-name))\n'}}, namespace='urn:brocade.com:mgmt:brocade-dhcpv6', defining_module='brocade-dhcpv6', yang_type='dhcpv6-ifname', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_name must be of a type compatible with dhcpv6-ifname""",
          'defined-type': "brocade-dhcpv6:dhcpv6-ifname",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(((([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-3][0-9])/)?(([0-9]|1[0-6]))/([1-9]|[1-9][0-9])(:[1-4])?)|([1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-7][0-9]{3}|8[0-1][0-9][0-1]))'}), is_leaf=True, yang_name="interface-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface name', u'cli-drop-node-name': None, u'cli-run-template': u'ipv6 dhcp relay address$(relay-ip-addr) $($(server-vrf-name)==.?: use-vrf $(server-vrf-name))\n'}}, namespace='urn:brocade.com:mgmt:brocade-dhcpv6', defining_module='brocade-dhcpv6', yang_type='dhcpv6-ifname', is_config=True)""",
        })

    self.__interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_name(self):
    self.__interface_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(((([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-3][0-9])/)?(([0-9]|1[0-6]))/([1-9]|[1-9][0-9])(:[1-4])?)|([1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-7][0-9]{3}|8[0-1][0-9][0-1]))'}), is_leaf=True, yang_name="interface-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface name', u'cli-drop-node-name': None, u'cli-run-template': u'ipv6 dhcp relay address$(relay-ip-addr) $($(server-vrf-name)==.?: use-vrf $(server-vrf-name))\n'}}, namespace='urn:brocade.com:mgmt:brocade-dhcpv6', defining_module='brocade-dhcpv6', yang_type='dhcpv6-ifname', is_config=True)

  interface_type = __builtin__.property(_get_interface_type, _set_interface_type)
  interface_name = __builtin__.property(_get_interface_name, _set_interface_name)


  _pyangbind_elements = {'interface_type': interface_type, 'interface_name': interface_name, }


