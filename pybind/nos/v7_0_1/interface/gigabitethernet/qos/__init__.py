
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import trust
import random_detect
import drop_monitor
import rcv_queue
import flowcontrol
class qos(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/gigabitethernet/qos. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__default_cos','__trust','__cos_mutation','__cos_traffic_class','__dscp_mutation','__dscp_traffic_class','__dscp_cos','__random_detect','__drop_monitor','__rcv_queue','__flowcontrol',)

  _yang_name = 'qos'
  _rest_name = 'qos'

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
    self.__cos_mutation = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="cos-mutation", rest_name="cos-mutation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CoS-to-CoS mutation', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='map-name-type', is_config=True)
    self.__default_cos = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32)(0), is_leaf=True, yang_name="default-cos", rest_name="cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure default Class of Service (CoS)', u'cli-full-command': None, u'alt-name': u'cos', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    self.__dscp_mutation = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-mutation", rest_name="dscp-mutation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure DSCP-to-DSCP mutation', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='map-name-type', is_config=True)
    self.__dscp_traffic_class = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-traffic-class", rest_name="dscp-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure DSCP-to-Traffic Class map', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='map-name-type', is_config=True)
    self.__random_detect = YANGDynClass(base=random_detect.random_detect, is_container='container', yang_name="random-detect", rest_name="random-detect", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Random Early Detect (RED) Profile', u'callpoint': u'cos_profile_te', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)
    self.__cos_traffic_class = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="cos-traffic-class", rest_name="cos-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CoS-to-Traffic Class map', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='map-name-type', is_config=True)
    self.__drop_monitor = YANGDynClass(base=drop_monitor.drop_monitor, is_container='container', yang_name="drop-monitor", rest_name="drop-monitor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure QoS drop monitor polling', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)
    self.__dscp_cos = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-cos", rest_name="dscp-cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure DSCP-to-COS map', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='map-name-type', is_config=True)
    self.__rcv_queue = YANGDynClass(base=rcv_queue.rcv_queue, is_container='container', yang_name="rcv-queue", rest_name="rcv-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Queue Parameters', u'cli-compact-syntax': None, u'callpoint': u'qos_cos_threshold', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)
    self.__flowcontrol = YANGDynClass(base=flowcontrol.flowcontrol, is_container='container', yang_name="flowcontrol", rest_name="flowcontrol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IEEE 802.3x Flow Control', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)
    self.__trust = YANGDynClass(base=trust.trust, is_container='container', yang_name="trust", rest_name="trust", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure QoS Trust', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)

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
      return [u'interface', u'gigabitethernet', u'qos']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'GigabitEthernet', u'qos']

  def _get_default_cos(self):
    """
    Getter method for default_cos, mapped from YANG variable /interface/gigabitethernet/qos/default_cos (int32)
    """
    return self.__default_cos
      
  def _set_default_cos(self, v, load=False):
    """
    Setter method for default_cos, mapped from YANG variable /interface/gigabitethernet/qos/default_cos (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_cos is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_cos() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32)(0), is_leaf=True, yang_name="default-cos", rest_name="cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure default Class of Service (CoS)', u'cli-full-command': None, u'alt-name': u'cos', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_cos must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32)(0), is_leaf=True, yang_name="default-cos", rest_name="cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure default Class of Service (CoS)', u'cli-full-command': None, u'alt-name': u'cos', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)""",
        })

    self.__default_cos = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_cos(self):
    self.__default_cos = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32)(0), is_leaf=True, yang_name="default-cos", rest_name="cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure default Class of Service (CoS)', u'cli-full-command': None, u'alt-name': u'cos', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)


  def _get_trust(self):
    """
    Getter method for trust, mapped from YANG variable /interface/gigabitethernet/qos/trust (container)
    """
    return self.__trust
      
  def _set_trust(self, v, load=False):
    """
    Setter method for trust, mapped from YANG variable /interface/gigabitethernet/qos/trust (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trust is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trust() directly.
    """
    try:
      t = YANGDynClass(v,base=trust.trust, is_container='container', yang_name="trust", rest_name="trust", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure QoS Trust', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trust must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=trust.trust, is_container='container', yang_name="trust", rest_name="trust", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure QoS Trust', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)""",
        })

    self.__trust = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trust(self):
    self.__trust = YANGDynClass(base=trust.trust, is_container='container', yang_name="trust", rest_name="trust", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure QoS Trust', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)


  def _get_cos_mutation(self):
    """
    Getter method for cos_mutation, mapped from YANG variable /interface/gigabitethernet/qos/cos_mutation (map-name-type)
    """
    return self.__cos_mutation
      
  def _set_cos_mutation(self, v, load=False):
    """
    Setter method for cos_mutation, mapped from YANG variable /interface/gigabitethernet/qos/cos_mutation (map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cos_mutation is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cos_mutation() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="cos-mutation", rest_name="cos-mutation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CoS-to-CoS mutation', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cos_mutation must be of a type compatible with map-name-type""",
          'defined-type': "brocade-qos:map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="cos-mutation", rest_name="cos-mutation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CoS-to-CoS mutation', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='map-name-type', is_config=True)""",
        })

    self.__cos_mutation = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cos_mutation(self):
    self.__cos_mutation = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="cos-mutation", rest_name="cos-mutation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CoS-to-CoS mutation', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='map-name-type', is_config=True)


  def _get_cos_traffic_class(self):
    """
    Getter method for cos_traffic_class, mapped from YANG variable /interface/gigabitethernet/qos/cos_traffic_class (map-name-type)
    """
    return self.__cos_traffic_class
      
  def _set_cos_traffic_class(self, v, load=False):
    """
    Setter method for cos_traffic_class, mapped from YANG variable /interface/gigabitethernet/qos/cos_traffic_class (map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cos_traffic_class is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cos_traffic_class() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="cos-traffic-class", rest_name="cos-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CoS-to-Traffic Class map', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cos_traffic_class must be of a type compatible with map-name-type""",
          'defined-type': "brocade-qos:map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="cos-traffic-class", rest_name="cos-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CoS-to-Traffic Class map', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='map-name-type', is_config=True)""",
        })

    self.__cos_traffic_class = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cos_traffic_class(self):
    self.__cos_traffic_class = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="cos-traffic-class", rest_name="cos-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CoS-to-Traffic Class map', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='map-name-type', is_config=True)


  def _get_dscp_mutation(self):
    """
    Getter method for dscp_mutation, mapped from YANG variable /interface/gigabitethernet/qos/dscp_mutation (map-name-type)
    """
    return self.__dscp_mutation
      
  def _set_dscp_mutation(self, v, load=False):
    """
    Setter method for dscp_mutation, mapped from YANG variable /interface/gigabitethernet/qos/dscp_mutation (map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dscp_mutation is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dscp_mutation() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-mutation", rest_name="dscp-mutation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure DSCP-to-DSCP mutation', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dscp_mutation must be of a type compatible with map-name-type""",
          'defined-type': "brocade-qos:map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-mutation", rest_name="dscp-mutation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure DSCP-to-DSCP mutation', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='map-name-type', is_config=True)""",
        })

    self.__dscp_mutation = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dscp_mutation(self):
    self.__dscp_mutation = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-mutation", rest_name="dscp-mutation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure DSCP-to-DSCP mutation', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='map-name-type', is_config=True)


  def _get_dscp_traffic_class(self):
    """
    Getter method for dscp_traffic_class, mapped from YANG variable /interface/gigabitethernet/qos/dscp_traffic_class (map-name-type)
    """
    return self.__dscp_traffic_class
      
  def _set_dscp_traffic_class(self, v, load=False):
    """
    Setter method for dscp_traffic_class, mapped from YANG variable /interface/gigabitethernet/qos/dscp_traffic_class (map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dscp_traffic_class is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dscp_traffic_class() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-traffic-class", rest_name="dscp-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure DSCP-to-Traffic Class map', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dscp_traffic_class must be of a type compatible with map-name-type""",
          'defined-type': "brocade-qos:map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-traffic-class", rest_name="dscp-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure DSCP-to-Traffic Class map', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='map-name-type', is_config=True)""",
        })

    self.__dscp_traffic_class = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dscp_traffic_class(self):
    self.__dscp_traffic_class = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-traffic-class", rest_name="dscp-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure DSCP-to-Traffic Class map', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='map-name-type', is_config=True)


  def _get_dscp_cos(self):
    """
    Getter method for dscp_cos, mapped from YANG variable /interface/gigabitethernet/qos/dscp_cos (map-name-type)
    """
    return self.__dscp_cos
      
  def _set_dscp_cos(self, v, load=False):
    """
    Setter method for dscp_cos, mapped from YANG variable /interface/gigabitethernet/qos/dscp_cos (map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dscp_cos is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dscp_cos() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-cos", rest_name="dscp-cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure DSCP-to-COS map', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dscp_cos must be of a type compatible with map-name-type""",
          'defined-type': "brocade-qos:map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-cos", rest_name="dscp-cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure DSCP-to-COS map', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='map-name-type', is_config=True)""",
        })

    self.__dscp_cos = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dscp_cos(self):
    self.__dscp_cos = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-cos", rest_name="dscp-cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure DSCP-to-COS map', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='map-name-type', is_config=True)


  def _get_random_detect(self):
    """
    Getter method for random_detect, mapped from YANG variable /interface/gigabitethernet/qos/random_detect (container)
    """
    return self.__random_detect
      
  def _set_random_detect(self, v, load=False):
    """
    Setter method for random_detect, mapped from YANG variable /interface/gigabitethernet/qos/random_detect (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_random_detect is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_random_detect() directly.
    """
    try:
      t = YANGDynClass(v,base=random_detect.random_detect, is_container='container', yang_name="random-detect", rest_name="random-detect", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Random Early Detect (RED) Profile', u'callpoint': u'cos_profile_te', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """random_detect must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=random_detect.random_detect, is_container='container', yang_name="random-detect", rest_name="random-detect", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Random Early Detect (RED) Profile', u'callpoint': u'cos_profile_te', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)""",
        })

    self.__random_detect = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_random_detect(self):
    self.__random_detect = YANGDynClass(base=random_detect.random_detect, is_container='container', yang_name="random-detect", rest_name="random-detect", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Random Early Detect (RED) Profile', u'callpoint': u'cos_profile_te', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)


  def _get_drop_monitor(self):
    """
    Getter method for drop_monitor, mapped from YANG variable /interface/gigabitethernet/qos/drop_monitor (container)
    """
    return self.__drop_monitor
      
  def _set_drop_monitor(self, v, load=False):
    """
    Setter method for drop_monitor, mapped from YANG variable /interface/gigabitethernet/qos/drop_monitor (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_drop_monitor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_drop_monitor() directly.
    """
    try:
      t = YANGDynClass(v,base=drop_monitor.drop_monitor, is_container='container', yang_name="drop-monitor", rest_name="drop-monitor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure QoS drop monitor polling', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """drop_monitor must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=drop_monitor.drop_monitor, is_container='container', yang_name="drop-monitor", rest_name="drop-monitor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure QoS drop monitor polling', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)""",
        })

    self.__drop_monitor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_drop_monitor(self):
    self.__drop_monitor = YANGDynClass(base=drop_monitor.drop_monitor, is_container='container', yang_name="drop-monitor", rest_name="drop-monitor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure QoS drop monitor polling', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)


  def _get_rcv_queue(self):
    """
    Getter method for rcv_queue, mapped from YANG variable /interface/gigabitethernet/qos/rcv_queue (container)

    YANG Description: Configure Queue Parameters
    """
    return self.__rcv_queue
      
  def _set_rcv_queue(self, v, load=False):
    """
    Setter method for rcv_queue, mapped from YANG variable /interface/gigabitethernet/qos/rcv_queue (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rcv_queue is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rcv_queue() directly.

    YANG Description: Configure Queue Parameters
    """
    try:
      t = YANGDynClass(v,base=rcv_queue.rcv_queue, is_container='container', yang_name="rcv-queue", rest_name="rcv-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Queue Parameters', u'cli-compact-syntax': None, u'callpoint': u'qos_cos_threshold', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rcv_queue must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=rcv_queue.rcv_queue, is_container='container', yang_name="rcv-queue", rest_name="rcv-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Queue Parameters', u'cli-compact-syntax': None, u'callpoint': u'qos_cos_threshold', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)""",
        })

    self.__rcv_queue = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rcv_queue(self):
    self.__rcv_queue = YANGDynClass(base=rcv_queue.rcv_queue, is_container='container', yang_name="rcv-queue", rest_name="rcv-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Queue Parameters', u'cli-compact-syntax': None, u'callpoint': u'qos_cos_threshold', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)


  def _get_flowcontrol(self):
    """
    Getter method for flowcontrol, mapped from YANG variable /interface/gigabitethernet/qos/flowcontrol (container)
    """
    return self.__flowcontrol
      
  def _set_flowcontrol(self, v, load=False):
    """
    Setter method for flowcontrol, mapped from YANG variable /interface/gigabitethernet/qos/flowcontrol (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_flowcontrol is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_flowcontrol() directly.
    """
    try:
      t = YANGDynClass(v,base=flowcontrol.flowcontrol, is_container='container', yang_name="flowcontrol", rest_name="flowcontrol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IEEE 802.3x Flow Control', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """flowcontrol must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=flowcontrol.flowcontrol, is_container='container', yang_name="flowcontrol", rest_name="flowcontrol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IEEE 802.3x Flow Control', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)""",
        })

    self.__flowcontrol = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_flowcontrol(self):
    self.__flowcontrol = YANGDynClass(base=flowcontrol.flowcontrol, is_container='container', yang_name="flowcontrol", rest_name="flowcontrol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IEEE 802.3x Flow Control', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)

  default_cos = __builtin__.property(_get_default_cos, _set_default_cos)
  trust = __builtin__.property(_get_trust, _set_trust)
  cos_mutation = __builtin__.property(_get_cos_mutation, _set_cos_mutation)
  cos_traffic_class = __builtin__.property(_get_cos_traffic_class, _set_cos_traffic_class)
  dscp_mutation = __builtin__.property(_get_dscp_mutation, _set_dscp_mutation)
  dscp_traffic_class = __builtin__.property(_get_dscp_traffic_class, _set_dscp_traffic_class)
  dscp_cos = __builtin__.property(_get_dscp_cos, _set_dscp_cos)
  random_detect = __builtin__.property(_get_random_detect, _set_random_detect)
  drop_monitor = __builtin__.property(_get_drop_monitor, _set_drop_monitor)
  rcv_queue = __builtin__.property(_get_rcv_queue, _set_rcv_queue)
  flowcontrol = __builtin__.property(_get_flowcontrol, _set_flowcontrol)


  _pyangbind_elements = {'default_cos': default_cos, 'trust': trust, 'cos_mutation': cos_mutation, 'cos_traffic_class': cos_traffic_class, 'dscp_mutation': dscp_mutation, 'dscp_traffic_class': dscp_traffic_class, 'dscp_cos': dscp_cos, 'random_detect': random_detect, 'drop_monitor': drop_monitor, 'rcv_queue': rcv_queue, 'flowcontrol': flowcontrol, }


