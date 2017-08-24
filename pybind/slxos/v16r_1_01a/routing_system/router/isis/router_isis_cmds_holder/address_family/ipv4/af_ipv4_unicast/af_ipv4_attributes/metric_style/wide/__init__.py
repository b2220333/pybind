
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class wide(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/isis/router-isis-cmds-holder/address-family/ipv4/af-ipv4-unicast/af-ipv4-attributes/metric-style/wide. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__metric_style_wide_level1','__metric_style_wide_level2',)

  _yang_name = 'wide'
  _rest_name = 'wide'

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
    self.__metric_style_wide_level1 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="metric-style-wide-level1", rest_name="level-1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Level-1 Only', u'cli-full-no': None, u'alt-name': u'level-1'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)
    self.__metric_style_wide_level2 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="metric-style-wide-level2", rest_name="level-2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Level-2 Only', u'cli-full-no': None, u'alt-name': u'level-2'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'router', u'isis', u'router-isis-cmds-holder', u'address-family', u'ipv4', u'af-ipv4-unicast', u'af-ipv4-attributes', u'metric-style', u'wide']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'isis', u'address-family', u'ipv4', u'unicast', u'metric-style', u'wide']

  def _get_metric_style_wide_level1(self):
    """
    Getter method for metric_style_wide_level1, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/metric_style/wide/metric_style_wide_level1 (empty)
    """
    return self.__metric_style_wide_level1
      
  def _set_metric_style_wide_level1(self, v, load=False):
    """
    Setter method for metric_style_wide_level1, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/metric_style/wide/metric_style_wide_level1 (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_metric_style_wide_level1 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_metric_style_wide_level1() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="metric-style-wide-level1", rest_name="level-1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Level-1 Only', u'cli-full-no': None, u'alt-name': u'level-1'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """metric_style_wide_level1 must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="metric-style-wide-level1", rest_name="level-1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Level-1 Only', u'cli-full-no': None, u'alt-name': u'level-1'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)""",
        })

    self.__metric_style_wide_level1 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_metric_style_wide_level1(self):
    self.__metric_style_wide_level1 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="metric-style-wide-level1", rest_name="level-1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Level-1 Only', u'cli-full-no': None, u'alt-name': u'level-1'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)


  def _get_metric_style_wide_level2(self):
    """
    Getter method for metric_style_wide_level2, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/metric_style/wide/metric_style_wide_level2 (empty)
    """
    return self.__metric_style_wide_level2
      
  def _set_metric_style_wide_level2(self, v, load=False):
    """
    Setter method for metric_style_wide_level2, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/metric_style/wide/metric_style_wide_level2 (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_metric_style_wide_level2 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_metric_style_wide_level2() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="metric-style-wide-level2", rest_name="level-2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Level-2 Only', u'cli-full-no': None, u'alt-name': u'level-2'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """metric_style_wide_level2 must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="metric-style-wide-level2", rest_name="level-2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Level-2 Only', u'cli-full-no': None, u'alt-name': u'level-2'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)""",
        })

    self.__metric_style_wide_level2 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_metric_style_wide_level2(self):
    self.__metric_style_wide_level2 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="metric-style-wide-level2", rest_name="level-2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Level-2 Only', u'cli-full-no': None, u'alt-name': u'level-2'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)

  metric_style_wide_level1 = __builtin__.property(_get_metric_style_wide_level1, _set_metric_style_wide_level1)
  metric_style_wide_level2 = __builtin__.property(_get_metric_style_wide_level2, _set_metric_style_wide_level2)


  _pyangbind_elements = {'metric_style_wide_level1': metric_style_wide_level1, 'metric_style_wide_level2': metric_style_wide_level2, }


