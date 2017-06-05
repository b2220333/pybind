
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class member_vlan(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-nsm-operational - based on the path /topology-group-state/topology-group-data/member-vlan. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: member vlan info
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vlan_id','__free_ports',)

  _yang_name = 'member-vlan'
  _rest_name = 'member-vlan'

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
    self.__free_ports = YANGDynClass(base=unicode, is_leaf=True, yang_name="free-ports", rest_name="free-ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint16', is_config=False)

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
      return [u'topology-group-state', u'topology-group-data', u'member-vlan']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'topology-group-state', u'topology-group-data', u'member-vlan']

  def _get_vlan_id(self):
    """
    Getter method for vlan_id, mapped from YANG variable /topology_group_state/topology_group_data/member_vlan/vlan_id (uint16)

    YANG Description: member vlan id
    """
    return self.__vlan_id
      
  def _set_vlan_id(self, v, load=False):
    """
    Setter method for vlan_id, mapped from YANG variable /topology_group_state/topology_group_data/member_vlan/vlan_id (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_id() directly.

    YANG Description: member vlan id
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_id must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint16', is_config=False)""",
        })

    self.__vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_id(self):
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint16', is_config=False)


  def _get_free_ports(self):
    """
    Getter method for free_ports, mapped from YANG variable /topology_group_state/topology_group_data/member_vlan/free_ports (string)

    YANG Description: Free ports
    """
    return self.__free_ports
      
  def _set_free_ports(self, v, load=False):
    """
    Setter method for free_ports, mapped from YANG variable /topology_group_state/topology_group_data/member_vlan/free_ports (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_free_ports is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_free_ports() directly.

    YANG Description: Free ports
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="free-ports", rest_name="free-ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """free_ports must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="free-ports", rest_name="free-ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)""",
        })

    self.__free_ports = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_free_ports(self):
    self.__free_ports = YANGDynClass(base=unicode, is_leaf=True, yang_name="free-ports", rest_name="free-ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)

  vlan_id = __builtin__.property(_get_vlan_id)
  free_ports = __builtin__.property(_get_free_ports)


  _pyangbind_elements = {'vlan_id': vlan_id, 'free_ports': free_ports, }


