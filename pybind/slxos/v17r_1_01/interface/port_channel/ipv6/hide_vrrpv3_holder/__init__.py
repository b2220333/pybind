
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import vrrpv3
import vrrpv3e
class hide_vrrpv3_holder(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/port-channel/ipv6/hide-vrrpv3-holder. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vrrpv3','__vrrpv3e',)

  _yang_name = 'hide-vrrpv3-holder'
  _rest_name = ''

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
    self.__vrrpv3 = YANGDynClass(base=YANGListType("vrid",vrrpv3.vrrpv3, yang_name="vrrpv3", rest_name="vrrp-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vrid', extensions={u'tailf-common': {u'info': u'Start VRRP configuration', u'cli-no-key-completion': None, u'alt-name': u'vrrp-group', u'sort-priority': u'137', u'cli-suppress-list-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'vrrpv3SessionPo'}}), is_container='list', yang_name="vrrpv3", rest_name="vrrp-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Start VRRP configuration', u'cli-no-key-completion': None, u'alt-name': u'vrrp-group', u'sort-priority': u'137', u'cli-suppress-list-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'vrrpv3SessionPo'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='list', is_config=True)
    self.__vrrpv3e = YANGDynClass(base=YANGListType("vrid",vrrpv3e.vrrpv3e, yang_name="vrrpv3e", rest_name="vrrp-extended-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vrid', extensions={u'tailf-common': {u'info': u'Start VRRPE configuration', u'cli-no-key-completion': None, u'alt-name': u'vrrp-extended-group', u'sort-priority': u'138', u'cli-suppress-list-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'vrrpv3eSessionPointf'}}), is_container='list', yang_name="vrrpv3e", rest_name="vrrp-extended-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Start VRRPE configuration', u'cli-no-key-completion': None, u'alt-name': u'vrrp-extended-group', u'sort-priority': u'138', u'cli-suppress-list-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'vrrpv3eSessionPointf'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='list', is_config=True)

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
      return [u'interface', u'port-channel', u'ipv6', u'hide-vrrpv3-holder']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Port-channel', u'ipv6']

  def _get_vrrpv3(self):
    """
    Getter method for vrrpv3, mapped from YANG variable /interface/port_channel/ipv6/hide_vrrpv3_holder/vrrpv3 (list)
    """
    return self.__vrrpv3
      
  def _set_vrrpv3(self, v, load=False):
    """
    Setter method for vrrpv3, mapped from YANG variable /interface/port_channel/ipv6/hide_vrrpv3_holder/vrrpv3 (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vrrpv3 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vrrpv3() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("vrid",vrrpv3.vrrpv3, yang_name="vrrpv3", rest_name="vrrp-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vrid', extensions={u'tailf-common': {u'info': u'Start VRRP configuration', u'cli-no-key-completion': None, u'alt-name': u'vrrp-group', u'sort-priority': u'137', u'cli-suppress-list-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'vrrpv3SessionPo'}}), is_container='list', yang_name="vrrpv3", rest_name="vrrp-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Start VRRP configuration', u'cli-no-key-completion': None, u'alt-name': u'vrrp-group', u'sort-priority': u'137', u'cli-suppress-list-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'vrrpv3SessionPo'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vrrpv3 must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vrid",vrrpv3.vrrpv3, yang_name="vrrpv3", rest_name="vrrp-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vrid', extensions={u'tailf-common': {u'info': u'Start VRRP configuration', u'cli-no-key-completion': None, u'alt-name': u'vrrp-group', u'sort-priority': u'137', u'cli-suppress-list-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'vrrpv3SessionPo'}}), is_container='list', yang_name="vrrpv3", rest_name="vrrp-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Start VRRP configuration', u'cli-no-key-completion': None, u'alt-name': u'vrrp-group', u'sort-priority': u'137', u'cli-suppress-list-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'vrrpv3SessionPo'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='list', is_config=True)""",
        })

    self.__vrrpv3 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vrrpv3(self):
    self.__vrrpv3 = YANGDynClass(base=YANGListType("vrid",vrrpv3.vrrpv3, yang_name="vrrpv3", rest_name="vrrp-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vrid', extensions={u'tailf-common': {u'info': u'Start VRRP configuration', u'cli-no-key-completion': None, u'alt-name': u'vrrp-group', u'sort-priority': u'137', u'cli-suppress-list-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'vrrpv3SessionPo'}}), is_container='list', yang_name="vrrpv3", rest_name="vrrp-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Start VRRP configuration', u'cli-no-key-completion': None, u'alt-name': u'vrrp-group', u'sort-priority': u'137', u'cli-suppress-list-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'vrrpv3SessionPo'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='list', is_config=True)


  def _get_vrrpv3e(self):
    """
    Getter method for vrrpv3e, mapped from YANG variable /interface/port_channel/ipv6/hide_vrrpv3_holder/vrrpv3e (list)
    """
    return self.__vrrpv3e
      
  def _set_vrrpv3e(self, v, load=False):
    """
    Setter method for vrrpv3e, mapped from YANG variable /interface/port_channel/ipv6/hide_vrrpv3_holder/vrrpv3e (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vrrpv3e is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vrrpv3e() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("vrid",vrrpv3e.vrrpv3e, yang_name="vrrpv3e", rest_name="vrrp-extended-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vrid', extensions={u'tailf-common': {u'info': u'Start VRRPE configuration', u'cli-no-key-completion': None, u'alt-name': u'vrrp-extended-group', u'sort-priority': u'138', u'cli-suppress-list-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'vrrpv3eSessionPointf'}}), is_container='list', yang_name="vrrpv3e", rest_name="vrrp-extended-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Start VRRPE configuration', u'cli-no-key-completion': None, u'alt-name': u'vrrp-extended-group', u'sort-priority': u'138', u'cli-suppress-list-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'vrrpv3eSessionPointf'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vrrpv3e must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vrid",vrrpv3e.vrrpv3e, yang_name="vrrpv3e", rest_name="vrrp-extended-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vrid', extensions={u'tailf-common': {u'info': u'Start VRRPE configuration', u'cli-no-key-completion': None, u'alt-name': u'vrrp-extended-group', u'sort-priority': u'138', u'cli-suppress-list-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'vrrpv3eSessionPointf'}}), is_container='list', yang_name="vrrpv3e", rest_name="vrrp-extended-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Start VRRPE configuration', u'cli-no-key-completion': None, u'alt-name': u'vrrp-extended-group', u'sort-priority': u'138', u'cli-suppress-list-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'vrrpv3eSessionPointf'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='list', is_config=True)""",
        })

    self.__vrrpv3e = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vrrpv3e(self):
    self.__vrrpv3e = YANGDynClass(base=YANGListType("vrid",vrrpv3e.vrrpv3e, yang_name="vrrpv3e", rest_name="vrrp-extended-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vrid', extensions={u'tailf-common': {u'info': u'Start VRRPE configuration', u'cli-no-key-completion': None, u'alt-name': u'vrrp-extended-group', u'sort-priority': u'138', u'cli-suppress-list-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'vrrpv3eSessionPointf'}}), is_container='list', yang_name="vrrpv3e", rest_name="vrrp-extended-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Start VRRPE configuration', u'cli-no-key-completion': None, u'alt-name': u'vrrp-extended-group', u'sort-priority': u'138', u'cli-suppress-list-no': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'vrrpv3eSessionPointf'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='list', is_config=True)

  vrrpv3 = __builtin__.property(_get_vrrpv3, _set_vrrpv3)
  vrrpv3e = __builtin__.property(_get_vrrpv3e, _set_vrrpv3e)


  _pyangbind_elements = {'vrrpv3': vrrpv3, 'vrrpv3e': vrrpv3e, }


