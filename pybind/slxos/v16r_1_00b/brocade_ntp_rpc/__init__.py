
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import show_ntp
class brocade_ntp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ntp - based on the path /brocade_ntp_rpc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Instrument to configure ntp servers and monitoring active server
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__show_ntp',)

  _yang_name = 'brocade-ntp'
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
    self.__show_ntp = YANGDynClass(base=show_ntp.show_ntp, is_leaf=True, yang_name="show-ntp", rest_name="show-ntp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'ntp-status'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='rpc', is_config=True)

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
      return [u'brocade_ntp_rpc']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return []

  def _get_show_ntp(self):
    """
    Getter method for show_ntp, mapped from YANG variable /brocade_ntp_rpc/show_ntp (rpc)

    YANG Description: show active ntp server for cluster or specified switchid
    """
    return self.__show_ntp
      
  def _set_show_ntp(self, v, load=False):
    """
    Setter method for show_ntp, mapped from YANG variable /brocade_ntp_rpc/show_ntp (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_ntp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_ntp() directly.

    YANG Description: show active ntp server for cluster or specified switchid
    """
    try:
      t = YANGDynClass(v,base=show_ntp.show_ntp, is_leaf=True, yang_name="show-ntp", rest_name="show-ntp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'ntp-status'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_ntp must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=show_ntp.show_ntp, is_leaf=True, yang_name="show-ntp", rest_name="show-ntp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'ntp-status'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='rpc', is_config=True)""",
        })

    self.__show_ntp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_ntp(self):
    self.__show_ntp = YANGDynClass(base=show_ntp.show_ntp, is_leaf=True, yang_name="show-ntp", rest_name="show-ntp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'ntp-status'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='rpc', is_config=True)

  show_ntp = __builtin__.property(_get_show_ntp, _set_show_ntp)


  _pyangbind_elements = {'show_ntp': show_ntp, }


