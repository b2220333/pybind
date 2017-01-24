
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class redistribute(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/ospf/permit/redistribute. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__redist_value','__route_option','__address','__mask','__set_metric_val','__match_metric_val',)

  _yang_name = 'redistribute'
  _rest_name = 'redistribute'

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
    self.__redist_value = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..64']}), is_leaf=True, yang_name="redist-value", rest_name="redist-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number', u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)
    self.__set_metric_val = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="set-metric-val", rest_name="set-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Metric value', u'alt-name': u'set-metric'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)
    self.__mask = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mask", rest_name="mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Subnet Mask', u'cli-drop-node-name': None, u'display-when': u'(../address)', u'cli-break-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='inet:ipv4-address', is_config=True)
    self.__route_option = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'static': {'value': 4}, u'all': {'value': 1}, u'connected': {'value': 2}},), is_leaf=True, yang_name="route-option", rest_name="route-option", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'OSPF route option'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='route-option-type', is_config=True)
    self.__match_metric_val = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="match-metric-val", rest_name="match-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Metric value', u'alt-name': u'match-metric'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)
    self.__address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="address", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP address', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='inet:ipv4-address', is_config=True)

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
      return [u'rbridge-id', u'router', u'ospf', u'permit', u'redistribute']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'ospf', u'permit', u'redistribute']

  def _get_redist_value(self):
    """
    Getter method for redist_value, mapped from YANG variable /rbridge_id/router/ospf/permit/redistribute/redist_value (uint32)
    """
    return self.__redist_value
      
  def _set_redist_value(self, v, load=False):
    """
    Setter method for redist_value, mapped from YANG variable /rbridge_id/router/ospf/permit/redistribute/redist_value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redist_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redist_value() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..64']}), is_leaf=True, yang_name="redist-value", rest_name="redist-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number', u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redist_value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..64']}), is_leaf=True, yang_name="redist-value", rest_name="redist-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number', u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)""",
        })

    self.__redist_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redist_value(self):
    self.__redist_value = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..64']}), is_leaf=True, yang_name="redist-value", rest_name="redist-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number', u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)


  def _get_route_option(self):
    """
    Getter method for route_option, mapped from YANG variable /rbridge_id/router/ospf/permit/redistribute/route_option (route-option-type)
    """
    return self.__route_option
      
  def _set_route_option(self, v, load=False):
    """
    Setter method for route_option, mapped from YANG variable /rbridge_id/router/ospf/permit/redistribute/route_option (route-option-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_option is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_option() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'static': {'value': 4}, u'all': {'value': 1}, u'connected': {'value': 2}},), is_leaf=True, yang_name="route-option", rest_name="route-option", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'OSPF route option'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='route-option-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_option must be of a type compatible with route-option-type""",
          'defined-type': "brocade-ospf:route-option-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'static': {'value': 4}, u'all': {'value': 1}, u'connected': {'value': 2}},), is_leaf=True, yang_name="route-option", rest_name="route-option", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'OSPF route option'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='route-option-type', is_config=True)""",
        })

    self.__route_option = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_option(self):
    self.__route_option = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'static': {'value': 4}, u'all': {'value': 1}, u'connected': {'value': 2}},), is_leaf=True, yang_name="route-option", rest_name="route-option", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'OSPF route option'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='route-option-type', is_config=True)


  def _get_address(self):
    """
    Getter method for address, mapped from YANG variable /rbridge_id/router/ospf/permit/redistribute/address (inet:ipv4-address)
    """
    return self.__address
      
  def _set_address(self, v, load=False):
    """
    Setter method for address, mapped from YANG variable /rbridge_id/router/ospf/permit/redistribute/address (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="address", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP address', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="address", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP address', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address(self):
    self.__address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="address", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP address', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='inet:ipv4-address', is_config=True)


  def _get_mask(self):
    """
    Getter method for mask, mapped from YANG variable /rbridge_id/router/ospf/permit/redistribute/mask (inet:ipv4-address)
    """
    return self.__mask
      
  def _set_mask(self, v, load=False):
    """
    Setter method for mask, mapped from YANG variable /rbridge_id/router/ospf/permit/redistribute/mask (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mask is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mask() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mask", rest_name="mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Subnet Mask', u'cli-drop-node-name': None, u'display-when': u'(../address)', u'cli-break-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mask must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mask", rest_name="mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Subnet Mask', u'cli-drop-node-name': None, u'display-when': u'(../address)', u'cli-break-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__mask = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mask(self):
    self.__mask = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mask", rest_name="mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Subnet Mask', u'cli-drop-node-name': None, u'display-when': u'(../address)', u'cli-break-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='inet:ipv4-address', is_config=True)


  def _get_set_metric_val(self):
    """
    Getter method for set_metric_val, mapped from YANG variable /rbridge_id/router/ospf/permit/redistribute/set_metric_val (uint32)
    """
    return self.__set_metric_val
      
  def _set_set_metric_val(self, v, load=False):
    """
    Setter method for set_metric_val, mapped from YANG variable /rbridge_id/router/ospf/permit/redistribute/set_metric_val (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_metric_val is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_metric_val() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="set-metric-val", rest_name="set-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Metric value', u'alt-name': u'set-metric'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_metric_val must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="set-metric-val", rest_name="set-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Metric value', u'alt-name': u'set-metric'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)""",
        })

    self.__set_metric_val = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_metric_val(self):
    self.__set_metric_val = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="set-metric-val", rest_name="set-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Metric value', u'alt-name': u'set-metric'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)


  def _get_match_metric_val(self):
    """
    Getter method for match_metric_val, mapped from YANG variable /rbridge_id/router/ospf/permit/redistribute/match_metric_val (uint32)
    """
    return self.__match_metric_val
      
  def _set_match_metric_val(self, v, load=False):
    """
    Setter method for match_metric_val, mapped from YANG variable /rbridge_id/router/ospf/permit/redistribute/match_metric_val (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_match_metric_val is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_match_metric_val() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="match-metric-val", rest_name="match-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Metric value', u'alt-name': u'match-metric'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """match_metric_val must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="match-metric-val", rest_name="match-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Metric value', u'alt-name': u'match-metric'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)""",
        })

    self.__match_metric_val = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_match_metric_val(self):
    self.__match_metric_val = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="match-metric-val", rest_name="match-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Metric value', u'alt-name': u'match-metric'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)

  redist_value = __builtin__.property(_get_redist_value, _set_redist_value)
  route_option = __builtin__.property(_get_route_option, _set_route_option)
  address = __builtin__.property(_get_address, _set_address)
  mask = __builtin__.property(_get_mask, _set_mask)
  set_metric_val = __builtin__.property(_get_set_metric_val, _set_set_metric_val)
  match_metric_val = __builtin__.property(_get_match_metric_val, _set_match_metric_val)


  _pyangbind_elements = {'redist_value': redist_value, 'route_option': route_option, 'address': address, 'mask': mask, 'set_metric_val': set_metric_val, 'match_metric_val': match_metric_val, }


