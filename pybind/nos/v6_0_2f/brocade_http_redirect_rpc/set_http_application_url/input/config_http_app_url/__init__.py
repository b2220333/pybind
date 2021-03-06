
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class config_http_app_url(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-http-redirect - based on the path /brocade_http_redirect_rpc/set-http-application-url/input/config-http-app-url. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__url','__op_type',)

  _yang_name = 'config-http-app-url'
  _rest_name = 'config-http-app-url'

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
    self.__url = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..512']}), is_leaf=True, yang_name="url", rest_name="url", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-http-redirect', defining_module='brocade-http-redirect', yang_type='string', is_config=True)
    self.__op_type = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 1']}), is_leaf=True, yang_name="op-type", rest_name="op-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-http-redirect', defining_module='brocade-http-redirect', yang_type='uint32', is_config=True)

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
      return [u'brocade_http_redirect_rpc', u'set-http-application-url', u'input', u'config-http-app-url']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'set-http-application-url', u'input', u'config-http-app-url']

  def _get_url(self):
    """
    Getter method for url, mapped from YANG variable /brocade_http_redirect_rpc/set_http_application_url/input/config_http_app_url/url (string)

    YANG Description: HTTP application URL
    """
    return self.__url
      
  def _set_url(self, v, load=False):
    """
    Setter method for url, mapped from YANG variable /brocade_http_redirect_rpc/set_http_application_url/input/config_http_app_url/url (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_url is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_url() directly.

    YANG Description: HTTP application URL
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..512']}), is_leaf=True, yang_name="url", rest_name="url", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-http-redirect', defining_module='brocade-http-redirect', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """url must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..512']}), is_leaf=True, yang_name="url", rest_name="url", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-http-redirect', defining_module='brocade-http-redirect', yang_type='string', is_config=True)""",
        })

    self.__url = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_url(self):
    self.__url = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..512']}), is_leaf=True, yang_name="url", rest_name="url", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-http-redirect', defining_module='brocade-http-redirect', yang_type='string', is_config=True)


  def _get_op_type(self):
    """
    Getter method for op_type, mapped from YANG variable /brocade_http_redirect_rpc/set_http_application_url/input/config_http_app_url/op_type (uint32)

    YANG Description: Update URL - 1, unregister URL - 0
    """
    return self.__op_type
      
  def _set_op_type(self, v, load=False):
    """
    Setter method for op_type, mapped from YANG variable /brocade_http_redirect_rpc/set_http_application_url/input/config_http_app_url/op_type (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_op_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_op_type() directly.

    YANG Description: Update URL - 1, unregister URL - 0
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 1']}), is_leaf=True, yang_name="op-type", rest_name="op-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-http-redirect', defining_module='brocade-http-redirect', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """op_type must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 1']}), is_leaf=True, yang_name="op-type", rest_name="op-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-http-redirect', defining_module='brocade-http-redirect', yang_type='uint32', is_config=True)""",
        })

    self.__op_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_op_type(self):
    self.__op_type = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 1']}), is_leaf=True, yang_name="op-type", rest_name="op-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-http-redirect', defining_module='brocade-http-redirect', yang_type='uint32', is_config=True)

  url = __builtin__.property(_get_url, _set_url)
  op_type = __builtin__.property(_get_op_type, _set_op_type)


  _pyangbind_elements = {'url': url, 'op_type': op_type, }


