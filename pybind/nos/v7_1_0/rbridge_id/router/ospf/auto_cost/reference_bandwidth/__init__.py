
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class reference_bandwidth(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/ospf/auto-cost/reference-bandwidth. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ref_bandwidth','__use_active_ports',)

  _yang_name = 'reference-bandwidth'
  _rest_name = 'reference-bandwidth'

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
    self.__ref_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(100), is_leaf=True, yang_name="ref-bandwidth", rest_name="ref-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='band-width', is_config=True)
    self.__use_active_ports = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="use-active-ports", rest_name="use-active-ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Dynamic change of BW will reflect cost change'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)

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
      return [u'rbridge-id', u'router', u'ospf', u'auto-cost', u'reference-bandwidth']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'ospf', u'auto-cost', u'reference-bandwidth']

  def _get_ref_bandwidth(self):
    """
    Getter method for ref_bandwidth, mapped from YANG variable /rbridge_id/router/ospf/auto_cost/reference_bandwidth/ref_bandwidth (band-width)
    """
    return self.__ref_bandwidth
      
  def _set_ref_bandwidth(self, v, load=False):
    """
    Setter method for ref_bandwidth, mapped from YANG variable /rbridge_id/router/ospf/auto_cost/reference_bandwidth/ref_bandwidth (band-width)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ref_bandwidth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ref_bandwidth() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(100), is_leaf=True, yang_name="ref-bandwidth", rest_name="ref-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='band-width', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ref_bandwidth must be of a type compatible with band-width""",
          'defined-type': "brocade-ospf:band-width",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(100), is_leaf=True, yang_name="ref-bandwidth", rest_name="ref-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='band-width', is_config=True)""",
        })

    self.__ref_bandwidth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ref_bandwidth(self):
    self.__ref_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(100), is_leaf=True, yang_name="ref-bandwidth", rest_name="ref-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='band-width', is_config=True)


  def _get_use_active_ports(self):
    """
    Getter method for use_active_ports, mapped from YANG variable /rbridge_id/router/ospf/auto_cost/reference_bandwidth/use_active_ports (empty)
    """
    return self.__use_active_ports
      
  def _set_use_active_ports(self, v, load=False):
    """
    Setter method for use_active_ports, mapped from YANG variable /rbridge_id/router/ospf/auto_cost/reference_bandwidth/use_active_ports (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_use_active_ports is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_use_active_ports() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="use-active-ports", rest_name="use-active-ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Dynamic change of BW will reflect cost change'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """use_active_ports must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="use-active-ports", rest_name="use-active-ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Dynamic change of BW will reflect cost change'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)""",
        })

    self.__use_active_ports = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_use_active_ports(self):
    self.__use_active_ports = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="use-active-ports", rest_name="use-active-ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Dynamic change of BW will reflect cost change'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)

  ref_bandwidth = __builtin__.property(_get_ref_bandwidth, _set_ref_bandwidth)
  use_active_ports = __builtin__.property(_get_use_active_ports, _set_use_active_ports)


  _pyangbind_elements = {'ref_bandwidth': ref_bandwidth, 'use_active_ports': use_active_ports, }


