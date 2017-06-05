
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import sec_path
class show_mpls_lsp_sec_path_info(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-bypass-lsp-name-extensive/output/bypass-lsp/show-mpls-lsp-extensive-info/show-mpls-lsp-sec-path-info. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__sec_path',)

  _yang_name = 'show-mpls-lsp-sec-path-info'
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
    self.__sec_path = YANGDynClass(base=YANGListType("lsp_sec_path_path_name",sec_path.sec_path, yang_name="sec-path", rest_name="sec-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-sec-path-path-name', extensions=None), is_container='list', yang_name="sec-path", rest_name="sec-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-bypass-lsp-name-extensive', u'output', u'bypass-lsp', u'show-mpls-lsp-extensive-info', u'show-mpls-lsp-sec-path-info']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-bypass-lsp-name-extensive', u'output', u'bypass-lsp']

  def _get_sec_path(self):
    """
    Getter method for sec_path, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_sec_path_info/sec_path (list)
    """
    return self.__sec_path
      
  def _set_sec_path(self, v, load=False):
    """
    Setter method for sec_path, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_name_extensive/output/bypass_lsp/show_mpls_lsp_extensive_info/show_mpls_lsp_sec_path_info/sec_path (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sec_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sec_path() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("lsp_sec_path_path_name",sec_path.sec_path, yang_name="sec-path", rest_name="sec-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-sec-path-path-name', extensions=None), is_container='list', yang_name="sec-path", rest_name="sec-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sec_path must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("lsp_sec_path_path_name",sec_path.sec_path, yang_name="sec-path", rest_name="sec-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-sec-path-path-name', extensions=None), is_container='list', yang_name="sec-path", rest_name="sec-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)""",
        })

    self.__sec_path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sec_path(self):
    self.__sec_path = YANGDynClass(base=YANGListType("lsp_sec_path_path_name",sec_path.sec_path, yang_name="sec-path", rest_name="sec-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-sec-path-path-name', extensions=None), is_container='list', yang_name="sec-path", rest_name="sec-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)

  sec_path = __builtin__.property(_get_sec_path, _set_sec_path)


  _pyangbind_elements = {'sec_path': sec_path, }


