
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import pim_ecmp
class pim_ecmp_state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-pim-operational - based on the path /pim-ecmp-state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Pim Load Sharing
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__addr_filter','__pim_ecmp',)

  _yang_name = 'pim-ecmp-state'
  _rest_name = 'pim-ecmp-state'

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
    self.__addr_filter = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="addr-filter", rest_name="addr-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__pim_ecmp = YANGDynClass(base=YANGListType("src_ip rp_addr",pim_ecmp.pim_ecmp, yang_name="pim-ecmp", rest_name="pim-ecmp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='src-ip rp-addr', extensions={u'tailf-common': {u'callpoint': u'pim-pim-ecmp-instance', u'cli-suppress-show-path': None}}), is_container='list', yang_name="pim-ecmp", rest_name="pim-ecmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'pim-pim-ecmp-instance', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='list', is_config=False)

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
      return [u'pim-ecmp-state']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'pim-ecmp-state']

  def _get_addr_filter(self):
    """
    Getter method for addr_filter, mapped from YANG variable /pim_ecmp_state/addr_filter (inet:ipv4-address)

    YANG Description: RP Or SRC Ip Address
    """
    return self.__addr_filter
      
  def _set_addr_filter(self, v, load=False):
    """
    Setter method for addr_filter, mapped from YANG variable /pim_ecmp_state/addr_filter (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_addr_filter is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_addr_filter() directly.

    YANG Description: RP Or SRC Ip Address
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="addr-filter", rest_name="addr-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """addr_filter must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="addr-filter", rest_name="addr-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__addr_filter = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_addr_filter(self):
    self.__addr_filter = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="addr-filter", rest_name="addr-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_pim_ecmp(self):
    """
    Getter method for pim_ecmp, mapped from YANG variable /pim_ecmp_state/pim_ecmp (list)

    YANG Description: Pim Load Sharing
    """
    return self.__pim_ecmp
      
  def _set_pim_ecmp(self, v, load=False):
    """
    Setter method for pim_ecmp, mapped from YANG variable /pim_ecmp_state/pim_ecmp (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pim_ecmp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pim_ecmp() directly.

    YANG Description: Pim Load Sharing
    """
    try:
      t = YANGDynClass(v,base=YANGListType("src_ip rp_addr",pim_ecmp.pim_ecmp, yang_name="pim-ecmp", rest_name="pim-ecmp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='src-ip rp-addr', extensions={u'tailf-common': {u'callpoint': u'pim-pim-ecmp-instance', u'cli-suppress-show-path': None}}), is_container='list', yang_name="pim-ecmp", rest_name="pim-ecmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'pim-pim-ecmp-instance', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pim_ecmp must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("src_ip rp_addr",pim_ecmp.pim_ecmp, yang_name="pim-ecmp", rest_name="pim-ecmp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='src-ip rp-addr', extensions={u'tailf-common': {u'callpoint': u'pim-pim-ecmp-instance', u'cli-suppress-show-path': None}}), is_container='list', yang_name="pim-ecmp", rest_name="pim-ecmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'pim-pim-ecmp-instance', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='list', is_config=False)""",
        })

    self.__pim_ecmp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pim_ecmp(self):
    self.__pim_ecmp = YANGDynClass(base=YANGListType("src_ip rp_addr",pim_ecmp.pim_ecmp, yang_name="pim-ecmp", rest_name="pim-ecmp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='src-ip rp-addr', extensions={u'tailf-common': {u'callpoint': u'pim-pim-ecmp-instance', u'cli-suppress-show-path': None}}), is_container='list', yang_name="pim-ecmp", rest_name="pim-ecmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'pim-pim-ecmp-instance', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='list', is_config=False)

  addr_filter = __builtin__.property(_get_addr_filter)
  pim_ecmp = __builtin__.property(_get_pim_ecmp)


  _pyangbind_elements = {'addr_filter': addr_filter, 'pim_ecmp': pim_ecmp, }

