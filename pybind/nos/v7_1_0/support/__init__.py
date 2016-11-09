
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import autoupload_param
import support_param
import autoupload
class support(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ras - based on the path /support. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__autoupload_param','__support_param','__autoupload','__ffdc',)

  _yang_name = 'support'
  _rest_name = 'support'

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
    self.__autoupload = YANGDynClass(base=autoupload.autoupload, is_container='container', yang_name="autoupload", rest_name="autoupload", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Autoupload Operation', u'callpoint': u'RASAutoUploadCallPoint', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)
    self.__autoupload_param = YANGDynClass(base=autoupload_param.autoupload_param, is_container='container', yang_name="autoupload-param", rest_name="autoupload-param", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure autoupload parameters', u'callpoint': u'RASAutoUploadCallPoint', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)
    self.__support_param = YANGDynClass(base=support_param.support_param, is_container='container', yang_name="support-param", rest_name="support-param", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure copy support parameters', u'callpoint': u'RASCopySupportCallPoint', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)
    self.__ffdc = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ffdc", rest_name="ffdc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable/Disable FFDC file generation', u'cli-full-command': None, u'hidden': u'debug', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='empty', is_config=True)

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
      return [u'support']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'support']

  def _get_autoupload_param(self):
    """
    Getter method for autoupload_param, mapped from YANG variable /support/autoupload_param (container)
    """
    return self.__autoupload_param
      
  def _set_autoupload_param(self, v, load=False):
    """
    Setter method for autoupload_param, mapped from YANG variable /support/autoupload_param (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_autoupload_param is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_autoupload_param() directly.
    """
    try:
      t = YANGDynClass(v,base=autoupload_param.autoupload_param, is_container='container', yang_name="autoupload-param", rest_name="autoupload-param", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure autoupload parameters', u'callpoint': u'RASAutoUploadCallPoint', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """autoupload_param must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=autoupload_param.autoupload_param, is_container='container', yang_name="autoupload-param", rest_name="autoupload-param", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure autoupload parameters', u'callpoint': u'RASAutoUploadCallPoint', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)""",
        })

    self.__autoupload_param = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_autoupload_param(self):
    self.__autoupload_param = YANGDynClass(base=autoupload_param.autoupload_param, is_container='container', yang_name="autoupload-param", rest_name="autoupload-param", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure autoupload parameters', u'callpoint': u'RASAutoUploadCallPoint', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)


  def _get_support_param(self):
    """
    Getter method for support_param, mapped from YANG variable /support/support_param (container)
    """
    return self.__support_param
      
  def _set_support_param(self, v, load=False):
    """
    Setter method for support_param, mapped from YANG variable /support/support_param (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_support_param is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_support_param() directly.
    """
    try:
      t = YANGDynClass(v,base=support_param.support_param, is_container='container', yang_name="support-param", rest_name="support-param", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure copy support parameters', u'callpoint': u'RASCopySupportCallPoint', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """support_param must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=support_param.support_param, is_container='container', yang_name="support-param", rest_name="support-param", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure copy support parameters', u'callpoint': u'RASCopySupportCallPoint', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)""",
        })

    self.__support_param = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_support_param(self):
    self.__support_param = YANGDynClass(base=support_param.support_param, is_container='container', yang_name="support-param", rest_name="support-param", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure copy support parameters', u'callpoint': u'RASCopySupportCallPoint', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)


  def _get_autoupload(self):
    """
    Getter method for autoupload, mapped from YANG variable /support/autoupload (container)
    """
    return self.__autoupload
      
  def _set_autoupload(self, v, load=False):
    """
    Setter method for autoupload, mapped from YANG variable /support/autoupload (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_autoupload is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_autoupload() directly.
    """
    try:
      t = YANGDynClass(v,base=autoupload.autoupload, is_container='container', yang_name="autoupload", rest_name="autoupload", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Autoupload Operation', u'callpoint': u'RASAutoUploadCallPoint', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """autoupload must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=autoupload.autoupload, is_container='container', yang_name="autoupload", rest_name="autoupload", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Autoupload Operation', u'callpoint': u'RASAutoUploadCallPoint', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)""",
        })

    self.__autoupload = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_autoupload(self):
    self.__autoupload = YANGDynClass(base=autoupload.autoupload, is_container='container', yang_name="autoupload", rest_name="autoupload", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Autoupload Operation', u'callpoint': u'RASAutoUploadCallPoint', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)


  def _get_ffdc(self):
    """
    Getter method for ffdc, mapped from YANG variable /support/ffdc (empty)

    YANG Description: FFDC operation
    """
    return self.__ffdc
      
  def _set_ffdc(self, v, load=False):
    """
    Setter method for ffdc, mapped from YANG variable /support/ffdc (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ffdc is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ffdc() directly.

    YANG Description: FFDC operation
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ffdc", rest_name="ffdc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable/Disable FFDC file generation', u'cli-full-command': None, u'hidden': u'debug', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ffdc must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ffdc", rest_name="ffdc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable/Disable FFDC file generation', u'cli-full-command': None, u'hidden': u'debug', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='empty', is_config=True)""",
        })

    self.__ffdc = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ffdc(self):
    self.__ffdc = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ffdc", rest_name="ffdc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable/Disable FFDC file generation', u'cli-full-command': None, u'hidden': u'debug', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='empty', is_config=True)

  autoupload_param = __builtin__.property(_get_autoupload_param, _set_autoupload_param)
  support_param = __builtin__.property(_get_support_param, _set_support_param)
  autoupload = __builtin__.property(_get_autoupload, _set_autoupload)
  ffdc = __builtin__.property(_get_ffdc, _set_ffdc)


  _pyangbind_elements = {'autoupload_param': autoupload_param, 'support_param': support_param, 'autoupload': autoupload, 'ffdc': ffdc, }


