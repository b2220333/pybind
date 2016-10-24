
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class connected(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/ipv4/ipv4-unicast/af-vrf/af-ipv4-uc-and-vrf-cmds-call-point-holder/redistribute/connected. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__redistribute_connected','__unicast_metric','__redistribute_route_map',)

  _yang_name = 'connected'
  _rest_name = 'connected'

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
    self.__redistribute_connected = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="redistribute-connected", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-run-template': u'$(.?$(../unicast-metric?\\r:$(../redistribute-route-map?\\r:redistribute connected\n)):\\r)', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__unicast_metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="unicast-metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Metric for redistributed routes', u'cli-full-command': None, u'alt-name': u'metric'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='conn-metric', is_config=True)
    self.__redistribute_route_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="redistribute-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route map reference', u'cli-full-command': None, u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rmap-type', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv4', u'ipv4-unicast', u'af-vrf', u'af-ipv4-uc-and-vrf-cmds-call-point-holder', u'redistribute', u'connected']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'address-family', u'ipv4', u'unicast', u'vrf', u'redistribute', u'connected']

  def _get_redistribute_connected(self):
    """
    Getter method for redistribute_connected, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/af_ipv4_uc_and_vrf_cmds_call_point_holder/redistribute/connected/redistribute_connected (empty)
    """
    return self.__redistribute_connected
      
  def _set_redistribute_connected(self, v, load=False):
    """
    Setter method for redistribute_connected, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/af_ipv4_uc_and_vrf_cmds_call_point_holder/redistribute/connected/redistribute_connected (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redistribute_connected is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redistribute_connected() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="redistribute-connected", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-run-template': u'$(.?$(../unicast-metric?\\r:$(../redistribute-route-map?\\r:redistribute connected\n)):\\r)', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redistribute_connected must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="redistribute-connected", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-run-template': u'$(.?$(../unicast-metric?\\r:$(../redistribute-route-map?\\r:redistribute connected\n)):\\r)', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__redistribute_connected = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redistribute_connected(self):
    self.__redistribute_connected = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="redistribute-connected", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-run-template': u'$(.?$(../unicast-metric?\\r:$(../redistribute-route-map?\\r:redistribute connected\n)):\\r)', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_unicast_metric(self):
    """
    Getter method for unicast_metric, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/af_ipv4_uc_and_vrf_cmds_call_point_holder/redistribute/connected/unicast_metric (conn-metric)
    """
    return self.__unicast_metric
      
  def _set_unicast_metric(self, v, load=False):
    """
    Setter method for unicast_metric, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/af_ipv4_uc_and_vrf_cmds_call_point_holder/redistribute/connected/unicast_metric (conn-metric)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unicast_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unicast_metric() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="unicast-metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Metric for redistributed routes', u'cli-full-command': None, u'alt-name': u'metric'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='conn-metric', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unicast_metric must be of a type compatible with conn-metric""",
          'defined-type': "brocade-bgp:conn-metric",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="unicast-metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Metric for redistributed routes', u'cli-full-command': None, u'alt-name': u'metric'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='conn-metric', is_config=True)""",
        })

    self.__unicast_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unicast_metric(self):
    self.__unicast_metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="unicast-metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Metric for redistributed routes', u'cli-full-command': None, u'alt-name': u'metric'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='conn-metric', is_config=True)


  def _get_redistribute_route_map(self):
    """
    Getter method for redistribute_route_map, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/af_ipv4_uc_and_vrf_cmds_call_point_holder/redistribute/connected/redistribute_route_map (rmap-type)
    """
    return self.__redistribute_route_map
      
  def _set_redistribute_route_map(self, v, load=False):
    """
    Setter method for redistribute_route_map, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/af_ipv4_uc_and_vrf_cmds_call_point_holder/redistribute/connected/redistribute_route_map (rmap-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redistribute_route_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redistribute_route_map() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="redistribute-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route map reference', u'cli-full-command': None, u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rmap-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redistribute_route_map must be of a type compatible with rmap-type""",
          'defined-type': "brocade-bgp:rmap-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="redistribute-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route map reference', u'cli-full-command': None, u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rmap-type', is_config=True)""",
        })

    self.__redistribute_route_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redistribute_route_map(self):
    self.__redistribute_route_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="redistribute-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route map reference', u'cli-full-command': None, u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rmap-type', is_config=True)

  redistribute_connected = __builtin__.property(_get_redistribute_connected, _set_redistribute_connected)
  unicast_metric = __builtin__.property(_get_unicast_metric, _set_unicast_metric)
  redistribute_route_map = __builtin__.property(_get_redistribute_route_map, _set_redistribute_route_map)


  _pyangbind_elements = {'redistribute_connected': redistribute_connected, 'unicast_metric': unicast_metric, 'redistribute_route_map': redistribute_route_map, }


