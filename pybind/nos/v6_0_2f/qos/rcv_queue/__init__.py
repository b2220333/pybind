
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import multicast
class rcv_queue(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos - based on the path /qos/rcv-queue. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__multicast',)

  _yang_name = 'rcv-queue'
  _rest_name = 'rcv-queue'

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
    self.__multicast = YANGDynClass(base=multicast.multicast, is_container='container', presence=False, yang_name="multicast", rest_name="multicast", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure multicast packet expansion handling', u'callpoint': u'rcv_queue_multicast', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)

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
      return [u'qos', u'rcv-queue']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'qos', u'rcv-queue']

  def _get_multicast(self):
    """
    Getter method for multicast, mapped from YANG variable /qos/rcv_queue/multicast (container)
    """
    return self.__multicast
      
  def _set_multicast(self, v, load=False):
    """
    Setter method for multicast, mapped from YANG variable /qos/rcv_queue/multicast (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_multicast is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_multicast() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=multicast.multicast, is_container='container', presence=False, yang_name="multicast", rest_name="multicast", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure multicast packet expansion handling', u'callpoint': u'rcv_queue_multicast', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """multicast must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=multicast.multicast, is_container='container', presence=False, yang_name="multicast", rest_name="multicast", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure multicast packet expansion handling', u'callpoint': u'rcv_queue_multicast', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)""",
        })

    self.__multicast = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_multicast(self):
    self.__multicast = YANGDynClass(base=multicast.multicast, is_container='container', presence=False, yang_name="multicast", rest_name="multicast", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure multicast packet expansion handling', u'callpoint': u'rcv_queue_multicast', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)

  multicast = __builtin__.property(_get_multicast, _set_multicast)


  _pyangbind_elements = {'multicast': multicast, }


