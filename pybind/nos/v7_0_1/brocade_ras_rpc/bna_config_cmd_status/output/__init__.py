
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ras - based on the path /brocade_ras_rpc/bna-config-cmd-status/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__status','__status_string',)

  _yang_name = 'output'
  _rest_name = 'output'

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
    self.__status = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'in-progress': {'value': 3}, u'unknown': {'value': 1}, u'completed': {'value': 2}, u'error': {'value': 4}},), is_leaf=True, yang_name="status", rest_name="status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='cmd-status', is_config=True)
    self.__status_string = YANGDynClass(base=unicode, is_leaf=True, yang_name="status-string", rest_name="status-string", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='string', is_config=True)

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
      return [u'brocade_ras_rpc', u'bna-config-cmd-status', u'output']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'bna-config-cmd-status', u'output']

  def _get_status(self):
    """
    Getter method for status, mapped from YANG variable /brocade_ras_rpc/bna_config_cmd_status/output/status (cmd-status)
    """
    return self.__status
      
  def _set_status(self, v, load=False):
    """
    Setter method for status, mapped from YANG variable /brocade_ras_rpc/bna_config_cmd_status/output/status (cmd-status)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_status() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'in-progress': {'value': 3}, u'unknown': {'value': 1}, u'completed': {'value': 2}, u'error': {'value': 4}},), is_leaf=True, yang_name="status", rest_name="status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='cmd-status', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """status must be of a type compatible with cmd-status""",
          'defined-type': "brocade-ras:cmd-status",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'in-progress': {'value': 3}, u'unknown': {'value': 1}, u'completed': {'value': 2}, u'error': {'value': 4}},), is_leaf=True, yang_name="status", rest_name="status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='cmd-status', is_config=True)""",
        })

    self.__status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_status(self):
    self.__status = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'in-progress': {'value': 3}, u'unknown': {'value': 1}, u'completed': {'value': 2}, u'error': {'value': 4}},), is_leaf=True, yang_name="status", rest_name="status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='cmd-status', is_config=True)


  def _get_status_string(self):
    """
    Getter method for status_string, mapped from YANG variable /brocade_ras_rpc/bna_config_cmd_status/output/status_string (string)

    YANG Description: Error in string format
    """
    return self.__status_string
      
  def _set_status_string(self, v, load=False):
    """
    Setter method for status_string, mapped from YANG variable /brocade_ras_rpc/bna_config_cmd_status/output/status_string (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_status_string is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_status_string() directly.

    YANG Description: Error in string format
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="status-string", rest_name="status-string", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """status_string must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="status-string", rest_name="status-string", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='string', is_config=True)""",
        })

    self.__status_string = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_status_string(self):
    self.__status_string = YANGDynClass(base=unicode, is_leaf=True, yang_name="status-string", rest_name="status-string", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='string', is_config=True)

  status = __builtin__.property(_get_status, _set_status)
  status_string = __builtin__.property(_get_status_string, _set_status_string)


  _pyangbind_elements = {'status': status, 'status_string': status_string, }


