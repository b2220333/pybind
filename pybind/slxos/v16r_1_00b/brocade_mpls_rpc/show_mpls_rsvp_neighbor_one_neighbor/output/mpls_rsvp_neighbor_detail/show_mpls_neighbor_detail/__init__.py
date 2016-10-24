
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class show_mpls_neighbor_detail(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-rsvp-neighbor-one-neighbor/output/mpls-rsvp-neighbor-detail/show-mpls-neighbor-detail. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mpls_rsvp_neighbor_active_lsps','__mpls_rsvp_neighbor_hello_interval','__mpls_rsvp_neighbor_hello_tolerance','__mpls_rsvp_neighbor_last_hello_rx','__mpls_rsvp_neighbor_next_hello_req_tx','__mpls_rsvp_neighbor_remote_instance','__mpls_rsvp_neighbor_local_instance',)

  _yang_name = 'show-mpls-neighbor-detail'
  _rest_name = 'show-mpls-neighbor-detail'

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
    self.__mpls_rsvp_neighbor_next_hello_req_tx = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-rsvp-neighbor-next-hello-req-tx", rest_name="mpls-rsvp-neighbor-next-hello-req-tx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__mpls_rsvp_neighbor_remote_instance = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-remote-instance", rest_name="mpls-rsvp-neighbor-remote-instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__mpls_rsvp_neighbor_last_hello_rx = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-rsvp-neighbor-last-hello-rx", rest_name="mpls-rsvp-neighbor-last-hello-rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__mpls_rsvp_neighbor_hello_tolerance = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-hello-tolerance", rest_name="mpls-rsvp-neighbor-hello-tolerance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__mpls_rsvp_neighbor_hello_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-hello-interval", rest_name="mpls-rsvp-neighbor-hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__mpls_rsvp_neighbor_local_instance = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-local-instance", rest_name="mpls-rsvp-neighbor-local-instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__mpls_rsvp_neighbor_active_lsps = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-active-lsps", rest_name="mpls-rsvp-neighbor-active-lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-rsvp-neighbor-one-neighbor', u'output', u'mpls-rsvp-neighbor-detail', u'show-mpls-neighbor-detail']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-rsvp-neighbor-one-neighbor', u'output', u'mpls-rsvp-neighbor-detail', u'show-mpls-neighbor-detail']

  def _get_mpls_rsvp_neighbor_active_lsps(self):
    """
    Getter method for mpls_rsvp_neighbor_active_lsps, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor_one_neighbor/output/mpls_rsvp_neighbor_detail/show_mpls_neighbor_detail/mpls_rsvp_neighbor_active_lsps (uint32)

    YANG Description: Number of Active LSPs to or from the RSVP neighbor
    """
    return self.__mpls_rsvp_neighbor_active_lsps
      
  def _set_mpls_rsvp_neighbor_active_lsps(self, v, load=False):
    """
    Setter method for mpls_rsvp_neighbor_active_lsps, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor_one_neighbor/output/mpls_rsvp_neighbor_detail/show_mpls_neighbor_detail/mpls_rsvp_neighbor_active_lsps (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_rsvp_neighbor_active_lsps is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_rsvp_neighbor_active_lsps() directly.

    YANG Description: Number of Active LSPs to or from the RSVP neighbor
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-active-lsps", rest_name="mpls-rsvp-neighbor-active-lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_rsvp_neighbor_active_lsps must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-active-lsps", rest_name="mpls-rsvp-neighbor-active-lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__mpls_rsvp_neighbor_active_lsps = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_rsvp_neighbor_active_lsps(self):
    self.__mpls_rsvp_neighbor_active_lsps = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-active-lsps", rest_name="mpls-rsvp-neighbor-active-lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_mpls_rsvp_neighbor_hello_interval(self):
    """
    Getter method for mpls_rsvp_neighbor_hello_interval, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor_one_neighbor/output/mpls_rsvp_neighbor_detail/show_mpls_neighbor_detail/mpls_rsvp_neighbor_hello_interval (uint32)

    YANG Description: RSVP Hello interval for the RSVP neighbor
    """
    return self.__mpls_rsvp_neighbor_hello_interval
      
  def _set_mpls_rsvp_neighbor_hello_interval(self, v, load=False):
    """
    Setter method for mpls_rsvp_neighbor_hello_interval, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor_one_neighbor/output/mpls_rsvp_neighbor_detail/show_mpls_neighbor_detail/mpls_rsvp_neighbor_hello_interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_rsvp_neighbor_hello_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_rsvp_neighbor_hello_interval() directly.

    YANG Description: RSVP Hello interval for the RSVP neighbor
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-hello-interval", rest_name="mpls-rsvp-neighbor-hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_rsvp_neighbor_hello_interval must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-hello-interval", rest_name="mpls-rsvp-neighbor-hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__mpls_rsvp_neighbor_hello_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_rsvp_neighbor_hello_interval(self):
    self.__mpls_rsvp_neighbor_hello_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-hello-interval", rest_name="mpls-rsvp-neighbor-hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_mpls_rsvp_neighbor_hello_tolerance(self):
    """
    Getter method for mpls_rsvp_neighbor_hello_tolerance, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor_one_neighbor/output/mpls_rsvp_neighbor_detail/show_mpls_neighbor_detail/mpls_rsvp_neighbor_hello_tolerance (uint32)

    YANG Description: RSVP Hello tolerance for the RSVP neighbor
    """
    return self.__mpls_rsvp_neighbor_hello_tolerance
      
  def _set_mpls_rsvp_neighbor_hello_tolerance(self, v, load=False):
    """
    Setter method for mpls_rsvp_neighbor_hello_tolerance, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor_one_neighbor/output/mpls_rsvp_neighbor_detail/show_mpls_neighbor_detail/mpls_rsvp_neighbor_hello_tolerance (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_rsvp_neighbor_hello_tolerance is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_rsvp_neighbor_hello_tolerance() directly.

    YANG Description: RSVP Hello tolerance for the RSVP neighbor
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-hello-tolerance", rest_name="mpls-rsvp-neighbor-hello-tolerance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_rsvp_neighbor_hello_tolerance must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-hello-tolerance", rest_name="mpls-rsvp-neighbor-hello-tolerance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__mpls_rsvp_neighbor_hello_tolerance = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_rsvp_neighbor_hello_tolerance(self):
    self.__mpls_rsvp_neighbor_hello_tolerance = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-hello-tolerance", rest_name="mpls-rsvp-neighbor-hello-tolerance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_mpls_rsvp_neighbor_last_hello_rx(self):
    """
    Getter method for mpls_rsvp_neighbor_last_hello_rx, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor_one_neighbor/output/mpls_rsvp_neighbor_detail/show_mpls_neighbor_detail/mpls_rsvp_neighbor_last_hello_rx (string)

    YANG Description: Time elapsed since the last Hello message was received
    """
    return self.__mpls_rsvp_neighbor_last_hello_rx
      
  def _set_mpls_rsvp_neighbor_last_hello_rx(self, v, load=False):
    """
    Setter method for mpls_rsvp_neighbor_last_hello_rx, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor_one_neighbor/output/mpls_rsvp_neighbor_detail/show_mpls_neighbor_detail/mpls_rsvp_neighbor_last_hello_rx (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_rsvp_neighbor_last_hello_rx is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_rsvp_neighbor_last_hello_rx() directly.

    YANG Description: Time elapsed since the last Hello message was received
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mpls-rsvp-neighbor-last-hello-rx", rest_name="mpls-rsvp-neighbor-last-hello-rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_rsvp_neighbor_last_hello_rx must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-rsvp-neighbor-last-hello-rx", rest_name="mpls-rsvp-neighbor-last-hello-rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__mpls_rsvp_neighbor_last_hello_rx = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_rsvp_neighbor_last_hello_rx(self):
    self.__mpls_rsvp_neighbor_last_hello_rx = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-rsvp-neighbor-last-hello-rx", rest_name="mpls-rsvp-neighbor-last-hello-rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_mpls_rsvp_neighbor_next_hello_req_tx(self):
    """
    Getter method for mpls_rsvp_neighbor_next_hello_req_tx, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor_one_neighbor/output/mpls_rsvp_neighbor_detail/show_mpls_neighbor_detail/mpls_rsvp_neighbor_next_hello_req_tx (string)

    YANG Description: Time remaining for the next Hello Request to be sent
    """
    return self.__mpls_rsvp_neighbor_next_hello_req_tx
      
  def _set_mpls_rsvp_neighbor_next_hello_req_tx(self, v, load=False):
    """
    Setter method for mpls_rsvp_neighbor_next_hello_req_tx, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor_one_neighbor/output/mpls_rsvp_neighbor_detail/show_mpls_neighbor_detail/mpls_rsvp_neighbor_next_hello_req_tx (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_rsvp_neighbor_next_hello_req_tx is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_rsvp_neighbor_next_hello_req_tx() directly.

    YANG Description: Time remaining for the next Hello Request to be sent
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mpls-rsvp-neighbor-next-hello-req-tx", rest_name="mpls-rsvp-neighbor-next-hello-req-tx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_rsvp_neighbor_next_hello_req_tx must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-rsvp-neighbor-next-hello-req-tx", rest_name="mpls-rsvp-neighbor-next-hello-req-tx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__mpls_rsvp_neighbor_next_hello_req_tx = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_rsvp_neighbor_next_hello_req_tx(self):
    self.__mpls_rsvp_neighbor_next_hello_req_tx = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-rsvp-neighbor-next-hello-req-tx", rest_name="mpls-rsvp-neighbor-next-hello-req-tx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_mpls_rsvp_neighbor_remote_instance(self):
    """
    Getter method for mpls_rsvp_neighbor_remote_instance, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor_one_neighbor/output/mpls_rsvp_neighbor_detail/show_mpls_neighbor_detail/mpls_rsvp_neighbor_remote_instance (uint32)

    YANG Description: Remote instance ID
    """
    return self.__mpls_rsvp_neighbor_remote_instance
      
  def _set_mpls_rsvp_neighbor_remote_instance(self, v, load=False):
    """
    Setter method for mpls_rsvp_neighbor_remote_instance, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor_one_neighbor/output/mpls_rsvp_neighbor_detail/show_mpls_neighbor_detail/mpls_rsvp_neighbor_remote_instance (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_rsvp_neighbor_remote_instance is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_rsvp_neighbor_remote_instance() directly.

    YANG Description: Remote instance ID
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-remote-instance", rest_name="mpls-rsvp-neighbor-remote-instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_rsvp_neighbor_remote_instance must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-remote-instance", rest_name="mpls-rsvp-neighbor-remote-instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__mpls_rsvp_neighbor_remote_instance = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_rsvp_neighbor_remote_instance(self):
    self.__mpls_rsvp_neighbor_remote_instance = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-remote-instance", rest_name="mpls-rsvp-neighbor-remote-instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_mpls_rsvp_neighbor_local_instance(self):
    """
    Getter method for mpls_rsvp_neighbor_local_instance, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor_one_neighbor/output/mpls_rsvp_neighbor_detail/show_mpls_neighbor_detail/mpls_rsvp_neighbor_local_instance (uint32)

    YANG Description: Local instance ID
    """
    return self.__mpls_rsvp_neighbor_local_instance
      
  def _set_mpls_rsvp_neighbor_local_instance(self, v, load=False):
    """
    Setter method for mpls_rsvp_neighbor_local_instance, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor_one_neighbor/output/mpls_rsvp_neighbor_detail/show_mpls_neighbor_detail/mpls_rsvp_neighbor_local_instance (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_rsvp_neighbor_local_instance is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_rsvp_neighbor_local_instance() directly.

    YANG Description: Local instance ID
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-local-instance", rest_name="mpls-rsvp-neighbor-local-instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_rsvp_neighbor_local_instance must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-local-instance", rest_name="mpls-rsvp-neighbor-local-instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__mpls_rsvp_neighbor_local_instance = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_rsvp_neighbor_local_instance(self):
    self.__mpls_rsvp_neighbor_local_instance = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-rsvp-neighbor-local-instance", rest_name="mpls-rsvp-neighbor-local-instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

  mpls_rsvp_neighbor_active_lsps = __builtin__.property(_get_mpls_rsvp_neighbor_active_lsps, _set_mpls_rsvp_neighbor_active_lsps)
  mpls_rsvp_neighbor_hello_interval = __builtin__.property(_get_mpls_rsvp_neighbor_hello_interval, _set_mpls_rsvp_neighbor_hello_interval)
  mpls_rsvp_neighbor_hello_tolerance = __builtin__.property(_get_mpls_rsvp_neighbor_hello_tolerance, _set_mpls_rsvp_neighbor_hello_tolerance)
  mpls_rsvp_neighbor_last_hello_rx = __builtin__.property(_get_mpls_rsvp_neighbor_last_hello_rx, _set_mpls_rsvp_neighbor_last_hello_rx)
  mpls_rsvp_neighbor_next_hello_req_tx = __builtin__.property(_get_mpls_rsvp_neighbor_next_hello_req_tx, _set_mpls_rsvp_neighbor_next_hello_req_tx)
  mpls_rsvp_neighbor_remote_instance = __builtin__.property(_get_mpls_rsvp_neighbor_remote_instance, _set_mpls_rsvp_neighbor_remote_instance)
  mpls_rsvp_neighbor_local_instance = __builtin__.property(_get_mpls_rsvp_neighbor_local_instance, _set_mpls_rsvp_neighbor_local_instance)


  _pyangbind_elements = {'mpls_rsvp_neighbor_active_lsps': mpls_rsvp_neighbor_active_lsps, 'mpls_rsvp_neighbor_hello_interval': mpls_rsvp_neighbor_hello_interval, 'mpls_rsvp_neighbor_hello_tolerance': mpls_rsvp_neighbor_hello_tolerance, 'mpls_rsvp_neighbor_last_hello_rx': mpls_rsvp_neighbor_last_hello_rx, 'mpls_rsvp_neighbor_next_hello_req_tx': mpls_rsvp_neighbor_next_hello_req_tx, 'mpls_rsvp_neighbor_remote_instance': mpls_rsvp_neighbor_remote_instance, 'mpls_rsvp_neighbor_local_instance': mpls_rsvp_neighbor_local_instance, }


