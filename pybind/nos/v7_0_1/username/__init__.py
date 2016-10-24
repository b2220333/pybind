
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class username(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-aaa - based on the path /username. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__name','__user_password','__encryption_level','__role','__desc','__enable','__expire','__access_time','__end_time',)

  _yang_name = 'username'
  _rest_name = 'username'

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
    self.__encryption_level = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'0': {'value': 0}, u'7': {'value': 7}},), is_leaf=True, yang_name="encryption-level", rest_name="encryption-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Level of encryption of the password\n(default=0)', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='enumeration', is_config=True)
    self.__enable = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Represents whether the user account is enabled\n(default=true)', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='username-enable', is_config=True)
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 40']}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)
    self.__access_time = YANGDynClass(base=unicode, default=unicode(""), is_leaf=True, yang_name="access-time", rest_name="access-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Granting user access for configured time period from', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)
    self.__user_password = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..40']}), is_leaf=True, yang_name="user-password", rest_name="password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Password of the user', u'alt-name': u'password'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='user-passwd', is_config=True)
    self.__expire = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((19(0[2-9]|[1-9][0-9])|20([012][0-9]|3[0-7]))-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01]))|never', 'length': [u'0 .. 10']}), default=unicode("never"), is_leaf=True, yang_name="expire", rest_name="expire", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Date until when the password will remain valid after being updated\n(default=never)', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='date', is_config=True)
    self.__role = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'4 .. 32']}), is_leaf=True, yang_name="role", rest_name="role", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Role of the user'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)
    self.__end_time = YANGDynClass(base=unicode, default=unicode(""), is_leaf=True, yang_name="end-time", rest_name="to", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'To time period granting user access', u'alt-name': u'to', u'cli-suppress-no': None, u'display-when': u'(../access-time)'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)
    self.__desc = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0 .. 64']}), default=unicode(""), is_leaf=True, yang_name="desc", rest_name="desc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u"Description of the user (default='')", u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)

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
      return [u'username']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'username']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /username/name (string)
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /username/name (string)
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
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 40']}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 40']}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 40']}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)


  def _get_user_password(self):
    """
    Getter method for user_password, mapped from YANG variable /username/user_password (user-passwd)
    """
    return self.__user_password
      
  def _set_user_password(self, v, load=False):
    """
    Setter method for user_password, mapped from YANG variable /username/user_password (user-passwd)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_user_password is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_user_password() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..40']}), is_leaf=True, yang_name="user-password", rest_name="password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Password of the user', u'alt-name': u'password'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='user-passwd', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """user_password must be of a type compatible with user-passwd""",
          'defined-type': "brocade-aaa:user-passwd",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..40']}), is_leaf=True, yang_name="user-password", rest_name="password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Password of the user', u'alt-name': u'password'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='user-passwd', is_config=True)""",
        })

    self.__user_password = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_user_password(self):
    self.__user_password = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..40']}), is_leaf=True, yang_name="user-password", rest_name="password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Password of the user', u'alt-name': u'password'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='user-passwd', is_config=True)


  def _get_encryption_level(self):
    """
    Getter method for encryption_level, mapped from YANG variable /username/encryption_level (enumeration)
    """
    return self.__encryption_level
      
  def _set_encryption_level(self, v, load=False):
    """
    Setter method for encryption_level, mapped from YANG variable /username/encryption_level (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_encryption_level is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_encryption_level() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'0': {'value': 0}, u'7': {'value': 7}},), is_leaf=True, yang_name="encryption-level", rest_name="encryption-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Level of encryption of the password\n(default=0)', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """encryption_level must be of a type compatible with enumeration""",
          'defined-type': "brocade-aaa:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'0': {'value': 0}, u'7': {'value': 7}},), is_leaf=True, yang_name="encryption-level", rest_name="encryption-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Level of encryption of the password\n(default=0)', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='enumeration', is_config=True)""",
        })

    self.__encryption_level = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_encryption_level(self):
    self.__encryption_level = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'0': {'value': 0}, u'7': {'value': 7}},), is_leaf=True, yang_name="encryption-level", rest_name="encryption-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Level of encryption of the password\n(default=0)', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='enumeration', is_config=True)


  def _get_role(self):
    """
    Getter method for role, mapped from YANG variable /username/role (string)
    """
    return self.__role
      
  def _set_role(self, v, load=False):
    """
    Setter method for role, mapped from YANG variable /username/role (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_role is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_role() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'4 .. 32']}), is_leaf=True, yang_name="role", rest_name="role", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Role of the user'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """role must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'4 .. 32']}), is_leaf=True, yang_name="role", rest_name="role", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Role of the user'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)""",
        })

    self.__role = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_role(self):
    self.__role = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'4 .. 32']}), is_leaf=True, yang_name="role", rest_name="role", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Role of the user'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)


  def _get_desc(self):
    """
    Getter method for desc, mapped from YANG variable /username/desc (string)
    """
    return self.__desc
      
  def _set_desc(self, v, load=False):
    """
    Setter method for desc, mapped from YANG variable /username/desc (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_desc is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_desc() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0 .. 64']}), default=unicode(""), is_leaf=True, yang_name="desc", rest_name="desc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u"Description of the user (default='')", u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """desc must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0 .. 64']}), default=unicode(""), is_leaf=True, yang_name="desc", rest_name="desc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u"Description of the user (default='')", u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)""",
        })

    self.__desc = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_desc(self):
    self.__desc = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0 .. 64']}), default=unicode(""), is_leaf=True, yang_name="desc", rest_name="desc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u"Description of the user (default='')", u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)


  def _get_enable(self):
    """
    Getter method for enable, mapped from YANG variable /username/enable (username-enable)
    """
    return self.__enable
      
  def _set_enable(self, v, load=False):
    """
    Setter method for enable, mapped from YANG variable /username/enable (username-enable)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Represents whether the user account is enabled\n(default=true)', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='username-enable', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable must be of a type compatible with username-enable""",
          'defined-type': "brocade-aaa:username-enable",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Represents whether the user account is enabled\n(default=true)', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='username-enable', is_config=True)""",
        })

    self.__enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable(self):
    self.__enable = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Represents whether the user account is enabled\n(default=true)', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='username-enable', is_config=True)


  def _get_expire(self):
    """
    Getter method for expire, mapped from YANG variable /username/expire (date)
    """
    return self.__expire
      
  def _set_expire(self, v, load=False):
    """
    Setter method for expire, mapped from YANG variable /username/expire (date)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_expire is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_expire() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((19(0[2-9]|[1-9][0-9])|20([012][0-9]|3[0-7]))-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01]))|never', 'length': [u'0 .. 10']}), default=unicode("never"), is_leaf=True, yang_name="expire", rest_name="expire", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Date until when the password will remain valid after being updated\n(default=never)', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='date', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """expire must be of a type compatible with date""",
          'defined-type': "brocade-aaa:date",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((19(0[2-9]|[1-9][0-9])|20([012][0-9]|3[0-7]))-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01]))|never', 'length': [u'0 .. 10']}), default=unicode("never"), is_leaf=True, yang_name="expire", rest_name="expire", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Date until when the password will remain valid after being updated\n(default=never)', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='date', is_config=True)""",
        })

    self.__expire = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_expire(self):
    self.__expire = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((19(0[2-9]|[1-9][0-9])|20([012][0-9]|3[0-7]))-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01]))|never', 'length': [u'0 .. 10']}), default=unicode("never"), is_leaf=True, yang_name="expire", rest_name="expire", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Date until when the password will remain valid after being updated\n(default=never)', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='date', is_config=True)


  def _get_access_time(self):
    """
    Getter method for access_time, mapped from YANG variable /username/access_time (string)
    """
    return self.__access_time
      
  def _set_access_time(self, v, load=False):
    """
    Setter method for access_time, mapped from YANG variable /username/access_time (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_access_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_access_time() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, default=unicode(""), is_leaf=True, yang_name="access-time", rest_name="access-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Granting user access for configured time period from', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """access_time must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, default=unicode(""), is_leaf=True, yang_name="access-time", rest_name="access-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Granting user access for configured time period from', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)""",
        })

    self.__access_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_access_time(self):
    self.__access_time = YANGDynClass(base=unicode, default=unicode(""), is_leaf=True, yang_name="access-time", rest_name="access-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Granting user access for configured time period from', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)


  def _get_end_time(self):
    """
    Getter method for end_time, mapped from YANG variable /username/end_time (string)
    """
    return self.__end_time
      
  def _set_end_time(self, v, load=False):
    """
    Setter method for end_time, mapped from YANG variable /username/end_time (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_end_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_end_time() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, default=unicode(""), is_leaf=True, yang_name="end-time", rest_name="to", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'To time period granting user access', u'alt-name': u'to', u'cli-suppress-no': None, u'display-when': u'(../access-time)'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """end_time must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, default=unicode(""), is_leaf=True, yang_name="end-time", rest_name="to", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'To time period granting user access', u'alt-name': u'to', u'cli-suppress-no': None, u'display-when': u'(../access-time)'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)""",
        })

    self.__end_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_end_time(self):
    self.__end_time = YANGDynClass(base=unicode, default=unicode(""), is_leaf=True, yang_name="end-time", rest_name="to", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'To time period granting user access', u'alt-name': u'to', u'cli-suppress-no': None, u'display-when': u'(../access-time)'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  user_password = __builtin__.property(_get_user_password, _set_user_password)
  encryption_level = __builtin__.property(_get_encryption_level, _set_encryption_level)
  role = __builtin__.property(_get_role, _set_role)
  desc = __builtin__.property(_get_desc, _set_desc)
  enable = __builtin__.property(_get_enable, _set_enable)
  expire = __builtin__.property(_get_expire, _set_expire)
  access_time = __builtin__.property(_get_access_time, _set_access_time)
  end_time = __builtin__.property(_get_end_time, _set_end_time)


  _pyangbind_elements = {'name': name, 'user_password': user_password, 'encryption_level': encryption_level, 'role': role, 'desc': desc, 'enable': enable, 'expire': expire, 'access_time': access_time, 'end_time': end_time, }


