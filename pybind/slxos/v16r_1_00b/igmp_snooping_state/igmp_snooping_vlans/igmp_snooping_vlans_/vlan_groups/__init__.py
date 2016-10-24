
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class vlan_groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mc-hms-operational - based on the path /igmp-snooping-state/igmp-snooping-vlans/igmp-snooping-vlans/vlan-groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Group information on an interface
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__grp_ip_addr','__member_ports',)

  _yang_name = 'vlan-groups'
  _rest_name = 'vlan-groups'

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
    self.__grp_ip_addr = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="grp-ip-addr", rest_name="grp-ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    self.__member_ports = YANGDynClass(base=unicode, is_leaf=True, yang_name="member-ports", rest_name="member-ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)

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
      return [u'igmp-snooping-state', u'igmp-snooping-vlans', u'igmp-snooping-vlans', u'vlan-groups']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'igmp-snooping-state', u'igmp-snooping-vlans', u'igmp-snooping-vlans', u'vlan-groups']

  def _get_grp_ip_addr(self):
    """
    Getter method for grp_ip_addr, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/vlan_groups/grp_ip_addr (uint32)

    YANG Description: group address
    """
    return self.__grp_ip_addr
      
  def _set_grp_ip_addr(self, v, load=False):
    """
    Setter method for grp_ip_addr, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/vlan_groups/grp_ip_addr (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_grp_ip_addr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_grp_ip_addr() directly.

    YANG Description: group address
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="grp-ip-addr", rest_name="grp-ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """grp_ip_addr must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="grp-ip-addr", rest_name="grp-ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)""",
        })

    self.__grp_ip_addr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_grp_ip_addr(self):
    self.__grp_ip_addr = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="grp-ip-addr", rest_name="grp-ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)


  def _get_member_ports(self):
    """
    Getter method for member_ports, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/vlan_groups/member_ports (string)

    YANG Description: group member ports
    """
    return self.__member_ports
      
  def _set_member_ports(self, v, load=False):
    """
    Setter method for member_ports, mapped from YANG variable /igmp_snooping_state/igmp_snooping_vlans/igmp_snooping_vlans/vlan_groups/member_ports (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_member_ports is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_member_ports() directly.

    YANG Description: group member ports
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="member-ports", rest_name="member-ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """member_ports must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="member-ports", rest_name="member-ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)""",
        })

    self.__member_ports = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_member_ports(self):
    self.__member_ports = YANGDynClass(base=unicode, is_leaf=True, yang_name="member-ports", rest_name="member-ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)

  grp_ip_addr = __builtin__.property(_get_grp_ip_addr)
  member_ports = __builtin__.property(_get_member_ports)


  _pyangbind_elements = {'grp_ip_addr': grp_ip_addr, 'member_ports': member_ports, }


