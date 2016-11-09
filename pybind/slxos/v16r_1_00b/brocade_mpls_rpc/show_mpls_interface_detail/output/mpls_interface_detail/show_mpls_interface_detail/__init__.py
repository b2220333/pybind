
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class show_mpls_interface_detail(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-interface-detail/output/mpls-interface-detail/show-mpls-interface-detail. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mpls_interface_mtu','__mpls_interface_gre_port','__mpls_interface_max_resv_bw_percentage','__mpls_interface_te_metric_default','__mpls_interface_te_metric_value','__mpls_interface_reservable_bw','__mpls_interface_advertised_unreserved_bw','__mpls_interface_under_prov_bw','__mpls_interface_ldp_ingress_count','__mpls_interface_p2mp_capability',)

  _yang_name = 'show-mpls-interface-detail'
  _rest_name = 'show-mpls-interface-detail'

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
    self.__mpls_interface_gre_port = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-interface-gre-port", rest_name="mpls-interface-gre-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__mpls_interface_te_metric_default = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-interface-te-metric-default", rest_name="mpls-interface-te-metric-default", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__mpls_interface_mtu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-mtu", rest_name="mpls-interface-mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__mpls_interface_te_metric_value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-te-metric-value", rest_name="mpls-interface-te-metric-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__mpls_interface_p2mp_capability = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-interface-p2mp-capability", rest_name="mpls-interface-p2mp-capability", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__mpls_interface_advertised_unreserved_bw = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="mpls-interface-advertised-unreserved-bw", rest_name="mpls-interface-advertised-unreserved-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__mpls_interface_max_resv_bw_percentage = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-interface-max-resv-bw-percentage", rest_name="mpls-interface-max-resv-bw-percentage", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__mpls_interface_reservable_bw = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="mpls-interface-reservable-bw", rest_name="mpls-interface-reservable-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__mpls_interface_under_prov_bw = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="mpls-interface-under-prov-bw", rest_name="mpls-interface-under-prov-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__mpls_interface_ldp_ingress_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-ldp-ingress-count", rest_name="mpls-interface-ldp-ingress-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-interface-detail', u'output', u'mpls-interface-detail', u'show-mpls-interface-detail']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-interface-detail', u'output', u'mpls-interface-detail', u'show-mpls-interface-detail']

  def _get_mpls_interface_mtu(self):
    """
    Getter method for mpls_interface_mtu, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface_detail/output/mpls_interface_detail/show_mpls_interface_detail/mpls_interface_mtu (uint32)

    YANG Description: MTU of the MPLS Interface
    """
    return self.__mpls_interface_mtu
      
  def _set_mpls_interface_mtu(self, v, load=False):
    """
    Setter method for mpls_interface_mtu, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface_detail/output/mpls_interface_detail/show_mpls_interface_detail/mpls_interface_mtu (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_interface_mtu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_interface_mtu() directly.

    YANG Description: MTU of the MPLS Interface
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-mtu", rest_name="mpls-interface-mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_interface_mtu must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-mtu", rest_name="mpls-interface-mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__mpls_interface_mtu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_interface_mtu(self):
    self.__mpls_interface_mtu = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-mtu", rest_name="mpls-interface-mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_mpls_interface_gre_port(self):
    """
    Getter method for mpls_interface_gre_port, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface_detail/output/mpls_interface_detail/show_mpls_interface_detail/mpls_interface_gre_port (boolean)

    YANG Description: Specifies if MPLS interface is a GRE IP Tunnel Port
    """
    return self.__mpls_interface_gre_port
      
  def _set_mpls_interface_gre_port(self, v, load=False):
    """
    Setter method for mpls_interface_gre_port, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface_detail/output/mpls_interface_detail/show_mpls_interface_detail/mpls_interface_gre_port (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_interface_gre_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_interface_gre_port() directly.

    YANG Description: Specifies if MPLS interface is a GRE IP Tunnel Port
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="mpls-interface-gre-port", rest_name="mpls-interface-gre-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_interface_gre_port must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-interface-gre-port", rest_name="mpls-interface-gre-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__mpls_interface_gre_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_interface_gre_port(self):
    self.__mpls_interface_gre_port = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-interface-gre-port", rest_name="mpls-interface-gre-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_mpls_interface_max_resv_bw_percentage(self):
    """
    Getter method for mpls_interface_max_resv_bw_percentage, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface_detail/output/mpls_interface_detail/show_mpls_interface_detail/mpls_interface_max_resv_bw_percentage (boolean)

    YANG Description: Maximum Reservable Bandwidth of the MPLS interface in percentage if configured as %
    """
    return self.__mpls_interface_max_resv_bw_percentage
      
  def _set_mpls_interface_max_resv_bw_percentage(self, v, load=False):
    """
    Setter method for mpls_interface_max_resv_bw_percentage, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface_detail/output/mpls_interface_detail/show_mpls_interface_detail/mpls_interface_max_resv_bw_percentage (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_interface_max_resv_bw_percentage is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_interface_max_resv_bw_percentage() directly.

    YANG Description: Maximum Reservable Bandwidth of the MPLS interface in percentage if configured as %
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="mpls-interface-max-resv-bw-percentage", rest_name="mpls-interface-max-resv-bw-percentage", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_interface_max_resv_bw_percentage must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-interface-max-resv-bw-percentage", rest_name="mpls-interface-max-resv-bw-percentage", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__mpls_interface_max_resv_bw_percentage = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_interface_max_resv_bw_percentage(self):
    self.__mpls_interface_max_resv_bw_percentage = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-interface-max-resv-bw-percentage", rest_name="mpls-interface-max-resv-bw-percentage", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_mpls_interface_te_metric_default(self):
    """
    Getter method for mpls_interface_te_metric_default, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface_detail/output/mpls_interface_detail/show_mpls_interface_detail/mpls_interface_te_metric_default (boolean)

    YANG Description: TE metric default configuration of the MPLS interface
    """
    return self.__mpls_interface_te_metric_default
      
  def _set_mpls_interface_te_metric_default(self, v, load=False):
    """
    Setter method for mpls_interface_te_metric_default, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface_detail/output/mpls_interface_detail/show_mpls_interface_detail/mpls_interface_te_metric_default (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_interface_te_metric_default is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_interface_te_metric_default() directly.

    YANG Description: TE metric default configuration of the MPLS interface
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="mpls-interface-te-metric-default", rest_name="mpls-interface-te-metric-default", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_interface_te_metric_default must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-interface-te-metric-default", rest_name="mpls-interface-te-metric-default", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__mpls_interface_te_metric_default = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_interface_te_metric_default(self):
    self.__mpls_interface_te_metric_default = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-interface-te-metric-default", rest_name="mpls-interface-te-metric-default", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_mpls_interface_te_metric_value(self):
    """
    Getter method for mpls_interface_te_metric_value, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface_detail/output/mpls_interface_detail/show_mpls_interface_detail/mpls_interface_te_metric_value (uint32)

    YANG Description: TE metric value configured on the MPLS interface
    """
    return self.__mpls_interface_te_metric_value
      
  def _set_mpls_interface_te_metric_value(self, v, load=False):
    """
    Setter method for mpls_interface_te_metric_value, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface_detail/output/mpls_interface_detail/show_mpls_interface_detail/mpls_interface_te_metric_value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_interface_te_metric_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_interface_te_metric_value() directly.

    YANG Description: TE metric value configured on the MPLS interface
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-te-metric-value", rest_name="mpls-interface-te-metric-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_interface_te_metric_value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-te-metric-value", rest_name="mpls-interface-te-metric-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__mpls_interface_te_metric_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_interface_te_metric_value(self):
    self.__mpls_interface_te_metric_value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-te-metric-value", rest_name="mpls-interface-te-metric-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_mpls_interface_reservable_bw(self):
    """
    Getter method for mpls_interface_reservable_bw, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface_detail/output/mpls_interface_detail/show_mpls_interface_detail/mpls_interface_reservable_bw (uint32)

    YANG Description: Reservable bandwidth per priority in kbits/sec
    """
    return self.__mpls_interface_reservable_bw
      
  def _set_mpls_interface_reservable_bw(self, v, load=False):
    """
    Setter method for mpls_interface_reservable_bw, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface_detail/output/mpls_interface_detail/show_mpls_interface_detail/mpls_interface_reservable_bw (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_interface_reservable_bw is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_interface_reservable_bw() directly.

    YANG Description: Reservable bandwidth per priority in kbits/sec
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="mpls-interface-reservable-bw", rest_name="mpls-interface-reservable-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_interface_reservable_bw must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="mpls-interface-reservable-bw", rest_name="mpls-interface-reservable-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__mpls_interface_reservable_bw = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_interface_reservable_bw(self):
    self.__mpls_interface_reservable_bw = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="mpls-interface-reservable-bw", rest_name="mpls-interface-reservable-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_mpls_interface_advertised_unreserved_bw(self):
    """
    Getter method for mpls_interface_advertised_unreserved_bw, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface_detail/output/mpls_interface_detail/show_mpls_interface_detail/mpls_interface_advertised_unreserved_bw (uint32)

    YANG Description: Last sent reservable bandwidth per priority in kbits/sec
    """
    return self.__mpls_interface_advertised_unreserved_bw
      
  def _set_mpls_interface_advertised_unreserved_bw(self, v, load=False):
    """
    Setter method for mpls_interface_advertised_unreserved_bw, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface_detail/output/mpls_interface_detail/show_mpls_interface_detail/mpls_interface_advertised_unreserved_bw (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_interface_advertised_unreserved_bw is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_interface_advertised_unreserved_bw() directly.

    YANG Description: Last sent reservable bandwidth per priority in kbits/sec
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="mpls-interface-advertised-unreserved-bw", rest_name="mpls-interface-advertised-unreserved-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_interface_advertised_unreserved_bw must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="mpls-interface-advertised-unreserved-bw", rest_name="mpls-interface-advertised-unreserved-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__mpls_interface_advertised_unreserved_bw = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_interface_advertised_unreserved_bw(self):
    self.__mpls_interface_advertised_unreserved_bw = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="mpls-interface-advertised-unreserved-bw", rest_name="mpls-interface-advertised-unreserved-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_mpls_interface_under_prov_bw(self):
    """
    Getter method for mpls_interface_under_prov_bw, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface_detail/output/mpls_interface_detail/show_mpls_interface_detail/mpls_interface_under_prov_bw (uint32)

    YANG Description: Soft Preemption under provisioned bandwidth per priority in kbits/sec
    """
    return self.__mpls_interface_under_prov_bw
      
  def _set_mpls_interface_under_prov_bw(self, v, load=False):
    """
    Setter method for mpls_interface_under_prov_bw, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface_detail/output/mpls_interface_detail/show_mpls_interface_detail/mpls_interface_under_prov_bw (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_interface_under_prov_bw is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_interface_under_prov_bw() directly.

    YANG Description: Soft Preemption under provisioned bandwidth per priority in kbits/sec
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="mpls-interface-under-prov-bw", rest_name="mpls-interface-under-prov-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_interface_under_prov_bw must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="mpls-interface-under-prov-bw", rest_name="mpls-interface-under-prov-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__mpls_interface_under_prov_bw = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_interface_under_prov_bw(self):
    self.__mpls_interface_under_prov_bw = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="mpls-interface-under-prov-bw", rest_name="mpls-interface-under-prov-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_mpls_interface_ldp_ingress_count(self):
    """
    Getter method for mpls_interface_ldp_ingress_count, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface_detail/output/mpls_interface_detail/show_mpls_interface_detail/mpls_interface_ldp_ingress_count (uint32)

    YANG Description: Number of LDP tunnels on the MPLS interface
    """
    return self.__mpls_interface_ldp_ingress_count
      
  def _set_mpls_interface_ldp_ingress_count(self, v, load=False):
    """
    Setter method for mpls_interface_ldp_ingress_count, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface_detail/output/mpls_interface_detail/show_mpls_interface_detail/mpls_interface_ldp_ingress_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_interface_ldp_ingress_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_interface_ldp_ingress_count() directly.

    YANG Description: Number of LDP tunnels on the MPLS interface
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-ldp-ingress-count", rest_name="mpls-interface-ldp-ingress-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_interface_ldp_ingress_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-ldp-ingress-count", rest_name="mpls-interface-ldp-ingress-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__mpls_interface_ldp_ingress_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_interface_ldp_ingress_count(self):
    self.__mpls_interface_ldp_ingress_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-ldp-ingress-count", rest_name="mpls-interface-ldp-ingress-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_mpls_interface_p2mp_capability(self):
    """
    Getter method for mpls_interface_p2mp_capability, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface_detail/output/mpls_interface_detail/show_mpls_interface_detail/mpls_interface_p2mp_capability (boolean)

    YANG Description: P2MP capability of MPLS interface
    """
    return self.__mpls_interface_p2mp_capability
      
  def _set_mpls_interface_p2mp_capability(self, v, load=False):
    """
    Setter method for mpls_interface_p2mp_capability, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface_detail/output/mpls_interface_detail/show_mpls_interface_detail/mpls_interface_p2mp_capability (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_interface_p2mp_capability is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_interface_p2mp_capability() directly.

    YANG Description: P2MP capability of MPLS interface
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="mpls-interface-p2mp-capability", rest_name="mpls-interface-p2mp-capability", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_interface_p2mp_capability must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-interface-p2mp-capability", rest_name="mpls-interface-p2mp-capability", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__mpls_interface_p2mp_capability = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_interface_p2mp_capability(self):
    self.__mpls_interface_p2mp_capability = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-interface-p2mp-capability", rest_name="mpls-interface-p2mp-capability", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)

  mpls_interface_mtu = __builtin__.property(_get_mpls_interface_mtu, _set_mpls_interface_mtu)
  mpls_interface_gre_port = __builtin__.property(_get_mpls_interface_gre_port, _set_mpls_interface_gre_port)
  mpls_interface_max_resv_bw_percentage = __builtin__.property(_get_mpls_interface_max_resv_bw_percentage, _set_mpls_interface_max_resv_bw_percentage)
  mpls_interface_te_metric_default = __builtin__.property(_get_mpls_interface_te_metric_default, _set_mpls_interface_te_metric_default)
  mpls_interface_te_metric_value = __builtin__.property(_get_mpls_interface_te_metric_value, _set_mpls_interface_te_metric_value)
  mpls_interface_reservable_bw = __builtin__.property(_get_mpls_interface_reservable_bw, _set_mpls_interface_reservable_bw)
  mpls_interface_advertised_unreserved_bw = __builtin__.property(_get_mpls_interface_advertised_unreserved_bw, _set_mpls_interface_advertised_unreserved_bw)
  mpls_interface_under_prov_bw = __builtin__.property(_get_mpls_interface_under_prov_bw, _set_mpls_interface_under_prov_bw)
  mpls_interface_ldp_ingress_count = __builtin__.property(_get_mpls_interface_ldp_ingress_count, _set_mpls_interface_ldp_ingress_count)
  mpls_interface_p2mp_capability = __builtin__.property(_get_mpls_interface_p2mp_capability, _set_mpls_interface_p2mp_capability)


  _pyangbind_elements = {'mpls_interface_mtu': mpls_interface_mtu, 'mpls_interface_gre_port': mpls_interface_gre_port, 'mpls_interface_max_resv_bw_percentage': mpls_interface_max_resv_bw_percentage, 'mpls_interface_te_metric_default': mpls_interface_te_metric_default, 'mpls_interface_te_metric_value': mpls_interface_te_metric_value, 'mpls_interface_reservable_bw': mpls_interface_reservable_bw, 'mpls_interface_advertised_unreserved_bw': mpls_interface_advertised_unreserved_bw, 'mpls_interface_under_prov_bw': mpls_interface_under_prov_bw, 'mpls_interface_ldp_ingress_count': mpls_interface_ldp_ingress_count, 'mpls_interface_p2mp_capability': mpls_interface_p2mp_capability, }


