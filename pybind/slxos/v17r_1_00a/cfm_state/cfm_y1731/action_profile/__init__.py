
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import action_profile_event_actions
class action_profile(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-dot1ag-operational - based on the path /cfm-state/cfm-y1731/action-profile. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: CFM Action Profile Details
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__action_profile_name','__action_profile_event_actions',)

  _yang_name = 'action-profile'
  _rest_name = 'action-profile'

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
    self.__action_profile_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="action-profile-name", rest_name="action-profile-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)
    self.__action_profile_event_actions = YANGDynClass(base=action_profile_event_actions.action_profile_event_actions, is_container='container', presence=False, yang_name="action-profile-event-actions", rest_name="action-profile-event-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'dot1ag-action-profile-event-actions', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='container', is_config=False)

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
      return [u'cfm-state', u'cfm-y1731', u'action-profile']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'cfm-state', u'cfm-y1731', u'action-profile']

  def _get_action_profile_name(self):
    """
    Getter method for action_profile_name, mapped from YANG variable /cfm_state/cfm_y1731/action_profile/action_profile_name (string)

    YANG Description: action profile name
    """
    return self.__action_profile_name
      
  def _set_action_profile_name(self, v, load=False):
    """
    Setter method for action_profile_name, mapped from YANG variable /cfm_state/cfm_y1731/action_profile/action_profile_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_action_profile_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_action_profile_name() directly.

    YANG Description: action profile name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="action-profile-name", rest_name="action-profile-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """action_profile_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="action-profile-name", rest_name="action-profile-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)""",
        })

    self.__action_profile_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_action_profile_name(self):
    self.__action_profile_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="action-profile-name", rest_name="action-profile-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)


  def _get_action_profile_event_actions(self):
    """
    Getter method for action_profile_event_actions, mapped from YANG variable /cfm_state/cfm_y1731/action_profile/action_profile_event_actions (container)

    YANG Description: Action Profile Event type and associated actions
    """
    return self.__action_profile_event_actions
      
  def _set_action_profile_event_actions(self, v, load=False):
    """
    Setter method for action_profile_event_actions, mapped from YANG variable /cfm_state/cfm_y1731/action_profile/action_profile_event_actions (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_action_profile_event_actions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_action_profile_event_actions() directly.

    YANG Description: Action Profile Event type and associated actions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=action_profile_event_actions.action_profile_event_actions, is_container='container', presence=False, yang_name="action-profile-event-actions", rest_name="action-profile-event-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'dot1ag-action-profile-event-actions', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """action_profile_event_actions must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=action_profile_event_actions.action_profile_event_actions, is_container='container', presence=False, yang_name="action-profile-event-actions", rest_name="action-profile-event-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'dot1ag-action-profile-event-actions', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='container', is_config=False)""",
        })

    self.__action_profile_event_actions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_action_profile_event_actions(self):
    self.__action_profile_event_actions = YANGDynClass(base=action_profile_event_actions.action_profile_event_actions, is_container='container', presence=False, yang_name="action-profile-event-actions", rest_name="action-profile-event-actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'dot1ag-action-profile-event-actions', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='container', is_config=False)

  action_profile_name = __builtin__.property(_get_action_profile_name)
  action_profile_event_actions = __builtin__.property(_get_action_profile_event_actions)


  _pyangbind_elements = {'action_profile_name': action_profile_name, 'action_profile_event_actions': action_profile_event_actions, }


