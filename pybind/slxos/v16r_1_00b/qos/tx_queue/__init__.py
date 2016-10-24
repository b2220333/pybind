
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import scheduler
class tx_queue(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-mls - based on the path /qos/tx-queue. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__tx_queue_limit','__scheduler',)

  _yang_name = 'tx-queue'
  _rest_name = 'tx-queue'

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
    self.__scheduler = YANGDynClass(base=scheduler.scheduler, is_container='container', yang_name="scheduler", rest_name="scheduler", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Traffic Class Scheduler', u'callpoint': u'unicast_scheduler', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='container', is_config=True)
    self.__tx_queue_limit = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'128 .. 8000']}), is_leaf=True, yang_name="tx-queue-limit", rest_name="limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Egress Queue Limit', u'alt-name': u'limit', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='uint32', is_config=True)

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
      return [u'qos', u'tx-queue']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'qos', u'tx-queue']

  def _get_tx_queue_limit(self):
    """
    Getter method for tx_queue_limit, mapped from YANG variable /qos/tx_queue/tx_queue_limit (uint32)
    """
    return self.__tx_queue_limit
      
  def _set_tx_queue_limit(self, v, load=False):
    """
    Setter method for tx_queue_limit, mapped from YANG variable /qos/tx_queue/tx_queue_limit (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tx_queue_limit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tx_queue_limit() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'128 .. 8000']}), is_leaf=True, yang_name="tx-queue-limit", rest_name="limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Egress Queue Limit', u'alt-name': u'limit', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tx_queue_limit must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'128 .. 8000']}), is_leaf=True, yang_name="tx-queue-limit", rest_name="limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Egress Queue Limit', u'alt-name': u'limit', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='uint32', is_config=True)""",
        })

    self.__tx_queue_limit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tx_queue_limit(self):
    self.__tx_queue_limit = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'128 .. 8000']}), is_leaf=True, yang_name="tx-queue-limit", rest_name="limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Egress Queue Limit', u'alt-name': u'limit', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='uint32', is_config=True)


  def _get_scheduler(self):
    """
    Getter method for scheduler, mapped from YANG variable /qos/tx_queue/scheduler (container)
    """
    return self.__scheduler
      
  def _set_scheduler(self, v, load=False):
    """
    Setter method for scheduler, mapped from YANG variable /qos/tx_queue/scheduler (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_scheduler is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_scheduler() directly.
    """
    try:
      t = YANGDynClass(v,base=scheduler.scheduler, is_container='container', yang_name="scheduler", rest_name="scheduler", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Traffic Class Scheduler', u'callpoint': u'unicast_scheduler', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """scheduler must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=scheduler.scheduler, is_container='container', yang_name="scheduler", rest_name="scheduler", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Traffic Class Scheduler', u'callpoint': u'unicast_scheduler', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='container', is_config=True)""",
        })

    self.__scheduler = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_scheduler(self):
    self.__scheduler = YANGDynClass(base=scheduler.scheduler, is_container='container', yang_name="scheduler", rest_name="scheduler", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Traffic Class Scheduler', u'callpoint': u'unicast_scheduler', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='container', is_config=True)

  tx_queue_limit = __builtin__.property(_get_tx_queue_limit, _set_tx_queue_limit)
  scheduler = __builtin__.property(_get_scheduler, _set_scheduler)


  _pyangbind_elements = {'tx_queue_limit': tx_queue_limit, 'scheduler': scheduler, }


