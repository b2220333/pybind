
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class show_mpls_lsp_forwarding_info(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-bypass-lsp-name-extensive/output/bypass-lsp/show-mpls-lsp-extensive-info/show-mpls-lsp-forwarding-info. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__lsp_forwarding_primary_active','__lsp_forwarding_primary_up','__lsp_forwarding_secondary_active','__lsp_forwarding_secondary_up','__lsp_forwarding_frr_active','__lsp_forwarding_frr_up','__lsp_forwarding_out_port_id','__lsp_forwarding_out_port_name','__lsp_forwarding_out_label',)

  _yang_name = 'show-mpls-lsp-forwarding-info'
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
    self.__lsp_forwarding_frr_active = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-forwarding-frr-active", rest_name="lsp-forwarding-frr-active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__lsp_forwarding_out_label = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lsp-forwarding-out-label", rest_name="lsp-forwarding-out-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__lsp_forwarding_out_port_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="lsp-forwarding-out-port-name", rest_name="lsp-forwarding-out-port-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__lsp_forwarding_secondary_active = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-forwarding-secondary-active", rest_name="lsp-forwarding-secondary-active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__lsp_forwarding_out_port_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lsp-forwarding-out-port-id", rest_name="lsp-forwarding-out-port-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__lsp_forwarding_secondary_up = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-forwarding-secondary-up", rest_name="lsp-forwarding-secondary-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__lsp_forwarding_frr_up = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-forwarding-frr-up", rest_name="lsp-forwarding-frr-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__lsp_forwarding_primary_active = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-forwarding-primary-active", rest_name="lsp-forwarding-primary-active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__lsp_forwarding_primary_up = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-forwarding-primary-up", rest_name="lsp-forwarding-primary-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-bypass-lsp-name-extensive', u'output', u'bypass-lsp', u'show-mpls-lsp-extensive-info', u'show-mpls-lsp-forwarding-info']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-bypass-lsp-name-extensive', u'output', u'bypass-lsp']

  def _get_lsp_forwarding_primary_active(self):
    """
    Getter method for lsp_forwarding_primary_active, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_forwarding_info/lsp_forwarding_primary_active (boolean)

    YANG Description: LSP forwarding state primary is active
    """
    return self.__lsp_forwarding_primary_active
      
  def _set_lsp_forwarding_primary_active(self, v, load=False):
    """
    Setter method for lsp_forwarding_primary_active, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_forwarding_info/lsp_forwarding_primary_active (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_forwarding_primary_active is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_forwarding_primary_active() directly.

    YANG Description: LSP forwarding state primary is active
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-forwarding-primary-active", rest_name="lsp-forwarding-primary-active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_forwarding_primary_active must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-forwarding-primary-active", rest_name="lsp-forwarding-primary-active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_forwarding_primary_active = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_forwarding_primary_active(self):
    self.__lsp_forwarding_primary_active = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-forwarding-primary-active", rest_name="lsp-forwarding-primary-active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_lsp_forwarding_primary_up(self):
    """
    Getter method for lsp_forwarding_primary_up, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_forwarding_info/lsp_forwarding_primary_up (boolean)

    YANG Description: LSP forwarding state primary is up
    """
    return self.__lsp_forwarding_primary_up
      
  def _set_lsp_forwarding_primary_up(self, v, load=False):
    """
    Setter method for lsp_forwarding_primary_up, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_forwarding_info/lsp_forwarding_primary_up (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_forwarding_primary_up is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_forwarding_primary_up() directly.

    YANG Description: LSP forwarding state primary is up
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-forwarding-primary-up", rest_name="lsp-forwarding-primary-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_forwarding_primary_up must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-forwarding-primary-up", rest_name="lsp-forwarding-primary-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_forwarding_primary_up = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_forwarding_primary_up(self):
    self.__lsp_forwarding_primary_up = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-forwarding-primary-up", rest_name="lsp-forwarding-primary-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_lsp_forwarding_secondary_active(self):
    """
    Getter method for lsp_forwarding_secondary_active, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_forwarding_info/lsp_forwarding_secondary_active (boolean)

    YANG Description: LSP forwarding state secondary is active
    """
    return self.__lsp_forwarding_secondary_active
      
  def _set_lsp_forwarding_secondary_active(self, v, load=False):
    """
    Setter method for lsp_forwarding_secondary_active, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_forwarding_info/lsp_forwarding_secondary_active (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_forwarding_secondary_active is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_forwarding_secondary_active() directly.

    YANG Description: LSP forwarding state secondary is active
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-forwarding-secondary-active", rest_name="lsp-forwarding-secondary-active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_forwarding_secondary_active must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-forwarding-secondary-active", rest_name="lsp-forwarding-secondary-active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_forwarding_secondary_active = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_forwarding_secondary_active(self):
    self.__lsp_forwarding_secondary_active = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-forwarding-secondary-active", rest_name="lsp-forwarding-secondary-active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_lsp_forwarding_secondary_up(self):
    """
    Getter method for lsp_forwarding_secondary_up, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_forwarding_info/lsp_forwarding_secondary_up (boolean)

    YANG Description: LSP forwarding state secondary is up
    """
    return self.__lsp_forwarding_secondary_up
      
  def _set_lsp_forwarding_secondary_up(self, v, load=False):
    """
    Setter method for lsp_forwarding_secondary_up, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_forwarding_info/lsp_forwarding_secondary_up (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_forwarding_secondary_up is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_forwarding_secondary_up() directly.

    YANG Description: LSP forwarding state secondary is up
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-forwarding-secondary-up", rest_name="lsp-forwarding-secondary-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_forwarding_secondary_up must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-forwarding-secondary-up", rest_name="lsp-forwarding-secondary-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_forwarding_secondary_up = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_forwarding_secondary_up(self):
    self.__lsp_forwarding_secondary_up = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-forwarding-secondary-up", rest_name="lsp-forwarding-secondary-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_lsp_forwarding_frr_active(self):
    """
    Getter method for lsp_forwarding_frr_active, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_forwarding_info/lsp_forwarding_frr_active (boolean)

    YANG Description: LSP forwarding state frr detour or backup is active
    """
    return self.__lsp_forwarding_frr_active
      
  def _set_lsp_forwarding_frr_active(self, v, load=False):
    """
    Setter method for lsp_forwarding_frr_active, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_forwarding_info/lsp_forwarding_frr_active (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_forwarding_frr_active is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_forwarding_frr_active() directly.

    YANG Description: LSP forwarding state frr detour or backup is active
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-forwarding-frr-active", rest_name="lsp-forwarding-frr-active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_forwarding_frr_active must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-forwarding-frr-active", rest_name="lsp-forwarding-frr-active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_forwarding_frr_active = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_forwarding_frr_active(self):
    self.__lsp_forwarding_frr_active = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-forwarding-frr-active", rest_name="lsp-forwarding-frr-active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_lsp_forwarding_frr_up(self):
    """
    Getter method for lsp_forwarding_frr_up, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_forwarding_info/lsp_forwarding_frr_up (boolean)

    YANG Description: LSP forwarding state frr detour or backup is up
    """
    return self.__lsp_forwarding_frr_up
      
  def _set_lsp_forwarding_frr_up(self, v, load=False):
    """
    Setter method for lsp_forwarding_frr_up, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_forwarding_info/lsp_forwarding_frr_up (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_forwarding_frr_up is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_forwarding_frr_up() directly.

    YANG Description: LSP forwarding state frr detour or backup is up
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-forwarding-frr-up", rest_name="lsp-forwarding-frr-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_forwarding_frr_up must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-forwarding-frr-up", rest_name="lsp-forwarding-frr-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_forwarding_frr_up = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_forwarding_frr_up(self):
    self.__lsp_forwarding_frr_up = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-forwarding-frr-up", rest_name="lsp-forwarding-frr-up", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_lsp_forwarding_out_port_id(self):
    """
    Getter method for lsp_forwarding_out_port_id, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_forwarding_info/lsp_forwarding_out_port_id (uint32)

    YANG Description: LSP outgoing port id
    """
    return self.__lsp_forwarding_out_port_id
      
  def _set_lsp_forwarding_out_port_id(self, v, load=False):
    """
    Setter method for lsp_forwarding_out_port_id, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_forwarding_info/lsp_forwarding_out_port_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_forwarding_out_port_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_forwarding_out_port_id() directly.

    YANG Description: LSP outgoing port id
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lsp-forwarding-out-port-id", rest_name="lsp-forwarding-out-port-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_forwarding_out_port_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lsp-forwarding-out-port-id", rest_name="lsp-forwarding-out-port-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__lsp_forwarding_out_port_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_forwarding_out_port_id(self):
    self.__lsp_forwarding_out_port_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lsp-forwarding-out-port-id", rest_name="lsp-forwarding-out-port-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_lsp_forwarding_out_port_name(self):
    """
    Getter method for lsp_forwarding_out_port_name, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_forwarding_info/lsp_forwarding_out_port_name (string)

    YANG Description: LSP outgoing port name
    """
    return self.__lsp_forwarding_out_port_name
      
  def _set_lsp_forwarding_out_port_name(self, v, load=False):
    """
    Setter method for lsp_forwarding_out_port_name, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_forwarding_info/lsp_forwarding_out_port_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_forwarding_out_port_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_forwarding_out_port_name() directly.

    YANG Description: LSP outgoing port name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="lsp-forwarding-out-port-name", rest_name="lsp-forwarding-out-port-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_forwarding_out_port_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="lsp-forwarding-out-port-name", rest_name="lsp-forwarding-out-port-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__lsp_forwarding_out_port_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_forwarding_out_port_name(self):
    self.__lsp_forwarding_out_port_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="lsp-forwarding-out-port-name", rest_name="lsp-forwarding-out-port-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_lsp_forwarding_out_label(self):
    """
    Getter method for lsp_forwarding_out_label, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_forwarding_info/lsp_forwarding_out_label (uint32)

    YANG Description: LSP path outgoing label
    """
    return self.__lsp_forwarding_out_label
      
  def _set_lsp_forwarding_out_label(self, v, load=False):
    """
    Setter method for lsp_forwarding_out_label, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_forwarding_info/lsp_forwarding_out_label (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_forwarding_out_label is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_forwarding_out_label() directly.

    YANG Description: LSP path outgoing label
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lsp-forwarding-out-label", rest_name="lsp-forwarding-out-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_forwarding_out_label must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lsp-forwarding-out-label", rest_name="lsp-forwarding-out-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__lsp_forwarding_out_label = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_forwarding_out_label(self):
    self.__lsp_forwarding_out_label = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lsp-forwarding-out-label", rest_name="lsp-forwarding-out-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

  lsp_forwarding_primary_active = __builtin__.property(_get_lsp_forwarding_primary_active, _set_lsp_forwarding_primary_active)
  lsp_forwarding_primary_up = __builtin__.property(_get_lsp_forwarding_primary_up, _set_lsp_forwarding_primary_up)
  lsp_forwarding_secondary_active = __builtin__.property(_get_lsp_forwarding_secondary_active, _set_lsp_forwarding_secondary_active)
  lsp_forwarding_secondary_up = __builtin__.property(_get_lsp_forwarding_secondary_up, _set_lsp_forwarding_secondary_up)
  lsp_forwarding_frr_active = __builtin__.property(_get_lsp_forwarding_frr_active, _set_lsp_forwarding_frr_active)
  lsp_forwarding_frr_up = __builtin__.property(_get_lsp_forwarding_frr_up, _set_lsp_forwarding_frr_up)
  lsp_forwarding_out_port_id = __builtin__.property(_get_lsp_forwarding_out_port_id, _set_lsp_forwarding_out_port_id)
  lsp_forwarding_out_port_name = __builtin__.property(_get_lsp_forwarding_out_port_name, _set_lsp_forwarding_out_port_name)
  lsp_forwarding_out_label = __builtin__.property(_get_lsp_forwarding_out_label, _set_lsp_forwarding_out_label)


  _pyangbind_elements = {'lsp_forwarding_primary_active': lsp_forwarding_primary_active, 'lsp_forwarding_primary_up': lsp_forwarding_primary_up, 'lsp_forwarding_secondary_active': lsp_forwarding_secondary_active, 'lsp_forwarding_secondary_up': lsp_forwarding_secondary_up, 'lsp_forwarding_frr_active': lsp_forwarding_frr_active, 'lsp_forwarding_frr_up': lsp_forwarding_frr_up, 'lsp_forwarding_out_port_id': lsp_forwarding_out_port_id, 'lsp_forwarding_out_port_name': lsp_forwarding_out_port_name, 'lsp_forwarding_out_label': lsp_forwarding_out_label, }


