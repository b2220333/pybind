
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import addpath_txrx
import addpath_select
class af_additional_paths(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/ipv6/ipv6-unicast/default-vrf/af-common-cmds-holder/af-additional-paths. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__addpath_txrx','__addpath_select',)

  _yang_name = 'af-additional-paths'
  _rest_name = 'additional-paths'

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
    self.__addpath_txrx = YANGDynClass(base=addpath_txrx.addpath_txrx, is_container='container', presence=False, yang_name="addpath-txrx", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__addpath_select = YANGDynClass(base=addpath_select.addpath_select, is_container='container', presence=False, yang_name="addpath-select", rest_name="select", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify which routes should be selected as candidates for additioanal paths', u'cli-compact-syntax': None, u'alt-name': u'select', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv6', u'ipv6-unicast', u'default-vrf', u'af-common-cmds-holder', u'af-additional-paths']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'address-family', u'ipv6', u'unicast', u'additional-paths']

  def _get_addpath_txrx(self):
    """
    Getter method for addpath_txrx, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_common_cmds_holder/af_additional_paths/addpath_txrx (container)
    """
    return self.__addpath_txrx
      
  def _set_addpath_txrx(self, v, load=False):
    """
    Setter method for addpath_txrx, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_common_cmds_holder/af_additional_paths/addpath_txrx (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_addpath_txrx is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_addpath_txrx() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=addpath_txrx.addpath_txrx, is_container='container', presence=False, yang_name="addpath-txrx", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """addpath_txrx must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=addpath_txrx.addpath_txrx, is_container='container', presence=False, yang_name="addpath-txrx", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__addpath_txrx = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_addpath_txrx(self):
    self.__addpath_txrx = YANGDynClass(base=addpath_txrx.addpath_txrx, is_container='container', presence=False, yang_name="addpath-txrx", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_addpath_select(self):
    """
    Getter method for addpath_select, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_common_cmds_holder/af_additional_paths/addpath_select (container)
    """
    return self.__addpath_select
      
  def _set_addpath_select(self, v, load=False):
    """
    Setter method for addpath_select, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_common_cmds_holder/af_additional_paths/addpath_select (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_addpath_select is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_addpath_select() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=addpath_select.addpath_select, is_container='container', presence=False, yang_name="addpath-select", rest_name="select", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify which routes should be selected as candidates for additioanal paths', u'cli-compact-syntax': None, u'alt-name': u'select', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """addpath_select must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=addpath_select.addpath_select, is_container='container', presence=False, yang_name="addpath-select", rest_name="select", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify which routes should be selected as candidates for additioanal paths', u'cli-compact-syntax': None, u'alt-name': u'select', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__addpath_select = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_addpath_select(self):
    self.__addpath_select = YANGDynClass(base=addpath_select.addpath_select, is_container='container', presence=False, yang_name="addpath-select", rest_name="select", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify which routes should be selected as candidates for additioanal paths', u'cli-compact-syntax': None, u'alt-name': u'select', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

  addpath_txrx = __builtin__.property(_get_addpath_txrx, _set_addpath_txrx)
  addpath_select = __builtin__.property(_get_addpath_select, _set_addpath_select)


  _pyangbind_elements = {'addpath_txrx': addpath_txrx, 'addpath_select': addpath_select, }


