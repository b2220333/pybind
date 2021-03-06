
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import bd_label_info
class show_cluster_mem_bd(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-l2sys-operational - based on the path /mct-l2ys-state/show-cluster-mem-bd. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Cluster BD Labels
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__num_bds','__bd_label_info',)

  _yang_name = 'show-cluster-mem-bd'
  _rest_name = 'show-cluster-mem-bd'

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
    self.__bd_label_info = YANGDynClass(base=YANGListType("bd_id",bd_label_info.bd_label_info, yang_name="bd-label-info", rest_name="bd-label-info", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bd-id', extensions={u'tailf-common': {u'callpoint': u'l2sys-bd-label-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="bd-label-info", rest_name="bd-label-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'l2sys-bd-label-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='list', is_config=False)
    self.__num_bds = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-bds", rest_name="num-bds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='uint32', is_config=False)

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
      return [u'mct-l2ys-state', u'show-cluster-mem-bd']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mct-l2ys-state', u'show-cluster-mem-bd']

  def _get_num_bds(self):
    """
    Getter method for num_bds, mapped from YANG variable /mct_l2ys_state/show_cluster_mem_bd/num_bds (uint32)

    YANG Description: No. of BDs configured
    """
    return self.__num_bds
      
  def _set_num_bds(self, v, load=False):
    """
    Setter method for num_bds, mapped from YANG variable /mct_l2ys_state/show_cluster_mem_bd/num_bds (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_num_bds is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_num_bds() directly.

    YANG Description: No. of BDs configured
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-bds", rest_name="num-bds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """num_bds must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-bds", rest_name="num-bds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='uint32', is_config=False)""",
        })

    self.__num_bds = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_num_bds(self):
    self.__num_bds = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-bds", rest_name="num-bds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='uint32', is_config=False)


  def _get_bd_label_info(self):
    """
    Getter method for bd_label_info, mapped from YANG variable /mct_l2ys_state/show_cluster_mem_bd/bd_label_info (list)

    YANG Description: BD Label Info
    """
    return self.__bd_label_info
      
  def _set_bd_label_info(self, v, load=False):
    """
    Setter method for bd_label_info, mapped from YANG variable /mct_l2ys_state/show_cluster_mem_bd/bd_label_info (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bd_label_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bd_label_info() directly.

    YANG Description: BD Label Info
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("bd_id",bd_label_info.bd_label_info, yang_name="bd-label-info", rest_name="bd-label-info", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bd-id', extensions={u'tailf-common': {u'callpoint': u'l2sys-bd-label-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="bd-label-info", rest_name="bd-label-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'l2sys-bd-label-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bd_label_info must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("bd_id",bd_label_info.bd_label_info, yang_name="bd-label-info", rest_name="bd-label-info", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bd-id', extensions={u'tailf-common': {u'callpoint': u'l2sys-bd-label-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="bd-label-info", rest_name="bd-label-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'l2sys-bd-label-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='list', is_config=False)""",
        })

    self.__bd_label_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bd_label_info(self):
    self.__bd_label_info = YANGDynClass(base=YANGListType("bd_id",bd_label_info.bd_label_info, yang_name="bd-label-info", rest_name="bd-label-info", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bd-id', extensions={u'tailf-common': {u'callpoint': u'l2sys-bd-label-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="bd-label-info", rest_name="bd-label-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'l2sys-bd-label-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-l2sys-operational', defining_module='brocade-l2sys-operational', yang_type='list', is_config=False)

  num_bds = __builtin__.property(_get_num_bds)
  bd_label_info = __builtin__.property(_get_bd_label_info)


  _pyangbind_elements = {'num_bds': num_bds, 'bd_label_info': bd_label_info, }


