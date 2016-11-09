
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class autobw_threshold_table_bandwidth(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /mpls-config/router/mpls/mpls-cmds-holder/autobw-threshold-table/autobw-threshold-table-bandwidth. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__bandwidth_value','__autobw_threshold_table_threshold',)

  _yang_name = 'autobw-threshold-table-bandwidth'
  _rest_name = 'bandwidth'

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
    self.__autobw_threshold_table_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..2147483647']}), is_leaf=True, yang_name="autobw-threshold-table-threshold", rest_name="threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'DECIMAL;;Absolute threshold value for the bandwidth', u'alt-name': u'threshold'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__bandwidth_value = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..2147483647']}), is_leaf=True, yang_name="bandwidth-value", rest_name="bandwidth-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'DECIMAL;;Bandwidth upto which threshold will apply', u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

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
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'autobw-threshold-table', u'autobw-threshold-table-bandwidth']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'mpls', u'autobw-threshold-table', u'bandwidth']

  def _get_bandwidth_value(self):
    """
    Getter method for bandwidth_value, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_threshold_table/autobw_threshold_table_bandwidth/bandwidth_value (uint32)
    """
    return self.__bandwidth_value
      
  def _set_bandwidth_value(self, v, load=False):
    """
    Setter method for bandwidth_value, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_threshold_table/autobw_threshold_table_bandwidth/bandwidth_value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bandwidth_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bandwidth_value() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..2147483647']}), is_leaf=True, yang_name="bandwidth-value", rest_name="bandwidth-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'DECIMAL;;Bandwidth upto which threshold will apply', u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bandwidth_value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..2147483647']}), is_leaf=True, yang_name="bandwidth-value", rest_name="bandwidth-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'DECIMAL;;Bandwidth upto which threshold will apply', u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__bandwidth_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bandwidth_value(self):
    self.__bandwidth_value = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..2147483647']}), is_leaf=True, yang_name="bandwidth-value", rest_name="bandwidth-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'DECIMAL;;Bandwidth upto which threshold will apply', u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_autobw_threshold_table_threshold(self):
    """
    Getter method for autobw_threshold_table_threshold, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_threshold_table/autobw_threshold_table_bandwidth/autobw_threshold_table_threshold (uint32)
    """
    return self.__autobw_threshold_table_threshold
      
  def _set_autobw_threshold_table_threshold(self, v, load=False):
    """
    Setter method for autobw_threshold_table_threshold, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_threshold_table/autobw_threshold_table_bandwidth/autobw_threshold_table_threshold (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_autobw_threshold_table_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_autobw_threshold_table_threshold() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..2147483647']}), is_leaf=True, yang_name="autobw-threshold-table-threshold", rest_name="threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'DECIMAL;;Absolute threshold value for the bandwidth', u'alt-name': u'threshold'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """autobw_threshold_table_threshold must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..2147483647']}), is_leaf=True, yang_name="autobw-threshold-table-threshold", rest_name="threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'DECIMAL;;Absolute threshold value for the bandwidth', u'alt-name': u'threshold'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__autobw_threshold_table_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_autobw_threshold_table_threshold(self):
    self.__autobw_threshold_table_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..2147483647']}), is_leaf=True, yang_name="autobw-threshold-table-threshold", rest_name="threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'DECIMAL;;Absolute threshold value for the bandwidth', u'alt-name': u'threshold'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

  bandwidth_value = __builtin__.property(_get_bandwidth_value, _set_bandwidth_value)
  autobw_threshold_table_threshold = __builtin__.property(_get_autobw_threshold_table_threshold, _set_autobw_threshold_table_threshold)


  _pyangbind_elements = {'bandwidth_value': bandwidth_value, 'autobw_threshold_table_threshold': autobw_threshold_table_threshold, }


