
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ecmp
import route
import port_channel
import login_policy
class fabric(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/fabric. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This function is used to configure fabric
parameters such as ECMP load balancing parameters
and multicast priority.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ecmp','__route','__port_channel','__login_policy','__neighbor_discovery',)

  _yang_name = 'fabric'
  _rest_name = 'fabric'

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
    self.__port_channel = YANGDynClass(base=YANGListType("po_id",port_channel.port_channel, yang_name="port-channel", rest_name="port-channel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='po-id', extensions={u'tailf-common': {u'info': u'Vlag load-balancing', u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None, u'callpoint': u'node_vlag_cp'}}), is_container='list', yang_name="port-channel", rest_name="port-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Vlag load-balancing', u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None, u'callpoint': u'node_vlag_cp'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='list', is_config=True)
    self.__route = YANGDynClass(base=route.route, is_container='container', yang_name="route", rest_name="route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure routing related parameters'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='container', is_config=True)
    self.__neighbor_discovery = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="neighbor-discovery", rest_name="neighbor-discovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable neighbor discovery to form VCS cluster', u'hidden': u'eft-only', u'callpoint': u'FabricNeighborDiscoveryCallPoint', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='empty', is_config=True)
    self.__login_policy = YANGDynClass(base=login_policy.login_policy, is_container='container', yang_name="login-policy", rest_name="login-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-add-mode': None, u'cli-full-command': None, u'callpoint': u'switch_login_policy', u'info': u'Configure switch login parameters in a fabric.'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='container', is_config=True)
    self.__ecmp = YANGDynClass(base=ecmp.ecmp, is_container='container', yang_name="ecmp", rest_name="ecmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ECMP parameters', u'callpoint': u'Ecmp_loadbalance', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='container', is_config=True)

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
      return [u'rbridge-id', u'fabric']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'fabric']

  def _get_ecmp(self):
    """
    Getter method for ecmp, mapped from YANG variable /rbridge_id/fabric/ecmp (container)

    YANG Description: This function allows to configure ECMP
related parameters.
    """
    return self.__ecmp
      
  def _set_ecmp(self, v, load=False):
    """
    Setter method for ecmp, mapped from YANG variable /rbridge_id/fabric/ecmp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ecmp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ecmp() directly.

    YANG Description: This function allows to configure ECMP
related parameters.
    """
    try:
      t = YANGDynClass(v,base=ecmp.ecmp, is_container='container', yang_name="ecmp", rest_name="ecmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ECMP parameters', u'callpoint': u'Ecmp_loadbalance', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ecmp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ecmp.ecmp, is_container='container', yang_name="ecmp", rest_name="ecmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ECMP parameters', u'callpoint': u'Ecmp_loadbalance', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='container', is_config=True)""",
        })

    self.__ecmp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ecmp(self):
    self.__ecmp = YANGDynClass(base=ecmp.ecmp, is_container='container', yang_name="ecmp", rest_name="ecmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ECMP parameters', u'callpoint': u'Ecmp_loadbalance', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='container', is_config=True)


  def _get_route(self):
    """
    Getter method for route, mapped from YANG variable /rbridge_id/fabric/route (container)

    YANG Description: Function to configure routing related information
such as multicast priority.
    """
    return self.__route
      
  def _set_route(self, v, load=False):
    """
    Setter method for route, mapped from YANG variable /rbridge_id/fabric/route (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route() directly.

    YANG Description: Function to configure routing related information
such as multicast priority.
    """
    try:
      t = YANGDynClass(v,base=route.route, is_container='container', yang_name="route", rest_name="route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure routing related parameters'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=route.route, is_container='container', yang_name="route", rest_name="route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure routing related parameters'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='container', is_config=True)""",
        })

    self.__route = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route(self):
    self.__route = YANGDynClass(base=route.route, is_container='container', yang_name="route", rest_name="route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure routing related parameters'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='container', is_config=True)


  def _get_port_channel(self):
    """
    Getter method for port_channel, mapped from YANG variable /rbridge_id/fabric/port_channel (list)
    """
    return self.__port_channel
      
  def _set_port_channel(self, v, load=False):
    """
    Setter method for port_channel, mapped from YANG variable /rbridge_id/fabric/port_channel (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_channel is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_channel() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("po_id",port_channel.port_channel, yang_name="port-channel", rest_name="port-channel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='po-id', extensions={u'tailf-common': {u'info': u'Vlag load-balancing', u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None, u'callpoint': u'node_vlag_cp'}}), is_container='list', yang_name="port-channel", rest_name="port-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Vlag load-balancing', u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None, u'callpoint': u'node_vlag_cp'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_channel must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("po_id",port_channel.port_channel, yang_name="port-channel", rest_name="port-channel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='po-id', extensions={u'tailf-common': {u'info': u'Vlag load-balancing', u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None, u'callpoint': u'node_vlag_cp'}}), is_container='list', yang_name="port-channel", rest_name="port-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Vlag load-balancing', u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None, u'callpoint': u'node_vlag_cp'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='list', is_config=True)""",
        })

    self.__port_channel = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_channel(self):
    self.__port_channel = YANGDynClass(base=YANGListType("po_id",port_channel.port_channel, yang_name="port-channel", rest_name="port-channel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='po-id', extensions={u'tailf-common': {u'info': u'Vlag load-balancing', u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None, u'callpoint': u'node_vlag_cp'}}), is_container='list', yang_name="port-channel", rest_name="port-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Vlag load-balancing', u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None, u'callpoint': u'node_vlag_cp'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='list', is_config=True)


  def _get_login_policy(self):
    """
    Getter method for login_policy, mapped from YANG variable /rbridge_id/fabric/login_policy (container)

    YANG Description: This function control the switch login configurations
- Allow FLOGI/FDISC duplicate port WWN to login into switch.
    """
    return self.__login_policy
      
  def _set_login_policy(self, v, load=False):
    """
    Setter method for login_policy, mapped from YANG variable /rbridge_id/fabric/login_policy (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_login_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_login_policy() directly.

    YANG Description: This function control the switch login configurations
- Allow FLOGI/FDISC duplicate port WWN to login into switch.
    """
    try:
      t = YANGDynClass(v,base=login_policy.login_policy, is_container='container', yang_name="login-policy", rest_name="login-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-add-mode': None, u'cli-full-command': None, u'callpoint': u'switch_login_policy', u'info': u'Configure switch login parameters in a fabric.'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """login_policy must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=login_policy.login_policy, is_container='container', yang_name="login-policy", rest_name="login-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-add-mode': None, u'cli-full-command': None, u'callpoint': u'switch_login_policy', u'info': u'Configure switch login parameters in a fabric.'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='container', is_config=True)""",
        })

    self.__login_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_login_policy(self):
    self.__login_policy = YANGDynClass(base=login_policy.login_policy, is_container='container', yang_name="login-policy", rest_name="login-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-add-mode': None, u'cli-full-command': None, u'callpoint': u'switch_login_policy', u'info': u'Configure switch login parameters in a fabric.'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='container', is_config=True)


  def _get_neighbor_discovery(self):
    """
    Getter method for neighbor_discovery, mapped from YANG variable /rbridge_id/fabric/neighbor_discovery (empty)
    """
    return self.__neighbor_discovery
      
  def _set_neighbor_discovery(self, v, load=False):
    """
    Setter method for neighbor_discovery, mapped from YANG variable /rbridge_id/fabric/neighbor_discovery (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor_discovery is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor_discovery() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="neighbor-discovery", rest_name="neighbor-discovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable neighbor discovery to form VCS cluster', u'hidden': u'eft-only', u'callpoint': u'FabricNeighborDiscoveryCallPoint', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor_discovery must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="neighbor-discovery", rest_name="neighbor-discovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable neighbor discovery to form VCS cluster', u'hidden': u'eft-only', u'callpoint': u'FabricNeighborDiscoveryCallPoint', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='empty', is_config=True)""",
        })

    self.__neighbor_discovery = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor_discovery(self):
    self.__neighbor_discovery = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="neighbor-discovery", rest_name="neighbor-discovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable neighbor discovery to form VCS cluster', u'hidden': u'eft-only', u'callpoint': u'FabricNeighborDiscoveryCallPoint', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='empty', is_config=True)

  ecmp = __builtin__.property(_get_ecmp, _set_ecmp)
  route = __builtin__.property(_get_route, _set_route)
  port_channel = __builtin__.property(_get_port_channel, _set_port_channel)
  login_policy = __builtin__.property(_get_login_policy, _set_login_policy)
  neighbor_discovery = __builtin__.property(_get_neighbor_discovery, _set_neighbor_discovery)


  _pyangbind_elements = {'ecmp': ecmp, 'route': route, 'port_channel': port_channel, 'login_policy': login_policy, 'neighbor_discovery': neighbor_discovery, }


