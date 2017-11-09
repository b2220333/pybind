
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class match(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/ipv6/ipv6-unicast/af-ipv6-vrf/af-ipv6-uc-and-vrf-cmds-call-point-holder/redistribute/ospf/match. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ospf_internal','__ospf_external1','__ospf_external2',)

  _yang_name = 'match'
  _rest_name = 'match'

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
    self.__ospf_internal = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ospf-internal", rest_name="internal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internal routes', u'cli-run-template': u'$(.?$(../ospf-external1?redistribute ospf match internal\n:$(../ospf-external2?redistribute ospf match internal\n:\\r)):\\r)', u'alt-name': u'internal', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__ospf_external2 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ospf-external2", rest_name="external2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'External type 2 routes', u'cli-full-command': None, u'alt-name': u'external2'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__ospf_external1 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ospf-external1", rest_name="external1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'External type 1 routes', u'cli-full-command': None, u'alt-name': u'external1'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv6', u'ipv6-unicast', u'af-ipv6-vrf', u'af-ipv6-uc-and-vrf-cmds-call-point-holder', u'redistribute', u'ospf', u'match']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'address-family', u'ipv6', u'unicast', u'vrf', u'redistribute', u'ospf', u'match']

  def _get_ospf_internal(self):
    """
    Getter method for ospf_internal, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/redistribute/ospf/match/ospf_internal (empty)
    """
    return self.__ospf_internal
      
  def _set_ospf_internal(self, v, load=False):
    """
    Setter method for ospf_internal, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/redistribute/ospf/match/ospf_internal (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ospf_internal is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ospf_internal() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ospf-internal", rest_name="internal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internal routes', u'cli-run-template': u'$(.?$(../ospf-external1?redistribute ospf match internal\n:$(../ospf-external2?redistribute ospf match internal\n:\\r)):\\r)', u'alt-name': u'internal', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ospf_internal must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ospf-internal", rest_name="internal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internal routes', u'cli-run-template': u'$(.?$(../ospf-external1?redistribute ospf match internal\n:$(../ospf-external2?redistribute ospf match internal\n:\\r)):\\r)', u'alt-name': u'internal', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__ospf_internal = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ospf_internal(self):
    self.__ospf_internal = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ospf-internal", rest_name="internal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internal routes', u'cli-run-template': u'$(.?$(../ospf-external1?redistribute ospf match internal\n:$(../ospf-external2?redistribute ospf match internal\n:\\r)):\\r)', u'alt-name': u'internal', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_ospf_external1(self):
    """
    Getter method for ospf_external1, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/redistribute/ospf/match/ospf_external1 (empty)
    """
    return self.__ospf_external1
      
  def _set_ospf_external1(self, v, load=False):
    """
    Setter method for ospf_external1, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/redistribute/ospf/match/ospf_external1 (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ospf_external1 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ospf_external1() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ospf-external1", rest_name="external1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'External type 1 routes', u'cli-full-command': None, u'alt-name': u'external1'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ospf_external1 must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ospf-external1", rest_name="external1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'External type 1 routes', u'cli-full-command': None, u'alt-name': u'external1'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__ospf_external1 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ospf_external1(self):
    self.__ospf_external1 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ospf-external1", rest_name="external1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'External type 1 routes', u'cli-full-command': None, u'alt-name': u'external1'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_ospf_external2(self):
    """
    Getter method for ospf_external2, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/redistribute/ospf/match/ospf_external2 (empty)
    """
    return self.__ospf_external2
      
  def _set_ospf_external2(self, v, load=False):
    """
    Setter method for ospf_external2, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/redistribute/ospf/match/ospf_external2 (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ospf_external2 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ospf_external2() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ospf-external2", rest_name="external2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'External type 2 routes', u'cli-full-command': None, u'alt-name': u'external2'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ospf_external2 must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ospf-external2", rest_name="external2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'External type 2 routes', u'cli-full-command': None, u'alt-name': u'external2'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__ospf_external2 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ospf_external2(self):
    self.__ospf_external2 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ospf-external2", rest_name="external2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'External type 2 routes', u'cli-full-command': None, u'alt-name': u'external2'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

  ospf_internal = __builtin__.property(_get_ospf_internal, _set_ospf_internal)
  ospf_external1 = __builtin__.property(_get_ospf_external1, _set_ospf_external1)
  ospf_external2 = __builtin__.property(_get_ospf_external2, _set_ospf_external2)


  _pyangbind_elements = {'ospf_internal': ospf_internal, 'ospf_external1': ospf_external1, 'ospf_external2': ospf_external2, }


