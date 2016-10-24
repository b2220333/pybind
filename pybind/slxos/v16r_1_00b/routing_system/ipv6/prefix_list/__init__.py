
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class prefix_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/ipv6/prefix-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: IPv6 address prefix list.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__name','__seq_keyword','__instance','__action_ipp','__ipv6_prefix_ipp','__ge_ipp','__le_ipp',)

  _yang_name = 'prefix-list'
  _rest_name = 'prefix-list'

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
    self.__ge_ipp = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..128']}), is_leaf=True, yang_name="ge-ipp", rest_name="ge", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Minimum IPv6 prefix length.', u'alt-name': u'ge', u'cli-suppress-no': None, u'cli-break-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ipv6-prefix-len-t', is_config=True)
    self.__le_ipp = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..128']}), is_leaf=True, yang_name="le-ipp", rest_name="le", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Maximum IPv6 prefix length.', u'alt-name': u'le', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ipv6-prefix-len-t', is_config=True)
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ipv6-prefix-name-t', is_config=True)
    self.__ipv6_prefix_ipp = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="ipv6-prefix-ipp", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='inet:ipv6-prefix', is_config=True)
    self.__instance = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="instance", rest_name="instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='instance-id-t', is_config=True)
    self.__seq_keyword = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'seq': {'value': 1}},), is_leaf=True, yang_name="seq-keyword", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='enumeration', is_config=True)
    self.__action_ipp = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'receive': {'value': 2}, u'send': {'value': 1}},), is_leaf=True, yang_name="action-ipp", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='action-t', is_config=True)

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
      return [u'routing-system', u'ipv6', u'prefix-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ipv6', u'prefix-list']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /routing_system/ipv6/prefix_list/name (ipv6-prefix-name-t)
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /routing_system/ipv6/prefix_list/name (ipv6-prefix-name-t)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ipv6-prefix-name-t', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with ipv6-prefix-name-t""",
          'defined-type': "brocade-ip-policy:ipv6-prefix-name-t",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ipv6-prefix-name-t', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ipv6-prefix-name-t', is_config=True)


  def _get_seq_keyword(self):
    """
    Getter method for seq_keyword, mapped from YANG variable /routing_system/ipv6/prefix_list/seq_keyword (enumeration)
    """
    return self.__seq_keyword
      
  def _set_seq_keyword(self, v, load=False):
    """
    Setter method for seq_keyword, mapped from YANG variable /routing_system/ipv6/prefix_list/seq_keyword (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_seq_keyword is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_seq_keyword() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'seq': {'value': 1}},), is_leaf=True, yang_name="seq-keyword", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """seq_keyword must be of a type compatible with enumeration""",
          'defined-type': "brocade-ip-policy:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'seq': {'value': 1}},), is_leaf=True, yang_name="seq-keyword", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='enumeration', is_config=True)""",
        })

    self.__seq_keyword = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_seq_keyword(self):
    self.__seq_keyword = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'seq': {'value': 1}},), is_leaf=True, yang_name="seq-keyword", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='enumeration', is_config=True)


  def _get_instance(self):
    """
    Getter method for instance, mapped from YANG variable /routing_system/ipv6/prefix_list/instance (instance-id-t)
    """
    return self.__instance
      
  def _set_instance(self, v, load=False):
    """
    Setter method for instance, mapped from YANG variable /routing_system/ipv6/prefix_list/instance (instance-id-t)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_instance is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_instance() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="instance", rest_name="instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='instance-id-t', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """instance must be of a type compatible with instance-id-t""",
          'defined-type': "brocade-ip-policy:instance-id-t",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="instance", rest_name="instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='instance-id-t', is_config=True)""",
        })

    self.__instance = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_instance(self):
    self.__instance = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="instance", rest_name="instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='instance-id-t', is_config=True)


  def _get_action_ipp(self):
    """
    Getter method for action_ipp, mapped from YANG variable /routing_system/ipv6/prefix_list/action_ipp (action-t)
    """
    return self.__action_ipp
      
  def _set_action_ipp(self, v, load=False):
    """
    Setter method for action_ipp, mapped from YANG variable /routing_system/ipv6/prefix_list/action_ipp (action-t)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_action_ipp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_action_ipp() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'receive': {'value': 2}, u'send': {'value': 1}},), is_leaf=True, yang_name="action-ipp", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='action-t', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """action_ipp must be of a type compatible with action-t""",
          'defined-type': "brocade-ip-policy:action-t",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'receive': {'value': 2}, u'send': {'value': 1}},), is_leaf=True, yang_name="action-ipp", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='action-t', is_config=True)""",
        })

    self.__action_ipp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_action_ipp(self):
    self.__action_ipp = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'receive': {'value': 2}, u'send': {'value': 1}},), is_leaf=True, yang_name="action-ipp", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='action-t', is_config=True)


  def _get_ipv6_prefix_ipp(self):
    """
    Getter method for ipv6_prefix_ipp, mapped from YANG variable /routing_system/ipv6/prefix_list/ipv6_prefix_ipp (inet:ipv6-prefix)
    """
    return self.__ipv6_prefix_ipp
      
  def _set_ipv6_prefix_ipp(self, v, load=False):
    """
    Setter method for ipv6_prefix_ipp, mapped from YANG variable /routing_system/ipv6/prefix_list/ipv6_prefix_ipp (inet:ipv6-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_prefix_ipp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_prefix_ipp() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="ipv6-prefix-ipp", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='inet:ipv6-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_prefix_ipp must be of a type compatible with inet:ipv6-prefix""",
          'defined-type': "inet:ipv6-prefix",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="ipv6-prefix-ipp", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='inet:ipv6-prefix', is_config=True)""",
        })

    self.__ipv6_prefix_ipp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_prefix_ipp(self):
    self.__ipv6_prefix_ipp = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="ipv6-prefix-ipp", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='inet:ipv6-prefix', is_config=True)


  def _get_ge_ipp(self):
    """
    Getter method for ge_ipp, mapped from YANG variable /routing_system/ipv6/prefix_list/ge_ipp (ipv6-prefix-len-t)

    YANG Description: Minimum IPv6 prefix length.
    """
    return self.__ge_ipp
      
  def _set_ge_ipp(self, v, load=False):
    """
    Setter method for ge_ipp, mapped from YANG variable /routing_system/ipv6/prefix_list/ge_ipp (ipv6-prefix-len-t)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ge_ipp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ge_ipp() directly.

    YANG Description: Minimum IPv6 prefix length.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..128']}), is_leaf=True, yang_name="ge-ipp", rest_name="ge", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Minimum IPv6 prefix length.', u'alt-name': u'ge', u'cli-suppress-no': None, u'cli-break-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ipv6-prefix-len-t', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ge_ipp must be of a type compatible with ipv6-prefix-len-t""",
          'defined-type': "brocade-ip-policy:ipv6-prefix-len-t",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..128']}), is_leaf=True, yang_name="ge-ipp", rest_name="ge", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Minimum IPv6 prefix length.', u'alt-name': u'ge', u'cli-suppress-no': None, u'cli-break-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ipv6-prefix-len-t', is_config=True)""",
        })

    self.__ge_ipp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ge_ipp(self):
    self.__ge_ipp = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..128']}), is_leaf=True, yang_name="ge-ipp", rest_name="ge", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Minimum IPv6 prefix length.', u'alt-name': u'ge', u'cli-suppress-no': None, u'cli-break-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ipv6-prefix-len-t', is_config=True)


  def _get_le_ipp(self):
    """
    Getter method for le_ipp, mapped from YANG variable /routing_system/ipv6/prefix_list/le_ipp (ipv6-prefix-len-t)

    YANG Description: Maximum IPv6 prefix length.
    """
    return self.__le_ipp
      
  def _set_le_ipp(self, v, load=False):
    """
    Setter method for le_ipp, mapped from YANG variable /routing_system/ipv6/prefix_list/le_ipp (ipv6-prefix-len-t)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_le_ipp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_le_ipp() directly.

    YANG Description: Maximum IPv6 prefix length.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..128']}), is_leaf=True, yang_name="le-ipp", rest_name="le", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Maximum IPv6 prefix length.', u'alt-name': u'le', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ipv6-prefix-len-t', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """le_ipp must be of a type compatible with ipv6-prefix-len-t""",
          'defined-type': "brocade-ip-policy:ipv6-prefix-len-t",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..128']}), is_leaf=True, yang_name="le-ipp", rest_name="le", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Maximum IPv6 prefix length.', u'alt-name': u'le', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ipv6-prefix-len-t', is_config=True)""",
        })

    self.__le_ipp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_le_ipp(self):
    self.__le_ipp = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..128']}), is_leaf=True, yang_name="le-ipp", rest_name="le", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Maximum IPv6 prefix length.', u'alt-name': u'le', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ipv6-prefix-len-t', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  seq_keyword = __builtin__.property(_get_seq_keyword, _set_seq_keyword)
  instance = __builtin__.property(_get_instance, _set_instance)
  action_ipp = __builtin__.property(_get_action_ipp, _set_action_ipp)
  ipv6_prefix_ipp = __builtin__.property(_get_ipv6_prefix_ipp, _set_ipv6_prefix_ipp)
  ge_ipp = __builtin__.property(_get_ge_ipp, _set_ge_ipp)
  le_ipp = __builtin__.property(_get_le_ipp, _set_le_ipp)


  _pyangbind_elements = {'name': name, 'seq_keyword': seq_keyword, 'instance': instance, 'action_ipp': action_ipp, 'ipv6_prefix_ipp': ipv6_prefix_ipp, 'ge_ipp': ge_ipp, 'le_ipp': le_ipp, }


