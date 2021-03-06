
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class consistency_check(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mac-address-table - based on the path /mac-address-table/consistency-check. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: MAC Consistency check
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mac_consistency_check_suppress','__mac_consistency_check_interval',)

  _yang_name = 'consistency-check'
  _rest_name = 'consistency-check'

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
    self.__mac_consistency_check_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'120..3600']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(300), is_leaf=True, yang_name="mac-consistency-check-interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MAC Consistency check interval in seconds (default = 300)', u'cli-full-command': None, u'alt-name': u'interval'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='uint32', is_config=True)
    self.__mac_consistency_check_suppress = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mac-consistency-check-suppress", rest_name="suppress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Suppress MAC Consistency check', u'cli-full-command': None, u'alt-name': u'suppress'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='empty', is_config=True)

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
      return [u'mac-address-table', u'consistency-check']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mac-address-table', u'consistency-check']

  def _get_mac_consistency_check_suppress(self):
    """
    Getter method for mac_consistency_check_suppress, mapped from YANG variable /mac_address_table/consistency_check/mac_consistency_check_suppress (empty)

    YANG Description: Suppress MAC Consistency check
    """
    return self.__mac_consistency_check_suppress
      
  def _set_mac_consistency_check_suppress(self, v, load=False):
    """
    Setter method for mac_consistency_check_suppress, mapped from YANG variable /mac_address_table/consistency_check/mac_consistency_check_suppress (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_consistency_check_suppress is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_consistency_check_suppress() directly.

    YANG Description: Suppress MAC Consistency check
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="mac-consistency-check-suppress", rest_name="suppress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Suppress MAC Consistency check', u'cli-full-command': None, u'alt-name': u'suppress'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_consistency_check_suppress must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mac-consistency-check-suppress", rest_name="suppress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Suppress MAC Consistency check', u'cli-full-command': None, u'alt-name': u'suppress'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='empty', is_config=True)""",
        })

    self.__mac_consistency_check_suppress = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_consistency_check_suppress(self):
    self.__mac_consistency_check_suppress = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mac-consistency-check-suppress", rest_name="suppress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Suppress MAC Consistency check', u'cli-full-command': None, u'alt-name': u'suppress'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='empty', is_config=True)


  def _get_mac_consistency_check_interval(self):
    """
    Getter method for mac_consistency_check_interval, mapped from YANG variable /mac_address_table/consistency_check/mac_consistency_check_interval (uint32)

    YANG Description: MAC Consistency check interval in seconds (default = 300)
    """
    return self.__mac_consistency_check_interval
      
  def _set_mac_consistency_check_interval(self, v, load=False):
    """
    Setter method for mac_consistency_check_interval, mapped from YANG variable /mac_address_table/consistency_check/mac_consistency_check_interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_consistency_check_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_consistency_check_interval() directly.

    YANG Description: MAC Consistency check interval in seconds (default = 300)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'120..3600']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(300), is_leaf=True, yang_name="mac-consistency-check-interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MAC Consistency check interval in seconds (default = 300)', u'cli-full-command': None, u'alt-name': u'interval'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_consistency_check_interval must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'120..3600']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(300), is_leaf=True, yang_name="mac-consistency-check-interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MAC Consistency check interval in seconds (default = 300)', u'cli-full-command': None, u'alt-name': u'interval'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='uint32', is_config=True)""",
        })

    self.__mac_consistency_check_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_consistency_check_interval(self):
    self.__mac_consistency_check_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'120..3600']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(300), is_leaf=True, yang_name="mac-consistency-check-interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MAC Consistency check interval in seconds (default = 300)', u'cli-full-command': None, u'alt-name': u'interval'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='uint32', is_config=True)

  mac_consistency_check_suppress = __builtin__.property(_get_mac_consistency_check_suppress, _set_mac_consistency_check_suppress)
  mac_consistency_check_interval = __builtin__.property(_get_mac_consistency_check_interval, _set_mac_consistency_check_interval)


  _pyangbind_elements = {'mac_consistency_check_suppress': mac_consistency_check_suppress, 'mac_consistency_check_interval': mac_consistency_check_interval, }


