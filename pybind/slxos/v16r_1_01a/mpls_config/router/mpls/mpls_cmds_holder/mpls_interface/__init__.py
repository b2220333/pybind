
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ldp_params
import rsvp
import interface_dynamic_bypass
class mpls_interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /mpls-config/router/mpls/mpls-cmds-holder/mpls-interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__interface_type','__interface_name','__mpls_interface_ldp_enable','__ldp_params','__rsvp','__interface_dynamic_bypass',)

  _yang_name = 'mpls-interface'
  _rest_name = 'mpls-interface'

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
    self.__ldp_params = YANGDynClass(base=ldp_params.ldp_params, is_container='container', presence=False, yang_name="ldp-params", rest_name="ldp-params", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure LDP parameters', u'cli-full-command': None, u'cli-full-no': None, u'cli-add-mode': None, u'cli-mode-name': u'config-router-mpls-if-$(interface-type)-$(interface-name)-ldp-params'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    self.__interface_dynamic_bypass = YANGDynClass(base=interface_dynamic_bypass.interface_dynamic_bypass, is_container='container', presence=True, yang_name="interface-dynamic-bypass", rest_name="dynamic-bypass", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'MplsInterfaceDynamicBypass', u'info': u'Configure Dynamic bypass interface level parameters', u'cli-full-no': None, u'cli-add-mode': None, u'cli-full-command': None, u'hidden': u'full', u'alt-name': u'dynamic-bypass', u'cli-mode-name': u'config-router-mpls-if-$(interface-type)-$(interface-name)-dynamic-bypass'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    self.__interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 2}, u've': {'value': 6}},), is_leaf=True, yang_name="interface-type", rest_name="interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='enumeration', is_config=True)
    self.__interface_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6])/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)|([0-9]([0-9])?([0-9])?([0-9])?))', 'length': [u'1..16']}), is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Interface value.'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='interface-type', is_config=True)
    self.__mpls_interface_ldp_enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-interface-ldp-enable", rest_name="ldp-enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable LDP on Interface', u'cli-full-no': None, u'alt-name': u'ldp-enable'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    self.__rsvp = YANGDynClass(base=rsvp.rsvp, is_container='container', presence=False, yang_name="rsvp", rest_name="rsvp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RSVP parameters', u'callpoint': u'MplsInterface', u'cli-add-mode': None, u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-router-mpls-if-$(interface-type)-$(interface-name)-rsvp'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)

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
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'mpls-interface']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'mpls', u'mpls-interface']

  def _get_interface_type(self):
    """
    Getter method for interface_type, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/interface_type (enumeration)
    """
    return self.__interface_type
      
  def _set_interface_type(self, v, load=False):
    """
    Setter method for interface_type, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/interface_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_type() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 2}, u've': {'value': 6}},), is_leaf=True, yang_name="interface-type", rest_name="interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-mpls:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 2}, u've': {'value': 6}},), is_leaf=True, yang_name="interface-type", rest_name="interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='enumeration', is_config=True)""",
        })

    self.__interface_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_type(self):
    self.__interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 2}, u've': {'value': 6}},), is_leaf=True, yang_name="interface-type", rest_name="interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='enumeration', is_config=True)


  def _get_interface_name(self):
    """
    Getter method for interface_name, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/interface_name (interface-type)
    """
    return self.__interface_name
      
  def _set_interface_name(self, v, load=False):
    """
    Setter method for interface_name, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/interface_name (interface-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6])/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)|([0-9]([0-9])?([0-9])?([0-9])?))', 'length': [u'1..16']}), is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Interface value.'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='interface-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_name must be of a type compatible with interface-type""",
          'defined-type': "brocade-mpls:interface-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6])/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)|([0-9]([0-9])?([0-9])?([0-9])?))', 'length': [u'1..16']}), is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Interface value.'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='interface-type', is_config=True)""",
        })

    self.__interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_name(self):
    self.__interface_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6])/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)|([0-9]([0-9])?([0-9])?([0-9])?))', 'length': [u'1..16']}), is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Interface value.'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='interface-type', is_config=True)


  def _get_mpls_interface_ldp_enable(self):
    """
    Getter method for mpls_interface_ldp_enable, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/mpls_interface_ldp_enable (empty)
    """
    return self.__mpls_interface_ldp_enable
      
  def _set_mpls_interface_ldp_enable(self, v, load=False):
    """
    Setter method for mpls_interface_ldp_enable, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/mpls_interface_ldp_enable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_interface_ldp_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_interface_ldp_enable() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="mpls-interface-ldp-enable", rest_name="ldp-enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable LDP on Interface', u'cli-full-no': None, u'alt-name': u'ldp-enable'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_interface_ldp_enable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-interface-ldp-enable", rest_name="ldp-enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable LDP on Interface', u'cli-full-no': None, u'alt-name': u'ldp-enable'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)""",
        })

    self.__mpls_interface_ldp_enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_interface_ldp_enable(self):
    self.__mpls_interface_ldp_enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-interface-ldp-enable", rest_name="ldp-enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable LDP on Interface', u'cli-full-no': None, u'alt-name': u'ldp-enable'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)


  def _get_ldp_params(self):
    """
    Getter method for ldp_params, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/ldp_params (container)
    """
    return self.__ldp_params
      
  def _set_ldp_params(self, v, load=False):
    """
    Setter method for ldp_params, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/ldp_params (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_params is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_params() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ldp_params.ldp_params, is_container='container', presence=False, yang_name="ldp-params", rest_name="ldp-params", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure LDP parameters', u'cli-full-command': None, u'cli-full-no': None, u'cli-add-mode': None, u'cli-mode-name': u'config-router-mpls-if-$(interface-type)-$(interface-name)-ldp-params'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_params must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ldp_params.ldp_params, is_container='container', presence=False, yang_name="ldp-params", rest_name="ldp-params", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure LDP parameters', u'cli-full-command': None, u'cli-full-no': None, u'cli-add-mode': None, u'cli-mode-name': u'config-router-mpls-if-$(interface-type)-$(interface-name)-ldp-params'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__ldp_params = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_params(self):
    self.__ldp_params = YANGDynClass(base=ldp_params.ldp_params, is_container='container', presence=False, yang_name="ldp-params", rest_name="ldp-params", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure LDP parameters', u'cli-full-command': None, u'cli-full-no': None, u'cli-add-mode': None, u'cli-mode-name': u'config-router-mpls-if-$(interface-type)-$(interface-name)-ldp-params'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)


  def _get_rsvp(self):
    """
    Getter method for rsvp, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/rsvp (container)
    """
    return self.__rsvp
      
  def _set_rsvp(self, v, load=False):
    """
    Setter method for rsvp, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/rsvp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rsvp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rsvp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=rsvp.rsvp, is_container='container', presence=False, yang_name="rsvp", rest_name="rsvp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RSVP parameters', u'callpoint': u'MplsInterface', u'cli-add-mode': None, u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-router-mpls-if-$(interface-type)-$(interface-name)-rsvp'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rsvp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=rsvp.rsvp, is_container='container', presence=False, yang_name="rsvp", rest_name="rsvp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RSVP parameters', u'callpoint': u'MplsInterface', u'cli-add-mode': None, u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-router-mpls-if-$(interface-type)-$(interface-name)-rsvp'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__rsvp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rsvp(self):
    self.__rsvp = YANGDynClass(base=rsvp.rsvp, is_container='container', presence=False, yang_name="rsvp", rest_name="rsvp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RSVP parameters', u'callpoint': u'MplsInterface', u'cli-add-mode': None, u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-router-mpls-if-$(interface-type)-$(interface-name)-rsvp'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)


  def _get_interface_dynamic_bypass(self):
    """
    Getter method for interface_dynamic_bypass, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/interface_dynamic_bypass (container)
    """
    return self.__interface_dynamic_bypass
      
  def _set_interface_dynamic_bypass(self, v, load=False):
    """
    Setter method for interface_dynamic_bypass, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/interface_dynamic_bypass (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_dynamic_bypass is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_dynamic_bypass() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interface_dynamic_bypass.interface_dynamic_bypass, is_container='container', presence=True, yang_name="interface-dynamic-bypass", rest_name="dynamic-bypass", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'MplsInterfaceDynamicBypass', u'info': u'Configure Dynamic bypass interface level parameters', u'cli-full-no': None, u'cli-add-mode': None, u'cli-full-command': None, u'hidden': u'full', u'alt-name': u'dynamic-bypass', u'cli-mode-name': u'config-router-mpls-if-$(interface-type)-$(interface-name)-dynamic-bypass'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_dynamic_bypass must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface_dynamic_bypass.interface_dynamic_bypass, is_container='container', presence=True, yang_name="interface-dynamic-bypass", rest_name="dynamic-bypass", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'MplsInterfaceDynamicBypass', u'info': u'Configure Dynamic bypass interface level parameters', u'cli-full-no': None, u'cli-add-mode': None, u'cli-full-command': None, u'hidden': u'full', u'alt-name': u'dynamic-bypass', u'cli-mode-name': u'config-router-mpls-if-$(interface-type)-$(interface-name)-dynamic-bypass'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__interface_dynamic_bypass = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_dynamic_bypass(self):
    self.__interface_dynamic_bypass = YANGDynClass(base=interface_dynamic_bypass.interface_dynamic_bypass, is_container='container', presence=True, yang_name="interface-dynamic-bypass", rest_name="dynamic-bypass", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'MplsInterfaceDynamicBypass', u'info': u'Configure Dynamic bypass interface level parameters', u'cli-full-no': None, u'cli-add-mode': None, u'cli-full-command': None, u'hidden': u'full', u'alt-name': u'dynamic-bypass', u'cli-mode-name': u'config-router-mpls-if-$(interface-type)-$(interface-name)-dynamic-bypass'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)

  interface_type = __builtin__.property(_get_interface_type, _set_interface_type)
  interface_name = __builtin__.property(_get_interface_name, _set_interface_name)
  mpls_interface_ldp_enable = __builtin__.property(_get_mpls_interface_ldp_enable, _set_mpls_interface_ldp_enable)
  ldp_params = __builtin__.property(_get_ldp_params, _set_ldp_params)
  rsvp = __builtin__.property(_get_rsvp, _set_rsvp)
  interface_dynamic_bypass = __builtin__.property(_get_interface_dynamic_bypass, _set_interface_dynamic_bypass)


  _pyangbind_elements = {'interface_type': interface_type, 'interface_name': interface_name, 'mpls_interface_ldp_enable': mpls_interface_ldp_enable, 'ldp_params': ldp_params, 'rsvp': rsvp, 'interface_dynamic_bypass': interface_dynamic_bypass, }


