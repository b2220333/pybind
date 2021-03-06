
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class link_error_disable(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/ethernet/link-error-disable. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__link_error_disable_entry','__sampling_time_in_sec','__wait_time_in_sec',)

  _yang_name = 'link-error-disable'
  _rest_name = 'link-error-disable'

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
    self.__link_error_disable_entry = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..50']}), is_leaf=True, yang_name="link-error-disable-entry", rest_name="link-error-disable-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NUMBER:1-50;;toggle-threshold', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-pld', defining_module='brocade-pld', yang_type='uint32', is_config=True)
    self.__wait_time_in_sec = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65565']}), is_leaf=True, yang_name="wait-time-in-sec", rest_name="wait-time-in-sec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'NUMBER:0-65565;;wait-time-in-sec'}}, namespace='urn:brocade.com:mgmt:brocade-pld', defining_module='brocade-pld', yang_type='uint32', is_config=True)
    self.__sampling_time_in_sec = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65565']}), is_leaf=True, yang_name="sampling-time-in-sec", rest_name="sampling-time-in-sec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NUMBER:1-65565;;sampling-time-in-sec', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-pld', defining_module='brocade-pld', yang_type='uint32', is_config=True)

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
      return [u'interface', u'ethernet', u'link-error-disable']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ethernet', u'link-error-disable']

  def _get_link_error_disable_entry(self):
    """
    Getter method for link_error_disable_entry, mapped from YANG variable /interface/ethernet/link_error_disable/link_error_disable_entry (uint32)
    """
    return self.__link_error_disable_entry
      
  def _set_link_error_disable_entry(self, v, load=False):
    """
    Setter method for link_error_disable_entry, mapped from YANG variable /interface/ethernet/link_error_disable/link_error_disable_entry (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_error_disable_entry is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_error_disable_entry() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..50']}), is_leaf=True, yang_name="link-error-disable-entry", rest_name="link-error-disable-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NUMBER:1-50;;toggle-threshold', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-pld', defining_module='brocade-pld', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_error_disable_entry must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..50']}), is_leaf=True, yang_name="link-error-disable-entry", rest_name="link-error-disable-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NUMBER:1-50;;toggle-threshold', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-pld', defining_module='brocade-pld', yang_type='uint32', is_config=True)""",
        })

    self.__link_error_disable_entry = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_error_disable_entry(self):
    self.__link_error_disable_entry = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..50']}), is_leaf=True, yang_name="link-error-disable-entry", rest_name="link-error-disable-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NUMBER:1-50;;toggle-threshold', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-pld', defining_module='brocade-pld', yang_type='uint32', is_config=True)


  def _get_sampling_time_in_sec(self):
    """
    Getter method for sampling_time_in_sec, mapped from YANG variable /interface/ethernet/link_error_disable/sampling_time_in_sec (uint32)
    """
    return self.__sampling_time_in_sec
      
  def _set_sampling_time_in_sec(self, v, load=False):
    """
    Setter method for sampling_time_in_sec, mapped from YANG variable /interface/ethernet/link_error_disable/sampling_time_in_sec (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sampling_time_in_sec is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sampling_time_in_sec() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65565']}), is_leaf=True, yang_name="sampling-time-in-sec", rest_name="sampling-time-in-sec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NUMBER:1-65565;;sampling-time-in-sec', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-pld', defining_module='brocade-pld', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sampling_time_in_sec must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65565']}), is_leaf=True, yang_name="sampling-time-in-sec", rest_name="sampling-time-in-sec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NUMBER:1-65565;;sampling-time-in-sec', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-pld', defining_module='brocade-pld', yang_type='uint32', is_config=True)""",
        })

    self.__sampling_time_in_sec = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sampling_time_in_sec(self):
    self.__sampling_time_in_sec = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65565']}), is_leaf=True, yang_name="sampling-time-in-sec", rest_name="sampling-time-in-sec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NUMBER:1-65565;;sampling-time-in-sec', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-pld', defining_module='brocade-pld', yang_type='uint32', is_config=True)


  def _get_wait_time_in_sec(self):
    """
    Getter method for wait_time_in_sec, mapped from YANG variable /interface/ethernet/link_error_disable/wait_time_in_sec (uint32)
    """
    return self.__wait_time_in_sec
      
  def _set_wait_time_in_sec(self, v, load=False):
    """
    Setter method for wait_time_in_sec, mapped from YANG variable /interface/ethernet/link_error_disable/wait_time_in_sec (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_wait_time_in_sec is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_wait_time_in_sec() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65565']}), is_leaf=True, yang_name="wait-time-in-sec", rest_name="wait-time-in-sec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'NUMBER:0-65565;;wait-time-in-sec'}}, namespace='urn:brocade.com:mgmt:brocade-pld', defining_module='brocade-pld', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """wait_time_in_sec must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65565']}), is_leaf=True, yang_name="wait-time-in-sec", rest_name="wait-time-in-sec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'NUMBER:0-65565;;wait-time-in-sec'}}, namespace='urn:brocade.com:mgmt:brocade-pld', defining_module='brocade-pld', yang_type='uint32', is_config=True)""",
        })

    self.__wait_time_in_sec = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_wait_time_in_sec(self):
    self.__wait_time_in_sec = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65565']}), is_leaf=True, yang_name="wait-time-in-sec", rest_name="wait-time-in-sec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'NUMBER:0-65565;;wait-time-in-sec'}}, namespace='urn:brocade.com:mgmt:brocade-pld', defining_module='brocade-pld', yang_type='uint32', is_config=True)

  link_error_disable_entry = __builtin__.property(_get_link_error_disable_entry, _set_link_error_disable_entry)
  sampling_time_in_sec = __builtin__.property(_get_sampling_time_in_sec, _set_sampling_time_in_sec)
  wait_time_in_sec = __builtin__.property(_get_wait_time_in_sec, _set_wait_time_in_sec)


  _pyangbind_elements = {'link_error_disable_entry': link_error_disable_entry, 'sampling_time_in_sec': sampling_time_in_sec, 'wait_time_in_sec': wait_time_in_sec, }


