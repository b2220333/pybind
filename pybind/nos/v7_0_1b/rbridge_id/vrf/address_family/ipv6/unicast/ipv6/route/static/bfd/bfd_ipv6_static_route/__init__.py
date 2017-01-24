
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import bfd_ipv6_interval_attributes
class bfd_ipv6_static_route(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/vrf/address-family/ipv6/unicast/ipv6/route/static/bfd/bfd-ipv6-static-route. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__bfd_ipv6_static_route_dest','__bfd_ipv6_static_route_src','__bfd_ipv6_interval_attributes',)

  _yang_name = 'bfd-ipv6-static-route'
  _rest_name = 'bfd-ipv6-static-route'

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
    self.__bfd_ipv6_static_route_dest = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="bfd-ipv6-static-route-dest", rest_name="bfd-ipv6-static-route-dest", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D ;; Destination IPv6 address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-address', is_config=True)
    self.__bfd_ipv6_interval_attributes = YANGDynClass(base=bfd_ipv6_interval_attributes.bfd_ipv6_interval_attributes, is_container='container', presence=False, yang_name="bfd-ipv6-interval-attributes", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='container', is_config=True)
    self.__bfd_ipv6_static_route_src = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="bfd-ipv6-static-route-src", rest_name="bfd-ipv6-static-route-src", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D ;; Source IPv6 address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-address', is_config=True)

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
      return [u'rbridge-id', u'vrf', u'address-family', u'ipv6', u'unicast', u'ipv6', u'route', u'static', u'bfd', u'bfd-ipv6-static-route']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'vrf', u'address-family', u'ipv6', u'unicast', u'ipv6', u'route', u'static', u'bfd', u'bfd-ipv6-static-route']

  def _get_bfd_ipv6_static_route_dest(self):
    """
    Getter method for bfd_ipv6_static_route_dest, mapped from YANG variable /rbridge_id/vrf/address_family/ipv6/unicast/ipv6/route/static/bfd/bfd_ipv6_static_route/bfd_ipv6_static_route_dest (inet:ipv6-address)
    """
    return self.__bfd_ipv6_static_route_dest
      
  def _set_bfd_ipv6_static_route_dest(self, v, load=False):
    """
    Setter method for bfd_ipv6_static_route_dest, mapped from YANG variable /rbridge_id/vrf/address_family/ipv6/unicast/ipv6/route/static/bfd/bfd_ipv6_static_route/bfd_ipv6_static_route_dest (inet:ipv6-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bfd_ipv6_static_route_dest is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bfd_ipv6_static_route_dest() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="bfd-ipv6-static-route-dest", rest_name="bfd-ipv6-static-route-dest", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D ;; Destination IPv6 address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bfd_ipv6_static_route_dest must be of a type compatible with inet:ipv6-address""",
          'defined-type': "inet:ipv6-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="bfd-ipv6-static-route-dest", rest_name="bfd-ipv6-static-route-dest", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D ;; Destination IPv6 address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-address', is_config=True)""",
        })

    self.__bfd_ipv6_static_route_dest = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bfd_ipv6_static_route_dest(self):
    self.__bfd_ipv6_static_route_dest = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="bfd-ipv6-static-route-dest", rest_name="bfd-ipv6-static-route-dest", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D ;; Destination IPv6 address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-address', is_config=True)


  def _get_bfd_ipv6_static_route_src(self):
    """
    Getter method for bfd_ipv6_static_route_src, mapped from YANG variable /rbridge_id/vrf/address_family/ipv6/unicast/ipv6/route/static/bfd/bfd_ipv6_static_route/bfd_ipv6_static_route_src (inet:ipv6-address)
    """
    return self.__bfd_ipv6_static_route_src
      
  def _set_bfd_ipv6_static_route_src(self, v, load=False):
    """
    Setter method for bfd_ipv6_static_route_src, mapped from YANG variable /rbridge_id/vrf/address_family/ipv6/unicast/ipv6/route/static/bfd/bfd_ipv6_static_route/bfd_ipv6_static_route_src (inet:ipv6-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bfd_ipv6_static_route_src is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bfd_ipv6_static_route_src() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="bfd-ipv6-static-route-src", rest_name="bfd-ipv6-static-route-src", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D ;; Source IPv6 address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bfd_ipv6_static_route_src must be of a type compatible with inet:ipv6-address""",
          'defined-type': "inet:ipv6-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="bfd-ipv6-static-route-src", rest_name="bfd-ipv6-static-route-src", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D ;; Source IPv6 address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-address', is_config=True)""",
        })

    self.__bfd_ipv6_static_route_src = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bfd_ipv6_static_route_src(self):
    self.__bfd_ipv6_static_route_src = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="bfd-ipv6-static-route-src", rest_name="bfd-ipv6-static-route-src", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D ;; Source IPv6 address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-address', is_config=True)


  def _get_bfd_ipv6_interval_attributes(self):
    """
    Getter method for bfd_ipv6_interval_attributes, mapped from YANG variable /rbridge_id/vrf/address_family/ipv6/unicast/ipv6/route/static/bfd/bfd_ipv6_static_route/bfd_ipv6_interval_attributes (container)
    """
    return self.__bfd_ipv6_interval_attributes
      
  def _set_bfd_ipv6_interval_attributes(self, v, load=False):
    """
    Setter method for bfd_ipv6_interval_attributes, mapped from YANG variable /rbridge_id/vrf/address_family/ipv6/unicast/ipv6/route/static/bfd/bfd_ipv6_static_route/bfd_ipv6_interval_attributes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bfd_ipv6_interval_attributes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bfd_ipv6_interval_attributes() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=bfd_ipv6_interval_attributes.bfd_ipv6_interval_attributes, is_container='container', presence=False, yang_name="bfd-ipv6-interval-attributes", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bfd_ipv6_interval_attributes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=bfd_ipv6_interval_attributes.bfd_ipv6_interval_attributes, is_container='container', presence=False, yang_name="bfd-ipv6-interval-attributes", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='container', is_config=True)""",
        })

    self.__bfd_ipv6_interval_attributes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bfd_ipv6_interval_attributes(self):
    self.__bfd_ipv6_interval_attributes = YANGDynClass(base=bfd_ipv6_interval_attributes.bfd_ipv6_interval_attributes, is_container='container', presence=False, yang_name="bfd-ipv6-interval-attributes", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='container', is_config=True)

  bfd_ipv6_static_route_dest = __builtin__.property(_get_bfd_ipv6_static_route_dest, _set_bfd_ipv6_static_route_dest)
  bfd_ipv6_static_route_src = __builtin__.property(_get_bfd_ipv6_static_route_src, _set_bfd_ipv6_static_route_src)
  bfd_ipv6_interval_attributes = __builtin__.property(_get_bfd_ipv6_interval_attributes, _set_bfd_ipv6_interval_attributes)


  _pyangbind_elements = {'bfd_ipv6_static_route_dest': bfd_ipv6_static_route_dest, 'bfd_ipv6_static_route_src': bfd_ipv6_static_route_src, 'bfd_ipv6_interval_attributes': bfd_ipv6_interval_attributes, }


