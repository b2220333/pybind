
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import credentials
import discovery
class vcenter(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vswitch - based on the path /vcenter. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: vCenter
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__id','__credentials','__vlan_create','__activate','__interval','__discovery',)

  _yang_name = 'vcenter'
  _rest_name = 'vcenter'

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
    self.__activate = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Activate the vCenter discovery'}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='empty', is_config=True)
    self.__interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..1440']}), is_leaf=True, yang_name="interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Discovery Timer Interval'}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='uint32', is_config=True)
    self.__vlan_create = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'auto': {'value': 0}, u'switch-admin': {'value': 1}},), is_leaf=True, yang_name="vlan-create", rest_name="vlan-create", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure VLAN creation during vCenter discovery/Events process.', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='enumeration', is_config=True)
    self.__credentials = YANGDynClass(base=credentials.credentials, is_container='container', presence=False, yang_name="credentials", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='container', is_config=True)
    self.__id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="id", rest_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NAME;;vCenter name (Max Size - 32)', u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='common-def:name-string32', is_config=True)
    self.__discovery = YANGDynClass(base=discovery.discovery, is_container='container', presence=False, yang_name="discovery", rest_name="discovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='container', is_config=True)

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
      return [u'vcenter']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'vcenter']

  def _get_id(self):
    """
    Getter method for id, mapped from YANG variable /vcenter/id (common-def:name-string32)

    YANG Description: NAME;;vCenter name (Max Size - 32)
    """
    return self.__id
      
  def _set_id(self, v, load=False):
    """
    Setter method for id, mapped from YANG variable /vcenter/id (common-def:name-string32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_id() directly.

    YANG Description: NAME;;vCenter name (Max Size - 32)
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="id", rest_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NAME;;vCenter name (Max Size - 32)', u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='common-def:name-string32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """id must be of a type compatible with common-def:name-string32""",
          'defined-type': "common-def:name-string32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="id", rest_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NAME;;vCenter name (Max Size - 32)', u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='common-def:name-string32', is_config=True)""",
        })

    self.__id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_id(self):
    self.__id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="id", rest_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NAME;;vCenter name (Max Size - 32)', u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='common-def:name-string32', is_config=True)


  def _get_credentials(self):
    """
    Getter method for credentials, mapped from YANG variable /vcenter/credentials (container)
    """
    return self.__credentials
      
  def _set_credentials(self, v, load=False):
    """
    Setter method for credentials, mapped from YANG variable /vcenter/credentials (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_credentials is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_credentials() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=credentials.credentials, is_container='container', presence=False, yang_name="credentials", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """credentials must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=credentials.credentials, is_container='container', presence=False, yang_name="credentials", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='container', is_config=True)""",
        })

    self.__credentials = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_credentials(self):
    self.__credentials = YANGDynClass(base=credentials.credentials, is_container='container', presence=False, yang_name="credentials", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='container', is_config=True)


  def _get_vlan_create(self):
    """
    Getter method for vlan_create, mapped from YANG variable /vcenter/vlan_create (enumeration)
    """
    return self.__vlan_create
      
  def _set_vlan_create(self, v, load=False):
    """
    Setter method for vlan_create, mapped from YANG variable /vcenter/vlan_create (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_create is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_create() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'auto': {'value': 0}, u'switch-admin': {'value': 1}},), is_leaf=True, yang_name="vlan-create", rest_name="vlan-create", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure VLAN creation during vCenter discovery/Events process.', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_create must be of a type compatible with enumeration""",
          'defined-type': "brocade-vswitch:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'auto': {'value': 0}, u'switch-admin': {'value': 1}},), is_leaf=True, yang_name="vlan-create", rest_name="vlan-create", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure VLAN creation during vCenter discovery/Events process.', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='enumeration', is_config=True)""",
        })

    self.__vlan_create = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_create(self):
    self.__vlan_create = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'auto': {'value': 0}, u'switch-admin': {'value': 1}},), is_leaf=True, yang_name="vlan-create", rest_name="vlan-create", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure VLAN creation during vCenter discovery/Events process.', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='enumeration', is_config=True)


  def _get_activate(self):
    """
    Getter method for activate, mapped from YANG variable /vcenter/activate (empty)

    YANG Description: Activate the vCenter discovery
    """
    return self.__activate
      
  def _set_activate(self, v, load=False):
    """
    Setter method for activate, mapped from YANG variable /vcenter/activate (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_activate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_activate() directly.

    YANG Description: Activate the vCenter discovery
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Activate the vCenter discovery'}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """activate must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Activate the vCenter discovery'}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='empty', is_config=True)""",
        })

    self.__activate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_activate(self):
    self.__activate = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Activate the vCenter discovery'}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='empty', is_config=True)


  def _get_interval(self):
    """
    Getter method for interval, mapped from YANG variable /vcenter/interval (uint32)

    YANG Description: Discovery Timer Interval
    """
    return self.__interval
      
  def _set_interval(self, v, load=False):
    """
    Setter method for interval, mapped from YANG variable /vcenter/interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interval() directly.

    YANG Description: Discovery Timer Interval
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..1440']}), is_leaf=True, yang_name="interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Discovery Timer Interval'}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interval must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..1440']}), is_leaf=True, yang_name="interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Discovery Timer Interval'}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='uint32', is_config=True)""",
        })

    self.__interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interval(self):
    self.__interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..1440']}), is_leaf=True, yang_name="interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Discovery Timer Interval'}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='uint32', is_config=True)


  def _get_discovery(self):
    """
    Getter method for discovery, mapped from YANG variable /vcenter/discovery (container)
    """
    return self.__discovery
      
  def _set_discovery(self, v, load=False):
    """
    Setter method for discovery, mapped from YANG variable /vcenter/discovery (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_discovery is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_discovery() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=discovery.discovery, is_container='container', presence=False, yang_name="discovery", rest_name="discovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """discovery must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=discovery.discovery, is_container='container', presence=False, yang_name="discovery", rest_name="discovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='container', is_config=True)""",
        })

    self.__discovery = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_discovery(self):
    self.__discovery = YANGDynClass(base=discovery.discovery, is_container='container', presence=False, yang_name="discovery", rest_name="discovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='container', is_config=True)

  id = __builtin__.property(_get_id, _set_id)
  credentials = __builtin__.property(_get_credentials, _set_credentials)
  vlan_create = __builtin__.property(_get_vlan_create, _set_vlan_create)
  activate = __builtin__.property(_get_activate, _set_activate)
  interval = __builtin__.property(_get_interval, _set_interval)
  discovery = __builtin__.property(_get_discovery, _set_discovery)


  _pyangbind_elements = {'id': id, 'credentials': credentials, 'vlan_create': vlan_create, 'activate': activate, 'interval': interval, 'discovery': discovery, }


