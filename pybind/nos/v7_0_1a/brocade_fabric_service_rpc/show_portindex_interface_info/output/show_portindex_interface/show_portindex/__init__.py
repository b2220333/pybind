
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class show_portindex(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-fabric-service - based on the path /brocade_fabric_service_rpc/show-portindex-interface-info/output/show-portindex-interface/show-portindex. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__port_index','__port_type','__port_interface',)

  _yang_name = 'show-portindex'
  _rest_name = 'show-portindex'

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
    self.__port_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="port-index", rest_name="port-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The port index of the RBridge'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='uint32', is_config=True)
    self.__port_interface = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="port-interface", rest_name="port-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Port index interface representation'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='interface:interface-type', is_config=True)
    self.__port_type = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'Te|FCOE', 'length': [u'0..4']}), is_leaf=True, yang_name="port-type", rest_name="port-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The port type'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='ethernet-port-type', is_config=True)

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
      return [u'brocade_fabric_service_rpc', u'show-portindex-interface-info', u'output', u'show-portindex-interface', u'show-portindex']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-portindex-interface-info', u'output', u'show-portindex-interface', u'show-portindex']

  def _get_port_index(self):
    """
    Getter method for port_index, mapped from YANG variable /brocade_fabric_service_rpc/show_portindex_interface_info/output/show_portindex_interface/show_portindex/port_index (uint32)

    YANG Description: The port index of the RBridge.
    """
    return self.__port_index
      
  def _set_port_index(self, v, load=False):
    """
    Setter method for port_index, mapped from YANG variable /brocade_fabric_service_rpc/show_portindex_interface_info/output/show_portindex_interface/show_portindex/port_index (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_index() directly.

    YANG Description: The port index of the RBridge.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="port-index", rest_name="port-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The port index of the RBridge'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_index must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="port-index", rest_name="port-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The port index of the RBridge'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='uint32', is_config=True)""",
        })

    self.__port_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_index(self):
    self.__port_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="port-index", rest_name="port-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The port index of the RBridge'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='uint32', is_config=True)


  def _get_port_type(self):
    """
    Getter method for port_type, mapped from YANG variable /brocade_fabric_service_rpc/show_portindex_interface_info/output/show_portindex_interface/show_portindex/port_type (ethernet-port-type)

    YANG Description: The port type of the RBridge.
It can be either Te or FCOE.
Te   - Stands for 10G Physical
       Ethernet ports.
FCOE - Stands for Fibre Channel over
       Ethernet ports.
    """
    return self.__port_type
      
  def _set_port_type(self, v, load=False):
    """
    Setter method for port_type, mapped from YANG variable /brocade_fabric_service_rpc/show_portindex_interface_info/output/show_portindex_interface/show_portindex/port_type (ethernet-port-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_type() directly.

    YANG Description: The port type of the RBridge.
It can be either Te or FCOE.
Te   - Stands for 10G Physical
       Ethernet ports.
FCOE - Stands for Fibre Channel over
       Ethernet ports.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'Te|FCOE', 'length': [u'0..4']}), is_leaf=True, yang_name="port-type", rest_name="port-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The port type'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='ethernet-port-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_type must be of a type compatible with ethernet-port-type""",
          'defined-type': "brocade-fabric-service:ethernet-port-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'Te|FCOE', 'length': [u'0..4']}), is_leaf=True, yang_name="port-type", rest_name="port-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The port type'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='ethernet-port-type', is_config=True)""",
        })

    self.__port_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_type(self):
    self.__port_type = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'Te|FCOE', 'length': [u'0..4']}), is_leaf=True, yang_name="port-type", rest_name="port-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The port type'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='ethernet-port-type', is_config=True)


  def _get_port_interface(self):
    """
    Getter method for port_interface, mapped from YANG variable /brocade_fabric_service_rpc/show_portindex_interface_info/output/show_portindex_interface/show_portindex/port_interface (interface:interface-type)

    YANG Description: Port index interface representation.
It is represented in the format
Te   - rbridge-id/slot/port
FCOE - vlan-id/rbridge-id/port.
    """
    return self.__port_interface
      
  def _set_port_interface(self, v, load=False):
    """
    Setter method for port_interface, mapped from YANG variable /brocade_fabric_service_rpc/show_portindex_interface_info/output/show_portindex_interface/show_portindex/port_interface (interface:interface-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_interface() directly.

    YANG Description: Port index interface representation.
It is represented in the format
Te   - rbridge-id/slot/port
FCOE - vlan-id/rbridge-id/port.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="port-interface", rest_name="port-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Port index interface representation'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='interface:interface-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_interface must be of a type compatible with interface:interface-type""",
          'defined-type': "interface:interface-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="port-interface", rest_name="port-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Port index interface representation'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='interface:interface-type', is_config=True)""",
        })

    self.__port_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_interface(self):
    self.__port_interface = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="port-interface", rest_name="port-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Port index interface representation'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='interface:interface-type', is_config=True)

  port_index = __builtin__.property(_get_port_index, _set_port_index)
  port_type = __builtin__.property(_get_port_type, _set_port_type)
  port_interface = __builtin__.property(_get_port_interface, _set_port_interface)


  _pyangbind_elements = {'port_index': port_index, 'port_type': port_type, 'port_interface': port_interface, }


