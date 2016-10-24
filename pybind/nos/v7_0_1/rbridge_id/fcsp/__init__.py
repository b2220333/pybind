
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import auth
class fcsp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/fcsp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__auth',)

  _yang_name = 'fcsp'
  _rest_name = 'fcsp'

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
    self.__auth = YANGDynClass(base=auth.auth, is_container='container', yang_name="auth", rest_name="auth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Authentication type configuration', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fc-auth', defining_module='brocade-fc-auth', yang_type='container', is_config=True)

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
      return [u'rbridge-id', u'fcsp']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'fcsp']

  def _get_auth(self):
    """
    Getter method for auth, mapped from YANG variable /rbridge_id/fcsp/auth (container)
    """
    return self.__auth
      
  def _set_auth(self, v, load=False):
    """
    Setter method for auth, mapped from YANG variable /rbridge_id/fcsp/auth (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth() directly.
    """
    try:
      t = YANGDynClass(v,base=auth.auth, is_container='container', yang_name="auth", rest_name="auth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Authentication type configuration', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fc-auth', defining_module='brocade-fc-auth', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=auth.auth, is_container='container', yang_name="auth", rest_name="auth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Authentication type configuration', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fc-auth', defining_module='brocade-fc-auth', yang_type='container', is_config=True)""",
        })

    self.__auth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth(self):
    self.__auth = YANGDynClass(base=auth.auth, is_container='container', yang_name="auth", rest_name="auth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Authentication type configuration', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fc-auth', defining_module='brocade-fc-auth', yang_type='container', is_config=True)

  auth = __builtin__.property(_get_auth, _set_auth)


  _pyangbind_elements = {'auth': auth, }


