
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ve(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-tunnels - based on the path /overlay-gateway/ip/interface/ve. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ve_id','__vrrp_extended_group',)

  _yang_name = 've'
  _rest_name = 'Ve'

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
    self.__ve_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="ve-id", rest_name="ve-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='intf:ve-type', is_config=True)
    self.__vrrp_extended_group = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="vrrp-extended-group", rest_name="vrrp-extended-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-optional-in-sequence': None, u'info': u'VRRP-E group id'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='vrrp:vrid-type', is_config=True)

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
      return [u'overlay-gateway', u'ip', u'interface', u've']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'overlay-gateway', u'ip', u'interface', u'Ve']

  def _get_ve_id(self):
    """
    Getter method for ve_id, mapped from YANG variable /overlay_gateway/ip/interface/ve/ve_id (intf:ve-type)
    """
    return self.__ve_id
      
  def _set_ve_id(self, v, load=False):
    """
    Setter method for ve_id, mapped from YANG variable /overlay_gateway/ip/interface/ve/ve_id (intf:ve-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ve_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ve_id() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="ve-id", rest_name="ve-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='intf:ve-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ve_id must be of a type compatible with intf:ve-type""",
          'defined-type': "intf:ve-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="ve-id", rest_name="ve-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='intf:ve-type', is_config=True)""",
        })

    self.__ve_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ve_id(self):
    self.__ve_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="ve-id", rest_name="ve-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='intf:ve-type', is_config=True)


  def _get_vrrp_extended_group(self):
    """
    Getter method for vrrp_extended_group, mapped from YANG variable /overlay_gateway/ip/interface/ve/vrrp_extended_group (vrrp:vrid-type)
    """
    return self.__vrrp_extended_group
      
  def _set_vrrp_extended_group(self, v, load=False):
    """
    Setter method for vrrp_extended_group, mapped from YANG variable /overlay_gateway/ip/interface/ve/vrrp_extended_group (vrrp:vrid-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vrrp_extended_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vrrp_extended_group() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="vrrp-extended-group", rest_name="vrrp-extended-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-optional-in-sequence': None, u'info': u'VRRP-E group id'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='vrrp:vrid-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vrrp_extended_group must be of a type compatible with vrrp:vrid-type""",
          'defined-type': "vrrp:vrid-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="vrrp-extended-group", rest_name="vrrp-extended-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-optional-in-sequence': None, u'info': u'VRRP-E group id'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='vrrp:vrid-type', is_config=True)""",
        })

    self.__vrrp_extended_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vrrp_extended_group(self):
    self.__vrrp_extended_group = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="vrrp-extended-group", rest_name="vrrp-extended-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-optional-in-sequence': None, u'info': u'VRRP-E group id'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='vrrp:vrid-type', is_config=True)

  ve_id = __builtin__.property(_get_ve_id, _set_ve_id)
  vrrp_extended_group = __builtin__.property(_get_vrrp_extended_group, _set_vrrp_extended_group)


  _pyangbind_elements = {'ve_id': ve_id, 'vrrp_extended_group': vrrp_extended_group, }


