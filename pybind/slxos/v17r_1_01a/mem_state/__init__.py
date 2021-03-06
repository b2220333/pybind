
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import summary
import mem_list
class mem_state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-RAS-operational - based on the path /mem-state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Memory information
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__summary','__mem_list',)

  _yang_name = 'mem-state'
  _rest_name = 'mem-state'

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
    self.__mem_list = YANGDynClass(base=mem_list.mem_list, is_container='container', presence=False, yang_name="mem-list", rest_name="mem-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'RAS-process-memory', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='container', is_config=False)
    self.__summary = YANGDynClass(base=summary.summary, is_container='container', presence=False, yang_name="summary", rest_name="summary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'RAS-process-mem-summary', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='container', is_config=False)

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
      return [u'mem-state']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mem-state']

  def _get_summary(self):
    """
    Getter method for summary, mapped from YANG variable /mem_state/summary (container)

    YANG Description:  Overall Memory utilization summary 
    """
    return self.__summary
      
  def _set_summary(self, v, load=False):
    """
    Setter method for summary, mapped from YANG variable /mem_state/summary (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_summary is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_summary() directly.

    YANG Description:  Overall Memory utilization summary 
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=summary.summary, is_container='container', presence=False, yang_name="summary", rest_name="summary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'RAS-process-mem-summary', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """summary must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=summary.summary, is_container='container', presence=False, yang_name="summary", rest_name="summary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'RAS-process-mem-summary', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='container', is_config=False)""",
        })

    self.__summary = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_summary(self):
    self.__summary = YANGDynClass(base=summary.summary, is_container='container', presence=False, yang_name="summary", rest_name="summary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'RAS-process-mem-summary', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='container', is_config=False)


  def _get_mem_list(self):
    """
    Getter method for mem_list, mapped from YANG variable /mem_state/mem_list (container)

    YANG Description:  Memory utilization of all the process 
    """
    return self.__mem_list
      
  def _set_mem_list(self, v, load=False):
    """
    Setter method for mem_list, mapped from YANG variable /mem_state/mem_list (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mem_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mem_list() directly.

    YANG Description:  Memory utilization of all the process 
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=mem_list.mem_list, is_container='container', presence=False, yang_name="mem-list", rest_name="mem-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'RAS-process-memory', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mem_list must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=mem_list.mem_list, is_container='container', presence=False, yang_name="mem-list", rest_name="mem-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'RAS-process-memory', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='container', is_config=False)""",
        })

    self.__mem_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mem_list(self):
    self.__mem_list = YANGDynClass(base=mem_list.mem_list, is_container='container', presence=False, yang_name="mem-list", rest_name="mem-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'RAS-process-memory', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='container', is_config=False)

  summary = __builtin__.property(_get_summary)
  mem_list = __builtin__.property(_get_mem_list)


  _pyangbind_elements = {'summary': summary, 'mem_list': mem_list, }


