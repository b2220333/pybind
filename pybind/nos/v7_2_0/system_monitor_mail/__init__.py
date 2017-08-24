
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import fru
import sfp
import security
import interface
import relay
class system_monitor_mail(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-system-monitor - based on the path /system-monitor-mail. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__fru','__sfp','__security','__interface','__relay',)

  _yang_name = 'system-monitor-mail'
  _rest_name = 'system-monitor-mail'

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
    self.__interface = YANGDynClass(base=interface.interface, is_container='container', presence=False, yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure interface mail settings'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)
    self.__security = YANGDynClass(base=security.security, is_container='container', presence=False, yang_name="security", rest_name="security", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure security mail settings'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)
    self.__relay = YANGDynClass(base=YANGListType("host_ip",relay.relay, yang_name="relay", rest_name="relay", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='host-ip', extensions={u'tailf-common': {u'info': u'Configure relay ip mail settings', u'cli-suppress-mode': None, u'callpoint': u'relay-ip-server', u'cli-suppress-key-abbreviation': None, u'cli-suppress-list-no': None}}), is_container='list', yang_name="relay", rest_name="relay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure relay ip mail settings', u'cli-suppress-mode': None, u'callpoint': u'relay-ip-server', u'cli-suppress-key-abbreviation': None, u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='list', is_config=True)
    self.__sfp = YANGDynClass(base=sfp.sfp, is_container='container', presence=False, yang_name="sfp", rest_name="sfp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure sfp mail settings'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)
    self.__fru = YANGDynClass(base=fru.fru, is_container='container', presence=False, yang_name="fru", rest_name="fru", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure FRU mail settings'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)

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
      return [u'system-monitor-mail']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'system-monitor-mail']

  def _get_fru(self):
    """
    Getter method for fru, mapped from YANG variable /system_monitor_mail/fru (container)
    """
    return self.__fru
      
  def _set_fru(self, v, load=False):
    """
    Setter method for fru, mapped from YANG variable /system_monitor_mail/fru (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fru is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fru() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=fru.fru, is_container='container', presence=False, yang_name="fru", rest_name="fru", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure FRU mail settings'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fru must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=fru.fru, is_container='container', presence=False, yang_name="fru", rest_name="fru", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure FRU mail settings'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)""",
        })

    self.__fru = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fru(self):
    self.__fru = YANGDynClass(base=fru.fru, is_container='container', presence=False, yang_name="fru", rest_name="fru", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure FRU mail settings'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)


  def _get_sfp(self):
    """
    Getter method for sfp, mapped from YANG variable /system_monitor_mail/sfp (container)
    """
    return self.__sfp
      
  def _set_sfp(self, v, load=False):
    """
    Setter method for sfp, mapped from YANG variable /system_monitor_mail/sfp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sfp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sfp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=sfp.sfp, is_container='container', presence=False, yang_name="sfp", rest_name="sfp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure sfp mail settings'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sfp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=sfp.sfp, is_container='container', presence=False, yang_name="sfp", rest_name="sfp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure sfp mail settings'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)""",
        })

    self.__sfp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sfp(self):
    self.__sfp = YANGDynClass(base=sfp.sfp, is_container='container', presence=False, yang_name="sfp", rest_name="sfp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure sfp mail settings'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)


  def _get_security(self):
    """
    Getter method for security, mapped from YANG variable /system_monitor_mail/security (container)
    """
    return self.__security
      
  def _set_security(self, v, load=False):
    """
    Setter method for security, mapped from YANG variable /system_monitor_mail/security (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_security is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_security() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=security.security, is_container='container', presence=False, yang_name="security", rest_name="security", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure security mail settings'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """security must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=security.security, is_container='container', presence=False, yang_name="security", rest_name="security", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure security mail settings'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)""",
        })

    self.__security = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_security(self):
    self.__security = YANGDynClass(base=security.security, is_container='container', presence=False, yang_name="security", rest_name="security", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure security mail settings'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)


  def _get_interface(self):
    """
    Getter method for interface, mapped from YANG variable /system_monitor_mail/interface (container)
    """
    return self.__interface
      
  def _set_interface(self, v, load=False):
    """
    Setter method for interface, mapped from YANG variable /system_monitor_mail/interface (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interface.interface, is_container='container', presence=False, yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure interface mail settings'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface.interface, is_container='container', presence=False, yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure interface mail settings'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)""",
        })

    self.__interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface(self):
    self.__interface = YANGDynClass(base=interface.interface, is_container='container', presence=False, yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure interface mail settings'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)


  def _get_relay(self):
    """
    Getter method for relay, mapped from YANG variable /system_monitor_mail/relay (list)
    """
    return self.__relay
      
  def _set_relay(self, v, load=False):
    """
    Setter method for relay, mapped from YANG variable /system_monitor_mail/relay (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_relay is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_relay() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("host_ip",relay.relay, yang_name="relay", rest_name="relay", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='host-ip', extensions={u'tailf-common': {u'info': u'Configure relay ip mail settings', u'cli-suppress-mode': None, u'callpoint': u'relay-ip-server', u'cli-suppress-key-abbreviation': None, u'cli-suppress-list-no': None}}), is_container='list', yang_name="relay", rest_name="relay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure relay ip mail settings', u'cli-suppress-mode': None, u'callpoint': u'relay-ip-server', u'cli-suppress-key-abbreviation': None, u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """relay must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("host_ip",relay.relay, yang_name="relay", rest_name="relay", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='host-ip', extensions={u'tailf-common': {u'info': u'Configure relay ip mail settings', u'cli-suppress-mode': None, u'callpoint': u'relay-ip-server', u'cli-suppress-key-abbreviation': None, u'cli-suppress-list-no': None}}), is_container='list', yang_name="relay", rest_name="relay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure relay ip mail settings', u'cli-suppress-mode': None, u'callpoint': u'relay-ip-server', u'cli-suppress-key-abbreviation': None, u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='list', is_config=True)""",
        })

    self.__relay = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_relay(self):
    self.__relay = YANGDynClass(base=YANGListType("host_ip",relay.relay, yang_name="relay", rest_name="relay", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='host-ip', extensions={u'tailf-common': {u'info': u'Configure relay ip mail settings', u'cli-suppress-mode': None, u'callpoint': u'relay-ip-server', u'cli-suppress-key-abbreviation': None, u'cli-suppress-list-no': None}}), is_container='list', yang_name="relay", rest_name="relay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure relay ip mail settings', u'cli-suppress-mode': None, u'callpoint': u'relay-ip-server', u'cli-suppress-key-abbreviation': None, u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='list', is_config=True)

  fru = __builtin__.property(_get_fru, _set_fru)
  sfp = __builtin__.property(_get_sfp, _set_sfp)
  security = __builtin__.property(_get_security, _set_security)
  interface = __builtin__.property(_get_interface, _set_interface)
  relay = __builtin__.property(_get_relay, _set_relay)


  _pyangbind_elements = {'fru': fru, 'sfp': sfp, 'security': security, 'interface': interface, 'relay': relay, }


