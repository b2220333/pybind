
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class non_empty_voq(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-sysdiag-operational - based on the path /tm-state/non-empty-voq. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: non empty voq's in the system
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__slot','__tower','__voq_id','__voq_size',)

  _yang_name = 'non-empty-voq'
  _rest_name = 'non-empty-voq'

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
    self.__slot = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="slot", rest_name="slot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    self.__voq_id = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="voq-id", rest_name="voq-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint32', is_config=False)
    self.__tower = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tower", rest_name="tower", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    self.__voq_size = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="voq-size", rest_name="voq-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint32', is_config=False)

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
      return [u'tm-state', u'non-empty-voq']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'tm-state', u'non-empty-voq']

  def _get_slot(self):
    """
    Getter method for slot, mapped from YANG variable /tm_state/non_empty_voq/slot (uint16)

    YANG Description: slot id
    """
    return self.__slot
      
  def _set_slot(self, v, load=False):
    """
    Setter method for slot, mapped from YANG variable /tm_state/non_empty_voq/slot (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_slot is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_slot() directly.

    YANG Description: slot id
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="slot", rest_name="slot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """slot must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="slot", rest_name="slot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)""",
        })

    self.__slot = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_slot(self):
    self.__slot = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="slot", rest_name="slot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)


  def _get_tower(self):
    """
    Getter method for tower, mapped from YANG variable /tm_state/non_empty_voq/tower (uint16)

    YANG Description: tower id
    """
    return self.__tower
      
  def _set_tower(self, v, load=False):
    """
    Setter method for tower, mapped from YANG variable /tm_state/non_empty_voq/tower (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tower is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tower() directly.

    YANG Description: tower id
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tower", rest_name="tower", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tower must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tower", rest_name="tower", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)""",
        })

    self.__tower = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tower(self):
    self.__tower = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tower", rest_name="tower", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)


  def _get_voq_id(self):
    """
    Getter method for voq_id, mapped from YANG variable /tm_state/non_empty_voq/voq_id (uint32)

    YANG Description: voq id
    """
    return self.__voq_id
      
  def _set_voq_id(self, v, load=False):
    """
    Setter method for voq_id, mapped from YANG variable /tm_state/non_empty_voq/voq_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_voq_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_voq_id() directly.

    YANG Description: voq id
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="voq-id", rest_name="voq-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """voq_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="voq-id", rest_name="voq-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint32', is_config=False)""",
        })

    self.__voq_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_voq_id(self):
    self.__voq_id = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="voq-id", rest_name="voq-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint32', is_config=False)


  def _get_voq_size(self):
    """
    Getter method for voq_size, mapped from YANG variable /tm_state/non_empty_voq/voq_size (uint32)

    YANG Description: queue size
    """
    return self.__voq_size
      
  def _set_voq_size(self, v, load=False):
    """
    Setter method for voq_size, mapped from YANG variable /tm_state/non_empty_voq/voq_size (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_voq_size is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_voq_size() directly.

    YANG Description: queue size
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="voq-size", rest_name="voq-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """voq_size must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="voq-size", rest_name="voq-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint32', is_config=False)""",
        })

    self.__voq_size = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_voq_size(self):
    self.__voq_size = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="voq-size", rest_name="voq-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint32', is_config=False)

  slot = __builtin__.property(_get_slot)
  tower = __builtin__.property(_get_tower)
  voq_id = __builtin__.property(_get_voq_id)
  voq_size = __builtin__.property(_get_voq_size)


  _pyangbind_elements = {'slot': slot, 'tower': tower, 'voq_id': voq_id, 'voq_size': voq_size, }


