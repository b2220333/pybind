
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import lsp_info
class nh_info(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-isis-operational - based on the path /isis-state/ipv4-routes/ipv4-route-entry/nh-info. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: is-is route nexthop information
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ipv4_nh_addr','__outgoing_intf_name','__is_mpls_tunnel_port','__lsp_info',)

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
    self.__is_mpls_tunnel_port = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="is-mpls-tunnel-port", rest_name="is-mpls-tunnel-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='boolean', is_config=False)
    self.__outgoing_intf_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="outgoing-intf-name", rest_name="outgoing-intf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)
    self.__ipv4_nh_addr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ipv4-nh-addr", rest_name="ipv4-nh-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__lsp_info = YANGDynClass(base=YANGListType("lsp_name",lsp_info.lsp_info, yang_name="lsp-info", rest_name="lsp-info", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-name', extensions={u'tailf-common': {u'callpoint': u'isis-lsp-entry', u'cli-suppress-show-path': None}}), is_container='list', yang_name="lsp-info", rest_name="lsp-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'isis-lsp-entry', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)

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
      return [u'isis-state', u'ipv4-routes', u'ipv4-route-entry', u'nh-info']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'isis-state', u'ipv4-routes', u'ipv4-route-entry', u'nh-info']

  def _get_ipv4_nh_addr(self):
    """
    Getter method for ipv4_nh_addr, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/nh_info/ipv4_nh_addr (inet:ipv4-address)

    YANG Description: IPv4 nexthop address 
    """
    return self.__ipv4_nh_addr
      
  def _set_ipv4_nh_addr(self, v, load=False):
    """
    Setter method for ipv4_nh_addr, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/nh_info/ipv4_nh_addr (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv4_nh_addr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv4_nh_addr() directly.

    YANG Description: IPv4 nexthop address 
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ipv4-nh-addr", rest_name="ipv4-nh-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv4_nh_addr must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ipv4-nh-addr", rest_name="ipv4-nh-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__ipv4_nh_addr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv4_nh_addr(self):
    self.__ipv4_nh_addr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ipv4-nh-addr", rest_name="ipv4-nh-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_outgoing_intf_name(self):
    """
    Getter method for outgoing_intf_name, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/nh_info/outgoing_intf_name (string)

    YANG Description: outgoing interface name
    """
    return self.__outgoing_intf_name
      
  def _set_outgoing_intf_name(self, v, load=False):
    """
    Setter method for outgoing_intf_name, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/nh_info/outgoing_intf_name (string)
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


  def _get_is_mpls_tunnel_port(self):
    """
    Getter method for is_mpls_tunnel_port, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/nh_info/is_mpls_tunnel_port (boolean)

    YANG Description: Interface Type
    """
    return self.__is_mpls_tunnel_port
      
  def _set_is_mpls_tunnel_port(self, v, load=False):
    """
    Setter method for is_mpls_tunnel_port, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/nh_info/is_mpls_tunnel_port (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_is_mpls_tunnel_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_is_mpls_tunnel_port() directly.

    YANG Description: Interface Type
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="is-mpls-tunnel-port", rest_name="is-mpls-tunnel-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """is_mpls_tunnel_port must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="is-mpls-tunnel-port", rest_name="is-mpls-tunnel-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='boolean', is_config=False)""",
        })

    self.__is_mpls_tunnel_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_is_mpls_tunnel_port(self):
    self.__is_mpls_tunnel_port = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="is-mpls-tunnel-port", rest_name="is-mpls-tunnel-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='boolean', is_config=False)


  def _get_lsp_info(self):
    """
    Getter method for lsp_info, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/nh_info/lsp_info (list)

    YANG Description: LSP Name
    """
    return self.__lsp_info
      
  def _set_lsp_info(self, v, load=False):
    """
    Setter method for lsp_info, mapped from YANG variable /isis_state/ipv4_routes/ipv4_route_entry/nh_info/lsp_info (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_info() directly.

    YANG Description: LSP Name
    """
    try:
      t = YANGDynClass(v,base=YANGListType("lsp_name",lsp_info.lsp_info, yang_name="lsp-info", rest_name="lsp-info", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-name', extensions={u'tailf-common': {u'callpoint': u'isis-lsp-entry', u'cli-suppress-show-path': None}}), is_container='list', yang_name="lsp-info", rest_name="lsp-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'isis-lsp-entry', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_info must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("lsp_name",lsp_info.lsp_info, yang_name="lsp-info", rest_name="lsp-info", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-name', extensions={u'tailf-common': {u'callpoint': u'isis-lsp-entry', u'cli-suppress-show-path': None}}), is_container='list', yang_name="lsp-info", rest_name="lsp-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'isis-lsp-entry', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)""",
        })

    self.__lsp_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_info(self):
    self.__lsp_info = YANGDynClass(base=YANGListType("lsp_name",lsp_info.lsp_info, yang_name="lsp-info", rest_name="lsp-info", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-name', extensions={u'tailf-common': {u'callpoint': u'isis-lsp-entry', u'cli-suppress-show-path': None}}), is_container='list', yang_name="lsp-info", rest_name="lsp-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'isis-lsp-entry', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)

  ipv4_nh_addr = __builtin__.property(_get_ipv4_nh_addr)
  outgoing_intf_name = __builtin__.property(_get_outgoing_intf_name)
  is_mpls_tunnel_port = __builtin__.property(_get_is_mpls_tunnel_port)
  lsp_info = __builtin__.property(_get_lsp_info)


  _pyangbind_elements = {'ipv4_nh_addr': ipv4_nh_addr, 'outgoing_intf_name': outgoing_intf_name, 'is_mpls_tunnel_port': is_mpls_tunnel_port, 'lsp_info': lsp_info, }


