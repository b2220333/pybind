
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import rbridge_id
class mcast(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-fabric-service - based on the path /fabric/route/mcast. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This function is to configure multicast routing
related information like multicast priority for
a node. Node with highest multicast priority
(and/or lowest RBridge-ID) becomes the root of
the multicast tree.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__rbridge_id',)

  _yang_name = 'mcast'
  _rest_name = 'mcast'

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
    self.__rbridge_id = YANGDynClass(base=YANGListType("rbridge_id",rbridge_id.rbridge_id, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='rbridge-id', extensions={u'tailf-common': {u'info': u'Configure multicast priority for this rbridge', u'callpoint': u'bcastPriority_cp'}}), is_container='list', yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure multicast priority for this rbridge', u'callpoint': u'bcastPriority_cp'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='list', is_config=True)

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
      return [u'fabric', u'route', u'mcast']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'fabric', u'route', u'mcast']

  def _get_rbridge_id(self):
    """
    Getter method for rbridge_id, mapped from YANG variable /fabric/route/mcast/rbridge_id (list)

    YANG Description: This function is to configure multicast
priority for a given RBridge.
    """
    return self.__rbridge_id
      
  def _set_rbridge_id(self, v, load=False):
    """
    Setter method for rbridge_id, mapped from YANG variable /fabric/route/mcast/rbridge_id (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rbridge_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rbridge_id() directly.

    YANG Description: This function is to configure multicast
priority for a given RBridge.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("rbridge_id",rbridge_id.rbridge_id, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='rbridge-id', extensions={u'tailf-common': {u'info': u'Configure multicast priority for this rbridge', u'callpoint': u'bcastPriority_cp'}}), is_container='list', yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure multicast priority for this rbridge', u'callpoint': u'bcastPriority_cp'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rbridge_id must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("rbridge_id",rbridge_id.rbridge_id, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='rbridge-id', extensions={u'tailf-common': {u'info': u'Configure multicast priority for this rbridge', u'callpoint': u'bcastPriority_cp'}}), is_container='list', yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure multicast priority for this rbridge', u'callpoint': u'bcastPriority_cp'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='list', is_config=True)""",
        })

    self.__rbridge_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rbridge_id(self):
    self.__rbridge_id = YANGDynClass(base=YANGListType("rbridge_id",rbridge_id.rbridge_id, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='rbridge-id', extensions={u'tailf-common': {u'info': u'Configure multicast priority for this rbridge', u'callpoint': u'bcastPriority_cp'}}), is_container='list', yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure multicast priority for this rbridge', u'callpoint': u'bcastPriority_cp'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='list', is_config=True)

  rbridge_id = __builtin__.property(_get_rbridge_id, _set_rbridge_id)


  _pyangbind_elements = {'rbridge_id': rbridge_id, }


