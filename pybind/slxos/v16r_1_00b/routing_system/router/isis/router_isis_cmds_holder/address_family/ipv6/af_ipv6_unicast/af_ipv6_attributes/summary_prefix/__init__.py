
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class summary_prefix(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/isis/router-isis-cmds-holder/address-family/ipv6/af-ipv6-unicast/af-ipv6-attributes/summary-prefix. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__summary_prefix_ipv6','__summary_prefix_level1','__summary_prefix_level2',)

  _yang_name = 'summary-prefix'
  _rest_name = 'summary-prefix'

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
    self.__summary_prefix_ipv6 = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="summary-prefix-ipv6", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='common-def:ipv6-address-prefix', is_config=True)
    self.__summary_prefix_level1 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="summary-prefix-level1", rest_name="Level-1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'For Level-1', u'cli-full-no': None, u'alt-name': u'Level-1'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)
    self.__summary_prefix_level2 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="summary-prefix-level2", rest_name="Level-2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'For Level-2', u'cli-full-no': None, u'alt-name': u'Level-2'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'router', u'isis', u'router-isis-cmds-holder', u'address-family', u'ipv6', u'af-ipv6-unicast', u'af-ipv6-attributes', u'summary-prefix']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'isis', u'address-family', u'ipv6', u'unicast', u'summary-prefix']

  def _get_summary_prefix_ipv6(self):
    """
    Getter method for summary_prefix_ipv6, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/summary_prefix/summary_prefix_ipv6 (common-def:ipv6-address-prefix)
    """
    return self.__summary_prefix_ipv6
      
  def _set_summary_prefix_ipv6(self, v, load=False):
    """
    Setter method for summary_prefix_ipv6, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/summary_prefix/summary_prefix_ipv6 (common-def:ipv6-address-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_summary_prefix_ipv6 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_summary_prefix_ipv6() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="summary-prefix-ipv6", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='common-def:ipv6-address-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """summary_prefix_ipv6 must be of a type compatible with common-def:ipv6-address-prefix""",
          'defined-type': "common-def:ipv6-address-prefix",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="summary-prefix-ipv6", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='common-def:ipv6-address-prefix', is_config=True)""",
        })

    self.__summary_prefix_ipv6 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_summary_prefix_ipv6(self):
    self.__summary_prefix_ipv6 = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="summary-prefix-ipv6", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='common-def:ipv6-address-prefix', is_config=True)


  def _get_summary_prefix_level1(self):
    """
    Getter method for summary_prefix_level1, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/summary_prefix/summary_prefix_level1 (empty)
    """
    return self.__summary_prefix_level1
      
  def _set_summary_prefix_level1(self, v, load=False):
    """
    Setter method for summary_prefix_level1, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/summary_prefix/summary_prefix_level1 (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_summary_prefix_level1 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_summary_prefix_level1() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="summary-prefix-level1", rest_name="Level-1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'For Level-1', u'cli-full-no': None, u'alt-name': u'Level-1'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """summary_prefix_level1 must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="summary-prefix-level1", rest_name="Level-1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'For Level-1', u'cli-full-no': None, u'alt-name': u'Level-1'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)""",
        })

    self.__summary_prefix_level1 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_summary_prefix_level1(self):
    self.__summary_prefix_level1 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="summary-prefix-level1", rest_name="Level-1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'For Level-1', u'cli-full-no': None, u'alt-name': u'Level-1'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)


  def _get_summary_prefix_level2(self):
    """
    Getter method for summary_prefix_level2, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/summary_prefix/summary_prefix_level2 (empty)
    """
    return self.__summary_prefix_level2
      
  def _set_summary_prefix_level2(self, v, load=False):
    """
    Setter method for summary_prefix_level2, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/summary_prefix/summary_prefix_level2 (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_summary_prefix_level2 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_summary_prefix_level2() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="summary-prefix-level2", rest_name="Level-2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'For Level-2', u'cli-full-no': None, u'alt-name': u'Level-2'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """summary_prefix_level2 must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="summary-prefix-level2", rest_name="Level-2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'For Level-2', u'cli-full-no': None, u'alt-name': u'Level-2'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)""",
        })

    self.__summary_prefix_level2 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_summary_prefix_level2(self):
    self.__summary_prefix_level2 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="summary-prefix-level2", rest_name="Level-2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'For Level-2', u'cli-full-no': None, u'alt-name': u'Level-2'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)

  summary_prefix_ipv6 = __builtin__.property(_get_summary_prefix_ipv6, _set_summary_prefix_ipv6)
  summary_prefix_level1 = __builtin__.property(_get_summary_prefix_level1, _set_summary_prefix_level1)
  summary_prefix_level2 = __builtin__.property(_get_summary_prefix_level2, _set_summary_prefix_level2)


  _pyangbind_elements = {'summary_prefix_ipv6': summary_prefix_ipv6, 'summary_prefix_level1': summary_prefix_level1, 'summary_prefix_level2': summary_prefix_level2, }


