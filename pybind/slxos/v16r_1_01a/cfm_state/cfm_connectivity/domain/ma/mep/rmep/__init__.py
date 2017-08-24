
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class rmep(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-dot1ag-operational - based on the path /cfm-state/cfm-connectivity/domain/ma/mep/rmep. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: RMEP Details
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__rmep_id','__rmep_mac','__vlan_id','__rmep_port','__rmep_state',)

  _yang_name = 'rmep'
  _rest_name = 'rmep'

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
    self.__rmep_state = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="rmep-state", rest_name="rmep-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint8', is_config=False)
    self.__rmep_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="rmep-id", rest_name="rmep-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint16', is_config=False)
    self.__rmep_mac = YANGDynClass(base=unicode, is_leaf=True, yang_name="rmep-mac", rest_name="rmep-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)
    self.__rmep_port = YANGDynClass(base=unicode, is_leaf=True, yang_name="rmep-port", rest_name="rmep-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)

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
      return [u'cfm-state', u'cfm-connectivity', u'domain', u'ma', u'mep', u'rmep']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'cfm-state', u'cfm-connectivity', u'domain', u'ma', u'mep', u'rmep']

  def _get_rmep_id(self):
    """
    Getter method for rmep_id, mapped from YANG variable /cfm_state/cfm_connectivity/domain/ma/mep/rmep/rmep_id (uint16)

    YANG Description: rmep id
    """
    return self.__rmep_id
      
  def _set_rmep_id(self, v, load=False):
    """
    Setter method for rmep_id, mapped from YANG variable /cfm_state/cfm_connectivity/domain/ma/mep/rmep/rmep_id (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rmep_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rmep_id() directly.

    YANG Description: rmep id
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="rmep-id", rest_name="rmep-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rmep_id must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="rmep-id", rest_name="rmep-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint16', is_config=False)""",
        })

    self.__rmep_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rmep_id(self):
    self.__rmep_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="rmep-id", rest_name="rmep-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint16', is_config=False)


  def _get_rmep_mac(self):
    """
    Getter method for rmep_mac, mapped from YANG variable /cfm_state/cfm_connectivity/domain/ma/mep/rmep/rmep_mac (string)

    YANG Description: RMEP MAC
    """
    return self.__rmep_mac
      
  def _set_rmep_mac(self, v, load=False):
    """
    Setter method for rmep_mac, mapped from YANG variable /cfm_state/cfm_connectivity/domain/ma/mep/rmep/rmep_mac (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rmep_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rmep_mac() directly.

    YANG Description: RMEP MAC
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="rmep-mac", rest_name="rmep-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rmep_mac must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="rmep-mac", rest_name="rmep-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)""",
        })

    self.__rmep_mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rmep_mac(self):
    self.__rmep_mac = YANGDynClass(base=unicode, is_leaf=True, yang_name="rmep-mac", rest_name="rmep-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)


  def _get_vlan_id(self):
    """
    Getter method for vlan_id, mapped from YANG variable /cfm_state/cfm_connectivity/domain/ma/mep/rmep/vlan_id (uint32)

    YANG Description: VLAN Id
    """
    return self.__vlan_id
      
  def _set_vlan_id(self, v, load=False):
    """
    Setter method for vlan_id, mapped from YANG variable /cfm_state/cfm_connectivity/domain/ma/mep/rmep/vlan_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_id() directly.

    YANG Description: VLAN Id
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)""",
        })

    self.__vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_id(self):
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)


  def _get_rmep_port(self):
    """
    Getter method for rmep_port, mapped from YANG variable /cfm_state/cfm_connectivity/domain/ma/mep/rmep/rmep_port (string)

    YANG Description: RMEP Port
    """
    return self.__rmep_port
      
  def _set_rmep_port(self, v, load=False):
    """
    Setter method for rmep_port, mapped from YANG variable /cfm_state/cfm_connectivity/domain/ma/mep/rmep/rmep_port (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rmep_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rmep_port() directly.

    YANG Description: RMEP Port
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="rmep-port", rest_name="rmep-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rmep_port must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="rmep-port", rest_name="rmep-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)""",
        })

    self.__rmep_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rmep_port(self):
    self.__rmep_port = YANGDynClass(base=unicode, is_leaf=True, yang_name="rmep-port", rest_name="rmep-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)


  def _get_rmep_state(self):
    """
    Getter method for rmep_state, mapped from YANG variable /cfm_state/cfm_connectivity/domain/ma/mep/rmep/rmep_state (uint8)

    YANG Description: RMEP State
    """
    return self.__rmep_state
      
  def _set_rmep_state(self, v, load=False):
    """
    Setter method for rmep_state, mapped from YANG variable /cfm_state/cfm_connectivity/domain/ma/mep/rmep/rmep_state (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rmep_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rmep_state() directly.

    YANG Description: RMEP State
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="rmep-state", rest_name="rmep-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rmep_state must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="rmep-state", rest_name="rmep-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint8', is_config=False)""",
        })

    self.__rmep_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rmep_state(self):
    self.__rmep_state = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="rmep-state", rest_name="rmep-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint8', is_config=False)

  rmep_id = __builtin__.property(_get_rmep_id)
  rmep_mac = __builtin__.property(_get_rmep_mac)
  vlan_id = __builtin__.property(_get_vlan_id)
  rmep_port = __builtin__.property(_get_rmep_port)
  rmep_state = __builtin__.property(_get_rmep_state)


  _pyangbind_elements = {'rmep_id': rmep_id, 'rmep_mac': rmep_mac, 'vlan_id': vlan_id, 'rmep_port': rmep_port, 'rmep_state': rmep_state, }


