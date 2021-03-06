
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class static_ac_lif(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mac-address-table - based on the path /mac-address-table/static/static-ac-lif. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mac_address_lif','__forward_lif','__logical_interface','__interface_type_lif','__logical_interface_name',)

  _yang_name = 'static-ac-lif'
  _rest_name = 'static-ac-lif'

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
    self.__forward_lif = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'forward': {'value': 1}},), is_leaf=True, yang_name="forward-lif", rest_name="forward-lif", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Forward'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)
    self.__mac_address_lif = YANGDynClass(base=unicode, is_leaf=True, yang_name="mac-address-lif", rest_name="mac-address-lif", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='mac-access-list:mac-address-type', is_config=True)
    self.__logical_interface = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'logical-interface': {'value': 1}},), is_leaf=True, yang_name="logical-interface", rest_name="logical-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Logical Interface'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)
    self.__interface_type_lif = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 7}, u'port-channel': {'value': 8}},), is_leaf=True, yang_name="interface-type-lif", rest_name="interface-type-lif", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Logical Ethernet Interface'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)
    self.__logical_interface_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(((([0-9]|1[0-6])/([1-9]|[1-9][0-9])(:[1-4])?)|([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|10[0-1][0-9]|102[0-4]))\\.([1-9]|[1-9][0-9]+))'}), is_leaf=True, yang_name="logical-interface-name", rest_name="logical-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Logical interface name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='logical-ifname', is_config=True)

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
      return [u'mac-address-table', u'static', u'static-ac-lif']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mac-address-table', u'static', u'static-ac-lif']

  def _get_mac_address_lif(self):
    """
    Getter method for mac_address_lif, mapped from YANG variable /mac_address_table/static/static_ac_lif/mac_address_lif (mac-access-list:mac-address-type)
    """
    return self.__mac_address_lif
      
  def _set_mac_address_lif(self, v, load=False):
    """
    Setter method for mac_address_lif, mapped from YANG variable /mac_address_table/static/static_ac_lif/mac_address_lif (mac-access-list:mac-address-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_address_lif is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_address_lif() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mac-address-lif", rest_name="mac-address-lif", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='mac-access-list:mac-address-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_address_lif must be of a type compatible with mac-access-list:mac-address-type""",
          'defined-type': "mac-access-list:mac-address-type",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mac-address-lif", rest_name="mac-address-lif", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='mac-access-list:mac-address-type', is_config=True)""",
        })

    self.__mac_address_lif = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_address_lif(self):
    self.__mac_address_lif = YANGDynClass(base=unicode, is_leaf=True, yang_name="mac-address-lif", rest_name="mac-address-lif", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='mac-access-list:mac-address-type', is_config=True)


  def _get_forward_lif(self):
    """
    Getter method for forward_lif, mapped from YANG variable /mac_address_table/static/static_ac_lif/forward_lif (enumeration)
    """
    return self.__forward_lif
      
  def _set_forward_lif(self, v, load=False):
    """
    Setter method for forward_lif, mapped from YANG variable /mac_address_table/static/static_ac_lif/forward_lif (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_forward_lif is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_forward_lif() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'forward': {'value': 1}},), is_leaf=True, yang_name="forward-lif", rest_name="forward-lif", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Forward'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """forward_lif must be of a type compatible with enumeration""",
          'defined-type': "brocade-mac-address-table:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'forward': {'value': 1}},), is_leaf=True, yang_name="forward-lif", rest_name="forward-lif", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Forward'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)""",
        })

    self.__forward_lif = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_forward_lif(self):
    self.__forward_lif = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'forward': {'value': 1}},), is_leaf=True, yang_name="forward-lif", rest_name="forward-lif", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Forward'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)


  def _get_logical_interface(self):
    """
    Getter method for logical_interface, mapped from YANG variable /mac_address_table/static/static_ac_lif/logical_interface (enumeration)
    """
    return self.__logical_interface
      
  def _set_logical_interface(self, v, load=False):
    """
    Setter method for logical_interface, mapped from YANG variable /mac_address_table/static/static_ac_lif/logical_interface (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_logical_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_logical_interface() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'logical-interface': {'value': 1}},), is_leaf=True, yang_name="logical-interface", rest_name="logical-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Logical Interface'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """logical_interface must be of a type compatible with enumeration""",
          'defined-type': "brocade-mac-address-table:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'logical-interface': {'value': 1}},), is_leaf=True, yang_name="logical-interface", rest_name="logical-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Logical Interface'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)""",
        })

    self.__logical_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_logical_interface(self):
    self.__logical_interface = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'logical-interface': {'value': 1}},), is_leaf=True, yang_name="logical-interface", rest_name="logical-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Logical Interface'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)


  def _get_interface_type_lif(self):
    """
    Getter method for interface_type_lif, mapped from YANG variable /mac_address_table/static/static_ac_lif/interface_type_lif (enumeration)
    """
    return self.__interface_type_lif
      
  def _set_interface_type_lif(self, v, load=False):
    """
    Setter method for interface_type_lif, mapped from YANG variable /mac_address_table/static/static_ac_lif/interface_type_lif (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_type_lif is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_type_lif() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 7}, u'port-channel': {'value': 8}},), is_leaf=True, yang_name="interface-type-lif", rest_name="interface-type-lif", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Logical Ethernet Interface'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_type_lif must be of a type compatible with enumeration""",
          'defined-type': "brocade-mac-address-table:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 7}, u'port-channel': {'value': 8}},), is_leaf=True, yang_name="interface-type-lif", rest_name="interface-type-lif", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Logical Ethernet Interface'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)""",
        })

    self.__interface_type_lif = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_type_lif(self):
    self.__interface_type_lif = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 7}, u'port-channel': {'value': 8}},), is_leaf=True, yang_name="interface-type-lif", rest_name="interface-type-lif", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Logical Ethernet Interface'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)


  def _get_logical_interface_name(self):
    """
    Getter method for logical_interface_name, mapped from YANG variable /mac_address_table/static/static_ac_lif/logical_interface_name (logical-ifname)
    """
    return self.__logical_interface_name
      
  def _set_logical_interface_name(self, v, load=False):
    """
    Setter method for logical_interface_name, mapped from YANG variable /mac_address_table/static/static_ac_lif/logical_interface_name (logical-ifname)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_logical_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_logical_interface_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(((([0-9]|1[0-6])/([1-9]|[1-9][0-9])(:[1-4])?)|([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|10[0-1][0-9]|102[0-4]))\\.([1-9]|[1-9][0-9]+))'}), is_leaf=True, yang_name="logical-interface-name", rest_name="logical-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Logical interface name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='logical-ifname', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """logical_interface_name must be of a type compatible with logical-ifname""",
          'defined-type': "brocade-mac-address-table:logical-ifname",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(((([0-9]|1[0-6])/([1-9]|[1-9][0-9])(:[1-4])?)|([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|10[0-1][0-9]|102[0-4]))\\.([1-9]|[1-9][0-9]+))'}), is_leaf=True, yang_name="logical-interface-name", rest_name="logical-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Logical interface name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='logical-ifname', is_config=True)""",
        })

    self.__logical_interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_logical_interface_name(self):
    self.__logical_interface_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(((([0-9]|1[0-6])/([1-9]|[1-9][0-9])(:[1-4])?)|([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|10[0-1][0-9]|102[0-4]))\\.([1-9]|[1-9][0-9]+))'}), is_leaf=True, yang_name="logical-interface-name", rest_name="logical-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Logical interface name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='logical-ifname', is_config=True)

  mac_address_lif = __builtin__.property(_get_mac_address_lif, _set_mac_address_lif)
  forward_lif = __builtin__.property(_get_forward_lif, _set_forward_lif)
  logical_interface = __builtin__.property(_get_logical_interface, _set_logical_interface)
  interface_type_lif = __builtin__.property(_get_interface_type_lif, _set_interface_type_lif)
  logical_interface_name = __builtin__.property(_get_logical_interface_name, _set_logical_interface_name)


  _pyangbind_elements = {'mac_address_lif': mac_address_lif, 'forward_lif': forward_lif, 'logical_interface': logical_interface, 'interface_type_lif': interface_type_lif, 'logical_interface_name': logical_interface_name, }


