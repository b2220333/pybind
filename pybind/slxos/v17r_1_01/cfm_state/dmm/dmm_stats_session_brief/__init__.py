
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import dmm_stats_session_history_brief
class dmm_stats_session_brief(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-dot1ag-operational - based on the path /cfm-state/dmm/dmm-stats-session-brief. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Brief display of DMM statistics
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__session_index','__test_profile_name','__dmm_stats_session_history_brief',)

  _yang_name = 'dmm-stats-session-brief'
  _rest_name = 'dmm-stats-session-brief'

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
    self.__session_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="session-index", rest_name="session-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)
    self.__dmm_stats_session_history_brief = YANGDynClass(base=YANGListType("history_index",dmm_stats_session_history_brief.dmm_stats_session_history_brief, yang_name="dmm-stats-session-history-brief", rest_name="dmm-stats-session-history-brief", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='history-index', extensions={u'tailf-common': {u'callpoint': u'dot1ag-dmm-stats-session-history-brief', u'cli-suppress-show-path': None}}), is_container='list', yang_name="dmm-stats-session-history-brief", rest_name="dmm-stats-session-history-brief", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'dot1ag-dmm-stats-session-history-brief', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='list', is_config=False)
    self.__test_profile_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="test-profile-name", rest_name="test-profile-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)

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
      return [u'cfm-state', u'dmm', u'dmm-stats-session-brief']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'cfm-state', u'dmm', u'dmm-stats-session-brief']

  def _get_session_index(self):
    """
    Getter method for session_index, mapped from YANG variable /cfm_state/dmm/dmm_stats_session_brief/session_index (uint32)

    YANG Description: DMM session index
    """
    return self.__session_index
      
  def _set_session_index(self, v, load=False):
    """
    Setter method for session_index, mapped from YANG variable /cfm_state/dmm/dmm_stats_session_brief/session_index (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_session_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_session_index() directly.

    YANG Description: DMM session index
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="session-index", rest_name="session-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """session_index must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="session-index", rest_name="session-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)""",
        })

    self.__session_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_session_index(self):
    self.__session_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="session-index", rest_name="session-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint32', is_config=False)


  def _get_test_profile_name(self):
    """
    Getter method for test_profile_name, mapped from YANG variable /cfm_state/dmm/dmm_stats_session_brief/test_profile_name (string)

    YANG Description: Test Profile name
    """
    return self.__test_profile_name
      
  def _set_test_profile_name(self, v, load=False):
    """
    Setter method for test_profile_name, mapped from YANG variable /cfm_state/dmm/dmm_stats_session_brief/test_profile_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_test_profile_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_test_profile_name() directly.

    YANG Description: Test Profile name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="test-profile-name", rest_name="test-profile-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """test_profile_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="test-profile-name", rest_name="test-profile-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)""",
        })

    self.__test_profile_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_test_profile_name(self):
    self.__test_profile_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="test-profile-name", rest_name="test-profile-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)


  def _get_dmm_stats_session_history_brief(self):
    """
    Getter method for dmm_stats_session_history_brief, mapped from YANG variable /cfm_state/dmm/dmm_stats_session_brief/dmm_stats_session_history_brief (list)

    YANG Description: Brief display of DMM statistics for histories
    """
    return self.__dmm_stats_session_history_brief
      
  def _set_dmm_stats_session_history_brief(self, v, load=False):
    """
    Setter method for dmm_stats_session_history_brief, mapped from YANG variable /cfm_state/dmm/dmm_stats_session_brief/dmm_stats_session_history_brief (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dmm_stats_session_history_brief is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dmm_stats_session_history_brief() directly.

    YANG Description: Brief display of DMM statistics for histories
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("history_index",dmm_stats_session_history_brief.dmm_stats_session_history_brief, yang_name="dmm-stats-session-history-brief", rest_name="dmm-stats-session-history-brief", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='history-index', extensions={u'tailf-common': {u'callpoint': u'dot1ag-dmm-stats-session-history-brief', u'cli-suppress-show-path': None}}), is_container='list', yang_name="dmm-stats-session-history-brief", rest_name="dmm-stats-session-history-brief", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'dot1ag-dmm-stats-session-history-brief', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dmm_stats_session_history_brief must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("history_index",dmm_stats_session_history_brief.dmm_stats_session_history_brief, yang_name="dmm-stats-session-history-brief", rest_name="dmm-stats-session-history-brief", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='history-index', extensions={u'tailf-common': {u'callpoint': u'dot1ag-dmm-stats-session-history-brief', u'cli-suppress-show-path': None}}), is_container='list', yang_name="dmm-stats-session-history-brief", rest_name="dmm-stats-session-history-brief", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'dot1ag-dmm-stats-session-history-brief', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='list', is_config=False)""",
        })

    self.__dmm_stats_session_history_brief = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dmm_stats_session_history_brief(self):
    self.__dmm_stats_session_history_brief = YANGDynClass(base=YANGListType("history_index",dmm_stats_session_history_brief.dmm_stats_session_history_brief, yang_name="dmm-stats-session-history-brief", rest_name="dmm-stats-session-history-brief", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='history-index', extensions={u'tailf-common': {u'callpoint': u'dot1ag-dmm-stats-session-history-brief', u'cli-suppress-show-path': None}}), is_container='list', yang_name="dmm-stats-session-history-brief", rest_name="dmm-stats-session-history-brief", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'dot1ag-dmm-stats-session-history-brief', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='list', is_config=False)

  session_index = __builtin__.property(_get_session_index)
  test_profile_name = __builtin__.property(_get_test_profile_name)
  dmm_stats_session_history_brief = __builtin__.property(_get_dmm_stats_session_history_brief)


  _pyangbind_elements = {'session_index': session_index, 'test_profile_name': test_profile_name, 'dmm_stats_session_history_brief': dmm_stats_session_history_brief, }


