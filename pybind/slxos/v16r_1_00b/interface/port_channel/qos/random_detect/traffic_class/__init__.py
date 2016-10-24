
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class traffic_class(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/port-channel/qos/random-detect/traffic-class. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__red_tc_value','__red_profile_id',)

  _yang_name = 'traffic-class'
  _rest_name = 'traffic-class'

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
    self.__red_tc_value = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="red-tc-value", rest_name="red-tc-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='traffic-class-id-type', is_config=True)
    self.__red_profile_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 383']}), is_leaf=True, yang_name="red-profile-id", rest_name="red-profile-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Keyword for all other VDX platforms'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='uint32', is_config=True)

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
      return [u'interface', u'port-channel', u'qos', u'random-detect', u'traffic-class']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Port-channel', u'qos', u'random-detect', u'traffic-class']

  def _get_red_tc_value(self):
    """
    Getter method for red_tc_value, mapped from YANG variable /interface/port_channel/qos/random_detect/traffic_class/red_tc_value (traffic-class-id-type)
    """
    return self.__red_tc_value
      
  def _set_red_tc_value(self, v, load=False):
    """
    Setter method for red_tc_value, mapped from YANG variable /interface/port_channel/qos/random_detect/traffic_class/red_tc_value (traffic-class-id-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_red_tc_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_red_tc_value() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="red-tc-value", rest_name="red-tc-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='traffic-class-id-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """red_tc_value must be of a type compatible with traffic-class-id-type""",
          'defined-type': "brocade-qos-mls:traffic-class-id-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="red-tc-value", rest_name="red-tc-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='traffic-class-id-type', is_config=True)""",
        })

    self.__red_tc_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_red_tc_value(self):
    self.__red_tc_value = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="red-tc-value", rest_name="red-tc-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='traffic-class-id-type', is_config=True)


  def _get_red_profile_id(self):
    """
    Getter method for red_profile_id, mapped from YANG variable /interface/port_channel/qos/random_detect/traffic_class/red_profile_id (uint32)

    YANG Description: Keyword for all other VDX platforms
    """
    return self.__red_profile_id
      
  def _set_red_profile_id(self, v, load=False):
    """
    Setter method for red_profile_id, mapped from YANG variable /interface/port_channel/qos/random_detect/traffic_class/red_profile_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_red_profile_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_red_profile_id() directly.

    YANG Description: Keyword for all other VDX platforms
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 383']}), is_leaf=True, yang_name="red-profile-id", rest_name="red-profile-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Keyword for all other VDX platforms'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """red_profile_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 383']}), is_leaf=True, yang_name="red-profile-id", rest_name="red-profile-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Keyword for all other VDX platforms'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='uint32', is_config=True)""",
        })

    self.__red_profile_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_red_profile_id(self):
    self.__red_profile_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 383']}), is_leaf=True, yang_name="red-profile-id", rest_name="red-profile-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Keyword for all other VDX platforms'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='uint32', is_config=True)

  red_tc_value = __builtin__.property(_get_red_tc_value, _set_red_tc_value)
  red_profile_id = __builtin__.property(_get_red_profile_id, _set_red_profile_id)


  _pyangbind_elements = {'red_tc_value': red_tc_value, 'red_profile_id': red_profile_id, }


