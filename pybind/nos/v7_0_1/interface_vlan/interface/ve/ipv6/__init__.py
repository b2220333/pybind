
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ipv6_anycast_gateway
class ipv6(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface-vlan/interface/ve/ipv6. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The IPv6 configurations for an interface.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ipv6_anycast_gateway',)

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
    self.__ipv6_anycast_gateway = YANGDynClass(base=YANGListType("ipv6_gw_id",ipv6_anycast_gateway.ipv6_anycast_gateway, yang_name="ipv6-anycast-gateway", rest_name="fabric-virtual-gateway", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-gw-id', extensions={u'tailf-common': {u'info': u'IPv6 Fabric virtual gateway', u'cli-run-template-enter': u'$(.?:)', u'alt-name': u'fabric-virtual-gateway', u'callpoint': u'AnycastGatewayGlobalVeIpv6Config', u'cli-no-key-completion': None, u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-ipv6-fabric-virtual-gw'}}), is_container='list', yang_name="ipv6-anycast-gateway", rest_name="fabric-virtual-gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv6 Fabric virtual gateway', u'cli-run-template-enter': u'$(.?:)', u'alt-name': u'fabric-virtual-gateway', u'callpoint': u'AnycastGatewayGlobalVeIpv6Config', u'cli-no-key-completion': None, u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-ipv6-fabric-virtual-gw'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)

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
      return [u'interface-vlan', u'interface', u've', u'ipv6']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ve', u'ipv6']

  def _get_ipv6_anycast_gateway(self):
    """
    Getter method for ipv6_anycast_gateway, mapped from YANG variable /interface_vlan/interface/ve/ipv6/ipv6_anycast_gateway (list)
    """
    return self.__ipv6_anycast_gateway
      
  def _set_ipv6_anycast_gateway(self, v, load=False):
    """
    Setter method for ipv6_anycast_gateway, mapped from YANG variable /interface_vlan/interface/ve/ipv6/ipv6_anycast_gateway (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_anycast_gateway is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_anycast_gateway() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("ipv6_gw_id",ipv6_anycast_gateway.ipv6_anycast_gateway, yang_name="ipv6-anycast-gateway", rest_name="fabric-virtual-gateway", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-gw-id', extensions={u'tailf-common': {u'info': u'IPv6 Fabric virtual gateway', u'cli-run-template-enter': u'$(.?:)', u'alt-name': u'fabric-virtual-gateway', u'callpoint': u'AnycastGatewayGlobalVeIpv6Config', u'cli-no-key-completion': None, u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-ipv6-fabric-virtual-gw'}}), is_container='list', yang_name="ipv6-anycast-gateway", rest_name="fabric-virtual-gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv6 Fabric virtual gateway', u'cli-run-template-enter': u'$(.?:)', u'alt-name': u'fabric-virtual-gateway', u'callpoint': u'AnycastGatewayGlobalVeIpv6Config', u'cli-no-key-completion': None, u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-ipv6-fabric-virtual-gw'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_anycast_gateway must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ipv6_gw_id",ipv6_anycast_gateway.ipv6_anycast_gateway, yang_name="ipv6-anycast-gateway", rest_name="fabric-virtual-gateway", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-gw-id', extensions={u'tailf-common': {u'info': u'IPv6 Fabric virtual gateway', u'cli-run-template-enter': u'$(.?:)', u'alt-name': u'fabric-virtual-gateway', u'callpoint': u'AnycastGatewayGlobalVeIpv6Config', u'cli-no-key-completion': None, u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-ipv6-fabric-virtual-gw'}}), is_container='list', yang_name="ipv6-anycast-gateway", rest_name="fabric-virtual-gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv6 Fabric virtual gateway', u'cli-run-template-enter': u'$(.?:)', u'alt-name': u'fabric-virtual-gateway', u'callpoint': u'AnycastGatewayGlobalVeIpv6Config', u'cli-no-key-completion': None, u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-ipv6-fabric-virtual-gw'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)""",
        })

    self.__ipv6_anycast_gateway = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_anycast_gateway(self):
    self.__ipv6_anycast_gateway = YANGDynClass(base=YANGListType("ipv6_gw_id",ipv6_anycast_gateway.ipv6_anycast_gateway, yang_name="ipv6-anycast-gateway", rest_name="fabric-virtual-gateway", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-gw-id', extensions={u'tailf-common': {u'info': u'IPv6 Fabric virtual gateway', u'cli-run-template-enter': u'$(.?:)', u'alt-name': u'fabric-virtual-gateway', u'callpoint': u'AnycastGatewayGlobalVeIpv6Config', u'cli-no-key-completion': None, u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-ipv6-fabric-virtual-gw'}}), is_container='list', yang_name="ipv6-anycast-gateway", rest_name="fabric-virtual-gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv6 Fabric virtual gateway', u'cli-run-template-enter': u'$(.?:)', u'alt-name': u'fabric-virtual-gateway', u'callpoint': u'AnycastGatewayGlobalVeIpv6Config', u'cli-no-key-completion': None, u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-ipv6-fabric-virtual-gw'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)

  ipv6_anycast_gateway = __builtin__.property(_get_ipv6_anycast_gateway, _set_ipv6_anycast_gateway)


  _pyangbind_elements = {'ipv6_anycast_gateway': ipv6_anycast_gateway, }


