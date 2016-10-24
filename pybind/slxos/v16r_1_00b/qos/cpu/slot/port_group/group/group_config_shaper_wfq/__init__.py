
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import group_shaper
import group_wfq
import group_prio
class group_config_shaper_wfq(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-mls - based on the path /qos/cpu/slot/port-group/group/group-config-shaper-wfq. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__group_shaper','__group_wfq','__group_prio',)

  _yang_name = 'group-config-shaper-wfq'
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
    self.__group_prio = YANGDynClass(base=YANGListType("group_prio_id",group_prio.group_prio, yang_name="group-prio", rest_name="prio", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='group-prio-id', extensions={u'tailf-common': {u'info': u'Configure CPU group priority parameters', u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'callpoint': u'QosCpuPrioConfig', u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'alt-name': u'prio'}}), is_container='list', yang_name="group-prio", rest_name="prio", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CPU group priority parameters', u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'callpoint': u'QosCpuPrioConfig', u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'alt-name': u'prio'}}, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='list', is_config=True)
    self.__group_wfq = YANGDynClass(base=group_wfq.group_wfq, is_container='container', yang_name="group-wfq", rest_name="wfq", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CPU group wfq', u'alt-name': u'wfq', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='container', is_config=True)
    self.__group_shaper = YANGDynClass(base=group_shaper.group_shaper, is_container='container', yang_name="group-shaper", rest_name="shaper", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CPU group shaper', u'cli-sequence-commands': None, u'alt-name': u'shaper', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='container', is_config=True)

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
      return [u'qos', u'cpu', u'slot', u'port-group', u'group', u'group-config-shaper-wfq']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'qos', u'cpu', u'slot', u'group']

  def _get_group_shaper(self):
    """
    Getter method for group_shaper, mapped from YANG variable /qos/cpu/slot/port_group/group/group_config_shaper_wfq/group_shaper (container)
    """
    return self.__group_shaper
      
  def _set_group_shaper(self, v, load=False):
    """
    Setter method for group_shaper, mapped from YANG variable /qos/cpu/slot/port_group/group/group_config_shaper_wfq/group_shaper (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group_shaper is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group_shaper() directly.
    """
    try:
      t = YANGDynClass(v,base=group_shaper.group_shaper, is_container='container', yang_name="group-shaper", rest_name="shaper", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CPU group shaper', u'cli-sequence-commands': None, u'alt-name': u'shaper', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group_shaper must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=group_shaper.group_shaper, is_container='container', yang_name="group-shaper", rest_name="shaper", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CPU group shaper', u'cli-sequence-commands': None, u'alt-name': u'shaper', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='container', is_config=True)""",
        })

    self.__group_shaper = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group_shaper(self):
    self.__group_shaper = YANGDynClass(base=group_shaper.group_shaper, is_container='container', yang_name="group-shaper", rest_name="shaper", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CPU group shaper', u'cli-sequence-commands': None, u'alt-name': u'shaper', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='container', is_config=True)


  def _get_group_wfq(self):
    """
    Getter method for group_wfq, mapped from YANG variable /qos/cpu/slot/port_group/group/group_config_shaper_wfq/group_wfq (container)
    """
    return self.__group_wfq
      
  def _set_group_wfq(self, v, load=False):
    """
    Setter method for group_wfq, mapped from YANG variable /qos/cpu/slot/port_group/group/group_config_shaper_wfq/group_wfq (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group_wfq is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group_wfq() directly.
    """
    try:
      t = YANGDynClass(v,base=group_wfq.group_wfq, is_container='container', yang_name="group-wfq", rest_name="wfq", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CPU group wfq', u'alt-name': u'wfq', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group_wfq must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=group_wfq.group_wfq, is_container='container', yang_name="group-wfq", rest_name="wfq", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CPU group wfq', u'alt-name': u'wfq', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='container', is_config=True)""",
        })

    self.__group_wfq = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group_wfq(self):
    self.__group_wfq = YANGDynClass(base=group_wfq.group_wfq, is_container='container', yang_name="group-wfq", rest_name="wfq", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CPU group wfq', u'alt-name': u'wfq', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='container', is_config=True)


  def _get_group_prio(self):
    """
    Getter method for group_prio, mapped from YANG variable /qos/cpu/slot/port_group/group/group_config_shaper_wfq/group_prio (list)
    """
    return self.__group_prio
      
  def _set_group_prio(self, v, load=False):
    """
    Setter method for group_prio, mapped from YANG variable /qos/cpu/slot/port_group/group/group_config_shaper_wfq/group_prio (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group_prio is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group_prio() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("group_prio_id",group_prio.group_prio, yang_name="group-prio", rest_name="prio", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='group-prio-id', extensions={u'tailf-common': {u'info': u'Configure CPU group priority parameters', u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'callpoint': u'QosCpuPrioConfig', u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'alt-name': u'prio'}}), is_container='list', yang_name="group-prio", rest_name="prio", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CPU group priority parameters', u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'callpoint': u'QosCpuPrioConfig', u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'alt-name': u'prio'}}, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group_prio must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("group_prio_id",group_prio.group_prio, yang_name="group-prio", rest_name="prio", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='group-prio-id', extensions={u'tailf-common': {u'info': u'Configure CPU group priority parameters', u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'callpoint': u'QosCpuPrioConfig', u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'alt-name': u'prio'}}), is_container='list', yang_name="group-prio", rest_name="prio", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CPU group priority parameters', u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'callpoint': u'QosCpuPrioConfig', u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'alt-name': u'prio'}}, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='list', is_config=True)""",
        })

    self.__group_prio = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group_prio(self):
    self.__group_prio = YANGDynClass(base=YANGListType("group_prio_id",group_prio.group_prio, yang_name="group-prio", rest_name="prio", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='group-prio-id', extensions={u'tailf-common': {u'info': u'Configure CPU group priority parameters', u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'callpoint': u'QosCpuPrioConfig', u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'alt-name': u'prio'}}), is_container='list', yang_name="group-prio", rest_name="prio", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CPU group priority parameters', u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'callpoint': u'QosCpuPrioConfig', u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'alt-name': u'prio'}}, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='list', is_config=True)

  group_shaper = __builtin__.property(_get_group_shaper, _set_group_shaper)
  group_wfq = __builtin__.property(_get_group_wfq, _set_group_wfq)
  group_prio = __builtin__.property(_get_group_prio, _set_group_prio)


  _pyangbind_elements = {'group_shaper': group_shaper, 'group_wfq': group_wfq, 'group_prio': group_prio, }


