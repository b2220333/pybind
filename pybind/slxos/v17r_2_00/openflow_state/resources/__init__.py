
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import group_resouces_list
import slot_resouces_list
class resources(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-openflow-operational - based on the path /openflow-state/resources. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Openflow Meter Resources
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__meter_max','__meter_used','__meter_free','__tcam_profile','__group_resouces_list','__slot_resouces_list',)

  _yang_name = 'resources'
  _rest_name = 'resources'

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
    self.__group_resouces_list = YANGDynClass(base=YANGListType("group_type",group_resouces_list.group_resouces_list, yang_name="group-resouces-list", rest_name="group-resouces-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='group-type', extensions={u'tailf-common': {u'callpoint': u'openflow-group-resources', u'cli-suppress-show-path': None}}), is_container='list', yang_name="group-resouces-list", rest_name="group-resouces-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-group-resources', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)
    self.__slot_resouces_list = YANGDynClass(base=YANGListType("slot_id",slot_resouces_list.slot_resouces_list, yang_name="slot-resouces-list", rest_name="slot-resouces-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='slot-id', extensions={u'tailf-common': {u'callpoint': u'openflow-slot-resources', u'cli-suppress-show-path': None}}), is_container='list', yang_name="slot-resouces-list", rest_name="slot-resouces-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-slot-resources', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)
    self.__meter_free = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="meter-free", rest_name="meter-free", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__meter_used = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="meter-used", rest_name="meter-used", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__meter_max = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="meter-max", rest_name="meter-max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__tcam_profile = YANGDynClass(base=unicode, is_leaf=True, yang_name="tcam-profile", rest_name="tcam-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)

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
      return [u'openflow-state', u'resources']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'openflow-state', u'resources']

  def _get_meter_max(self):
    """
    Getter method for meter_max, mapped from YANG variable /openflow_state/resources/meter_max (uint32)

    YANG Description: MAX
    """
    return self.__meter_max
      
  def _set_meter_max(self, v, load=False):
    """
    Setter method for meter_max, mapped from YANG variable /openflow_state/resources/meter_max (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_meter_max is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_meter_max() directly.

    YANG Description: MAX
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="meter-max", rest_name="meter-max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """meter_max must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="meter-max", rest_name="meter-max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__meter_max = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_meter_max(self):
    self.__meter_max = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="meter-max", rest_name="meter-max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_meter_used(self):
    """
    Getter method for meter_used, mapped from YANG variable /openflow_state/resources/meter_used (uint32)

    YANG Description: Used
    """
    return self.__meter_used
      
  def _set_meter_used(self, v, load=False):
    """
    Setter method for meter_used, mapped from YANG variable /openflow_state/resources/meter_used (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_meter_used is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_meter_used() directly.

    YANG Description: Used
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="meter-used", rest_name="meter-used", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """meter_used must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="meter-used", rest_name="meter-used", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__meter_used = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_meter_used(self):
    self.__meter_used = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="meter-used", rest_name="meter-used", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_meter_free(self):
    """
    Getter method for meter_free, mapped from YANG variable /openflow_state/resources/meter_free (uint32)

    YANG Description: Free
    """
    return self.__meter_free
      
  def _set_meter_free(self, v, load=False):
    """
    Setter method for meter_free, mapped from YANG variable /openflow_state/resources/meter_free (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_meter_free is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_meter_free() directly.

    YANG Description: Free
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="meter-free", rest_name="meter-free", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """meter_free must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="meter-free", rest_name="meter-free", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__meter_free = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_meter_free(self):
    self.__meter_free = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="meter-free", rest_name="meter-free", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_tcam_profile(self):
    """
    Getter method for tcam_profile, mapped from YANG variable /openflow_state/resources/tcam_profile (string)

    YANG Description: Tcam Profile
    """
    return self.__tcam_profile
      
  def _set_tcam_profile(self, v, load=False):
    """
    Setter method for tcam_profile, mapped from YANG variable /openflow_state/resources/tcam_profile (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tcam_profile is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tcam_profile() directly.

    YANG Description: Tcam Profile
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="tcam-profile", rest_name="tcam-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tcam_profile must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="tcam-profile", rest_name="tcam-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)""",
        })

    self.__tcam_profile = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tcam_profile(self):
    self.__tcam_profile = YANGDynClass(base=unicode, is_leaf=True, yang_name="tcam-profile", rest_name="tcam-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)


  def _get_group_resouces_list(self):
    """
    Getter method for group_resouces_list, mapped from YANG variable /openflow_state/resources/group_resouces_list (list)

    YANG Description: Group resources
    """
    return self.__group_resouces_list
      
  def _set_group_resouces_list(self, v, load=False):
    """
    Setter method for group_resouces_list, mapped from YANG variable /openflow_state/resources/group_resouces_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group_resouces_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group_resouces_list() directly.

    YANG Description: Group resources
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("group_type",group_resouces_list.group_resouces_list, yang_name="group-resouces-list", rest_name="group-resouces-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='group-type', extensions={u'tailf-common': {u'callpoint': u'openflow-group-resources', u'cli-suppress-show-path': None}}), is_container='list', yang_name="group-resouces-list", rest_name="group-resouces-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-group-resources', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group_resouces_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("group_type",group_resouces_list.group_resouces_list, yang_name="group-resouces-list", rest_name="group-resouces-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='group-type', extensions={u'tailf-common': {u'callpoint': u'openflow-group-resources', u'cli-suppress-show-path': None}}), is_container='list', yang_name="group-resouces-list", rest_name="group-resouces-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-group-resources', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)""",
        })

    self.__group_resouces_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group_resouces_list(self):
    self.__group_resouces_list = YANGDynClass(base=YANGListType("group_type",group_resouces_list.group_resouces_list, yang_name="group-resouces-list", rest_name="group-resouces-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='group-type', extensions={u'tailf-common': {u'callpoint': u'openflow-group-resources', u'cli-suppress-show-path': None}}), is_container='list', yang_name="group-resouces-list", rest_name="group-resouces-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-group-resources', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)


  def _get_slot_resouces_list(self):
    """
    Getter method for slot_resouces_list, mapped from YANG variable /openflow_state/resources/slot_resouces_list (list)

    YANG Description: Slot Resources
    """
    return self.__slot_resouces_list
      
  def _set_slot_resouces_list(self, v, load=False):
    """
    Setter method for slot_resouces_list, mapped from YANG variable /openflow_state/resources/slot_resouces_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_slot_resouces_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_slot_resouces_list() directly.

    YANG Description: Slot Resources
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("slot_id",slot_resouces_list.slot_resouces_list, yang_name="slot-resouces-list", rest_name="slot-resouces-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='slot-id', extensions={u'tailf-common': {u'callpoint': u'openflow-slot-resources', u'cli-suppress-show-path': None}}), is_container='list', yang_name="slot-resouces-list", rest_name="slot-resouces-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-slot-resources', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """slot_resouces_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("slot_id",slot_resouces_list.slot_resouces_list, yang_name="slot-resouces-list", rest_name="slot-resouces-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='slot-id', extensions={u'tailf-common': {u'callpoint': u'openflow-slot-resources', u'cli-suppress-show-path': None}}), is_container='list', yang_name="slot-resouces-list", rest_name="slot-resouces-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-slot-resources', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)""",
        })

    self.__slot_resouces_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_slot_resouces_list(self):
    self.__slot_resouces_list = YANGDynClass(base=YANGListType("slot_id",slot_resouces_list.slot_resouces_list, yang_name="slot-resouces-list", rest_name="slot-resouces-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='slot-id', extensions={u'tailf-common': {u'callpoint': u'openflow-slot-resources', u'cli-suppress-show-path': None}}), is_container='list', yang_name="slot-resouces-list", rest_name="slot-resouces-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-slot-resources', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)

  meter_max = __builtin__.property(_get_meter_max)
  meter_used = __builtin__.property(_get_meter_used)
  meter_free = __builtin__.property(_get_meter_free)
  tcam_profile = __builtin__.property(_get_tcam_profile)
  group_resouces_list = __builtin__.property(_get_group_resouces_list)
  slot_resouces_list = __builtin__.property(_get_slot_resouces_list)


  _pyangbind_elements = {'meter_max': meter_max, 'meter_used': meter_used, 'meter_free': meter_free, 'tcam_profile': tcam_profile, 'group_resouces_list': group_resouces_list, 'slot_resouces_list': slot_resouces_list, }


