
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ldp_fec_prefix_nexthop_rec_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-ldp-fec-prefix-prefix-longer/output/ldp-fec-prefix-prefix-longer-rec-list/ldp-fec-prefix-nexthop-rec-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ldp_fec_prefix_nexthop','__ldp_fec_prefix_out_if',)

  _yang_name = 'ldp-fec-prefix-nexthop-rec-list'
  _rest_name = 'ldp-fec-prefix-nexthop-rec-list'

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
    self.__ldp_fec_prefix_nexthop = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="ldp-fec-prefix-nexthop", rest_name="ldp-fec-prefix-nexthop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-prefix', is_config=True)
    self.__ldp_fec_prefix_out_if = YANGDynClass(base=unicode, is_leaf=True, yang_name="ldp-fec-prefix-out-if", rest_name="ldp-fec-prefix-out-if", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-ldp-fec-prefix-prefix-longer', u'output', u'ldp-fec-prefix-prefix-longer-rec-list', u'ldp-fec-prefix-nexthop-rec-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-ldp-fec-prefix-prefix-longer', u'output', u'ldp-fec-prefix-prefix-longer-rec-list', u'ldp-fec-prefix-nexthop-rec-list']

  def _get_ldp_fec_prefix_nexthop(self):
    """
    Getter method for ldp_fec_prefix_nexthop, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_longer/output/ldp_fec_prefix_prefix_longer_rec_list/ldp_fec_prefix_nexthop_rec_list/ldp_fec_prefix_nexthop (inet:ipv4-prefix)

    YANG Description: next_hop
    """
    return self.__ldp_fec_prefix_nexthop
      
  def _set_ldp_fec_prefix_nexthop(self, v, load=False):
    """
    Setter method for ldp_fec_prefix_nexthop, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_longer/output/ldp_fec_prefix_prefix_longer_rec_list/ldp_fec_prefix_nexthop_rec_list/ldp_fec_prefix_nexthop (inet:ipv4-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_prefix_nexthop is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_prefix_nexthop() directly.

    YANG Description: next_hop
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="ldp-fec-prefix-nexthop", rest_name="ldp-fec-prefix-nexthop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_prefix_nexthop must be of a type compatible with inet:ipv4-prefix""",
          'defined-type': "inet:ipv4-prefix",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="ldp-fec-prefix-nexthop", rest_name="ldp-fec-prefix-nexthop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-prefix', is_config=True)""",
        })

    self.__ldp_fec_prefix_nexthop = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_prefix_nexthop(self):
    self.__ldp_fec_prefix_nexthop = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="ldp-fec-prefix-nexthop", rest_name="ldp-fec-prefix-nexthop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-prefix', is_config=True)


  def _get_ldp_fec_prefix_out_if(self):
    """
    Getter method for ldp_fec_prefix_out_if, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_longer/output/ldp_fec_prefix_prefix_longer_rec_list/ldp_fec_prefix_nexthop_rec_list/ldp_fec_prefix_out_if (string)

    YANG Description: out_if
    """
    return self.__ldp_fec_prefix_out_if
      
  def _set_ldp_fec_prefix_out_if(self, v, load=False):
    """
    Setter method for ldp_fec_prefix_out_if, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_longer/output/ldp_fec_prefix_prefix_longer_rec_list/ldp_fec_prefix_nexthop_rec_list/ldp_fec_prefix_out_if (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_prefix_out_if is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_prefix_out_if() directly.

    YANG Description: out_if
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="ldp-fec-prefix-out-if", rest_name="ldp-fec-prefix-out-if", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_prefix_out_if must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="ldp-fec-prefix-out-if", rest_name="ldp-fec-prefix-out-if", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__ldp_fec_prefix_out_if = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_prefix_out_if(self):
    self.__ldp_fec_prefix_out_if = YANGDynClass(base=unicode, is_leaf=True, yang_name="ldp-fec-prefix-out-if", rest_name="ldp-fec-prefix-out-if", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)

  ldp_fec_prefix_nexthop = __builtin__.property(_get_ldp_fec_prefix_nexthop, _set_ldp_fec_prefix_nexthop)
  ldp_fec_prefix_out_if = __builtin__.property(_get_ldp_fec_prefix_out_if, _set_ldp_fec_prefix_out_if)


  _pyangbind_elements = {'ldp_fec_prefix_nexthop': ldp_fec_prefix_nexthop, 'ldp_fec_prefix_out_if': ldp_fec_prefix_out_if, }


