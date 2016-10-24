
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
  from YANG module brocade-openflow-operational - based on the path /openflow-state/interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Openflow enabled interface details
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__port','__link','__port_state','__speed','__mac','__port_id','__mode',)

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
    self.__port_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="port-id", rest_name="port-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__port_state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-port-state-live': {'value': 3}, u'dcm-port-state-forward': {'value': 4}, u'dcm-port-state-invalid': {'value': 0}, u'dcm-port-state-blocked': {'value': 2}, u'dcm-port-state-link-down': {'value': 1}},), is_leaf=True, yang_name="port-state", rest_name="port-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='port-state', is_config=False)
    self.__mac = YANGDynClass(base=unicode, is_leaf=True, yang_name="mac", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    self.__link = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="link", rest_name="link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='boolean', is_config=False)
    self.__mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-port-mode-unknown': {'value': 0}, u'dcm-port-mode-hybrid-l3': {'value': 5}, u'dcm-port-mode-hybrid-l2': {'value': 4}, u'dcm-port-mode-l23': {'value': 3}, u'dcm-port-mode-hybrid-l23': {'value': 6}, u'dcm-port-mode-l3': {'value': 2}, u'dcm-port-mode-l2': {'value': 1}},), is_leaf=True, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='port-mode', is_config=False)
    self.__speed = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-port-speed-gig': {'value': 1}, u'dcm-port-speed-hundredgig': {'value': 4}, u'dcm-port-speed-tengig': {'value': 2}, u'dcm-port-speed-fortygig': {'value': 3}, u'dcm-port-speed-unknown': {'value': 0}},), is_leaf=True, yang_name="speed", rest_name="speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='port-speed', is_config=False)
    self.__port = YANGDynClass(base=unicode, is_leaf=True, yang_name="port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)

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
      return [u'openflow-state', u'interface']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'openflow-state', u'interface']

  def _get_port(self):
    """
    Getter method for port, mapped from YANG variable /openflow_state/interface/port (string)

    YANG Description: Port
    """
    return self.__port
      
  def _set_port(self, v, load=False):
    """
    Setter method for port, mapped from YANG variable /openflow_state/interface/port (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port() directly.

    YANG Description: Port
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)""",
        })

    self.__port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port(self):
    self.__port = YANGDynClass(base=unicode, is_leaf=True, yang_name="port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)


  def _get_link(self):
    """
    Getter method for link, mapped from YANG variable /openflow_state/interface/link (boolean)

    YANG Description: Link
    """
    return self.__link
      
  def _set_link(self, v, load=False):
    """
    Setter method for link, mapped from YANG variable /openflow_state/interface/link (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link() directly.

    YANG Description: Link
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="link", rest_name="link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="link", rest_name="link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='boolean', is_config=False)""",
        })

    self.__link = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link(self):
    self.__link = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="link", rest_name="link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='boolean', is_config=False)


  def _get_port_state(self):
    """
    Getter method for port_state, mapped from YANG variable /openflow_state/interface/port_state (port-state)

    YANG Description: Port State
    """
    return self.__port_state
      
  def _set_port_state(self, v, load=False):
    """
    Setter method for port_state, mapped from YANG variable /openflow_state/interface/port_state (port-state)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_state() directly.

    YANG Description: Port State
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-port-state-live': {'value': 3}, u'dcm-port-state-forward': {'value': 4}, u'dcm-port-state-invalid': {'value': 0}, u'dcm-port-state-blocked': {'value': 2}, u'dcm-port-state-link-down': {'value': 1}},), is_leaf=True, yang_name="port-state", rest_name="port-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='port-state', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_state must be of a type compatible with port-state""",
          'defined-type': "brocade-openflow-operational:port-state",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-port-state-live': {'value': 3}, u'dcm-port-state-forward': {'value': 4}, u'dcm-port-state-invalid': {'value': 0}, u'dcm-port-state-blocked': {'value': 2}, u'dcm-port-state-link-down': {'value': 1}},), is_leaf=True, yang_name="port-state", rest_name="port-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='port-state', is_config=False)""",
        })

    self.__port_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_state(self):
    self.__port_state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-port-state-live': {'value': 3}, u'dcm-port-state-forward': {'value': 4}, u'dcm-port-state-invalid': {'value': 0}, u'dcm-port-state-blocked': {'value': 2}, u'dcm-port-state-link-down': {'value': 1}},), is_leaf=True, yang_name="port-state", rest_name="port-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='port-state', is_config=False)


  def _get_speed(self):
    """
    Getter method for speed, mapped from YANG variable /openflow_state/interface/speed (port-speed)

    YANG Description: Speed
    """
    return self.__speed
      
  def _set_speed(self, v, load=False):
    """
    Setter method for speed, mapped from YANG variable /openflow_state/interface/speed (port-speed)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_speed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_speed() directly.

    YANG Description: Speed
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-port-speed-gig': {'value': 1}, u'dcm-port-speed-hundredgig': {'value': 4}, u'dcm-port-speed-tengig': {'value': 2}, u'dcm-port-speed-fortygig': {'value': 3}, u'dcm-port-speed-unknown': {'value': 0}},), is_leaf=True, yang_name="speed", rest_name="speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='port-speed', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """speed must be of a type compatible with port-speed""",
          'defined-type': "brocade-openflow-operational:port-speed",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-port-speed-gig': {'value': 1}, u'dcm-port-speed-hundredgig': {'value': 4}, u'dcm-port-speed-tengig': {'value': 2}, u'dcm-port-speed-fortygig': {'value': 3}, u'dcm-port-speed-unknown': {'value': 0}},), is_leaf=True, yang_name="speed", rest_name="speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='port-speed', is_config=False)""",
        })

    self.__speed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_speed(self):
    self.__speed = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-port-speed-gig': {'value': 1}, u'dcm-port-speed-hundredgig': {'value': 4}, u'dcm-port-speed-tengig': {'value': 2}, u'dcm-port-speed-fortygig': {'value': 3}, u'dcm-port-speed-unknown': {'value': 0}},), is_leaf=True, yang_name="speed", rest_name="speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='port-speed', is_config=False)


  def _get_mac(self):
    """
    Getter method for mac, mapped from YANG variable /openflow_state/interface/mac (string)

    YANG Description: MAC
    """
    return self.__mac
      
  def _set_mac(self, v, load=False):
    """
    Setter method for mac, mapped from YANG variable /openflow_state/interface/mac (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac() directly.

    YANG Description: MAC
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mac", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mac", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)""",
        })

    self.__mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac(self):
    self.__mac = YANGDynClass(base=unicode, is_leaf=True, yang_name="mac", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)


  def _get_port_id(self):
    """
    Getter method for port_id, mapped from YANG variable /openflow_state/interface/port_id (uint32)

    YANG Description: OF-Port-ID
    """
    return self.__port_id
      
  def _set_port_id(self, v, load=False):
    """
    Setter method for port_id, mapped from YANG variable /openflow_state/interface/port_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_id() directly.

    YANG Description: OF-Port-ID
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="port-id", rest_name="port-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="port-id", rest_name="port-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__port_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_id(self):
    self.__port_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="port-id", rest_name="port-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_mode(self):
    """
    Getter method for mode, mapped from YANG variable /openflow_state/interface/mode (port-mode)

    YANG Description: Mode
    """
    return self.__mode
      
  def _set_mode(self, v, load=False):
    """
    Setter method for mode, mapped from YANG variable /openflow_state/interface/mode (port-mode)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mode() directly.

    YANG Description: Mode
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-port-mode-unknown': {'value': 0}, u'dcm-port-mode-hybrid-l3': {'value': 5}, u'dcm-port-mode-hybrid-l2': {'value': 4}, u'dcm-port-mode-l23': {'value': 3}, u'dcm-port-mode-hybrid-l23': {'value': 6}, u'dcm-port-mode-l3': {'value': 2}, u'dcm-port-mode-l2': {'value': 1}},), is_leaf=True, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='port-mode', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mode must be of a type compatible with port-mode""",
          'defined-type': "brocade-openflow-operational:port-mode",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-port-mode-unknown': {'value': 0}, u'dcm-port-mode-hybrid-l3': {'value': 5}, u'dcm-port-mode-hybrid-l2': {'value': 4}, u'dcm-port-mode-l23': {'value': 3}, u'dcm-port-mode-hybrid-l23': {'value': 6}, u'dcm-port-mode-l3': {'value': 2}, u'dcm-port-mode-l2': {'value': 1}},), is_leaf=True, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='port-mode', is_config=False)""",
        })

    self.__mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mode(self):
    self.__mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-port-mode-unknown': {'value': 0}, u'dcm-port-mode-hybrid-l3': {'value': 5}, u'dcm-port-mode-hybrid-l2': {'value': 4}, u'dcm-port-mode-l23': {'value': 3}, u'dcm-port-mode-hybrid-l23': {'value': 6}, u'dcm-port-mode-l3': {'value': 2}, u'dcm-port-mode-l2': {'value': 1}},), is_leaf=True, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='port-mode', is_config=False)

  port = __builtin__.property(_get_port)
  link = __builtin__.property(_get_link)
  port_state = __builtin__.property(_get_port_state)
  speed = __builtin__.property(_get_speed)
  mac = __builtin__.property(_get_mac)
  port_id = __builtin__.property(_get_port_id)
  mode = __builtin__.property(_get_mode)


  _pyangbind_elements = {'port': port, 'link': link, 'port_state': port_state, 'speed': speed, 'mac': mac, 'port_id': port_id, 'mode': mode, }


