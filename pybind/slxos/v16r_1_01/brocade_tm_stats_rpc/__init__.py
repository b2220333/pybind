
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import clear_tm_voq_stat_ing_all_egr_all
import clear_tm_voq_stat_ing_all_egr_ifname
import clear_tm_voq_stat_slot_id_egr_all
import clear_tm_voq_slot_id_egress_port_name
class brocade_tm_stats(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-tm-stats - based on the path /brocade_tm_stats_rpc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This module manages Traffic Manager stats
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__clear_tm_voq_stat_ing_all_egr_all','__clear_tm_voq_stat_ing_all_egr_ifname','__clear_tm_voq_stat_slot_id_egr_all','__clear_tm_voq_slot_id_egress_port_name',)

  _yang_name = 'brocade-tm-stats'
  _rest_name = ''

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
    self.__clear_tm_voq_slot_id_egress_port_name = YANGDynClass(base=clear_tm_voq_slot_id_egress_port_name.clear_tm_voq_slot_id_egress_port_name, is_leaf=True, yang_name="clear-tm-voq-slot-id-egress-port-name", rest_name="clear-tm-voq-slot-id-egress-port-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'tmCpuVoqClearGrp'}}, namespace='urn:brocade.com:mgmt:brocade-tm-stats', defining_module='brocade-tm-stats', yang_type='rpc', is_config=True)
    self.__clear_tm_voq_stat_ing_all_egr_all = YANGDynClass(base=clear_tm_voq_stat_ing_all_egr_all.clear_tm_voq_stat_ing_all_egr_all, is_leaf=True, yang_name="clear-tm-voq-stat-ing-all-egr-all", rest_name="clear-tm-voq-stat-ing-all-egr-all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'tmVoqClearIntf'}}, namespace='urn:brocade.com:mgmt:brocade-tm-stats', defining_module='brocade-tm-stats', yang_type='rpc', is_config=True)
    self.__clear_tm_voq_stat_slot_id_egr_all = YANGDynClass(base=clear_tm_voq_stat_slot_id_egr_all.clear_tm_voq_stat_slot_id_egr_all, is_leaf=True, yang_name="clear-tm-voq-stat-slot-id-egr-all", rest_name="clear-tm-voq-stat-slot-id-egr-all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'tmCpuVoqClearGrp'}}, namespace='urn:brocade.com:mgmt:brocade-tm-stats', defining_module='brocade-tm-stats', yang_type='rpc', is_config=True)
    self.__clear_tm_voq_stat_ing_all_egr_ifname = YANGDynClass(base=clear_tm_voq_stat_ing_all_egr_ifname.clear_tm_voq_stat_ing_all_egr_ifname, is_leaf=True, yang_name="clear-tm-voq-stat-ing-all-egr-ifname", rest_name="clear-tm-voq-stat-ing-all-egr-ifname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'tmVoqClearIntf'}}, namespace='urn:brocade.com:mgmt:brocade-tm-stats', defining_module='brocade-tm-stats', yang_type='rpc', is_config=True)

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
      return [u'brocade_tm_stats_rpc']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return []

  def _get_clear_tm_voq_stat_ing_all_egr_all(self):
    """
    Getter method for clear_tm_voq_stat_ing_all_egr_all, mapped from YANG variable /brocade_tm_stats_rpc/clear_tm_voq_stat_ing_all_egr_all (rpc)
    """
    return self.__clear_tm_voq_stat_ing_all_egr_all
      
  def _set_clear_tm_voq_stat_ing_all_egr_all(self, v, load=False):
    """
    Setter method for clear_tm_voq_stat_ing_all_egr_all, mapped from YANG variable /brocade_tm_stats_rpc/clear_tm_voq_stat_ing_all_egr_all (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_clear_tm_voq_stat_ing_all_egr_all is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_clear_tm_voq_stat_ing_all_egr_all() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=clear_tm_voq_stat_ing_all_egr_all.clear_tm_voq_stat_ing_all_egr_all, is_leaf=True, yang_name="clear-tm-voq-stat-ing-all-egr-all", rest_name="clear-tm-voq-stat-ing-all-egr-all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'tmVoqClearIntf'}}, namespace='urn:brocade.com:mgmt:brocade-tm-stats', defining_module='brocade-tm-stats', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """clear_tm_voq_stat_ing_all_egr_all must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=clear_tm_voq_stat_ing_all_egr_all.clear_tm_voq_stat_ing_all_egr_all, is_leaf=True, yang_name="clear-tm-voq-stat-ing-all-egr-all", rest_name="clear-tm-voq-stat-ing-all-egr-all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'tmVoqClearIntf'}}, namespace='urn:brocade.com:mgmt:brocade-tm-stats', defining_module='brocade-tm-stats', yang_type='rpc', is_config=True)""",
        })

    self.__clear_tm_voq_stat_ing_all_egr_all = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_clear_tm_voq_stat_ing_all_egr_all(self):
    self.__clear_tm_voq_stat_ing_all_egr_all = YANGDynClass(base=clear_tm_voq_stat_ing_all_egr_all.clear_tm_voq_stat_ing_all_egr_all, is_leaf=True, yang_name="clear-tm-voq-stat-ing-all-egr-all", rest_name="clear-tm-voq-stat-ing-all-egr-all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'tmVoqClearIntf'}}, namespace='urn:brocade.com:mgmt:brocade-tm-stats', defining_module='brocade-tm-stats', yang_type='rpc', is_config=True)


  def _get_clear_tm_voq_stat_ing_all_egr_ifname(self):
    """
    Getter method for clear_tm_voq_stat_ing_all_egr_ifname, mapped from YANG variable /brocade_tm_stats_rpc/clear_tm_voq_stat_ing_all_egr_ifname (rpc)
    """
    return self.__clear_tm_voq_stat_ing_all_egr_ifname
      
  def _set_clear_tm_voq_stat_ing_all_egr_ifname(self, v, load=False):
    """
    Setter method for clear_tm_voq_stat_ing_all_egr_ifname, mapped from YANG variable /brocade_tm_stats_rpc/clear_tm_voq_stat_ing_all_egr_ifname (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_clear_tm_voq_stat_ing_all_egr_ifname is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_clear_tm_voq_stat_ing_all_egr_ifname() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=clear_tm_voq_stat_ing_all_egr_ifname.clear_tm_voq_stat_ing_all_egr_ifname, is_leaf=True, yang_name="clear-tm-voq-stat-ing-all-egr-ifname", rest_name="clear-tm-voq-stat-ing-all-egr-ifname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'tmVoqClearIntf'}}, namespace='urn:brocade.com:mgmt:brocade-tm-stats', defining_module='brocade-tm-stats', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """clear_tm_voq_stat_ing_all_egr_ifname must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=clear_tm_voq_stat_ing_all_egr_ifname.clear_tm_voq_stat_ing_all_egr_ifname, is_leaf=True, yang_name="clear-tm-voq-stat-ing-all-egr-ifname", rest_name="clear-tm-voq-stat-ing-all-egr-ifname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'tmVoqClearIntf'}}, namespace='urn:brocade.com:mgmt:brocade-tm-stats', defining_module='brocade-tm-stats', yang_type='rpc', is_config=True)""",
        })

    self.__clear_tm_voq_stat_ing_all_egr_ifname = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_clear_tm_voq_stat_ing_all_egr_ifname(self):
    self.__clear_tm_voq_stat_ing_all_egr_ifname = YANGDynClass(base=clear_tm_voq_stat_ing_all_egr_ifname.clear_tm_voq_stat_ing_all_egr_ifname, is_leaf=True, yang_name="clear-tm-voq-stat-ing-all-egr-ifname", rest_name="clear-tm-voq-stat-ing-all-egr-ifname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'tmVoqClearIntf'}}, namespace='urn:brocade.com:mgmt:brocade-tm-stats', defining_module='brocade-tm-stats', yang_type='rpc', is_config=True)


  def _get_clear_tm_voq_stat_slot_id_egr_all(self):
    """
    Getter method for clear_tm_voq_stat_slot_id_egr_all, mapped from YANG variable /brocade_tm_stats_rpc/clear_tm_voq_stat_slot_id_egr_all (rpc)
    """
    return self.__clear_tm_voq_stat_slot_id_egr_all
      
  def _set_clear_tm_voq_stat_slot_id_egr_all(self, v, load=False):
    """
    Setter method for clear_tm_voq_stat_slot_id_egr_all, mapped from YANG variable /brocade_tm_stats_rpc/clear_tm_voq_stat_slot_id_egr_all (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_clear_tm_voq_stat_slot_id_egr_all is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_clear_tm_voq_stat_slot_id_egr_all() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=clear_tm_voq_stat_slot_id_egr_all.clear_tm_voq_stat_slot_id_egr_all, is_leaf=True, yang_name="clear-tm-voq-stat-slot-id-egr-all", rest_name="clear-tm-voq-stat-slot-id-egr-all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'tmCpuVoqClearGrp'}}, namespace='urn:brocade.com:mgmt:brocade-tm-stats', defining_module='brocade-tm-stats', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """clear_tm_voq_stat_slot_id_egr_all must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=clear_tm_voq_stat_slot_id_egr_all.clear_tm_voq_stat_slot_id_egr_all, is_leaf=True, yang_name="clear-tm-voq-stat-slot-id-egr-all", rest_name="clear-tm-voq-stat-slot-id-egr-all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'tmCpuVoqClearGrp'}}, namespace='urn:brocade.com:mgmt:brocade-tm-stats', defining_module='brocade-tm-stats', yang_type='rpc', is_config=True)""",
        })

    self.__clear_tm_voq_stat_slot_id_egr_all = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_clear_tm_voq_stat_slot_id_egr_all(self):
    self.__clear_tm_voq_stat_slot_id_egr_all = YANGDynClass(base=clear_tm_voq_stat_slot_id_egr_all.clear_tm_voq_stat_slot_id_egr_all, is_leaf=True, yang_name="clear-tm-voq-stat-slot-id-egr-all", rest_name="clear-tm-voq-stat-slot-id-egr-all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'tmCpuVoqClearGrp'}}, namespace='urn:brocade.com:mgmt:brocade-tm-stats', defining_module='brocade-tm-stats', yang_type='rpc', is_config=True)


  def _get_clear_tm_voq_slot_id_egress_port_name(self):
    """
    Getter method for clear_tm_voq_slot_id_egress_port_name, mapped from YANG variable /brocade_tm_stats_rpc/clear_tm_voq_slot_id_egress_port_name (rpc)
    """
    return self.__clear_tm_voq_slot_id_egress_port_name
      
  def _set_clear_tm_voq_slot_id_egress_port_name(self, v, load=False):
    """
    Setter method for clear_tm_voq_slot_id_egress_port_name, mapped from YANG variable /brocade_tm_stats_rpc/clear_tm_voq_slot_id_egress_port_name (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_clear_tm_voq_slot_id_egress_port_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_clear_tm_voq_slot_id_egress_port_name() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=clear_tm_voq_slot_id_egress_port_name.clear_tm_voq_slot_id_egress_port_name, is_leaf=True, yang_name="clear-tm-voq-slot-id-egress-port-name", rest_name="clear-tm-voq-slot-id-egress-port-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'tmCpuVoqClearGrp'}}, namespace='urn:brocade.com:mgmt:brocade-tm-stats', defining_module='brocade-tm-stats', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """clear_tm_voq_slot_id_egress_port_name must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=clear_tm_voq_slot_id_egress_port_name.clear_tm_voq_slot_id_egress_port_name, is_leaf=True, yang_name="clear-tm-voq-slot-id-egress-port-name", rest_name="clear-tm-voq-slot-id-egress-port-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'tmCpuVoqClearGrp'}}, namespace='urn:brocade.com:mgmt:brocade-tm-stats', defining_module='brocade-tm-stats', yang_type='rpc', is_config=True)""",
        })

    self.__clear_tm_voq_slot_id_egress_port_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_clear_tm_voq_slot_id_egress_port_name(self):
    self.__clear_tm_voq_slot_id_egress_port_name = YANGDynClass(base=clear_tm_voq_slot_id_egress_port_name.clear_tm_voq_slot_id_egress_port_name, is_leaf=True, yang_name="clear-tm-voq-slot-id-egress-port-name", rest_name="clear-tm-voq-slot-id-egress-port-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'tmCpuVoqClearGrp'}}, namespace='urn:brocade.com:mgmt:brocade-tm-stats', defining_module='brocade-tm-stats', yang_type='rpc', is_config=True)

  clear_tm_voq_stat_ing_all_egr_all = __builtin__.property(_get_clear_tm_voq_stat_ing_all_egr_all, _set_clear_tm_voq_stat_ing_all_egr_all)
  clear_tm_voq_stat_ing_all_egr_ifname = __builtin__.property(_get_clear_tm_voq_stat_ing_all_egr_ifname, _set_clear_tm_voq_stat_ing_all_egr_ifname)
  clear_tm_voq_stat_slot_id_egr_all = __builtin__.property(_get_clear_tm_voq_stat_slot_id_egr_all, _set_clear_tm_voq_stat_slot_id_egr_all)
  clear_tm_voq_slot_id_egress_port_name = __builtin__.property(_get_clear_tm_voq_slot_id_egress_port_name, _set_clear_tm_voq_slot_id_egress_port_name)


  _pyangbind_elements = {'clear_tm_voq_stat_ing_all_egr_all': clear_tm_voq_stat_ing_all_egr_all, 'clear_tm_voq_stat_ing_all_egr_ifname': clear_tm_voq_stat_ing_all_egr_ifname, 'clear_tm_voq_stat_slot_id_egr_all': clear_tm_voq_stat_slot_id_egr_all, 'clear_tm_voq_slot_id_egress_port_name': clear_tm_voq_slot_id_egress_port_name, }


