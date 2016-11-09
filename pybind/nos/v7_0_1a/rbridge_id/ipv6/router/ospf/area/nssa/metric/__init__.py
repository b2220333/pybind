
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class metric(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/ipv6/router/ospf/area/nssa/metric. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__nssa_area_metric',)

  _yang_name = 'metric'
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
    self.__nssa_area_metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1048575']}), is_leaf=True, yang_name="nssa-area-metric", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='uint32', is_config=True)

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
      return [u'rbridge-id', u'ipv6', u'router', u'ospf', u'area', u'nssa', u'metric']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'ipv6', u'router', u'ospf', u'area', u'nssa']

  def _get_nssa_area_metric(self):
    """
    Getter method for nssa_area_metric, mapped from YANG variable /rbridge_id/ipv6/router/ospf/area/nssa/metric/nssa_area_metric (uint32)

    YANG Description: NSSA's advertised stub route metricThe metric specifies the cost of the default LSA originated into the NSSA area. The range is 1 to 1048575. There is no default
    """
    return self.__nssa_area_metric
      
  def _set_nssa_area_metric(self, v, load=False):
    """
    Setter method for nssa_area_metric, mapped from YANG variable /rbridge_id/ipv6/router/ospf/area/nssa/metric/nssa_area_metric (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_nssa_area_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_nssa_area_metric() directly.

    YANG Description: NSSA's advertised stub route metricThe metric specifies the cost of the default LSA originated into the NSSA area. The range is 1 to 1048575. There is no default
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1048575']}), is_leaf=True, yang_name="nssa-area-metric", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """nssa_area_metric must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1048575']}), is_leaf=True, yang_name="nssa-area-metric", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='uint32', is_config=True)""",
        })

    self.__nssa_area_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_nssa_area_metric(self):
    self.__nssa_area_metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1048575']}), is_leaf=True, yang_name="nssa-area-metric", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='uint32', is_config=True)

  nssa_area_metric = __builtin__.property(_get_nssa_area_metric, _set_nssa_area_metric)


  _pyangbind_elements = {'nssa_area_metric': nssa_area_metric, }


