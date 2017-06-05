
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class redist_isis(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-isis-operational - based on the path /isis-state/router-isis-config/is-address-family-v4/redist-isis. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Redistribution config for IS-IS routes into IS-IS between levels
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__redist_is_l2_to_l1','__redist_is_l2_to_l1_prefix','__redist_is_l1_to_l2','__redist_is_l1_to_l2_prefix',)

  _yang_name = 'redist-isis'
  _rest_name = 'redist-isis'

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
    self.__redist_is_l1_to_l2_prefix = YANGDynClass(base=unicode, is_leaf=True, yang_name="redist-is-l1-to-l2-prefix", rest_name="redist-is-l1-to-l2-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)
    self.__redist_is_l1_to_l2 = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="redist-is-l1-to-l2", rest_name="redist-is-l1-to-l2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)
    self.__redist_is_l2_to_l1_prefix = YANGDynClass(base=unicode, is_leaf=True, yang_name="redist-is-l2-to-l1-prefix", rest_name="redist-is-l2-to-l1-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)
    self.__redist_is_l2_to_l1 = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="redist-is-l2-to-l1", rest_name="redist-is-l2-to-l1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)

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
      return [u'isis-state', u'router-isis-config', u'is-address-family-v4', u'redist-isis']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'isis-state', u'router-isis-config', u'is-address-family-v4', u'redist-isis']

  def _get_redist_is_l2_to_l1(self):
    """
    Getter method for redist_is_l2_to_l1, mapped from YANG variable /isis_state/router_isis_config/is_address_family_v4/redist_isis/redist_is_l2_to_l1 (isis-status)

    YANG Description: If IS-IS route redistribution from level-2 into level-1 is enabled
    """
    return self.__redist_is_l2_to_l1
      
  def _set_redist_is_l2_to_l1(self, v, load=False):
    """
    Setter method for redist_is_l2_to_l1, mapped from YANG variable /isis_state/router_isis_config/is_address_family_v4/redist_isis/redist_is_l2_to_l1 (isis-status)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redist_is_l2_to_l1 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redist_is_l2_to_l1() directly.

    YANG Description: If IS-IS route redistribution from level-2 into level-1 is enabled
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="redist-is-l2-to-l1", rest_name="redist-is-l2-to-l1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redist_is_l2_to_l1 must be of a type compatible with isis-status""",
          'defined-type': "brocade-isis-operational:isis-status",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="redist-is-l2-to-l1", rest_name="redist-is-l2-to-l1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)""",
        })

    self.__redist_is_l2_to_l1 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redist_is_l2_to_l1(self):
    self.__redist_is_l2_to_l1 = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="redist-is-l2-to-l1", rest_name="redist-is-l2-to-l1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)


  def _get_redist_is_l2_to_l1_prefix(self):
    """
    Getter method for redist_is_l2_to_l1_prefix, mapped from YANG variable /isis_state/router_isis_config/is_address_family_v4/redist_isis/redist_is_l2_to_l1_prefix (string)

    YANG Description: Prefix list name for level-2 to level-1 route distribution
    """
    return self.__redist_is_l2_to_l1_prefix
      
  def _set_redist_is_l2_to_l1_prefix(self, v, load=False):
    """
    Setter method for redist_is_l2_to_l1_prefix, mapped from YANG variable /isis_state/router_isis_config/is_address_family_v4/redist_isis/redist_is_l2_to_l1_prefix (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redist_is_l2_to_l1_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redist_is_l2_to_l1_prefix() directly.

    YANG Description: Prefix list name for level-2 to level-1 route distribution
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="redist-is-l2-to-l1-prefix", rest_name="redist-is-l2-to-l1-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redist_is_l2_to_l1_prefix must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="redist-is-l2-to-l1-prefix", rest_name="redist-is-l2-to-l1-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)""",
        })

    self.__redist_is_l2_to_l1_prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redist_is_l2_to_l1_prefix(self):
    self.__redist_is_l2_to_l1_prefix = YANGDynClass(base=unicode, is_leaf=True, yang_name="redist-is-l2-to-l1-prefix", rest_name="redist-is-l2-to-l1-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)


  def _get_redist_is_l1_to_l2(self):
    """
    Getter method for redist_is_l1_to_l2, mapped from YANG variable /isis_state/router_isis_config/is_address_family_v4/redist_isis/redist_is_l1_to_l2 (isis-status)

    YANG Description: If IS-IS route redistribution from level-1 into level-2 is enabled
    """
    return self.__redist_is_l1_to_l2
      
  def _set_redist_is_l1_to_l2(self, v, load=False):
    """
    Setter method for redist_is_l1_to_l2, mapped from YANG variable /isis_state/router_isis_config/is_address_family_v4/redist_isis/redist_is_l1_to_l2 (isis-status)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redist_is_l1_to_l2 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redist_is_l1_to_l2() directly.

    YANG Description: If IS-IS route redistribution from level-1 into level-2 is enabled
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="redist-is-l1-to-l2", rest_name="redist-is-l1-to-l2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redist_is_l1_to_l2 must be of a type compatible with isis-status""",
          'defined-type': "brocade-isis-operational:isis-status",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="redist-is-l1-to-l2", rest_name="redist-is-l1-to-l2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)""",
        })

    self.__redist_is_l1_to_l2 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redist_is_l1_to_l2(self):
    self.__redist_is_l1_to_l2 = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="redist-is-l1-to-l2", rest_name="redist-is-l1-to-l2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)


  def _get_redist_is_l1_to_l2_prefix(self):
    """
    Getter method for redist_is_l1_to_l2_prefix, mapped from YANG variable /isis_state/router_isis_config/is_address_family_v4/redist_isis/redist_is_l1_to_l2_prefix (string)

    YANG Description: Prefix list name for level-1 to level-2 route distribution
    """
    return self.__redist_is_l1_to_l2_prefix
      
  def _set_redist_is_l1_to_l2_prefix(self, v, load=False):
    """
    Setter method for redist_is_l1_to_l2_prefix, mapped from YANG variable /isis_state/router_isis_config/is_address_family_v4/redist_isis/redist_is_l1_to_l2_prefix (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redist_is_l1_to_l2_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redist_is_l1_to_l2_prefix() directly.

    YANG Description: Prefix list name for level-1 to level-2 route distribution
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="redist-is-l1-to-l2-prefix", rest_name="redist-is-l1-to-l2-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redist_is_l1_to_l2_prefix must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="redist-is-l1-to-l2-prefix", rest_name="redist-is-l1-to-l2-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)""",
        })

    self.__redist_is_l1_to_l2_prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redist_is_l1_to_l2_prefix(self):
    self.__redist_is_l1_to_l2_prefix = YANGDynClass(base=unicode, is_leaf=True, yang_name="redist-is-l1-to-l2-prefix", rest_name="redist-is-l1-to-l2-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)

  redist_is_l2_to_l1 = __builtin__.property(_get_redist_is_l2_to_l1)
  redist_is_l2_to_l1_prefix = __builtin__.property(_get_redist_is_l2_to_l1_prefix)
  redist_is_l1_to_l2 = __builtin__.property(_get_redist_is_l1_to_l2)
  redist_is_l1_to_l2_prefix = __builtin__.property(_get_redist_is_l1_to_l2_prefix)


  _pyangbind_elements = {'redist_is_l2_to_l1': redist_is_l2_to_l1, 'redist_is_l2_to_l1_prefix': redist_is_l2_to_l1_prefix, 'redist_is_l1_to_l2': redist_is_l1_to_l2, 'redist_is_l1_to_l2_prefix': redist_is_l1_to_l2_prefix, }


