
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import show_raslog
import show_support_save_status
import show_system_info
class brocade_ras_ext(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ras-ext - based on the path /brocade_ras_ext_rpc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This module defines RASLOG related information.
Copyright (c) 2010-11 by Brocade Communications Systems, Inc.
All rights reserved.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__show_raslog','__show_support_save_status','__show_system_info',)

  _yang_name = 'brocade-ras-ext'
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
    self.__show_system_info = YANGDynClass(base=show_system_info.show_system_info, is_leaf=True, yang_name="show-system-info", rest_name="show-system-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'showSystemInfo'}}, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='rpc', is_config=True)
    self.__show_raslog = YANGDynClass(base=show_raslog.show_raslog, is_leaf=True, yang_name="show-raslog", rest_name="show-raslog", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'showRaslog'}}, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='rpc', is_config=True)
    self.__show_support_save_status = YANGDynClass(base=show_support_save_status.show_support_save_status, is_leaf=True, yang_name="show-support-save-status", rest_name="show-support-save-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'showSupportSaveStatus'}}, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='rpc', is_config=True)

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
      return [u'brocade_ras_ext_rpc']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return []

  def _get_show_raslog(self):
    """
    Getter method for show_raslog, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog (rpc)

    YANG Description: Shows the entries of RASLOG
    """
    return self.__show_raslog
      
  def _set_show_raslog(self, v, load=False):
    """
    Setter method for show_raslog, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_raslog is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_raslog() directly.

    YANG Description: Shows the entries of RASLOG
    """
    try:
      t = YANGDynClass(v,base=show_raslog.show_raslog, is_leaf=True, yang_name="show-raslog", rest_name="show-raslog", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'showRaslog'}}, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_raslog must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=show_raslog.show_raslog, is_leaf=True, yang_name="show-raslog", rest_name="show-raslog", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'showRaslog'}}, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='rpc', is_config=True)""",
        })

    self.__show_raslog = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_raslog(self):
    self.__show_raslog = YANGDynClass(base=show_raslog.show_raslog, is_leaf=True, yang_name="show-raslog", rest_name="show-raslog", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'showRaslog'}}, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='rpc', is_config=True)


  def _get_show_support_save_status(self):
    """
    Getter method for show_support_save_status, mapped from YANG variable /brocade_ras_ext_rpc/show_support_save_status (rpc)

    YANG Description: Information on the status of recent support save request
    """
    return self.__show_support_save_status
      
  def _set_show_support_save_status(self, v, load=False):
    """
    Setter method for show_support_save_status, mapped from YANG variable /brocade_ras_ext_rpc/show_support_save_status (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_support_save_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_support_save_status() directly.

    YANG Description: Information on the status of recent support save request
    """
    try:
      t = YANGDynClass(v,base=show_support_save_status.show_support_save_status, is_leaf=True, yang_name="show-support-save-status", rest_name="show-support-save-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'showSupportSaveStatus'}}, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_support_save_status must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=show_support_save_status.show_support_save_status, is_leaf=True, yang_name="show-support-save-status", rest_name="show-support-save-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'showSupportSaveStatus'}}, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='rpc', is_config=True)""",
        })

    self.__show_support_save_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_support_save_status(self):
    self.__show_support_save_status = YANGDynClass(base=show_support_save_status.show_support_save_status, is_leaf=True, yang_name="show-support-save-status", rest_name="show-support-save-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'showSupportSaveStatus'}}, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='rpc', is_config=True)


  def _get_show_system_info(self):
    """
    Getter method for show_system_info, mapped from YANG variable /brocade_ras_ext_rpc/show_system_info (rpc)

    YANG Description: Shows the system information MAC etc.
    """
    return self.__show_system_info
      
  def _set_show_system_info(self, v, load=False):
    """
    Setter method for show_system_info, mapped from YANG variable /brocade_ras_ext_rpc/show_system_info (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_system_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_system_info() directly.

    YANG Description: Shows the system information MAC etc.
    """
    try:
      t = YANGDynClass(v,base=show_system_info.show_system_info, is_leaf=True, yang_name="show-system-info", rest_name="show-system-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'showSystemInfo'}}, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_system_info must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=show_system_info.show_system_info, is_leaf=True, yang_name="show-system-info", rest_name="show-system-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'showSystemInfo'}}, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='rpc', is_config=True)""",
        })

    self.__show_system_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_system_info(self):
    self.__show_system_info = YANGDynClass(base=show_system_info.show_system_info, is_leaf=True, yang_name="show-system-info", rest_name="show-system-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'showSystemInfo'}}, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='rpc', is_config=True)

  show_raslog = __builtin__.property(_get_show_raslog, _set_show_raslog)
  show_support_save_status = __builtin__.property(_get_show_support_save_status, _set_show_support_save_status)
  show_system_info = __builtin__.property(_get_show_system_info, _set_show_system_info)


  _pyangbind_elements = {'show_raslog': show_raslog, 'show_support_save_status': show_support_save_status, 'show_system_info': show_system_info, }

