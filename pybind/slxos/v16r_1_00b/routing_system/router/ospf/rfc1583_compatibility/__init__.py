
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class rfc1583_compatibility(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/ospf/rfc1583-compatibility. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__rfc1583_compatibility_flag',)

  _yang_name = 'rfc1583-compatibility'
  _rest_name = 'rfc1583-compatibility'

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
    self.__rfc1583_compatibility_flag = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="rfc1583-compatibility-flag", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable RFC 1583 OSPF v2 compatibility', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'router', u'ospf', u'rfc1583-compatibility']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'ospf', u'rfc1583-compatibility']

  def _get_rfc1583_compatibility_flag(self):
    """
    Getter method for rfc1583_compatibility_flag, mapped from YANG variable /routing_system/router/ospf/rfc1583_compatibility/rfc1583_compatibility_flag (empty)
    """
    return self.__rfc1583_compatibility_flag
      
  def _set_rfc1583_compatibility_flag(self, v, load=False):
    """
    Setter method for rfc1583_compatibility_flag, mapped from YANG variable /routing_system/router/ospf/rfc1583_compatibility/rfc1583_compatibility_flag (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rfc1583_compatibility_flag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rfc1583_compatibility_flag() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="rfc1583-compatibility-flag", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable RFC 1583 OSPF v2 compatibility', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rfc1583_compatibility_flag must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="rfc1583-compatibility-flag", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable RFC 1583 OSPF v2 compatibility', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)""",
        })

    self.__rfc1583_compatibility_flag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rfc1583_compatibility_flag(self):
    self.__rfc1583_compatibility_flag = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="rfc1583-compatibility-flag", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable RFC 1583 OSPF v2 compatibility', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)

  rfc1583_compatibility_flag = __builtin__.property(_get_rfc1583_compatibility_flag, _set_rfc1583_compatibility_flag)


  _pyangbind_elements = {'rfc1583_compatibility_flag': rfc1583_compatibility_flag, }


