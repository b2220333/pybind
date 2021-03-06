
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class fe_access_check(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-sysmon - based on the path /sysmon/fe-access-check. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__fe_access_check_disable','__fe_access_check_interval','__fe_access_check_threshold','__fe_access_check_recovery_threshold','__fe_access_check_action',)

  _yang_name = 'fe-access-check'
  _rest_name = 'fe-access-check'

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
    self.__fe_access_check_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1 .. 10']}), is_leaf=True, yang_name="fe-access-check-threshold", rest_name="threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'fe-access-check-th', u'cli-full-no': None, u'info': u'Set Fe-Access-Check threshold', u'alt-name': u'threshold'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='uint8', is_config=True)
    self.__fe_access_check_action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'recover': {'value': 3}, u'log': {'value': 1}},), is_leaf=True, yang_name="fe-access-check-action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'fe-access-check-act', u'cli-full-no': None, u'info': u'Set Fe-Access-Check action', u'alt-name': u'action'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='enumeration', is_config=True)
    self.__fe_access_check_recovery_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1 .. 3']}), is_leaf=True, yang_name="fe-access-check-recovery-threshold", rest_name="recovery-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'fe-access-check-rec-th', u'cli-full-no': None, u'info': u'Set Fe-Access-Check recovery threshold', u'alt-name': u'recovery-threshold'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='uint8', is_config=True)
    self.__fe_access_check_disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fe-access-check-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'fe-access-check-dis', u'cli-full-no': None, u'info': u'Disable Fe Access Check (Default: Enabled)', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='empty', is_config=True)
    self.__fe_access_check_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1 .. 300']}), is_leaf=True, yang_name="fe-access-check-interval", rest_name="poll-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'fe-access-check-intvl', u'cli-full-no': None, u'info': u'Set Fe-Access-Check poll-interval', u'alt-name': u'poll-interval'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='uint16', is_config=True)

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
      return [u'sysmon', u'fe-access-check']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'sysmon', u'fe-access-check']

  def _get_fe_access_check_disable(self):
    """
    Getter method for fe_access_check_disable, mapped from YANG variable /sysmon/fe_access_check/fe_access_check_disable (empty)
    """
    return self.__fe_access_check_disable
      
  def _set_fe_access_check_disable(self, v, load=False):
    """
    Setter method for fe_access_check_disable, mapped from YANG variable /sysmon/fe_access_check/fe_access_check_disable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fe_access_check_disable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fe_access_check_disable() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="fe-access-check-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'fe-access-check-dis', u'cli-full-no': None, u'info': u'Disable Fe Access Check (Default: Enabled)', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fe_access_check_disable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fe-access-check-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'fe-access-check-dis', u'cli-full-no': None, u'info': u'Disable Fe Access Check (Default: Enabled)', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='empty', is_config=True)""",
        })

    self.__fe_access_check_disable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fe_access_check_disable(self):
    self.__fe_access_check_disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fe-access-check-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'fe-access-check-dis', u'cli-full-no': None, u'info': u'Disable Fe Access Check (Default: Enabled)', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='empty', is_config=True)


  def _get_fe_access_check_interval(self):
    """
    Getter method for fe_access_check_interval, mapped from YANG variable /sysmon/fe_access_check/fe_access_check_interval (uint16)
    """
    return self.__fe_access_check_interval
      
  def _set_fe_access_check_interval(self, v, load=False):
    """
    Setter method for fe_access_check_interval, mapped from YANG variable /sysmon/fe_access_check/fe_access_check_interval (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fe_access_check_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fe_access_check_interval() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1 .. 300']}), is_leaf=True, yang_name="fe-access-check-interval", rest_name="poll-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'fe-access-check-intvl', u'cli-full-no': None, u'info': u'Set Fe-Access-Check poll-interval', u'alt-name': u'poll-interval'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fe_access_check_interval must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1 .. 300']}), is_leaf=True, yang_name="fe-access-check-interval", rest_name="poll-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'fe-access-check-intvl', u'cli-full-no': None, u'info': u'Set Fe-Access-Check poll-interval', u'alt-name': u'poll-interval'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='uint16', is_config=True)""",
        })

    self.__fe_access_check_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fe_access_check_interval(self):
    self.__fe_access_check_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1 .. 300']}), is_leaf=True, yang_name="fe-access-check-interval", rest_name="poll-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'fe-access-check-intvl', u'cli-full-no': None, u'info': u'Set Fe-Access-Check poll-interval', u'alt-name': u'poll-interval'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='uint16', is_config=True)


  def _get_fe_access_check_threshold(self):
    """
    Getter method for fe_access_check_threshold, mapped from YANG variable /sysmon/fe_access_check/fe_access_check_threshold (uint8)
    """
    return self.__fe_access_check_threshold
      
  def _set_fe_access_check_threshold(self, v, load=False):
    """
    Setter method for fe_access_check_threshold, mapped from YANG variable /sysmon/fe_access_check/fe_access_check_threshold (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fe_access_check_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fe_access_check_threshold() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1 .. 10']}), is_leaf=True, yang_name="fe-access-check-threshold", rest_name="threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'fe-access-check-th', u'cli-full-no': None, u'info': u'Set Fe-Access-Check threshold', u'alt-name': u'threshold'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fe_access_check_threshold must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1 .. 10']}), is_leaf=True, yang_name="fe-access-check-threshold", rest_name="threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'fe-access-check-th', u'cli-full-no': None, u'info': u'Set Fe-Access-Check threshold', u'alt-name': u'threshold'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='uint8', is_config=True)""",
        })

    self.__fe_access_check_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fe_access_check_threshold(self):
    self.__fe_access_check_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1 .. 10']}), is_leaf=True, yang_name="fe-access-check-threshold", rest_name="threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'fe-access-check-th', u'cli-full-no': None, u'info': u'Set Fe-Access-Check threshold', u'alt-name': u'threshold'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='uint8', is_config=True)


  def _get_fe_access_check_recovery_threshold(self):
    """
    Getter method for fe_access_check_recovery_threshold, mapped from YANG variable /sysmon/fe_access_check/fe_access_check_recovery_threshold (uint8)
    """
    return self.__fe_access_check_recovery_threshold
      
  def _set_fe_access_check_recovery_threshold(self, v, load=False):
    """
    Setter method for fe_access_check_recovery_threshold, mapped from YANG variable /sysmon/fe_access_check/fe_access_check_recovery_threshold (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fe_access_check_recovery_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fe_access_check_recovery_threshold() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1 .. 3']}), is_leaf=True, yang_name="fe-access-check-recovery-threshold", rest_name="recovery-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'fe-access-check-rec-th', u'cli-full-no': None, u'info': u'Set Fe-Access-Check recovery threshold', u'alt-name': u'recovery-threshold'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fe_access_check_recovery_threshold must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1 .. 3']}), is_leaf=True, yang_name="fe-access-check-recovery-threshold", rest_name="recovery-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'fe-access-check-rec-th', u'cli-full-no': None, u'info': u'Set Fe-Access-Check recovery threshold', u'alt-name': u'recovery-threshold'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='uint8', is_config=True)""",
        })

    self.__fe_access_check_recovery_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fe_access_check_recovery_threshold(self):
    self.__fe_access_check_recovery_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1 .. 3']}), is_leaf=True, yang_name="fe-access-check-recovery-threshold", rest_name="recovery-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'fe-access-check-rec-th', u'cli-full-no': None, u'info': u'Set Fe-Access-Check recovery threshold', u'alt-name': u'recovery-threshold'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='uint8', is_config=True)


  def _get_fe_access_check_action(self):
    """
    Getter method for fe_access_check_action, mapped from YANG variable /sysmon/fe_access_check/fe_access_check_action (enumeration)
    """
    return self.__fe_access_check_action
      
  def _set_fe_access_check_action(self, v, load=False):
    """
    Setter method for fe_access_check_action, mapped from YANG variable /sysmon/fe_access_check/fe_access_check_action (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fe_access_check_action is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fe_access_check_action() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'recover': {'value': 3}, u'log': {'value': 1}},), is_leaf=True, yang_name="fe-access-check-action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'fe-access-check-act', u'cli-full-no': None, u'info': u'Set Fe-Access-Check action', u'alt-name': u'action'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fe_access_check_action must be of a type compatible with enumeration""",
          'defined-type': "brocade-sysmon:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'recover': {'value': 3}, u'log': {'value': 1}},), is_leaf=True, yang_name="fe-access-check-action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'fe-access-check-act', u'cli-full-no': None, u'info': u'Set Fe-Access-Check action', u'alt-name': u'action'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='enumeration', is_config=True)""",
        })

    self.__fe_access_check_action = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fe_access_check_action(self):
    self.__fe_access_check_action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'recover': {'value': 3}, u'log': {'value': 1}},), is_leaf=True, yang_name="fe-access-check-action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'fe-access-check-act', u'cli-full-no': None, u'info': u'Set Fe-Access-Check action', u'alt-name': u'action'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='enumeration', is_config=True)

  fe_access_check_disable = __builtin__.property(_get_fe_access_check_disable, _set_fe_access_check_disable)
  fe_access_check_interval = __builtin__.property(_get_fe_access_check_interval, _set_fe_access_check_interval)
  fe_access_check_threshold = __builtin__.property(_get_fe_access_check_threshold, _set_fe_access_check_threshold)
  fe_access_check_recovery_threshold = __builtin__.property(_get_fe_access_check_recovery_threshold, _set_fe_access_check_recovery_threshold)
  fe_access_check_action = __builtin__.property(_get_fe_access_check_action, _set_fe_access_check_action)


  _pyangbind_elements = {'fe_access_check_disable': fe_access_check_disable, 'fe_access_check_interval': fe_access_check_interval, 'fe_access_check_threshold': fe_access_check_threshold, 'fe_access_check_recovery_threshold': fe_access_check_recovery_threshold, 'fe_access_check_action': fe_access_check_action, }


