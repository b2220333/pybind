
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class msgId(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ras - based on the path /logging/raslog/message/msgId. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__msgId','__severity','__suppress','__syslog',)

  _yang_name = 'msgId'
  _rest_name = 'msgId'

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
    self.__syslog = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="syslog", rest_name="syslog", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable syslog logging for internal raslog message'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='empty', is_config=True)
    self.__msgId = YANGDynClass(base=unicode, is_leaf=True, yang_name="msgId", rest_name="msgId", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify the Msg ID'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='string', is_config=True)
    self.__severity = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INFO': {'value': 1}, u'CRITICAL': {'value': 4}, u'WARNING': {'value': 3}, u'DEFAULT': {'value': 5}, u'ERROR': {'value': 2}},), is_leaf=True, yang_name="severity", rest_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure raslog message severity', u'hidden': u'debug'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='message-severity', is_config=True)
    self.__suppress = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="suppress", rest_name="suppress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Suppress raslog message'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='empty', is_config=True)

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
      return [u'logging', u'raslog', u'message', u'msgId']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'logging', u'raslog', u'message', u'msgId']

  def _get_msgId(self):
    """
    Getter method for msgId, mapped from YANG variable /logging/raslog/message/msgId/msgId (string)
    """
    return self.__msgId
      
  def _set_msgId(self, v, load=False):
    """
    Setter method for msgId, mapped from YANG variable /logging/raslog/message/msgId/msgId (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_msgId is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_msgId() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="msgId", rest_name="msgId", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify the Msg ID'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """msgId must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="msgId", rest_name="msgId", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify the Msg ID'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='string', is_config=True)""",
        })

    self.__msgId = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_msgId(self):
    self.__msgId = YANGDynClass(base=unicode, is_leaf=True, yang_name="msgId", rest_name="msgId", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify the Msg ID'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='string', is_config=True)


  def _get_severity(self):
    """
    Getter method for severity, mapped from YANG variable /logging/raslog/message/msgId/severity (message-severity)
    """
    return self.__severity
      
  def _set_severity(self, v, load=False):
    """
    Setter method for severity, mapped from YANG variable /logging/raslog/message/msgId/severity (message-severity)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_severity is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_severity() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INFO': {'value': 1}, u'CRITICAL': {'value': 4}, u'WARNING': {'value': 3}, u'DEFAULT': {'value': 5}, u'ERROR': {'value': 2}},), is_leaf=True, yang_name="severity", rest_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure raslog message severity', u'hidden': u'debug'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='message-severity', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """severity must be of a type compatible with message-severity""",
          'defined-type': "brocade-ras:message-severity",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INFO': {'value': 1}, u'CRITICAL': {'value': 4}, u'WARNING': {'value': 3}, u'DEFAULT': {'value': 5}, u'ERROR': {'value': 2}},), is_leaf=True, yang_name="severity", rest_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure raslog message severity', u'hidden': u'debug'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='message-severity', is_config=True)""",
        })

    self.__severity = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_severity(self):
    self.__severity = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INFO': {'value': 1}, u'CRITICAL': {'value': 4}, u'WARNING': {'value': 3}, u'DEFAULT': {'value': 5}, u'ERROR': {'value': 2}},), is_leaf=True, yang_name="severity", rest_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure raslog message severity', u'hidden': u'debug'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='message-severity', is_config=True)


  def _get_suppress(self):
    """
    Getter method for suppress, mapped from YANG variable /logging/raslog/message/msgId/suppress (empty)
    """
    return self.__suppress
      
  def _set_suppress(self, v, load=False):
    """
    Setter method for suppress, mapped from YANG variable /logging/raslog/message/msgId/suppress (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_suppress is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_suppress() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="suppress", rest_name="suppress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Suppress raslog message'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """suppress must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="suppress", rest_name="suppress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Suppress raslog message'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='empty', is_config=True)""",
        })

    self.__suppress = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_suppress(self):
    self.__suppress = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="suppress", rest_name="suppress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Suppress raslog message'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='empty', is_config=True)


  def _get_syslog(self):
    """
    Getter method for syslog, mapped from YANG variable /logging/raslog/message/msgId/syslog (empty)
    """
    return self.__syslog
      
  def _set_syslog(self, v, load=False):
    """
    Setter method for syslog, mapped from YANG variable /logging/raslog/message/msgId/syslog (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_syslog is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_syslog() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="syslog", rest_name="syslog", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable syslog logging for internal raslog message'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """syslog must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="syslog", rest_name="syslog", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable syslog logging for internal raslog message'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='empty', is_config=True)""",
        })

    self.__syslog = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_syslog(self):
    self.__syslog = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="syslog", rest_name="syslog", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable syslog logging for internal raslog message'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='empty', is_config=True)

  msgId = __builtin__.property(_get_msgId, _set_msgId)
  severity = __builtin__.property(_get_severity, _set_severity)
  suppress = __builtin__.property(_get_suppress, _set_suppress)
  syslog = __builtin__.property(_get_syslog, _set_syslog)


  _pyangbind_elements = {'msgId': msgId, 'severity': severity, 'suppress': suppress, 'syslog': syslog, }


