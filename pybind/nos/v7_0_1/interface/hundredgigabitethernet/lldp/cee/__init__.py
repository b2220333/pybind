
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class cee(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/hundredgigabitethernet/lldp/cee. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Generate CEE capable event
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__lldp_cee_on_off',)

  _yang_name = 'cee'
  _rest_name = 'cee'

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
    self.__lldp_cee_on_off = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'on': {'value': 1}, u'off': {'value': 0}},), is_leaf=True, yang_name="lldp-cee-on-off", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='enumeration', is_config=True)

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
      return [u'interface', u'hundredgigabitethernet', u'lldp', u'cee']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'HundredGigabitEthernet', u'lldp', u'cee']

  def _get_lldp_cee_on_off(self):
    """
    Getter method for lldp_cee_on_off, mapped from YANG variable /interface/hundredgigabitethernet/lldp/cee/lldp_cee_on_off (enumeration)
    """
    return self.__lldp_cee_on_off
      
  def _set_lldp_cee_on_off(self, v, load=False):
    """
    Setter method for lldp_cee_on_off, mapped from YANG variable /interface/hundredgigabitethernet/lldp/cee/lldp_cee_on_off (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lldp_cee_on_off is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lldp_cee_on_off() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'on': {'value': 1}, u'off': {'value': 0}},), is_leaf=True, yang_name="lldp-cee-on-off", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lldp_cee_on_off must be of a type compatible with enumeration""",
          'defined-type': "brocade-lldp:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'on': {'value': 1}, u'off': {'value': 0}},), is_leaf=True, yang_name="lldp-cee-on-off", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='enumeration', is_config=True)""",
        })

    self.__lldp_cee_on_off = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lldp_cee_on_off(self):
    self.__lldp_cee_on_off = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'on': {'value': 1}, u'off': {'value': 0}},), is_leaf=True, yang_name="lldp-cee-on-off", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='enumeration', is_config=True)

  lldp_cee_on_off = __builtin__.property(_get_lldp_cee_on_off, _set_lldp_cee_on_off)


  _pyangbind_elements = {'lldp_cee_on_off': lldp_cee_on_off, }


