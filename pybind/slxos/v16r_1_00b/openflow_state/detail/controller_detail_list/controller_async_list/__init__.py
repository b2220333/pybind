
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class controller_async_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-openflow-operational - based on the path /openflow-state/detail/controller-detail-list/controller-async-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: 
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__async_type','__config_data',)

  _yang_name = 'controller-async-list'
  _rest_name = 'controller-async-list'

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
    self.__async_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-port-status': {'value': 2}, u'dcm-packet-in': {'value': 1}, u'dcm-async-invalid': {'value': 0}, u'dcm-flow-removed': {'value': 3}},), is_leaf=True, yang_name="async-type", rest_name="async-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='async-type', is_config=False)
    self.__config_data = YANGDynClass(base=unicode, is_leaf=True, yang_name="config-data", rest_name="config-data", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)

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
      return [u'openflow-state', u'detail', u'controller-detail-list', u'controller-async-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'openflow-state', u'detail', u'controller-detail-list', u'controller-async-list']

  def _get_async_type(self):
    """
    Getter method for async_type, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_async_list/async_type (async-type)

    YANG Description: Asynchronous Configuration type
    """
    return self.__async_type
      
  def _set_async_type(self, v, load=False):
    """
    Setter method for async_type, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_async_list/async_type (async-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_async_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_async_type() directly.

    YANG Description: Asynchronous Configuration type
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-port-status': {'value': 2}, u'dcm-packet-in': {'value': 1}, u'dcm-async-invalid': {'value': 0}, u'dcm-flow-removed': {'value': 3}},), is_leaf=True, yang_name="async-type", rest_name="async-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='async-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """async_type must be of a type compatible with async-type""",
          'defined-type': "brocade-openflow-operational:async-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-port-status': {'value': 2}, u'dcm-packet-in': {'value': 1}, u'dcm-async-invalid': {'value': 0}, u'dcm-flow-removed': {'value': 3}},), is_leaf=True, yang_name="async-type", rest_name="async-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='async-type', is_config=False)""",
        })

    self.__async_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_async_type(self):
    self.__async_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-port-status': {'value': 2}, u'dcm-packet-in': {'value': 1}, u'dcm-async-invalid': {'value': 0}, u'dcm-flow-removed': {'value': 3}},), is_leaf=True, yang_name="async-type", rest_name="async-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='async-type', is_config=False)


  def _get_config_data(self):
    """
    Getter method for config_data, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_async_list/config_data (string)

    YANG Description: Asynchronous Configuration data
    """
    return self.__config_data
      
  def _set_config_data(self, v, load=False):
    """
    Setter method for config_data, mapped from YANG variable /openflow_state/detail/controller_detail_list/controller_async_list/config_data (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config_data is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config_data() directly.

    YANG Description: Asynchronous Configuration data
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="config-data", rest_name="config-data", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config_data must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="config-data", rest_name="config-data", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)""",
        })

    self.__config_data = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config_data(self):
    self.__config_data = YANGDynClass(base=unicode, is_leaf=True, yang_name="config-data", rest_name="config-data", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)

  async_type = __builtin__.property(_get_async_type)
  config_data = __builtin__.property(_get_config_data)


  _pyangbind_elements = {'async_type': async_type, 'config_data': config_data, }


