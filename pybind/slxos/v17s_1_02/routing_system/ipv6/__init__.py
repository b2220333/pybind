
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import router
import static_ag_ipv6_config
import receive
import prefix_list
class ipv6(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/ipv6. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Internet Protoccol (IPv6). 
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__router','__static_ag_ipv6_config','__receive','__prefix_list',)

  _yang_name = 'ipv6'
  _rest_name = 'ipv6'

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
    self.__receive = YANGDynClass(base=receive.receive, is_container='container', presence=False, yang_name="receive", rest_name="receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IPv6 Receive Access group', u'callpoint': u'ipv6_receive_ag_cp', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-access-list', defining_module='brocade-ipv6-access-list', yang_type='container', is_config=True)
    self.__router = YANGDynClass(base=router.router, is_container='container', presence=False, yang_name="router", rest_name="router", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ipv6 router', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_LEVEL_ROUTER_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-common-def', defining_module='brocade-common-def', yang_type='container', is_config=True)
    self.__prefix_list = YANGDynClass(base=YANGListType("name seq_keyword instance",prefix_list.prefix_list, yang_name="prefix-list", rest_name="prefix-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name seq-keyword instance', extensions={u'tailf-common': {u'info': u'IPv6 address prefix list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'68', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipv6prefix-cp'}}), is_container='list', yang_name="prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv6 address prefix list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'68', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipv6prefix-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)
    self.__static_ag_ipv6_config = YANGDynClass(base=static_ag_ipv6_config.static_ag_ipv6_config, is_container='container', presence=False, yang_name="static-ag-ipv6-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'Ipv6AnycastGatewayMacCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='container', is_config=True)

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
      return [u'routing-system', u'ipv6']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ipv6']

  def _get_router(self):
    """
    Getter method for router, mapped from YANG variable /routing_system/ipv6/router (container)

    YANG Description: The ipv6 routing system.
    """
    return self.__router
      
  def _set_router(self, v, load=False):
    """
    Setter method for router, mapped from YANG variable /routing_system/ipv6/router (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_router is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_router() directly.

    YANG Description: The ipv6 routing system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=router.router, is_container='container', presence=False, yang_name="router", rest_name="router", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ipv6 router', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_LEVEL_ROUTER_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-common-def', defining_module='brocade-common-def', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """router must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=router.router, is_container='container', presence=False, yang_name="router", rest_name="router", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ipv6 router', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_LEVEL_ROUTER_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-common-def', defining_module='brocade-common-def', yang_type='container', is_config=True)""",
        })

    self.__router = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_router(self):
    self.__router = YANGDynClass(base=router.router, is_container='container', presence=False, yang_name="router", rest_name="router", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ipv6 router', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_LEVEL_ROUTER_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-common-def', defining_module='brocade-common-def', yang_type='container', is_config=True)


  def _get_static_ag_ipv6_config(self):
    """
    Getter method for static_ag_ipv6_config, mapped from YANG variable /routing_system/ipv6/static_ag_ipv6_config (container)
    """
    return self.__static_ag_ipv6_config
      
  def _set_static_ag_ipv6_config(self, v, load=False):
    """
    Setter method for static_ag_ipv6_config, mapped from YANG variable /routing_system/ipv6/static_ag_ipv6_config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static_ag_ipv6_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static_ag_ipv6_config() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=static_ag_ipv6_config.static_ag_ipv6_config, is_container='container', presence=False, yang_name="static-ag-ipv6-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'Ipv6AnycastGatewayMacCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static_ag_ipv6_config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=static_ag_ipv6_config.static_ag_ipv6_config, is_container='container', presence=False, yang_name="static-ag-ipv6-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'Ipv6AnycastGatewayMacCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='container', is_config=True)""",
        })

    self.__static_ag_ipv6_config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static_ag_ipv6_config(self):
    self.__static_ag_ipv6_config = YANGDynClass(base=static_ag_ipv6_config.static_ag_ipv6_config, is_container='container', presence=False, yang_name="static-ag-ipv6-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'Ipv6AnycastGatewayMacCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='container', is_config=True)


  def _get_receive(self):
    """
    Getter method for receive, mapped from YANG variable /routing_system/ipv6/receive (container)
    """
    return self.__receive
      
  def _set_receive(self, v, load=False):
    """
    Setter method for receive, mapped from YANG variable /routing_system/ipv6/receive (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_receive is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_receive() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=receive.receive, is_container='container', presence=False, yang_name="receive", rest_name="receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IPv6 Receive Access group', u'callpoint': u'ipv6_receive_ag_cp', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-access-list', defining_module='brocade-ipv6-access-list', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """receive must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=receive.receive, is_container='container', presence=False, yang_name="receive", rest_name="receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IPv6 Receive Access group', u'callpoint': u'ipv6_receive_ag_cp', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-access-list', defining_module='brocade-ipv6-access-list', yang_type='container', is_config=True)""",
        })

    self.__receive = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_receive(self):
    self.__receive = YANGDynClass(base=receive.receive, is_container='container', presence=False, yang_name="receive", rest_name="receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IPv6 Receive Access group', u'callpoint': u'ipv6_receive_ag_cp', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-access-list', defining_module='brocade-ipv6-access-list', yang_type='container', is_config=True)


  def _get_prefix_list(self):
    """
    Getter method for prefix_list, mapped from YANG variable /routing_system/ipv6/prefix_list (list)

    YANG Description: IPv6 address prefix list.
    """
    return self.__prefix_list
      
  def _set_prefix_list(self, v, load=False):
    """
    Setter method for prefix_list, mapped from YANG variable /routing_system/ipv6/prefix_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_list() directly.

    YANG Description: IPv6 address prefix list.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name seq_keyword instance",prefix_list.prefix_list, yang_name="prefix-list", rest_name="prefix-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name seq-keyword instance', extensions={u'tailf-common': {u'info': u'IPv6 address prefix list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'68', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipv6prefix-cp'}}), is_container='list', yang_name="prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv6 address prefix list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'68', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipv6prefix-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name seq_keyword instance",prefix_list.prefix_list, yang_name="prefix-list", rest_name="prefix-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name seq-keyword instance', extensions={u'tailf-common': {u'info': u'IPv6 address prefix list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'68', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipv6prefix-cp'}}), is_container='list', yang_name="prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv6 address prefix list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'68', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipv6prefix-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)""",
        })

    self.__prefix_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_list(self):
    self.__prefix_list = YANGDynClass(base=YANGListType("name seq_keyword instance",prefix_list.prefix_list, yang_name="prefix-list", rest_name="prefix-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name seq-keyword instance', extensions={u'tailf-common': {u'info': u'IPv6 address prefix list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'68', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipv6prefix-cp'}}), is_container='list', yang_name="prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv6 address prefix list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'68', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipv6prefix-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)

  router = __builtin__.property(_get_router, _set_router)
  static_ag_ipv6_config = __builtin__.property(_get_static_ag_ipv6_config, _set_static_ag_ipv6_config)
  receive = __builtin__.property(_get_receive, _set_receive)
  prefix_list = __builtin__.property(_get_prefix_list, _set_prefix_list)


  _pyangbind_elements = {'router': router, 'static_ag_ipv6_config': static_ag_ipv6_config, 'receive': receive, 'prefix_list': prefix_list, }


