
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import test_profile
import action_profile_name
class y1731(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-dot1ag - based on the path /cfm-config/protocol/cfm/y1731. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__test_profile','__action_profile_name',)

  _yang_name = 'y1731'
  _rest_name = 'y1731'

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
    self.__action_profile_name = YANGDynClass(base=YANGListType("action_profile_name",action_profile_name.action_profile_name, yang_name="action-profile-name", rest_name="action-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='action-profile-name', extensions={u'tailf-common': {u'info': u'Configure action profile related parameters', u'cli-full-no': None, u'cli-suppress-list-no': None, u'alt-name': u'action-profile', u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'setY1731ActionProfiles', u'cli-mode-name': u'config-cfm-y1731-action-profile-$(action-profile-name)'}}), is_container='list', yang_name="action-profile-name", rest_name="action-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure action profile related parameters', u'cli-full-no': None, u'cli-suppress-list-no': None, u'alt-name': u'action-profile', u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'setY1731ActionProfiles', u'cli-mode-name': u'config-cfm-y1731-action-profile-$(action-profile-name)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='list', is_config=True)
    self.__test_profile = YANGDynClass(base=YANGListType("test_profile",test_profile.test_profile, yang_name="test-profile", rest_name="test-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='test-profile', extensions={u'tailf-common': {u'info': u'Configure test profile related parameters', u'cli-suppress-list-no': None, u'cli-full-no': None, u'callpoint': u'setY1731TestProfile', u'cli-mode-name': u'config-cfm-y1731-test-profile-$(test-profile)'}}), is_container='list', yang_name="test-profile", rest_name="test-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure test profile related parameters', u'cli-suppress-list-no': None, u'cli-full-no': None, u'callpoint': u'setY1731TestProfile', u'cli-mode-name': u'config-cfm-y1731-test-profile-$(test-profile)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='list', is_config=True)

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
      return [u'cfm-config', u'protocol', u'cfm', u'y1731']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'protocol', u'cfm', u'y1731']

  def _get_test_profile(self):
    """
    Getter method for test_profile, mapped from YANG variable /cfm_config/protocol/cfm/y1731/test_profile (list)
    """
    return self.__test_profile
      
  def _set_test_profile(self, v, load=False):
    """
    Setter method for test_profile, mapped from YANG variable /cfm_config/protocol/cfm/y1731/test_profile (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_test_profile is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_test_profile() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("test_profile",test_profile.test_profile, yang_name="test-profile", rest_name="test-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='test-profile', extensions={u'tailf-common': {u'info': u'Configure test profile related parameters', u'cli-suppress-list-no': None, u'cli-full-no': None, u'callpoint': u'setY1731TestProfile', u'cli-mode-name': u'config-cfm-y1731-test-profile-$(test-profile)'}}), is_container='list', yang_name="test-profile", rest_name="test-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure test profile related parameters', u'cli-suppress-list-no': None, u'cli-full-no': None, u'callpoint': u'setY1731TestProfile', u'cli-mode-name': u'config-cfm-y1731-test-profile-$(test-profile)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """test_profile must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("test_profile",test_profile.test_profile, yang_name="test-profile", rest_name="test-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='test-profile', extensions={u'tailf-common': {u'info': u'Configure test profile related parameters', u'cli-suppress-list-no': None, u'cli-full-no': None, u'callpoint': u'setY1731TestProfile', u'cli-mode-name': u'config-cfm-y1731-test-profile-$(test-profile)'}}), is_container='list', yang_name="test-profile", rest_name="test-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure test profile related parameters', u'cli-suppress-list-no': None, u'cli-full-no': None, u'callpoint': u'setY1731TestProfile', u'cli-mode-name': u'config-cfm-y1731-test-profile-$(test-profile)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='list', is_config=True)""",
        })

    self.__test_profile = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_test_profile(self):
    self.__test_profile = YANGDynClass(base=YANGListType("test_profile",test_profile.test_profile, yang_name="test-profile", rest_name="test-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='test-profile', extensions={u'tailf-common': {u'info': u'Configure test profile related parameters', u'cli-suppress-list-no': None, u'cli-full-no': None, u'callpoint': u'setY1731TestProfile', u'cli-mode-name': u'config-cfm-y1731-test-profile-$(test-profile)'}}), is_container='list', yang_name="test-profile", rest_name="test-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure test profile related parameters', u'cli-suppress-list-no': None, u'cli-full-no': None, u'callpoint': u'setY1731TestProfile', u'cli-mode-name': u'config-cfm-y1731-test-profile-$(test-profile)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='list', is_config=True)


  def _get_action_profile_name(self):
    """
    Getter method for action_profile_name, mapped from YANG variable /cfm_config/protocol/cfm/y1731/action_profile_name (list)
    """
    return self.__action_profile_name
      
  def _set_action_profile_name(self, v, load=False):
    """
    Setter method for action_profile_name, mapped from YANG variable /cfm_config/protocol/cfm/y1731/action_profile_name (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_action_profile_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_action_profile_name() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("action_profile_name",action_profile_name.action_profile_name, yang_name="action-profile-name", rest_name="action-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='action-profile-name', extensions={u'tailf-common': {u'info': u'Configure action profile related parameters', u'cli-full-no': None, u'cli-suppress-list-no': None, u'alt-name': u'action-profile', u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'setY1731ActionProfiles', u'cli-mode-name': u'config-cfm-y1731-action-profile-$(action-profile-name)'}}), is_container='list', yang_name="action-profile-name", rest_name="action-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure action profile related parameters', u'cli-full-no': None, u'cli-suppress-list-no': None, u'alt-name': u'action-profile', u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'setY1731ActionProfiles', u'cli-mode-name': u'config-cfm-y1731-action-profile-$(action-profile-name)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """action_profile_name must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("action_profile_name",action_profile_name.action_profile_name, yang_name="action-profile-name", rest_name="action-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='action-profile-name', extensions={u'tailf-common': {u'info': u'Configure action profile related parameters', u'cli-full-no': None, u'cli-suppress-list-no': None, u'alt-name': u'action-profile', u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'setY1731ActionProfiles', u'cli-mode-name': u'config-cfm-y1731-action-profile-$(action-profile-name)'}}), is_container='list', yang_name="action-profile-name", rest_name="action-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure action profile related parameters', u'cli-full-no': None, u'cli-suppress-list-no': None, u'alt-name': u'action-profile', u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'setY1731ActionProfiles', u'cli-mode-name': u'config-cfm-y1731-action-profile-$(action-profile-name)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='list', is_config=True)""",
        })

    self.__action_profile_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_action_profile_name(self):
    self.__action_profile_name = YANGDynClass(base=YANGListType("action_profile_name",action_profile_name.action_profile_name, yang_name="action-profile-name", rest_name="action-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='action-profile-name', extensions={u'tailf-common': {u'info': u'Configure action profile related parameters', u'cli-full-no': None, u'cli-suppress-list-no': None, u'alt-name': u'action-profile', u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'setY1731ActionProfiles', u'cli-mode-name': u'config-cfm-y1731-action-profile-$(action-profile-name)'}}), is_container='list', yang_name="action-profile-name", rest_name="action-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure action profile related parameters', u'cli-full-no': None, u'cli-suppress-list-no': None, u'alt-name': u'action-profile', u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'setY1731ActionProfiles', u'cli-mode-name': u'config-cfm-y1731-action-profile-$(action-profile-name)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='list', is_config=True)

  test_profile = __builtin__.property(_get_test_profile, _set_test_profile)
  action_profile_name = __builtin__.property(_get_action_profile_name, _set_action_profile_name)


  _pyangbind_elements = {'test_profile': test_profile, 'action_profile_name': action_profile_name, }


