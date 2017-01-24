
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class wait_for_bgp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/isis/router-isis-cmds-holder/router-isis-attributes/set-overload-bit/on-startup/wait-for-bgp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__wait_for_bgp_value',)

  _yang_name = 'wait-for-bgp'
  _rest_name = 'wait-for-bgp'

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
    self.__wait_for_bgp_value = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'5..86400']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(600), is_leaf=True, yang_name="wait-for-bgp-value", rest_name="wait-for-bgp-value", parent=self, choice=(u'ch-on-startup', u'ca-on-startup-wfbgp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'Set overload-bit till BGP converges on reboot'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)

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
      return [u'routing-system', u'router', u'isis', u'router-isis-cmds-holder', u'router-isis-attributes', u'set-overload-bit', u'on-startup', u'wait-for-bgp']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'isis', u'set-overload-bit', u'on-startup', u'wait-for-bgp']

  def _get_wait_for_bgp_value(self):
    """
    Getter method for wait_for_bgp_value, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/router_isis_attributes/set_overload_bit/on_startup/wait_for_bgp/wait_for_bgp_value (uint32)
    """
    return self.__wait_for_bgp_value
      
  def _set_wait_for_bgp_value(self, v, load=False):
    """
    Setter method for wait_for_bgp_value, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/router_isis_attributes/set_overload_bit/on_startup/wait_for_bgp/wait_for_bgp_value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_wait_for_bgp_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_wait_for_bgp_value() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'5..86400']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(600), is_leaf=True, yang_name="wait-for-bgp-value", rest_name="wait-for-bgp-value", parent=self, choice=(u'ch-on-startup', u'ca-on-startup-wfbgp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'Set overload-bit till BGP converges on reboot'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """wait_for_bgp_value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'5..86400']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(600), is_leaf=True, yang_name="wait-for-bgp-value", rest_name="wait-for-bgp-value", parent=self, choice=(u'ch-on-startup', u'ca-on-startup-wfbgp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'Set overload-bit till BGP converges on reboot'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)""",
        })

    self.__wait_for_bgp_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_wait_for_bgp_value(self):
    self.__wait_for_bgp_value = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'5..86400']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(600), is_leaf=True, yang_name="wait-for-bgp-value", rest_name="wait-for-bgp-value", parent=self, choice=(u'ch-on-startup', u'ca-on-startup-wfbgp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'Set overload-bit till BGP converges on reboot'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)

  wait_for_bgp_value = __builtin__.property(_get_wait_for_bgp_value, _set_wait_for_bgp_value)

  __choices__ = {u'ch-on-startup': {u'ca-on-startup-wfbgp': [u'wait_for_bgp_value']}}
  _pyangbind_elements = {'wait_for_bgp_value': wait_for_bgp_value, }


