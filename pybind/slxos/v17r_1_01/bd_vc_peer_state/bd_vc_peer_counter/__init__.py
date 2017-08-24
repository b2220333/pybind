
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class bd_vc_peer_counter(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-pwm-operational - based on the path /bd-vc-peer-state/bd-vc-peer-counter. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description:  VC peer counters
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__no_of_peer_configured','__no_of_peer_operational',)

  _yang_name = 'bd-vc-peer-counter'
  _rest_name = 'bd-vc-peer-counter'

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
    self.__no_of_peer_configured = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="no-of-peer-configured", rest_name="no-of-peer-configured", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='uint32', is_config=False)
    self.__no_of_peer_operational = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="no-of-peer-operational", rest_name="no-of-peer-operational", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='uint32', is_config=False)

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
      return [u'bd-vc-peer-state', u'bd-vc-peer-counter']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'bd-vc-peer-state', u'bd-vc-peer-counter']

  def _get_no_of_peer_configured(self):
    """
    Getter method for no_of_peer_configured, mapped from YANG variable /bd_vc_peer_state/bd_vc_peer_counter/no_of_peer_configured (uint32)

    YANG Description: no_of_peer_configured
    """
    return self.__no_of_peer_configured
      
  def _set_no_of_peer_configured(self, v, load=False):
    """
    Setter method for no_of_peer_configured, mapped from YANG variable /bd_vc_peer_state/bd_vc_peer_counter/no_of_peer_configured (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_no_of_peer_configured is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_no_of_peer_configured() directly.

    YANG Description: no_of_peer_configured
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="no-of-peer-configured", rest_name="no-of-peer-configured", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """no_of_peer_configured must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="no-of-peer-configured", rest_name="no-of-peer-configured", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='uint32', is_config=False)""",
        })

    self.__no_of_peer_configured = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_no_of_peer_configured(self):
    self.__no_of_peer_configured = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="no-of-peer-configured", rest_name="no-of-peer-configured", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='uint32', is_config=False)


  def _get_no_of_peer_operational(self):
    """
    Getter method for no_of_peer_operational, mapped from YANG variable /bd_vc_peer_state/bd_vc_peer_counter/no_of_peer_operational (uint32)

    YANG Description: no_of_peer_operational
    """
    return self.__no_of_peer_operational
      
  def _set_no_of_peer_operational(self, v, load=False):
    """
    Setter method for no_of_peer_operational, mapped from YANG variable /bd_vc_peer_state/bd_vc_peer_counter/no_of_peer_operational (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_no_of_peer_operational is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_no_of_peer_operational() directly.

    YANG Description: no_of_peer_operational
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="no-of-peer-operational", rest_name="no-of-peer-operational", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """no_of_peer_operational must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="no-of-peer-operational", rest_name="no-of-peer-operational", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='uint32', is_config=False)""",
        })

    self.__no_of_peer_operational = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_no_of_peer_operational(self):
    self.__no_of_peer_operational = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="no-of-peer-operational", rest_name="no-of-peer-operational", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='uint32', is_config=False)

  no_of_peer_configured = __builtin__.property(_get_no_of_peer_configured)
  no_of_peer_operational = __builtin__.property(_get_no_of_peer_operational)


  _pyangbind_elements = {'no_of_peer_configured': no_of_peer_configured, 'no_of_peer_operational': no_of_peer_operational, }


