
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import pim_interface_data
class interfaces(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-pim-operational - based on the path /pim-global-state/interfaces. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: PIM enabled interfaces
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vrf_name','__pim_interface_data',)

  _yang_name = 'interfaces'
  _rest_name = 'interfaces'

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
    self.__pim_interface_data = YANGDynClass(base=YANGListType("vrf_name interface_name interface_type",pim_interface_data.pim_interface_data, yang_name="pim-interface-data", rest_name="pim-interface-data", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vrf-name interface-name interface-type', extensions={u'tailf-common': {u'callpoint': u'pim-pim-interface-data', u'cli-suppress-show-path': None}}), is_container='list', yang_name="pim-interface-data", rest_name="pim-interface-data", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'pim-pim-interface-data', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='list', is_config=False)
    self.__vrf_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf-name", rest_name="vrf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)

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
      return [u'pim-global-state', u'interfaces']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'pim-global-state', u'interfaces']

  def _get_vrf_name(self):
    """
    Getter method for vrf_name, mapped from YANG variable /pim_global_state/interfaces/vrf_name (string)

    YANG Description: vrf name
    """
    return self.__vrf_name
      
  def _set_vrf_name(self, v, load=False):
    """
    Setter method for vrf_name, mapped from YANG variable /pim_global_state/interfaces/vrf_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vrf_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vrf_name() directly.

    YANG Description: vrf name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vrf-name", rest_name="vrf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vrf_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf-name", rest_name="vrf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)""",
        })

    self.__vrf_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vrf_name(self):
    self.__vrf_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf-name", rest_name="vrf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)


  def _get_pim_interface_data(self):
    """
    Getter method for pim_interface_data, mapped from YANG variable /pim_global_state/interfaces/pim_interface_data (list)

    YANG Description: PIM interface information
    """
    return self.__pim_interface_data
      
  def _set_pim_interface_data(self, v, load=False):
    """
    Setter method for pim_interface_data, mapped from YANG variable /pim_global_state/interfaces/pim_interface_data (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pim_interface_data is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pim_interface_data() directly.

    YANG Description: PIM interface information
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("vrf_name interface_name interface_type",pim_interface_data.pim_interface_data, yang_name="pim-interface-data", rest_name="pim-interface-data", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vrf-name interface-name interface-type', extensions={u'tailf-common': {u'callpoint': u'pim-pim-interface-data', u'cli-suppress-show-path': None}}), is_container='list', yang_name="pim-interface-data", rest_name="pim-interface-data", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'pim-pim-interface-data', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pim_interface_data must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vrf_name interface_name interface_type",pim_interface_data.pim_interface_data, yang_name="pim-interface-data", rest_name="pim-interface-data", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vrf-name interface-name interface-type', extensions={u'tailf-common': {u'callpoint': u'pim-pim-interface-data', u'cli-suppress-show-path': None}}), is_container='list', yang_name="pim-interface-data", rest_name="pim-interface-data", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'pim-pim-interface-data', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='list', is_config=False)""",
        })

    self.__pim_interface_data = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pim_interface_data(self):
    self.__pim_interface_data = YANGDynClass(base=YANGListType("vrf_name interface_name interface_type",pim_interface_data.pim_interface_data, yang_name="pim-interface-data", rest_name="pim-interface-data", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vrf-name interface-name interface-type', extensions={u'tailf-common': {u'callpoint': u'pim-pim-interface-data', u'cli-suppress-show-path': None}}), is_container='list', yang_name="pim-interface-data", rest_name="pim-interface-data", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'pim-pim-interface-data', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='list', is_config=False)

  vrf_name = __builtin__.property(_get_vrf_name)
  pim_interface_data = __builtin__.property(_get_pim_interface_data)


  _pyangbind_elements = {'vrf_name': vrf_name, 'pim_interface_data': pim_interface_data, }


