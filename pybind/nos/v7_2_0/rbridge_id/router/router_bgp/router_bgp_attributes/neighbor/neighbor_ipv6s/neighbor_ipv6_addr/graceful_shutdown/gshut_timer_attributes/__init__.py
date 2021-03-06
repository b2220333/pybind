
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class gshut_timer_attributes(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/router-bgp/router-bgp-attributes/neighbor/neighbor-ipv6s/neighbor-ipv6-addr/graceful-shutdown/gshut-timer-attributes. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__gshut_local_pref','__gshut_community',)

  _yang_name = 'gshut-timer-attributes'
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
    self.__gshut_community = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="gshut-community", rest_name="community", parent=self, choice=(u'ch-gshut-options', u'ca-gshut-timer-attributes'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set community attribute for graceful shutdown', u'alt-name': u'community', u'cli-reset-container': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bgp-gshut-community', is_config=True)
    self.__gshut_local_pref = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="gshut-local-pref", rest_name="local-preference", parent=self, choice=(u'ch-gshut-options', u'ca-gshut-timer-attributes'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set local preference attribute for graceful shutdown', u'alt-name': u'local-preference', u'cli-reset-container': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bgp-gshut-local-pref', is_config=True)

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
      return [u'rbridge-id', u'router', u'router-bgp', u'router-bgp-attributes', u'neighbor', u'neighbor-ipv6s', u'neighbor-ipv6-addr', u'graceful-shutdown', u'gshut-timer-attributes']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'bgp', u'neighbor', u'neighbor-ipv6-addr', u'graceful-shutdown']

  def _get_gshut_local_pref(self):
    """
    Getter method for gshut_local_pref, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s/neighbor_ipv6_addr/graceful_shutdown/gshut_timer_attributes/gshut_local_pref (bgp-gshut-local-pref)
    """
    return self.__gshut_local_pref
      
  def _set_gshut_local_pref(self, v, load=False):
    """
    Setter method for gshut_local_pref, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s/neighbor_ipv6_addr/graceful_shutdown/gshut_timer_attributes/gshut_local_pref (bgp-gshut-local-pref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_gshut_local_pref is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_gshut_local_pref() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="gshut-local-pref", rest_name="local-preference", parent=self, choice=(u'ch-gshut-options', u'ca-gshut-timer-attributes'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set local preference attribute for graceful shutdown', u'alt-name': u'local-preference', u'cli-reset-container': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bgp-gshut-local-pref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """gshut_local_pref must be of a type compatible with bgp-gshut-local-pref""",
          'defined-type': "brocade-bgp:bgp-gshut-local-pref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="gshut-local-pref", rest_name="local-preference", parent=self, choice=(u'ch-gshut-options', u'ca-gshut-timer-attributes'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set local preference attribute for graceful shutdown', u'alt-name': u'local-preference', u'cli-reset-container': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bgp-gshut-local-pref', is_config=True)""",
        })

    self.__gshut_local_pref = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_gshut_local_pref(self):
    self.__gshut_local_pref = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="gshut-local-pref", rest_name="local-preference", parent=self, choice=(u'ch-gshut-options', u'ca-gshut-timer-attributes'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set local preference attribute for graceful shutdown', u'alt-name': u'local-preference', u'cli-reset-container': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bgp-gshut-local-pref', is_config=True)


  def _get_gshut_community(self):
    """
    Getter method for gshut_community, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s/neighbor_ipv6_addr/graceful_shutdown/gshut_timer_attributes/gshut_community (bgp-gshut-community)
    """
    return self.__gshut_community
      
  def _set_gshut_community(self, v, load=False):
    """
    Setter method for gshut_community, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s/neighbor_ipv6_addr/graceful_shutdown/gshut_timer_attributes/gshut_community (bgp-gshut-community)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_gshut_community is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_gshut_community() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="gshut-community", rest_name="community", parent=self, choice=(u'ch-gshut-options', u'ca-gshut-timer-attributes'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set community attribute for graceful shutdown', u'alt-name': u'community', u'cli-reset-container': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bgp-gshut-community', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """gshut_community must be of a type compatible with bgp-gshut-community""",
          'defined-type': "brocade-bgp:bgp-gshut-community",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="gshut-community", rest_name="community", parent=self, choice=(u'ch-gshut-options', u'ca-gshut-timer-attributes'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set community attribute for graceful shutdown', u'alt-name': u'community', u'cli-reset-container': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bgp-gshut-community', is_config=True)""",
        })

    self.__gshut_community = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_gshut_community(self):
    self.__gshut_community = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="gshut-community", rest_name="community", parent=self, choice=(u'ch-gshut-options', u'ca-gshut-timer-attributes'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set community attribute for graceful shutdown', u'alt-name': u'community', u'cli-reset-container': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bgp-gshut-community', is_config=True)

  gshut_local_pref = __builtin__.property(_get_gshut_local_pref, _set_gshut_local_pref)
  gshut_community = __builtin__.property(_get_gshut_community, _set_gshut_community)

  __choices__ = {u'ch-gshut-options': {u'ca-gshut-timer-attributes': [u'gshut_local_pref', u'gshut_community']}}
  _pyangbind_elements = {'gshut_local_pref': gshut_local_pref, 'gshut_community': gshut_community, }


