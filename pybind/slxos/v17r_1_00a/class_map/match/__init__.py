
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import access_group
import vlan
import bridge_domain
class match(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-mqc - based on the path /class-map/match. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__access_group','__vlan','__bridge_domain',)

  _yang_name = 'match'
  _rest_name = 'match'

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
    self.__bridge_domain = YANGDynClass(base=bridge_domain.bridge_domain, is_container='container', presence=False, yang_name="bridge-domain", rest_name="bridge-domain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Configure Bridge-domain Id', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    self.__vlan = YANGDynClass(base=vlan.vlan, is_container='container', presence=False, yang_name="vlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Configure VLAN Id', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    self.__access_group = YANGDynClass(base=access_group.access_group, is_container='container', presence=False, yang_name="access-group", rest_name="access-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Configure MAC/IP Access group', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)

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
      return [u'class-map', u'match']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'class-map', u'match']

  def _get_access_group(self):
    """
    Getter method for access_group, mapped from YANG variable /class_map/match/access_group (container)

    YANG Description: This provides the grouping of configuration
elements of MAC/IP access list.
    """
    return self.__access_group
      
  def _set_access_group(self, v, load=False):
    """
    Setter method for access_group, mapped from YANG variable /class_map/match/access_group (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_access_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_access_group() directly.

    YANG Description: This provides the grouping of configuration
elements of MAC/IP access list.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=access_group.access_group, is_container='container', presence=False, yang_name="access-group", rest_name="access-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Configure MAC/IP Access group', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """access_group must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=access_group.access_group, is_container='container', presence=False, yang_name="access-group", rest_name="access-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Configure MAC/IP Access group', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)""",
        })

    self.__access_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_access_group(self):
    self.__access_group = YANGDynClass(base=access_group.access_group, is_container='container', presence=False, yang_name="access-group", rest_name="access-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Configure MAC/IP Access group', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)


  def _get_vlan(self):
    """
    Getter method for vlan, mapped from YANG variable /class_map/match/vlan (container)
    """
    return self.__vlan
      
  def _set_vlan(self, v, load=False):
    """
    Setter method for vlan, mapped from YANG variable /class_map/match/vlan (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=vlan.vlan, is_container='container', presence=False, yang_name="vlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Configure VLAN Id', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=vlan.vlan, is_container='container', presence=False, yang_name="vlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Configure VLAN Id', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)""",
        })

    self.__vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan(self):
    self.__vlan = YANGDynClass(base=vlan.vlan, is_container='container', presence=False, yang_name="vlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Configure VLAN Id', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)


  def _get_bridge_domain(self):
    """
    Getter method for bridge_domain, mapped from YANG variable /class_map/match/bridge_domain (container)
    """
    return self.__bridge_domain
      
  def _set_bridge_domain(self, v, load=False):
    """
    Setter method for bridge_domain, mapped from YANG variable /class_map/match/bridge_domain (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bridge_domain is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bridge_domain() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=bridge_domain.bridge_domain, is_container='container', presence=False, yang_name="bridge-domain", rest_name="bridge-domain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Configure Bridge-domain Id', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bridge_domain must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=bridge_domain.bridge_domain, is_container='container', presence=False, yang_name="bridge-domain", rest_name="bridge-domain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Configure Bridge-domain Id', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)""",
        })

    self.__bridge_domain = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bridge_domain(self):
    self.__bridge_domain = YANGDynClass(base=bridge_domain.bridge_domain, is_container='container', presence=False, yang_name="bridge-domain", rest_name="bridge-domain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Configure Bridge-domain Id', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)

  access_group = __builtin__.property(_get_access_group, _set_access_group)
  vlan = __builtin__.property(_get_vlan, _set_vlan)
  bridge_domain = __builtin__.property(_get_bridge_domain, _set_bridge_domain)


  _pyangbind_elements = {'access_group': access_group, 'vlan': vlan, 'bridge_domain': bridge_domain, }


