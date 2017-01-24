
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import routing_parameter
class predefined(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/hardware-profile/route-table/predefined. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__routing_profiletype','__routing_parameter',)

  _yang_name = 'predefined'
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
    self.__routing_parameter = YANGDynClass(base=routing_parameter.routing_parameter, is_container='container', presence=False, yang_name="routing_parameter", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    self.__routing_profiletype = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ipv4-min-v6': {'value': 3}, u'ipv6-max-route': {'value': 4}, u'default': {'value': 0}, u'ipv4-max-arp': {'value': 2}, u'ipv4-max-route': {'value': 1}, u'ipv6-max-nd': {'value': 5}},), is_leaf=True, yang_name="routing_profiletype", rest_name="routing_profiletype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='routing-profile-subtype', is_config=True)

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
      return [u'rbridge-id', u'hardware-profile', u'route-table', u'predefined']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'hardware-profile', u'route-table']

  def _get_routing_profiletype(self):
    """
    Getter method for routing_profiletype, mapped from YANG variable /rbridge_id/hardware_profile/route_table/predefined/routing_profiletype (routing-profile-subtype)
    """
    return self.__routing_profiletype
      
  def _set_routing_profiletype(self, v, load=False):
    """
    Setter method for routing_profiletype, mapped from YANG variable /rbridge_id/hardware_profile/route_table/predefined/routing_profiletype (routing-profile-subtype)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_routing_profiletype is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_routing_profiletype() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ipv4-min-v6': {'value': 3}, u'ipv6-max-route': {'value': 4}, u'default': {'value': 0}, u'ipv4-max-arp': {'value': 2}, u'ipv4-max-route': {'value': 1}, u'ipv6-max-nd': {'value': 5}},), is_leaf=True, yang_name="routing_profiletype", rest_name="routing_profiletype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='routing-profile-subtype', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """routing_profiletype must be of a type compatible with routing-profile-subtype""",
          'defined-type': "brocade-hardware:routing-profile-subtype",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ipv4-min-v6': {'value': 3}, u'ipv6-max-route': {'value': 4}, u'default': {'value': 0}, u'ipv4-max-arp': {'value': 2}, u'ipv4-max-route': {'value': 1}, u'ipv6-max-nd': {'value': 5}},), is_leaf=True, yang_name="routing_profiletype", rest_name="routing_profiletype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='routing-profile-subtype', is_config=True)""",
        })

    self.__routing_profiletype = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_routing_profiletype(self):
    self.__routing_profiletype = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ipv4-min-v6': {'value': 3}, u'ipv6-max-route': {'value': 4}, u'default': {'value': 0}, u'ipv4-max-arp': {'value': 2}, u'ipv4-max-route': {'value': 1}, u'ipv6-max-nd': {'value': 5}},), is_leaf=True, yang_name="routing_profiletype", rest_name="routing_profiletype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='routing-profile-subtype', is_config=True)


  def _get_routing_parameter(self):
    """
    Getter method for routing_parameter, mapped from YANG variable /rbridge_id/hardware_profile/route_table/predefined/routing_parameter (container)
    """
    return self.__routing_parameter
      
  def _set_routing_parameter(self, v, load=False):
    """
    Setter method for routing_parameter, mapped from YANG variable /rbridge_id/hardware_profile/route_table/predefined/routing_parameter (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_routing_parameter is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_routing_parameter() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=routing_parameter.routing_parameter, is_container='container', presence=False, yang_name="routing_parameter", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """routing_parameter must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=routing_parameter.routing_parameter, is_container='container', presence=False, yang_name="routing_parameter", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)""",
        })

    self.__routing_parameter = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_routing_parameter(self):
    self.__routing_parameter = YANGDynClass(base=routing_parameter.routing_parameter, is_container='container', presence=False, yang_name="routing_parameter", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)

  routing_profiletype = __builtin__.property(_get_routing_profiletype, _set_routing_profiletype)
  routing_parameter = __builtin__.property(_get_routing_parameter, _set_routing_parameter)


  _pyangbind_elements = {'routing_profiletype': routing_profiletype, 'routing_parameter': routing_parameter, }


