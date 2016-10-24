
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class vc(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/ldp/fec/ldp-fec-vcs/vc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: 
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__peer_id','__peer_lblspc','__state','__vc_id','__peer_vc_type','__peer_fec_type','__ingress','__egress',)

  _yang_name = 'vc'
  _rest_name = 'vc'

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
    self.__ingress = YANGDynClass(base=unicode, is_leaf=True, yang_name="ingress", rest_name="ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    self.__peer_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="peer-id", rest_name="peer-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__state = YANGDynClass(base=unicode, is_leaf=True, yang_name="state", rest_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    self.__peer_lblspc = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peer-lblspc", rest_name="peer-lblspc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__egress = YANGDynClass(base=unicode, is_leaf=True, yang_name="egress", rest_name="egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    self.__vc_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vc-id", rest_name="vc-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__peer_vc_type = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peer-vc-type", rest_name="peer-vc-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__peer_fec_type = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peer-fec-type", rest_name="peer-fec-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)

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
      return [u'mpls-state', u'ldp', u'fec', u'ldp-fec-vcs', u'vc']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'ldp', u'fec', u'ldp-fec-vcs', u'vc']

  def _get_peer_id(self):
    """
    Getter method for peer_id, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_vcs/vc/peer_id (inet:ipv4-address)

    YANG Description: peer_id
    """
    return self.__peer_id
      
  def _set_peer_id(self, v, load=False):
    """
    Setter method for peer_id, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_vcs/vc/peer_id (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_id() directly.

    YANG Description: peer_id
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="peer-id", rest_name="peer-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_id must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="peer-id", rest_name="peer-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__peer_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_id(self):
    self.__peer_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="peer-id", rest_name="peer-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_peer_lblspc(self):
    """
    Getter method for peer_lblspc, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_vcs/vc/peer_lblspc (uint32)

    YANG Description: peer_lblspc
    """
    return self.__peer_lblspc
      
  def _set_peer_lblspc(self, v, load=False):
    """
    Setter method for peer_lblspc, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_vcs/vc/peer_lblspc (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_lblspc is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_lblspc() directly.

    YANG Description: peer_lblspc
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peer-lblspc", rest_name="peer-lblspc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_lblspc must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peer-lblspc", rest_name="peer-lblspc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__peer_lblspc = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_lblspc(self):
    self.__peer_lblspc = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peer-lblspc", rest_name="peer-lblspc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_vcs/vc/state (string)

    YANG Description: state
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_vcs/vc/state (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: state
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="state", rest_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="state", rest_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=unicode, is_leaf=True, yang_name="state", rest_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)


  def _get_vc_id(self):
    """
    Getter method for vc_id, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_vcs/vc/vc_id (uint32)

    YANG Description: vc_id
    """
    return self.__vc_id
      
  def _set_vc_id(self, v, load=False):
    """
    Setter method for vc_id, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_vcs/vc/vc_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vc_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vc_id() directly.

    YANG Description: vc_id
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vc-id", rest_name="vc-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vc_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vc-id", rest_name="vc-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__vc_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vc_id(self):
    self.__vc_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vc-id", rest_name="vc-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_peer_vc_type(self):
    """
    Getter method for peer_vc_type, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_vcs/vc/peer_vc_type (uint32)

    YANG Description: peer_vc_type
    """
    return self.__peer_vc_type
      
  def _set_peer_vc_type(self, v, load=False):
    """
    Setter method for peer_vc_type, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_vcs/vc/peer_vc_type (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_vc_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_vc_type() directly.

    YANG Description: peer_vc_type
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peer-vc-type", rest_name="peer-vc-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_vc_type must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peer-vc-type", rest_name="peer-vc-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__peer_vc_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_vc_type(self):
    self.__peer_vc_type = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peer-vc-type", rest_name="peer-vc-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_peer_fec_type(self):
    """
    Getter method for peer_fec_type, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_vcs/vc/peer_fec_type (uint32)

    YANG Description: peer_fec_type
    """
    return self.__peer_fec_type
      
  def _set_peer_fec_type(self, v, load=False):
    """
    Setter method for peer_fec_type, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_vcs/vc/peer_fec_type (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_fec_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_fec_type() directly.

    YANG Description: peer_fec_type
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peer-fec-type", rest_name="peer-fec-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_fec_type must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peer-fec-type", rest_name="peer-fec-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__peer_fec_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_fec_type(self):
    self.__peer_fec_type = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peer-fec-type", rest_name="peer-fec-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_ingress(self):
    """
    Getter method for ingress, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_vcs/vc/ingress (string)

    YANG Description: ingress
    """
    return self.__ingress
      
  def _set_ingress(self, v, load=False):
    """
    Setter method for ingress, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_vcs/vc/ingress (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ingress is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ingress() directly.

    YANG Description: ingress
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="ingress", rest_name="ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ingress must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="ingress", rest_name="ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)""",
        })

    self.__ingress = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ingress(self):
    self.__ingress = YANGDynClass(base=unicode, is_leaf=True, yang_name="ingress", rest_name="ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)


  def _get_egress(self):
    """
    Getter method for egress, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_vcs/vc/egress (string)

    YANG Description: egress
    """
    return self.__egress
      
  def _set_egress(self, v, load=False):
    """
    Setter method for egress, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_vcs/vc/egress (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_egress is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_egress() directly.

    YANG Description: egress
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="egress", rest_name="egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """egress must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="egress", rest_name="egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)""",
        })

    self.__egress = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_egress(self):
    self.__egress = YANGDynClass(base=unicode, is_leaf=True, yang_name="egress", rest_name="egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)

  peer_id = __builtin__.property(_get_peer_id)
  peer_lblspc = __builtin__.property(_get_peer_lblspc)
  state = __builtin__.property(_get_state)
  vc_id = __builtin__.property(_get_vc_id)
  peer_vc_type = __builtin__.property(_get_peer_vc_type)
  peer_fec_type = __builtin__.property(_get_peer_fec_type)
  ingress = __builtin__.property(_get_ingress)
  egress = __builtin__.property(_get_egress)


  _pyangbind_elements = {'peer_id': peer_id, 'peer_lblspc': peer_lblspc, 'state': state, 'vc_id': vc_id, 'peer_vc_type': peer_vc_type, 'peer_fec_type': peer_fec_type, 'ingress': ingress, 'egress': egress, }


