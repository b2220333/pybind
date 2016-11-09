
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class history_control_entry(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/tengigabitethernet/rmon/collection/history-control-entry. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__history_control_index','__history_control_buckets_requested','__history_control_interval','__history_control_owner',)

  _yang_name = 'history-control-entry'
  _rest_name = 'history'

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
    self.__history_control_owner = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,14})', 'length': [u'1 .. 15']}), is_leaf=True, yang_name="history-control-owner", rest_name="owner", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Owner identity', u'alt-name': u'owner'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='owner-string', is_config=True)
    self.__history_control_buckets_requested = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32)(50), is_leaf=True, yang_name="history-control-buckets-requested", rest_name="buckets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Buckets (default 50)', u'alt-name': u'buckets'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='history-control-buckets-requested-type', is_config=True)
    self.__history_control_index = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="history-control-index", rest_name="history-control-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='history-control-index-type', is_config=True)
    self.__history_control_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 3600']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32)(1800), is_leaf=True, yang_name="history-control-interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Polling Interval (default 1800)', u'alt-name': u'interval'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='history-control-interval-type', is_config=True)

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
      return [u'interface', u'tengigabitethernet', u'rmon', u'collection', u'history-control-entry']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'TenGigabitEthernet', u'rmon', u'collection', u'history']

  def _get_history_control_index(self):
    """
    Getter method for history_control_index, mapped from YANG variable /interface/tengigabitethernet/rmon/collection/history_control_entry/history_control_index (history-control-index-type)
    """
    return self.__history_control_index
      
  def _set_history_control_index(self, v, load=False):
    """
    Setter method for history_control_index, mapped from YANG variable /interface/tengigabitethernet/rmon/collection/history_control_entry/history_control_index (history-control-index-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_history_control_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_history_control_index() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="history-control-index", rest_name="history-control-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='history-control-index-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """history_control_index must be of a type compatible with history-control-index-type""",
          'defined-type': "brocade-rmon:history-control-index-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="history-control-index", rest_name="history-control-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='history-control-index-type', is_config=True)""",
        })

    self.__history_control_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_history_control_index(self):
    self.__history_control_index = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="history-control-index", rest_name="history-control-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='history-control-index-type', is_config=True)


  def _get_history_control_buckets_requested(self):
    """
    Getter method for history_control_buckets_requested, mapped from YANG variable /interface/tengigabitethernet/rmon/collection/history_control_entry/history_control_buckets_requested (history-control-buckets-requested-type)
    """
    return self.__history_control_buckets_requested
      
  def _set_history_control_buckets_requested(self, v, load=False):
    """
    Setter method for history_control_buckets_requested, mapped from YANG variable /interface/tengigabitethernet/rmon/collection/history_control_entry/history_control_buckets_requested (history-control-buckets-requested-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_history_control_buckets_requested is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_history_control_buckets_requested() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32)(50), is_leaf=True, yang_name="history-control-buckets-requested", rest_name="buckets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Buckets (default 50)', u'alt-name': u'buckets'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='history-control-buckets-requested-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """history_control_buckets_requested must be of a type compatible with history-control-buckets-requested-type""",
          'defined-type': "brocade-rmon:history-control-buckets-requested-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32)(50), is_leaf=True, yang_name="history-control-buckets-requested", rest_name="buckets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Buckets (default 50)', u'alt-name': u'buckets'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='history-control-buckets-requested-type', is_config=True)""",
        })

    self.__history_control_buckets_requested = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_history_control_buckets_requested(self):
    self.__history_control_buckets_requested = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32)(50), is_leaf=True, yang_name="history-control-buckets-requested", rest_name="buckets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Buckets (default 50)', u'alt-name': u'buckets'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='history-control-buckets-requested-type', is_config=True)


  def _get_history_control_interval(self):
    """
    Getter method for history_control_interval, mapped from YANG variable /interface/tengigabitethernet/rmon/collection/history_control_entry/history_control_interval (history-control-interval-type)
    """
    return self.__history_control_interval
      
  def _set_history_control_interval(self, v, load=False):
    """
    Setter method for history_control_interval, mapped from YANG variable /interface/tengigabitethernet/rmon/collection/history_control_entry/history_control_interval (history-control-interval-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_history_control_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_history_control_interval() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 3600']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32)(1800), is_leaf=True, yang_name="history-control-interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Polling Interval (default 1800)', u'alt-name': u'interval'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='history-control-interval-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """history_control_interval must be of a type compatible with history-control-interval-type""",
          'defined-type': "brocade-rmon:history-control-interval-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 3600']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32)(1800), is_leaf=True, yang_name="history-control-interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Polling Interval (default 1800)', u'alt-name': u'interval'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='history-control-interval-type', is_config=True)""",
        })

    self.__history_control_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_history_control_interval(self):
    self.__history_control_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 3600']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32)(1800), is_leaf=True, yang_name="history-control-interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Polling Interval (default 1800)', u'alt-name': u'interval'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='history-control-interval-type', is_config=True)


  def _get_history_control_owner(self):
    """
    Getter method for history_control_owner, mapped from YANG variable /interface/tengigabitethernet/rmon/collection/history_control_entry/history_control_owner (owner-string)
    """
    return self.__history_control_owner
      
  def _set_history_control_owner(self, v, load=False):
    """
    Setter method for history_control_owner, mapped from YANG variable /interface/tengigabitethernet/rmon/collection/history_control_entry/history_control_owner (owner-string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_history_control_owner is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_history_control_owner() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,14})', 'length': [u'1 .. 15']}), is_leaf=True, yang_name="history-control-owner", rest_name="owner", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Owner identity', u'alt-name': u'owner'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='owner-string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """history_control_owner must be of a type compatible with owner-string""",
          'defined-type': "brocade-rmon:owner-string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,14})', 'length': [u'1 .. 15']}), is_leaf=True, yang_name="history-control-owner", rest_name="owner", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Owner identity', u'alt-name': u'owner'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='owner-string', is_config=True)""",
        })

    self.__history_control_owner = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_history_control_owner(self):
    self.__history_control_owner = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,14})', 'length': [u'1 .. 15']}), is_leaf=True, yang_name="history-control-owner", rest_name="owner", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Owner identity', u'alt-name': u'owner'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='owner-string', is_config=True)

  history_control_index = __builtin__.property(_get_history_control_index, _set_history_control_index)
  history_control_buckets_requested = __builtin__.property(_get_history_control_buckets_requested, _set_history_control_buckets_requested)
  history_control_interval = __builtin__.property(_get_history_control_interval, _set_history_control_interval)
  history_control_owner = __builtin__.property(_get_history_control_owner, _set_history_control_owner)


  _pyangbind_elements = {'history_control_index': history_control_index, 'history_control_buckets_requested': history_control_buckets_requested, 'history_control_interval': history_control_interval, 'history_control_owner': history_control_owner, }


