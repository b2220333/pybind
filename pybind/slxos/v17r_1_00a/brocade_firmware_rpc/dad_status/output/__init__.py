
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import dad_status_entries
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-firmware - based on the path /brocade_firmware_rpc/dad-status/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__dad_last_state','__dad_status_entries',)

  _yang_name = 'output'
  _rest_name = 'output'

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
    self.__dad_last_state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dad-in-progress': {'value': 0}, u'dad-failed': {'value': 1}, u'dad-completed': {'value': 2}},), is_leaf=True, yang_name="dad-last-state", rest_name="dad-last-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'DHCP auto-deployment state'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='enumeration', is_config=True)
    self.__dad_status_entries = YANGDynClass(base=YANGListType(False,dad_status_entries.dad_status_entries, yang_name="dad-status-entries", rest_name="dad-status-entries", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="dad-status-entries", rest_name="dad-status-entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='list', is_config=True)

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
      return [u'brocade_firmware_rpc', u'dad-status', u'output']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'dad-status', u'output']

  def _get_dad_last_state(self):
    """
    Getter method for dad_last_state, mapped from YANG variable /brocade_firmware_rpc/dad_status/output/dad_last_state (enumeration)
    """
    return self.__dad_last_state
      
  def _set_dad_last_state(self, v, load=False):
    """
    Setter method for dad_last_state, mapped from YANG variable /brocade_firmware_rpc/dad_status/output/dad_last_state (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dad_last_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dad_last_state() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dad-in-progress': {'value': 0}, u'dad-failed': {'value': 1}, u'dad-completed': {'value': 2}},), is_leaf=True, yang_name="dad-last-state", rest_name="dad-last-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'DHCP auto-deployment state'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dad_last_state must be of a type compatible with enumeration""",
          'defined-type': "brocade-firmware:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dad-in-progress': {'value': 0}, u'dad-failed': {'value': 1}, u'dad-completed': {'value': 2}},), is_leaf=True, yang_name="dad-last-state", rest_name="dad-last-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'DHCP auto-deployment state'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='enumeration', is_config=True)""",
        })

    self.__dad_last_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dad_last_state(self):
    self.__dad_last_state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dad-in-progress': {'value': 0}, u'dad-failed': {'value': 1}, u'dad-completed': {'value': 2}},), is_leaf=True, yang_name="dad-last-state", rest_name="dad-last-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'DHCP auto-deployment state'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='enumeration', is_config=True)


  def _get_dad_status_entries(self):
    """
    Getter method for dad_status_entries, mapped from YANG variable /brocade_firmware_rpc/dad_status/output/dad_status_entries (list)
    """
    return self.__dad_status_entries
      
  def _set_dad_status_entries(self, v, load=False):
    """
    Setter method for dad_status_entries, mapped from YANG variable /brocade_firmware_rpc/dad_status/output/dad_status_entries (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dad_status_entries is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dad_status_entries() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType(False,dad_status_entries.dad_status_entries, yang_name="dad-status-entries", rest_name="dad-status-entries", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="dad-status-entries", rest_name="dad-status-entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dad_status_entries must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType(False,dad_status_entries.dad_status_entries, yang_name="dad-status-entries", rest_name="dad-status-entries", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="dad-status-entries", rest_name="dad-status-entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='list', is_config=True)""",
        })

    self.__dad_status_entries = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dad_status_entries(self):
    self.__dad_status_entries = YANGDynClass(base=YANGListType(False,dad_status_entries.dad_status_entries, yang_name="dad-status-entries", rest_name="dad-status-entries", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="dad-status-entries", rest_name="dad-status-entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='list', is_config=True)

  dad_last_state = __builtin__.property(_get_dad_last_state, _set_dad_last_state)
  dad_status_entries = __builtin__.property(_get_dad_status_entries, _set_dad_status_entries)


  _pyangbind_elements = {'dad_last_state': dad_last_state, 'dad_status_entries': dad_status_entries, }

