
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class virtual_ip(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/interface/ve/ipv6/vrrpv3e/virtual-ip. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__virtual_ipaddr',)

  _yang_name = 'virtual-ip'
  _rest_name = 'virtual-ip'

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
    self.__virtual_ipaddr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="virtual-ipaddr", rest_name="virtual-ipaddr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Virtual IPv6 address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='inet:ipv6-address', is_config=True)

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
      return [u'rbridge-id', u'interface', u've', u'ipv6', u'vrrpv3e', u'virtual-ip']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'interface', u'Ve', u'ipv6', u'vrrp-extended-group', u'virtual-ip']

  def _get_virtual_ipaddr(self):
    """
    Getter method for virtual_ipaddr, mapped from YANG variable /rbridge_id/interface/ve/ipv6/vrrpv3e/virtual_ip/virtual_ipaddr (inet:ipv6-address)

    YANG Description: Virtual IPv6 address
    """
    return self.__virtual_ipaddr
      
  def _set_virtual_ipaddr(self, v, load=False):
    """
    Setter method for virtual_ipaddr, mapped from YANG variable /rbridge_id/interface/ve/ipv6/vrrpv3e/virtual_ip/virtual_ipaddr (inet:ipv6-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_virtual_ipaddr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_virtual_ipaddr() directly.

    YANG Description: Virtual IPv6 address
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="virtual-ipaddr", rest_name="virtual-ipaddr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Virtual IPv6 address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='inet:ipv6-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """virtual_ipaddr must be of a type compatible with inet:ipv6-address""",
          'defined-type': "inet:ipv6-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="virtual-ipaddr", rest_name="virtual-ipaddr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Virtual IPv6 address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='inet:ipv6-address', is_config=True)""",
        })

    self.__virtual_ipaddr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_virtual_ipaddr(self):
    self.__virtual_ipaddr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="virtual-ipaddr", rest_name="virtual-ipaddr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Virtual IPv6 address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='inet:ipv6-address', is_config=True)

  virtual_ipaddr = __builtin__.property(_get_virtual_ipaddr, _set_virtual_ipaddr)


  _pyangbind_elements = {'virtual_ipaddr': virtual_ipaddr, }

