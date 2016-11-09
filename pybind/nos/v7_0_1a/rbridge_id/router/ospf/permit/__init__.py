
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import redistribute
class permit(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/ospf/permit. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__redistribute',)

  _yang_name = 'permit'
  _rest_name = 'permit'

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
    self.__redistribute = YANGDynClass(base=YANGListType("redist_value route_option",redistribute.redistribute, yang_name="redistribute", rest_name="redistribute", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='redist-value route-option', extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-mode': None, u'callpoint': u'OSPFPermitRedistributeCallPoint'}}), is_container='list', yang_name="redistribute", rest_name="redistribute", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-mode': None, u'callpoint': u'OSPFPermitRedistributeCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='list', is_config=True)

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
      return [u'rbridge-id', u'router', u'ospf', u'permit']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'ospf', u'permit']

  def _get_redistribute(self):
    """
    Getter method for redistribute, mapped from YANG variable /rbridge_id/router/ospf/permit/redistribute (list)
    """
    return self.__redistribute
      
  def _set_redistribute(self, v, load=False):
    """
    Setter method for redistribute, mapped from YANG variable /rbridge_id/router/ospf/permit/redistribute (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redistribute is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redistribute() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("redist_value route_option",redistribute.redistribute, yang_name="redistribute", rest_name="redistribute", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='redist-value route-option', extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-mode': None, u'callpoint': u'OSPFPermitRedistributeCallPoint'}}), is_container='list', yang_name="redistribute", rest_name="redistribute", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-mode': None, u'callpoint': u'OSPFPermitRedistributeCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redistribute must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("redist_value route_option",redistribute.redistribute, yang_name="redistribute", rest_name="redistribute", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='redist-value route-option', extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-mode': None, u'callpoint': u'OSPFPermitRedistributeCallPoint'}}), is_container='list', yang_name="redistribute", rest_name="redistribute", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-mode': None, u'callpoint': u'OSPFPermitRedistributeCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='list', is_config=True)""",
        })

    self.__redistribute = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redistribute(self):
    self.__redistribute = YANGDynClass(base=YANGListType("redist_value route_option",redistribute.redistribute, yang_name="redistribute", rest_name="redistribute", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='redist-value route-option', extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-mode': None, u'callpoint': u'OSPFPermitRedistributeCallPoint'}}), is_container='list', yang_name="redistribute", rest_name="redistribute", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-mode': None, u'callpoint': u'OSPFPermitRedistributeCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='list', is_config=True)

  redistribute = __builtin__.property(_get_redistribute, _set_redistribute)


  _pyangbind_elements = {'redistribute': redistribute, }


