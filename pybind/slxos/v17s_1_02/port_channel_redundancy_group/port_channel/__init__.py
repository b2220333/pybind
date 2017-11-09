
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class port_channel(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-lag - based on the path /port-channel-redundancy-group/port-channel. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The list of port-channels in the managed device. Each
entry represents a port-channel.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__name','__port_channel_active',)

  _yang_name = 'port-channel'
  _rest_name = 'port-channel'

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
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1024']}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-lag', defining_module='brocade-lag', yang_type='interface:portchannel-type', is_config=True)
    self.__port_channel_active = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="port-channel-active", rest_name="active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Select port-channel as active in port-channel redundancy group.', u'alt-name': u'active'}}, namespace='urn:brocade.com:mgmt:brocade-lag', defining_module='brocade-lag', yang_type='empty', is_config=True)

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
      return [u'port-channel-redundancy-group', u'port-channel']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'port-channel-redundancy-group', u'port-channel']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /port_channel_redundancy_group/port_channel/name (interface:portchannel-type)

    YANG Description: The port-channel identifier.
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /port_channel_redundancy_group/port_channel/name (interface:portchannel-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: The port-channel identifier.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1024']}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-lag', defining_module='brocade-lag', yang_type='interface:portchannel-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with interface:portchannel-type""",
          'defined-type': "interface:portchannel-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1024']}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-lag', defining_module='brocade-lag', yang_type='interface:portchannel-type', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1024']}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-lag', defining_module='brocade-lag', yang_type='interface:portchannel-type', is_config=True)


  def _get_port_channel_active(self):
    """
    Getter method for port_channel_active, mapped from YANG variable /port_channel_redundancy_group/port_channel/port_channel_active (empty)
    """
    return self.__port_channel_active
      
  def _set_port_channel_active(self, v, load=False):
    """
    Setter method for port_channel_active, mapped from YANG variable /port_channel_redundancy_group/port_channel/port_channel_active (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_channel_active is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_channel_active() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="port-channel-active", rest_name="active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Select port-channel as active in port-channel redundancy group.', u'alt-name': u'active'}}, namespace='urn:brocade.com:mgmt:brocade-lag', defining_module='brocade-lag', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_channel_active must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="port-channel-active", rest_name="active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Select port-channel as active in port-channel redundancy group.', u'alt-name': u'active'}}, namespace='urn:brocade.com:mgmt:brocade-lag', defining_module='brocade-lag', yang_type='empty', is_config=True)""",
        })

    self.__port_channel_active = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_channel_active(self):
    self.__port_channel_active = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="port-channel-active", rest_name="active", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Select port-channel as active in port-channel redundancy group.', u'alt-name': u'active'}}, namespace='urn:brocade.com:mgmt:brocade-lag', defining_module='brocade-lag', yang_type='empty', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  port_channel_active = __builtin__.property(_get_port_channel_active, _set_port_channel_active)


  _pyangbind_elements = {'name': name, 'port_channel_active': port_channel_active, }


