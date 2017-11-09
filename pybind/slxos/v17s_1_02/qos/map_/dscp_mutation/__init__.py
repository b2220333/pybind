
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import dscp_to_dscp_mapping
class dscp_mutation(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-mls - based on the path /qos/map/dscp-mutation. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__dscp_mutation_map_name','__dscp_to_dscp_mapping',)

  _yang_name = 'dscp-mutation'
  _rest_name = 'dscp-mutation'

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
    self.__dscp_to_dscp_mapping = YANGDynClass(base=YANGListType("dscp_in_values",dscp_to_dscp_mapping.dscp_to_dscp_mapping, yang_name="dscp-to-dscp-mapping", rest_name="map", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dscp-in-values', extensions={u'tailf-common': {u'info': u'Map DSCP values to outbound DSCP value', u'cli-suppress-mode': None, u'cli-suppress-no': None, u'alt-name': u'map', u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'dscp_mark_list_mutation'}}), is_container='list', yang_name="dscp-to-dscp-mapping", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Map DSCP values to outbound DSCP value', u'cli-suppress-mode': None, u'cli-suppress-no': None, u'alt-name': u'map', u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'dscp_mark_list_mutation'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)
    self.__dscp_mutation_map_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-mutation-map-name", rest_name="dscp-mutation-map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name for the MAP(Max 64)', u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='map-name-type', is_config=True)

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
      return [u'qos', u'map', u'dscp-mutation']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'qos', u'map', u'dscp-mutation']

  def _get_dscp_mutation_map_name(self):
    """
    Getter method for dscp_mutation_map_name, mapped from YANG variable /qos/map/dscp_mutation/dscp_mutation_map_name (map-name-type)
    """
    return self.__dscp_mutation_map_name
      
  def _set_dscp_mutation_map_name(self, v, load=False):
    """
    Setter method for dscp_mutation_map_name, mapped from YANG variable /qos/map/dscp_mutation/dscp_mutation_map_name (map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dscp_mutation_map_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dscp_mutation_map_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-mutation-map-name", rest_name="dscp-mutation-map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name for the MAP(Max 64)', u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dscp_mutation_map_name must be of a type compatible with map-name-type""",
          'defined-type': "brocade-qos-mls:map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-mutation-map-name", rest_name="dscp-mutation-map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name for the MAP(Max 64)', u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='map-name-type', is_config=True)""",
        })

    self.__dscp_mutation_map_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dscp_mutation_map_name(self):
    self.__dscp_mutation_map_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-mutation-map-name", rest_name="dscp-mutation-map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name for the MAP(Max 64)', u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='map-name-type', is_config=True)


  def _get_dscp_to_dscp_mapping(self):
    """
    Getter method for dscp_to_dscp_mapping, mapped from YANG variable /qos/map/dscp_mutation/dscp_to_dscp_mapping (list)
    """
    return self.__dscp_to_dscp_mapping
      
  def _set_dscp_to_dscp_mapping(self, v, load=False):
    """
    Setter method for dscp_to_dscp_mapping, mapped from YANG variable /qos/map/dscp_mutation/dscp_to_dscp_mapping (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dscp_to_dscp_mapping is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dscp_to_dscp_mapping() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("dscp_in_values",dscp_to_dscp_mapping.dscp_to_dscp_mapping, yang_name="dscp-to-dscp-mapping", rest_name="map", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dscp-in-values', extensions={u'tailf-common': {u'info': u'Map DSCP values to outbound DSCP value', u'cli-suppress-mode': None, u'cli-suppress-no': None, u'alt-name': u'map', u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'dscp_mark_list_mutation'}}), is_container='list', yang_name="dscp-to-dscp-mapping", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Map DSCP values to outbound DSCP value', u'cli-suppress-mode': None, u'cli-suppress-no': None, u'alt-name': u'map', u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'dscp_mark_list_mutation'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dscp_to_dscp_mapping must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("dscp_in_values",dscp_to_dscp_mapping.dscp_to_dscp_mapping, yang_name="dscp-to-dscp-mapping", rest_name="map", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dscp-in-values', extensions={u'tailf-common': {u'info': u'Map DSCP values to outbound DSCP value', u'cli-suppress-mode': None, u'cli-suppress-no': None, u'alt-name': u'map', u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'dscp_mark_list_mutation'}}), is_container='list', yang_name="dscp-to-dscp-mapping", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Map DSCP values to outbound DSCP value', u'cli-suppress-mode': None, u'cli-suppress-no': None, u'alt-name': u'map', u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'dscp_mark_list_mutation'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)""",
        })

    self.__dscp_to_dscp_mapping = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dscp_to_dscp_mapping(self):
    self.__dscp_to_dscp_mapping = YANGDynClass(base=YANGListType("dscp_in_values",dscp_to_dscp_mapping.dscp_to_dscp_mapping, yang_name="dscp-to-dscp-mapping", rest_name="map", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dscp-in-values', extensions={u'tailf-common': {u'info': u'Map DSCP values to outbound DSCP value', u'cli-suppress-mode': None, u'cli-suppress-no': None, u'alt-name': u'map', u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'dscp_mark_list_mutation'}}), is_container='list', yang_name="dscp-to-dscp-mapping", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Map DSCP values to outbound DSCP value', u'cli-suppress-mode': None, u'cli-suppress-no': None, u'alt-name': u'map', u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'dscp_mark_list_mutation'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)

  dscp_mutation_map_name = __builtin__.property(_get_dscp_mutation_map_name, _set_dscp_mutation_map_name)
  dscp_to_dscp_mapping = __builtin__.property(_get_dscp_to_dscp_mapping, _set_dscp_to_dscp_mapping)


  _pyangbind_elements = {'dscp_mutation_map_name': dscp_mutation_map_name, 'dscp_to_dscp_mapping': dscp_to_dscp_mapping, }


