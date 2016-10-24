
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import vc
import key
class ldp_fec_vcs(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/ldp/fec/ldp-fec-vcs. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: 
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__tot_no_of_vc_fec','__tot_no_of_vc_fec_installed','__vc','__key',)

  _yang_name = 'ldp-fec-vcs'
  _rest_name = 'ldp-fec-vcs'

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
    self.__vc = YANGDynClass(base=YANGListType("peer_id",vc.vc, yang_name="vc", rest_name="vc", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='peer-id', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-vc', u'cli-suppress-show-path': None}}), is_container='list', yang_name="vc", rest_name="vc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-vc', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    self.__tot_no_of_vc_fec = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tot-no-of-vc-fec", rest_name="tot-no-of-vc-fec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__tot_no_of_vc_fec_installed = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tot-no-of-vc-fec-installed", rest_name="tot-no-of-vc-fec-installed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__key = YANGDynClass(base=key.key, is_container='container', yang_name="key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-key-key-3'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)

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
      return [u'mpls-state', u'ldp', u'fec', u'ldp-fec-vcs']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'ldp', u'fec', u'ldp-fec-vcs']

  def _get_tot_no_of_vc_fec(self):
    """
    Getter method for tot_no_of_vc_fec, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_vcs/tot_no_of_vc_fec (uint32)

    YANG Description: tot_no_of_vc_fec
    """
    return self.__tot_no_of_vc_fec
      
  def _set_tot_no_of_vc_fec(self, v, load=False):
    """
    Setter method for tot_no_of_vc_fec, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_vcs/tot_no_of_vc_fec (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tot_no_of_vc_fec is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tot_no_of_vc_fec() directly.

    YANG Description: tot_no_of_vc_fec
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tot-no-of-vc-fec", rest_name="tot-no-of-vc-fec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tot_no_of_vc_fec must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tot-no-of-vc-fec", rest_name="tot-no-of-vc-fec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__tot_no_of_vc_fec = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tot_no_of_vc_fec(self):
    self.__tot_no_of_vc_fec = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tot-no-of-vc-fec", rest_name="tot-no-of-vc-fec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_tot_no_of_vc_fec_installed(self):
    """
    Getter method for tot_no_of_vc_fec_installed, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_vcs/tot_no_of_vc_fec_installed (uint32)

    YANG Description: tot_no_of_vc_fec_installed
    """
    return self.__tot_no_of_vc_fec_installed
      
  def _set_tot_no_of_vc_fec_installed(self, v, load=False):
    """
    Setter method for tot_no_of_vc_fec_installed, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_vcs/tot_no_of_vc_fec_installed (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tot_no_of_vc_fec_installed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tot_no_of_vc_fec_installed() directly.

    YANG Description: tot_no_of_vc_fec_installed
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tot-no-of-vc-fec-installed", rest_name="tot-no-of-vc-fec-installed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tot_no_of_vc_fec_installed must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tot-no-of-vc-fec-installed", rest_name="tot-no-of-vc-fec-installed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__tot_no_of_vc_fec_installed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tot_no_of_vc_fec_installed(self):
    self.__tot_no_of_vc_fec_installed = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tot-no-of-vc-fec-installed", rest_name="tot-no-of-vc-fec-installed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_vc(self):
    """
    Getter method for vc, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_vcs/vc (list)
    """
    return self.__vc
      
  def _set_vc(self, v, load=False):
    """
    Setter method for vc, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_vcs/vc (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vc is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vc() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("peer_id",vc.vc, yang_name="vc", rest_name="vc", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='peer-id', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-vc', u'cli-suppress-show-path': None}}), is_container='list', yang_name="vc", rest_name="vc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-vc', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vc must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("peer_id",vc.vc, yang_name="vc", rest_name="vc", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='peer-id', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-vc', u'cli-suppress-show-path': None}}), is_container='list', yang_name="vc", rest_name="vc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-vc', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)""",
        })

    self.__vc = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vc(self):
    self.__vc = YANGDynClass(base=YANGListType("peer_id",vc.vc, yang_name="vc", rest_name="vc", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='peer-id', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-vc', u'cli-suppress-show-path': None}}), is_container='list', yang_name="vc", rest_name="vc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-vc', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)


  def _get_key(self):
    """
    Getter method for key, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_vcs/key (container)
    """
    return self.__key
      
  def _set_key(self, v, load=False):
    """
    Setter method for key, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_vcs/key (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_key is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_key() directly.
    """
    try:
      t = YANGDynClass(v,base=key.key, is_container='container', yang_name="key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-key-key-3'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """key must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=key.key, is_container='container', yang_name="key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-key-key-3'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)""",
        })

    self.__key = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_key(self):
    self.__key = YANGDynClass(base=key.key, is_container='container', yang_name="key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-key-key-3'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)

  tot_no_of_vc_fec = __builtin__.property(_get_tot_no_of_vc_fec)
  tot_no_of_vc_fec_installed = __builtin__.property(_get_tot_no_of_vc_fec_installed)
  vc = __builtin__.property(_get_vc)
  key = __builtin__.property(_get_key)


  _pyangbind_elements = {'tot_no_of_vc_fec': tot_no_of_vc_fec, 'tot_no_of_vc_fec_installed': tot_no_of_vc_fec_installed, 'vc': vc, 'key': key, }


