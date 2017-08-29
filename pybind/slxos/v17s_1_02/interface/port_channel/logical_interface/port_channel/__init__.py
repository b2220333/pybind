
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import pc_cmd_container_dummy
class port_channel(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/port-channel/logical-interface/port-channel. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__pc_instance_id','__pc_cmd_container_dummy',)

  _yang_name = 'port-channel'
  _rest_name = 'port-channel'

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
    self.__pc_cmd_container_dummy = YANGDynClass(base=pc_cmd_container_dummy.pc_cmd_container_dummy, is_container='container', presence=False, yang_name="pc-cmd-container-dummy", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='container', is_config=True)
    self.__pc_instance_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-6][0-9][0-9][0-9])\\.([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9]|1[0-1][0-9][0-9][0-9]|12[0-1][0-9][0-9]|122[0-7][0-9]|1228[0-8]))'}), is_leaf=True, yang_name="pc-instance-id", rest_name="pc-instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='lif-port-channel-type', is_config=True)

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
      return [u'interface', u'port-channel', u'logical-interface', u'port-channel']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Port-channel', u'logical-interface', u'port-channel']

  def _get_pc_instance_id(self):
    """
    Getter method for pc_instance_id, mapped from YANG variable /interface/port_channel/logical_interface/port_channel/pc_instance_id (lif-port-channel-type)
    """
    return self.__pc_instance_id
      
  def _set_pc_instance_id(self, v, load=False):
    """
    Setter method for pc_instance_id, mapped from YANG variable /interface/port_channel/logical_interface/port_channel/pc_instance_id (lif-port-channel-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pc_instance_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pc_instance_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-6][0-9][0-9][0-9])\\.([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9]|1[0-1][0-9][0-9][0-9]|12[0-1][0-9][0-9]|122[0-7][0-9]|1228[0-8]))'}), is_leaf=True, yang_name="pc-instance-id", rest_name="pc-instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='lif-port-channel-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pc_instance_id must be of a type compatible with lif-port-channel-type""",
          'defined-type': "brocade-lif:lif-port-channel-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-6][0-9][0-9][0-9])\\.([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9]|1[0-1][0-9][0-9][0-9]|12[0-1][0-9][0-9]|122[0-7][0-9]|1228[0-8]))'}), is_leaf=True, yang_name="pc-instance-id", rest_name="pc-instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='lif-port-channel-type', is_config=True)""",
        })

    self.__pc_instance_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pc_instance_id(self):
    self.__pc_instance_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-6][0-9][0-9][0-9])\\.([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9]|1[0-1][0-9][0-9][0-9]|12[0-1][0-9][0-9]|122[0-7][0-9]|1228[0-8]))'}), is_leaf=True, yang_name="pc-instance-id", rest_name="pc-instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='lif-port-channel-type', is_config=True)


  def _get_pc_cmd_container_dummy(self):
    """
    Getter method for pc_cmd_container_dummy, mapped from YANG variable /interface/port_channel/logical_interface/port_channel/pc_cmd_container_dummy (container)
    """
    return self.__pc_cmd_container_dummy
      
  def _set_pc_cmd_container_dummy(self, v, load=False):
    """
    Setter method for pc_cmd_container_dummy, mapped from YANG variable /interface/port_channel/logical_interface/port_channel/pc_cmd_container_dummy (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pc_cmd_container_dummy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pc_cmd_container_dummy() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=pc_cmd_container_dummy.pc_cmd_container_dummy, is_container='container', presence=False, yang_name="pc-cmd-container-dummy", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pc_cmd_container_dummy must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=pc_cmd_container_dummy.pc_cmd_container_dummy, is_container='container', presence=False, yang_name="pc-cmd-container-dummy", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='container', is_config=True)""",
        })

    self.__pc_cmd_container_dummy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pc_cmd_container_dummy(self):
    self.__pc_cmd_container_dummy = YANGDynClass(base=pc_cmd_container_dummy.pc_cmd_container_dummy, is_container='container', presence=False, yang_name="pc-cmd-container-dummy", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='container', is_config=True)

  pc_instance_id = __builtin__.property(_get_pc_instance_id, _set_pc_instance_id)
  pc_cmd_container_dummy = __builtin__.property(_get_pc_cmd_container_dummy, _set_pc_cmd_container_dummy)


  _pyangbind_elements = {'pc_instance_id': pc_instance_id, 'pc_cmd_container_dummy': pc_cmd_container_dummy, }

