
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class direction_in(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/router-bgp/address-family/ipv6/ipv6-unicast/default-vrf/neighbor/af-ipv6-neighbor-peergroup-holder/af-ipv6-neighbor-peergroup/prefix-list/direction-in. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__prefix_list_direction_in_prefix_name','__prefix_list_direction_in',)

  _yang_name = 'direction-in'
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
    self.__prefix_list_direction_in = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="prefix-list-direction-in", rest_name="in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Filter incoming routes', u'alt-name': u'in'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__prefix_list_direction_in_prefix_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="prefix-list-direction-in-prefix-name", rest_name="ip-access-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'alt-name': u'ip-access-number', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='nei-prefix-list-filter', is_config=True)

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
      return [u'rbridge-id', u'router', u'router-bgp', u'address-family', u'ipv6', u'ipv6-unicast', u'default-vrf', u'neighbor', u'af-ipv6-neighbor-peergroup-holder', u'af-ipv6-neighbor-peergroup', u'prefix-list', u'direction-in']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'bgp', u'address-family', u'ipv6', u'unicast', u'neighbor', u'prefix-list']

  def _get_prefix_list_direction_in_prefix_name(self):
    """
    Getter method for prefix_list_direction_in_prefix_name, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/neighbor/af_ipv6_neighbor_peergroup_holder/af_ipv6_neighbor_peergroup/prefix_list/direction_in/prefix_list_direction_in_prefix_name (nei-prefix-list-filter)
    """
    return self.__prefix_list_direction_in_prefix_name
      
  def _set_prefix_list_direction_in_prefix_name(self, v, load=False):
    """
    Setter method for prefix_list_direction_in_prefix_name, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/neighbor/af_ipv6_neighbor_peergroup_holder/af_ipv6_neighbor_peergroup/prefix_list/direction_in/prefix_list_direction_in_prefix_name (nei-prefix-list-filter)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_list_direction_in_prefix_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_list_direction_in_prefix_name() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="prefix-list-direction-in-prefix-name", rest_name="ip-access-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'alt-name': u'ip-access-number', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='nei-prefix-list-filter', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_list_direction_in_prefix_name must be of a type compatible with nei-prefix-list-filter""",
          'defined-type': "brocade-bgp:nei-prefix-list-filter",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="prefix-list-direction-in-prefix-name", rest_name="ip-access-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'alt-name': u'ip-access-number', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='nei-prefix-list-filter', is_config=True)""",
        })

    self.__prefix_list_direction_in_prefix_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_list_direction_in_prefix_name(self):
    self.__prefix_list_direction_in_prefix_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="prefix-list-direction-in-prefix-name", rest_name="ip-access-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'alt-name': u'ip-access-number', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='nei-prefix-list-filter', is_config=True)


  def _get_prefix_list_direction_in(self):
    """
    Getter method for prefix_list_direction_in, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/neighbor/af_ipv6_neighbor_peergroup_holder/af_ipv6_neighbor_peergroup/prefix_list/direction_in/prefix_list_direction_in (empty)
    """
    return self.__prefix_list_direction_in
      
  def _set_prefix_list_direction_in(self, v, load=False):
    """
    Setter method for prefix_list_direction_in, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/neighbor/af_ipv6_neighbor_peergroup_holder/af_ipv6_neighbor_peergroup/prefix_list/direction_in/prefix_list_direction_in (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_list_direction_in is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_list_direction_in() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="prefix-list-direction-in", rest_name="in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Filter incoming routes', u'alt-name': u'in'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_list_direction_in must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="prefix-list-direction-in", rest_name="in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Filter incoming routes', u'alt-name': u'in'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__prefix_list_direction_in = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_list_direction_in(self):
    self.__prefix_list_direction_in = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="prefix-list-direction-in", rest_name="in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Filter incoming routes', u'alt-name': u'in'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

  prefix_list_direction_in_prefix_name = __builtin__.property(_get_prefix_list_direction_in_prefix_name, _set_prefix_list_direction_in_prefix_name)
  prefix_list_direction_in = __builtin__.property(_get_prefix_list_direction_in, _set_prefix_list_direction_in)


  _pyangbind_elements = {'prefix_list_direction_in_prefix_name': prefix_list_direction_in_prefix_name, 'prefix_list_direction_in': prefix_list_direction_in, }


