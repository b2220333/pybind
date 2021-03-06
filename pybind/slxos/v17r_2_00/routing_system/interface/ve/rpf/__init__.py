
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class rpf(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/interface/ve/rpf. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Reverse Path Forwarding configuration
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__log','__mode',)

  _yang_name = 'rpf'
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
    self.__log = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log", rest_name="log", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Log packets that fail RPF check and are to be dropped', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-rpf', defining_module='brocade-rpf', yang_type='empty', is_config=True)
    self.__mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'strict': {'value': 3}, u'loose': {'value': 2}},), is_leaf=True, yang_name="mode", rest_name="rpf-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'rpf-mode'}}, namespace='urn:brocade.com:mgmt:brocade-rpf', defining_module='brocade-rpf', yang_type='enumeration', is_config=True)

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
      return [u'routing-system', u'interface', u've', u'rpf']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ve']

  def _get_log(self):
    """
    Getter method for log, mapped from YANG variable /routing_system/interface/ve/rpf/log (empty)

    YANG Description: Log packets that fail RPF check and are to be dropped
    """
    return self.__log
      
  def _set_log(self, v, load=False):
    """
    Setter method for log, mapped from YANG variable /routing_system/interface/ve/rpf/log (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_log is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_log() directly.

    YANG Description: Log packets that fail RPF check and are to be dropped
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="log", rest_name="log", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Log packets that fail RPF check and are to be dropped', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-rpf', defining_module='brocade-rpf', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """log must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log", rest_name="log", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Log packets that fail RPF check and are to be dropped', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-rpf', defining_module='brocade-rpf', yang_type='empty', is_config=True)""",
        })

    self.__log = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_log(self):
    self.__log = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log", rest_name="log", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Log packets that fail RPF check and are to be dropped', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-rpf', defining_module='brocade-rpf', yang_type='empty', is_config=True)


  def _get_mode(self):
    """
    Getter method for mode, mapped from YANG variable /routing_system/interface/ve/rpf/mode (enumeration)
    """
    return self.__mode
      
  def _set_mode(self, v, load=False):
    """
    Setter method for mode, mapped from YANG variable /routing_system/interface/ve/rpf/mode (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mode() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'strict': {'value': 3}, u'loose': {'value': 2}},), is_leaf=True, yang_name="mode", rest_name="rpf-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'rpf-mode'}}, namespace='urn:brocade.com:mgmt:brocade-rpf', defining_module='brocade-rpf', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mode must be of a type compatible with enumeration""",
          'defined-type': "brocade-rpf:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'strict': {'value': 3}, u'loose': {'value': 2}},), is_leaf=True, yang_name="mode", rest_name="rpf-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'rpf-mode'}}, namespace='urn:brocade.com:mgmt:brocade-rpf', defining_module='brocade-rpf', yang_type='enumeration', is_config=True)""",
        })

    self.__mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mode(self):
    self.__mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'strict': {'value': 3}, u'loose': {'value': 2}},), is_leaf=True, yang_name="mode", rest_name="rpf-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'rpf-mode'}}, namespace='urn:brocade.com:mgmt:brocade-rpf', defining_module='brocade-rpf', yang_type='enumeration', is_config=True)

  log = __builtin__.property(_get_log, _set_log)
  mode = __builtin__.property(_get_mode, _set_mode)


  _pyangbind_elements = {'log': log, 'mode': mode, }


