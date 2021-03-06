
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import stp
import rstp
import mstp
import pvstp
import rpvstp
class spanning_tree_info(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-xstp-ext - based on the path /brocade_xstp_ext_rpc/get-stp-brief-info/output/spanning-tree-info. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__stp_mode','__stp','__rstp','__mstp','__pvstp','__rpvstp',)

  _yang_name = 'spanning-tree-info'
  _rest_name = 'spanning-tree-info'

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
    self.__rstp = YANGDynClass(base=rstp.rstp, is_container='container', presence=False, yang_name="rstp", rest_name="rstp", parent=self, choice=(u'spanning-tree-mode', u'rstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)
    self.__mstp = YANGDynClass(base=mstp.mstp, is_container='container', presence=False, yang_name="mstp", rest_name="mstp", parent=self, choice=(u'spanning-tree-mode', u'mstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)
    self.__rpvstp = YANGDynClass(base=YANGListType("vlan_id",rpvstp.rpvstp, yang_name="rpvstp", rest_name="rpvstp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions=None, choice=False), is_container='list', yang_name="rpvstp", rest_name="rpvstp", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='list', is_config=True)
    self.__stp_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {'value': 1}, u'rstp': {'value': 3}, u'mstp': {'value': 4}, u'rpvstp': {'value': 6}, u'pvstp': {'value': 5}, u'stp': {'value': 2}},), is_leaf=True, yang_name="stp-mode", rest_name="stp-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='stp-type', is_config=True)
    self.__pvstp = YANGDynClass(base=YANGListType("vlan_id",pvstp.pvstp, yang_name="pvstp", rest_name="pvstp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions=None, choice=False), is_container='list', yang_name="pvstp", rest_name="pvstp", parent=self, choice=(u'spanning-tree-mode', u'pvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='list', is_config=True)
    self.__stp = YANGDynClass(base=stp.stp, is_container='container', presence=False, yang_name="stp", rest_name="stp", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)

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
      return [u'brocade_xstp_ext_rpc', u'get-stp-brief-info', u'output', u'spanning-tree-info']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-stp-brief-info', u'output', u'spanning-tree-info']

  def _get_stp_mode(self):
    """
    Getter method for stp_mode, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/stp_mode (stp-type)

    YANG Description: Type of the spanning tree protocol configured
on this switch
    """
    return self.__stp_mode
      
  def _set_stp_mode(self, v, load=False):
    """
    Setter method for stp_mode, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/stp_mode (stp-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_stp_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_stp_mode() directly.

    YANG Description: Type of the spanning tree protocol configured
on this switch
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {'value': 1}, u'rstp': {'value': 3}, u'mstp': {'value': 4}, u'rpvstp': {'value': 6}, u'pvstp': {'value': 5}, u'stp': {'value': 2}},), is_leaf=True, yang_name="stp-mode", rest_name="stp-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='stp-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """stp_mode must be of a type compatible with stp-type""",
          'defined-type': "brocade-xstp-ext:stp-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {'value': 1}, u'rstp': {'value': 3}, u'mstp': {'value': 4}, u'rpvstp': {'value': 6}, u'pvstp': {'value': 5}, u'stp': {'value': 2}},), is_leaf=True, yang_name="stp-mode", rest_name="stp-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='stp-type', is_config=True)""",
        })

    self.__stp_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_stp_mode(self):
    self.__stp_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {'value': 1}, u'rstp': {'value': 3}, u'mstp': {'value': 4}, u'rpvstp': {'value': 6}, u'pvstp': {'value': 5}, u'stp': {'value': 2}},), is_leaf=True, yang_name="stp-mode", rest_name="stp-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='stp-type', is_config=True)


  def _get_stp(self):
    """
    Getter method for stp, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/stp (container)
    """
    return self.__stp
      
  def _set_stp(self, v, load=False):
    """
    Setter method for stp, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/stp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_stp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_stp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=stp.stp, is_container='container', presence=False, yang_name="stp", rest_name="stp", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """stp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=stp.stp, is_container='container', presence=False, yang_name="stp", rest_name="stp", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)""",
        })

    self.__stp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_stp(self):
    self.__stp = YANGDynClass(base=stp.stp, is_container='container', presence=False, yang_name="stp", rest_name="stp", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)


  def _get_rstp(self):
    """
    Getter method for rstp, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/rstp (container)
    """
    return self.__rstp
      
  def _set_rstp(self, v, load=False):
    """
    Setter method for rstp, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/rstp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rstp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rstp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=rstp.rstp, is_container='container', presence=False, yang_name="rstp", rest_name="rstp", parent=self, choice=(u'spanning-tree-mode', u'rstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rstp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=rstp.rstp, is_container='container', presence=False, yang_name="rstp", rest_name="rstp", parent=self, choice=(u'spanning-tree-mode', u'rstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)""",
        })

    self.__rstp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rstp(self):
    self.__rstp = YANGDynClass(base=rstp.rstp, is_container='container', presence=False, yang_name="rstp", rest_name="rstp", parent=self, choice=(u'spanning-tree-mode', u'rstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)


  def _get_mstp(self):
    """
    Getter method for mstp, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/mstp (container)

    YANG Description: CIST information
    """
    return self.__mstp
      
  def _set_mstp(self, v, load=False):
    """
    Setter method for mstp, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/mstp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mstp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mstp() directly.

    YANG Description: CIST information
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=mstp.mstp, is_container='container', presence=False, yang_name="mstp", rest_name="mstp", parent=self, choice=(u'spanning-tree-mode', u'mstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mstp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=mstp.mstp, is_container='container', presence=False, yang_name="mstp", rest_name="mstp", parent=self, choice=(u'spanning-tree-mode', u'mstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)""",
        })

    self.__mstp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mstp(self):
    self.__mstp = YANGDynClass(base=mstp.mstp, is_container='container', presence=False, yang_name="mstp", rest_name="mstp", parent=self, choice=(u'spanning-tree-mode', u'mstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)


  def _get_pvstp(self):
    """
    Getter method for pvstp, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/pvstp (list)

    YANG Description: PVST instance information
    """
    return self.__pvstp
      
  def _set_pvstp(self, v, load=False):
    """
    Setter method for pvstp, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/pvstp (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pvstp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pvstp() directly.

    YANG Description: PVST instance information
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("vlan_id",pvstp.pvstp, yang_name="pvstp", rest_name="pvstp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions=None, choice=False), is_container='list', yang_name="pvstp", rest_name="pvstp", parent=self, choice=(u'spanning-tree-mode', u'pvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pvstp must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vlan_id",pvstp.pvstp, yang_name="pvstp", rest_name="pvstp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions=None, choice=False), is_container='list', yang_name="pvstp", rest_name="pvstp", parent=self, choice=(u'spanning-tree-mode', u'pvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='list', is_config=True)""",
        })

    self.__pvstp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pvstp(self):
    self.__pvstp = YANGDynClass(base=YANGListType("vlan_id",pvstp.pvstp, yang_name="pvstp", rest_name="pvstp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions=None, choice=False), is_container='list', yang_name="pvstp", rest_name="pvstp", parent=self, choice=(u'spanning-tree-mode', u'pvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='list', is_config=True)


  def _get_rpvstp(self):
    """
    Getter method for rpvstp, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/rpvstp (list)

    YANG Description: RPVST instance information
    """
    return self.__rpvstp
      
  def _set_rpvstp(self, v, load=False):
    """
    Setter method for rpvstp, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/rpvstp (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rpvstp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rpvstp() directly.

    YANG Description: RPVST instance information
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("vlan_id",rpvstp.rpvstp, yang_name="rpvstp", rest_name="rpvstp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions=None, choice=False), is_container='list', yang_name="rpvstp", rest_name="rpvstp", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rpvstp must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vlan_id",rpvstp.rpvstp, yang_name="rpvstp", rest_name="rpvstp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions=None, choice=False), is_container='list', yang_name="rpvstp", rest_name="rpvstp", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='list', is_config=True)""",
        })

    self.__rpvstp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rpvstp(self):
    self.__rpvstp = YANGDynClass(base=YANGListType("vlan_id",rpvstp.rpvstp, yang_name="rpvstp", rest_name="rpvstp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions=None, choice=False), is_container='list', yang_name="rpvstp", rest_name="rpvstp", parent=self, choice=(u'spanning-tree-mode', u'rpvstp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='list', is_config=True)

  stp_mode = __builtin__.property(_get_stp_mode, _set_stp_mode)
  stp = __builtin__.property(_get_stp, _set_stp)
  rstp = __builtin__.property(_get_rstp, _set_rstp)
  mstp = __builtin__.property(_get_mstp, _set_mstp)
  pvstp = __builtin__.property(_get_pvstp, _set_pvstp)
  rpvstp = __builtin__.property(_get_rpvstp, _set_rpvstp)

  __choices__ = {u'spanning-tree-mode': {u'pvstp': [u'pvstp'], u'mstp': [u'mstp'], u'stp': [u'stp'], u'rstp': [u'rstp'], u'rpvstp': [u'rpvstp']}}
  _pyangbind_elements = {'stp_mode': stp_mode, 'stp': stp, 'rstp': rstp, 'mstp': mstp, 'pvstp': pvstp, 'rpvstp': rpvstp, }


