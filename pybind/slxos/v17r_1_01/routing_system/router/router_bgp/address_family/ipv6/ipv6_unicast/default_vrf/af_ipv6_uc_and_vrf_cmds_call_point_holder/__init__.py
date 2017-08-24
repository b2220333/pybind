
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import redistribute
class af_ipv6_uc_and_vrf_cmds_call_point_holder(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/ipv6/ipv6-unicast/default-vrf/af-ipv6-uc-and-vrf-cmds-call-point-holder. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__bgp_redistribute_internal','__redistribute',)

  _yang_name = 'af-ipv6-uc-and-vrf-cmds-call-point-holder'
  _rest_name = ''

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
    self.__redistribute = YANGDynClass(base=redistribute.redistribute, is_container='container', presence=False, yang_name="redistribute", rest_name="redistribute", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Redistribute information from another routing protocol', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__bgp_redistribute_internal = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bgp-redistribute-internal", rest_name="bgp-redistribute-internal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Allow redistribution of iBGP routes into IGPs'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv6', u'ipv6-unicast', u'default-vrf', u'af-ipv6-uc-and-vrf-cmds-call-point-holder']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'address-family', u'ipv6', u'unicast']

  def _get_bgp_redistribute_internal(self):
    """
    Getter method for bgp_redistribute_internal, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/bgp_redistribute_internal (empty)
    """
    return self.__bgp_redistribute_internal
      
  def _set_bgp_redistribute_internal(self, v, load=False):
    """
    Setter method for bgp_redistribute_internal, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/bgp_redistribute_internal (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bgp_redistribute_internal is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bgp_redistribute_internal() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="bgp-redistribute-internal", rest_name="bgp-redistribute-internal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Allow redistribution of iBGP routes into IGPs'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bgp_redistribute_internal must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bgp-redistribute-internal", rest_name="bgp-redistribute-internal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Allow redistribution of iBGP routes into IGPs'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__bgp_redistribute_internal = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bgp_redistribute_internal(self):
    self.__bgp_redistribute_internal = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bgp-redistribute-internal", rest_name="bgp-redistribute-internal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Allow redistribution of iBGP routes into IGPs'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_redistribute(self):
    """
    Getter method for redistribute, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/redistribute (container)
    """
    return self.__redistribute
      
  def _set_redistribute(self, v, load=False):
    """
    Setter method for redistribute, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/redistribute (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redistribute is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redistribute() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=redistribute.redistribute, is_container='container', presence=False, yang_name="redistribute", rest_name="redistribute", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Redistribute information from another routing protocol', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redistribute must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=redistribute.redistribute, is_container='container', presence=False, yang_name="redistribute", rest_name="redistribute", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Redistribute information from another routing protocol', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__redistribute = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redistribute(self):
    self.__redistribute = YANGDynClass(base=redistribute.redistribute, is_container='container', presence=False, yang_name="redistribute", rest_name="redistribute", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Redistribute information from another routing protocol', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

  bgp_redistribute_internal = __builtin__.property(_get_bgp_redistribute_internal, _set_bgp_redistribute_internal)
  redistribute = __builtin__.property(_get_redistribute, _set_redistribute)


  _pyangbind_elements = {'bgp_redistribute_internal': bgp_redistribute_internal, 'redistribute': redistribute, }


