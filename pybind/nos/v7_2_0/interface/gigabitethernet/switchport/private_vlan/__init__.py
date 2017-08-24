
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import trunk
import host_association
import association
import mapping
class private_vlan(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/gigabitethernet/switchport/private-vlan. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Set Private-Vlan Configuration
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__trunk','__host_association','__association','__mapping',)

  _yang_name = 'private-vlan'
  _rest_name = 'private-vlan'

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
    self.__mapping = YANGDynClass(base=YANGListType("promis_pri_pvlan",mapping.mapping, yang_name="mapping", rest_name="mapping", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='promis-pri-pvlan', extensions={u'tailf-common': {u'info': u'Promiscuous Mapping', u'cli-suppress-mode': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-incomplete-command': None, u'callpoint': u'pvlanMappingCallPointWorker_te'}}), is_container='list', yang_name="mapping", rest_name="mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Promiscuous Mapping', u'cli-suppress-mode': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-incomplete-command': None, u'callpoint': u'pvlanMappingCallPointWorker_te'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)
    self.__association = YANGDynClass(base=association.association, is_container='container', presence=False, yang_name="association", rest_name="association", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'trunk-association', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_PVLAN_ASSOCIATION'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__host_association = YANGDynClass(base=host_association.host_association, is_container='container', presence=False, yang_name="host-association", rest_name="host-association", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Host-association', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__trunk = YANGDynClass(base=trunk.trunk, is_container='container', presence=False, yang_name="trunk", rest_name="trunk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as trunk', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_PVLAN_TRUNK_NATIVE'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)

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
      return [u'interface', u'gigabitethernet', u'switchport', u'private-vlan']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'GigabitEthernet', u'switchport', u'private-vlan']

  def _get_trunk(self):
    """
    Getter method for trunk, mapped from YANG variable /interface/gigabitethernet/switchport/private_vlan/trunk (container)

    YANG Description: trunk
    """
    return self.__trunk
      
  def _set_trunk(self, v, load=False):
    """
    Setter method for trunk, mapped from YANG variable /interface/gigabitethernet/switchport/private_vlan/trunk (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk() directly.

    YANG Description: trunk
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=trunk.trunk, is_container='container', presence=False, yang_name="trunk", rest_name="trunk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as trunk', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_PVLAN_TRUNK_NATIVE'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=trunk.trunk, is_container='container', presence=False, yang_name="trunk", rest_name="trunk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as trunk', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_PVLAN_TRUNK_NATIVE'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__trunk = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk(self):
    self.__trunk = YANGDynClass(base=trunk.trunk, is_container='container', presence=False, yang_name="trunk", rest_name="trunk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as trunk', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_PVLAN_TRUNK_NATIVE'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_host_association(self):
    """
    Getter method for host_association, mapped from YANG variable /interface/gigabitethernet/switchport/private_vlan/host_association (container)

    YANG Description: Host-association
    """
    return self.__host_association
      
  def _set_host_association(self, v, load=False):
    """
    Setter method for host_association, mapped from YANG variable /interface/gigabitethernet/switchport/private_vlan/host_association (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_host_association is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_host_association() directly.

    YANG Description: Host-association
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=host_association.host_association, is_container='container', presence=False, yang_name="host-association", rest_name="host-association", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Host-association', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """host_association must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=host_association.host_association, is_container='container', presence=False, yang_name="host-association", rest_name="host-association", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Host-association', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__host_association = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_host_association(self):
    self.__host_association = YANGDynClass(base=host_association.host_association, is_container='container', presence=False, yang_name="host-association", rest_name="host-association", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Host-association', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_association(self):
    """
    Getter method for association, mapped from YANG variable /interface/gigabitethernet/switchport/private_vlan/association (container)

    YANG Description: Association
    """
    return self.__association
      
  def _set_association(self, v, load=False):
    """
    Setter method for association, mapped from YANG variable /interface/gigabitethernet/switchport/private_vlan/association (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_association is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_association() directly.

    YANG Description: Association
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=association.association, is_container='container', presence=False, yang_name="association", rest_name="association", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'trunk-association', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_PVLAN_ASSOCIATION'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """association must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=association.association, is_container='container', presence=False, yang_name="association", rest_name="association", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'trunk-association', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_PVLAN_ASSOCIATION'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__association = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_association(self):
    self.__association = YANGDynClass(base=association.association, is_container='container', presence=False, yang_name="association", rest_name="association", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'trunk-association', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_PVLAN_ASSOCIATION'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_mapping(self):
    """
    Getter method for mapping, mapped from YANG variable /interface/gigabitethernet/switchport/private_vlan/mapping (list)

    YANG Description: Promiscuous mapping
    """
    return self.__mapping
      
  def _set_mapping(self, v, load=False):
    """
    Setter method for mapping, mapped from YANG variable /interface/gigabitethernet/switchport/private_vlan/mapping (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mapping is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mapping() directly.

    YANG Description: Promiscuous mapping
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("promis_pri_pvlan",mapping.mapping, yang_name="mapping", rest_name="mapping", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='promis-pri-pvlan', extensions={u'tailf-common': {u'info': u'Promiscuous Mapping', u'cli-suppress-mode': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-incomplete-command': None, u'callpoint': u'pvlanMappingCallPointWorker_te'}}), is_container='list', yang_name="mapping", rest_name="mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Promiscuous Mapping', u'cli-suppress-mode': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-incomplete-command': None, u'callpoint': u'pvlanMappingCallPointWorker_te'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mapping must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("promis_pri_pvlan",mapping.mapping, yang_name="mapping", rest_name="mapping", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='promis-pri-pvlan', extensions={u'tailf-common': {u'info': u'Promiscuous Mapping', u'cli-suppress-mode': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-incomplete-command': None, u'callpoint': u'pvlanMappingCallPointWorker_te'}}), is_container='list', yang_name="mapping", rest_name="mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Promiscuous Mapping', u'cli-suppress-mode': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-incomplete-command': None, u'callpoint': u'pvlanMappingCallPointWorker_te'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)""",
        })

    self.__mapping = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mapping(self):
    self.__mapping = YANGDynClass(base=YANGListType("promis_pri_pvlan",mapping.mapping, yang_name="mapping", rest_name="mapping", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='promis-pri-pvlan', extensions={u'tailf-common': {u'info': u'Promiscuous Mapping', u'cli-suppress-mode': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-incomplete-command': None, u'callpoint': u'pvlanMappingCallPointWorker_te'}}), is_container='list', yang_name="mapping", rest_name="mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Promiscuous Mapping', u'cli-suppress-mode': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-incomplete-command': None, u'callpoint': u'pvlanMappingCallPointWorker_te'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)

  trunk = __builtin__.property(_get_trunk, _set_trunk)
  host_association = __builtin__.property(_get_host_association, _set_host_association)
  association = __builtin__.property(_get_association, _set_association)
  mapping = __builtin__.property(_get_mapping, _set_mapping)


  _pyangbind_elements = {'trunk': trunk, 'host_association': host_association, 'association': association, 'mapping': mapping, }


