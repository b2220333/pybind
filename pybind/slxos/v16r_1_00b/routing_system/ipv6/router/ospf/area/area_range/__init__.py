
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class area_range(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/ipv6/router/ospf/area/area-range. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: If the ABR that connects the NSSA to other areas needs to summarize the routes in the NSSA before translating them into Type-5 LSAs and flooding them into the other areas, configure an address range. The ABR creates an aggregate value based on the address range. The aggregate value becomes the address that the ABR advertises instead of advertising the individual addresses represented by the aggregate.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__range_address','__range_effect','__range_cost',)

  _yang_name = 'area-range'
  _rest_name = 'range'

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
    self.__range_cost = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="range-cost", rest_name="cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure area range cost', u'cli-optional-in-sequence': None, u'alt-name': u'cost'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='ospf:range-metric', is_config=True)
    self.__range_effect = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'advertise': {'value': 1}, u'not-advertise': {'value': 2}},), is_leaf=True, yang_name="range-effect", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise/Do not advertise this type-3 summarization', u'cli-drop-node-name': None, u'cli-suppress-no': None, u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='enumeration', is_config=True)
    self.__range_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="range-address", rest_name="range-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D/LEN;; IPv6 address to match'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:ipv6-address-prefix', is_config=True)

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
      return [u'routing-system', u'ipv6', u'router', u'ospf', u'area', u'area-range']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ipv6', u'router', u'ospf', u'area', u'range']

  def _get_range_address(self):
    """
    Getter method for range_address, mapped from YANG variable /routing_system/ipv6/router/ospf/area/area_range/range_address (common-def:ipv6-address-prefix)

    YANG Description: Specifies the IP address portion of the range. The software compares the address with the significant bits in the mask. All network addresses that match thiscomparison are summarized in a single route advertised by the router.
    """
    return self.__range_address
      
  def _set_range_address(self, v, load=False):
    """
    Setter method for range_address, mapped from YANG variable /routing_system/ipv6/router/ospf/area/area_range/range_address (common-def:ipv6-address-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_range_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_range_address() directly.

    YANG Description: Specifies the IP address portion of the range. The software compares the address with the significant bits in the mask. All network addresses that match thiscomparison are summarized in a single route advertised by the router.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="range-address", rest_name="range-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D/LEN;; IPv6 address to match'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:ipv6-address-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """range_address must be of a type compatible with common-def:ipv6-address-prefix""",
          'defined-type': "common-def:ipv6-address-prefix",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="range-address", rest_name="range-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D/LEN;; IPv6 address to match'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:ipv6-address-prefix', is_config=True)""",
        })

    self.__range_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_range_address(self):
    self.__range_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="range-address", rest_name="range-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D/LEN;; IPv6 address to match'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:ipv6-address-prefix', is_config=True)


  def _get_range_effect(self):
    """
    Getter method for range_effect, mapped from YANG variable /routing_system/ipv6/router/ospf/area/area_range/range_effect (enumeration)

    YANG Description: Advertise/Do not advertise this type-3 summarization
    """
    return self.__range_effect
      
  def _set_range_effect(self, v, load=False):
    """
    Setter method for range_effect, mapped from YANG variable /routing_system/ipv6/router/ospf/area/area_range/range_effect (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_range_effect is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_range_effect() directly.

    YANG Description: Advertise/Do not advertise this type-3 summarization
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'advertise': {'value': 1}, u'not-advertise': {'value': 2}},), is_leaf=True, yang_name="range-effect", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise/Do not advertise this type-3 summarization', u'cli-drop-node-name': None, u'cli-suppress-no': None, u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """range_effect must be of a type compatible with enumeration""",
          'defined-type': "brocade-ospfv3:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'advertise': {'value': 1}, u'not-advertise': {'value': 2}},), is_leaf=True, yang_name="range-effect", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise/Do not advertise this type-3 summarization', u'cli-drop-node-name': None, u'cli-suppress-no': None, u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='enumeration', is_config=True)""",
        })

    self.__range_effect = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_range_effect(self):
    self.__range_effect = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'advertise': {'value': 1}, u'not-advertise': {'value': 2}},), is_leaf=True, yang_name="range-effect", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise/Do not advertise this type-3 summarization', u'cli-drop-node-name': None, u'cli-suppress-no': None, u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='enumeration', is_config=True)


  def _get_range_cost(self):
    """
    Getter method for range_cost, mapped from YANG variable /routing_system/ipv6/router/ospf/area/area_range/range_cost (ospf:range-metric)

    YANG Description: Used to consolidate and summarize routes at an area boundary.If the cost parameter is specified, it will be used (overriding the computed cost) to generate the summary LSA. If the cost parameter is not specified, then the existing range metric computation max or min cost of routes falling under this range will be used to generate summary LSA.
    """
    return self.__range_cost
      
  def _set_range_cost(self, v, load=False):
    """
    Setter method for range_cost, mapped from YANG variable /routing_system/ipv6/router/ospf/area/area_range/range_cost (ospf:range-metric)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_range_cost is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_range_cost() directly.

    YANG Description: Used to consolidate and summarize routes at an area boundary.If the cost parameter is specified, it will be used (overriding the computed cost) to generate the summary LSA. If the cost parameter is not specified, then the existing range metric computation max or min cost of routes falling under this range will be used to generate summary LSA.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="range-cost", rest_name="cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure area range cost', u'cli-optional-in-sequence': None, u'alt-name': u'cost'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='ospf:range-metric', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """range_cost must be of a type compatible with ospf:range-metric""",
          'defined-type': "ospf:range-metric",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="range-cost", rest_name="cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure area range cost', u'cli-optional-in-sequence': None, u'alt-name': u'cost'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='ospf:range-metric', is_config=True)""",
        })

    self.__range_cost = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_range_cost(self):
    self.__range_cost = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="range-cost", rest_name="cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure area range cost', u'cli-optional-in-sequence': None, u'alt-name': u'cost'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='ospf:range-metric', is_config=True)

  range_address = __builtin__.property(_get_range_address, _set_range_address)
  range_effect = __builtin__.property(_get_range_effect, _set_range_effect)
  range_cost = __builtin__.property(_get_range_cost, _set_range_cost)


  _pyangbind_elements = {'range_address': range_address, 'range_effect': range_effect, 'range_cost': range_cost, }


