
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class trigger_function_container(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-event-handler - based on the path /event-handler/activate/name/trigger-function-container. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__trigger_function','__time_window',)

  _yang_name = 'trigger-function-container'
  _rest_name = ''

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
    self.__time_window = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="time-window", rest_name="time-window", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number of seconds that is valid for all triggers to be received in order to launch the action.'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='uint32', is_config=True)
    self.__trigger_function = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'AND': {'value': 2}, u'OR': {'value': 1}},), default=unicode("OR"), is_leaf=True, yang_name="trigger-function", rest_name="trigger-function", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Trigger-function controls how multiple triggers are interpreted to launch the action (default = OR).'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='enumeration', is_config=True)

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
      return [u'event-handler', u'activate', u'name', u'trigger-function-container']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'event-handler', u'activate']

  def _get_trigger_function(self):
    """
    Getter method for trigger_function, mapped from YANG variable /event_handler/activate/name/trigger_function_container/trigger_function (enumeration)
    """
    return self.__trigger_function
      
  def _set_trigger_function(self, v, load=False):
    """
    Setter method for trigger_function, mapped from YANG variable /event_handler/activate/name/trigger_function_container/trigger_function (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trigger_function is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trigger_function() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'AND': {'value': 2}, u'OR': {'value': 1}},), default=unicode("OR"), is_leaf=True, yang_name="trigger-function", rest_name="trigger-function", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Trigger-function controls how multiple triggers are interpreted to launch the action (default = OR).'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trigger_function must be of a type compatible with enumeration""",
          'defined-type': "brocade-event-handler:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'AND': {'value': 2}, u'OR': {'value': 1}},), default=unicode("OR"), is_leaf=True, yang_name="trigger-function", rest_name="trigger-function", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Trigger-function controls how multiple triggers are interpreted to launch the action (default = OR).'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='enumeration', is_config=True)""",
        })

    self.__trigger_function = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trigger_function(self):
    self.__trigger_function = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'AND': {'value': 2}, u'OR': {'value': 1}},), default=unicode("OR"), is_leaf=True, yang_name="trigger-function", rest_name="trigger-function", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Trigger-function controls how multiple triggers are interpreted to launch the action (default = OR).'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='enumeration', is_config=True)


  def _get_time_window(self):
    """
    Getter method for time_window, mapped from YANG variable /event_handler/activate/name/trigger_function_container/time_window (uint32)
    """
    return self.__time_window
      
  def _set_time_window(self, v, load=False):
    """
    Setter method for time_window, mapped from YANG variable /event_handler/activate/name/trigger_function_container/time_window (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_time_window is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_time_window() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="time-window", rest_name="time-window", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number of seconds that is valid for all triggers to be received in order to launch the action.'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """time_window must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="time-window", rest_name="time-window", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number of seconds that is valid for all triggers to be received in order to launch the action.'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='uint32', is_config=True)""",
        })

    self.__time_window = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_time_window(self):
    self.__time_window = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="time-window", rest_name="time-window", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number of seconds that is valid for all triggers to be received in order to launch the action.'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='uint32', is_config=True)

  trigger_function = __builtin__.property(_get_trigger_function, _set_trigger_function)
  time_window = __builtin__.property(_get_time_window, _set_time_window)


  _pyangbind_elements = {'trigger_function': trigger_function, 'time_window': time_window, }


