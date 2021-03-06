
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import router_lsa
class max_metric(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/ipv6/router/ospf/max-metric. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The OSPFv3 max-metric router LSA feature enables OSPFv3 to advertise its locally generated router LSAs with a maximum metric to direct transit traffic away from the router, while still routing for directly connected networks.By advertising the maximum metric, the router will not attract transit traffic. A router which does not handle transit traffic and only forwards packets destined for its directly connected links is known as a stub router. In OSPFv3 networks, a device could be placed in a stub router role by advertising large metrics for its connected links, so that the cost of a path through the device becomes larger than that of an alternative path.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__router_lsa',)

  _yang_name = 'max-metric'
  _rest_name = 'max-metric'

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
    self.__router_lsa = YANGDynClass(base=router_lsa.router_lsa, is_container='container', presence=True, yang_name="router-lsa", rest_name="router-lsa", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The maximum metric advertisement in Router LSAs'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)

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
      return [u'routing-system', u'ipv6', u'router', u'ospf', u'max-metric']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ipv6', u'router', u'ospf', u'max-metric']

  def _get_router_lsa(self):
    """
    Getter method for router_lsa, mapped from YANG variable /routing_system/ipv6/router/ospf/max_metric/router_lsa (container)

    YANG Description: The router-lsa parameter configures the device to advertise the maximum metric for point-to-point and transit links.
    """
    return self.__router_lsa
      
  def _set_router_lsa(self, v, load=False):
    """
    Setter method for router_lsa, mapped from YANG variable /routing_system/ipv6/router/ospf/max_metric/router_lsa (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_router_lsa is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_router_lsa() directly.

    YANG Description: The router-lsa parameter configures the device to advertise the maximum metric for point-to-point and transit links.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=router_lsa.router_lsa, is_container='container', presence=True, yang_name="router-lsa", rest_name="router-lsa", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The maximum metric advertisement in Router LSAs'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """router_lsa must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=router_lsa.router_lsa, is_container='container', presence=True, yang_name="router-lsa", rest_name="router-lsa", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The maximum metric advertisement in Router LSAs'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)""",
        })

    self.__router_lsa = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_router_lsa(self):
    self.__router_lsa = YANGDynClass(base=router_lsa.router_lsa, is_container='container', presence=True, yang_name="router-lsa", rest_name="router-lsa", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The maximum metric advertisement in Router LSAs'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)

  router_lsa = __builtin__.property(_get_router_lsa, _set_router_lsa)


  _pyangbind_elements = {'router_lsa': router_lsa, }


