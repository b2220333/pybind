
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class cpu_queue_info_details(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ssm-operational - based on the path /cpu-queue-info-state/cpu-queue-info-details. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: CPU Queue fps and usage
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__queue_id','__fps','__priority','__usage',)

  _yang_name = 'cpu-queue-info-details'
  _rest_name = 'cpu-queue-info-details'

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
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='uint8', is_config=False)
    self.__usage = YANGDynClass(base=unicode, is_leaf=True, yang_name="usage", rest_name="usage", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)
    self.__fps = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="fps", rest_name="fps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='uint32', is_config=False)
    self.__queue_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="queue-id", rest_name="queue-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='uint8', is_config=False)

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
      return [u'cpu-queue-info-state', u'cpu-queue-info-details']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'cpu-queue-info-state', u'cpu-queue-info-details']

  def _get_queue_id(self):
    """
    Getter method for queue_id, mapped from YANG variable /cpu_queue_info_state/cpu_queue_info_details/queue_id (uint8)

    YANG Description: CPU Queue ID
    """
    return self.__queue_id
      
  def _set_queue_id(self, v, load=False):
    """
    Setter method for queue_id, mapped from YANG variable /cpu_queue_info_state/cpu_queue_info_details/queue_id (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_queue_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_queue_id() directly.

    YANG Description: CPU Queue ID
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="queue-id", rest_name="queue-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """queue_id must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="queue-id", rest_name="queue-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='uint8', is_config=False)""",
        })

    self.__queue_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_queue_id(self):
    self.__queue_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="queue-id", rest_name="queue-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='uint8', is_config=False)


  def _get_fps(self):
    """
    Getter method for fps, mapped from YANG variable /cpu_queue_info_state/cpu_queue_info_details/fps (uint32)

    YANG Description: Queue rate in fps
    """
    return self.__fps
      
  def _set_fps(self, v, load=False):
    """
    Setter method for fps, mapped from YANG variable /cpu_queue_info_state/cpu_queue_info_details/fps (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fps is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fps() directly.

    YANG Description: Queue rate in fps
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="fps", rest_name="fps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fps must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="fps", rest_name="fps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='uint32', is_config=False)""",
        })

    self.__fps = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fps(self):
    self.__fps = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="fps", rest_name="fps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='uint32', is_config=False)


  def _get_priority(self):
    """
    Getter method for priority, mapped from YANG variable /cpu_queue_info_state/cpu_queue_info_details/priority (uint8)

    YANG Description: CPU queue priority
    """
    return self.__priority
      
  def _set_priority(self, v, load=False):
    """
    Setter method for priority, mapped from YANG variable /cpu_queue_info_state/cpu_queue_info_details/priority (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority() directly.

    YANG Description: CPU queue priority
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='uint8', is_config=False)""",
        })

    self.__priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority(self):
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='uint8', is_config=False)


  def _get_usage(self):
    """
    Getter method for usage, mapped from YANG variable /cpu_queue_info_state/cpu_queue_info_details/usage (string)

    YANG Description: Usage details
    """
    return self.__usage
      
  def _set_usage(self, v, load=False):
    """
    Setter method for usage, mapped from YANG variable /cpu_queue_info_state/cpu_queue_info_details/usage (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_usage is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_usage() directly.

    YANG Description: Usage details
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="usage", rest_name="usage", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """usage must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="usage", rest_name="usage", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)""",
        })

    self.__usage = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_usage(self):
    self.__usage = YANGDynClass(base=unicode, is_leaf=True, yang_name="usage", rest_name="usage", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)

  queue_id = __builtin__.property(_get_queue_id)
  fps = __builtin__.property(_get_fps)
  priority = __builtin__.property(_get_priority)
  usage = __builtin__.property(_get_usage)


  _pyangbind_elements = {'queue_id': queue_id, 'fps': fps, 'priority': priority, 'usage': usage, }


