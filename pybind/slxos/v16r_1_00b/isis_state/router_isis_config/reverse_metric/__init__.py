
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class reverse_metric(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-isis-operational - based on the path /isis-state/router-isis-config/reverse-metric. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: IS-IS system level reverse-metric configuration
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__reverse_metric_value','__rev_metric_whole_lan','__rev_metric_te_def_metric','__rev_metric_tlv_type',)

  _yang_name = 'reverse-metric'
  _rest_name = 'reverse-metric'

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
    self.__rev_metric_whole_lan = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="rev-metric-whole-lan", rest_name="rev-metric-whole-lan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)
    self.__rev_metric_te_def_metric = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="rev-metric-te-def-metric", rest_name="rev-metric-te-def-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)
    self.__rev_metric_tlv_type = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rev-metric-tlv-type", rest_name="rev-metric-tlv-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    self.__reverse_metric_value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reverse-metric-value", rest_name="reverse-metric-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)

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
      return [u'isis-state', u'router-isis-config', u'reverse-metric']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'isis-state', u'router-isis-config', u'reverse-metric']

  def _get_reverse_metric_value(self):
    """
    Getter method for reverse_metric_value, mapped from YANG variable /isis_state/router_isis_config/reverse_metric/reverse_metric_value (uint32)

    YANG Description: IS-IS reverse metric value
    """
    return self.__reverse_metric_value
      
  def _set_reverse_metric_value(self, v, load=False):
    """
    Setter method for reverse_metric_value, mapped from YANG variable /isis_state/router_isis_config/reverse_metric/reverse_metric_value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reverse_metric_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reverse_metric_value() directly.

    YANG Description: IS-IS reverse metric value
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reverse-metric-value", rest_name="reverse-metric-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reverse_metric_value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reverse-metric-value", rest_name="reverse-metric-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__reverse_metric_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reverse_metric_value(self):
    self.__reverse_metric_value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="reverse-metric-value", rest_name="reverse-metric-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)


  def _get_rev_metric_whole_lan(self):
    """
    Getter method for rev_metric_whole_lan, mapped from YANG variable /isis_state/router_isis_config/reverse_metric/rev_metric_whole_lan (isis-status)

    YANG Description: If IS-IS metric to be changed across whole LAN
    """
    return self.__rev_metric_whole_lan
      
  def _set_rev_metric_whole_lan(self, v, load=False):
    """
    Setter method for rev_metric_whole_lan, mapped from YANG variable /isis_state/router_isis_config/reverse_metric/rev_metric_whole_lan (isis-status)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rev_metric_whole_lan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rev_metric_whole_lan() directly.

    YANG Description: If IS-IS metric to be changed across whole LAN
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="rev-metric-whole-lan", rest_name="rev-metric-whole-lan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rev_metric_whole_lan must be of a type compatible with isis-status""",
          'defined-type': "brocade-isis-operational:isis-status",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="rev-metric-whole-lan", rest_name="rev-metric-whole-lan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)""",
        })

    self.__rev_metric_whole_lan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rev_metric_whole_lan(self):
    self.__rev_metric_whole_lan = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="rev-metric-whole-lan", rest_name="rev-metric-whole-lan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)


  def _get_rev_metric_te_def_metric(self):
    """
    Getter method for rev_metric_te_def_metric, mapped from YANG variable /isis_state/router_isis_config/reverse_metric/rev_metric_te_def_metric (isis-status)

    YANG Description: If TE default-metric subtlv has to be updated
    """
    return self.__rev_metric_te_def_metric
      
  def _set_rev_metric_te_def_metric(self, v, load=False):
    """
    Setter method for rev_metric_te_def_metric, mapped from YANG variable /isis_state/router_isis_config/reverse_metric/rev_metric_te_def_metric (isis-status)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rev_metric_te_def_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rev_metric_te_def_metric() directly.

    YANG Description: If TE default-metric subtlv has to be updated
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="rev-metric-te-def-metric", rest_name="rev-metric-te-def-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rev_metric_te_def_metric must be of a type compatible with isis-status""",
          'defined-type': "brocade-isis-operational:isis-status",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="rev-metric-te-def-metric", rest_name="rev-metric-te-def-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)""",
        })

    self.__rev_metric_te_def_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rev_metric_te_def_metric(self):
    self.__rev_metric_te_def_metric = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="rev-metric-te-def-metric", rest_name="rev-metric-te-def-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)


  def _get_rev_metric_tlv_type(self):
    """
    Getter method for rev_metric_tlv_type, mapped from YANG variable /isis_state/router_isis_config/reverse_metric/rev_metric_tlv_type (uint32)

    YANG Description: IS-IS reverse metric TLV type
    """
    return self.__rev_metric_tlv_type
      
  def _set_rev_metric_tlv_type(self, v, load=False):
    """
    Setter method for rev_metric_tlv_type, mapped from YANG variable /isis_state/router_isis_config/reverse_metric/rev_metric_tlv_type (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rev_metric_tlv_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rev_metric_tlv_type() directly.

    YANG Description: IS-IS reverse metric TLV type
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rev-metric-tlv-type", rest_name="rev-metric-tlv-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rev_metric_tlv_type must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rev-metric-tlv-type", rest_name="rev-metric-tlv-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__rev_metric_tlv_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rev_metric_tlv_type(self):
    self.__rev_metric_tlv_type = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rev-metric-tlv-type", rest_name="rev-metric-tlv-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)

  reverse_metric_value = __builtin__.property(_get_reverse_metric_value)
  rev_metric_whole_lan = __builtin__.property(_get_rev_metric_whole_lan)
  rev_metric_te_def_metric = __builtin__.property(_get_rev_metric_te_def_metric)
  rev_metric_tlv_type = __builtin__.property(_get_rev_metric_tlv_type)


  _pyangbind_elements = {'reverse_metric_value': reverse_metric_value, 'rev_metric_whole_lan': rev_metric_whole_lan, 'rev_metric_te_def_metric': rev_metric_te_def_metric, 'rev_metric_tlv_type': rev_metric_tlv_type, }


