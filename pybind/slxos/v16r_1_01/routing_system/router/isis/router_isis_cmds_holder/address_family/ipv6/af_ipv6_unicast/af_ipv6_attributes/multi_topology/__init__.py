
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class multi_topology(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/isis/router-isis-cmds-holder/address-family/ipv6/af-ipv6-unicast/af-ipv6-attributes/multi-topology. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__multi_topology_transition',)

  _yang_name = 'multi-topology'
  _rest_name = 'multi-topology'

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
    self.__multi_topology_transition = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="multi-topology-transition", rest_name="transition", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Accept and generate both ISIS IPv6 and Multi-topology IPv6 TLVs', u'alt-name': u'transition'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'router', u'isis', u'router-isis-cmds-holder', u'address-family', u'ipv6', u'af-ipv6-unicast', u'af-ipv6-attributes', u'multi-topology']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'isis', u'address-family', u'ipv6', u'unicast', u'multi-topology']

  def _get_multi_topology_transition(self):
    """
    Getter method for multi_topology_transition, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/multi_topology/multi_topology_transition (empty)
    """
    return self.__multi_topology_transition
      
  def _set_multi_topology_transition(self, v, load=False):
    """
    Setter method for multi_topology_transition, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/multi_topology/multi_topology_transition (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_multi_topology_transition is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_multi_topology_transition() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="multi-topology-transition", rest_name="transition", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Accept and generate both ISIS IPv6 and Multi-topology IPv6 TLVs', u'alt-name': u'transition'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """multi_topology_transition must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="multi-topology-transition", rest_name="transition", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Accept and generate both ISIS IPv6 and Multi-topology IPv6 TLVs', u'alt-name': u'transition'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)""",
        })

    self.__multi_topology_transition = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_multi_topology_transition(self):
    self.__multi_topology_transition = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="multi-topology-transition", rest_name="transition", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Accept and generate both ISIS IPv6 and Multi-topology IPv6 TLVs', u'alt-name': u'transition'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)

  multi_topology_transition = __builtin__.property(_get_multi_topology_transition, _set_multi_topology_transition)


  _pyangbind_elements = {'multi_topology_transition': multi_topology_transition, }


