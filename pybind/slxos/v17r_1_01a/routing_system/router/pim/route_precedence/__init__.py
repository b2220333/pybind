
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class route_precedence(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/pim/route-precedence. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__uc_default','__uc_non_default','__none',)

  _yang_name = 'route-precedence'
  _rest_name = 'route-precedence'

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
    self.__uc_non_default = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="uc-non-default", rest_name="uc-non-default", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Select non default route from the unicast routing table'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='empty', is_config=True)
    self.__none = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="none", rest_name="none", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Skip precedence level'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='empty', is_config=True)
    self.__uc_default = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="uc-default", rest_name="uc-default", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Select default route from the unicast routing table'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'router', u'pim', u'route-precedence']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'pim', u'route-precedence']

  def _get_uc_default(self):
    """
    Getter method for uc_default, mapped from YANG variable /routing_system/router/pim/route_precedence/uc_default (empty)
    """
    return self.__uc_default
      
  def _set_uc_default(self, v, load=False):
    """
    Setter method for uc_default, mapped from YANG variable /routing_system/router/pim/route_precedence/uc_default (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_uc_default is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_uc_default() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="uc-default", rest_name="uc-default", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Select default route from the unicast routing table'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """uc_default must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="uc-default", rest_name="uc-default", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Select default route from the unicast routing table'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='empty', is_config=True)""",
        })

    self.__uc_default = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_uc_default(self):
    self.__uc_default = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="uc-default", rest_name="uc-default", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Select default route from the unicast routing table'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='empty', is_config=True)


  def _get_uc_non_default(self):
    """
    Getter method for uc_non_default, mapped from YANG variable /routing_system/router/pim/route_precedence/uc_non_default (empty)
    """
    return self.__uc_non_default
      
  def _set_uc_non_default(self, v, load=False):
    """
    Setter method for uc_non_default, mapped from YANG variable /routing_system/router/pim/route_precedence/uc_non_default (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_uc_non_default is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_uc_non_default() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="uc-non-default", rest_name="uc-non-default", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Select non default route from the unicast routing table'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """uc_non_default must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="uc-non-default", rest_name="uc-non-default", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Select non default route from the unicast routing table'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='empty', is_config=True)""",
        })

    self.__uc_non_default = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_uc_non_default(self):
    self.__uc_non_default = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="uc-non-default", rest_name="uc-non-default", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Select non default route from the unicast routing table'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='empty', is_config=True)


  def _get_none(self):
    """
    Getter method for none, mapped from YANG variable /routing_system/router/pim/route_precedence/none (empty)
    """
    return self.__none
      
  def _set_none(self, v, load=False):
    """
    Setter method for none, mapped from YANG variable /routing_system/router/pim/route_precedence/none (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_none is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_none() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="none", rest_name="none", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Skip precedence level'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """none must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="none", rest_name="none", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Skip precedence level'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='empty', is_config=True)""",
        })

    self.__none = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_none(self):
    self.__none = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="none", rest_name="none", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Skip precedence level'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='empty', is_config=True)

  uc_default = __builtin__.property(_get_uc_default, _set_uc_default)
  uc_non_default = __builtin__.property(_get_uc_non_default, _set_uc_non_default)
  none = __builtin__.property(_get_none, _set_none)


  _pyangbind_elements = {'uc_default': uc_default, 'uc_non_default': uc_non_default, 'none': none, }


