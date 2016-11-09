
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class input(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-trilloam - based on the path /brocade_trilloam_rpc/l2traceroute/input. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__src_mac','__dest_mac','__vlan_id','__rbridge_id','__src_ip','__dest_ip','__l4protocol','__l4_src_port','__l4_dest_port',)

  _yang_name = 'input'
  _rest_name = 'input'

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
    self.__rbridge_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..239']}), is_leaf=True, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Syntax: rbridge-id [rbridge-id]'}}, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='common-def:rbridge-id-type', is_config=True)
    self.__l4_src_port = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="l4-src-port", rest_name="l4-src-port", parent=self, choice=(u'protocolType', u'IP'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='inet:port-number', is_config=True)
    self.__src_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="src-ip", rest_name="src-ip", parent=self, choice=(u'protocolType', u'IP'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='inet:ipv4-address', is_config=True)
    self.__dest_mac = YANGDynClass(base=unicode, is_leaf=True, yang_name="dest-mac", rest_name="dest-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='mac:mac-address-type', is_config=True)
    self.__l4protocol = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'UDP': {'value': 2}, u'TCP': {'value': 1}},), is_leaf=True, yang_name="l4protocol", rest_name="l4protocol", parent=self, choice=(u'protocolType', u'IP'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='enumeration', is_config=True)
    self.__l4_dest_port = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="l4-dest-port", rest_name="l4-dest-port", parent=self, choice=(u'protocolType', u'IP'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='inet:port-number', is_config=True)
    self.__src_mac = YANGDynClass(base=unicode, is_leaf=True, yang_name="src-mac", rest_name="src-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='mac:mac-address-type', is_config=True)
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='interface:vlan-type', is_config=True)
    self.__dest_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="dest-ip", rest_name="dest-ip", parent=self, choice=(u'protocolType', u'IP'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='inet:ipv4-address', is_config=True)

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
      return [u'brocade_trilloam_rpc', u'l2traceroute', u'input']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'l2traceroute', u'input']

  def _get_src_mac(self):
    """
    Getter method for src_mac, mapped from YANG variable /brocade_trilloam_rpc/l2traceroute/input/src_mac (mac:mac-address-type)

    YANG Description: Source mac address of the host
    """
    return self.__src_mac
      
  def _set_src_mac(self, v, load=False):
    """
    Setter method for src_mac, mapped from YANG variable /brocade_trilloam_rpc/l2traceroute/input/src_mac (mac:mac-address-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_src_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_src_mac() directly.

    YANG Description: Source mac address of the host
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="src-mac", rest_name="src-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='mac:mac-address-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """src_mac must be of a type compatible with mac:mac-address-type""",
          'defined-type': "mac:mac-address-type",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="src-mac", rest_name="src-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='mac:mac-address-type', is_config=True)""",
        })

    self.__src_mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_src_mac(self):
    self.__src_mac = YANGDynClass(base=unicode, is_leaf=True, yang_name="src-mac", rest_name="src-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='mac:mac-address-type', is_config=True)


  def _get_dest_mac(self):
    """
    Getter method for dest_mac, mapped from YANG variable /brocade_trilloam_rpc/l2traceroute/input/dest_mac (mac:mac-address-type)

    YANG Description: Destination mac address of the host
    """
    return self.__dest_mac
      
  def _set_dest_mac(self, v, load=False):
    """
    Setter method for dest_mac, mapped from YANG variable /brocade_trilloam_rpc/l2traceroute/input/dest_mac (mac:mac-address-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dest_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dest_mac() directly.

    YANG Description: Destination mac address of the host
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="dest-mac", rest_name="dest-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='mac:mac-address-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dest_mac must be of a type compatible with mac:mac-address-type""",
          'defined-type': "mac:mac-address-type",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="dest-mac", rest_name="dest-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='mac:mac-address-type', is_config=True)""",
        })

    self.__dest_mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dest_mac(self):
    self.__dest_mac = YANGDynClass(base=unicode, is_leaf=True, yang_name="dest-mac", rest_name="dest-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='mac:mac-address-type', is_config=True)


  def _get_vlan_id(self):
    """
    Getter method for vlan_id, mapped from YANG variable /brocade_trilloam_rpc/l2traceroute/input/vlan_id (interface:vlan-type)

    YANG Description: VLAN Id
    """
    return self.__vlan_id
      
  def _set_vlan_id(self, v, load=False):
    """
    Setter method for vlan_id, mapped from YANG variable /brocade_trilloam_rpc/l2traceroute/input/vlan_id (interface:vlan-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_id() directly.

    YANG Description: VLAN Id
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='interface:vlan-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_id must be of a type compatible with interface:vlan-type""",
          'defined-type': "interface:vlan-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='interface:vlan-type', is_config=True)""",
        })

    self.__vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_id(self):
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='interface:vlan-type', is_config=True)


  def _get_rbridge_id(self):
    """
    Getter method for rbridge_id, mapped from YANG variable /brocade_trilloam_rpc/l2traceroute/input/rbridge_id (common-def:rbridge-id-type)

    YANG Description: rbridge-id
    """
    return self.__rbridge_id
      
  def _set_rbridge_id(self, v, load=False):
    """
    Setter method for rbridge_id, mapped from YANG variable /brocade_trilloam_rpc/l2traceroute/input/rbridge_id (common-def:rbridge-id-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rbridge_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rbridge_id() directly.

    YANG Description: rbridge-id
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..239']}), is_leaf=True, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Syntax: rbridge-id [rbridge-id]'}}, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='common-def:rbridge-id-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rbridge_id must be of a type compatible with common-def:rbridge-id-type""",
          'defined-type': "common-def:rbridge-id-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..239']}), is_leaf=True, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Syntax: rbridge-id [rbridge-id]'}}, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='common-def:rbridge-id-type', is_config=True)""",
        })

    self.__rbridge_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rbridge_id(self):
    self.__rbridge_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..239']}), is_leaf=True, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Syntax: rbridge-id [rbridge-id]'}}, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='common-def:rbridge-id-type', is_config=True)


  def _get_src_ip(self):
    """
    Getter method for src_ip, mapped from YANG variable /brocade_trilloam_rpc/l2traceroute/input/src_ip (inet:ipv4-address)

    YANG Description: Source IP address
    """
    return self.__src_ip
      
  def _set_src_ip(self, v, load=False):
    """
    Setter method for src_ip, mapped from YANG variable /brocade_trilloam_rpc/l2traceroute/input/src_ip (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_src_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_src_ip() directly.

    YANG Description: Source IP address
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="src-ip", rest_name="src-ip", parent=self, choice=(u'protocolType', u'IP'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """src_ip must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="src-ip", rest_name="src-ip", parent=self, choice=(u'protocolType', u'IP'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__src_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_src_ip(self):
    self.__src_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="src-ip", rest_name="src-ip", parent=self, choice=(u'protocolType', u'IP'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='inet:ipv4-address', is_config=True)


  def _get_dest_ip(self):
    """
    Getter method for dest_ip, mapped from YANG variable /brocade_trilloam_rpc/l2traceroute/input/dest_ip (inet:ipv4-address)

    YANG Description: Destination IP address
    """
    return self.__dest_ip
      
  def _set_dest_ip(self, v, load=False):
    """
    Setter method for dest_ip, mapped from YANG variable /brocade_trilloam_rpc/l2traceroute/input/dest_ip (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dest_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dest_ip() directly.

    YANG Description: Destination IP address
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="dest-ip", rest_name="dest-ip", parent=self, choice=(u'protocolType', u'IP'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dest_ip must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="dest-ip", rest_name="dest-ip", parent=self, choice=(u'protocolType', u'IP'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__dest_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dest_ip(self):
    self.__dest_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="dest-ip", rest_name="dest-ip", parent=self, choice=(u'protocolType', u'IP'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='inet:ipv4-address', is_config=True)


  def _get_l4protocol(self):
    """
    Getter method for l4protocol, mapped from YANG variable /brocade_trilloam_rpc/l2traceroute/input/l4protocol (enumeration)

    YANG Description: Layer 4 protocol, TCP or UDP
    """
    return self.__l4protocol
      
  def _set_l4protocol(self, v, load=False):
    """
    Setter method for l4protocol, mapped from YANG variable /brocade_trilloam_rpc/l2traceroute/input/l4protocol (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_l4protocol is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_l4protocol() directly.

    YANG Description: Layer 4 protocol, TCP or UDP
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'UDP': {'value': 2}, u'TCP': {'value': 1}},), is_leaf=True, yang_name="l4protocol", rest_name="l4protocol", parent=self, choice=(u'protocolType', u'IP'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """l4protocol must be of a type compatible with enumeration""",
          'defined-type': "brocade-trilloam:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'UDP': {'value': 2}, u'TCP': {'value': 1}},), is_leaf=True, yang_name="l4protocol", rest_name="l4protocol", parent=self, choice=(u'protocolType', u'IP'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='enumeration', is_config=True)""",
        })

    self.__l4protocol = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_l4protocol(self):
    self.__l4protocol = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'UDP': {'value': 2}, u'TCP': {'value': 1}},), is_leaf=True, yang_name="l4protocol", rest_name="l4protocol", parent=self, choice=(u'protocolType', u'IP'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='enumeration', is_config=True)


  def _get_l4_src_port(self):
    """
    Getter method for l4_src_port, mapped from YANG variable /brocade_trilloam_rpc/l2traceroute/input/l4_src_port (inet:port-number)

    YANG Description: Source port number for the l4protocol
    """
    return self.__l4_src_port
      
  def _set_l4_src_port(self, v, load=False):
    """
    Setter method for l4_src_port, mapped from YANG variable /brocade_trilloam_rpc/l2traceroute/input/l4_src_port (inet:port-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_l4_src_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_l4_src_port() directly.

    YANG Description: Source port number for the l4protocol
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="l4-src-port", rest_name="l4-src-port", parent=self, choice=(u'protocolType', u'IP'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='inet:port-number', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """l4_src_port must be of a type compatible with inet:port-number""",
          'defined-type': "inet:port-number",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="l4-src-port", rest_name="l4-src-port", parent=self, choice=(u'protocolType', u'IP'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='inet:port-number', is_config=True)""",
        })

    self.__l4_src_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_l4_src_port(self):
    self.__l4_src_port = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="l4-src-port", rest_name="l4-src-port", parent=self, choice=(u'protocolType', u'IP'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='inet:port-number', is_config=True)


  def _get_l4_dest_port(self):
    """
    Getter method for l4_dest_port, mapped from YANG variable /brocade_trilloam_rpc/l2traceroute/input/l4_dest_port (inet:port-number)

    YANG Description: Destination port number for l4protocol
    """
    return self.__l4_dest_port
      
  def _set_l4_dest_port(self, v, load=False):
    """
    Setter method for l4_dest_port, mapped from YANG variable /brocade_trilloam_rpc/l2traceroute/input/l4_dest_port (inet:port-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_l4_dest_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_l4_dest_port() directly.

    YANG Description: Destination port number for l4protocol
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="l4-dest-port", rest_name="l4-dest-port", parent=self, choice=(u'protocolType', u'IP'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='inet:port-number', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """l4_dest_port must be of a type compatible with inet:port-number""",
          'defined-type': "inet:port-number",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="l4-dest-port", rest_name="l4-dest-port", parent=self, choice=(u'protocolType', u'IP'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='inet:port-number', is_config=True)""",
        })

    self.__l4_dest_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_l4_dest_port(self):
    self.__l4_dest_port = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="l4-dest-port", rest_name="l4-dest-port", parent=self, choice=(u'protocolType', u'IP'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-trilloam', defining_module='brocade-trilloam', yang_type='inet:port-number', is_config=True)

  src_mac = __builtin__.property(_get_src_mac, _set_src_mac)
  dest_mac = __builtin__.property(_get_dest_mac, _set_dest_mac)
  vlan_id = __builtin__.property(_get_vlan_id, _set_vlan_id)
  rbridge_id = __builtin__.property(_get_rbridge_id, _set_rbridge_id)
  src_ip = __builtin__.property(_get_src_ip, _set_src_ip)
  dest_ip = __builtin__.property(_get_dest_ip, _set_dest_ip)
  l4protocol = __builtin__.property(_get_l4protocol, _set_l4protocol)
  l4_src_port = __builtin__.property(_get_l4_src_port, _set_l4_src_port)
  l4_dest_port = __builtin__.property(_get_l4_dest_port, _set_l4_dest_port)

  __choices__ = {u'protocolType': {u'IP': [u'src_ip', u'dest_ip', u'l4protocol', u'l4_src_port', u'l4_dest_port']}}
  _pyangbind_elements = {'src_mac': src_mac, 'dest_mac': dest_mac, 'vlan_id': vlan_id, 'rbridge_id': rbridge_id, 'src_ip': src_ip, 'dest_ip': dest_ip, 'l4protocol': l4protocol, 'l4_src_port': l4_src_port, 'l4_dest_port': l4_dest_port, }


