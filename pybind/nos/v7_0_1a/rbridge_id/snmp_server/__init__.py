
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import engineID
import user
import v3host
import offline_if
import three_tuple_if
class snmp_server(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/snmp-server. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__engineID','__user','__v3host','__offline_if','__three_tuple_if',)

  _yang_name = 'snmp-server'
  _rest_name = 'snmp-server'

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
    self.__v3host = YANGDynClass(base=YANGListType("hostip username",v3host.v3host, yang_name="v3host", rest_name="v3host", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='hostip username', extensions={u'tailf-common': {u'info': u'Holds IP Address, username, severity level and \nport number used to send v3 traps and informs', u'cli-suppress-list-no': None, u'callpoint': u'snmplocalV3host', u'cli-suppress-key-abbreviation': None, u'sort-priority': u'25'}}), is_container='list', yang_name="v3host", rest_name="v3host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Holds IP Address, username, severity level and \nport number used to send v3 traps and informs', u'cli-suppress-list-no': None, u'callpoint': u'snmplocalV3host', u'cli-suppress-key-abbreviation': None, u'sort-priority': u'25'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='list', is_config=True)
    self.__offline_if = YANGDynClass(base=offline_if.offline_if, is_container='container', yang_name="offline-if", rest_name="offline-if", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow SNMP to display offline interfaces when linecard powered-off', u'display-when': u'((../../swbd-number = "1000") or (../../swbd-number = "1001") or (../../swbd-number = "1002"))', u'callpoint': u'snmplocalconfig_cp'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='container', is_config=True)
    self.__three_tuple_if = YANGDynClass(base=three_tuple_if.three_tuple_if, is_container='container', yang_name="three-tuple-if", rest_name="three-tuple-if", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow SNMP to display physical interfaces in 3-tuple format for ifDescr and ifName', u'callpoint': u'snmp3tupleconfig_cp'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='container', is_config=True)
    self.__engineID = YANGDynClass(base=engineID.engineID, is_container='container', yang_name="engineID", rest_name="engineID", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u"Holds local Agents's Engine ID. Reboot is required to make changes to be effective in snmp", u'callpoint': u'snmplocalengineid', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='container', is_config=True)
    self.__user = YANGDynClass(base=YANGListType("username",user.user, yang_name="user", rest_name="user", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='username', extensions={u'tailf-common': {u'info': u'Holds username, groupname auth\nand priv attributes associated with SNMP username', u'cli-suppress-mode': None, u'sort-priority': u'24', u'cli-suppress-show-match': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'snmplocaluser'}}), is_container='list', yang_name="user", rest_name="user", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Holds username, groupname auth\nand priv attributes associated with SNMP username', u'cli-suppress-mode': None, u'sort-priority': u'24', u'cli-suppress-show-match': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'snmplocaluser'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='list', is_config=True)

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
      return [u'rbridge-id', u'snmp-server']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'snmp-server']

  def _get_engineID(self):
    """
    Getter method for engineID, mapped from YANG variable /rbridge_id/snmp_server/engineID (container)
    """
    return self.__engineID
      
  def _set_engineID(self, v, load=False):
    """
    Setter method for engineID, mapped from YANG variable /rbridge_id/snmp_server/engineID (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_engineID is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_engineID() directly.
    """
    try:
      t = YANGDynClass(v,base=engineID.engineID, is_container='container', yang_name="engineID", rest_name="engineID", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u"Holds local Agents's Engine ID. Reboot is required to make changes to be effective in snmp", u'callpoint': u'snmplocalengineid', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """engineID must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=engineID.engineID, is_container='container', yang_name="engineID", rest_name="engineID", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u"Holds local Agents's Engine ID. Reboot is required to make changes to be effective in snmp", u'callpoint': u'snmplocalengineid', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='container', is_config=True)""",
        })

    self.__engineID = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_engineID(self):
    self.__engineID = YANGDynClass(base=engineID.engineID, is_container='container', yang_name="engineID", rest_name="engineID", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u"Holds local Agents's Engine ID. Reboot is required to make changes to be effective in snmp", u'callpoint': u'snmplocalengineid', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='container', is_config=True)


  def _get_user(self):
    """
    Getter method for user, mapped from YANG variable /rbridge_id/snmp_server/user (list)
    """
    return self.__user
      
  def _set_user(self, v, load=False):
    """
    Setter method for user, mapped from YANG variable /rbridge_id/snmp_server/user (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_user is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_user() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("username",user.user, yang_name="user", rest_name="user", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='username', extensions={u'tailf-common': {u'info': u'Holds username, groupname auth\nand priv attributes associated with SNMP username', u'cli-suppress-mode': None, u'sort-priority': u'24', u'cli-suppress-show-match': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'snmplocaluser'}}), is_container='list', yang_name="user", rest_name="user", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Holds username, groupname auth\nand priv attributes associated with SNMP username', u'cli-suppress-mode': None, u'sort-priority': u'24', u'cli-suppress-show-match': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'snmplocaluser'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """user must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("username",user.user, yang_name="user", rest_name="user", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='username', extensions={u'tailf-common': {u'info': u'Holds username, groupname auth\nand priv attributes associated with SNMP username', u'cli-suppress-mode': None, u'sort-priority': u'24', u'cli-suppress-show-match': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'snmplocaluser'}}), is_container='list', yang_name="user", rest_name="user", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Holds username, groupname auth\nand priv attributes associated with SNMP username', u'cli-suppress-mode': None, u'sort-priority': u'24', u'cli-suppress-show-match': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'snmplocaluser'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='list', is_config=True)""",
        })

    self.__user = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_user(self):
    self.__user = YANGDynClass(base=YANGListType("username",user.user, yang_name="user", rest_name="user", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='username', extensions={u'tailf-common': {u'info': u'Holds username, groupname auth\nand priv attributes associated with SNMP username', u'cli-suppress-mode': None, u'sort-priority': u'24', u'cli-suppress-show-match': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'snmplocaluser'}}), is_container='list', yang_name="user", rest_name="user", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Holds username, groupname auth\nand priv attributes associated with SNMP username', u'cli-suppress-mode': None, u'sort-priority': u'24', u'cli-suppress-show-match': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'snmplocaluser'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='list', is_config=True)


  def _get_v3host(self):
    """
    Getter method for v3host, mapped from YANG variable /rbridge_id/snmp_server/v3host (list)
    """
    return self.__v3host
      
  def _set_v3host(self, v, load=False):
    """
    Setter method for v3host, mapped from YANG variable /rbridge_id/snmp_server/v3host (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_v3host is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_v3host() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("hostip username",v3host.v3host, yang_name="v3host", rest_name="v3host", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='hostip username', extensions={u'tailf-common': {u'info': u'Holds IP Address, username, severity level and \nport number used to send v3 traps and informs', u'cli-suppress-list-no': None, u'callpoint': u'snmplocalV3host', u'cli-suppress-key-abbreviation': None, u'sort-priority': u'25'}}), is_container='list', yang_name="v3host", rest_name="v3host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Holds IP Address, username, severity level and \nport number used to send v3 traps and informs', u'cli-suppress-list-no': None, u'callpoint': u'snmplocalV3host', u'cli-suppress-key-abbreviation': None, u'sort-priority': u'25'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """v3host must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("hostip username",v3host.v3host, yang_name="v3host", rest_name="v3host", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='hostip username', extensions={u'tailf-common': {u'info': u'Holds IP Address, username, severity level and \nport number used to send v3 traps and informs', u'cli-suppress-list-no': None, u'callpoint': u'snmplocalV3host', u'cli-suppress-key-abbreviation': None, u'sort-priority': u'25'}}), is_container='list', yang_name="v3host", rest_name="v3host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Holds IP Address, username, severity level and \nport number used to send v3 traps and informs', u'cli-suppress-list-no': None, u'callpoint': u'snmplocalV3host', u'cli-suppress-key-abbreviation': None, u'sort-priority': u'25'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='list', is_config=True)""",
        })

    self.__v3host = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_v3host(self):
    self.__v3host = YANGDynClass(base=YANGListType("hostip username",v3host.v3host, yang_name="v3host", rest_name="v3host", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='hostip username', extensions={u'tailf-common': {u'info': u'Holds IP Address, username, severity level and \nport number used to send v3 traps and informs', u'cli-suppress-list-no': None, u'callpoint': u'snmplocalV3host', u'cli-suppress-key-abbreviation': None, u'sort-priority': u'25'}}), is_container='list', yang_name="v3host", rest_name="v3host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Holds IP Address, username, severity level and \nport number used to send v3 traps and informs', u'cli-suppress-list-no': None, u'callpoint': u'snmplocalV3host', u'cli-suppress-key-abbreviation': None, u'sort-priority': u'25'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='list', is_config=True)


  def _get_offline_if(self):
    """
    Getter method for offline_if, mapped from YANG variable /rbridge_id/snmp_server/offline_if (container)
    """
    return self.__offline_if
      
  def _set_offline_if(self, v, load=False):
    """
    Setter method for offline_if, mapped from YANG variable /rbridge_id/snmp_server/offline_if (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_offline_if is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_offline_if() directly.
    """
    try:
      t = YANGDynClass(v,base=offline_if.offline_if, is_container='container', yang_name="offline-if", rest_name="offline-if", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow SNMP to display offline interfaces when linecard powered-off', u'display-when': u'((../../swbd-number = "1000") or (../../swbd-number = "1001") or (../../swbd-number = "1002"))', u'callpoint': u'snmplocalconfig_cp'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """offline_if must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=offline_if.offline_if, is_container='container', yang_name="offline-if", rest_name="offline-if", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow SNMP to display offline interfaces when linecard powered-off', u'display-when': u'((../../swbd-number = "1000") or (../../swbd-number = "1001") or (../../swbd-number = "1002"))', u'callpoint': u'snmplocalconfig_cp'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='container', is_config=True)""",
        })

    self.__offline_if = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_offline_if(self):
    self.__offline_if = YANGDynClass(base=offline_if.offline_if, is_container='container', yang_name="offline-if", rest_name="offline-if", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow SNMP to display offline interfaces when linecard powered-off', u'display-when': u'((../../swbd-number = "1000") or (../../swbd-number = "1001") or (../../swbd-number = "1002"))', u'callpoint': u'snmplocalconfig_cp'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='container', is_config=True)


  def _get_three_tuple_if(self):
    """
    Getter method for three_tuple_if, mapped from YANG variable /rbridge_id/snmp_server/three_tuple_if (container)
    """
    return self.__three_tuple_if
      
  def _set_three_tuple_if(self, v, load=False):
    """
    Setter method for three_tuple_if, mapped from YANG variable /rbridge_id/snmp_server/three_tuple_if (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_three_tuple_if is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_three_tuple_if() directly.
    """
    try:
      t = YANGDynClass(v,base=three_tuple_if.three_tuple_if, is_container='container', yang_name="three-tuple-if", rest_name="three-tuple-if", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow SNMP to display physical interfaces in 3-tuple format for ifDescr and ifName', u'callpoint': u'snmp3tupleconfig_cp'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """three_tuple_if must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=three_tuple_if.three_tuple_if, is_container='container', yang_name="three-tuple-if", rest_name="three-tuple-if", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow SNMP to display physical interfaces in 3-tuple format for ifDescr and ifName', u'callpoint': u'snmp3tupleconfig_cp'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='container', is_config=True)""",
        })

    self.__three_tuple_if = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_three_tuple_if(self):
    self.__three_tuple_if = YANGDynClass(base=three_tuple_if.three_tuple_if, is_container='container', yang_name="three-tuple-if", rest_name="three-tuple-if", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow SNMP to display physical interfaces in 3-tuple format for ifDescr and ifName', u'callpoint': u'snmp3tupleconfig_cp'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='container', is_config=True)

  engineID = __builtin__.property(_get_engineID, _set_engineID)
  user = __builtin__.property(_get_user, _set_user)
  v3host = __builtin__.property(_get_v3host, _set_v3host)
  offline_if = __builtin__.property(_get_offline_if, _set_offline_if)
  three_tuple_if = __builtin__.property(_get_three_tuple_if, _set_three_tuple_if)


  _pyangbind_elements = {'engineID': engineID, 'user': user, 'v3host': v3host, 'offline_if': offline_if, 'three_tuple_if': three_tuple_if, }


