
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class hop(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-bypass-lsp-debug/output/bypass-lsp/show-mpls-lsp-debug-info/show-mpls-lsp-instances-info/lsp-instances/lsp-cspf-exclude-hops/show-mpls-lsp-hop-list/hop. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__lsp_hop_address','__lsp_hop_strict_hop','__lsp_hop_loose_hop','__lsp_hop_is_router_id','__lsp_hop_has_protection','__lsp_hop_has_node_protection','__lsp_hop_has_bandwidth_protection','__lsp_hop_has_protection_in_use','__lsp_hop_avoid_node','__lsp_hop_avoid_local','__lsp_hop_avoid_remote',)

  _yang_name = 'hop'
  _rest_name = 'hop'

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
    self.__lsp_hop_avoid_remote = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-avoid-remote", rest_name="lsp-hop-avoid-remote", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__lsp_hop_avoid_node = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-avoid-node", rest_name="lsp-hop-avoid-node", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__lsp_hop_has_protection_in_use = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-has-protection-in-use", rest_name="lsp-hop-has-protection-in-use", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__lsp_hop_has_protection = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-has-protection", rest_name="lsp-hop-has-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__lsp_hop_avoid_local = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-avoid-local", rest_name="lsp-hop-avoid-local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__lsp_hop_has_bandwidth_protection = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-has-bandwidth-protection", rest_name="lsp-hop-has-bandwidth-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__lsp_hop_strict_hop = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-strict-hop", rest_name="lsp-hop-strict-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__lsp_hop_is_router_id = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-is-router-id", rest_name="lsp-hop-is-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__lsp_hop_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="lsp-hop-address", rest_name="lsp-hop-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    self.__lsp_hop_has_node_protection = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-has-node-protection", rest_name="lsp-hop-has-node-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__lsp_hop_loose_hop = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-loose-hop", rest_name="lsp-hop-loose-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-bypass-lsp-debug', u'output', u'bypass-lsp', u'show-mpls-lsp-debug-info', u'show-mpls-lsp-instances-info', u'lsp-instances', u'lsp-cspf-exclude-hops', u'show-mpls-lsp-hop-list', u'hop']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-bypass-lsp-debug', u'output', u'bypass-lsp', u'lsp-instances', u'lsp-cspf-exclude-hops', u'hop']

  def _get_lsp_hop_address(self):
    """
    Getter method for lsp_hop_address, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_debug/output/bypass_lsp/show_mpls_lsp_debug_info/show_mpls_lsp_instances_info/lsp_instances/lsp_cspf_exclude_hops/show_mpls_lsp_hop_list/hop/lsp_hop_address (inet:ipv4-address)

    YANG Description: Hop IP address
    """
    return self.__lsp_hop_address
      
  def _set_lsp_hop_address(self, v, load=False):
    """
    Setter method for lsp_hop_address, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_debug/output/bypass_lsp/show_mpls_lsp_debug_info/show_mpls_lsp_instances_info/lsp_instances/lsp_cspf_exclude_hops/show_mpls_lsp_hop_list/hop/lsp_hop_address (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_hop_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_hop_address() directly.

    YANG Description: Hop IP address
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="lsp-hop-address", rest_name="lsp-hop-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_hop_address must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="lsp-hop-address", rest_name="lsp-hop-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__lsp_hop_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_hop_address(self):
    self.__lsp_hop_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="lsp-hop-address", rest_name="lsp-hop-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)


  def _get_lsp_hop_strict_hop(self):
    """
    Getter method for lsp_hop_strict_hop, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_debug/output/bypass_lsp/show_mpls_lsp_debug_info/show_mpls_lsp_instances_info/lsp_instances/lsp_cspf_exclude_hops/show_mpls_lsp_hop_list/hop/lsp_hop_strict_hop (boolean)

    YANG Description: CSPF path Strict hop
    """
    return self.__lsp_hop_strict_hop
      
  def _set_lsp_hop_strict_hop(self, v, load=False):
    """
    Setter method for lsp_hop_strict_hop, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_debug/output/bypass_lsp/show_mpls_lsp_debug_info/show_mpls_lsp_instances_info/lsp_instances/lsp_cspf_exclude_hops/show_mpls_lsp_hop_list/hop/lsp_hop_strict_hop (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_hop_strict_hop is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_hop_strict_hop() directly.

    YANG Description: CSPF path Strict hop
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-hop-strict-hop", rest_name="lsp-hop-strict-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_hop_strict_hop must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-strict-hop", rest_name="lsp-hop-strict-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_hop_strict_hop = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_hop_strict_hop(self):
    self.__lsp_hop_strict_hop = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-strict-hop", rest_name="lsp-hop-strict-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_lsp_hop_loose_hop(self):
    """
    Getter method for lsp_hop_loose_hop, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_debug/output/bypass_lsp/show_mpls_lsp_debug_info/show_mpls_lsp_instances_info/lsp_instances/lsp_cspf_exclude_hops/show_mpls_lsp_hop_list/hop/lsp_hop_loose_hop (boolean)

    YANG Description: CSPF path Loose hop
    """
    return self.__lsp_hop_loose_hop
      
  def _set_lsp_hop_loose_hop(self, v, load=False):
    """
    Setter method for lsp_hop_loose_hop, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_debug/output/bypass_lsp/show_mpls_lsp_debug_info/show_mpls_lsp_instances_info/lsp_instances/lsp_cspf_exclude_hops/show_mpls_lsp_hop_list/hop/lsp_hop_loose_hop (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_hop_loose_hop is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_hop_loose_hop() directly.

    YANG Description: CSPF path Loose hop
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-hop-loose-hop", rest_name="lsp-hop-loose-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_hop_loose_hop must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-loose-hop", rest_name="lsp-hop-loose-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_hop_loose_hop = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_hop_loose_hop(self):
    self.__lsp_hop_loose_hop = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-loose-hop", rest_name="lsp-hop-loose-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_lsp_hop_is_router_id(self):
    """
    Getter method for lsp_hop_is_router_id, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_debug/output/bypass_lsp/show_mpls_lsp_debug_info/show_mpls_lsp_instances_info/lsp_instances/lsp_cspf_exclude_hops/show_mpls_lsp_hop_list/hop/lsp_hop_is_router_id (boolean)

    YANG Description: Hop is a router id hop
    """
    return self.__lsp_hop_is_router_id
      
  def _set_lsp_hop_is_router_id(self, v, load=False):
    """
    Setter method for lsp_hop_is_router_id, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_debug/output/bypass_lsp/show_mpls_lsp_debug_info/show_mpls_lsp_instances_info/lsp_instances/lsp_cspf_exclude_hops/show_mpls_lsp_hop_list/hop/lsp_hop_is_router_id (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_hop_is_router_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_hop_is_router_id() directly.

    YANG Description: Hop is a router id hop
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-hop-is-router-id", rest_name="lsp-hop-is-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_hop_is_router_id must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-is-router-id", rest_name="lsp-hop-is-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_hop_is_router_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_hop_is_router_id(self):
    self.__lsp_hop_is_router_id = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-is-router-id", rest_name="lsp-hop-is-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_lsp_hop_has_protection(self):
    """
    Getter method for lsp_hop_has_protection, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_debug/output/bypass_lsp/show_mpls_lsp_debug_info/show_mpls_lsp_instances_info/lsp_instances/lsp_cspf_exclude_hops/show_mpls_lsp_hop_list/hop/lsp_hop_has_protection (boolean)

    YANG Description: RRO hop Protection available
    """
    return self.__lsp_hop_has_protection
      
  def _set_lsp_hop_has_protection(self, v, load=False):
    """
    Setter method for lsp_hop_has_protection, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_debug/output/bypass_lsp/show_mpls_lsp_debug_info/show_mpls_lsp_instances_info/lsp_instances/lsp_cspf_exclude_hops/show_mpls_lsp_hop_list/hop/lsp_hop_has_protection (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_hop_has_protection is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_hop_has_protection() directly.

    YANG Description: RRO hop Protection available
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-hop-has-protection", rest_name="lsp-hop-has-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_hop_has_protection must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-has-protection", rest_name="lsp-hop-has-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_hop_has_protection = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_hop_has_protection(self):
    self.__lsp_hop_has_protection = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-has-protection", rest_name="lsp-hop-has-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_lsp_hop_has_node_protection(self):
    """
    Getter method for lsp_hop_has_node_protection, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_debug/output/bypass_lsp/show_mpls_lsp_debug_info/show_mpls_lsp_instances_info/lsp_instances/lsp_cspf_exclude_hops/show_mpls_lsp_hop_list/hop/lsp_hop_has_node_protection (boolean)

    YANG Description: RRO hop Node Protection available
    """
    return self.__lsp_hop_has_node_protection
      
  def _set_lsp_hop_has_node_protection(self, v, load=False):
    """
    Setter method for lsp_hop_has_node_protection, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_debug/output/bypass_lsp/show_mpls_lsp_debug_info/show_mpls_lsp_instances_info/lsp_instances/lsp_cspf_exclude_hops/show_mpls_lsp_hop_list/hop/lsp_hop_has_node_protection (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_hop_has_node_protection is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_hop_has_node_protection() directly.

    YANG Description: RRO hop Node Protection available
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-hop-has-node-protection", rest_name="lsp-hop-has-node-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_hop_has_node_protection must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-has-node-protection", rest_name="lsp-hop-has-node-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_hop_has_node_protection = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_hop_has_node_protection(self):
    self.__lsp_hop_has_node_protection = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-has-node-protection", rest_name="lsp-hop-has-node-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_lsp_hop_has_bandwidth_protection(self):
    """
    Getter method for lsp_hop_has_bandwidth_protection, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_debug/output/bypass_lsp/show_mpls_lsp_debug_info/show_mpls_lsp_instances_info/lsp_instances/lsp_cspf_exclude_hops/show_mpls_lsp_hop_list/hop/lsp_hop_has_bandwidth_protection (boolean)

    YANG Description: RRO hop bandwidth Protection available
    """
    return self.__lsp_hop_has_bandwidth_protection
      
  def _set_lsp_hop_has_bandwidth_protection(self, v, load=False):
    """
    Setter method for lsp_hop_has_bandwidth_protection, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_debug/output/bypass_lsp/show_mpls_lsp_debug_info/show_mpls_lsp_instances_info/lsp_instances/lsp_cspf_exclude_hops/show_mpls_lsp_hop_list/hop/lsp_hop_has_bandwidth_protection (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_hop_has_bandwidth_protection is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_hop_has_bandwidth_protection() directly.

    YANG Description: RRO hop bandwidth Protection available
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-hop-has-bandwidth-protection", rest_name="lsp-hop-has-bandwidth-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_hop_has_bandwidth_protection must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-has-bandwidth-protection", rest_name="lsp-hop-has-bandwidth-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_hop_has_bandwidth_protection = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_hop_has_bandwidth_protection(self):
    self.__lsp_hop_has_bandwidth_protection = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-has-bandwidth-protection", rest_name="lsp-hop-has-bandwidth-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_lsp_hop_has_protection_in_use(self):
    """
    Getter method for lsp_hop_has_protection_in_use, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_debug/output/bypass_lsp/show_mpls_lsp_debug_info/show_mpls_lsp_instances_info/lsp_instances/lsp_cspf_exclude_hops/show_mpls_lsp_hop_list/hop/lsp_hop_has_protection_in_use (boolean)

    YANG Description: RRO hop protection is in use
    """
    return self.__lsp_hop_has_protection_in_use
      
  def _set_lsp_hop_has_protection_in_use(self, v, load=False):
    """
    Setter method for lsp_hop_has_protection_in_use, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_debug/output/bypass_lsp/show_mpls_lsp_debug_info/show_mpls_lsp_instances_info/lsp_instances/lsp_cspf_exclude_hops/show_mpls_lsp_hop_list/hop/lsp_hop_has_protection_in_use (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_hop_has_protection_in_use is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_hop_has_protection_in_use() directly.

    YANG Description: RRO hop protection is in use
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-hop-has-protection-in-use", rest_name="lsp-hop-has-protection-in-use", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_hop_has_protection_in_use must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-has-protection-in-use", rest_name="lsp-hop-has-protection-in-use", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_hop_has_protection_in_use = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_hop_has_protection_in_use(self):
    self.__lsp_hop_has_protection_in_use = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-has-protection-in-use", rest_name="lsp-hop-has-protection-in-use", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_lsp_hop_avoid_node(self):
    """
    Getter method for lsp_hop_avoid_node, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_debug/output/bypass_lsp/show_mpls_lsp_debug_info/show_mpls_lsp_instances_info/lsp_instances/lsp_cspf_exclude_hops/show_mpls_lsp_hop_list/hop/lsp_hop_avoid_node (boolean)

    YANG Description: Avoid address type is node
    """
    return self.__lsp_hop_avoid_node
      
  def _set_lsp_hop_avoid_node(self, v, load=False):
    """
    Setter method for lsp_hop_avoid_node, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_debug/output/bypass_lsp/show_mpls_lsp_debug_info/show_mpls_lsp_instances_info/lsp_instances/lsp_cspf_exclude_hops/show_mpls_lsp_hop_list/hop/lsp_hop_avoid_node (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_hop_avoid_node is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_hop_avoid_node() directly.

    YANG Description: Avoid address type is node
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-hop-avoid-node", rest_name="lsp-hop-avoid-node", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_hop_avoid_node must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-avoid-node", rest_name="lsp-hop-avoid-node", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_hop_avoid_node = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_hop_avoid_node(self):
    self.__lsp_hop_avoid_node = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-avoid-node", rest_name="lsp-hop-avoid-node", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_lsp_hop_avoid_local(self):
    """
    Getter method for lsp_hop_avoid_local, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_debug/output/bypass_lsp/show_mpls_lsp_debug_info/show_mpls_lsp_instances_info/lsp_instances/lsp_cspf_exclude_hops/show_mpls_lsp_hop_list/hop/lsp_hop_avoid_local (boolean)

    YANG Description: Avoid address type is local
    """
    return self.__lsp_hop_avoid_local
      
  def _set_lsp_hop_avoid_local(self, v, load=False):
    """
    Setter method for lsp_hop_avoid_local, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_debug/output/bypass_lsp/show_mpls_lsp_debug_info/show_mpls_lsp_instances_info/lsp_instances/lsp_cspf_exclude_hops/show_mpls_lsp_hop_list/hop/lsp_hop_avoid_local (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_hop_avoid_local is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_hop_avoid_local() directly.

    YANG Description: Avoid address type is local
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-hop-avoid-local", rest_name="lsp-hop-avoid-local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_hop_avoid_local must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-avoid-local", rest_name="lsp-hop-avoid-local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_hop_avoid_local = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_hop_avoid_local(self):
    self.__lsp_hop_avoid_local = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-avoid-local", rest_name="lsp-hop-avoid-local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_lsp_hop_avoid_remote(self):
    """
    Getter method for lsp_hop_avoid_remote, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_debug/output/bypass_lsp/show_mpls_lsp_debug_info/show_mpls_lsp_instances_info/lsp_instances/lsp_cspf_exclude_hops/show_mpls_lsp_hop_list/hop/lsp_hop_avoid_remote (boolean)

    YANG Description: Avoid address type is remote
    """
    return self.__lsp_hop_avoid_remote
      
  def _set_lsp_hop_avoid_remote(self, v, load=False):
    """
    Setter method for lsp_hop_avoid_remote, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_debug/output/bypass_lsp/show_mpls_lsp_debug_info/show_mpls_lsp_instances_info/lsp_instances/lsp_cspf_exclude_hops/show_mpls_lsp_hop_list/hop/lsp_hop_avoid_remote (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_hop_avoid_remote is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_hop_avoid_remote() directly.

    YANG Description: Avoid address type is remote
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-hop-avoid-remote", rest_name="lsp-hop-avoid-remote", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_hop_avoid_remote must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-avoid-remote", rest_name="lsp-hop-avoid-remote", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_hop_avoid_remote = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_hop_avoid_remote(self):
    self.__lsp_hop_avoid_remote = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-hop-avoid-remote", rest_name="lsp-hop-avoid-remote", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)

  lsp_hop_address = __builtin__.property(_get_lsp_hop_address, _set_lsp_hop_address)
  lsp_hop_strict_hop = __builtin__.property(_get_lsp_hop_strict_hop, _set_lsp_hop_strict_hop)
  lsp_hop_loose_hop = __builtin__.property(_get_lsp_hop_loose_hop, _set_lsp_hop_loose_hop)
  lsp_hop_is_router_id = __builtin__.property(_get_lsp_hop_is_router_id, _set_lsp_hop_is_router_id)
  lsp_hop_has_protection = __builtin__.property(_get_lsp_hop_has_protection, _set_lsp_hop_has_protection)
  lsp_hop_has_node_protection = __builtin__.property(_get_lsp_hop_has_node_protection, _set_lsp_hop_has_node_protection)
  lsp_hop_has_bandwidth_protection = __builtin__.property(_get_lsp_hop_has_bandwidth_protection, _set_lsp_hop_has_bandwidth_protection)
  lsp_hop_has_protection_in_use = __builtin__.property(_get_lsp_hop_has_protection_in_use, _set_lsp_hop_has_protection_in_use)
  lsp_hop_avoid_node = __builtin__.property(_get_lsp_hop_avoid_node, _set_lsp_hop_avoid_node)
  lsp_hop_avoid_local = __builtin__.property(_get_lsp_hop_avoid_local, _set_lsp_hop_avoid_local)
  lsp_hop_avoid_remote = __builtin__.property(_get_lsp_hop_avoid_remote, _set_lsp_hop_avoid_remote)


  _pyangbind_elements = {'lsp_hop_address': lsp_hop_address, 'lsp_hop_strict_hop': lsp_hop_strict_hop, 'lsp_hop_loose_hop': lsp_hop_loose_hop, 'lsp_hop_is_router_id': lsp_hop_is_router_id, 'lsp_hop_has_protection': lsp_hop_has_protection, 'lsp_hop_has_node_protection': lsp_hop_has_node_protection, 'lsp_hop_has_bandwidth_protection': lsp_hop_has_bandwidth_protection, 'lsp_hop_has_protection_in_use': lsp_hop_has_protection_in_use, 'lsp_hop_avoid_node': lsp_hop_avoid_node, 'lsp_hop_avoid_local': lsp_hop_avoid_local, 'lsp_hop_avoid_remote': lsp_hop_avoid_remote, }


