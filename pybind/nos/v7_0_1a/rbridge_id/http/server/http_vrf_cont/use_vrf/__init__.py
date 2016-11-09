
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class use_vrf(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/http/server/http-vrf-cont/use-vrf. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__use_vrf_name','__http_vrf_shutdown',)

  _yang_name = 'use-vrf'
  _rest_name = 'use-vrf'

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
    self.__http_vrf_shutdown = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="http-vrf-shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shutdown HTTP/HTTPS server on the given vrf', u'cli-full-command': None, u'alt-name': u'shutdown'}}, namespace='urn:brocade.com:mgmt:brocade-http', defining_module='brocade-http-config', yang_type='empty', is_config=True)
    self.__use_vrf_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..max']}), is_leaf=True, yang_name="use-vrf-name", rest_name="use-vrf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-http', defining_module='brocade-http-config', yang_type='string', is_config=True)

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
      return [u'rbridge-id', u'http', u'server', u'http-vrf-cont', u'use-vrf']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'http', u'server', u'use-vrf']

  def _get_use_vrf_name(self):
    """
    Getter method for use_vrf_name, mapped from YANG variable /rbridge_id/http/server/http_vrf_cont/use_vrf/use_vrf_name (string)
    """
    return self.__use_vrf_name
      
  def _set_use_vrf_name(self, v, load=False):
    """
    Setter method for use_vrf_name, mapped from YANG variable /rbridge_id/http/server/http_vrf_cont/use_vrf/use_vrf_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_use_vrf_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_use_vrf_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..max']}), is_leaf=True, yang_name="use-vrf-name", rest_name="use-vrf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-http', defining_module='brocade-http-config', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """use_vrf_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..max']}), is_leaf=True, yang_name="use-vrf-name", rest_name="use-vrf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-http', defining_module='brocade-http-config', yang_type='string', is_config=True)""",
        })

    self.__use_vrf_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_use_vrf_name(self):
    self.__use_vrf_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..max']}), is_leaf=True, yang_name="use-vrf-name", rest_name="use-vrf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-http', defining_module='brocade-http-config', yang_type='string', is_config=True)


  def _get_http_vrf_shutdown(self):
    """
    Getter method for http_vrf_shutdown, mapped from YANG variable /rbridge_id/http/server/http_vrf_cont/use_vrf/http_vrf_shutdown (empty)
    """
    return self.__http_vrf_shutdown
      
  def _set_http_vrf_shutdown(self, v, load=False):
    """
    Setter method for http_vrf_shutdown, mapped from YANG variable /rbridge_id/http/server/http_vrf_cont/use_vrf/http_vrf_shutdown (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_http_vrf_shutdown is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_http_vrf_shutdown() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="http-vrf-shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shutdown HTTP/HTTPS server on the given vrf', u'cli-full-command': None, u'alt-name': u'shutdown'}}, namespace='urn:brocade.com:mgmt:brocade-http', defining_module='brocade-http-config', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """http_vrf_shutdown must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="http-vrf-shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shutdown HTTP/HTTPS server on the given vrf', u'cli-full-command': None, u'alt-name': u'shutdown'}}, namespace='urn:brocade.com:mgmt:brocade-http', defining_module='brocade-http-config', yang_type='empty', is_config=True)""",
        })

    self.__http_vrf_shutdown = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_http_vrf_shutdown(self):
    self.__http_vrf_shutdown = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="http-vrf-shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shutdown HTTP/HTTPS server on the given vrf', u'cli-full-command': None, u'alt-name': u'shutdown'}}, namespace='urn:brocade.com:mgmt:brocade-http', defining_module='brocade-http-config', yang_type='empty', is_config=True)

  use_vrf_name = __builtin__.property(_get_use_vrf_name, _set_use_vrf_name)
  http_vrf_shutdown = __builtin__.property(_get_http_vrf_shutdown, _set_http_vrf_shutdown)


  _pyangbind_elements = {'use_vrf_name': use_vrf_name, 'http_vrf_shutdown': http_vrf_shutdown, }


