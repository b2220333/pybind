
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class next_hop_mpls(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/ipv4/ipv4-unicast/default-vrf/next-hop-mpls. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__compare_lsp_metric','__follow_igp',)

  _yang_name = 'next-hop-mpls'
  _rest_name = 'next-hop-mpls'

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
    self.__follow_igp = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="follow-igp", rest_name="follow-igp", parent=self, choice=(u'ch-compare-lsp-follow-igp', u'ca-follow-igp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Use IGP metric and ignore LSP metric'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__compare_lsp_metric = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="compare-lsp-metric", rest_name="compare-lsp-metric", parent=self, choice=(u'ch-compare-lsp-follow-igp', u'ca-compare-lsp-metric'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Compare metric value among LSP ECMP paths'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv4', u'ipv4-unicast', u'default-vrf', u'next-hop-mpls']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'address-family', u'ipv4', u'unicast', u'next-hop-mpls']

  def _get_compare_lsp_metric(self):
    """
    Getter method for compare_lsp_metric, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/next_hop_mpls/compare_lsp_metric (empty)
    """
    return self.__compare_lsp_metric
      
  def _set_compare_lsp_metric(self, v, load=False):
    """
    Setter method for compare_lsp_metric, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/next_hop_mpls/compare_lsp_metric (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_compare_lsp_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_compare_lsp_metric() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="compare-lsp-metric", rest_name="compare-lsp-metric", parent=self, choice=(u'ch-compare-lsp-follow-igp', u'ca-compare-lsp-metric'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Compare metric value among LSP ECMP paths'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """compare_lsp_metric must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="compare-lsp-metric", rest_name="compare-lsp-metric", parent=self, choice=(u'ch-compare-lsp-follow-igp', u'ca-compare-lsp-metric'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Compare metric value among LSP ECMP paths'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__compare_lsp_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_compare_lsp_metric(self):
    self.__compare_lsp_metric = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="compare-lsp-metric", rest_name="compare-lsp-metric", parent=self, choice=(u'ch-compare-lsp-follow-igp', u'ca-compare-lsp-metric'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Compare metric value among LSP ECMP paths'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_follow_igp(self):
    """
    Getter method for follow_igp, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/next_hop_mpls/follow_igp (empty)
    """
    return self.__follow_igp
      
  def _set_follow_igp(self, v, load=False):
    """
    Setter method for follow_igp, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/next_hop_mpls/follow_igp (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_follow_igp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_follow_igp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="follow-igp", rest_name="follow-igp", parent=self, choice=(u'ch-compare-lsp-follow-igp', u'ca-follow-igp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Use IGP metric and ignore LSP metric'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """follow_igp must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="follow-igp", rest_name="follow-igp", parent=self, choice=(u'ch-compare-lsp-follow-igp', u'ca-follow-igp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Use IGP metric and ignore LSP metric'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__follow_igp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_follow_igp(self):
    self.__follow_igp = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="follow-igp", rest_name="follow-igp", parent=self, choice=(u'ch-compare-lsp-follow-igp', u'ca-follow-igp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Use IGP metric and ignore LSP metric'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

  compare_lsp_metric = __builtin__.property(_get_compare_lsp_metric, _set_compare_lsp_metric)
  follow_igp = __builtin__.property(_get_follow_igp, _set_follow_igp)

  __choices__ = {u'ch-compare-lsp-follow-igp': {u'ca-compare-lsp-metric': [u'compare_lsp_metric'], u'ca-follow-igp': [u'follow_igp']}}
  _pyangbind_elements = {'compare_lsp_metric': compare_lsp_metric, 'follow_igp': follow_igp, }


