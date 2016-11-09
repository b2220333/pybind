
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import mode
import access
import access_mac_vlan_classification
import access_mac_group_vlan_classification
import trunk
class switchport(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-port-profile - based on the path /port-profile/vlan-profile/switchport. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This provides the grouping of all Switching character 
configuration elements of Layer 2 interface.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mode','__access','__access_mac_vlan_classification','__access_mac_group_vlan_classification','__trunk',)

  _yang_name = 'switchport'
  _rest_name = 'switchport'

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
    self.__access = YANGDynClass(base=access.access, is_container='container', yang_name="access", rest_name="access", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as Access', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    self.__access_mac_group_vlan_classification = YANGDynClass(base=access_mac_group_vlan_classification.access_mac_group_vlan_classification, is_container='container', yang_name="access-mac-group-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'ampp-macgroup-based-vlan-classification'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    self.__trunk = YANGDynClass(base=trunk.trunk, is_container='container', yang_name="trunk", rest_name="trunk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as trunk', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    self.__mode = YANGDynClass(base=mode.mode, is_container='container', yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set mode of the Layer2 interface', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    self.__access_mac_vlan_classification = YANGDynClass(base=access_mac_vlan_classification.access_mac_vlan_classification, is_container='container', yang_name="access-mac-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'ampp-mac-based-vlan-classification'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)

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
      return [u'port-profile', u'vlan-profile', u'switchport']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'port-profile', u'vlan-profile', u'switchport']

  def _get_mode(self):
    """
    Getter method for mode, mapped from YANG variable /port_profile/vlan_profile/switchport/mode (container)

    YANG Description: The mode of the Layer2 interface.
    """
    return self.__mode
      
  def _set_mode(self, v, load=False):
    """
    Setter method for mode, mapped from YANG variable /port_profile/vlan_profile/switchport/mode (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mode() directly.

    YANG Description: The mode of the Layer2 interface.
    """
    try:
      t = YANGDynClass(v,base=mode.mode, is_container='container', yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set mode of the Layer2 interface', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mode must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=mode.mode, is_container='container', yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set mode of the Layer2 interface', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)""",
        })

    self.__mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mode(self):
    self.__mode = YANGDynClass(base=mode.mode, is_container='container', yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set mode of the Layer2 interface', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)


  def _get_access(self):
    """
    Getter method for access, mapped from YANG variable /port_profile/vlan_profile/switchport/access (container)

    YANG Description: This specifies that the Layer 2 interface is in
access mode.
    """
    return self.__access
      
  def _set_access(self, v, load=False):
    """
    Setter method for access, mapped from YANG variable /port_profile/vlan_profile/switchport/access (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_access is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_access() directly.

    YANG Description: This specifies that the Layer 2 interface is in
access mode.
    """
    try:
      t = YANGDynClass(v,base=access.access, is_container='container', yang_name="access", rest_name="access", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as Access', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """access must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=access.access, is_container='container', yang_name="access", rest_name="access", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as Access', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)""",
        })

    self.__access = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_access(self):
    self.__access = YANGDynClass(base=access.access, is_container='container', yang_name="access", rest_name="access", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as Access', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)


  def _get_access_mac_vlan_classification(self):
    """
    Getter method for access_mac_vlan_classification, mapped from YANG variable /port_profile/vlan_profile/switchport/access_mac_vlan_classification (container)
    """
    return self.__access_mac_vlan_classification
      
  def _set_access_mac_vlan_classification(self, v, load=False):
    """
    Setter method for access_mac_vlan_classification, mapped from YANG variable /port_profile/vlan_profile/switchport/access_mac_vlan_classification (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_access_mac_vlan_classification is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_access_mac_vlan_classification() directly.
    """
    try:
      t = YANGDynClass(v,base=access_mac_vlan_classification.access_mac_vlan_classification, is_container='container', yang_name="access-mac-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'ampp-mac-based-vlan-classification'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """access_mac_vlan_classification must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=access_mac_vlan_classification.access_mac_vlan_classification, is_container='container', yang_name="access-mac-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'ampp-mac-based-vlan-classification'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)""",
        })

    self.__access_mac_vlan_classification = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_access_mac_vlan_classification(self):
    self.__access_mac_vlan_classification = YANGDynClass(base=access_mac_vlan_classification.access_mac_vlan_classification, is_container='container', yang_name="access-mac-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'ampp-mac-based-vlan-classification'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)


  def _get_access_mac_group_vlan_classification(self):
    """
    Getter method for access_mac_group_vlan_classification, mapped from YANG variable /port_profile/vlan_profile/switchport/access_mac_group_vlan_classification (container)
    """
    return self.__access_mac_group_vlan_classification
      
  def _set_access_mac_group_vlan_classification(self, v, load=False):
    """
    Setter method for access_mac_group_vlan_classification, mapped from YANG variable /port_profile/vlan_profile/switchport/access_mac_group_vlan_classification (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_access_mac_group_vlan_classification is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_access_mac_group_vlan_classification() directly.
    """
    try:
      t = YANGDynClass(v,base=access_mac_group_vlan_classification.access_mac_group_vlan_classification, is_container='container', yang_name="access-mac-group-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'ampp-macgroup-based-vlan-classification'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """access_mac_group_vlan_classification must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=access_mac_group_vlan_classification.access_mac_group_vlan_classification, is_container='container', yang_name="access-mac-group-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'ampp-macgroup-based-vlan-classification'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)""",
        })

    self.__access_mac_group_vlan_classification = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_access_mac_group_vlan_classification(self):
    self.__access_mac_group_vlan_classification = YANGDynClass(base=access_mac_group_vlan_classification.access_mac_group_vlan_classification, is_container='container', yang_name="access-mac-group-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'ampp-macgroup-based-vlan-classification'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)


  def _get_trunk(self):
    """
    Getter method for trunk, mapped from YANG variable /port_profile/vlan_profile/switchport/trunk (container)

    YANG Description: This specifies that Layer2 interface in
trunking mode.
    """
    return self.__trunk
      
  def _set_trunk(self, v, load=False):
    """
    Setter method for trunk, mapped from YANG variable /port_profile/vlan_profile/switchport/trunk (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk() directly.

    YANG Description: This specifies that Layer2 interface in
trunking mode.
    """
    try:
      t = YANGDynClass(v,base=trunk.trunk, is_container='container', yang_name="trunk", rest_name="trunk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as trunk', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=trunk.trunk, is_container='container', yang_name="trunk", rest_name="trunk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as trunk', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)""",
        })

    self.__trunk = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk(self):
    self.__trunk = YANGDynClass(base=trunk.trunk, is_container='container', yang_name="trunk", rest_name="trunk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as trunk', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)

  mode = __builtin__.property(_get_mode, _set_mode)
  access = __builtin__.property(_get_access, _set_access)
  access_mac_vlan_classification = __builtin__.property(_get_access_mac_vlan_classification, _set_access_mac_vlan_classification)
  access_mac_group_vlan_classification = __builtin__.property(_get_access_mac_group_vlan_classification, _set_access_mac_group_vlan_classification)
  trunk = __builtin__.property(_get_trunk, _set_trunk)


  _pyangbind_elements = {'mode': mode, 'access': access, 'access_mac_vlan_classification': access_mac_vlan_classification, 'access_mac_group_vlan_classification': access_mac_group_vlan_classification, 'trunk': trunk, }


