
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class addpath_txrx(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/ipv6/ipv6-unicast/default-vrf/neighbor/af-ipv6-neighbor-peergroup-holder/af-ipv6-neighbor-peergroup/additional-paths/addpath-txrx. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__addpath_send','__addpath_receive',)

  _yang_name = 'addpath-txrx'
  _rest_name = ''

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
    self.__addpath_send = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="addpath-send", rest_name="send", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable to send additional paths', u'alt-name': u'send'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__addpath_receive = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="addpath-receive", rest_name="receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable to receive additional paths', u'alt-name': u'receive'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv6', u'ipv6-unicast', u'default-vrf', u'neighbor', u'af-ipv6-neighbor-peergroup-holder', u'af-ipv6-neighbor-peergroup', u'additional-paths', u'addpath-txrx']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'address-family', u'ipv6', u'unicast', u'neighbor', u'af-ipv6-neighbor-peergroup', u'additional-paths']

  def _get_addpath_send(self):
    """
    Getter method for addpath_send, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/neighbor/af_ipv6_neighbor_peergroup_holder/af_ipv6_neighbor_peergroup/additional_paths/addpath_txrx/addpath_send (empty)
    """
    return self.__addpath_send
      
  def _set_addpath_send(self, v, load=False):
    """
    Setter method for addpath_send, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/neighbor/af_ipv6_neighbor_peergroup_holder/af_ipv6_neighbor_peergroup/additional_paths/addpath_txrx/addpath_send (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_addpath_send is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_addpath_send() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="addpath-send", rest_name="send", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable to send additional paths', u'alt-name': u'send'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """addpath_send must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="addpath-send", rest_name="send", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable to send additional paths', u'alt-name': u'send'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__addpath_send = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_addpath_send(self):
    self.__addpath_send = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="addpath-send", rest_name="send", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable to send additional paths', u'alt-name': u'send'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_addpath_receive(self):
    """
    Getter method for addpath_receive, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/neighbor/af_ipv6_neighbor_peergroup_holder/af_ipv6_neighbor_peergroup/additional_paths/addpath_txrx/addpath_receive (empty)
    """
    return self.__addpath_receive
      
  def _set_addpath_receive(self, v, load=False):
    """
    Setter method for addpath_receive, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/neighbor/af_ipv6_neighbor_peergroup_holder/af_ipv6_neighbor_peergroup/additional_paths/addpath_txrx/addpath_receive (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_addpath_receive is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_addpath_receive() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="addpath-receive", rest_name="receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable to receive additional paths', u'alt-name': u'receive'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """addpath_receive must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="addpath-receive", rest_name="receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable to receive additional paths', u'alt-name': u'receive'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__addpath_receive = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_addpath_receive(self):
    self.__addpath_receive = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="addpath-receive", rest_name="receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable to receive additional paths', u'alt-name': u'receive'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

  addpath_send = __builtin__.property(_get_addpath_send, _set_addpath_send)
  addpath_receive = __builtin__.property(_get_addpath_receive, _set_addpath_receive)


  _pyangbind_elements = {'addpath_send': addpath_send, 'addpath_receive': addpath_receive, }


