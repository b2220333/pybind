
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import protected_vlans
import enableInterfaceLevel
class openflow(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/ethernet/openflow. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__protected_vlans','__enableInterfaceLevel',)

  _yang_name = 'openflow'
  _rest_name = 'openflow'

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
    self.__enableInterfaceLevel = YANGDynClass(base=enableInterfaceLevel.enableInterfaceLevel, is_container='container', presence=False, yang_name="enableInterfaceLevel", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Config Openflow mode', u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)
    self.__protected_vlans = YANGDynClass(base=protected_vlans.protected_vlans, is_container='container', presence=False, yang_name="protected-vlans", rest_name="protected-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'protected vlan ', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)

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
      return [u'interface', u'ethernet', u'openflow']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ethernet', u'openflow']

  def _get_protected_vlans(self):
    """
    Getter method for protected_vlans, mapped from YANG variable /interface/ethernet/openflow/protected_vlans (container)
    """
    return self.__protected_vlans
      
  def _set_protected_vlans(self, v, load=False):
    """
    Setter method for protected_vlans, mapped from YANG variable /interface/ethernet/openflow/protected_vlans (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protected_vlans is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protected_vlans() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=protected_vlans.protected_vlans, is_container='container', presence=False, yang_name="protected-vlans", rest_name="protected-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'protected vlan ', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protected_vlans must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=protected_vlans.protected_vlans, is_container='container', presence=False, yang_name="protected-vlans", rest_name="protected-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'protected vlan ', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)""",
        })

    self.__protected_vlans = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protected_vlans(self):
    self.__protected_vlans = YANGDynClass(base=protected_vlans.protected_vlans, is_container='container', presence=False, yang_name="protected-vlans", rest_name="protected-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'protected vlan ', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)


  def _get_enableInterfaceLevel(self):
    """
    Getter method for enableInterfaceLevel, mapped from YANG variable /interface/ethernet/openflow/enableInterfaceLevel (container)
    """
    return self.__enableInterfaceLevel
      
  def _set_enableInterfaceLevel(self, v, load=False):
    """
    Setter method for enableInterfaceLevel, mapped from YANG variable /interface/ethernet/openflow/enableInterfaceLevel (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enableInterfaceLevel is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enableInterfaceLevel() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=enableInterfaceLevel.enableInterfaceLevel, is_container='container', presence=False, yang_name="enableInterfaceLevel", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Config Openflow mode', u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enableInterfaceLevel must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=enableInterfaceLevel.enableInterfaceLevel, is_container='container', presence=False, yang_name="enableInterfaceLevel", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Config Openflow mode', u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)""",
        })

    self.__enableInterfaceLevel = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enableInterfaceLevel(self):
    self.__enableInterfaceLevel = YANGDynClass(base=enableInterfaceLevel.enableInterfaceLevel, is_container='container', presence=False, yang_name="enableInterfaceLevel", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Config Openflow mode', u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='container', is_config=True)

  protected_vlans = __builtin__.property(_get_protected_vlans, _set_protected_vlans)
  enableInterfaceLevel = __builtin__.property(_get_enableInterfaceLevel, _set_enableInterfaceLevel)


  _pyangbind_elements = {'protected_vlans': protected_vlans, 'enableInterfaceLevel': enableInterfaceLevel, }


