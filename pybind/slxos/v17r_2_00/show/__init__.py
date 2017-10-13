
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import fabric
import show_firmware_dummy
import infra
import telnet
import ssh
class show(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /show. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__fabric','__show_firmware_dummy','__infra','__telnet','__ssh',)

  _yang_name = 'show'
  _rest_name = 'show'

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
    self.__ssh = YANGDynClass(base=ssh.ssh, is_container='container', presence=False, yang_name="ssh", rest_name="ssh", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display SSH server status'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)
    self.__show_firmware_dummy = YANGDynClass(base=show_firmware_dummy.show_firmware_dummy, is_container='container', presence=False, yang_name="show-firmware-dummy", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'show firmware-dummy', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='container', is_config=True)
    self.__fabric = YANGDynClass(base=fabric.fabric, is_container='container', presence=False, yang_name="fabric", rest_name="fabric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Provides fabric related information', u'action': u'trunk', u'display-when': u'/vcsmode/vcs-mode = "true"'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='container', is_config=True)
    self.__telnet = YANGDynClass(base=telnet.telnet, is_container='container', presence=False, yang_name="telnet", rest_name="telnet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display Telnet server status'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)
    self.__infra = YANGDynClass(base=infra.infra, is_container='container', presence=False, yang_name="infra", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'action': u'chassis', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='container', is_config=True)

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
      return [u'show']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show']

  def _get_fabric(self):
    """
    Getter method for fabric, mapped from YANG variable /show/fabric (container)

    YANG Description: This function provides fabric related information.
This includes information about the various RBridges
in the fabric, ISL connectivity information, fabric
topology, routing info, multicast tree details, etc.
This information is applicable/available only when
the VCS mode is enabled. In VCS disabled mode
(standalone mode) fabric does not exist.
    """
    return self.__fabric
      
  def _set_fabric(self, v, load=False):
    """
    Setter method for fabric, mapped from YANG variable /show/fabric (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fabric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fabric() directly.

    YANG Description: This function provides fabric related information.
This includes information about the various RBridges
in the fabric, ISL connectivity information, fabric
topology, routing info, multicast tree details, etc.
This information is applicable/available only when
the VCS mode is enabled. In VCS disabled mode
(standalone mode) fabric does not exist.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=fabric.fabric, is_container='container', presence=False, yang_name="fabric", rest_name="fabric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Provides fabric related information', u'action': u'trunk', u'display-when': u'/vcsmode/vcs-mode = "true"'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fabric must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=fabric.fabric, is_container='container', presence=False, yang_name="fabric", rest_name="fabric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Provides fabric related information', u'action': u'trunk', u'display-when': u'/vcsmode/vcs-mode = "true"'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='container', is_config=True)""",
        })

    self.__fabric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fabric(self):
    self.__fabric = YANGDynClass(base=fabric.fabric, is_container='container', presence=False, yang_name="fabric", rest_name="fabric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Provides fabric related information', u'action': u'trunk', u'display-when': u'/vcsmode/vcs-mode = "true"'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='container', is_config=True)


  def _get_show_firmware_dummy(self):
    """
    Getter method for show_firmware_dummy, mapped from YANG variable /show/show_firmware_dummy (container)
    """
    return self.__show_firmware_dummy
      
  def _set_show_firmware_dummy(self, v, load=False):
    """
    Setter method for show_firmware_dummy, mapped from YANG variable /show/show_firmware_dummy (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_firmware_dummy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_firmware_dummy() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=show_firmware_dummy.show_firmware_dummy, is_container='container', presence=False, yang_name="show-firmware-dummy", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'show firmware-dummy', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_firmware_dummy must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=show_firmware_dummy.show_firmware_dummy, is_container='container', presence=False, yang_name="show-firmware-dummy", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'show firmware-dummy', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='container', is_config=True)""",
        })

    self.__show_firmware_dummy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_firmware_dummy(self):
    self.__show_firmware_dummy = YANGDynClass(base=show_firmware_dummy.show_firmware_dummy, is_container='container', presence=False, yang_name="show-firmware-dummy", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'show firmware-dummy', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='container', is_config=True)


  def _get_infra(self):
    """
    Getter method for infra, mapped from YANG variable /show/infra (container)

    YANG Description: Show system info
    """
    return self.__infra
      
  def _set_infra(self, v, load=False):
    """
    Setter method for infra, mapped from YANG variable /show/infra (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_infra is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_infra() directly.

    YANG Description: Show system info
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=infra.infra, is_container='container', presence=False, yang_name="infra", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'action': u'chassis', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """infra must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=infra.infra, is_container='container', presence=False, yang_name="infra", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'action': u'chassis', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='container', is_config=True)""",
        })

    self.__infra = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_infra(self):
    self.__infra = YANGDynClass(base=infra.infra, is_container='container', presence=False, yang_name="infra", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'action': u'chassis', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='container', is_config=True)


  def _get_telnet(self):
    """
    Getter method for telnet, mapped from YANG variable /show/telnet (container)
    """
    return self.__telnet
      
  def _set_telnet(self, v, load=False):
    """
    Setter method for telnet, mapped from YANG variable /show/telnet (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_telnet is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_telnet() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=telnet.telnet, is_container='container', presence=False, yang_name="telnet", rest_name="telnet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display Telnet server status'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """telnet must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=telnet.telnet, is_container='container', presence=False, yang_name="telnet", rest_name="telnet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display Telnet server status'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)""",
        })

    self.__telnet = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_telnet(self):
    self.__telnet = YANGDynClass(base=telnet.telnet, is_container='container', presence=False, yang_name="telnet", rest_name="telnet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display Telnet server status'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)


  def _get_ssh(self):
    """
    Getter method for ssh, mapped from YANG variable /show/ssh (container)
    """
    return self.__ssh
      
  def _set_ssh(self, v, load=False):
    """
    Setter method for ssh, mapped from YANG variable /show/ssh (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ssh is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ssh() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ssh.ssh, is_container='container', presence=False, yang_name="ssh", rest_name="ssh", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display SSH server status'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ssh must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ssh.ssh, is_container='container', presence=False, yang_name="ssh", rest_name="ssh", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display SSH server status'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)""",
        })

    self.__ssh = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ssh(self):
    self.__ssh = YANGDynClass(base=ssh.ssh, is_container='container', presence=False, yang_name="ssh", rest_name="ssh", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display SSH server status'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)

  fabric = __builtin__.property(_get_fabric, _set_fabric)
  show_firmware_dummy = __builtin__.property(_get_show_firmware_dummy, _set_show_firmware_dummy)
  infra = __builtin__.property(_get_infra, _set_infra)
  telnet = __builtin__.property(_get_telnet, _set_telnet)
  ssh = __builtin__.property(_get_ssh, _set_ssh)


  _pyangbind_elements = {'fabric': fabric, 'show_firmware_dummy': show_firmware_dummy, 'infra': infra, 'telnet': telnet, 'ssh': ssh, }

