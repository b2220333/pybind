
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class input(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-statistics-ldp-transit/input. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ldp_transit_stats','__ldp_transit_stats_fec_prefix','__ldp_transit_stats_fec_prefix_longer',)

  _yang_name = 'input'
  _rest_name = 'input'

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
    self.__ldp_transit_stats = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ldp-transit-stats", rest_name="ldp-transit-stats", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__ldp_transit_stats_fec_prefix = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-transit-stats-fec-prefix", rest_name="ldp-transit-stats-fec-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    self.__ldp_transit_stats_fec_prefix_longer = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ldp-transit-stats-fec-prefix-longer", rest_name="ldp-transit-stats-fec-prefix-longer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-statistics-ldp-transit', u'input']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-statistics-ldp-transit', u'input']

  def _get_ldp_transit_stats(self):
    """
    Getter method for ldp_transit_stats, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_ldp_transit/input/ldp_transit_stats (boolean)

    YANG Description: Ldp Transit FEC stats
    """
    return self.__ldp_transit_stats
      
  def _set_ldp_transit_stats(self, v, load=False):
    """
    Setter method for ldp_transit_stats, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_ldp_transit/input/ldp_transit_stats (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_transit_stats is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_transit_stats() directly.

    YANG Description: Ldp Transit FEC stats
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ldp-transit-stats", rest_name="ldp-transit-stats", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_transit_stats must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ldp-transit-stats", rest_name="ldp-transit-stats", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__ldp_transit_stats = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_transit_stats(self):
    self.__ldp_transit_stats = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ldp-transit-stats", rest_name="ldp-transit-stats", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_ldp_transit_stats_fec_prefix(self):
    """
    Getter method for ldp_transit_stats_fec_prefix, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_ldp_transit/input/ldp_transit_stats_fec_prefix (inet:ipv4-address)

    YANG Description: IP address/Subnet mask length
    """
    return self.__ldp_transit_stats_fec_prefix
      
  def _set_ldp_transit_stats_fec_prefix(self, v, load=False):
    """
    Setter method for ldp_transit_stats_fec_prefix, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_ldp_transit/input/ldp_transit_stats_fec_prefix (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_transit_stats_fec_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_transit_stats_fec_prefix() directly.

    YANG Description: IP address/Subnet mask length
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-transit-stats-fec-prefix", rest_name="ldp-transit-stats-fec-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_transit_stats_fec_prefix must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-transit-stats-fec-prefix", rest_name="ldp-transit-stats-fec-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__ldp_transit_stats_fec_prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_transit_stats_fec_prefix(self):
    self.__ldp_transit_stats_fec_prefix = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-transit-stats-fec-prefix", rest_name="ldp-transit-stats-fec-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)


  def _get_ldp_transit_stats_fec_prefix_longer(self):
    """
    Getter method for ldp_transit_stats_fec_prefix_longer, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_ldp_transit/input/ldp_transit_stats_fec_prefix_longer (boolean)

    YANG Description: Display all matching and more specific FECs traffic statistics
    """
    return self.__ldp_transit_stats_fec_prefix_longer
      
  def _set_ldp_transit_stats_fec_prefix_longer(self, v, load=False):
    """
    Setter method for ldp_transit_stats_fec_prefix_longer, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_ldp_transit/input/ldp_transit_stats_fec_prefix_longer (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_transit_stats_fec_prefix_longer is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_transit_stats_fec_prefix_longer() directly.

    YANG Description: Display all matching and more specific FECs traffic statistics
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ldp-transit-stats-fec-prefix-longer", rest_name="ldp-transit-stats-fec-prefix-longer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_transit_stats_fec_prefix_longer must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ldp-transit-stats-fec-prefix-longer", rest_name="ldp-transit-stats-fec-prefix-longer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__ldp_transit_stats_fec_prefix_longer = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_transit_stats_fec_prefix_longer(self):
    self.__ldp_transit_stats_fec_prefix_longer = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ldp-transit-stats-fec-prefix-longer", rest_name="ldp-transit-stats-fec-prefix-longer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)

  ldp_transit_stats = __builtin__.property(_get_ldp_transit_stats, _set_ldp_transit_stats)
  ldp_transit_stats_fec_prefix = __builtin__.property(_get_ldp_transit_stats_fec_prefix, _set_ldp_transit_stats_fec_prefix)
  ldp_transit_stats_fec_prefix_longer = __builtin__.property(_get_ldp_transit_stats_fec_prefix_longer, _set_ldp_transit_stats_fec_prefix_longer)


  _pyangbind_elements = {'ldp_transit_stats': ldp_transit_stats, 'ldp_transit_stats_fec_prefix': ldp_transit_stats_fec_prefix, 'ldp_transit_stats_fec_prefix_longer': ldp_transit_stats_fec_prefix_longer, }


