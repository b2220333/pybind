
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class vlan_label_info(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-l2sys-operational - based on the path /mct-l2ys-state/show-cluster-mem-vlan/vlan-label-info. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Vlan Label Info
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vlan_id','__unicast_label_local','__unicast_label_remote','__fw_state',)

  _yang_name = 'vlan-label-info'
  _rest_name = 'vlan-label-info'

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
    self.__unicast_label_remote = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="unicast-label-remote", rest_name="unicast-label-remote", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='uint32', is_config=False)
    self.__fw_state = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fw-state", rest_name="fw-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='boolean', is_config=False)
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='uint32', is_config=False)
    self.__unicast_label_local = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="unicast-label-local", rest_name="unicast-label-local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='uint32', is_config=False)

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
      return [u'mct-l2ys-state', u'show-cluster-mem-vlan', u'vlan-label-info']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mct-l2ys-state', u'show-cluster-mem-vlan', u'vlan-label-info']

  def _get_vlan_id(self):
    """
    Getter method for vlan_id, mapped from YANG variable /mct_l2ys_state/show_cluster_mem_vlan/vlan_label_info/vlan_id (uint32)

    YANG Description: Vlan Id
    """
    return self.__vlan_id
      
  def _set_vlan_id(self, v, load=False):
    """
    Setter method for vlan_id, mapped from YANG variable /mct_l2ys_state/show_cluster_mem_vlan/vlan_label_info/vlan_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_id() directly.

    YANG Description: Vlan Id
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='uint32', is_config=False)""",
        })

    self.__vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_id(self):
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='uint32', is_config=False)


  def _get_unicast_label_local(self):
    """
    Getter method for unicast_label_local, mapped from YANG variable /mct_l2ys_state/show_cluster_mem_vlan/vlan_label_info/unicast_label_local (uint32)

    YANG Description: Unicast Local Label
    """
    return self.__unicast_label_local
      
  def _set_unicast_label_local(self, v, load=False):
    """
    Setter method for unicast_label_local, mapped from YANG variable /mct_l2ys_state/show_cluster_mem_vlan/vlan_label_info/unicast_label_local (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unicast_label_local is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unicast_label_local() directly.

    YANG Description: Unicast Local Label
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="unicast-label-local", rest_name="unicast-label-local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unicast_label_local must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="unicast-label-local", rest_name="unicast-label-local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='uint32', is_config=False)""",
        })

    self.__unicast_label_local = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unicast_label_local(self):
    self.__unicast_label_local = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="unicast-label-local", rest_name="unicast-label-local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='uint32', is_config=False)


  def _get_unicast_label_remote(self):
    """
    Getter method for unicast_label_remote, mapped from YANG variable /mct_l2ys_state/show_cluster_mem_vlan/vlan_label_info/unicast_label_remote (uint32)

    YANG Description: Unicast Remote Label
    """
    return self.__unicast_label_remote
      
  def _set_unicast_label_remote(self, v, load=False):
    """
    Setter method for unicast_label_remote, mapped from YANG variable /mct_l2ys_state/show_cluster_mem_vlan/vlan_label_info/unicast_label_remote (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unicast_label_remote is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unicast_label_remote() directly.

    YANG Description: Unicast Remote Label
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="unicast-label-remote", rest_name="unicast-label-remote", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unicast_label_remote must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="unicast-label-remote", rest_name="unicast-label-remote", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='uint32', is_config=False)""",
        })

    self.__unicast_label_remote = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unicast_label_remote(self):
    self.__unicast_label_remote = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="unicast-label-remote", rest_name="unicast-label-remote", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='uint32', is_config=False)


  def _get_fw_state(self):
    """
    Getter method for fw_state, mapped from YANG variable /mct_l2ys_state/show_cluster_mem_vlan/vlan_label_info/fw_state (boolean)

    YANG Description: PW Forwarding State
    """
    return self.__fw_state
      
  def _set_fw_state(self, v, load=False):
    """
    Setter method for fw_state, mapped from YANG variable /mct_l2ys_state/show_cluster_mem_vlan/vlan_label_info/fw_state (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fw_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fw_state() directly.

    YANG Description: PW Forwarding State
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="fw-state", rest_name="fw-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fw_state must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fw-state", rest_name="fw-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='boolean', is_config=False)""",
        })

    self.__fw_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fw_state(self):
    self.__fw_state = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fw-state", rest_name="fw-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='boolean', is_config=False)

  vlan_id = __builtin__.property(_get_vlan_id)
  unicast_label_local = __builtin__.property(_get_unicast_label_local)
  unicast_label_remote = __builtin__.property(_get_unicast_label_remote)
  fw_state = __builtin__.property(_get_fw_state)


  _pyangbind_elements = {'vlan_id': vlan_id, 'unicast_label_local': unicast_label_local, 'unicast_label_remote': unicast_label_remote, 'fw_state': fw_state, }


