
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class mtu(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-pw-profile - based on the path /pw-profile/mtu. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: MTU for a Psuedo Wire
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mtu_value',)

  _yang_name = 'mtu'
  _rest_name = 'mtu'

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
    self.__mtu_value = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'64..15966']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1500), is_leaf=True, yang_name="mtu-value", rest_name="mtu-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MTU value is used during Psuedo Wire setup signalling', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-pw-profile', defining_module='brocade-pw-profile', yang_type='uint32', is_config=True)

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
      return [u'pw-profile', u'mtu']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'pw-profile', u'mtu']

  def _get_mtu_value(self):
    """
    Getter method for mtu_value, mapped from YANG variable /pw_profile/mtu/mtu_value (uint32)

    YANG Description: MTU value is used during Psuedo Wire setup signalling.
    """
    return self.__mtu_value
      
  def _set_mtu_value(self, v, load=False):
    """
    Setter method for mtu_value, mapped from YANG variable /pw_profile/mtu/mtu_value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mtu_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mtu_value() directly.

    YANG Description: MTU value is used during Psuedo Wire setup signalling.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'64..15966']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1500), is_leaf=True, yang_name="mtu-value", rest_name="mtu-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MTU value is used during Psuedo Wire setup signalling', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-pw-profile', defining_module='brocade-pw-profile', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mtu_value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'64..15966']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1500), is_leaf=True, yang_name="mtu-value", rest_name="mtu-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MTU value is used during Psuedo Wire setup signalling', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-pw-profile', defining_module='brocade-pw-profile', yang_type='uint32', is_config=True)""",
        })

    self.__mtu_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mtu_value(self):
    self.__mtu_value = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'64..15966']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1500), is_leaf=True, yang_name="mtu-value", rest_name="mtu-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MTU value is used during Psuedo Wire setup signalling', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-pw-profile', defining_module='brocade-pw-profile', yang_type='uint32', is_config=True)

  mtu_value = __builtin__.property(_get_mtu_value, _set_mtu_value)


  _pyangbind_elements = {'mtu_value': mtu_value, }

