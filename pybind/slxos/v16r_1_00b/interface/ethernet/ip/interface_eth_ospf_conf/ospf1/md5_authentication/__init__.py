
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import no_encrypt_key_table
import key_table
class md5_authentication(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/ethernet/ip/interface-eth-ospf-conf/ospf1/md5-authentication. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__key_activation_wait_time','__no_encrypt_key_table','__key_table',)

  _yang_name = 'md5-authentication'
  _rest_name = 'md5-authentication'

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
    self.__key_activation_wait_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..14400']}), is_leaf=True, yang_name="key-activation-wait-time", rest_name="key-activation-wait-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The activation wait time in Seconds'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='common-def:time-interval-sec', is_config=True)
    self.__key_table = YANGDynClass(base=key_table.key_table, is_container='container', yang_name="key-table", rest_name="key-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' MD5 authentication key ID table ', u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'alt-name': u'key-id'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    self.__no_encrypt_key_table = YANGDynClass(base=no_encrypt_key_table.no_encrypt_key_table, is_container='container', yang_name="no-encrypt-key-table", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)

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
      return [u'interface', u'ethernet', u'ip', u'interface-eth-ospf-conf', u'ospf1', u'md5-authentication']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ethernet', u'ip', u'ospf', u'md5-authentication']

  def _get_key_activation_wait_time(self):
    """
    Getter method for key_activation_wait_time, mapped from YANG variable /interface/ethernet/ip/interface_eth_ospf_conf/ospf1/md5_authentication/key_activation_wait_time (common-def:time-interval-sec)
    """
    return self.__key_activation_wait_time
      
  def _set_key_activation_wait_time(self, v, load=False):
    """
    Setter method for key_activation_wait_time, mapped from YANG variable /interface/ethernet/ip/interface_eth_ospf_conf/ospf1/md5_authentication/key_activation_wait_time (common-def:time-interval-sec)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_key_activation_wait_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_key_activation_wait_time() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..14400']}), is_leaf=True, yang_name="key-activation-wait-time", rest_name="key-activation-wait-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The activation wait time in Seconds'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='common-def:time-interval-sec', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """key_activation_wait_time must be of a type compatible with common-def:time-interval-sec""",
          'defined-type': "common-def:time-interval-sec",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..14400']}), is_leaf=True, yang_name="key-activation-wait-time", rest_name="key-activation-wait-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The activation wait time in Seconds'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='common-def:time-interval-sec', is_config=True)""",
        })

    self.__key_activation_wait_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_key_activation_wait_time(self):
    self.__key_activation_wait_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..14400']}), is_leaf=True, yang_name="key-activation-wait-time", rest_name="key-activation-wait-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The activation wait time in Seconds'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='common-def:time-interval-sec', is_config=True)


  def _get_no_encrypt_key_table(self):
    """
    Getter method for no_encrypt_key_table, mapped from YANG variable /interface/ethernet/ip/interface_eth_ospf_conf/ospf1/md5_authentication/no_encrypt_key_table (container)
    """
    return self.__no_encrypt_key_table
      
  def _set_no_encrypt_key_table(self, v, load=False):
    """
    Setter method for no_encrypt_key_table, mapped from YANG variable /interface/ethernet/ip/interface_eth_ospf_conf/ospf1/md5_authentication/no_encrypt_key_table (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_no_encrypt_key_table is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_no_encrypt_key_table() directly.
    """
    try:
      t = YANGDynClass(v,base=no_encrypt_key_table.no_encrypt_key_table, is_container='container', yang_name="no-encrypt-key-table", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """no_encrypt_key_table must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=no_encrypt_key_table.no_encrypt_key_table, is_container='container', yang_name="no-encrypt-key-table", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)""",
        })

    self.__no_encrypt_key_table = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_no_encrypt_key_table(self):
    self.__no_encrypt_key_table = YANGDynClass(base=no_encrypt_key_table.no_encrypt_key_table, is_container='container', yang_name="no-encrypt-key-table", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)


  def _get_key_table(self):
    """
    Getter method for key_table, mapped from YANG variable /interface/ethernet/ip/interface_eth_ospf_conf/ospf1/md5_authentication/key_table (container)
    """
    return self.__key_table
      
  def _set_key_table(self, v, load=False):
    """
    Setter method for key_table, mapped from YANG variable /interface/ethernet/ip/interface_eth_ospf_conf/ospf1/md5_authentication/key_table (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_key_table is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_key_table() directly.
    """
    try:
      t = YANGDynClass(v,base=key_table.key_table, is_container='container', yang_name="key-table", rest_name="key-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' MD5 authentication key ID table ', u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'alt-name': u'key-id'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """key_table must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=key_table.key_table, is_container='container', yang_name="key-table", rest_name="key-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' MD5 authentication key ID table ', u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'alt-name': u'key-id'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)""",
        })

    self.__key_table = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_key_table(self):
    self.__key_table = YANGDynClass(base=key_table.key_table, is_container='container', yang_name="key-table", rest_name="key-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' MD5 authentication key ID table ', u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'alt-name': u'key-id'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)

  key_activation_wait_time = __builtin__.property(_get_key_activation_wait_time, _set_key_activation_wait_time)
  no_encrypt_key_table = __builtin__.property(_get_no_encrypt_key_table, _set_no_encrypt_key_table)
  key_table = __builtin__.property(_get_key_table, _set_key_table)


  _pyangbind_elements = {'key_activation_wait_time': key_activation_wait_time, 'no_encrypt_key_table': no_encrypt_key_table, 'key_table': key_table, }


