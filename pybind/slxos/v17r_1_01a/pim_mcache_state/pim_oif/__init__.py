
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class pim_oif(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-pim-operational - based on the path /pim-mcache-state/pim-oif. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: OIF information
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__oif_name','__age','__expiry_time','__oif_flags',)

  _yang_name = 'pim-oif'
  _rest_name = 'pim-oif'

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
    self.__oif_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="oif-name", rest_name="oif-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)
    self.__age = YANGDynClass(base=unicode, is_leaf=True, yang_name="age", rest_name="age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)
    self.__expiry_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="expiry-time", rest_name="expiry-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='uint32', is_config=False)
    self.__oif_flags = YANGDynClass(base=unicode, is_leaf=True, yang_name="oif-flags", rest_name="oif-flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)

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
      return [u'pim-mcache-state', u'pim-oif']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'pim-mcache-state', u'pim-oif']

  def _get_oif_name(self):
    """
    Getter method for oif_name, mapped from YANG variable /pim_mcache_state/pim_oif/oif_name (string)

    YANG Description: oif_name
    """
    return self.__oif_name
      
  def _set_oif_name(self, v, load=False):
    """
    Setter method for oif_name, mapped from YANG variable /pim_mcache_state/pim_oif/oif_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_oif_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_oif_name() directly.

    YANG Description: oif_name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="oif-name", rest_name="oif-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """oif_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="oif-name", rest_name="oif-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)""",
        })

    self.__oif_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_oif_name(self):
    self.__oif_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="oif-name", rest_name="oif-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)


  def _get_age(self):
    """
    Getter method for age, mapped from YANG variable /pim_mcache_state/pim_oif/age (string)

    YANG Description: Age
    """
    return self.__age
      
  def _set_age(self, v, load=False):
    """
    Setter method for age, mapped from YANG variable /pim_mcache_state/pim_oif/age (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_age is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_age() directly.

    YANG Description: Age
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="age", rest_name="age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """age must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="age", rest_name="age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)""",
        })

    self.__age = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_age(self):
    self.__age = YANGDynClass(base=unicode, is_leaf=True, yang_name="age", rest_name="age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)


  def _get_expiry_time(self):
    """
    Getter method for expiry_time, mapped from YANG variable /pim_mcache_state/pim_oif/expiry_time (uint32)

    YANG Description: expiry time
    """
    return self.__expiry_time
      
  def _set_expiry_time(self, v, load=False):
    """
    Setter method for expiry_time, mapped from YANG variable /pim_mcache_state/pim_oif/expiry_time (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_expiry_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_expiry_time() directly.

    YANG Description: expiry time
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="expiry-time", rest_name="expiry-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """expiry_time must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="expiry-time", rest_name="expiry-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='uint32', is_config=False)""",
        })

    self.__expiry_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_expiry_time(self):
    self.__expiry_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="expiry-time", rest_name="expiry-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='uint32', is_config=False)


  def _get_oif_flags(self):
    """
    Getter method for oif_flags, mapped from YANG variable /pim_mcache_state/pim_oif/oif_flags (string)

    YANG Description: oif flags
    """
    return self.__oif_flags
      
  def _set_oif_flags(self, v, load=False):
    """
    Setter method for oif_flags, mapped from YANG variable /pim_mcache_state/pim_oif/oif_flags (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_oif_flags is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_oif_flags() directly.

    YANG Description: oif flags
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="oif-flags", rest_name="oif-flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """oif_flags must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="oif-flags", rest_name="oif-flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)""",
        })

    self.__oif_flags = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_oif_flags(self):
    self.__oif_flags = YANGDynClass(base=unicode, is_leaf=True, yang_name="oif-flags", rest_name="oif-flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)

  oif_name = __builtin__.property(_get_oif_name)
  age = __builtin__.property(_get_age)
  expiry_time = __builtin__.property(_get_expiry_time)
  oif_flags = __builtin__.property(_get_oif_flags)


  _pyangbind_elements = {'oif_name': oif_name, 'age': age, 'expiry_time': expiry_time, 'oif_flags': oif_flags, }


