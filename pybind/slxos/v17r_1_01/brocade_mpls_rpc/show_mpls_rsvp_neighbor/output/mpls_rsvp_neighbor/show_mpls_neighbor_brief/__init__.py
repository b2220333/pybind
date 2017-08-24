
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class show_mpls_neighbor_brief(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-rsvp-neighbor/output/mpls-rsvp-neighbor/show-mpls-neighbor-brief. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mpls_rsvp_neighbor_ip_addr','__mpls_rsvp_neighbor_interface','__mpls_rsvp_neighbor_status','__mpls_rsvp_neighbor_last_status_change','__mpls_rsvp_neighbor_hello_tx','__mpls_rsvp_neighbor_hello_rx','__mpls_rsvp_neighbor_refresh_reduction_support','__mpls_rsvp_neighbor_msg_id_support',)

  _yang_name = 'show-mpls-neighbor-brief'
  _rest_name = 'show-mpls-neighbor-brief'

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
    self.__mpls_rsvp_neighbor_interface = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-rsvp-neighbor-interface", rest_name="mpls-rsvp-neighbor-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__mpls_rsvp_neighbor_status = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-rsvp-neighbor-status", rest_name="mpls-rsvp-neighbor-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__mpls_rsvp_neighbor_msg_id_support = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-rsvp-neighbor-msg-id-support", rest_name="mpls-rsvp-neighbor-msg-id-support", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__mpls_rsvp_neighbor_last_status_change = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-rsvp-neighbor-last-status-change", rest_name="mpls-rsvp-neighbor-last-status-change", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__mpls_rsvp_neighbor_hello_rx = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-hello-rx", rest_name="mpls-rsvp-neighbor-hello-rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__mpls_rsvp_neighbor_ip_addr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mpls_rsvp_neighbor_ip_addr", rest_name="mpls_rsvp_neighbor_ip_addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    self.__mpls_rsvp_neighbor_hello_tx = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-hello-tx", rest_name="mpls-rsvp-neighbor-hello-tx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__mpls_rsvp_neighbor_refresh_reduction_support = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-rsvp-neighbor-refresh-reduction-support", rest_name="mpls-rsvp-neighbor-refresh-reduction-support", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-rsvp-neighbor', u'output', u'mpls-rsvp-neighbor', u'show-mpls-neighbor-brief']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-rsvp-neighbor', u'output', u'mpls-rsvp-neighbor', u'show-mpls-neighbor-brief']

  def _get_mpls_rsvp_neighbor_ip_addr(self):
    """
    Getter method for mpls_rsvp_neighbor_ip_addr, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor/output/mpls_rsvp_neighbor/show_mpls_neighbor_brief/mpls_rsvp_neighbor_ip_addr (inet:ipv4-address)

    YANG Description: MPLS RSVP Neighbor IP address
    """
    return self.__mpls_rsvp_neighbor_ip_addr
      
  def _set_mpls_rsvp_neighbor_ip_addr(self, v, load=False):
    """
    Setter method for mpls_rsvp_neighbor_ip_addr, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor/output/mpls_rsvp_neighbor/show_mpls_neighbor_brief/mpls_rsvp_neighbor_ip_addr (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_rsvp_neighbor_ip_addr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_rsvp_neighbor_ip_addr() directly.

    YANG Description: MPLS RSVP Neighbor IP address
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mpls_rsvp_neighbor_ip_addr", rest_name="mpls_rsvp_neighbor_ip_addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_rsvp_neighbor_ip_addr must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mpls_rsvp_neighbor_ip_addr", rest_name="mpls_rsvp_neighbor_ip_addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__mpls_rsvp_neighbor_ip_addr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_rsvp_neighbor_ip_addr(self):
    self.__mpls_rsvp_neighbor_ip_addr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mpls_rsvp_neighbor_ip_addr", rest_name="mpls_rsvp_neighbor_ip_addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)


  def _get_mpls_rsvp_neighbor_interface(self):
    """
    Getter method for mpls_rsvp_neighbor_interface, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor/output/mpls_rsvp_neighbor/show_mpls_neighbor_brief/mpls_rsvp_neighbor_interface (string)

    YANG Description: RSVP neighbor interface
    """
    return self.__mpls_rsvp_neighbor_interface
      
  def _set_mpls_rsvp_neighbor_interface(self, v, load=False):
    """
    Setter method for mpls_rsvp_neighbor_interface, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor/output/mpls_rsvp_neighbor/show_mpls_neighbor_brief/mpls_rsvp_neighbor_interface (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_rsvp_neighbor_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_rsvp_neighbor_interface() directly.

    YANG Description: RSVP neighbor interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mpls-rsvp-neighbor-interface", rest_name="mpls-rsvp-neighbor-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_rsvp_neighbor_interface must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-rsvp-neighbor-interface", rest_name="mpls-rsvp-neighbor-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__mpls_rsvp_neighbor_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_rsvp_neighbor_interface(self):
    self.__mpls_rsvp_neighbor_interface = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-rsvp-neighbor-interface", rest_name="mpls-rsvp-neighbor-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_mpls_rsvp_neighbor_status(self):
    """
    Getter method for mpls_rsvp_neighbor_status, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor/output/mpls_rsvp_neighbor/show_mpls_neighbor_brief/mpls_rsvp_neighbor_status (string)

    YANG Description: Status of MPLS RSVP neighbor
    """
    return self.__mpls_rsvp_neighbor_status
      
  def _set_mpls_rsvp_neighbor_status(self, v, load=False):
    """
    Setter method for mpls_rsvp_neighbor_status, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor/output/mpls_rsvp_neighbor/show_mpls_neighbor_brief/mpls_rsvp_neighbor_status (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_rsvp_neighbor_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_rsvp_neighbor_status() directly.

    YANG Description: Status of MPLS RSVP neighbor
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mpls-rsvp-neighbor-status", rest_name="mpls-rsvp-neighbor-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_rsvp_neighbor_status must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-rsvp-neighbor-status", rest_name="mpls-rsvp-neighbor-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__mpls_rsvp_neighbor_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_rsvp_neighbor_status(self):
    self.__mpls_rsvp_neighbor_status = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-rsvp-neighbor-status", rest_name="mpls-rsvp-neighbor-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_mpls_rsvp_neighbor_last_status_change(self):
    """
    Getter method for mpls_rsvp_neighbor_last_status_change, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor/output/mpls_rsvp_neighbor/show_mpls_neighbor_brief/mpls_rsvp_neighbor_last_status_change (string)

    YANG Description: Time since the status of RSVP neighbor last changed
    """
    return self.__mpls_rsvp_neighbor_last_status_change
      
  def _set_mpls_rsvp_neighbor_last_status_change(self, v, load=False):
    """
    Setter method for mpls_rsvp_neighbor_last_status_change, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor/output/mpls_rsvp_neighbor/show_mpls_neighbor_brief/mpls_rsvp_neighbor_last_status_change (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_rsvp_neighbor_last_status_change is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_rsvp_neighbor_last_status_change() directly.

    YANG Description: Time since the status of RSVP neighbor last changed
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mpls-rsvp-neighbor-last-status-change", rest_name="mpls-rsvp-neighbor-last-status-change", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_rsvp_neighbor_last_status_change must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-rsvp-neighbor-last-status-change", rest_name="mpls-rsvp-neighbor-last-status-change", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__mpls_rsvp_neighbor_last_status_change = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_rsvp_neighbor_last_status_change(self):
    self.__mpls_rsvp_neighbor_last_status_change = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-rsvp-neighbor-last-status-change", rest_name="mpls-rsvp-neighbor-last-status-change", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_mpls_rsvp_neighbor_hello_tx(self):
    """
    Getter method for mpls_rsvp_neighbor_hello_tx, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor/output/mpls_rsvp_neighbor/show_mpls_neighbor_brief/mpls_rsvp_neighbor_hello_tx (uint32)

    YANG Description: Number of RSVP Hello messages transmitted for the neighbor
    """
    return self.__mpls_rsvp_neighbor_hello_tx
      
  def _set_mpls_rsvp_neighbor_hello_tx(self, v, load=False):
    """
    Setter method for mpls_rsvp_neighbor_hello_tx, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor/output/mpls_rsvp_neighbor/show_mpls_neighbor_brief/mpls_rsvp_neighbor_hello_tx (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_rsvp_neighbor_hello_tx is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_rsvp_neighbor_hello_tx() directly.

    YANG Description: Number of RSVP Hello messages transmitted for the neighbor
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-hello-tx", rest_name="mpls-rsvp-neighbor-hello-tx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_rsvp_neighbor_hello_tx must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-hello-tx", rest_name="mpls-rsvp-neighbor-hello-tx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__mpls_rsvp_neighbor_hello_tx = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_rsvp_neighbor_hello_tx(self):
    self.__mpls_rsvp_neighbor_hello_tx = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-hello-tx", rest_name="mpls-rsvp-neighbor-hello-tx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_mpls_rsvp_neighbor_hello_rx(self):
    """
    Getter method for mpls_rsvp_neighbor_hello_rx, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor/output/mpls_rsvp_neighbor/show_mpls_neighbor_brief/mpls_rsvp_neighbor_hello_rx (uint32)

    YANG Description: Number of RSVP Hello messages received for the neighbor
    """
    return self.__mpls_rsvp_neighbor_hello_rx
      
  def _set_mpls_rsvp_neighbor_hello_rx(self, v, load=False):
    """
    Setter method for mpls_rsvp_neighbor_hello_rx, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor/output/mpls_rsvp_neighbor/show_mpls_neighbor_brief/mpls_rsvp_neighbor_hello_rx (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_rsvp_neighbor_hello_rx is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_rsvp_neighbor_hello_rx() directly.

    YANG Description: Number of RSVP Hello messages received for the neighbor
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-hello-rx", rest_name="mpls-rsvp-neighbor-hello-rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_rsvp_neighbor_hello_rx must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-hello-rx", rest_name="mpls-rsvp-neighbor-hello-rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__mpls_rsvp_neighbor_hello_rx = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_rsvp_neighbor_hello_rx(self):
    self.__mpls_rsvp_neighbor_hello_rx = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-hello-rx", rest_name="mpls-rsvp-neighbor-hello-rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_mpls_rsvp_neighbor_refresh_reduction_support(self):
    """
    Getter method for mpls_rsvp_neighbor_refresh_reduction_support, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor/output/mpls_rsvp_neighbor/show_mpls_neighbor_brief/mpls_rsvp_neighbor_refresh_reduction_support (boolean)

    YANG Description: Status of Refresh Reduction support for the RSVP neighbor
    """
    return self.__mpls_rsvp_neighbor_refresh_reduction_support
      
  def _set_mpls_rsvp_neighbor_refresh_reduction_support(self, v, load=False):
    """
    Setter method for mpls_rsvp_neighbor_refresh_reduction_support, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor/output/mpls_rsvp_neighbor/show_mpls_neighbor_brief/mpls_rsvp_neighbor_refresh_reduction_support (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_rsvp_neighbor_refresh_reduction_support is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_rsvp_neighbor_refresh_reduction_support() directly.

    YANG Description: Status of Refresh Reduction support for the RSVP neighbor
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="mpls-rsvp-neighbor-refresh-reduction-support", rest_name="mpls-rsvp-neighbor-refresh-reduction-support", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_rsvp_neighbor_refresh_reduction_support must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-rsvp-neighbor-refresh-reduction-support", rest_name="mpls-rsvp-neighbor-refresh-reduction-support", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__mpls_rsvp_neighbor_refresh_reduction_support = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_rsvp_neighbor_refresh_reduction_support(self):
    self.__mpls_rsvp_neighbor_refresh_reduction_support = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-rsvp-neighbor-refresh-reduction-support", rest_name="mpls-rsvp-neighbor-refresh-reduction-support", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_mpls_rsvp_neighbor_msg_id_support(self):
    """
    Getter method for mpls_rsvp_neighbor_msg_id_support, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor/output/mpls_rsvp_neighbor/show_mpls_neighbor_brief/mpls_rsvp_neighbor_msg_id_support (boolean)

    YANG Description: Status of Message ID support for the RSVP neighbor
    """
    return self.__mpls_rsvp_neighbor_msg_id_support
      
  def _set_mpls_rsvp_neighbor_msg_id_support(self, v, load=False):
    """
    Setter method for mpls_rsvp_neighbor_msg_id_support, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor/output/mpls_rsvp_neighbor/show_mpls_neighbor_brief/mpls_rsvp_neighbor_msg_id_support (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_rsvp_neighbor_msg_id_support is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_rsvp_neighbor_msg_id_support() directly.

    YANG Description: Status of Message ID support for the RSVP neighbor
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="mpls-rsvp-neighbor-msg-id-support", rest_name="mpls-rsvp-neighbor-msg-id-support", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_rsvp_neighbor_msg_id_support must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-rsvp-neighbor-msg-id-support", rest_name="mpls-rsvp-neighbor-msg-id-support", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__mpls_rsvp_neighbor_msg_id_support = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_rsvp_neighbor_msg_id_support(self):
    self.__mpls_rsvp_neighbor_msg_id_support = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-rsvp-neighbor-msg-id-support", rest_name="mpls-rsvp-neighbor-msg-id-support", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)

  mpls_rsvp_neighbor_ip_addr = __builtin__.property(_get_mpls_rsvp_neighbor_ip_addr, _set_mpls_rsvp_neighbor_ip_addr)
  mpls_rsvp_neighbor_interface = __builtin__.property(_get_mpls_rsvp_neighbor_interface, _set_mpls_rsvp_neighbor_interface)
  mpls_rsvp_neighbor_status = __builtin__.property(_get_mpls_rsvp_neighbor_status, _set_mpls_rsvp_neighbor_status)
  mpls_rsvp_neighbor_last_status_change = __builtin__.property(_get_mpls_rsvp_neighbor_last_status_change, _set_mpls_rsvp_neighbor_last_status_change)
  mpls_rsvp_neighbor_hello_tx = __builtin__.property(_get_mpls_rsvp_neighbor_hello_tx, _set_mpls_rsvp_neighbor_hello_tx)
  mpls_rsvp_neighbor_hello_rx = __builtin__.property(_get_mpls_rsvp_neighbor_hello_rx, _set_mpls_rsvp_neighbor_hello_rx)
  mpls_rsvp_neighbor_refresh_reduction_support = __builtin__.property(_get_mpls_rsvp_neighbor_refresh_reduction_support, _set_mpls_rsvp_neighbor_refresh_reduction_support)
  mpls_rsvp_neighbor_msg_id_support = __builtin__.property(_get_mpls_rsvp_neighbor_msg_id_support, _set_mpls_rsvp_neighbor_msg_id_support)


  _pyangbind_elements = {'mpls_rsvp_neighbor_ip_addr': mpls_rsvp_neighbor_ip_addr, 'mpls_rsvp_neighbor_interface': mpls_rsvp_neighbor_interface, 'mpls_rsvp_neighbor_status': mpls_rsvp_neighbor_status, 'mpls_rsvp_neighbor_last_status_change': mpls_rsvp_neighbor_last_status_change, 'mpls_rsvp_neighbor_hello_tx': mpls_rsvp_neighbor_hello_tx, 'mpls_rsvp_neighbor_hello_rx': mpls_rsvp_neighbor_hello_rx, 'mpls_rsvp_neighbor_refresh_reduction_support': mpls_rsvp_neighbor_refresh_reduction_support, 'mpls_rsvp_neighbor_msg_id_support': mpls_rsvp_neighbor_msg_id_support, }


