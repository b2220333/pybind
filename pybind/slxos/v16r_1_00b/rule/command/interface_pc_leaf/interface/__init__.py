
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-aaa - based on the path /rule/command/interface-pc-leaf/interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__port_channel_leaf',)

  _yang_name = 'interface'
  _rest_name = 'interface'

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
    self.__port_channel_leaf = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}), is_leaf=True, yang_name="port-channel-leaf", rest_name="port-channel", parent=self, choice=(u'cmdlist', u'interface-j'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'port-channel'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='interface:portchannel-type', is_config=True)

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
      return [u'rule', u'command', u'interface-pc-leaf', u'interface']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rule', u'command', u'interface']

  def _get_port_channel_leaf(self):
    """
    Getter method for port_channel_leaf, mapped from YANG variable /rule/command/interface_pc_leaf/interface/port_channel_leaf (interface:portchannel-type)
    """
    return self.__port_channel_leaf
      
  def _set_port_channel_leaf(self, v, load=False):
    """
    Setter method for port_channel_leaf, mapped from YANG variable /rule/command/interface_pc_leaf/interface/port_channel_leaf (interface:portchannel-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_channel_leaf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_channel_leaf() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}), is_leaf=True, yang_name="port-channel-leaf", rest_name="port-channel", parent=self, choice=(u'cmdlist', u'interface-j'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'port-channel'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='interface:portchannel-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_channel_leaf must be of a type compatible with interface:portchannel-type""",
          'defined-type': "interface:portchannel-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}), is_leaf=True, yang_name="port-channel-leaf", rest_name="port-channel", parent=self, choice=(u'cmdlist', u'interface-j'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'port-channel'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='interface:portchannel-type', is_config=True)""",
        })

    self.__port_channel_leaf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_channel_leaf(self):
    self.__port_channel_leaf = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}), is_leaf=True, yang_name="port-channel-leaf", rest_name="port-channel", parent=self, choice=(u'cmdlist', u'interface-j'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'port-channel'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='interface:portchannel-type', is_config=True)

  port_channel_leaf = __builtin__.property(_get_port_channel_leaf, _set_port_channel_leaf)

  __choices__ = {u'cmdlist': {u'interface-j': [u'port_channel_leaf']}}
  _pyangbind_elements = {'port_channel_leaf': port_channel_leaf, }

