
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import enable
import default_behavior
import controller
class openflow(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-openflow - based on the path /openflow-global/openflow. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__enable','__default_behavior','__controller',)

  _yang_name = 'openflow'
  _rest_name = 'openflow'

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
    self.__default_behavior = YANGDynClass(base=default_behavior.default_behavior, is_container='container', yang_name="default-behavior", rest_name="default-behavior", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'set openflow behavior'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)
    self.__controller = YANGDynClass(base=YANGListType("controller_name",controller.controller, yang_name="controller", rest_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='controller-name', extensions={u'tailf-common': {u'info': u'OpenFlow controller configuration', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-incomplete-command': None, u'callpoint': u'OpenFlowGlobalControllerCallpoint'}}), is_container='list', yang_name="controller", rest_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'OpenFlow controller configuration', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-incomplete-command': None, u'callpoint': u'OpenFlowGlobalControllerCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='list', is_config=True)
    self.__enable = YANGDynClass(base=enable.enable, is_container='container', yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Config Openflow Version', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)

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
      return [u'openflow-global', u'openflow']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'openflow']

  def _get_enable(self):
    """
    Getter method for enable, mapped from YANG variable /openflow_global/openflow/enable (container)
    """
    return self.__enable
      
  def _set_enable(self, v, load=False):
    """
    Setter method for enable, mapped from YANG variable /openflow_global/openflow/enable (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable() directly.
    """
    try:
      t = YANGDynClass(v,base=enable.enable, is_container='container', yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Config Openflow Version', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=enable.enable, is_container='container', yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Config Openflow Version', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)""",
        })

    self.__enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable(self):
    self.__enable = YANGDynClass(base=enable.enable, is_container='container', yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Config Openflow Version', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)


  def _get_default_behavior(self):
    """
    Getter method for default_behavior, mapped from YANG variable /openflow_global/openflow/default_behavior (container)
    """
    return self.__default_behavior
      
  def _set_default_behavior(self, v, load=False):
    """
    Setter method for default_behavior, mapped from YANG variable /openflow_global/openflow/default_behavior (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_behavior is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_behavior() directly.
    """
    try:
      t = YANGDynClass(v,base=default_behavior.default_behavior, is_container='container', yang_name="default-behavior", rest_name="default-behavior", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'set openflow behavior'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_behavior must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=default_behavior.default_behavior, is_container='container', yang_name="default-behavior", rest_name="default-behavior", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'set openflow behavior'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)""",
        })

    self.__default_behavior = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_behavior(self):
    self.__default_behavior = YANGDynClass(base=default_behavior.default_behavior, is_container='container', yang_name="default-behavior", rest_name="default-behavior", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'set openflow behavior'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)


  def _get_controller(self):
    """
    Getter method for controller, mapped from YANG variable /openflow_global/openflow/controller (list)

    YANG Description: OpenFlow controller configuration
    """
    return self.__controller
      
  def _set_controller(self, v, load=False):
    """
    Setter method for controller, mapped from YANG variable /openflow_global/openflow/controller (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_controller is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_controller() directly.

    YANG Description: OpenFlow controller configuration
    """
    try:
      t = YANGDynClass(v,base=YANGListType("controller_name",controller.controller, yang_name="controller", rest_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='controller-name', extensions={u'tailf-common': {u'info': u'OpenFlow controller configuration', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-incomplete-command': None, u'callpoint': u'OpenFlowGlobalControllerCallpoint'}}), is_container='list', yang_name="controller", rest_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'OpenFlow controller configuration', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-incomplete-command': None, u'callpoint': u'OpenFlowGlobalControllerCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """controller must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("controller_name",controller.controller, yang_name="controller", rest_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='controller-name', extensions={u'tailf-common': {u'info': u'OpenFlow controller configuration', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-incomplete-command': None, u'callpoint': u'OpenFlowGlobalControllerCallpoint'}}), is_container='list', yang_name="controller", rest_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'OpenFlow controller configuration', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-incomplete-command': None, u'callpoint': u'OpenFlowGlobalControllerCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='list', is_config=True)""",
        })

    self.__controller = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_controller(self):
    self.__controller = YANGDynClass(base=YANGListType("controller_name",controller.controller, yang_name="controller", rest_name="controller", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='controller-name', extensions={u'tailf-common': {u'info': u'OpenFlow controller configuration', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-incomplete-command': None, u'callpoint': u'OpenFlowGlobalControllerCallpoint'}}), is_container='list', yang_name="controller", rest_name="controller", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'OpenFlow controller configuration', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-incomplete-command': None, u'callpoint': u'OpenFlowGlobalControllerCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='list', is_config=True)

  enable = __builtin__.property(_get_enable, _set_enable)
  default_behavior = __builtin__.property(_get_default_behavior, _set_default_behavior)
  controller = __builtin__.property(_get_controller, _set_controller)


  _pyangbind_elements = {'enable': enable, 'default_behavior': default_behavior, 'controller': controller, }


