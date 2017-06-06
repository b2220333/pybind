
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class static(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-tunnels - based on the path /overlay-gateway/site/static. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Site Static MAC address configuration
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mac_address','__vni_num',)

  _yang_name = 'static'
  _rest_name = 'static'

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
    self.__vni_num = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16777215']}), is_leaf=True, yang_name="vni-num", rest_name="vni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify the VNI number for the Static MAC', u'cli-full-command': None, u'alt-name': u'vni', u'cli-expose-key-name': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='vni-num-type', is_config=True)
    self.__mac_address = YANGDynClass(base=unicode, is_leaf=True, yang_name="mac-address", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specifify the Static MAC for the site', u'alt-name': u'mac', u'cli-expose-key-name': None, u'cli-incomplete-command': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='mac-access-list:mac-address-type', is_config=True)

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
      return [u'overlay-gateway', u'site', u'static']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'overlay-gateway', u'site', u'static']

  def _get_mac_address(self):
    """
    Getter method for mac_address, mapped from YANG variable /overlay_gateway/site/static/mac_address (mac-access-list:mac-address-type)
    """
    return self.__mac_address
      
  def _set_mac_address(self, v, load=False):
    """
    Setter method for mac_address, mapped from YANG variable /overlay_gateway/site/static/mac_address (mac-access-list:mac-address-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_address() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mac-address", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specifify the Static MAC for the site', u'alt-name': u'mac', u'cli-expose-key-name': None, u'cli-incomplete-command': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='mac-access-list:mac-address-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_address must be of a type compatible with mac-access-list:mac-address-type""",
          'defined-type': "mac-access-list:mac-address-type",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mac-address", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specifify the Static MAC for the site', u'alt-name': u'mac', u'cli-expose-key-name': None, u'cli-incomplete-command': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='mac-access-list:mac-address-type', is_config=True)""",
        })

    self.__mac_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_address(self):
    self.__mac_address = YANGDynClass(base=unicode, is_leaf=True, yang_name="mac-address", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specifify the Static MAC for the site', u'alt-name': u'mac', u'cli-expose-key-name': None, u'cli-incomplete-command': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='mac-access-list:mac-address-type', is_config=True)


  def _get_vni_num(self):
    """
    Getter method for vni_num, mapped from YANG variable /overlay_gateway/site/static/vni_num (vni-num-type)
    """
    return self.__vni_num
      
  def _set_vni_num(self, v, load=False):
    """
    Setter method for vni_num, mapped from YANG variable /overlay_gateway/site/static/vni_num (vni-num-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vni_num is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vni_num() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16777215']}), is_leaf=True, yang_name="vni-num", rest_name="vni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify the VNI number for the Static MAC', u'cli-full-command': None, u'alt-name': u'vni', u'cli-expose-key-name': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='vni-num-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vni_num must be of a type compatible with vni-num-type""",
          'defined-type': "brocade-tunnels:vni-num-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16777215']}), is_leaf=True, yang_name="vni-num", rest_name="vni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify the VNI number for the Static MAC', u'cli-full-command': None, u'alt-name': u'vni', u'cli-expose-key-name': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='vni-num-type', is_config=True)""",
        })

    self.__vni_num = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vni_num(self):
    self.__vni_num = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16777215']}), is_leaf=True, yang_name="vni-num", rest_name="vni", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify the VNI number for the Static MAC', u'cli-full-command': None, u'alt-name': u'vni', u'cli-expose-key-name': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='vni-num-type', is_config=True)

  mac_address = __builtin__.property(_get_mac_address, _set_mac_address)
  vni_num = __builtin__.property(_get_vni_num, _set_vni_num)


  _pyangbind_elements = {'mac_address': mac_address, 'vni_num': vni_num, }


