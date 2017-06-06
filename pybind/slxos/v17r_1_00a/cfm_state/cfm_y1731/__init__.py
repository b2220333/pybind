
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import action_profile
import test_profile
class cfm_y1731(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-dot1ag-operational - based on the path /cfm-state/cfm-y1731. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: CFM Y1731 Details
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__action_profile','__test_profile',)

  _yang_name = 'cfm-y1731'
  _rest_name = 'cfm-y1731'

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
    self.__test_profile = YANGDynClass(base=YANGListType("test_profile_name",test_profile.test_profile, yang_name="test-profile", rest_name="test-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='test-profile-name', extensions={u'tailf-common': {u'callpoint': u'dot1ag-test-profile', u'cli-suppress-show-path': None}}), is_container='list', yang_name="test-profile", rest_name="test-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'dot1ag-test-profile', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='list', is_config=False)
    self.__action_profile = YANGDynClass(base=YANGListType("action_profile_name",action_profile.action_profile, yang_name="action-profile", rest_name="action-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='action-profile-name', extensions={u'tailf-common': {u'callpoint': u'dot1ag-action-profile', u'cli-suppress-show-path': None}}), is_container='list', yang_name="action-profile", rest_name="action-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'dot1ag-action-profile', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='list', is_config=False)

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
      return [u'cfm-state', u'cfm-y1731']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'cfm-state', u'cfm-y1731']

  def _get_action_profile(self):
    """
    Getter method for action_profile, mapped from YANG variable /cfm_state/cfm_y1731/action_profile (list)

    YANG Description: CFM Action Profile Details
    """
    return self.__action_profile
      
  def _set_action_profile(self, v, load=False):
    """
    Setter method for action_profile, mapped from YANG variable /cfm_state/cfm_y1731/action_profile (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_action_profile is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_action_profile() directly.

    YANG Description: CFM Action Profile Details
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("action_profile_name",action_profile.action_profile, yang_name="action-profile", rest_name="action-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='action-profile-name', extensions={u'tailf-common': {u'callpoint': u'dot1ag-action-profile', u'cli-suppress-show-path': None}}), is_container='list', yang_name="action-profile", rest_name="action-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'dot1ag-action-profile', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """action_profile must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("action_profile_name",action_profile.action_profile, yang_name="action-profile", rest_name="action-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='action-profile-name', extensions={u'tailf-common': {u'callpoint': u'dot1ag-action-profile', u'cli-suppress-show-path': None}}), is_container='list', yang_name="action-profile", rest_name="action-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'dot1ag-action-profile', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='list', is_config=False)""",
        })

    self.__action_profile = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_action_profile(self):
    self.__action_profile = YANGDynClass(base=YANGListType("action_profile_name",action_profile.action_profile, yang_name="action-profile", rest_name="action-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='action-profile-name', extensions={u'tailf-common': {u'callpoint': u'dot1ag-action-profile', u'cli-suppress-show-path': None}}), is_container='list', yang_name="action-profile", rest_name="action-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'dot1ag-action-profile', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='list', is_config=False)


  def _get_test_profile(self):
    """
    Getter method for test_profile, mapped from YANG variable /cfm_state/cfm_y1731/test_profile (list)

    YANG Description: CFM Test Profile Details
    """
    return self.__test_profile
      
  def _set_test_profile(self, v, load=False):
    """
    Setter method for test_profile, mapped from YANG variable /cfm_state/cfm_y1731/test_profile (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_test_profile is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_test_profile() directly.

    YANG Description: CFM Test Profile Details
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("test_profile_name",test_profile.test_profile, yang_name="test-profile", rest_name="test-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='test-profile-name', extensions={u'tailf-common': {u'callpoint': u'dot1ag-test-profile', u'cli-suppress-show-path': None}}), is_container='list', yang_name="test-profile", rest_name="test-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'dot1ag-test-profile', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """test_profile must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("test_profile_name",test_profile.test_profile, yang_name="test-profile", rest_name="test-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='test-profile-name', extensions={u'tailf-common': {u'callpoint': u'dot1ag-test-profile', u'cli-suppress-show-path': None}}), is_container='list', yang_name="test-profile", rest_name="test-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'dot1ag-test-profile', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='list', is_config=False)""",
        })

    self.__test_profile = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_test_profile(self):
    self.__test_profile = YANGDynClass(base=YANGListType("test_profile_name",test_profile.test_profile, yang_name="test-profile", rest_name="test-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='test-profile-name', extensions={u'tailf-common': {u'callpoint': u'dot1ag-test-profile', u'cli-suppress-show-path': None}}), is_container='list', yang_name="test-profile", rest_name="test-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'dot1ag-test-profile', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='list', is_config=False)

  action_profile = __builtin__.property(_get_action_profile)
  test_profile = __builtin__.property(_get_test_profile)


  _pyangbind_elements = {'action_profile': action_profile, 'test_profile': test_profile, }


