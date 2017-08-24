
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class interface_hello_multiplier(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/interface/loopback/intf-isis/interface-isis/interface-hello-multiplier. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__interface_hello_multiplier_level','__interface_hello_multiplier_val',)

  _yang_name = 'interface-hello-multiplier'
  _rest_name = 'hello-multiplier'

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
    self.__interface_hello_multiplier_val = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..1000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(3), is_leaf=True, yang_name="interface-hello-multiplier-val", rest_name="interface-hello-multiplier-val", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)
    self.__interface_hello_multiplier_level = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'level-2': {'value': 2}, u'level-1': {'value': 1}},), is_leaf=True, yang_name="interface-hello-multiplier-level", rest_name="interface-hello-multiplier-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='enumeration', is_config=True)

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
      return [u'routing-system', u'interface', u'loopback', u'intf-isis', u'interface-isis', u'interface-hello-multiplier']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Loopback', u'isis', u'hello-multiplier']

  def _get_interface_hello_multiplier_level(self):
    """
    Getter method for interface_hello_multiplier_level, mapped from YANG variable /routing_system/interface/loopback/intf_isis/interface_isis/interface_hello_multiplier/interface_hello_multiplier_level (enumeration)
    """
    return self.__interface_hello_multiplier_level
      
  def _set_interface_hello_multiplier_level(self, v, load=False):
    """
    Setter method for interface_hello_multiplier_level, mapped from YANG variable /routing_system/interface/loopback/intf_isis/interface_isis/interface_hello_multiplier/interface_hello_multiplier_level (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_hello_multiplier_level is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_hello_multiplier_level() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'level-2': {'value': 2}, u'level-1': {'value': 1}},), is_leaf=True, yang_name="interface-hello-multiplier-level", rest_name="interface-hello-multiplier-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_hello_multiplier_level must be of a type compatible with enumeration""",
          'defined-type': "brocade-isis:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'level-2': {'value': 2}, u'level-1': {'value': 1}},), is_leaf=True, yang_name="interface-hello-multiplier-level", rest_name="interface-hello-multiplier-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='enumeration', is_config=True)""",
        })

    self.__interface_hello_multiplier_level = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_hello_multiplier_level(self):
    self.__interface_hello_multiplier_level = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'level-2': {'value': 2}, u'level-1': {'value': 1}},), is_leaf=True, yang_name="interface-hello-multiplier-level", rest_name="interface-hello-multiplier-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='enumeration', is_config=True)


  def _get_interface_hello_multiplier_val(self):
    """
    Getter method for interface_hello_multiplier_val, mapped from YANG variable /routing_system/interface/loopback/intf_isis/interface_isis/interface_hello_multiplier/interface_hello_multiplier_val (uint32)
    """
    return self.__interface_hello_multiplier_val
      
  def _set_interface_hello_multiplier_val(self, v, load=False):
    """
    Setter method for interface_hello_multiplier_val, mapped from YANG variable /routing_system/interface/loopback/intf_isis/interface_isis/interface_hello_multiplier/interface_hello_multiplier_val (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_hello_multiplier_val is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_hello_multiplier_val() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..1000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(3), is_leaf=True, yang_name="interface-hello-multiplier-val", rest_name="interface-hello-multiplier-val", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_hello_multiplier_val must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..1000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(3), is_leaf=True, yang_name="interface-hello-multiplier-val", rest_name="interface-hello-multiplier-val", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)""",
        })

    self.__interface_hello_multiplier_val = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_hello_multiplier_val(self):
    self.__interface_hello_multiplier_val = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..1000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(3), is_leaf=True, yang_name="interface-hello-multiplier-val", rest_name="interface-hello-multiplier-val", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)

  interface_hello_multiplier_level = __builtin__.property(_get_interface_hello_multiplier_level, _set_interface_hello_multiplier_level)
  interface_hello_multiplier_val = __builtin__.property(_get_interface_hello_multiplier_val, _set_interface_hello_multiplier_val)


  _pyangbind_elements = {'interface_hello_multiplier_level': interface_hello_multiplier_level, 'interface_hello_multiplier_val': interface_hello_multiplier_val, }


