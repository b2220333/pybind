
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class nh_info(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-isis-operational - based on the path /isis-state/ipv6-routes/ipv6-route-entry/nh-info. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: is-is route nexthop information
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ipv6_nh_addr','__outgoing_intf_name',)

  _yang_name = 'nh-info'
  _rest_name = 'nh-info'

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
    self.__outgoing_intf_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="outgoing-intf-name", rest_name="outgoing-intf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)
    self.__ipv6_nh_addr = YANGDynClass(base=unicode, is_leaf=True, yang_name="ipv6-nh-addr", rest_name="ipv6-nh-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)

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
      return [u'isis-state', u'ipv6-routes', u'ipv6-route-entry', u'nh-info']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'isis-state', u'ipv6-routes', u'ipv6-route-entry', u'nh-info']

  def _get_ipv6_nh_addr(self):
    """
    Getter method for ipv6_nh_addr, mapped from YANG variable /isis_state/ipv6_routes/ipv6_route_entry/nh_info/ipv6_nh_addr (string)

    YANG Description: IPv6 nexthop address 
    """
    return self.__ipv6_nh_addr
      
  def _set_ipv6_nh_addr(self, v, load=False):
    """
    Setter method for ipv6_nh_addr, mapped from YANG variable /isis_state/ipv6_routes/ipv6_route_entry/nh_info/ipv6_nh_addr (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_nh_addr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_nh_addr() directly.

    YANG Description: IPv6 nexthop address 
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="ipv6-nh-addr", rest_name="ipv6-nh-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_nh_addr must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="ipv6-nh-addr", rest_name="ipv6-nh-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)""",
        })

    self.__ipv6_nh_addr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_nh_addr(self):
    self.__ipv6_nh_addr = YANGDynClass(base=unicode, is_leaf=True, yang_name="ipv6-nh-addr", rest_name="ipv6-nh-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)


  def _get_outgoing_intf_name(self):
    """
    Getter method for outgoing_intf_name, mapped from YANG variable /isis_state/ipv6_routes/ipv6_route_entry/nh_info/outgoing_intf_name (string)

    YANG Description: outgoing interface name
    """
    return self.__outgoing_intf_name
      
  def _set_outgoing_intf_name(self, v, load=False):
    """
    Setter method for outgoing_intf_name, mapped from YANG variable /isis_state/ipv6_routes/ipv6_route_entry/nh_info/outgoing_intf_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_outgoing_intf_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_outgoing_intf_name() directly.

    YANG Description: outgoing interface name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="outgoing-intf-name", rest_name="outgoing-intf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """outgoing_intf_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="outgoing-intf-name", rest_name="outgoing-intf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)""",
        })

    self.__outgoing_intf_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_outgoing_intf_name(self):
    self.__outgoing_intf_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="outgoing-intf-name", rest_name="outgoing-intf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)

  ipv6_nh_addr = __builtin__.property(_get_ipv6_nh_addr)
  outgoing_intf_name = __builtin__.property(_get_outgoing_intf_name)


  _pyangbind_elements = {'ipv6_nh_addr': ipv6_nh_addr, 'outgoing_intf_name': outgoing_intf_name, }


