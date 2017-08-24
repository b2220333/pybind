
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ingress(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/fortygigabitethernet/storm-control/ingress. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__protocol_type','__rate_format','__rate_bps','__rate_percent','__bum_action',)

  _yang_name = 'ingress'
  _rest_name = 'ingress'

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
    self.__rate_percent = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="rate-percent", rest_name="rate-percent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u"../rate-format = 'limit-percent'"}}, namespace='urn:brocade.com:mgmt:brocade-bum-storm-control', defining_module='brocade-bum-storm-control', yang_type='percentage-rate-limit', is_config=True)
    self.__bum_action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'monitor': {'value': 2}, u'shutdown': {'value': 3}},), is_leaf=True, yang_name="bum-action", rest_name="bum-action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-bum-storm-control', defining_module='brocade-bum-storm-control', yang_type='enumeration', is_config=True)
    self.__rate_format = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'limit-bps': {'value': 1}, u'limit-percent': {'value': 2}},), is_leaf=True, yang_name="rate-format", rest_name="rate-format", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bum-storm-control', defining_module='brocade-bum-storm-control', yang_type='enumeration', is_config=True)
    self.__rate_bps = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), restriction_dict={'range': [u'0 .. 100000000000']}), is_leaf=True, yang_name="rate-bps", rest_name="rate-bps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u"../rate-format = 'limit-bps'", u'cli-completion-actionpoint': u'storm-control-show-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-bum-storm-control', defining_module='brocade-bum-storm-control', yang_type='bps-rate-limit', is_config=True)
    self.__protocol_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'broadcast': {'value': 1}, u'unknown-unicast': {'value': 3}, u'multicast': {'value': 2}},), is_leaf=True, yang_name="protocol-type", rest_name="protocol-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bum-storm-control', defining_module='brocade-bum-storm-control', yang_type='enumeration', is_config=True)

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
      return [u'interface', u'fortygigabitethernet', u'storm-control', u'ingress']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'FortyGigabitEthernet', u'storm-control', u'ingress']

  def _get_protocol_type(self):
    """
    Getter method for protocol_type, mapped from YANG variable /interface/fortygigabitethernet/storm_control/ingress/protocol_type (enumeration)
    """
    return self.__protocol_type
      
  def _set_protocol_type(self, v, load=False):
    """
    Setter method for protocol_type, mapped from YANG variable /interface/fortygigabitethernet/storm_control/ingress/protocol_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protocol_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protocol_type() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'broadcast': {'value': 1}, u'unknown-unicast': {'value': 3}, u'multicast': {'value': 2}},), is_leaf=True, yang_name="protocol-type", rest_name="protocol-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bum-storm-control', defining_module='brocade-bum-storm-control', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protocol_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-bum-storm-control:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'broadcast': {'value': 1}, u'unknown-unicast': {'value': 3}, u'multicast': {'value': 2}},), is_leaf=True, yang_name="protocol-type", rest_name="protocol-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bum-storm-control', defining_module='brocade-bum-storm-control', yang_type='enumeration', is_config=True)""",
        })

    self.__protocol_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protocol_type(self):
    self.__protocol_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'broadcast': {'value': 1}, u'unknown-unicast': {'value': 3}, u'multicast': {'value': 2}},), is_leaf=True, yang_name="protocol-type", rest_name="protocol-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bum-storm-control', defining_module='brocade-bum-storm-control', yang_type='enumeration', is_config=True)


  def _get_rate_format(self):
    """
    Getter method for rate_format, mapped from YANG variable /interface/fortygigabitethernet/storm_control/ingress/rate_format (enumeration)
    """
    return self.__rate_format
      
  def _set_rate_format(self, v, load=False):
    """
    Setter method for rate_format, mapped from YANG variable /interface/fortygigabitethernet/storm_control/ingress/rate_format (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rate_format is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rate_format() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'limit-bps': {'value': 1}, u'limit-percent': {'value': 2}},), is_leaf=True, yang_name="rate-format", rest_name="rate-format", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bum-storm-control', defining_module='brocade-bum-storm-control', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rate_format must be of a type compatible with enumeration""",
          'defined-type': "brocade-bum-storm-control:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'limit-bps': {'value': 1}, u'limit-percent': {'value': 2}},), is_leaf=True, yang_name="rate-format", rest_name="rate-format", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bum-storm-control', defining_module='brocade-bum-storm-control', yang_type='enumeration', is_config=True)""",
        })

    self.__rate_format = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rate_format(self):
    self.__rate_format = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'limit-bps': {'value': 1}, u'limit-percent': {'value': 2}},), is_leaf=True, yang_name="rate-format", rest_name="rate-format", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bum-storm-control', defining_module='brocade-bum-storm-control', yang_type='enumeration', is_config=True)


  def _get_rate_bps(self):
    """
    Getter method for rate_bps, mapped from YANG variable /interface/fortygigabitethernet/storm_control/ingress/rate_bps (bps-rate-limit)
    """
    return self.__rate_bps
      
  def _set_rate_bps(self, v, load=False):
    """
    Setter method for rate_bps, mapped from YANG variable /interface/fortygigabitethernet/storm_control/ingress/rate_bps (bps-rate-limit)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rate_bps is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rate_bps() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), restriction_dict={'range': [u'0 .. 100000000000']}), is_leaf=True, yang_name="rate-bps", rest_name="rate-bps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u"../rate-format = 'limit-bps'", u'cli-completion-actionpoint': u'storm-control-show-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-bum-storm-control', defining_module='brocade-bum-storm-control', yang_type='bps-rate-limit', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rate_bps must be of a type compatible with bps-rate-limit""",
          'defined-type': "brocade-bum-storm-control:bps-rate-limit",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), restriction_dict={'range': [u'0 .. 100000000000']}), is_leaf=True, yang_name="rate-bps", rest_name="rate-bps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u"../rate-format = 'limit-bps'", u'cli-completion-actionpoint': u'storm-control-show-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-bum-storm-control', defining_module='brocade-bum-storm-control', yang_type='bps-rate-limit', is_config=True)""",
        })

    self.__rate_bps = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rate_bps(self):
    self.__rate_bps = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), restriction_dict={'range': [u'0 .. 100000000000']}), is_leaf=True, yang_name="rate-bps", rest_name="rate-bps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u"../rate-format = 'limit-bps'", u'cli-completion-actionpoint': u'storm-control-show-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-bum-storm-control', defining_module='brocade-bum-storm-control', yang_type='bps-rate-limit', is_config=True)


  def _get_rate_percent(self):
    """
    Getter method for rate_percent, mapped from YANG variable /interface/fortygigabitethernet/storm_control/ingress/rate_percent (percentage-rate-limit)
    """
    return self.__rate_percent
      
  def _set_rate_percent(self, v, load=False):
    """
    Setter method for rate_percent, mapped from YANG variable /interface/fortygigabitethernet/storm_control/ingress/rate_percent (percentage-rate-limit)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rate_percent is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rate_percent() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="rate-percent", rest_name="rate-percent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u"../rate-format = 'limit-percent'"}}, namespace='urn:brocade.com:mgmt:brocade-bum-storm-control', defining_module='brocade-bum-storm-control', yang_type='percentage-rate-limit', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rate_percent must be of a type compatible with percentage-rate-limit""",
          'defined-type': "brocade-bum-storm-control:percentage-rate-limit",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="rate-percent", rest_name="rate-percent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u"../rate-format = 'limit-percent'"}}, namespace='urn:brocade.com:mgmt:brocade-bum-storm-control', defining_module='brocade-bum-storm-control', yang_type='percentage-rate-limit', is_config=True)""",
        })

    self.__rate_percent = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rate_percent(self):
    self.__rate_percent = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="rate-percent", rest_name="rate-percent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u"../rate-format = 'limit-percent'"}}, namespace='urn:brocade.com:mgmt:brocade-bum-storm-control', defining_module='brocade-bum-storm-control', yang_type='percentage-rate-limit', is_config=True)


  def _get_bum_action(self):
    """
    Getter method for bum_action, mapped from YANG variable /interface/fortygigabitethernet/storm_control/ingress/bum_action (enumeration)
    """
    return self.__bum_action
      
  def _set_bum_action(self, v, load=False):
    """
    Setter method for bum_action, mapped from YANG variable /interface/fortygigabitethernet/storm_control/ingress/bum_action (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bum_action is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bum_action() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'monitor': {'value': 2}, u'shutdown': {'value': 3}},), is_leaf=True, yang_name="bum-action", rest_name="bum-action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-bum-storm-control', defining_module='brocade-bum-storm-control', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bum_action must be of a type compatible with enumeration""",
          'defined-type': "brocade-bum-storm-control:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'monitor': {'value': 2}, u'shutdown': {'value': 3}},), is_leaf=True, yang_name="bum-action", rest_name="bum-action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-bum-storm-control', defining_module='brocade-bum-storm-control', yang_type='enumeration', is_config=True)""",
        })

    self.__bum_action = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bum_action(self):
    self.__bum_action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'monitor': {'value': 2}, u'shutdown': {'value': 3}},), is_leaf=True, yang_name="bum-action", rest_name="bum-action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-bum-storm-control', defining_module='brocade-bum-storm-control', yang_type='enumeration', is_config=True)

  protocol_type = __builtin__.property(_get_protocol_type, _set_protocol_type)
  rate_format = __builtin__.property(_get_rate_format, _set_rate_format)
  rate_bps = __builtin__.property(_get_rate_bps, _set_rate_bps)
  rate_percent = __builtin__.property(_get_rate_percent, _set_rate_percent)
  bum_action = __builtin__.property(_get_bum_action, _set_bum_action)


  _pyangbind_elements = {'protocol_type': protocol_type, 'rate_format': rate_format, 'rate_bps': rate_bps, 'rate_percent': rate_percent, 'bum_action': bum_action, }


