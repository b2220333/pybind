
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import conform
import exceed
class police_priority_map(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-policer - based on the path /police-priority-map. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__name','__conform','__exceed',)

  _yang_name = 'police-priority-map'
  _rest_name = 'police-priority-map'

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
    self.__conform = YANGDynClass(base=conform.conform, is_container='container', presence=False, yang_name="conform", rest_name="conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Policer Priority Map for conforming traffic', u'cli-sequence-commands': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='container', is_config=True)
    self.__exceed = YANGDynClass(base=exceed.exceed, is_container='container', presence=False, yang_name="exceed", rest_name="exceed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Policer Priority Map for exceeding traffic', u'cli-sequence-commands': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='container', is_config=True)
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Policer Priority Map Name (Max Size - 64)', u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)

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
      return [u'police-priority-map']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'police-priority-map']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /police_priority_map/name (map-name-type)
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /police_priority_map/name (map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Policer Priority Map Name (Max Size - 64)', u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with map-name-type""",
          'defined-type': "brocade-policer:map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Policer Priority Map Name (Max Size - 64)', u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Policer Priority Map Name (Max Size - 64)', u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)


  def _get_conform(self):
    """
    Getter method for conform, mapped from YANG variable /police_priority_map/conform (container)
    """
    return self.__conform
      
  def _set_conform(self, v, load=False):
    """
    Setter method for conform, mapped from YANG variable /police_priority_map/conform (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_conform is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_conform() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=conform.conform, is_container='container', presence=False, yang_name="conform", rest_name="conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Policer Priority Map for conforming traffic', u'cli-sequence-commands': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """conform must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=conform.conform, is_container='container', presence=False, yang_name="conform", rest_name="conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Policer Priority Map for conforming traffic', u'cli-sequence-commands': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='container', is_config=True)""",
        })

    self.__conform = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_conform(self):
    self.__conform = YANGDynClass(base=conform.conform, is_container='container', presence=False, yang_name="conform", rest_name="conform", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Policer Priority Map for conforming traffic', u'cli-sequence-commands': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='container', is_config=True)


  def _get_exceed(self):
    """
    Getter method for exceed, mapped from YANG variable /police_priority_map/exceed (container)
    """
    return self.__exceed
      
  def _set_exceed(self, v, load=False):
    """
    Setter method for exceed, mapped from YANG variable /police_priority_map/exceed (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_exceed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_exceed() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=exceed.exceed, is_container='container', presence=False, yang_name="exceed", rest_name="exceed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Policer Priority Map for exceeding traffic', u'cli-sequence-commands': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """exceed must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=exceed.exceed, is_container='container', presence=False, yang_name="exceed", rest_name="exceed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Policer Priority Map for exceeding traffic', u'cli-sequence-commands': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='container', is_config=True)""",
        })

    self.__exceed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_exceed(self):
    self.__exceed = YANGDynClass(base=exceed.exceed, is_container='container', presence=False, yang_name="exceed", rest_name="exceed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Policer Priority Map for exceeding traffic', u'cli-sequence-commands': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='container', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  conform = __builtin__.property(_get_conform, _set_conform)
  exceed = __builtin__.property(_get_exceed, _set_exceed)


  _pyangbind_elements = {'name': name, 'conform': conform, 'exceed': exceed, }


