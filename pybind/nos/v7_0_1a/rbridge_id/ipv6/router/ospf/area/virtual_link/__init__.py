
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import link_properties
class virtual_link(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/ipv6/router/ospf/area/virtual-link. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: All ABRs must have either a direct or indirect link to an OSPF backbone area (0.0.0.0 or 0). If an ABR does not have a physical link to a backbone area, a virtual link can be configured from the ABR to another router within the same area that has a physical connection to the backbone area.The path for a virtual link is through an area shared by the neighbor ABR (router with a physical backbone connection) and the ABR requiring a logical connection to the backbone.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__virtual_link_neighbor','__link_properties',)

  _yang_name = 'virtual-link'
  _rest_name = 'virtual-link'

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
    self.__virtual_link_neighbor = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="virtual-link-neighbor", rest_name="virtual-link-neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='inet:ipv4-address', is_config=True)
    self.__link_properties = YANGDynClass(base=link_properties.link_properties, is_container='container', yang_name="link-properties", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)

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
      return [u'rbridge-id', u'ipv6', u'router', u'ospf', u'area', u'virtual-link']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'ipv6', u'router', u'ospf', u'area', u'virtual-link']

  def _get_virtual_link_neighbor(self):
    """
    Getter method for virtual_link_neighbor, mapped from YANG variable /rbridge_id/ipv6/router/ospf/area/virtual_link/virtual_link_neighbor (inet:ipv4-address)

    YANG Description: The neighbor router is the router ID (IPv4 address) of the router that is physically connected to the backbone when assigned from the router interface requiring a logical connection. The neighbor router is the router ID (IPv4 address) of the router requiring a logical connection to the backbone when assigned from the router interface with the physical connection.
    """
    return self.__virtual_link_neighbor
      
  def _set_virtual_link_neighbor(self, v, load=False):
    """
    Setter method for virtual_link_neighbor, mapped from YANG variable /rbridge_id/ipv6/router/ospf/area/virtual_link/virtual_link_neighbor (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_virtual_link_neighbor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_virtual_link_neighbor() directly.

    YANG Description: The neighbor router is the router ID (IPv4 address) of the router that is physically connected to the backbone when assigned from the router interface requiring a logical connection. The neighbor router is the router ID (IPv4 address) of the router requiring a logical connection to the backbone when assigned from the router interface with the physical connection.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="virtual-link-neighbor", rest_name="virtual-link-neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """virtual_link_neighbor must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="virtual-link-neighbor", rest_name="virtual-link-neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__virtual_link_neighbor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_virtual_link_neighbor(self):
    self.__virtual_link_neighbor = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="virtual-link-neighbor", rest_name="virtual-link-neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='inet:ipv4-address', is_config=True)


  def _get_link_properties(self):
    """
    Getter method for link_properties, mapped from YANG variable /rbridge_id/ipv6/router/ospf/area/virtual_link/link_properties (container)
    """
    return self.__link_properties
      
  def _set_link_properties(self, v, load=False):
    """
    Setter method for link_properties, mapped from YANG variable /rbridge_id/ipv6/router/ospf/area/virtual_link/link_properties (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_properties is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_properties() directly.
    """
    try:
      t = YANGDynClass(v,base=link_properties.link_properties, is_container='container', yang_name="link-properties", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_properties must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=link_properties.link_properties, is_container='container', yang_name="link-properties", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)""",
        })

    self.__link_properties = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_properties(self):
    self.__link_properties = YANGDynClass(base=link_properties.link_properties, is_container='container', yang_name="link-properties", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)

  virtual_link_neighbor = __builtin__.property(_get_virtual_link_neighbor, _set_virtual_link_neighbor)
  link_properties = __builtin__.property(_get_link_properties, _set_link_properties)


  _pyangbind_elements = {'virtual_link_neighbor': virtual_link_neighbor, 'link_properties': link_properties, }


