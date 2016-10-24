
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class summary_lsa_onstartup(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/ospf/max-metric/router-lsa/on-startup/summary-lsa-onstartup. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__summary_lsa_val_onstartup',)

  _yang_name = 'summary-lsa-onstartup'
  _rest_name = 'summary-lsa'

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
    self.__summary_lsa_val_onstartup = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16777214']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(16711680), is_leaf=True, yang_name="summary-lsa-val-onstartup", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Metric of all summary type 3 and type 4 LSAs', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)

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
      return [u'routing-system', u'router', u'ospf', u'max-metric', u'router-lsa', u'on-startup', u'summary-lsa-onstartup']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'ospf', u'max-metric', u'router-lsa', u'on-startup', u'summary-lsa']

  def _get_summary_lsa_val_onstartup(self):
    """
    Getter method for summary_lsa_val_onstartup, mapped from YANG variable /routing_system/router/ospf/max_metric/router_lsa/on_startup/summary_lsa_onstartup/summary_lsa_val_onstartup (uint32)
    """
    return self.__summary_lsa_val_onstartup
      
  def _set_summary_lsa_val_onstartup(self, v, load=False):
    """
    Setter method for summary_lsa_val_onstartup, mapped from YANG variable /routing_system/router/ospf/max_metric/router_lsa/on_startup/summary_lsa_onstartup/summary_lsa_val_onstartup (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_summary_lsa_val_onstartup is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_summary_lsa_val_onstartup() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16777214']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(16711680), is_leaf=True, yang_name="summary-lsa-val-onstartup", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Metric of all summary type 3 and type 4 LSAs', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """summary_lsa_val_onstartup must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16777214']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(16711680), is_leaf=True, yang_name="summary-lsa-val-onstartup", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Metric of all summary type 3 and type 4 LSAs', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)""",
        })

    self.__summary_lsa_val_onstartup = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_summary_lsa_val_onstartup(self):
    self.__summary_lsa_val_onstartup = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16777214']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(16711680), is_leaf=True, yang_name="summary-lsa-val-onstartup", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Metric of all summary type 3 and type 4 LSAs', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)

  summary_lsa_val_onstartup = __builtin__.property(_get_summary_lsa_val_onstartup, _set_summary_lsa_val_onstartup)


  _pyangbind_elements = {'summary_lsa_val_onstartup': summary_lsa_val_onstartup, }


