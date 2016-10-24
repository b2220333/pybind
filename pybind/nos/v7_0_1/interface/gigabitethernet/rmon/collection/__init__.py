
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ether_stats_entry
import history_control_entry
class collection(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/gigabitethernet/rmon/collection. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ether_stats_entry','__history_control_entry',)

  _yang_name = 'collection'
  _rest_name = 'collection'

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
    self.__history_control_entry = YANGDynClass(base=YANGListType("history_control_index",history_control_entry.history_control_entry, yang_name="history-control-entry", rest_name="history", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='history-control-index', extensions={u'tailf-common': {u'info': u'RMON ether History statistics collection', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'history', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'rmon_history'}}), is_container='list', yang_name="history-control-entry", rest_name="history", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RMON ether History statistics collection', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'history', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'rmon_history'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='list', is_config=True)
    self.__ether_stats_entry = YANGDynClass(base=YANGListType("ether_stats_index",ether_stats_entry.ether_stats_entry, yang_name="ether-stats-entry", rest_name="stats", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ether-stats-index', extensions={u'tailf-common': {u'info': u'RMON ether statistics collection', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'stats', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'rmon_stats'}}), is_container='list', yang_name="ether-stats-entry", rest_name="stats", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RMON ether statistics collection', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'stats', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'rmon_stats'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='list', is_config=True)

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
      return [u'interface', u'gigabitethernet', u'rmon', u'collection']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'GigabitEthernet', u'rmon', u'collection']

  def _get_ether_stats_entry(self):
    """
    Getter method for ether_stats_entry, mapped from YANG variable /interface/gigabitethernet/rmon/collection/ether_stats_entry (list)
    """
    return self.__ether_stats_entry
      
  def _set_ether_stats_entry(self, v, load=False):
    """
    Setter method for ether_stats_entry, mapped from YANG variable /interface/gigabitethernet/rmon/collection/ether_stats_entry (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ether_stats_entry is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ether_stats_entry() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("ether_stats_index",ether_stats_entry.ether_stats_entry, yang_name="ether-stats-entry", rest_name="stats", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ether-stats-index', extensions={u'tailf-common': {u'info': u'RMON ether statistics collection', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'stats', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'rmon_stats'}}), is_container='list', yang_name="ether-stats-entry", rest_name="stats", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RMON ether statistics collection', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'stats', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'rmon_stats'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ether_stats_entry must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ether_stats_index",ether_stats_entry.ether_stats_entry, yang_name="ether-stats-entry", rest_name="stats", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ether-stats-index', extensions={u'tailf-common': {u'info': u'RMON ether statistics collection', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'stats', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'rmon_stats'}}), is_container='list', yang_name="ether-stats-entry", rest_name="stats", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RMON ether statistics collection', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'stats', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'rmon_stats'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='list', is_config=True)""",
        })

    self.__ether_stats_entry = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ether_stats_entry(self):
    self.__ether_stats_entry = YANGDynClass(base=YANGListType("ether_stats_index",ether_stats_entry.ether_stats_entry, yang_name="ether-stats-entry", rest_name="stats", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ether-stats-index', extensions={u'tailf-common': {u'info': u'RMON ether statistics collection', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'stats', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'rmon_stats'}}), is_container='list', yang_name="ether-stats-entry", rest_name="stats", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RMON ether statistics collection', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'stats', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'rmon_stats'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='list', is_config=True)


  def _get_history_control_entry(self):
    """
    Getter method for history_control_entry, mapped from YANG variable /interface/gigabitethernet/rmon/collection/history_control_entry (list)
    """
    return self.__history_control_entry
      
  def _set_history_control_entry(self, v, load=False):
    """
    Setter method for history_control_entry, mapped from YANG variable /interface/gigabitethernet/rmon/collection/history_control_entry (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_history_control_entry is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_history_control_entry() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("history_control_index",history_control_entry.history_control_entry, yang_name="history-control-entry", rest_name="history", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='history-control-index', extensions={u'tailf-common': {u'info': u'RMON ether History statistics collection', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'history', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'rmon_history'}}), is_container='list', yang_name="history-control-entry", rest_name="history", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RMON ether History statistics collection', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'history', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'rmon_history'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """history_control_entry must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("history_control_index",history_control_entry.history_control_entry, yang_name="history-control-entry", rest_name="history", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='history-control-index', extensions={u'tailf-common': {u'info': u'RMON ether History statistics collection', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'history', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'rmon_history'}}), is_container='list', yang_name="history-control-entry", rest_name="history", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RMON ether History statistics collection', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'history', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'rmon_history'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='list', is_config=True)""",
        })

    self.__history_control_entry = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_history_control_entry(self):
    self.__history_control_entry = YANGDynClass(base=YANGListType("history_control_index",history_control_entry.history_control_entry, yang_name="history-control-entry", rest_name="history", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='history-control-index', extensions={u'tailf-common': {u'info': u'RMON ether History statistics collection', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'history', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'rmon_history'}}), is_container='list', yang_name="history-control-entry", rest_name="history", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RMON ether History statistics collection', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'alt-name': u'history', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'rmon_history'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='list', is_config=True)

  ether_stats_entry = __builtin__.property(_get_ether_stats_entry, _set_ether_stats_entry)
  history_control_entry = __builtin__.property(_get_history_control_entry, _set_history_control_entry)


  _pyangbind_elements = {'ether_stats_entry': ether_stats_entry, 'history_control_entry': history_control_entry, }


