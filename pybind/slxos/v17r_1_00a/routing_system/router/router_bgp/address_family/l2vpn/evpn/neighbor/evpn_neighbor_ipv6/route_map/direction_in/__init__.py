
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class direction_in(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/l2vpn/evpn/neighbor/evpn-neighbor-ipv6/route-map/direction-in. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__route_map_name_direction_in',)

  _yang_name = 'direction-in'
  _rest_name = 'in'

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
    self.__route_map_name_direction_in = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,63})'}), is_leaf=True, yang_name="route-map-name-direction-in", rest_name="route-map-name-direction-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='common-def:name-string64', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'l2vpn', u'evpn', u'neighbor', u'evpn-neighbor-ipv6', u'route-map', u'direction-in']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'address-family', u'l2vpn', u'evpn', u'neighbor', u'evpn-neighbor-ipv6', u'route-map', u'in']

  def _get_route_map_name_direction_in(self):
    """
    Getter method for route_map_name_direction_in, mapped from YANG variable /routing_system/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_neighbor_ipv6/route_map/direction_in/route_map_name_direction_in (common-def:name-string64)
    """
    return self.__route_map_name_direction_in
      
  def _set_route_map_name_direction_in(self, v, load=False):
    """
    Setter method for route_map_name_direction_in, mapped from YANG variable /routing_system/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_neighbor_ipv6/route_map/direction_in/route_map_name_direction_in (common-def:name-string64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_map_name_direction_in is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_map_name_direction_in() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,63})'}), is_leaf=True, yang_name="route-map-name-direction-in", rest_name="route-map-name-direction-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='common-def:name-string64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_map_name_direction_in must be of a type compatible with common-def:name-string64""",
          'defined-type': "common-def:name-string64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,63})'}), is_leaf=True, yang_name="route-map-name-direction-in", rest_name="route-map-name-direction-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='common-def:name-string64', is_config=True)""",
        })

    self.__route_map_name_direction_in = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_map_name_direction_in(self):
    self.__route_map_name_direction_in = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,63})'}), is_leaf=True, yang_name="route-map-name-direction-in", rest_name="route-map-name-direction-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='common-def:name-string64', is_config=True)

  route_map_name_direction_in = __builtin__.property(_get_route_map_name_direction_in, _set_route_map_name_direction_in)


  _pyangbind_elements = {'route_map_name_direction_in': route_map_name_direction_in, }


