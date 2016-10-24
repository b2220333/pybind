
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class level1_into_level2(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/isis/router-isis-cmds-holder/address-family/ipv4/af-ipv4-unicast/af-ipv4-attributes/af-common-attributes/redistribute/isis/level-1/into/level1-into-level2. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__prefix_list_level1','__level1_into_level2_disable',)

  _yang_name = 'level1-into-level2'
  _rest_name = 'level-2'

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
    self.__level1_into_level2_disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="level1-into-level2-disable", rest_name="disable", parent=self, choice=(u'ch-prefix-list-level1-disable', u'ca-leve11-into-level2-disable'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)
    self.__prefix_list_level1 = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="prefix-list-level1", rest_name="prefix-list", parent=self, choice=(u'ch-prefix-list-level1-disable', u'ca-prefix-list-level1'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Select routes using prefix-list', u'alt-name': u'prefix-list'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='string', is_config=True)

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
      return [u'routing-system', u'router', u'isis', u'router-isis-cmds-holder', u'address-family', u'ipv4', u'af-ipv4-unicast', u'af-ipv4-attributes', u'af-common-attributes', u'redistribute', u'isis', u'level-1', u'into', u'level1-into-level2']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'isis', u'address-family', u'ipv4', u'unicast', u'redistribute', u'isis', u'level-1', u'into', u'level-2']

  def _get_prefix_list_level1(self):
    """
    Getter method for prefix_list_level1, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/af_common_attributes/redistribute/isis/level_1/into/level1_into_level2/prefix_list_level1 (string)
    """
    return self.__prefix_list_level1
      
  def _set_prefix_list_level1(self, v, load=False):
    """
    Setter method for prefix_list_level1, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/af_common_attributes/redistribute/isis/level_1/into/level1_into_level2/prefix_list_level1 (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_list_level1 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_list_level1() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="prefix-list-level1", rest_name="prefix-list", parent=self, choice=(u'ch-prefix-list-level1-disable', u'ca-prefix-list-level1'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Select routes using prefix-list', u'alt-name': u'prefix-list'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_list_level1 must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="prefix-list-level1", rest_name="prefix-list", parent=self, choice=(u'ch-prefix-list-level1-disable', u'ca-prefix-list-level1'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Select routes using prefix-list', u'alt-name': u'prefix-list'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='string', is_config=True)""",
        })

    self.__prefix_list_level1 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_list_level1(self):
    self.__prefix_list_level1 = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="prefix-list-level1", rest_name="prefix-list", parent=self, choice=(u'ch-prefix-list-level1-disable', u'ca-prefix-list-level1'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Select routes using prefix-list', u'alt-name': u'prefix-list'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='string', is_config=True)


  def _get_level1_into_level2_disable(self):
    """
    Getter method for level1_into_level2_disable, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/af_common_attributes/redistribute/isis/level_1/into/level1_into_level2/level1_into_level2_disable (empty)
    """
    return self.__level1_into_level2_disable
      
  def _set_level1_into_level2_disable(self, v, load=False):
    """
    Setter method for level1_into_level2_disable, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/af_common_attributes/redistribute/isis/level_1/into/level1_into_level2/level1_into_level2_disable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_level1_into_level2_disable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_level1_into_level2_disable() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="level1-into-level2-disable", rest_name="disable", parent=self, choice=(u'ch-prefix-list-level1-disable', u'ca-leve11-into-level2-disable'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """level1_into_level2_disable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="level1-into-level2-disable", rest_name="disable", parent=self, choice=(u'ch-prefix-list-level1-disable', u'ca-leve11-into-level2-disable'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)""",
        })

    self.__level1_into_level2_disable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_level1_into_level2_disable(self):
    self.__level1_into_level2_disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="level1-into-level2-disable", rest_name="disable", parent=self, choice=(u'ch-prefix-list-level1-disable', u'ca-leve11-into-level2-disable'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)

  prefix_list_level1 = __builtin__.property(_get_prefix_list_level1, _set_prefix_list_level1)
  level1_into_level2_disable = __builtin__.property(_get_level1_into_level2_disable, _set_level1_into_level2_disable)

  __choices__ = {u'ch-prefix-list-level1-disable': {u'ca-leve11-into-level2-disable': [u'level1_into_level2_disable'], u'ca-prefix-list-level1': [u'prefix_list_level1']}}
  _pyangbind_elements = {'prefix_list_level1': prefix_list_level1, 'level1_into_level2_disable': level1_into_level2_disable, }


