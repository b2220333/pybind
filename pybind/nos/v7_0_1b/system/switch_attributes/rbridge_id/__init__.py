
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class rbridge_id(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ras - based on the path /system/switch-attributes/rbridge-id. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__rbridge_id','__chassis_name','__host_name',)

  _yang_name = 'rbridge-id'
  _rest_name = 'rbridge-id'

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
    self.__chassis_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..30']}), is_leaf=True, yang_name="chassis-name", rest_name="chassis-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Chassis name[length:1-30]'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='string', is_config=True)
    self.__rbridge_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9]', 'length': [u'1..3']}), is_leaf=True, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='switchidType-noall', is_config=True)
    self.__host_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..30']}), is_leaf=True, yang_name="host-name", rest_name="host-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Host name[length:1-30]'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='string', is_config=True)

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
      return [u'system', u'switch-attributes', u'rbridge-id']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'switch-attributes', u'rbridge-id']

  def _get_rbridge_id(self):
    """
    Getter method for rbridge_id, mapped from YANG variable /system/switch_attributes/rbridge_id/rbridge_id (switchidType-noall)
    """
    return self.__rbridge_id
      
  def _set_rbridge_id(self, v, load=False):
    """
    Setter method for rbridge_id, mapped from YANG variable /system/switch_attributes/rbridge_id/rbridge_id (switchidType-noall)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rbridge_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rbridge_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9]', 'length': [u'1..3']}), is_leaf=True, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='switchidType-noall', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rbridge_id must be of a type compatible with switchidType-noall""",
          'defined-type': "brocade-ras:switchidType-noall",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9]', 'length': [u'1..3']}), is_leaf=True, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='switchidType-noall', is_config=True)""",
        })

    self.__rbridge_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rbridge_id(self):
    self.__rbridge_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9]', 'length': [u'1..3']}), is_leaf=True, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='switchidType-noall', is_config=True)


  def _get_chassis_name(self):
    """
    Getter method for chassis_name, mapped from YANG variable /system/switch_attributes/rbridge_id/chassis_name (string)
    """
    return self.__chassis_name
      
  def _set_chassis_name(self, v, load=False):
    """
    Setter method for chassis_name, mapped from YANG variable /system/switch_attributes/rbridge_id/chassis_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_chassis_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_chassis_name() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..30']}), is_leaf=True, yang_name="chassis-name", rest_name="chassis-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Chassis name[length:1-30]'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """chassis_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..30']}), is_leaf=True, yang_name="chassis-name", rest_name="chassis-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Chassis name[length:1-30]'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='string', is_config=True)""",
        })

    self.__chassis_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_chassis_name(self):
    self.__chassis_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..30']}), is_leaf=True, yang_name="chassis-name", rest_name="chassis-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Chassis name[length:1-30]'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='string', is_config=True)


  def _get_host_name(self):
    """
    Getter method for host_name, mapped from YANG variable /system/switch_attributes/rbridge_id/host_name (string)
    """
    return self.__host_name
      
  def _set_host_name(self, v, load=False):
    """
    Setter method for host_name, mapped from YANG variable /system/switch_attributes/rbridge_id/host_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_host_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_host_name() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..30']}), is_leaf=True, yang_name="host-name", rest_name="host-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Host name[length:1-30]'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """host_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..30']}), is_leaf=True, yang_name="host-name", rest_name="host-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Host name[length:1-30]'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='string', is_config=True)""",
        })

    self.__host_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_host_name(self):
    self.__host_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..30']}), is_leaf=True, yang_name="host-name", rest_name="host-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Host name[length:1-30]'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='string', is_config=True)

  rbridge_id = __builtin__.property(_get_rbridge_id, _set_rbridge_id)
  chassis_name = __builtin__.property(_get_chassis_name, _set_chassis_name)
  host_name = __builtin__.property(_get_host_name, _set_host_name)


  _pyangbind_elements = {'rbridge_id': rbridge_id, 'chassis_name': chassis_name, 'host_name': host_name, }

