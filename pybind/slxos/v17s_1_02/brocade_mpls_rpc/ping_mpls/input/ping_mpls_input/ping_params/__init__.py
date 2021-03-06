
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ping_params(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/ping-mpls/input/ping-mpls-input/ping-params. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__count','__detail','__detour','__standby',)

  _yang_name = 'ping-params'
  _rest_name = 'ping-params'

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
    self.__count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="count", rest_name="count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__standby = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="standby", rest_name="standby", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    self.__detail = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="detail", rest_name="detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    self.__detour = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="detour", rest_name="detour", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)

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
      return [u'brocade_mpls_rpc', u'ping-mpls', u'input', u'ping-mpls-input', u'ping-params']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ping-mpls', u'input', u'ping-mpls-input', u'ping-params']

  def _get_count(self):
    """
    Getter method for count, mapped from YANG variable /brocade_mpls_rpc/ping_mpls/input/ping_mpls_input/ping_params/count (uint32)

    YANG Description: count
    """
    return self.__count
      
  def _set_count(self, v, load=False):
    """
    Setter method for count, mapped from YANG variable /brocade_mpls_rpc/ping_mpls/input/ping_mpls_input/ping_params/count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_count() directly.

    YANG Description: count
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="count", rest_name="count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="count", rest_name="count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_count(self):
    self.__count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="count", rest_name="count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_detail(self):
    """
    Getter method for detail, mapped from YANG variable /brocade_mpls_rpc/ping_mpls/input/ping_mpls_input/ping_params/detail (empty)

    YANG Description: detail
    """
    return self.__detail
      
  def _set_detail(self, v, load=False):
    """
    Setter method for detail, mapped from YANG variable /brocade_mpls_rpc/ping_mpls/input/ping_mpls_input/ping_params/detail (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_detail is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_detail() directly.

    YANG Description: detail
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="detail", rest_name="detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """detail must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="detail", rest_name="detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)""",
        })

    self.__detail = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_detail(self):
    self.__detail = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="detail", rest_name="detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)


  def _get_detour(self):
    """
    Getter method for detour, mapped from YANG variable /brocade_mpls_rpc/ping_mpls/input/ping_mpls_input/ping_params/detour (empty)

    YANG Description: detour
    """
    return self.__detour
      
  def _set_detour(self, v, load=False):
    """
    Setter method for detour, mapped from YANG variable /brocade_mpls_rpc/ping_mpls/input/ping_mpls_input/ping_params/detour (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_detour is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_detour() directly.

    YANG Description: detour
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="detour", rest_name="detour", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """detour must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="detour", rest_name="detour", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)""",
        })

    self.__detour = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_detour(self):
    self.__detour = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="detour", rest_name="detour", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)


  def _get_standby(self):
    """
    Getter method for standby, mapped from YANG variable /brocade_mpls_rpc/ping_mpls/input/ping_mpls_input/ping_params/standby (empty)

    YANG Description: standby
    """
    return self.__standby
      
  def _set_standby(self, v, load=False):
    """
    Setter method for standby, mapped from YANG variable /brocade_mpls_rpc/ping_mpls/input/ping_mpls_input/ping_params/standby (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_standby is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_standby() directly.

    YANG Description: standby
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="standby", rest_name="standby", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """standby must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="standby", rest_name="standby", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)""",
        })

    self.__standby = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_standby(self):
    self.__standby = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="standby", rest_name="standby", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)

  count = __builtin__.property(_get_count, _set_count)
  detail = __builtin__.property(_get_detail, _set_detail)
  detour = __builtin__.property(_get_detour, _set_detour)
  standby = __builtin__.property(_get_standby, _set_standby)


  _pyangbind_elements = {'count': count, 'detail': detail, 'detour': detour, 'standby': standby, }


