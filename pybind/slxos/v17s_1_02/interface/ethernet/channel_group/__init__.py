
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class channel_group(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/ethernet/channel-group. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: A container of configuration leaf elements for managing
the channel-group membership.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__port_int','__mode','__type',)

  _yang_name = 'channel-group'
  _rest_name = 'channel-group'

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
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'standard': {'value': 1}},), is_leaf=True, yang_name="type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The type of the port-channel.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='po-type', is_config=True)
    self.__mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'active': {'value': 1}, u'passive': {'value': 2}, u'on': {'value': 3}},), is_leaf=True, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The mode of the port channel.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='po-mode', is_config=True)
    self.__port_int = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1024']}), is_leaf=True, yang_name="port-int", rest_name="port-int", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Channel group number', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='portchannel-type', is_config=True)

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
      return [u'interface', u'ethernet', u'channel-group']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ethernet', u'channel-group']

  def _get_port_int(self):
    """
    Getter method for port_int, mapped from YANG variable /interface/ethernet/channel_group/port_int (portchannel-type)

    YANG Description: The port channel number.
    """
    return self.__port_int
      
  def _set_port_int(self, v, load=False):
    """
    Setter method for port_int, mapped from YANG variable /interface/ethernet/channel_group/port_int (portchannel-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_int is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_int() directly.

    YANG Description: The port channel number.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1024']}), is_leaf=True, yang_name="port-int", rest_name="port-int", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Channel group number', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='portchannel-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_int must be of a type compatible with portchannel-type""",
          'defined-type': "brocade-interface:portchannel-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1024']}), is_leaf=True, yang_name="port-int", rest_name="port-int", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Channel group number', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='portchannel-type', is_config=True)""",
        })

    self.__port_int = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_int(self):
    self.__port_int = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1024']}), is_leaf=True, yang_name="port-int", rest_name="port-int", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Channel group number', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='portchannel-type', is_config=True)


  def _get_mode(self):
    """
    Getter method for mode, mapped from YANG variable /interface/ethernet/channel_group/mode (po-mode)

    YANG Description: The mode of the port channel.
    """
    return self.__mode
      
  def _set_mode(self, v, load=False):
    """
    Setter method for mode, mapped from YANG variable /interface/ethernet/channel_group/mode (po-mode)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mode() directly.

    YANG Description: The mode of the port channel.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'active': {'value': 1}, u'passive': {'value': 2}, u'on': {'value': 3}},), is_leaf=True, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The mode of the port channel.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='po-mode', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mode must be of a type compatible with po-mode""",
          'defined-type': "brocade-interface:po-mode",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'active': {'value': 1}, u'passive': {'value': 2}, u'on': {'value': 3}},), is_leaf=True, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The mode of the port channel.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='po-mode', is_config=True)""",
        })

    self.__mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mode(self):
    self.__mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'active': {'value': 1}, u'passive': {'value': 2}, u'on': {'value': 3}},), is_leaf=True, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The mode of the port channel.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='po-mode', is_config=True)


  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /interface/ethernet/channel_group/type (po-type)

    YANG Description: The type of the port-channel.
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /interface/ethernet/channel_group/type (po-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: The type of the port-channel.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'standard': {'value': 1}},), is_leaf=True, yang_name="type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The type of the port-channel.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='po-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with po-type""",
          'defined-type': "brocade-interface:po-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'standard': {'value': 1}},), is_leaf=True, yang_name="type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The type of the port-channel.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='po-type', is_config=True)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'standard': {'value': 1}},), is_leaf=True, yang_name="type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The type of the port-channel.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='po-type', is_config=True)

  port_int = __builtin__.property(_get_port_int, _set_port_int)
  mode = __builtin__.property(_get_mode, _set_mode)
  type = __builtin__.property(_get_type, _set_type)


  _pyangbind_elements = {'port_int': port_int, 'mode': mode, 'type': type, }


