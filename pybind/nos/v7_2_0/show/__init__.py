
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import defaults
import crypto
import diag
import fabric
import fcsp
import infra
import http
import telnet
import ssh
import vnetwork
class show(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /show. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__defaults','__crypto','__diag','__fabric','__fcsp','__infra','__http','__telnet','__ssh','__vnetwork',)

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
    self.__http = YANGDynClass(base=http.http, is_container='container', presence=False, yang_name="http", rest_name="http", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display HTTP/HTTPS server status'}}, namespace='urn:brocade.com:mgmt:brocade-http', defining_module='brocade-http-config', yang_type='container', is_config=True)
    self.__fabric = YANGDynClass(base=fabric.fabric, is_container='container', presence=False, yang_name="fabric", rest_name="fabric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Provides fabric related information', u'action': u'trunk', u'display-when': u'/vcsmode/vcs-mode = "true"'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='container', is_config=True)
    self.__vnetwork = YANGDynClass(base=vnetwork.vnetwork, is_container='container', presence=False, yang_name="vnetwork", rest_name="vnetwork", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shows virtual infrastructure information', u'action': u'pgs'}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='container', is_config=True)
    self.__diag = YANGDynClass(base=diag.diag, is_container='container', presence=False, yang_name="diag", rest_name="diag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shows diagnostic tests results', u'action': u'burninerrshow'}}, namespace='urn:brocade.com:mgmt:brocade-diagnostics', defining_module='brocade-diagnostics', yang_type='container', is_config=True)
    self.__crypto = YANGDynClass(base=crypto.crypto, is_container='container', presence=False, yang_name="crypto", rest_name="crypto", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Show crypto configuration'}}, namespace='urn:brocade.com:mgmt:brocade-crypto-ext', defining_module='brocade-crypto-ext', yang_type='container', is_config=True)
    self.__telnet = YANGDynClass(base=telnet.telnet, is_container='container', presence=False, yang_name="telnet", rest_name="telnet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display Telnet server status'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)
    self.__infra = YANGDynClass(base=infra.infra, is_container='container', presence=False, yang_name="infra", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'action': u'chassis', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='container', is_config=True)
    self.__fcsp = YANGDynClass(base=fcsp.fcsp, is_container='container', presence=False, yang_name="fcsp", rest_name="fcsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display FCSP auth secrets'}}, namespace='urn:brocade.com:mgmt:brocade-fc-auth', defining_module='brocade-fc-auth', yang_type='container', is_config=True)
    self.__ssh = YANGDynClass(base=ssh.ssh, is_container='container', presence=False, yang_name="ssh", rest_name="ssh", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display SSH server status'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)
    self.__defaults = YANGDynClass(base=defaults.defaults, is_container='container', presence=False, yang_name="defaults", rest_name="defaults", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display default configuration'}}, namespace='urn:brocade.com:mgmt:brocade-common-def', defining_module='brocade-common-def', yang_type='container', is_config=True)

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

  def _get_defaults(self):
    """
    Getter method for defaults, mapped from YANG variable /show/defaults (container)
    """
    return self.__defaults
      
  def _set_defaults(self, v, load=False):
    """
    Setter method for defaults, mapped from YANG variable /show/defaults (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_defaults is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_defaults() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=defaults.defaults, is_container='container', presence=False, yang_name="defaults", rest_name="defaults", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display default configuration'}}, namespace='urn:brocade.com:mgmt:brocade-common-def', defining_module='brocade-common-def', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """defaults must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=defaults.defaults, is_container='container', presence=False, yang_name="defaults", rest_name="defaults", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display default configuration'}}, namespace='urn:brocade.com:mgmt:brocade-common-def', defining_module='brocade-common-def', yang_type='container', is_config=True)""",
        })

    self.__defaults = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_defaults(self):
    self.__defaults = YANGDynClass(base=defaults.defaults, is_container='container', presence=False, yang_name="defaults", rest_name="defaults", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display default configuration'}}, namespace='urn:brocade.com:mgmt:brocade-common-def', defining_module='brocade-common-def', yang_type='container', is_config=True)


  def _get_crypto(self):
    """
    Getter method for crypto, mapped from YANG variable /show/crypto (container)
    """
    return self.__crypto
      
  def _set_crypto(self, v, load=False):
    """
    Setter method for crypto, mapped from YANG variable /show/crypto (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_crypto is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_crypto() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=crypto.crypto, is_container='container', presence=False, yang_name="crypto", rest_name="crypto", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Show crypto configuration'}}, namespace='urn:brocade.com:mgmt:brocade-crypto-ext', defining_module='brocade-crypto-ext', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """crypto must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=crypto.crypto, is_container='container', presence=False, yang_name="crypto", rest_name="crypto", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Show crypto configuration'}}, namespace='urn:brocade.com:mgmt:brocade-crypto-ext', defining_module='brocade-crypto-ext', yang_type='container', is_config=True)""",
        })

    self.__crypto = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_crypto(self):
    self.__crypto = YANGDynClass(base=crypto.crypto, is_container='container', presence=False, yang_name="crypto", rest_name="crypto", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Show crypto configuration'}}, namespace='urn:brocade.com:mgmt:brocade-crypto-ext', defining_module='brocade-crypto-ext', yang_type='container', is_config=True)


  def _get_diag(self):
    """
    Getter method for diag, mapped from YANG variable /show/diag (container)
    """
    return self.__diag
      
  def _set_diag(self, v, load=False):
    """
    Setter method for diag, mapped from YANG variable /show/diag (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_diag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_diag() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=diag.diag, is_container='container', presence=False, yang_name="diag", rest_name="diag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shows diagnostic tests results', u'action': u'burninerrshow'}}, namespace='urn:brocade.com:mgmt:brocade-diagnostics', defining_module='brocade-diagnostics', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """diag must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=diag.diag, is_container='container', presence=False, yang_name="diag", rest_name="diag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shows diagnostic tests results', u'action': u'burninerrshow'}}, namespace='urn:brocade.com:mgmt:brocade-diagnostics', defining_module='brocade-diagnostics', yang_type='container', is_config=True)""",
        })

    self.__diag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_diag(self):
    self.__diag = YANGDynClass(base=diag.diag, is_container='container', presence=False, yang_name="diag", rest_name="diag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shows diagnostic tests results', u'action': u'burninerrshow'}}, namespace='urn:brocade.com:mgmt:brocade-diagnostics', defining_module='brocade-diagnostics', yang_type='container', is_config=True)


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


  def _get_fcsp(self):
    """
    Getter method for fcsp, mapped from YANG variable /show/fcsp (container)

    YANG Description: Displaying FCSP auth secrets
    """
    return self.__fcsp
      
  def _set_fcsp(self, v, load=False):
    """
    Setter method for fcsp, mapped from YANG variable /show/fcsp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcsp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcsp() directly.

    YANG Description: Displaying FCSP auth secrets
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=fcsp.fcsp, is_container='container', presence=False, yang_name="fcsp", rest_name="fcsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display FCSP auth secrets'}}, namespace='urn:brocade.com:mgmt:brocade-fc-auth', defining_module='brocade-fc-auth', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcsp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=fcsp.fcsp, is_container='container', presence=False, yang_name="fcsp", rest_name="fcsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display FCSP auth secrets'}}, namespace='urn:brocade.com:mgmt:brocade-fc-auth', defining_module='brocade-fc-auth', yang_type='container', is_config=True)""",
        })

    self.__fcsp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcsp(self):
    self.__fcsp = YANGDynClass(base=fcsp.fcsp, is_container='container', presence=False, yang_name="fcsp", rest_name="fcsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display FCSP auth secrets'}}, namespace='urn:brocade.com:mgmt:brocade-fc-auth', defining_module='brocade-fc-auth', yang_type='container', is_config=True)


  def _get_infra(self):
    """
    Getter method for infra, mapped from YANG variable /show/infra (container)

    YANG Description: show system info
    """
    return self.__infra
      
  def _set_infra(self, v, load=False):
    """
    Setter method for infra, mapped from YANG variable /show/infra (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_infra is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_infra() directly.

    YANG Description: show system info
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


  def _get_http(self):
    """
    Getter method for http, mapped from YANG variable /show/http (container)
    """
    return self.__http
      
  def _set_http(self, v, load=False):
    """
    Setter method for http, mapped from YANG variable /show/http (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_http is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_http() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=http.http, is_container='container', presence=False, yang_name="http", rest_name="http", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display HTTP/HTTPS server status'}}, namespace='urn:brocade.com:mgmt:brocade-http', defining_module='brocade-http-config', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """http must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=http.http, is_container='container', presence=False, yang_name="http", rest_name="http", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display HTTP/HTTPS server status'}}, namespace='urn:brocade.com:mgmt:brocade-http', defining_module='brocade-http-config', yang_type='container', is_config=True)""",
        })

    self.__http = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_http(self):
    self.__http = YANGDynClass(base=http.http, is_container='container', presence=False, yang_name="http", rest_name="http", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Display HTTP/HTTPS server status'}}, namespace='urn:brocade.com:mgmt:brocade-http', defining_module='brocade-http-config', yang_type='container', is_config=True)


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


  def _get_vnetwork(self):
    """
    Getter method for vnetwork, mapped from YANG variable /show/vnetwork (container)

    YANG Description: Shows virtual infrastructure information
    """
    return self.__vnetwork
      
  def _set_vnetwork(self, v, load=False):
    """
    Setter method for vnetwork, mapped from YANG variable /show/vnetwork (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vnetwork is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vnetwork() directly.

    YANG Description: Shows virtual infrastructure information
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=vnetwork.vnetwork, is_container='container', presence=False, yang_name="vnetwork", rest_name="vnetwork", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shows virtual infrastructure information', u'action': u'pgs'}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vnetwork must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=vnetwork.vnetwork, is_container='container', presence=False, yang_name="vnetwork", rest_name="vnetwork", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shows virtual infrastructure information', u'action': u'pgs'}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='container', is_config=True)""",
        })

    self.__vnetwork = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vnetwork(self):
    self.__vnetwork = YANGDynClass(base=vnetwork.vnetwork, is_container='container', presence=False, yang_name="vnetwork", rest_name="vnetwork", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shows virtual infrastructure information', u'action': u'pgs'}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='container', is_config=True)

  defaults = __builtin__.property(_get_defaults, _set_defaults)
  crypto = __builtin__.property(_get_crypto, _set_crypto)
  diag = __builtin__.property(_get_diag, _set_diag)
  fabric = __builtin__.property(_get_fabric, _set_fabric)
  fcsp = __builtin__.property(_get_fcsp, _set_fcsp)
  infra = __builtin__.property(_get_infra, _set_infra)
  http = __builtin__.property(_get_http, _set_http)
  telnet = __builtin__.property(_get_telnet, _set_telnet)
  ssh = __builtin__.property(_get_ssh, _set_ssh)
  vnetwork = __builtin__.property(_get_vnetwork, _set_vnetwork)


  _pyangbind_elements = {'defaults': defaults, 'crypto': crypto, 'diag': diag, 'fabric': fabric, 'fcsp': fcsp, 'infra': infra, 'http': http, 'telnet': telnet, 'ssh': ssh, 'vnetwork': vnetwork, }


