
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class subnet_rate_limit(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-control-plane - based on the path /control-plane/ipv6/subnet-rate-limit. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__cir','__cbr',)

  _yang_name = 'subnet-rate-limit'
  _rest_name = 'subnet-rate-limit'

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
    self.__cbr = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 64']}), is_leaf=True, yang_name="cbr", rest_name="cbr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Burst Value'}}, namespace='urn:brocade.com:mgmt:brocade-control-plane', defining_module='brocade-control-plane', yang_type='rate-limit-cbr', is_config=True)
    self.__cir = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100000']}), is_leaf=True, yang_name="cir", rest_name="cir", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Rate Value', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-control-plane', defining_module='brocade-control-plane', yang_type='rate-limit-cir', is_config=True)

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
      return [u'control-plane', u'ipv6', u'subnet-rate-limit']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'control-plane', u'ipv6', u'subnet-rate-limit']

  def _get_cir(self):
    """
    Getter method for cir, mapped from YANG variable /control_plane/ipv6/subnet_rate_limit/cir (rate-limit-cir)
    """
    return self.__cir
      
  def _set_cir(self, v, load=False):
    """
    Setter method for cir, mapped from YANG variable /control_plane/ipv6/subnet_rate_limit/cir (rate-limit-cir)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cir is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cir() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100000']}), is_leaf=True, yang_name="cir", rest_name="cir", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Rate Value', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-control-plane', defining_module='brocade-control-plane', yang_type='rate-limit-cir', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cir must be of a type compatible with rate-limit-cir""",
          'defined-type': "brocade-control-plane:rate-limit-cir",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100000']}), is_leaf=True, yang_name="cir", rest_name="cir", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Rate Value', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-control-plane', defining_module='brocade-control-plane', yang_type='rate-limit-cir', is_config=True)""",
        })

    self.__cir = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cir(self):
    self.__cir = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100000']}), is_leaf=True, yang_name="cir", rest_name="cir", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Rate Value', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-control-plane', defining_module='brocade-control-plane', yang_type='rate-limit-cir', is_config=True)


  def _get_cbr(self):
    """
    Getter method for cbr, mapped from YANG variable /control_plane/ipv6/subnet_rate_limit/cbr (rate-limit-cbr)
    """
    return self.__cbr
      
  def _set_cbr(self, v, load=False):
    """
    Setter method for cbr, mapped from YANG variable /control_plane/ipv6/subnet_rate_limit/cbr (rate-limit-cbr)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cbr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cbr() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 64']}), is_leaf=True, yang_name="cbr", rest_name="cbr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Burst Value'}}, namespace='urn:brocade.com:mgmt:brocade-control-plane', defining_module='brocade-control-plane', yang_type='rate-limit-cbr', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cbr must be of a type compatible with rate-limit-cbr""",
          'defined-type': "brocade-control-plane:rate-limit-cbr",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 64']}), is_leaf=True, yang_name="cbr", rest_name="cbr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Burst Value'}}, namespace='urn:brocade.com:mgmt:brocade-control-plane', defining_module='brocade-control-plane', yang_type='rate-limit-cbr', is_config=True)""",
        })

    self.__cbr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cbr(self):
    self.__cbr = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 64']}), is_leaf=True, yang_name="cbr", rest_name="cbr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Burst Value'}}, namespace='urn:brocade.com:mgmt:brocade-control-plane', defining_module='brocade-control-plane', yang_type='rate-limit-cbr', is_config=True)

  cir = __builtin__.property(_get_cir, _set_cir)
  cbr = __builtin__.property(_get_cbr, _set_cbr)


  _pyangbind_elements = {'cir': cir, 'cbr': cbr, }


