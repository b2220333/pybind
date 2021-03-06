
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class network(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/interface/ve/ipv6/vrrpv3e/track/network. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__network_address','__network_priority',)

  _yang_name = 'network'
  _rest_name = 'network'

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
    self.__network_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..254']}), is_leaf=True, yang_name="network-priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'priority'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='uint8', is_config=True)
    self.__network_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="network-address", rest_name="network-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'XXXX::YYYY/L;;IPv6 global address prefix in ipv6-address/Prefix length format'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='common-def:ipv6-address-prefix', is_config=True)

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
      return [u'routing-system', u'interface', u've', u'ipv6', u'vrrpv3e', u'track', u'network']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ve', u'ipv6', u'vrrp-extended-group', u'track', u'network']

  def _get_network_address(self):
    """
    Getter method for network_address, mapped from YANG variable /routing_system/interface/ve/ipv6/vrrpv3e/track/network/network_address (common-def:ipv6-address-prefix)

    YANG Description: IPv6 global address
    """
    return self.__network_address
      
  def _set_network_address(self, v, load=False):
    """
    Setter method for network_address, mapped from YANG variable /routing_system/interface/ve/ipv6/vrrpv3e/track/network/network_address (common-def:ipv6-address-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_network_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_network_address() directly.

    YANG Description: IPv6 global address
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="network-address", rest_name="network-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'XXXX::YYYY/L;;IPv6 global address prefix in ipv6-address/Prefix length format'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='common-def:ipv6-address-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """network_address must be of a type compatible with common-def:ipv6-address-prefix""",
          'defined-type': "common-def:ipv6-address-prefix",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="network-address", rest_name="network-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'XXXX::YYYY/L;;IPv6 global address prefix in ipv6-address/Prefix length format'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='common-def:ipv6-address-prefix', is_config=True)""",
        })

    self.__network_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_network_address(self):
    self.__network_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="network-address", rest_name="network-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'XXXX::YYYY/L;;IPv6 global address prefix in ipv6-address/Prefix length format'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='common-def:ipv6-address-prefix', is_config=True)


  def _get_network_priority(self):
    """
    Getter method for network_priority, mapped from YANG variable /routing_system/interface/ve/ipv6/vrrpv3e/track/network/network_priority (uint8)
    """
    return self.__network_priority
      
  def _set_network_priority(self, v, load=False):
    """
    Setter method for network_priority, mapped from YANG variable /routing_system/interface/ve/ipv6/vrrpv3e/track/network/network_priority (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_network_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_network_priority() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..254']}), is_leaf=True, yang_name="network-priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'priority'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """network_priority must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..254']}), is_leaf=True, yang_name="network-priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'priority'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='uint8', is_config=True)""",
        })

    self.__network_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_network_priority(self):
    self.__network_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..254']}), is_leaf=True, yang_name="network-priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'priority'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='uint8', is_config=True)

  network_address = __builtin__.property(_get_network_address, _set_network_address)
  network_priority = __builtin__.property(_get_network_priority, _set_network_priority)


  _pyangbind_elements = {'network_address': network_address, 'network_priority': network_priority, }


