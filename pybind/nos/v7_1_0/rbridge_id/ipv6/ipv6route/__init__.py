
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import route
class ipv6route(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/ipv6/ipv6route. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__route',)

  _yang_name = 'ipv6route'
  _rest_name = ''

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
    self.__route = YANGDynClass(base=YANGListType("dest",route.route, yang_name="route", rest_name="route", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dest', extensions={u'tailf-common': {u'info': u'Configure ipv6 static route', u'cli-suppress-list-no': None, u'hidden': u'full', u'cli-suppress-mode': None, u'cli-full-no': None}}), is_container='list', yang_name="route", rest_name="route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ipv6 static route', u'cli-suppress-list-no': None, u'hidden': u'full', u'cli-suppress-mode': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-forward', defining_module='brocade-ip-forward', yang_type='list', is_config=True)

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
      return [u'rbridge-id', u'ipv6', u'ipv6route']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'ipv6']

  def _get_route(self):
    """
    Getter method for route, mapped from YANG variable /rbridge_id/ipv6/ipv6route/route (list)
    """
    return self.__route
      
  def _set_route(self, v, load=False):
    """
    Setter method for route, mapped from YANG variable /rbridge_id/ipv6/ipv6route/route (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("dest",route.route, yang_name="route", rest_name="route", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dest', extensions={u'tailf-common': {u'info': u'Configure ipv6 static route', u'cli-suppress-list-no': None, u'hidden': u'full', u'cli-suppress-mode': None, u'cli-full-no': None}}), is_container='list', yang_name="route", rest_name="route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ipv6 static route', u'cli-suppress-list-no': None, u'hidden': u'full', u'cli-suppress-mode': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-forward', defining_module='brocade-ip-forward', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("dest",route.route, yang_name="route", rest_name="route", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dest', extensions={u'tailf-common': {u'info': u'Configure ipv6 static route', u'cli-suppress-list-no': None, u'hidden': u'full', u'cli-suppress-mode': None, u'cli-full-no': None}}), is_container='list', yang_name="route", rest_name="route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ipv6 static route', u'cli-suppress-list-no': None, u'hidden': u'full', u'cli-suppress-mode': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-forward', defining_module='brocade-ip-forward', yang_type='list', is_config=True)""",
        })

    self.__route = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route(self):
    self.__route = YANGDynClass(base=YANGListType("dest",route.route, yang_name="route", rest_name="route", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dest', extensions={u'tailf-common': {u'info': u'Configure ipv6 static route', u'cli-suppress-list-no': None, u'hidden': u'full', u'cli-suppress-mode': None, u'cli-full-no': None}}), is_container='list', yang_name="route", rest_name="route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ipv6 static route', u'cli-suppress-list-no': None, u'hidden': u'full', u'cli-suppress-mode': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-forward', defining_module='brocade-ip-forward', yang_type='list', is_config=True)

  route = __builtin__.property(_get_route, _set_route)


  _pyangbind_elements = {'route': route, }


