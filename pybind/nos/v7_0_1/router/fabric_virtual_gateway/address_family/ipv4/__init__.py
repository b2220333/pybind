
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import gratuitous_arp
class ipv4(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /router/fabric-virtual-gateway/address-family/ipv4. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Anycast gateway ipv4
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__enable_global','__gratuitous_arp','__gateway_mac_address','__accept_unicast_arp_request',)

  _yang_name = 'ipv4'
  _rest_name = 'ipv4'

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
    self.__enable_global = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable_global", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable Fabric virtual gateway', u'cli-show-no': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='empty', is_config=True)
    self.__gateway_mac_address = YANGDynClass(base=unicode, is_leaf=True, yang_name="gateway-mac-address", rest_name="gateway-mac-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Gateway MAC address for ARP requests'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='mac-access-list:mac-address-type', is_config=True)
    self.__accept_unicast_arp_request = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="accept-unicast-arp-request", rest_name="accept-unicast-arp-request", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Accept Unicast Arp Request'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='empty', is_config=True)
    self.__gratuitous_arp = YANGDynClass(base=gratuitous_arp.gratuitous_arp, is_container='container', yang_name="gratuitous-arp", rest_name="gratuitous-arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Gratuitous ARP'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='container', is_config=True)

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
      return [u'router', u'fabric-virtual-gateway', u'address-family', u'ipv4']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'fabric-virtual-gateway', u'address-family', u'ipv4']

  def _get_enable_global(self):
    """
    Getter method for enable_global, mapped from YANG variable /router/fabric_virtual_gateway/address_family/ipv4/enable_global (empty)
    """
    return self.__enable_global
      
  def _set_enable_global(self, v, load=False):
    """
    Setter method for enable_global, mapped from YANG variable /router/fabric_virtual_gateway/address_family/ipv4/enable_global (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable_global is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable_global() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="enable_global", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable Fabric virtual gateway', u'cli-show-no': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable_global must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable_global", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable Fabric virtual gateway', u'cli-show-no': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='empty', is_config=True)""",
        })

    self.__enable_global = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable_global(self):
    self.__enable_global = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable_global", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable Fabric virtual gateway', u'cli-show-no': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='empty', is_config=True)


  def _get_gratuitous_arp(self):
    """
    Getter method for gratuitous_arp, mapped from YANG variable /router/fabric_virtual_gateway/address_family/ipv4/gratuitous_arp (container)
    """
    return self.__gratuitous_arp
      
  def _set_gratuitous_arp(self, v, load=False):
    """
    Setter method for gratuitous_arp, mapped from YANG variable /router/fabric_virtual_gateway/address_family/ipv4/gratuitous_arp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_gratuitous_arp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_gratuitous_arp() directly.
    """
    try:
      t = YANGDynClass(v,base=gratuitous_arp.gratuitous_arp, is_container='container', yang_name="gratuitous-arp", rest_name="gratuitous-arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Gratuitous ARP'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """gratuitous_arp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=gratuitous_arp.gratuitous_arp, is_container='container', yang_name="gratuitous-arp", rest_name="gratuitous-arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Gratuitous ARP'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='container', is_config=True)""",
        })

    self.__gratuitous_arp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_gratuitous_arp(self):
    self.__gratuitous_arp = YANGDynClass(base=gratuitous_arp.gratuitous_arp, is_container='container', yang_name="gratuitous-arp", rest_name="gratuitous-arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Gratuitous ARP'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='container', is_config=True)


  def _get_gateway_mac_address(self):
    """
    Getter method for gateway_mac_address, mapped from YANG variable /router/fabric_virtual_gateway/address_family/ipv4/gateway_mac_address (mac-access-list:mac-address-type)
    """
    return self.__gateway_mac_address
      
  def _set_gateway_mac_address(self, v, load=False):
    """
    Setter method for gateway_mac_address, mapped from YANG variable /router/fabric_virtual_gateway/address_family/ipv4/gateway_mac_address (mac-access-list:mac-address-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_gateway_mac_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_gateway_mac_address() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="gateway-mac-address", rest_name="gateway-mac-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Gateway MAC address for ARP requests'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='mac-access-list:mac-address-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """gateway_mac_address must be of a type compatible with mac-access-list:mac-address-type""",
          'defined-type': "mac-access-list:mac-address-type",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="gateway-mac-address", rest_name="gateway-mac-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Gateway MAC address for ARP requests'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='mac-access-list:mac-address-type', is_config=True)""",
        })

    self.__gateway_mac_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_gateway_mac_address(self):
    self.__gateway_mac_address = YANGDynClass(base=unicode, is_leaf=True, yang_name="gateway-mac-address", rest_name="gateway-mac-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Gateway MAC address for ARP requests'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='mac-access-list:mac-address-type', is_config=True)


  def _get_accept_unicast_arp_request(self):
    """
    Getter method for accept_unicast_arp_request, mapped from YANG variable /router/fabric_virtual_gateway/address_family/ipv4/accept_unicast_arp_request (empty)

    YANG Description: Accept Unicast Arp Request
    """
    return self.__accept_unicast_arp_request
      
  def _set_accept_unicast_arp_request(self, v, load=False):
    """
    Setter method for accept_unicast_arp_request, mapped from YANG variable /router/fabric_virtual_gateway/address_family/ipv4/accept_unicast_arp_request (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_accept_unicast_arp_request is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_accept_unicast_arp_request() directly.

    YANG Description: Accept Unicast Arp Request
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="accept-unicast-arp-request", rest_name="accept-unicast-arp-request", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Accept Unicast Arp Request'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """accept_unicast_arp_request must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="accept-unicast-arp-request", rest_name="accept-unicast-arp-request", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Accept Unicast Arp Request'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='empty', is_config=True)""",
        })

    self.__accept_unicast_arp_request = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_accept_unicast_arp_request(self):
    self.__accept_unicast_arp_request = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="accept-unicast-arp-request", rest_name="accept-unicast-arp-request", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Accept Unicast Arp Request'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='empty', is_config=True)

  enable_global = __builtin__.property(_get_enable_global, _set_enable_global)
  gratuitous_arp = __builtin__.property(_get_gratuitous_arp, _set_gratuitous_arp)
  gateway_mac_address = __builtin__.property(_get_gateway_mac_address, _set_gateway_mac_address)
  accept_unicast_arp_request = __builtin__.property(_get_accept_unicast_arp_request, _set_accept_unicast_arp_request)


  _pyangbind_elements = {'enable_global': enable_global, 'gratuitous_arp': gratuitous_arp, 'gateway_mac_address': gateway_mac_address, 'accept_unicast_arp_request': accept_unicast_arp_request, }


