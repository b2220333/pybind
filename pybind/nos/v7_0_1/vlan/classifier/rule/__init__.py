
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import mac
import proto
class rule(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vlan - based on the path /vlan/classifier/rule. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ruleid','__mac','__proto',)

  _yang_name = 'rule'
  _rest_name = 'rule'

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
    self.__mac = YANGDynClass(base=mac.mac, is_container='container', yang_name="mac", rest_name="mac", parent=self, choice=(u'class-type', u'mac'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MAC address classification by source MAC address', u'cli-suppress-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='container', is_config=True)
    self.__proto = YANGDynClass(base=proto.proto, is_container='container', yang_name="proto", rest_name="proto", parent=self, choice=(u'class-type', u'proto'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Proto - specify an ethernet protocol\n                            classification', u'cli-sequence-commands': None, u'cli-suppress-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='container', is_config=True)
    self.__ruleid = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..256']}), is_leaf=True, yang_name="ruleid", rest_name="ruleid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='uint32', is_config=True)

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
      return [u'vlan', u'classifier', u'rule']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'vlan', u'classifier', u'rule']

  def _get_ruleid(self):
    """
    Getter method for ruleid, mapped from YANG variable /vlan/classifier/rule/ruleid (uint32)
    """
    return self.__ruleid
      
  def _set_ruleid(self, v, load=False):
    """
    Setter method for ruleid, mapped from YANG variable /vlan/classifier/rule/ruleid (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ruleid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ruleid() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..256']}), is_leaf=True, yang_name="ruleid", rest_name="ruleid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ruleid must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..256']}), is_leaf=True, yang_name="ruleid", rest_name="ruleid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='uint32', is_config=True)""",
        })

    self.__ruleid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ruleid(self):
    self.__ruleid = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..256']}), is_leaf=True, yang_name="ruleid", rest_name="ruleid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='uint32', is_config=True)


  def _get_mac(self):
    """
    Getter method for mac, mapped from YANG variable /vlan/classifier/rule/mac (container)
    """
    return self.__mac
      
  def _set_mac(self, v, load=False):
    """
    Setter method for mac, mapped from YANG variable /vlan/classifier/rule/mac (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac() directly.
    """
    try:
      t = YANGDynClass(v,base=mac.mac, is_container='container', yang_name="mac", rest_name="mac", parent=self, choice=(u'class-type', u'mac'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MAC address classification by source MAC address', u'cli-suppress-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=mac.mac, is_container='container', yang_name="mac", rest_name="mac", parent=self, choice=(u'class-type', u'mac'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MAC address classification by source MAC address', u'cli-suppress-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='container', is_config=True)""",
        })

    self.__mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac(self):
    self.__mac = YANGDynClass(base=mac.mac, is_container='container', yang_name="mac", rest_name="mac", parent=self, choice=(u'class-type', u'mac'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MAC address classification by source MAC address', u'cli-suppress-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='container', is_config=True)


  def _get_proto(self):
    """
    Getter method for proto, mapped from YANG variable /vlan/classifier/rule/proto (container)
    """
    return self.__proto
      
  def _set_proto(self, v, load=False):
    """
    Setter method for proto, mapped from YANG variable /vlan/classifier/rule/proto (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_proto is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_proto() directly.
    """
    try:
      t = YANGDynClass(v,base=proto.proto, is_container='container', yang_name="proto", rest_name="proto", parent=self, choice=(u'class-type', u'proto'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Proto - specify an ethernet protocol\n                            classification', u'cli-sequence-commands': None, u'cli-suppress-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """proto must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=proto.proto, is_container='container', yang_name="proto", rest_name="proto", parent=self, choice=(u'class-type', u'proto'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Proto - specify an ethernet protocol\n                            classification', u'cli-sequence-commands': None, u'cli-suppress-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='container', is_config=True)""",
        })

    self.__proto = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_proto(self):
    self.__proto = YANGDynClass(base=proto.proto, is_container='container', yang_name="proto", rest_name="proto", parent=self, choice=(u'class-type', u'proto'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Proto - specify an ethernet protocol\n                            classification', u'cli-sequence-commands': None, u'cli-suppress-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='container', is_config=True)

  ruleid = __builtin__.property(_get_ruleid, _set_ruleid)
  mac = __builtin__.property(_get_mac, _set_mac)
  proto = __builtin__.property(_get_proto, _set_proto)

  __choices__ = {u'class-type': {u'mac': [u'mac'], u'proto': [u'proto']}}
  _pyangbind_elements = {'ruleid': ruleid, 'mac': mac, 'proto': proto, }

