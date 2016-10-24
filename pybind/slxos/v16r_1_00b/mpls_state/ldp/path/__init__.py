
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import upstream_sessions
import downstream_sessions
class path(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/ldp/path. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description:  LDP Path information
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__destination_route','__upstream_sessions','__downstream_sessions',)

  _yang_name = 'path'
  _rest_name = 'path'

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
    self.__upstream_sessions = YANGDynClass(base=YANGListType("ip",upstream_sessions.upstream_sessions, yang_name="upstream-sessions", rest_name="upstream-sessions", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip', extensions={u'tailf-common': {u'callpoint': u'mpls-path-stream-upstream-sessions-1'}}), is_container='list', yang_name="upstream-sessions", rest_name="upstream-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-path-stream-upstream-sessions-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    self.__downstream_sessions = YANGDynClass(base=YANGListType("ip",downstream_sessions.downstream_sessions, yang_name="downstream-sessions", rest_name="downstream-sessions", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip', extensions={u'tailf-common': {u'callpoint': u'mpls-path-stream-downstream-sessions-1'}}), is_container='list', yang_name="downstream-sessions", rest_name="downstream-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-path-stream-downstream-sessions-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    self.__destination_route = YANGDynClass(base=unicode, is_leaf=True, yang_name="destination-route", rest_name="destination-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)

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
      return [u'mpls-state', u'ldp', u'path']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'ldp', u'path']

  def _get_destination_route(self):
    """
    Getter method for destination_route, mapped from YANG variable /mpls_state/ldp/path/destination_route (string)

    YANG Description: mpls_ldp_destination_route
    """
    return self.__destination_route
      
  def _set_destination_route(self, v, load=False):
    """
    Setter method for destination_route, mapped from YANG variable /mpls_state/ldp/path/destination_route (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_destination_route is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_destination_route() directly.

    YANG Description: mpls_ldp_destination_route
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="destination-route", rest_name="destination-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """destination_route must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="destination-route", rest_name="destination-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)""",
        })

    self.__destination_route = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_destination_route(self):
    self.__destination_route = YANGDynClass(base=unicode, is_leaf=True, yang_name="destination-route", rest_name="destination-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)


  def _get_upstream_sessions(self):
    """
    Getter method for upstream_sessions, mapped from YANG variable /mpls_state/ldp/path/upstream_sessions (list)
    """
    return self.__upstream_sessions
      
  def _set_upstream_sessions(self, v, load=False):
    """
    Setter method for upstream_sessions, mapped from YANG variable /mpls_state/ldp/path/upstream_sessions (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_upstream_sessions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_upstream_sessions() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("ip",upstream_sessions.upstream_sessions, yang_name="upstream-sessions", rest_name="upstream-sessions", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip', extensions={u'tailf-common': {u'callpoint': u'mpls-path-stream-upstream-sessions-1'}}), is_container='list', yang_name="upstream-sessions", rest_name="upstream-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-path-stream-upstream-sessions-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """upstream_sessions must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ip",upstream_sessions.upstream_sessions, yang_name="upstream-sessions", rest_name="upstream-sessions", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip', extensions={u'tailf-common': {u'callpoint': u'mpls-path-stream-upstream-sessions-1'}}), is_container='list', yang_name="upstream-sessions", rest_name="upstream-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-path-stream-upstream-sessions-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)""",
        })

    self.__upstream_sessions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_upstream_sessions(self):
    self.__upstream_sessions = YANGDynClass(base=YANGListType("ip",upstream_sessions.upstream_sessions, yang_name="upstream-sessions", rest_name="upstream-sessions", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip', extensions={u'tailf-common': {u'callpoint': u'mpls-path-stream-upstream-sessions-1'}}), is_container='list', yang_name="upstream-sessions", rest_name="upstream-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-path-stream-upstream-sessions-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)


  def _get_downstream_sessions(self):
    """
    Getter method for downstream_sessions, mapped from YANG variable /mpls_state/ldp/path/downstream_sessions (list)
    """
    return self.__downstream_sessions
      
  def _set_downstream_sessions(self, v, load=False):
    """
    Setter method for downstream_sessions, mapped from YANG variable /mpls_state/ldp/path/downstream_sessions (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_downstream_sessions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_downstream_sessions() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("ip",downstream_sessions.downstream_sessions, yang_name="downstream-sessions", rest_name="downstream-sessions", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip', extensions={u'tailf-common': {u'callpoint': u'mpls-path-stream-downstream-sessions-1'}}), is_container='list', yang_name="downstream-sessions", rest_name="downstream-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-path-stream-downstream-sessions-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """downstream_sessions must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ip",downstream_sessions.downstream_sessions, yang_name="downstream-sessions", rest_name="downstream-sessions", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip', extensions={u'tailf-common': {u'callpoint': u'mpls-path-stream-downstream-sessions-1'}}), is_container='list', yang_name="downstream-sessions", rest_name="downstream-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-path-stream-downstream-sessions-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)""",
        })

    self.__downstream_sessions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_downstream_sessions(self):
    self.__downstream_sessions = YANGDynClass(base=YANGListType("ip",downstream_sessions.downstream_sessions, yang_name="downstream-sessions", rest_name="downstream-sessions", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip', extensions={u'tailf-common': {u'callpoint': u'mpls-path-stream-downstream-sessions-1'}}), is_container='list', yang_name="downstream-sessions", rest_name="downstream-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-path-stream-downstream-sessions-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)

  destination_route = __builtin__.property(_get_destination_route)
  upstream_sessions = __builtin__.property(_get_upstream_sessions)
  downstream_sessions = __builtin__.property(_get_downstream_sessions)


  _pyangbind_elements = {'destination_route': destination_route, 'upstream_sessions': upstream_sessions, 'downstream_sessions': downstream_sessions, }


