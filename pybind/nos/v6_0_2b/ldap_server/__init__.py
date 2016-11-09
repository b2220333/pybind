
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import host
import maprole
class ldap_server(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-aaa - based on the path /ldap-server. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__host','__maprole',)

  _yang_name = 'ldap-server'
  _rest_name = 'ldap-server'

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
    self.__host = YANGDynClass(base=YANGListType("hostname",host.host, yang_name="host", rest_name="host", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='hostname', extensions={u'tailf-common': {u'info': u'Configure a LDAP Server for AAA', u'cli-suppress-key-sort': None, u'callpoint': u'ldap_host_cp', u'cli-suppress-key-abbreviation': None, u'cli-suppress-list-no': None}}), is_container='list', yang_name="host", rest_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a LDAP Server for AAA', u'cli-suppress-key-sort': None, u'callpoint': u'ldap_host_cp', u'cli-suppress-key-abbreviation': None, u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='list', is_config=True)
    self.__maprole = YANGDynClass(base=maprole.maprole, is_container='container', yang_name="maprole", rest_name="maprole", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Maps a role to a group', u'cli-incomplete-no': None, u'sort-priority': u'17'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='container', is_config=True)

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
      return [u'ldap-server']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ldap-server']

  def _get_host(self):
    """
    Getter method for host, mapped from YANG variable /ldap_server/host (list)
    """
    return self.__host
      
  def _set_host(self, v, load=False):
    """
    Setter method for host, mapped from YANG variable /ldap_server/host (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_host is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_host() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("hostname",host.host, yang_name="host", rest_name="host", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='hostname', extensions={u'tailf-common': {u'info': u'Configure a LDAP Server for AAA', u'cli-suppress-key-sort': None, u'callpoint': u'ldap_host_cp', u'cli-suppress-key-abbreviation': None, u'cli-suppress-list-no': None}}), is_container='list', yang_name="host", rest_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a LDAP Server for AAA', u'cli-suppress-key-sort': None, u'callpoint': u'ldap_host_cp', u'cli-suppress-key-abbreviation': None, u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """host must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("hostname",host.host, yang_name="host", rest_name="host", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='hostname', extensions={u'tailf-common': {u'info': u'Configure a LDAP Server for AAA', u'cli-suppress-key-sort': None, u'callpoint': u'ldap_host_cp', u'cli-suppress-key-abbreviation': None, u'cli-suppress-list-no': None}}), is_container='list', yang_name="host", rest_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a LDAP Server for AAA', u'cli-suppress-key-sort': None, u'callpoint': u'ldap_host_cp', u'cli-suppress-key-abbreviation': None, u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='list', is_config=True)""",
        })

    self.__host = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_host(self):
    self.__host = YANGDynClass(base=YANGListType("hostname",host.host, yang_name="host", rest_name="host", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='hostname', extensions={u'tailf-common': {u'info': u'Configure a LDAP Server for AAA', u'cli-suppress-key-sort': None, u'callpoint': u'ldap_host_cp', u'cli-suppress-key-abbreviation': None, u'cli-suppress-list-no': None}}), is_container='list', yang_name="host", rest_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a LDAP Server for AAA', u'cli-suppress-key-sort': None, u'callpoint': u'ldap_host_cp', u'cli-suppress-key-abbreviation': None, u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='list', is_config=True)


  def _get_maprole(self):
    """
    Getter method for maprole, mapped from YANG variable /ldap_server/maprole (container)
    """
    return self.__maprole
      
  def _set_maprole(self, v, load=False):
    """
    Setter method for maprole, mapped from YANG variable /ldap_server/maprole (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_maprole is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_maprole() directly.
    """
    try:
      t = YANGDynClass(v,base=maprole.maprole, is_container='container', yang_name="maprole", rest_name="maprole", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Maps a role to a group', u'cli-incomplete-no': None, u'sort-priority': u'17'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """maprole must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=maprole.maprole, is_container='container', yang_name="maprole", rest_name="maprole", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Maps a role to a group', u'cli-incomplete-no': None, u'sort-priority': u'17'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='container', is_config=True)""",
        })

    self.__maprole = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_maprole(self):
    self.__maprole = YANGDynClass(base=maprole.maprole, is_container='container', yang_name="maprole", rest_name="maprole", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Maps a role to a group', u'cli-incomplete-no': None, u'sort-priority': u'17'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='container', is_config=True)

  host = __builtin__.property(_get_host, _set_host)
  maprole = __builtin__.property(_get_maprole, _set_maprole)


  _pyangbind_elements = {'host': host, 'maprole': maprole, }


