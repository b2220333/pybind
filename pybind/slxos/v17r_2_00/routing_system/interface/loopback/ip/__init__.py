
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ip_config
import intf_router_isis
import interface_loopback_ospf_conf
import pim_intf_loopback_cont
class ip(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/interface/loopback/ip. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ip_config','__intf_router_isis','__interface_loopback_ospf_conf','__pim_intf_loopback_cont',)

  _yang_name = 'ip'
  _rest_name = 'ip'

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
    self.__intf_router_isis = YANGDynClass(base=intf_router_isis.intf_router_isis, is_container='container', presence=False, yang_name="intf-router-isis", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'IsisLoopbackInterfaceIpRouter'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    self.__interface_loopback_ospf_conf = YANGDynClass(base=interface_loopback_ospf_conf.interface_loopback_ospf_conf, is_container='container', presence=False, yang_name="interface-loopback-ospf-conf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'OSPFLoopbackInterfaceCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    self.__ip_config = YANGDynClass(base=ip_config.ip_config, is_container='container', presence=False, yang_name="ip-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='container', is_config=True)
    self.__pim_intf_loopback_cont = YANGDynClass(base=pim_intf_loopback_cont.pim_intf_loopback_cont, is_container='container', presence=False, yang_name="pim-intf-loopback-cont", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'PimLoopbackIntfCallpoint', u'sort-priority': u'136'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='container', is_config=True)

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
      return [u'routing-system', u'interface', u'loopback', u'ip']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Loopback', u'ip']

  def _get_ip_config(self):
    """
    Getter method for ip_config, mapped from YANG variable /routing_system/interface/loopback/ip/ip_config (container)
    """
    return self.__ip_config
      
  def _set_ip_config(self, v, load=False):
    """
    Setter method for ip_config, mapped from YANG variable /routing_system/interface/loopback/ip/ip_config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_config() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ip_config.ip_config, is_container='container', presence=False, yang_name="ip-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ip_config.ip_config, is_container='container', presence=False, yang_name="ip-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='container', is_config=True)""",
        })

    self.__ip_config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_config(self):
    self.__ip_config = YANGDynClass(base=ip_config.ip_config, is_container='container', presence=False, yang_name="ip-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='container', is_config=True)


  def _get_intf_router_isis(self):
    """
    Getter method for intf_router_isis, mapped from YANG variable /routing_system/interface/loopback/ip/intf_router_isis (container)
    """
    return self.__intf_router_isis
      
  def _set_intf_router_isis(self, v, load=False):
    """
    Setter method for intf_router_isis, mapped from YANG variable /routing_system/interface/loopback/ip/intf_router_isis (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_intf_router_isis is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_intf_router_isis() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=intf_router_isis.intf_router_isis, is_container='container', presence=False, yang_name="intf-router-isis", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'IsisLoopbackInterfaceIpRouter'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """intf_router_isis must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=intf_router_isis.intf_router_isis, is_container='container', presence=False, yang_name="intf-router-isis", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'IsisLoopbackInterfaceIpRouter'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)""",
        })

    self.__intf_router_isis = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_intf_router_isis(self):
    self.__intf_router_isis = YANGDynClass(base=intf_router_isis.intf_router_isis, is_container='container', presence=False, yang_name="intf-router-isis", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'IsisLoopbackInterfaceIpRouter'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)


  def _get_interface_loopback_ospf_conf(self):
    """
    Getter method for interface_loopback_ospf_conf, mapped from YANG variable /routing_system/interface/loopback/ip/interface_loopback_ospf_conf (container)
    """
    return self.__interface_loopback_ospf_conf
      
  def _set_interface_loopback_ospf_conf(self, v, load=False):
    """
    Setter method for interface_loopback_ospf_conf, mapped from YANG variable /routing_system/interface/loopback/ip/interface_loopback_ospf_conf (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_loopback_ospf_conf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_loopback_ospf_conf() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interface_loopback_ospf_conf.interface_loopback_ospf_conf, is_container='container', presence=False, yang_name="interface-loopback-ospf-conf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'OSPFLoopbackInterfaceCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_loopback_ospf_conf must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface_loopback_ospf_conf.interface_loopback_ospf_conf, is_container='container', presence=False, yang_name="interface-loopback-ospf-conf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'OSPFLoopbackInterfaceCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)""",
        })

    self.__interface_loopback_ospf_conf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_loopback_ospf_conf(self):
    self.__interface_loopback_ospf_conf = YANGDynClass(base=interface_loopback_ospf_conf.interface_loopback_ospf_conf, is_container='container', presence=False, yang_name="interface-loopback-ospf-conf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'OSPFLoopbackInterfaceCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)


  def _get_pim_intf_loopback_cont(self):
    """
    Getter method for pim_intf_loopback_cont, mapped from YANG variable /routing_system/interface/loopback/ip/pim_intf_loopback_cont (container)
    """
    return self.__pim_intf_loopback_cont
      
  def _set_pim_intf_loopback_cont(self, v, load=False):
    """
    Setter method for pim_intf_loopback_cont, mapped from YANG variable /routing_system/interface/loopback/ip/pim_intf_loopback_cont (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pim_intf_loopback_cont is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pim_intf_loopback_cont() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=pim_intf_loopback_cont.pim_intf_loopback_cont, is_container='container', presence=False, yang_name="pim-intf-loopback-cont", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'PimLoopbackIntfCallpoint', u'sort-priority': u'136'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pim_intf_loopback_cont must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=pim_intf_loopback_cont.pim_intf_loopback_cont, is_container='container', presence=False, yang_name="pim-intf-loopback-cont", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'PimLoopbackIntfCallpoint', u'sort-priority': u'136'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='container', is_config=True)""",
        })

    self.__pim_intf_loopback_cont = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pim_intf_loopback_cont(self):
    self.__pim_intf_loopback_cont = YANGDynClass(base=pim_intf_loopback_cont.pim_intf_loopback_cont, is_container='container', presence=False, yang_name="pim-intf-loopback-cont", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'PimLoopbackIntfCallpoint', u'sort-priority': u'136'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='container', is_config=True)

  ip_config = __builtin__.property(_get_ip_config, _set_ip_config)
  intf_router_isis = __builtin__.property(_get_intf_router_isis, _set_intf_router_isis)
  interface_loopback_ospf_conf = __builtin__.property(_get_interface_loopback_ospf_conf, _set_interface_loopback_ospf_conf)
  pim_intf_loopback_cont = __builtin__.property(_get_pim_intf_loopback_cont, _set_pim_intf_loopback_cont)


  _pyangbind_elements = {'ip_config': ip_config, 'intf_router_isis': intf_router_isis, 'interface_loopback_ospf_conf': interface_loopback_ospf_conf, 'pim_intf_loopback_cont': pim_intf_loopback_cont, }


