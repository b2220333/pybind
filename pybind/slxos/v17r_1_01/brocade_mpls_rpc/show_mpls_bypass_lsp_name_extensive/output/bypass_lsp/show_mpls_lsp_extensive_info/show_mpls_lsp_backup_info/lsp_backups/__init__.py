
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class lsp_backups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-bypass-lsp-name-extensive/output/bypass-lsp/show-mpls-lsp-extensive-info/show-mpls-lsp-backup-info/lsp-backups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__lsp_backup_from_address','__lsp_backup_to_address','__lsp_backup_name','__lsp_backup_type_ingress','__lsp_backup_type_transit','__lsp_backup_is_active',)

  _yang_name = 'lsp-backups'
  _rest_name = 'lsp-backups'

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
    self.__lsp_backup_is_active = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-backup-is-active", rest_name="lsp-backup-is-active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__lsp_backup_type_transit = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-backup-type-transit", rest_name="lsp-backup-type-transit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__lsp_backup_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="lsp-backup-name", rest_name="lsp-backup-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__lsp_backup_from_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="lsp-backup-from-address", rest_name="lsp-backup-from-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    self.__lsp_backup_to_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="lsp-backup-to-address", rest_name="lsp-backup-to-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    self.__lsp_backup_type_ingress = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-backup-type-ingress", rest_name="lsp-backup-type-ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-bypass-lsp-name-extensive', u'output', u'bypass-lsp', u'show-mpls-lsp-extensive-info', u'show-mpls-lsp-backup-info', u'lsp-backups']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-bypass-lsp-name-extensive', u'output', u'bypass-lsp', u'lsp-backups']

  def _get_lsp_backup_from_address(self):
    """
    Getter method for lsp_backup_from_address, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_backup_info/lsp_backups/lsp_backup_from_address (inet:ipv4-address)

    YANG Description: Backup from address
    """
    return self.__lsp_backup_from_address
      
  def _set_lsp_backup_from_address(self, v, load=False):
    """
    Setter method for lsp_backup_from_address, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_backup_info/lsp_backups/lsp_backup_from_address (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_backup_from_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_backup_from_address() directly.

    YANG Description: Backup from address
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="lsp-backup-from-address", rest_name="lsp-backup-from-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_backup_from_address must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="lsp-backup-from-address", rest_name="lsp-backup-from-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__lsp_backup_from_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_backup_from_address(self):
    self.__lsp_backup_from_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="lsp-backup-from-address", rest_name="lsp-backup-from-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)


  def _get_lsp_backup_to_address(self):
    """
    Getter method for lsp_backup_to_address, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_backup_info/lsp_backups/lsp_backup_to_address (inet:ipv4-address)

    YANG Description: Backup to address
    """
    return self.__lsp_backup_to_address
      
  def _set_lsp_backup_to_address(self, v, load=False):
    """
    Setter method for lsp_backup_to_address, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_backup_info/lsp_backups/lsp_backup_to_address (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_backup_to_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_backup_to_address() directly.

    YANG Description: Backup to address
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="lsp-backup-to-address", rest_name="lsp-backup-to-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_backup_to_address must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="lsp-backup-to-address", rest_name="lsp-backup-to-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__lsp_backup_to_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_backup_to_address(self):
    self.__lsp_backup_to_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="lsp-backup-to-address", rest_name="lsp-backup-to-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)


  def _get_lsp_backup_name(self):
    """
    Getter method for lsp_backup_name, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_backup_info/lsp_backups/lsp_backup_name (string)

    YANG Description: Backup name
    """
    return self.__lsp_backup_name
      
  def _set_lsp_backup_name(self, v, load=False):
    """
    Setter method for lsp_backup_name, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_backup_info/lsp_backups/lsp_backup_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_backup_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_backup_name() directly.

    YANG Description: Backup name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="lsp-backup-name", rest_name="lsp-backup-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_backup_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="lsp-backup-name", rest_name="lsp-backup-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__lsp_backup_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_backup_name(self):
    self.__lsp_backup_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="lsp-backup-name", rest_name="lsp-backup-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_lsp_backup_type_ingress(self):
    """
    Getter method for lsp_backup_type_ingress, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_backup_info/lsp_backups/lsp_backup_type_ingress (boolean)

    YANG Description: Backup type ingress
    """
    return self.__lsp_backup_type_ingress
      
  def _set_lsp_backup_type_ingress(self, v, load=False):
    """
    Setter method for lsp_backup_type_ingress, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_backup_info/lsp_backups/lsp_backup_type_ingress (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_backup_type_ingress is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_backup_type_ingress() directly.

    YANG Description: Backup type ingress
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-backup-type-ingress", rest_name="lsp-backup-type-ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_backup_type_ingress must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-backup-type-ingress", rest_name="lsp-backup-type-ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_backup_type_ingress = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_backup_type_ingress(self):
    self.__lsp_backup_type_ingress = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-backup-type-ingress", rest_name="lsp-backup-type-ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_lsp_backup_type_transit(self):
    """
    Getter method for lsp_backup_type_transit, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_backup_info/lsp_backups/lsp_backup_type_transit (boolean)

    YANG Description: Backup type transit
    """
    return self.__lsp_backup_type_transit
      
  def _set_lsp_backup_type_transit(self, v, load=False):
    """
    Setter method for lsp_backup_type_transit, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_backup_info/lsp_backups/lsp_backup_type_transit (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_backup_type_transit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_backup_type_transit() directly.

    YANG Description: Backup type transit
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-backup-type-transit", rest_name="lsp-backup-type-transit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_backup_type_transit must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-backup-type-transit", rest_name="lsp-backup-type-transit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_backup_type_transit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_backup_type_transit(self):
    self.__lsp_backup_type_transit = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-backup-type-transit", rest_name="lsp-backup-type-transit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_lsp_backup_is_active(self):
    """
    Getter method for lsp_backup_is_active, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_backup_info/lsp_backups/lsp_backup_is_active (boolean)

    YANG Description: Backup state is active or up
    """
    return self.__lsp_backup_is_active
      
  def _set_lsp_backup_is_active(self, v, load=False):
    """
    Setter method for lsp_backup_is_active, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_backup_info/lsp_backups/lsp_backup_is_active (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_backup_is_active is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_backup_is_active() directly.

    YANG Description: Backup state is active or up
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="lsp-backup-is-active", rest_name="lsp-backup-is-active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_backup_is_active must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-backup-is-active", rest_name="lsp-backup-is-active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__lsp_backup_is_active = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_backup_is_active(self):
    self.__lsp_backup_is_active = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="lsp-backup-is-active", rest_name="lsp-backup-is-active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)

  lsp_backup_from_address = __builtin__.property(_get_lsp_backup_from_address, _set_lsp_backup_from_address)
  lsp_backup_to_address = __builtin__.property(_get_lsp_backup_to_address, _set_lsp_backup_to_address)
  lsp_backup_name = __builtin__.property(_get_lsp_backup_name, _set_lsp_backup_name)
  lsp_backup_type_ingress = __builtin__.property(_get_lsp_backup_type_ingress, _set_lsp_backup_type_ingress)
  lsp_backup_type_transit = __builtin__.property(_get_lsp_backup_type_transit, _set_lsp_backup_type_transit)
  lsp_backup_is_active = __builtin__.property(_get_lsp_backup_is_active, _set_lsp_backup_is_active)


  _pyangbind_elements = {'lsp_backup_from_address': lsp_backup_from_address, 'lsp_backup_to_address': lsp_backup_to_address, 'lsp_backup_name': lsp_backup_name, 'lsp_backup_type_ingress': lsp_backup_type_ingress, 'lsp_backup_type_transit': lsp_backup_type_transit, 'lsp_backup_is_active': lsp_backup_is_active, }


