
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ldp_tunnels
class tunnels(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/ldp/tunnels. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: LDP Tunnels
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__total_tunnel_count','__ldp_tunnels',)

  _yang_name = 'tunnels'
  _rest_name = 'tunnels'

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
    self.__total_tunnel_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-tunnel-count", rest_name="total-tunnel-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__ldp_tunnels = YANGDynClass(base=YANGListType("tunnel_destination prefix_length",ldp_tunnels.ldp_tunnels, yang_name="ldp-tunnels", rest_name="ldp-tunnels", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='tunnel-destination prefix-length', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-tunnel', u'cli-suppress-show-path': None}}), is_container='list', yang_name="ldp-tunnels", rest_name="ldp-tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-tunnel', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)

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
      return [u'mpls-state', u'ldp', u'tunnels']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'ldp', u'tunnels']

  def _get_total_tunnel_count(self):
    """
    Getter method for total_tunnel_count, mapped from YANG variable /mpls_state/ldp/tunnels/total_tunnel_count (uint32)

    YANG Description: total tunnel count
    """
    return self.__total_tunnel_count
      
  def _set_total_tunnel_count(self, v, load=False):
    """
    Setter method for total_tunnel_count, mapped from YANG variable /mpls_state/ldp/tunnels/total_tunnel_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_total_tunnel_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_total_tunnel_count() directly.

    YANG Description: total tunnel count
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-tunnel-count", rest_name="total-tunnel-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """total_tunnel_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-tunnel-count", rest_name="total-tunnel-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__total_tunnel_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_total_tunnel_count(self):
    self.__total_tunnel_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-tunnel-count", rest_name="total-tunnel-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_ldp_tunnels(self):
    """
    Getter method for ldp_tunnels, mapped from YANG variable /mpls_state/ldp/tunnels/ldp_tunnels (list)

    YANG Description: ldp tunnel
    """
    return self.__ldp_tunnels
      
  def _set_ldp_tunnels(self, v, load=False):
    """
    Setter method for ldp_tunnels, mapped from YANG variable /mpls_state/ldp/tunnels/ldp_tunnels (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_tunnels is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_tunnels() directly.

    YANG Description: ldp tunnel
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("tunnel_destination prefix_length",ldp_tunnels.ldp_tunnels, yang_name="ldp-tunnels", rest_name="ldp-tunnels", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='tunnel-destination prefix-length', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-tunnel', u'cli-suppress-show-path': None}}), is_container='list', yang_name="ldp-tunnels", rest_name="ldp-tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-tunnel', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_tunnels must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("tunnel_destination prefix_length",ldp_tunnels.ldp_tunnels, yang_name="ldp-tunnels", rest_name="ldp-tunnels", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='tunnel-destination prefix-length', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-tunnel', u'cli-suppress-show-path': None}}), is_container='list', yang_name="ldp-tunnels", rest_name="ldp-tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-tunnel', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)""",
        })

    self.__ldp_tunnels = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_tunnels(self):
    self.__ldp_tunnels = YANGDynClass(base=YANGListType("tunnel_destination prefix_length",ldp_tunnels.ldp_tunnels, yang_name="ldp-tunnels", rest_name="ldp-tunnels", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='tunnel-destination prefix-length', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-tunnel', u'cli-suppress-show-path': None}}), is_container='list', yang_name="ldp-tunnels", rest_name="ldp-tunnels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-tunnel', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)

  total_tunnel_count = __builtin__.property(_get_total_tunnel_count)
  ldp_tunnels = __builtin__.property(_get_ldp_tunnels)


  _pyangbind_elements = {'total_tunnel_count': total_tunnel_count, 'ldp_tunnels': ldp_tunnels, }


