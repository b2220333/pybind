
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import heavy
import queue
class bp_rate_limit(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/bp-rate-limit. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__heavy','__queue',)

  _yang_name = 'bp-rate-limit'
  _rest_name = 'bp-rate-limit'

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
    self.__heavy = YANGDynClass(base=heavy.heavy, is_container='container', yang_name="heavy", rest_name="heavy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'bp-rate-limit under  heavy load', u'callpoint': u'bpratelimit', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-bprate-limit', defining_module='brocade-bprate-limit', yang_type='container', is_config=True)
    self.__queue = YANGDynClass(base=YANGListType("queue_id",queue.queue, yang_name="queue", rest_name="queue", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='queue-id', extensions={u'tailf-common': {u'info': u'Configure BP queue', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'hidden': u'performance-tuning', u'callpoint': u'bpratelimitQueue'}}), is_container='list', yang_name="queue", rest_name="queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BP queue', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'hidden': u'performance-tuning', u'callpoint': u'bpratelimitQueue'}}, namespace='urn:brocade.com:mgmt:brocade-bprate-limit', defining_module='brocade-bprate-limit', yang_type='list', is_config=True)

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
      return [u'rbridge-id', u'bp-rate-limit']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'bp-rate-limit']

  def _get_heavy(self):
    """
    Getter method for heavy, mapped from YANG variable /rbridge_id/bp_rate_limit/heavy (container)
    """
    return self.__heavy
      
  def _set_heavy(self, v, load=False):
    """
    Setter method for heavy, mapped from YANG variable /rbridge_id/bp_rate_limit/heavy (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_heavy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_heavy() directly.
    """
    try:
      t = YANGDynClass(v,base=heavy.heavy, is_container='container', yang_name="heavy", rest_name="heavy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'bp-rate-limit under  heavy load', u'callpoint': u'bpratelimit', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-bprate-limit', defining_module='brocade-bprate-limit', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """heavy must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=heavy.heavy, is_container='container', yang_name="heavy", rest_name="heavy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'bp-rate-limit under  heavy load', u'callpoint': u'bpratelimit', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-bprate-limit', defining_module='brocade-bprate-limit', yang_type='container', is_config=True)""",
        })

    self.__heavy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_heavy(self):
    self.__heavy = YANGDynClass(base=heavy.heavy, is_container='container', yang_name="heavy", rest_name="heavy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'bp-rate-limit under  heavy load', u'callpoint': u'bpratelimit', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-bprate-limit', defining_module='brocade-bprate-limit', yang_type='container', is_config=True)


  def _get_queue(self):
    """
    Getter method for queue, mapped from YANG variable /rbridge_id/bp_rate_limit/queue (list)
    """
    return self.__queue
      
  def _set_queue(self, v, load=False):
    """
    Setter method for queue, mapped from YANG variable /rbridge_id/bp_rate_limit/queue (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_queue is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_queue() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("queue_id",queue.queue, yang_name="queue", rest_name="queue", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='queue-id', extensions={u'tailf-common': {u'info': u'Configure BP queue', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'hidden': u'performance-tuning', u'callpoint': u'bpratelimitQueue'}}), is_container='list', yang_name="queue", rest_name="queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BP queue', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'hidden': u'performance-tuning', u'callpoint': u'bpratelimitQueue'}}, namespace='urn:brocade.com:mgmt:brocade-bprate-limit', defining_module='brocade-bprate-limit', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """queue must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("queue_id",queue.queue, yang_name="queue", rest_name="queue", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='queue-id', extensions={u'tailf-common': {u'info': u'Configure BP queue', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'hidden': u'performance-tuning', u'callpoint': u'bpratelimitQueue'}}), is_container='list', yang_name="queue", rest_name="queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BP queue', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'hidden': u'performance-tuning', u'callpoint': u'bpratelimitQueue'}}, namespace='urn:brocade.com:mgmt:brocade-bprate-limit', defining_module='brocade-bprate-limit', yang_type='list', is_config=True)""",
        })

    self.__queue = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_queue(self):
    self.__queue = YANGDynClass(base=YANGListType("queue_id",queue.queue, yang_name="queue", rest_name="queue", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='queue-id', extensions={u'tailf-common': {u'info': u'Configure BP queue', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'hidden': u'performance-tuning', u'callpoint': u'bpratelimitQueue'}}), is_container='list', yang_name="queue", rest_name="queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BP queue', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'hidden': u'performance-tuning', u'callpoint': u'bpratelimitQueue'}}, namespace='urn:brocade.com:mgmt:brocade-bprate-limit', defining_module='brocade-bprate-limit', yang_type='list', is_config=True)

  heavy = __builtin__.property(_get_heavy, _set_heavy)
  queue = __builtin__.property(_get_queue, _set_queue)


  _pyangbind_elements = {'heavy': heavy, 'queue': queue, }

