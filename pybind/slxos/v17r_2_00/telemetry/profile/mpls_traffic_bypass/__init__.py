
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import mpls_traffic_bypasses
import add_
class mpls_traffic_bypass(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-telemetry - based on the path /telemetry/profile/mpls-traffic-bypass. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__name','__interval','__mpls_traffic_bypasses','__add_',)

  _yang_name = 'mpls-traffic-bypass'
  _rest_name = 'mpls-traffic-bypass'

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
    self.__mpls_traffic_bypasses = YANGDynClass(base=YANGListType("mpls_traffic_bypass_name",mpls_traffic_bypasses.mpls_traffic_bypasses, yang_name="mpls-traffic-bypasses", rest_name="bypass-lsp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mpls-traffic-bypass-name', extensions={u'tailf-common': {u'callpoint': u'Mplstrafficbypass', u'cli-suppress-mode': None, u'alt-name': u'bypass-lsp', u'info': u'MPLS Stats profile by Bypass LSP name', u'cli-suppress-list-no': None}}), is_container='list', yang_name="mpls-traffic-bypasses", rest_name="bypass-lsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'Mplstrafficbypass', u'cli-suppress-mode': None, u'alt-name': u'bypass-lsp', u'info': u'MPLS Stats profile by Bypass LSP name', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='list', is_config=True)
    self.__add_ = YANGDynClass(base=YANGListType("object",add_.add_, yang_name="add", rest_name="add", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='object', extensions={u'tailf-common': {u'callpoint': u'MplstrafficbypassProfileObject', u'cli-suppress-list-no': None, u'cli-suppress-mode': None, u'info': u'Add MPLS traffic telemetry object'}}), is_container='list', yang_name="add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'MplstrafficbypassProfileObject', u'cli-suppress-list-no': None, u'cli-suppress-mode': None, u'info': u'Add MPLS traffic telemetry object'}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='list', is_config=True)
    self.__interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'60..3600']}), is_leaf=True, yang_name="interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'MPLS profile interval'}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='mpls-traffic-profile-interval-type', is_config=True)
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'default_mpls_traffic_bypass_statistics', 'length': [u'3..64']}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MPLS profile name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='mpls-traffic-bypass-profile-name-type', is_config=True)

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
      return [u'telemetry', u'profile', u'mpls-traffic-bypass']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'telemetry', u'profile', u'mpls-traffic-bypass']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /telemetry/profile/mpls_traffic_bypass/name (mpls-traffic-bypass-profile-name-type)
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /telemetry/profile/mpls_traffic_bypass/name (mpls-traffic-bypass-profile-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'default_mpls_traffic_bypass_statistics', 'length': [u'3..64']}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MPLS profile name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='mpls-traffic-bypass-profile-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with mpls-traffic-bypass-profile-name-type""",
          'defined-type': "brocade-telemetry:mpls-traffic-bypass-profile-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'default_mpls_traffic_bypass_statistics', 'length': [u'3..64']}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MPLS profile name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='mpls-traffic-bypass-profile-name-type', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'default_mpls_traffic_bypass_statistics', 'length': [u'3..64']}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MPLS profile name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='mpls-traffic-bypass-profile-name-type', is_config=True)


  def _get_interval(self):
    """
    Getter method for interval, mapped from YANG variable /telemetry/profile/mpls_traffic_bypass/interval (mpls-traffic-profile-interval-type)
    """
    return self.__interval
      
  def _set_interval(self, v, load=False):
    """
    Setter method for interval, mapped from YANG variable /telemetry/profile/mpls_traffic_bypass/interval (mpls-traffic-profile-interval-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interval() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'60..3600']}), is_leaf=True, yang_name="interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'MPLS profile interval'}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='mpls-traffic-profile-interval-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interval must be of a type compatible with mpls-traffic-profile-interval-type""",
          'defined-type': "brocade-telemetry:mpls-traffic-profile-interval-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'60..3600']}), is_leaf=True, yang_name="interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'MPLS profile interval'}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='mpls-traffic-profile-interval-type', is_config=True)""",
        })

    self.__interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interval(self):
    self.__interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'60..3600']}), is_leaf=True, yang_name="interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'MPLS profile interval'}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='mpls-traffic-profile-interval-type', is_config=True)


  def _get_mpls_traffic_bypasses(self):
    """
    Getter method for mpls_traffic_bypasses, mapped from YANG variable /telemetry/profile/mpls_traffic_bypass/mpls_traffic_bypasses (list)
    """
    return self.__mpls_traffic_bypasses
      
  def _set_mpls_traffic_bypasses(self, v, load=False):
    """
    Setter method for mpls_traffic_bypasses, mapped from YANG variable /telemetry/profile/mpls_traffic_bypass/mpls_traffic_bypasses (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_traffic_bypasses is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_traffic_bypasses() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("mpls_traffic_bypass_name",mpls_traffic_bypasses.mpls_traffic_bypasses, yang_name="mpls-traffic-bypasses", rest_name="bypass-lsp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mpls-traffic-bypass-name', extensions={u'tailf-common': {u'callpoint': u'Mplstrafficbypass', u'cli-suppress-mode': None, u'alt-name': u'bypass-lsp', u'info': u'MPLS Stats profile by Bypass LSP name', u'cli-suppress-list-no': None}}), is_container='list', yang_name="mpls-traffic-bypasses", rest_name="bypass-lsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'Mplstrafficbypass', u'cli-suppress-mode': None, u'alt-name': u'bypass-lsp', u'info': u'MPLS Stats profile by Bypass LSP name', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_traffic_bypasses must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("mpls_traffic_bypass_name",mpls_traffic_bypasses.mpls_traffic_bypasses, yang_name="mpls-traffic-bypasses", rest_name="bypass-lsp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mpls-traffic-bypass-name', extensions={u'tailf-common': {u'callpoint': u'Mplstrafficbypass', u'cli-suppress-mode': None, u'alt-name': u'bypass-lsp', u'info': u'MPLS Stats profile by Bypass LSP name', u'cli-suppress-list-no': None}}), is_container='list', yang_name="mpls-traffic-bypasses", rest_name="bypass-lsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'Mplstrafficbypass', u'cli-suppress-mode': None, u'alt-name': u'bypass-lsp', u'info': u'MPLS Stats profile by Bypass LSP name', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='list', is_config=True)""",
        })

    self.__mpls_traffic_bypasses = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_traffic_bypasses(self):
    self.__mpls_traffic_bypasses = YANGDynClass(base=YANGListType("mpls_traffic_bypass_name",mpls_traffic_bypasses.mpls_traffic_bypasses, yang_name="mpls-traffic-bypasses", rest_name="bypass-lsp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mpls-traffic-bypass-name', extensions={u'tailf-common': {u'callpoint': u'Mplstrafficbypass', u'cli-suppress-mode': None, u'alt-name': u'bypass-lsp', u'info': u'MPLS Stats profile by Bypass LSP name', u'cli-suppress-list-no': None}}), is_container='list', yang_name="mpls-traffic-bypasses", rest_name="bypass-lsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'Mplstrafficbypass', u'cli-suppress-mode': None, u'alt-name': u'bypass-lsp', u'info': u'MPLS Stats profile by Bypass LSP name', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='list', is_config=True)


  def _get_add_(self):
    """
    Getter method for add_, mapped from YANG variable /telemetry/profile/mpls_traffic_bypass/add (list)
    """
    return self.__add_
      
  def _set_add_(self, v, load=False):
    """
    Setter method for add_, mapped from YANG variable /telemetry/profile/mpls_traffic_bypass/add (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_add_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_add_() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("object",add_.add_, yang_name="add", rest_name="add", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='object', extensions={u'tailf-common': {u'callpoint': u'MplstrafficbypassProfileObject', u'cli-suppress-list-no': None, u'cli-suppress-mode': None, u'info': u'Add MPLS traffic telemetry object'}}), is_container='list', yang_name="add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'MplstrafficbypassProfileObject', u'cli-suppress-list-no': None, u'cli-suppress-mode': None, u'info': u'Add MPLS traffic telemetry object'}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """add_ must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("object",add_.add_, yang_name="add", rest_name="add", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='object', extensions={u'tailf-common': {u'callpoint': u'MplstrafficbypassProfileObject', u'cli-suppress-list-no': None, u'cli-suppress-mode': None, u'info': u'Add MPLS traffic telemetry object'}}), is_container='list', yang_name="add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'MplstrafficbypassProfileObject', u'cli-suppress-list-no': None, u'cli-suppress-mode': None, u'info': u'Add MPLS traffic telemetry object'}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='list', is_config=True)""",
        })

    self.__add_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_add_(self):
    self.__add_ = YANGDynClass(base=YANGListType("object",add_.add_, yang_name="add", rest_name="add", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='object', extensions={u'tailf-common': {u'callpoint': u'MplstrafficbypassProfileObject', u'cli-suppress-list-no': None, u'cli-suppress-mode': None, u'info': u'Add MPLS traffic telemetry object'}}), is_container='list', yang_name="add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'MplstrafficbypassProfileObject', u'cli-suppress-list-no': None, u'cli-suppress-mode': None, u'info': u'Add MPLS traffic telemetry object'}}, namespace='urn:brocade.com:mgmt:brocade-telemetry', defining_module='brocade-telemetry', yang_type='list', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  interval = __builtin__.property(_get_interval, _set_interval)
  mpls_traffic_bypasses = __builtin__.property(_get_mpls_traffic_bypasses, _set_mpls_traffic_bypasses)
  add_ = __builtin__.property(_get_add_, _set_add_)


  _pyangbind_elements = {'name': name, 'interval': interval, 'mpls_traffic_bypasses': mpls_traffic_bypasses, 'add_': add_, }


