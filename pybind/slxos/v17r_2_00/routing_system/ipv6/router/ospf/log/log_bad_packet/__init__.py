
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class log_bad_packet(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/ipv6/router/ospf/log/log-bad-packet. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configure logging for bad packets
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__log_bad_packet_checksum',)

  _yang_name = 'log-bad-packet'
  _rest_name = 'bad-packet'

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
    self.__log_bad_packet_checksum = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log-bad-packet-checksum", rest_name="checksum", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Logging bad checksum packets', u'alt-name': u'checksum'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'ipv6', u'router', u'ospf', u'log', u'log-bad-packet']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ipv6', u'router', u'ospf', u'log', u'bad-packet']

  def _get_log_bad_packet_checksum(self):
    """
    Getter method for log_bad_packet_checksum, mapped from YANG variable /routing_system/ipv6/router/ospf/log/log_bad_packet/log_bad_packet_checksum (empty)
    """
    return self.__log_bad_packet_checksum
      
  def _set_log_bad_packet_checksum(self, v, load=False):
    """
    Setter method for log_bad_packet_checksum, mapped from YANG variable /routing_system/ipv6/router/ospf/log/log_bad_packet/log_bad_packet_checksum (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_log_bad_packet_checksum is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_log_bad_packet_checksum() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="log-bad-packet-checksum", rest_name="checksum", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Logging bad checksum packets', u'alt-name': u'checksum'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """log_bad_packet_checksum must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log-bad-packet-checksum", rest_name="checksum", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Logging bad checksum packets', u'alt-name': u'checksum'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)""",
        })

    self.__log_bad_packet_checksum = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_log_bad_packet_checksum(self):
    self.__log_bad_packet_checksum = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log-bad-packet-checksum", rest_name="checksum", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Logging bad checksum packets', u'alt-name': u'checksum'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)

  log_bad_packet_checksum = __builtin__.property(_get_log_bad_packet_checksum, _set_log_bad_packet_checksum)


  _pyangbind_elements = {'log_bad_packet_checksum': log_bad_packet_checksum, }


