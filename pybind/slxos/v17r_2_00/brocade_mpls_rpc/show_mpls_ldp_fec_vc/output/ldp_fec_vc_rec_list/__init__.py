
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ldp_fec_vc_rec_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-ldp-fec-vc/output/ldp-fec-vc-rec-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ldp_fec_peer_id','__ldp_fec_peer_lblspc','__ldp_fec_state','__ldp_fec_vc_id','__ldp_fec_peer_vc_type','__ldp_fec_peer_fec_type','__ldp_fec_ingress','__ldp_fec_egress',)

  _yang_name = 'ldp-fec-vc-rec-list'
  _rest_name = 'ldp-fec-vc-rec-list'

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
    self.__ldp_fec_state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'current': {'value': 16384}, u'unknown': {'value': 0}, u'retained': {'value': 49152}, u'down': {'value': 32768}},), is_leaf=True, yang_name="ldp-fec-state", rest_name="ldp-fec-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='ldp-fec-state', is_config=True)
    self.__ldp_fec_vc_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-vc-id", rest_name="ldp-fec-vc-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__ldp_fec_peer_fec_type = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-peer-fec-type", rest_name="ldp-fec-peer-fec-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__ldp_fec_peer_vc_type = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-peer-vc-type", rest_name="ldp-fec-peer-vc-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__ldp_fec_ingress = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-fec-ingress", rest_name="ldp-fec-ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)
    self.__ldp_fec_egress = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-fec-egress", rest_name="ldp-fec-egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)
    self.__ldp_fec_peer_lblspc = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-peer-lblspc", rest_name="ldp-fec-peer-lblspc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__ldp_fec_peer_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-fec-peer-id", rest_name="ldp-fec-peer-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-ldp-fec-vc', u'output', u'ldp-fec-vc-rec-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-ldp-fec-vc', u'output', u'ldp-fec-vc-rec-list']

  def _get_ldp_fec_peer_id(self):
    """
    Getter method for ldp_fec_peer_id, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc/output/ldp_fec_vc_rec_list/ldp_fec_peer_id (inet:ipv4-address)

    YANG Description: Peer LDP ID
    """
    return self.__ldp_fec_peer_id
      
  def _set_ldp_fec_peer_id(self, v, load=False):
    """
    Setter method for ldp_fec_peer_id, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc/output/ldp_fec_vc_rec_list/ldp_fec_peer_id (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_peer_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_peer_id() directly.

    YANG Description: Peer LDP ID
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-fec-peer-id", rest_name="ldp-fec-peer-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_peer_id must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-fec-peer-id", rest_name="ldp-fec-peer-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__ldp_fec_peer_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_peer_id(self):
    self.__ldp_fec_peer_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-fec-peer-id", rest_name="ldp-fec-peer-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)


  def _get_ldp_fec_peer_lblspc(self):
    """
    Getter method for ldp_fec_peer_lblspc, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc/output/ldp_fec_vc_rec_list/ldp_fec_peer_lblspc (uint32)

    YANG Description: Peer Label Space
    """
    return self.__ldp_fec_peer_lblspc
      
  def _set_ldp_fec_peer_lblspc(self, v, load=False):
    """
    Setter method for ldp_fec_peer_lblspc, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc/output/ldp_fec_vc_rec_list/ldp_fec_peer_lblspc (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_peer_lblspc is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_peer_lblspc() directly.

    YANG Description: Peer Label Space
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-peer-lblspc", rest_name="ldp-fec-peer-lblspc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_peer_lblspc must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-peer-lblspc", rest_name="ldp-fec-peer-lblspc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__ldp_fec_peer_lblspc = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_peer_lblspc(self):
    self.__ldp_fec_peer_lblspc = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-peer-lblspc", rest_name="ldp-fec-peer-lblspc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_ldp_fec_state(self):
    """
    Getter method for ldp_fec_state, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc/output/ldp_fec_vc_rec_list/ldp_fec_state (ldp-fec-state)

    YANG Description: State
    """
    return self.__ldp_fec_state
      
  def _set_ldp_fec_state(self, v, load=False):
    """
    Setter method for ldp_fec_state, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc/output/ldp_fec_vc_rec_list/ldp_fec_state (ldp-fec-state)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_state() directly.

    YANG Description: State
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'current': {'value': 16384}, u'unknown': {'value': 0}, u'retained': {'value': 49152}, u'down': {'value': 32768}},), is_leaf=True, yang_name="ldp-fec-state", rest_name="ldp-fec-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='ldp-fec-state', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_state must be of a type compatible with ldp-fec-state""",
          'defined-type': "brocade-mpls:ldp-fec-state",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'current': {'value': 16384}, u'unknown': {'value': 0}, u'retained': {'value': 49152}, u'down': {'value': 32768}},), is_leaf=True, yang_name="ldp-fec-state", rest_name="ldp-fec-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='ldp-fec-state', is_config=True)""",
        })

    self.__ldp_fec_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_state(self):
    self.__ldp_fec_state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'current': {'value': 16384}, u'unknown': {'value': 0}, u'retained': {'value': 49152}, u'down': {'value': 32768}},), is_leaf=True, yang_name="ldp-fec-state", rest_name="ldp-fec-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='ldp-fec-state', is_config=True)


  def _get_ldp_fec_vc_id(self):
    """
    Getter method for ldp_fec_vc_id, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc/output/ldp_fec_vc_rec_list/ldp_fec_vc_id (uint32)

    YANG Description: VC-ID
    """
    return self.__ldp_fec_vc_id
      
  def _set_ldp_fec_vc_id(self, v, load=False):
    """
    Setter method for ldp_fec_vc_id, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc/output/ldp_fec_vc_rec_list/ldp_fec_vc_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_vc_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_vc_id() directly.

    YANG Description: VC-ID
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-vc-id", rest_name="ldp-fec-vc-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_vc_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-vc-id", rest_name="ldp-fec-vc-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__ldp_fec_vc_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_vc_id(self):
    self.__ldp_fec_vc_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-vc-id", rest_name="ldp-fec-vc-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_ldp_fec_peer_vc_type(self):
    """
    Getter method for ldp_fec_peer_vc_type, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc/output/ldp_fec_vc_rec_list/ldp_fec_peer_vc_type (uint32)

    YANG Description: VC-Type
    """
    return self.__ldp_fec_peer_vc_type
      
  def _set_ldp_fec_peer_vc_type(self, v, load=False):
    """
    Setter method for ldp_fec_peer_vc_type, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc/output/ldp_fec_vc_rec_list/ldp_fec_peer_vc_type (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_peer_vc_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_peer_vc_type() directly.

    YANG Description: VC-Type
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-peer-vc-type", rest_name="ldp-fec-peer-vc-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_peer_vc_type must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-peer-vc-type", rest_name="ldp-fec-peer-vc-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__ldp_fec_peer_vc_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_peer_vc_type(self):
    self.__ldp_fec_peer_vc_type = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-peer-vc-type", rest_name="ldp-fec-peer-vc-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_ldp_fec_peer_fec_type(self):
    """
    Getter method for ldp_fec_peer_fec_type, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc/output/ldp_fec_vc_rec_list/ldp_fec_peer_fec_type (uint32)

    YANG Description: FEC-Type
    """
    return self.__ldp_fec_peer_fec_type
      
  def _set_ldp_fec_peer_fec_type(self, v, load=False):
    """
    Setter method for ldp_fec_peer_fec_type, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc/output/ldp_fec_vc_rec_list/ldp_fec_peer_fec_type (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_peer_fec_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_peer_fec_type() directly.

    YANG Description: FEC-Type
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-peer-fec-type", rest_name="ldp-fec-peer-fec-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_peer_fec_type must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-peer-fec-type", rest_name="ldp-fec-peer-fec-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__ldp_fec_peer_fec_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_peer_fec_type(self):
    self.__ldp_fec_peer_fec_type = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-fec-peer-fec-type", rest_name="ldp-fec-peer-fec-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_ldp_fec_ingress(self):
    """
    Getter method for ldp_fec_ingress, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc/output/ldp_fec_vc_rec_list/ldp_fec_ingress (yes-no)

    YANG Description: Ingress
    """
    return self.__ldp_fec_ingress
      
  def _set_ldp_fec_ingress(self, v, load=False):
    """
    Setter method for ldp_fec_ingress, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc/output/ldp_fec_vc_rec_list/ldp_fec_ingress (yes-no)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_ingress is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_ingress() directly.

    YANG Description: Ingress
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-fec-ingress", rest_name="ldp-fec-ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_ingress must be of a type compatible with yes-no""",
          'defined-type': "brocade-mpls:yes-no",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-fec-ingress", rest_name="ldp-fec-ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)""",
        })

    self.__ldp_fec_ingress = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_ingress(self):
    self.__ldp_fec_ingress = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-fec-ingress", rest_name="ldp-fec-ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)


  def _get_ldp_fec_egress(self):
    """
    Getter method for ldp_fec_egress, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc/output/ldp_fec_vc_rec_list/ldp_fec_egress (yes-no)

    YANG Description: Egress
    """
    return self.__ldp_fec_egress
      
  def _set_ldp_fec_egress(self, v, load=False):
    """
    Setter method for ldp_fec_egress, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_vc/output/ldp_fec_vc_rec_list/ldp_fec_egress (yes-no)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_egress is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_egress() directly.

    YANG Description: Egress
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-fec-egress", rest_name="ldp-fec-egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_egress must be of a type compatible with yes-no""",
          'defined-type': "brocade-mpls:yes-no",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-fec-egress", rest_name="ldp-fec-egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)""",
        })

    self.__ldp_fec_egress = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_egress(self):
    self.__ldp_fec_egress = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'yes': {'value': 1}, u'no': {'value': 0}},), is_leaf=True, yang_name="ldp-fec-egress", rest_name="ldp-fec-egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='yes-no', is_config=True)

  ldp_fec_peer_id = __builtin__.property(_get_ldp_fec_peer_id, _set_ldp_fec_peer_id)
  ldp_fec_peer_lblspc = __builtin__.property(_get_ldp_fec_peer_lblspc, _set_ldp_fec_peer_lblspc)
  ldp_fec_state = __builtin__.property(_get_ldp_fec_state, _set_ldp_fec_state)
  ldp_fec_vc_id = __builtin__.property(_get_ldp_fec_vc_id, _set_ldp_fec_vc_id)
  ldp_fec_peer_vc_type = __builtin__.property(_get_ldp_fec_peer_vc_type, _set_ldp_fec_peer_vc_type)
  ldp_fec_peer_fec_type = __builtin__.property(_get_ldp_fec_peer_fec_type, _set_ldp_fec_peer_fec_type)
  ldp_fec_ingress = __builtin__.property(_get_ldp_fec_ingress, _set_ldp_fec_ingress)
  ldp_fec_egress = __builtin__.property(_get_ldp_fec_egress, _set_ldp_fec_egress)


  _pyangbind_elements = {'ldp_fec_peer_id': ldp_fec_peer_id, 'ldp_fec_peer_lblspc': ldp_fec_peer_lblspc, 'ldp_fec_state': ldp_fec_state, 'ldp_fec_vc_id': ldp_fec_vc_id, 'ldp_fec_peer_vc_type': ldp_fec_peer_vc_type, 'ldp_fec_peer_fec_type': ldp_fec_peer_fec_type, 'ldp_fec_ingress': ldp_fec_ingress, 'ldp_fec_egress': ldp_fec_egress, }


