
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ldp_interface_data(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/ldp/interface/ldp-interface-data. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description:  LDP interface
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ldp_interface_name','__ldp_interface_type','__ldp_interface_lbpsp','__ldp_interface_nbr_cnt','__ldp_interface_hello_intl','__ldp_interface_hello_timeout','__ldp_interface_hello_next',)

  _yang_name = 'ldp-interface-data'
  _rest_name = 'ldp-interface-data'

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
    self.__ldp_interface_hello_intl = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-interface-hello-intl", rest_name="ldp-interface-hello-intl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__ldp_interface_lbpsp = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-interface-lbpsp", rest_name="ldp-interface-lbpsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__ldp_interface_hello_timeout = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-interface-hello-timeout", rest_name="ldp-interface-hello-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__ldp_interface_hello_next = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-interface-hello-next", rest_name="ldp-interface-hello-next", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__ldp_interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="ldp-interface-name", rest_name="ldp-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    self.__ldp_interface_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="ldp-interface-type", rest_name="ldp-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    self.__ldp_interface_nbr_cnt = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-interface-nbr-cnt", rest_name="ldp-interface-nbr-cnt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)

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
      return [u'mpls-state', u'ldp', u'interface', u'ldp-interface-data']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'ldp', u'interface', u'ldp-interface-data']

  def _get_ldp_interface_name(self):
    """
    Getter method for ldp_interface_name, mapped from YANG variable /mpls_state/ldp/interface/ldp_interface_data/ldp_interface_name (string)

    YANG Description: ldp interface name
    """
    return self.__ldp_interface_name
      
  def _set_ldp_interface_name(self, v, load=False):
    """
    Setter method for ldp_interface_name, mapped from YANG variable /mpls_state/ldp/interface/ldp_interface_data/ldp_interface_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_interface_name() directly.

    YANG Description: ldp interface name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="ldp-interface-name", rest_name="ldp-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_interface_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="ldp-interface-name", rest_name="ldp-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)""",
        })

    self.__ldp_interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_interface_name(self):
    self.__ldp_interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="ldp-interface-name", rest_name="ldp-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)


  def _get_ldp_interface_type(self):
    """
    Getter method for ldp_interface_type, mapped from YANG variable /mpls_state/ldp/interface/ldp_interface_data/ldp_interface_type (string)

    YANG Description: ldp interface type
    """
    return self.__ldp_interface_type
      
  def _set_ldp_interface_type(self, v, load=False):
    """
    Setter method for ldp_interface_type, mapped from YANG variable /mpls_state/ldp/interface/ldp_interface_data/ldp_interface_type (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_interface_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_interface_type() directly.

    YANG Description: ldp interface type
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="ldp-interface-type", rest_name="ldp-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_interface_type must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="ldp-interface-type", rest_name="ldp-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)""",
        })

    self.__ldp_interface_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_interface_type(self):
    self.__ldp_interface_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="ldp-interface-type", rest_name="ldp-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)


  def _get_ldp_interface_lbpsp(self):
    """
    Getter method for ldp_interface_lbpsp, mapped from YANG variable /mpls_state/ldp/interface/ldp_interface_data/ldp_interface_lbpsp (uint32)

    YANG Description: ldp interface label space
    """
    return self.__ldp_interface_lbpsp
      
  def _set_ldp_interface_lbpsp(self, v, load=False):
    """
    Setter method for ldp_interface_lbpsp, mapped from YANG variable /mpls_state/ldp/interface/ldp_interface_data/ldp_interface_lbpsp (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_interface_lbpsp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_interface_lbpsp() directly.

    YANG Description: ldp interface label space
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-interface-lbpsp", rest_name="ldp-interface-lbpsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_interface_lbpsp must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-interface-lbpsp", rest_name="ldp-interface-lbpsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__ldp_interface_lbpsp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_interface_lbpsp(self):
    self.__ldp_interface_lbpsp = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-interface-lbpsp", rest_name="ldp-interface-lbpsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_ldp_interface_nbr_cnt(self):
    """
    Getter method for ldp_interface_nbr_cnt, mapped from YANG variable /mpls_state/ldp/interface/ldp_interface_data/ldp_interface_nbr_cnt (uint32)

    YANG Description: ldp interface neighbour count
    """
    return self.__ldp_interface_nbr_cnt
      
  def _set_ldp_interface_nbr_cnt(self, v, load=False):
    """
    Setter method for ldp_interface_nbr_cnt, mapped from YANG variable /mpls_state/ldp/interface/ldp_interface_data/ldp_interface_nbr_cnt (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_interface_nbr_cnt is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_interface_nbr_cnt() directly.

    YANG Description: ldp interface neighbour count
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-interface-nbr-cnt", rest_name="ldp-interface-nbr-cnt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_interface_nbr_cnt must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-interface-nbr-cnt", rest_name="ldp-interface-nbr-cnt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__ldp_interface_nbr_cnt = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_interface_nbr_cnt(self):
    self.__ldp_interface_nbr_cnt = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-interface-nbr-cnt", rest_name="ldp-interface-nbr-cnt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_ldp_interface_hello_intl(self):
    """
    Getter method for ldp_interface_hello_intl, mapped from YANG variable /mpls_state/ldp/interface/ldp_interface_data/ldp_interface_hello_intl (uint32)

    YANG Description: ldp interface hello interval
    """
    return self.__ldp_interface_hello_intl
      
  def _set_ldp_interface_hello_intl(self, v, load=False):
    """
    Setter method for ldp_interface_hello_intl, mapped from YANG variable /mpls_state/ldp/interface/ldp_interface_data/ldp_interface_hello_intl (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_interface_hello_intl is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_interface_hello_intl() directly.

    YANG Description: ldp interface hello interval
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-interface-hello-intl", rest_name="ldp-interface-hello-intl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_interface_hello_intl must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-interface-hello-intl", rest_name="ldp-interface-hello-intl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__ldp_interface_hello_intl = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_interface_hello_intl(self):
    self.__ldp_interface_hello_intl = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-interface-hello-intl", rest_name="ldp-interface-hello-intl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_ldp_interface_hello_timeout(self):
    """
    Getter method for ldp_interface_hello_timeout, mapped from YANG variable /mpls_state/ldp/interface/ldp_interface_data/ldp_interface_hello_timeout (uint32)

    YANG Description: ldp interface hello timeout
    """
    return self.__ldp_interface_hello_timeout
      
  def _set_ldp_interface_hello_timeout(self, v, load=False):
    """
    Setter method for ldp_interface_hello_timeout, mapped from YANG variable /mpls_state/ldp/interface/ldp_interface_data/ldp_interface_hello_timeout (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_interface_hello_timeout is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_interface_hello_timeout() directly.

    YANG Description: ldp interface hello timeout
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-interface-hello-timeout", rest_name="ldp-interface-hello-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_interface_hello_timeout must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-interface-hello-timeout", rest_name="ldp-interface-hello-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__ldp_interface_hello_timeout = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_interface_hello_timeout(self):
    self.__ldp_interface_hello_timeout = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-interface-hello-timeout", rest_name="ldp-interface-hello-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_ldp_interface_hello_next(self):
    """
    Getter method for ldp_interface_hello_next, mapped from YANG variable /mpls_state/ldp/interface/ldp_interface_data/ldp_interface_hello_next (uint32)

    YANG Description: ldp interface hello next
    """
    return self.__ldp_interface_hello_next
      
  def _set_ldp_interface_hello_next(self, v, load=False):
    """
    Setter method for ldp_interface_hello_next, mapped from YANG variable /mpls_state/ldp/interface/ldp_interface_data/ldp_interface_hello_next (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_interface_hello_next is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_interface_hello_next() directly.

    YANG Description: ldp interface hello next
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-interface-hello-next", rest_name="ldp-interface-hello-next", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_interface_hello_next must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-interface-hello-next", rest_name="ldp-interface-hello-next", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__ldp_interface_hello_next = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_interface_hello_next(self):
    self.__ldp_interface_hello_next = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-interface-hello-next", rest_name="ldp-interface-hello-next", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)

  ldp_interface_name = __builtin__.property(_get_ldp_interface_name)
  ldp_interface_type = __builtin__.property(_get_ldp_interface_type)
  ldp_interface_lbpsp = __builtin__.property(_get_ldp_interface_lbpsp)
  ldp_interface_nbr_cnt = __builtin__.property(_get_ldp_interface_nbr_cnt)
  ldp_interface_hello_intl = __builtin__.property(_get_ldp_interface_hello_intl)
  ldp_interface_hello_timeout = __builtin__.property(_get_ldp_interface_hello_timeout)
  ldp_interface_hello_next = __builtin__.property(_get_ldp_interface_hello_next)


  _pyangbind_elements = {'ldp_interface_name': ldp_interface_name, 'ldp_interface_type': ldp_interface_type, 'ldp_interface_lbpsp': ldp_interface_lbpsp, 'ldp_interface_nbr_cnt': ldp_interface_nbr_cnt, 'ldp_interface_hello_intl': ldp_interface_hello_intl, 'ldp_interface_hello_timeout': ldp_interface_hello_timeout, 'ldp_interface_hello_next': ldp_interface_hello_next, }


