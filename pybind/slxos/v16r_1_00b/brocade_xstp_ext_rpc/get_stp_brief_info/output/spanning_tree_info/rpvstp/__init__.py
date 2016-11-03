
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import root_bridge
import bridge
import port
class rpvstp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-xstp-ext - based on the path /brocade_xstp_ext_rpc/get-stp-brief-info/output/spanning-tree-info/rpvstp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: RPVST instance information
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vlan_id','__root_bridge','__bridge','__transmit_hold_count','__migrate_time','__port',)

  _yang_name = 'rpvstp'
  _rest_name = 'rpvstp'

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
    self.__bridge = YANGDynClass(base=bridge.bridge, is_container='container', yang_name="bridge", rest_name="bridge", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)
    self.__migrate_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="migrate-time", rest_name="migrate-time", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)
    self.__root_bridge = YANGDynClass(base=root_bridge.root_bridge, is_container='container', yang_name="root-bridge", rest_name="root-bridge", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)
    self.__transmit_hold_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="transmit-hold-count", rest_name="transmit-hold-count", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)
    self.__port = YANGDynClass(base=YANGListType(False,port.port, yang_name="port", rest_name="port", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None, choice=(u'spanning-tree-mode', u'rpvstp')), is_container='list', yang_name="port", rest_name="port", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='list', is_config=True)
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4090']}), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='interface:vlan-type', is_config=True)

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
      return [u'brocade_xstp_ext_rpc', u'get-stp-brief-info', u'output', u'spanning-tree-info', u'rpvstp']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-stp-brief-info', u'output', u'spanning-tree-info', u'rpvstp']

  def _get_vlan_id(self):
    """
    Getter method for vlan_id, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/rpvstp/vlan_id (interface:vlan-type)
    """
    return self.__vlan_id
      
  def _set_vlan_id(self, v, load=False):
    """
    Setter method for vlan_id, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/rpvstp/vlan_id (interface:vlan-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4090']}), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='interface:vlan-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_id must be of a type compatible with interface:vlan-type""",
          'defined-type': "interface:vlan-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4090']}), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='interface:vlan-type', is_config=True)""",
        })

    self.__vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_id(self):
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4090']}), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='interface:vlan-type', is_config=True)


  def _get_root_bridge(self):
    """
    Getter method for root_bridge, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/rpvstp/root_bridge (container)
    """
    return self.__root_bridge
      
  def _set_root_bridge(self, v, load=False):
    """
    Setter method for root_bridge, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/rpvstp/root_bridge (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_root_bridge is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_root_bridge() directly.
    """
    try:
      t = YANGDynClass(v,base=root_bridge.root_bridge, is_container='container', yang_name="root-bridge", rest_name="root-bridge", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """root_bridge must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=root_bridge.root_bridge, is_container='container', yang_name="root-bridge", rest_name="root-bridge", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)""",
        })

    self.__root_bridge = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_root_bridge(self):
    self.__root_bridge = YANGDynClass(base=root_bridge.root_bridge, is_container='container', yang_name="root-bridge", rest_name="root-bridge", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)


  def _get_bridge(self):
    """
    Getter method for bridge, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/rpvstp/bridge (container)
    """
    return self.__bridge
      
  def _set_bridge(self, v, load=False):
    """
    Setter method for bridge, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/rpvstp/bridge (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bridge is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bridge() directly.
    """
    try:
      t = YANGDynClass(v,base=bridge.bridge, is_container='container', yang_name="bridge", rest_name="bridge", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bridge must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=bridge.bridge, is_container='container', yang_name="bridge", rest_name="bridge", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)""",
        })

    self.__bridge = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bridge(self):
    self.__bridge = YANGDynClass(base=bridge.bridge, is_container='container', yang_name="bridge", rest_name="bridge", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)


  def _get_transmit_hold_count(self):
    """
    Getter method for transmit_hold_count, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/rpvstp/transmit_hold_count (uint32)

    YANG Description: Maximum number of Hello packets transmitted per
interval  (1..10)
    """
    return self.__transmit_hold_count
      
  def _set_transmit_hold_count(self, v, load=False):
    """
    Setter method for transmit_hold_count, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/rpvstp/transmit_hold_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_transmit_hold_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_transmit_hold_count() directly.

    YANG Description: Maximum number of Hello packets transmitted per
interval  (1..10)
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="transmit-hold-count", rest_name="transmit-hold-count", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """transmit_hold_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="transmit-hold-count", rest_name="transmit-hold-count", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)""",
        })

    self.__transmit_hold_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_transmit_hold_count(self):
    self.__transmit_hold_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="transmit-hold-count", rest_name="transmit-hold-count", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)


  def _get_migrate_time(self):
    """
    Getter method for migrate_time, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/rpvstp/migrate_time (uint32)

    YANG Description: Bridge migrate time (sec)
    """
    return self.__migrate_time
      
  def _set_migrate_time(self, v, load=False):
    """
    Setter method for migrate_time, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/rpvstp/migrate_time (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_migrate_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_migrate_time() directly.

    YANG Description: Bridge migrate time (sec)
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="migrate-time", rest_name="migrate-time", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """migrate_time must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="migrate-time", rest_name="migrate-time", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)""",
        })

    self.__migrate_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_migrate_time(self):
    self.__migrate_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="migrate-time", rest_name="migrate-time", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)


  def _get_port(self):
    """
    Getter method for port, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/rpvstp/port (list)
    """
    return self.__port
      
  def _set_port(self, v, load=False):
    """
    Setter method for port, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/rpvstp/port (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType(False,port.port, yang_name="port", rest_name="port", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None, choice=(u'spanning-tree-mode', u'rpvstp')), is_container='list', yang_name="port", rest_name="port", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType(False,port.port, yang_name="port", rest_name="port", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None, choice=(u'spanning-tree-mode', u'rpvstp')), is_container='list', yang_name="port", rest_name="port", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='list', is_config=True)""",
        })

    self.__port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port(self):
    self.__port = YANGDynClass(base=YANGListType(False,port.port, yang_name="port", rest_name="port", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None, choice=(u'spanning-tree-mode', u'rpvstp')), is_container='list', yang_name="port", rest_name="port", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='list', is_config=True)

  vlan_id = __builtin__.property(_get_vlan_id, _set_vlan_id)
  root_bridge = __builtin__.property(_get_root_bridge, _set_root_bridge)
  bridge = __builtin__.property(_get_bridge, _set_bridge)
  transmit_hold_count = __builtin__.property(_get_transmit_hold_count, _set_transmit_hold_count)
  migrate_time = __builtin__.property(_get_migrate_time, _set_migrate_time)
  port = __builtin__.property(_get_port, _set_port)

  __choices__ = {u'spanning-tree-mode': {u'rpvstp': [u'vlan_id', u'root_bridge', u'bridge', u'transmit_hold_count', u'migrate_time', u'port']}}
  _pyangbind_elements = {'vlan_id': vlan_id, 'root_bridge': root_bridge, 'bridge': bridge, 'transmit_hold_count': transmit_hold_count, 'migrate_time': migrate_time, 'port': port, }

