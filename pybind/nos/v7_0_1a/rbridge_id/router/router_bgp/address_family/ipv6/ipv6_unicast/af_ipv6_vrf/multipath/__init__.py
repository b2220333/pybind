
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class multipath(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/router-bgp/address-family/ipv6/ipv6-unicast/af-ipv6-vrf/multipath. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__multipath_ebgp','__multipath_ibgp','__multi_as',)

  _yang_name = 'multipath'
  _rest_name = 'multipath'

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
    self.__multipath_ebgp = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="multipath_ebgp", rest_name="ebgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow multipath for ebgp neighbors only', u'cli-full-command': None, u'alt-name': u'ebgp'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__multi_as = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="multi-as", rest_name="multi-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable multipath over different Neighboring AS', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__multipath_ibgp = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="multipath_ibgp", rest_name="ibgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow multipath for ibgp neighbors only', u'cli-full-command': None, u'alt-name': u'ibgp'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

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
      return [u'rbridge-id', u'router', u'router-bgp', u'address-family', u'ipv6', u'ipv6-unicast', u'af-ipv6-vrf', u'multipath']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'bgp', u'address-family', u'ipv6', u'unicast', u'vrf', u'multipath']

  def _get_multipath_ebgp(self):
    """
    Getter method for multipath_ebgp, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/multipath/multipath_ebgp (empty)
    """
    return self.__multipath_ebgp
      
  def _set_multipath_ebgp(self, v, load=False):
    """
    Setter method for multipath_ebgp, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/multipath/multipath_ebgp (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_multipath_ebgp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_multipath_ebgp() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="multipath_ebgp", rest_name="ebgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow multipath for ebgp neighbors only', u'cli-full-command': None, u'alt-name': u'ebgp'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """multipath_ebgp must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="multipath_ebgp", rest_name="ebgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow multipath for ebgp neighbors only', u'cli-full-command': None, u'alt-name': u'ebgp'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__multipath_ebgp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_multipath_ebgp(self):
    self.__multipath_ebgp = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="multipath_ebgp", rest_name="ebgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow multipath for ebgp neighbors only', u'cli-full-command': None, u'alt-name': u'ebgp'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_multipath_ibgp(self):
    """
    Getter method for multipath_ibgp, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/multipath/multipath_ibgp (empty)
    """
    return self.__multipath_ibgp
      
  def _set_multipath_ibgp(self, v, load=False):
    """
    Setter method for multipath_ibgp, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/multipath/multipath_ibgp (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_multipath_ibgp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_multipath_ibgp() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="multipath_ibgp", rest_name="ibgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow multipath for ibgp neighbors only', u'cli-full-command': None, u'alt-name': u'ibgp'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """multipath_ibgp must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="multipath_ibgp", rest_name="ibgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow multipath for ibgp neighbors only', u'cli-full-command': None, u'alt-name': u'ibgp'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__multipath_ibgp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_multipath_ibgp(self):
    self.__multipath_ibgp = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="multipath_ibgp", rest_name="ibgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow multipath for ibgp neighbors only', u'cli-full-command': None, u'alt-name': u'ibgp'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_multi_as(self):
    """
    Getter method for multi_as, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/multipath/multi_as (empty)
    """
    return self.__multi_as
      
  def _set_multi_as(self, v, load=False):
    """
    Setter method for multi_as, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/multipath/multi_as (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_multi_as is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_multi_as() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="multi-as", rest_name="multi-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable multipath over different Neighboring AS', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """multi_as must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="multi-as", rest_name="multi-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable multipath over different Neighboring AS', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__multi_as = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_multi_as(self):
    self.__multi_as = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="multi-as", rest_name="multi-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable multipath over different Neighboring AS', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

  multipath_ebgp = __builtin__.property(_get_multipath_ebgp, _set_multipath_ebgp)
  multipath_ibgp = __builtin__.property(_get_multipath_ibgp, _set_multipath_ibgp)
  multi_as = __builtin__.property(_get_multi_as, _set_multi_as)


  _pyangbind_elements = {'multipath_ebgp': multipath_ebgp, 'multipath_ibgp': multipath_ibgp, 'multi_as': multi_as, }


