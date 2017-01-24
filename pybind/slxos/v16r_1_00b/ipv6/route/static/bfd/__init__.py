
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import bfd_ipv6_static_route
import bfd_ipv6_link_local_static_route
class bfd(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /ipv6/route/static/bfd. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__bfd_ipv6_static_route','__bfd_ipv6_link_local_static_route','__ipv6_holdover_interval',)

  _yang_name = 'bfd'
  _rest_name = 'bfd'

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
    self.__bfd_ipv6_static_route = YANGDynClass(base=YANGListType("bfd_ipv6_static_route_dest bfd_ipv6_static_route_src",bfd_ipv6_static_route.bfd_ipv6_static_route, yang_name="bfd-ipv6-static-route", rest_name="bfd-ipv6-static-route", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bfd-ipv6-static-route-dest bfd-ipv6-static-route-src', extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'BfdIpv6StaticRouteInterval'}}), is_container='list', yang_name="bfd-ipv6-static-route", rest_name="bfd-ipv6-static-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'BfdIpv6StaticRouteInterval'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='list', is_config=True)
    self.__ipv6_holdover_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..30']}), is_leaf=True, yang_name="ipv6-holdover-interval", rest_name="holdover-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Holdover interval', u'cli-full-command': None, u'alt-name': u'holdover-interval', u'callpoint': u'BfdIpv6HoldOverInterval'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='uint8', is_config=True)
    self.__bfd_ipv6_link_local_static_route = YANGDynClass(base=YANGListType("bfd_ipv6_link_local_dest bfd_ipv6_link_local_src bfd_interface_type bfd_interface_name",bfd_ipv6_link_local_static_route.bfd_ipv6_link_local_static_route, yang_name="bfd-ipv6-link-local-static-route", rest_name="bfd-ipv6-link-local-static-route", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bfd-ipv6-link-local-dest bfd-ipv6-link-local-src bfd-interface-type bfd-interface-name', extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'BfdIpv6LinkLocalInterval'}}), is_container='list', yang_name="bfd-ipv6-link-local-static-route", rest_name="bfd-ipv6-link-local-static-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'BfdIpv6LinkLocalInterval'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='list', is_config=True)

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
      return [u'ipv6', u'route', u'static', u'bfd']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ipv6', u'route', u'static', u'bfd']

  def _get_bfd_ipv6_static_route(self):
    """
    Getter method for bfd_ipv6_static_route, mapped from YANG variable /ipv6/route/static/bfd/bfd_ipv6_static_route (list)
    """
    return self.__bfd_ipv6_static_route
      
  def _set_bfd_ipv6_static_route(self, v, load=False):
    """
    Setter method for bfd_ipv6_static_route, mapped from YANG variable /ipv6/route/static/bfd/bfd_ipv6_static_route (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bfd_ipv6_static_route is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bfd_ipv6_static_route() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("bfd_ipv6_static_route_dest bfd_ipv6_static_route_src",bfd_ipv6_static_route.bfd_ipv6_static_route, yang_name="bfd-ipv6-static-route", rest_name="bfd-ipv6-static-route", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bfd-ipv6-static-route-dest bfd-ipv6-static-route-src', extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'BfdIpv6StaticRouteInterval'}}), is_container='list', yang_name="bfd-ipv6-static-route", rest_name="bfd-ipv6-static-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'BfdIpv6StaticRouteInterval'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bfd_ipv6_static_route must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("bfd_ipv6_static_route_dest bfd_ipv6_static_route_src",bfd_ipv6_static_route.bfd_ipv6_static_route, yang_name="bfd-ipv6-static-route", rest_name="bfd-ipv6-static-route", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bfd-ipv6-static-route-dest bfd-ipv6-static-route-src', extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'BfdIpv6StaticRouteInterval'}}), is_container='list', yang_name="bfd-ipv6-static-route", rest_name="bfd-ipv6-static-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'BfdIpv6StaticRouteInterval'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='list', is_config=True)""",
        })

    self.__bfd_ipv6_static_route = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bfd_ipv6_static_route(self):
    self.__bfd_ipv6_static_route = YANGDynClass(base=YANGListType("bfd_ipv6_static_route_dest bfd_ipv6_static_route_src",bfd_ipv6_static_route.bfd_ipv6_static_route, yang_name="bfd-ipv6-static-route", rest_name="bfd-ipv6-static-route", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bfd-ipv6-static-route-dest bfd-ipv6-static-route-src', extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'BfdIpv6StaticRouteInterval'}}), is_container='list', yang_name="bfd-ipv6-static-route", rest_name="bfd-ipv6-static-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'BfdIpv6StaticRouteInterval'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='list', is_config=True)


  def _get_bfd_ipv6_link_local_static_route(self):
    """
    Getter method for bfd_ipv6_link_local_static_route, mapped from YANG variable /ipv6/route/static/bfd/bfd_ipv6_link_local_static_route (list)
    """
    return self.__bfd_ipv6_link_local_static_route
      
  def _set_bfd_ipv6_link_local_static_route(self, v, load=False):
    """
    Setter method for bfd_ipv6_link_local_static_route, mapped from YANG variable /ipv6/route/static/bfd/bfd_ipv6_link_local_static_route (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bfd_ipv6_link_local_static_route is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bfd_ipv6_link_local_static_route() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("bfd_ipv6_link_local_dest bfd_ipv6_link_local_src bfd_interface_type bfd_interface_name",bfd_ipv6_link_local_static_route.bfd_ipv6_link_local_static_route, yang_name="bfd-ipv6-link-local-static-route", rest_name="bfd-ipv6-link-local-static-route", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bfd-ipv6-link-local-dest bfd-ipv6-link-local-src bfd-interface-type bfd-interface-name', extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'BfdIpv6LinkLocalInterval'}}), is_container='list', yang_name="bfd-ipv6-link-local-static-route", rest_name="bfd-ipv6-link-local-static-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'BfdIpv6LinkLocalInterval'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bfd_ipv6_link_local_static_route must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("bfd_ipv6_link_local_dest bfd_ipv6_link_local_src bfd_interface_type bfd_interface_name",bfd_ipv6_link_local_static_route.bfd_ipv6_link_local_static_route, yang_name="bfd-ipv6-link-local-static-route", rest_name="bfd-ipv6-link-local-static-route", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bfd-ipv6-link-local-dest bfd-ipv6-link-local-src bfd-interface-type bfd-interface-name', extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'BfdIpv6LinkLocalInterval'}}), is_container='list', yang_name="bfd-ipv6-link-local-static-route", rest_name="bfd-ipv6-link-local-static-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'BfdIpv6LinkLocalInterval'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='list', is_config=True)""",
        })

    self.__bfd_ipv6_link_local_static_route = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bfd_ipv6_link_local_static_route(self):
    self.__bfd_ipv6_link_local_static_route = YANGDynClass(base=YANGListType("bfd_ipv6_link_local_dest bfd_ipv6_link_local_src bfd_interface_type bfd_interface_name",bfd_ipv6_link_local_static_route.bfd_ipv6_link_local_static_route, yang_name="bfd-ipv6-link-local-static-route", rest_name="bfd-ipv6-link-local-static-route", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bfd-ipv6-link-local-dest bfd-ipv6-link-local-src bfd-interface-type bfd-interface-name', extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'BfdIpv6LinkLocalInterval'}}), is_container='list', yang_name="bfd-ipv6-link-local-static-route", rest_name="bfd-ipv6-link-local-static-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'BfdIpv6LinkLocalInterval'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='list', is_config=True)


  def _get_ipv6_holdover_interval(self):
    """
    Getter method for ipv6_holdover_interval, mapped from YANG variable /ipv6/route/static/bfd/ipv6_holdover_interval (uint8)
    """
    return self.__ipv6_holdover_interval
      
  def _set_ipv6_holdover_interval(self, v, load=False):
    """
    Setter method for ipv6_holdover_interval, mapped from YANG variable /ipv6/route/static/bfd/ipv6_holdover_interval (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_holdover_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_holdover_interval() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..30']}), is_leaf=True, yang_name="ipv6-holdover-interval", rest_name="holdover-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Holdover interval', u'cli-full-command': None, u'alt-name': u'holdover-interval', u'callpoint': u'BfdIpv6HoldOverInterval'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_holdover_interval must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..30']}), is_leaf=True, yang_name="ipv6-holdover-interval", rest_name="holdover-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Holdover interval', u'cli-full-command': None, u'alt-name': u'holdover-interval', u'callpoint': u'BfdIpv6HoldOverInterval'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='uint8', is_config=True)""",
        })

    self.__ipv6_holdover_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_holdover_interval(self):
    self.__ipv6_holdover_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..30']}), is_leaf=True, yang_name="ipv6-holdover-interval", rest_name="holdover-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Holdover interval', u'cli-full-command': None, u'alt-name': u'holdover-interval', u'callpoint': u'BfdIpv6HoldOverInterval'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='uint8', is_config=True)

  bfd_ipv6_static_route = __builtin__.property(_get_bfd_ipv6_static_route, _set_bfd_ipv6_static_route)
  bfd_ipv6_link_local_static_route = __builtin__.property(_get_bfd_ipv6_link_local_static_route, _set_bfd_ipv6_link_local_static_route)
  ipv6_holdover_interval = __builtin__.property(_get_ipv6_holdover_interval, _set_ipv6_holdover_interval)


  _pyangbind_elements = {'bfd_ipv6_static_route': bfd_ipv6_static_route, 'bfd_ipv6_link_local_static_route': bfd_ipv6_link_local_static_route, 'ipv6_holdover_interval': ipv6_holdover_interval, }


